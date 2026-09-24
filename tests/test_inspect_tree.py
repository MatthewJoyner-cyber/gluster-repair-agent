# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Tests for the portable read-only tree inspector."""
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("inspect_tree", BASE / "scripts" / "inspect_tree.py")
inspect_tree = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inspect_tree)


class InspectTreeTests(unittest.TestCase):
    def test_search_is_bounded_and_skips_internal_directories(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "visible.txt").write_text("first\nneedle one\nneedle two\n")
            (root / ".git").mkdir()
            (root / ".git" / "hidden.txt").write_text("needle hidden\n")
            self.assertEqual(["visible.txt:2:needle one"], inspect_tree.bounded_search(root, "needle", None, 1))

    def test_file_window_rejects_escape_and_bounds_range(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "notes.txt").write_text("zero\none\ntwo\n")
            self.assertEqual(["     2\tone"], inspect_tree.bounded_file(root, "notes.txt", 2, 2, True))
            with self.assertRaises(ValueError):
                inspect_tree.bounded_file(root, "../outside", 1, 1, False)
            with self.assertRaises(ValueError):
                inspect_tree.bounded_file(root, "notes.txt", 1, 900, False)

    def test_git_operations_refuse_a_non_git_root(self):
        with tempfile.TemporaryDirectory() as temp:
            with redirect_stderr(io.StringIO()):
                self.assertEqual(2, inspect_tree.git_command(Path(temp), ["status", "--short"]))


if __name__ == "__main__":
    unittest.main()
