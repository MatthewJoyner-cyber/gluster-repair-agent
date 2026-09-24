#!/usr/bin/env python3
# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Run named, bounded checks for a companion candidate tree."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


def root_path(value: str) -> Path:
    root = Path(value).resolve()
    required = ("FILES.txt", "scripts/audit_tree.py", "tests")
    if not root.is_dir() or any(not (root / item).exists() for item in required):
        raise argparse.ArgumentTypeError("root is not a companion candidate")
    return root


def inventory(root: Path) -> int:
    expected = {line.strip() for line in (root / "FILES.txt").read_text().splitlines() if line.strip()}
    actual = {
        path.relative_to(root).as_posix() for path in root.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(root).parts and "__pycache__" not in path.relative_to(root).parts
    }
    if expected == actual:
        print(f"inventory passed: {len(actual)} files")
        return 0
    print("inventory mismatch", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=root_path)
    parser.add_argument("check", choices=("tests", "syntax", "privacy", "inventory"))
    parser.add_argument("--public-identity", action="append", default=[])
    parser.add_argument("--public-copyright-holder", action="append", default=[])
    parser.add_argument("--private-patterns", type=Path,
                        help="external literal-identifier file for the privacy check")
    args = parser.parse_args()
    if args.private_patterns is not None:
        if args.check != "privacy":
            parser.error("--private-patterns is only supported for the privacy check")
        # Resolve against the caller's directory before changing subprocess cwd.
        args.private_patterns = args.private_patterns.resolve()
        if args.private_patterns.is_relative_to(args.root):
            parser.error("private pattern list must be outside the candidate")
        if not args.private_patterns.is_file():
            parser.error("private pattern list must be an existing file")
    if args.check == "inventory":
        return inventory(args.root)
    if args.check == "tests":
        command = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"]
    elif args.check == "syntax":
        command = [sys.executable, "-m", "py_compile", *map(str, sorted((args.root / "scripts").glob("*.py")))]
    else:
        command = [sys.executable, "scripts/audit_tree.py", "."]
        if args.private_patterns is not None:
            command.extend(("--private-patterns", str(args.private_patterns)))
        for identity in args.public_identity:
            command.extend(("--public-identity", identity))
        for holder in args.public_copyright_holder:
            command.extend(("--public-copyright-holder", holder))
    return subprocess.run(command, cwd=args.root, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
