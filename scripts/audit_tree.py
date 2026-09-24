#!/usr/bin/env python3
# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Read-only release-tree scan. Reports locations, never matched private values."""
from __future__ import annotations
import argparse
import ipaddress
import json
from pathlib import Path
import re

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
EMAIL = re.compile(r"[A-Za-z0-9_.+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
IPV4 = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")
KEY = re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")
HOME = re.compile(r"/(?:home|Users|ghome)/[A-Za-z0-9_.-]+")
COPYRIGHT = re.compile(r"^# Copyright (?:[0-9]{4}(?:-[0-9]{4})? )?(.+)$")
DOCUMENTATION_NETS = [ipaddress.ip_network(x) for x in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")]

def scan(
    root: Path,
    patterns: list[str],
    contacts: set[str],
    copyright_holders: set[str] | None = None,
) -> list[dict]:
    copyright_holders = copyright_holders or set()
    findings = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_symlink():
            findings.append({"file": str(rel), "line": 0, "kind": "symlink"})
            continue
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.is_dir():
            if path.name in {"private", ".gluster-repair-private"}:
                findings.append({"file": str(rel), "line": 0, "kind": "private-directory"})
            continue
        if path.name.startswith(".env") or path.suffix in {".pem", ".key"}:
            findings.append({"file": str(rel), "line": 0, "kind": "credential-file"})
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            findings.append({"file": str(rel), "line": 0, "kind": "unreviewed-binary-or-unreadable"})
            continue
        for number, line in enumerate(text.splitlines(), 1):
            kinds = set()
            private_line = line
            if rel.as_posix() == "MAINTAINERS.md":
                for identity in sorted(contacts, key=len, reverse=True):
                    private_line = private_line.replace(identity, "")
            copyright_match = COPYRIGHT.fullmatch(line)
            if copyright_match and copyright_match.group(1) in copyright_holders:
                private_line = private_line.replace(copyright_match.group(1), "")
            if any(item.casefold() in private_line.casefold() for item in patterns):
                kinds.add("private-identifier")
            if KEY.search(line):
                kinds.add("private-key")
            if HOME.search(line):
                kinds.add("literal-user-home")
            for match in EMAIL.finditer(line):
                # License text is retained; only explicitly approved contacts may
                # otherwise occur, and only in the maintainer profile document.
                if rel.as_posix() != "COPYING" and not (
                    rel.as_posix() == "MAINTAINERS.md" and match.group() in contacts
                ):
                    kinds.add("contact-review")
            for match in IPV4.finditer(line):
                try:
                    addr = ipaddress.ip_address(match.group())
                except ValueError:
                    continue
                if not addr.is_loopback and not addr.is_unspecified and not any(addr in net for net in DOCUMENTATION_NETS):
                    kinds.add("network-identifier")
            for kind in sorted(kinds):
                findings.append({"file": str(rel), "line": number, "kind": kind})
    return findings

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--private-patterns", type=Path, help="external file, one literal private identifier per line")
    parser.add_argument("--public-identity", "--public-contact", dest="public_contact", action="append", default=[], help="explicitly approved alias/name/contact/URL, allowed only in MAINTAINERS.md")
    parser.add_argument("--public-copyright-holder", action="append", default=[], help="explicitly approved copyright holder, allowed only in an exact source copyright notice")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error("root must be a directory")
    patterns = []
    if args.private_patterns:
        pattern_path = args.private_patterns.resolve()
        if pattern_path.is_relative_to(root):
            parser.error("private pattern list must be outside the candidate")
        patterns = [line.strip() for line in pattern_path.read_text().splitlines() if line.strip()]
    findings = scan(root, patterns, set(args.public_contact), set(args.public_copyright_holder))
    print(json.dumps({"findings": findings, "count": len(findings)}, indent=2))
    return 1 if findings else 0

if __name__ == "__main__":
    raise SystemExit(main())
