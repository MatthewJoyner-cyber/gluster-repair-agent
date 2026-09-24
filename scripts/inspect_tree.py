#!/usr/bin/env python3
# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Run bounded, read-only inspection operations below one selected Git tree."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_GIT_LINES = 500


def root_path(value: str) -> Path:
    root = Path(value).resolve()
    if not root.is_dir():
        raise argparse.ArgumentTypeError("root must be an existing directory")
    return root


def relative_path(root: Path, value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError("path must be relative and must not contain '..'")
    resolved = (root / candidate).resolve()
    if resolved != root and root not in resolved.parents:
        raise ValueError("path escapes the selected root")
    if not resolved.exists():
        raise ValueError("path does not exist below the selected root")
    return resolved


def bounded_search(root: Path, pattern: str, path: str | None, maximum: int) -> list[str]:
    start = relative_path(root, path) if path else root
    files = [start] if start.is_file() else sorted(item for item in start.rglob("*") if item.is_file())
    matches: list[str] = []
    for item in files:
        relative = item.relative_to(root)
        if any(part in SKIP_PARTS for part in relative.parts) or item.stat().st_size > MAX_FILE_BYTES:
            continue
        try:
            lines = item.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, 1):
            if pattern in line:
                matches.append(f"{relative}:{number}:{line}")
                if len(matches) >= maximum:
                    return matches
    return matches


def bounded_file(root: Path, path: str, first: int, last: int, numbered: bool) -> list[str]:
    if first < 1 or last < first or last - first > 800:
        raise ValueError("line range must be 1-801 lines with a positive start")
    target = relative_path(root, path)
    if not target.is_file() or target.stat().st_size > MAX_FILE_BYTES:
        raise ValueError("path must be a text file no larger than 2 MiB")
    try:
        lines = target.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise ValueError("path is not UTF-8 text") from exc
    window = lines[first - 1:last]
    if numbered:
        return [f"{number:6d}\t{line}" for number, line in enumerate(window, first)]
    return window


def git_command(root: Path, arguments: list[str]) -> int:
    probe = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if probe.returncode != 0 or probe.stdout.strip() != "true":
        print("inspect-tree: selected root is not a Git work tree", file=sys.stderr)
        return 2
    result = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for stream, target in ((result.stdout, sys.stdout), (result.stderr, sys.stderr)):
        lines = stream.splitlines()
        print("\n".join(lines[:MAX_GIT_LINES]), file=target)
        if len(lines) > MAX_GIT_LINES:
            print(f"inspect-tree: output truncated after {MAX_GIT_LINES} lines", file=target)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=root_path, help="Git tree to inspect")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("status", help="show Git short status")
    diff = commands.add_parser("diff", help="run one bounded Git diff check")
    diff.add_argument("--check", action="store_true", help="check whitespace")
    diff.add_argument("--stat", action="store_true", help="show summary only")
    search = commands.add_parser("search", help="literal text search below the selected root")
    search.add_argument("pattern")
    search.add_argument("--path", help="relative file or directory")
    search.add_argument("--max", dest="maximum", type=int, default=200)
    file_view = commands.add_parser("file", help="show a bounded UTF-8 file window")
    file_view.add_argument("path")
    file_view.add_argument("--from", dest="first", type=int, default=1)
    file_view.add_argument("--to", dest="last", type=int, default=240)
    file_view.add_argument("--no-number", dest="numbered", action="store_false")
    file_view.set_defaults(numbered=True)
    args = parser.parse_args()
    if args.command == "status":
        return git_command(args.root, ["status", "--short"])
    if args.command == "diff":
        if args.check == args.stat:
            parser.error("diff requires exactly one of --check or --stat")
        return git_command(args.root, ["diff", "--check" if args.check else "--stat"])
    try:
        if args.command == "search":
            if args.maximum < 1 or args.maximum > 5000:
                raise ValueError("--max must be between 1 and 5000")
            print("\n".join(bounded_search(args.root, args.pattern, args.path, args.maximum)))
        else:
            print("\n".join(bounded_file(args.root, args.path, args.first, args.last, args.numbered)))
    except ValueError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
