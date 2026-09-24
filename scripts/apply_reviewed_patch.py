#!/usr/bin/env python3
# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Check or apply one reviewed patch below one explicitly selected Git root."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


def git_root(value: str) -> Path:
    root = Path(value).resolve()
    probe = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True, capture_output=True)
    if probe.returncode or not root.is_dir():
        raise argparse.ArgumentTypeError("root must be an existing Git work tree")
    return Path(probe.stdout.strip())


def patch_path(value: str) -> Path:
    patch = Path(value).resolve()
    if not patch.is_file() or patch.stat().st_size > 2 * 1024 * 1024:
        raise argparse.ArgumentTypeError("patch must be a regular file no larger than 2 MiB")
    return patch


def paths_from_patch(text: str) -> list[str]:
    paths: list[str] = []
    for line in text.splitlines():
        if not (line.startswith("--- ") or line.startswith("+++ ")):
            continue
        value = line[4:].split("\t", 1)[0]
        if value == "/dev/null":
            continue
        if value.startswith(("a/", "b/")):
            value = value[2:]
        candidate = Path(value)
        if candidate.is_absolute() or ".." in candidate.parts or ".git" in candidate.parts:
            raise ValueError(f"unsafe patch path: {value}")
        paths.append(value)
    if not paths:
        raise ValueError("patch has no file headers")
    return sorted(set(paths))


def run(root: Path, patch: Path, apply: bool) -> int:
    try:
        paths = paths_from_patch(patch.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        print(f"apply-reviewed-patch: {exc}", file=sys.stderr)
        return 2
    print("reviewed paths:")
    print("\n".join(paths))
    check = subprocess.run(["git", "-C", str(root), "apply", "--check", "--whitespace=error-all", str(patch)])
    if check.returncode:
        return check.returncode
    print("patch check passed")
    if not apply:
        return 0
    return subprocess.run(["git", "-C", str(root), "apply", "--whitespace=error-all", str(patch)]).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=git_root)
    parser.add_argument("--patch", required=True, type=patch_path)
    parser.add_argument("operation", choices=("check", "apply"))
    args = parser.parse_args()
    return run(args.root, args.patch, args.operation == "apply")


if __name__ == "__main__":
    raise SystemExit(main())
