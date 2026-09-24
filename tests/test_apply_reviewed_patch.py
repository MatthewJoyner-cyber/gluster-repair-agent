# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Patch-header safety tests for the portable reviewed-patch helper."""
import importlib.util
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("apply_reviewed_patch", BASE / "scripts" / "apply_reviewed_patch.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReviewedPatchTests(unittest.TestCase):
    def test_accepts_normal_git_paths(self):
        text = "--- a/docs/guide.md\n+++ b/docs/guide.md\n"
        self.assertEqual(["docs/guide.md"], module.paths_from_patch(text))

    def test_rejects_metadata_and_parent_escape(self):
        for path in ("a/../secret", "b/.git/config", "/etc/passwd"):
            with self.assertRaises(ValueError):
                module.paths_from_patch(f"--- {path}\n+++ {path}\n")
