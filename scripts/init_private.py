#!/usr/bin/env python3
# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Create blank private steering and ledger files; never overwrite existing data."""
from __future__ import annotations
import os
from pathlib import Path

def initialize(home: Path, root: Path, templates: Path) -> list[str]:
    home = home.resolve()
    if not root.is_absolute() or not root.is_relative_to(home):
        raise ValueError("private root must be an absolute path under the user's home")
    # Reject existing symlinks rather than following them into a repository.
    for component in [root, *root.parents]:
        if component.is_symlink():
            raise ValueError("private root must not traverse a symlink")
    if root.is_relative_to(templates.parent.resolve()):
        raise ValueError("private files must remain outside the companion")
    for component in [root, *root.parents]:
        marker = component / ".git"
        if marker.is_file() or marker.is_symlink() or (marker / "HEAD").is_file():
            raise ValueError("private files must remain outside repositories")
    old_umask = os.umask(0o077)
    created = []
    try:
        root.mkdir(parents=True, exist_ok=True, mode=0o700)
        root.chmod(0o700)
        for folder, source in [("steering", "private-steering"), ("ledger", "private-ledger")]:
            target = root / folder
            if target.is_symlink():
                raise ValueError("private subdirectory must not be a symlink")
            target.mkdir(exist_ok=True, mode=0o700)
            target.chmod(0o700)
            for template in sorted((templates / source).glob("*.md")):
                destination = target / template.name
                if destination.is_symlink():
                    raise ValueError("private document must not be a symlink")
                try:
                    with destination.open("x", encoding="utf-8") as stream:
                        stream.write(template.read_text())
                    created.append(str(destination.relative_to(root)))
                except FileExistsError:
                    pass
        return created
    finally:
        os.umask(old_umask)

def main() -> int:
    home = Path.home().resolve()
    root = Path(os.environ.get("GLUSTER_REPAIR_PRIVATE_ROOT") or home / ".gluster-repair-private")
    templates = Path(__file__).resolve().parents[1] / "templates"
    try:
        created = initialize(home, root, templates)
    except (ValueError, OSError) as exc:
        print("Private initialization refused:", exc)
        return 2
    print("Created", len(created), "private documents; existing files preserved.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
