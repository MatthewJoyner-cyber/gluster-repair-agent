# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Tests for the portable named candidate checks."""
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
import shutil
import subprocess
import sys
from contextlib import redirect_stderr, redirect_stdout

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_candidate", BASE / "scripts" / "check_candidate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CandidateCheckTests(unittest.TestCase):
    def privacy_fixture(self, base):
        root = base / "candidate"
        (root / "scripts").mkdir(parents=True)
        (root / "tests").mkdir()
        (root / "FILES.txt").write_text("FILES.txt\n")
        shutil.copy2(BASE / "scripts/audit_tree.py", root / "scripts/audit_tree.py")
        (root / "sample.txt").write_text("synthetic-private-marker\n")
        return root

    def run_check(self, cwd, root, *arguments):
        return subprocess.run(
            [sys.executable, "-B", str(BASE / "scripts/check_candidate.py"),
             "--root", str(root), *arguments], cwd=cwd, capture_output=True, text=True,
        )

    def test_privacy_uses_external_pattern_relative_to_caller_without_echo(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = self.privacy_fixture(base)
            patterns = base / "identifiers.txt"
            patterns.write_text("synthetic-private-marker\n")
            baseline = self.run_check(base, root, "privacy")
            self.assertEqual(0, baseline.returncode, baseline.stderr)
            result = self.run_check(base, root, "privacy", "--private-patterns", patterns.name)
            self.assertEqual(1, result.returncode, result.stderr)
            self.assertIn('"kind": "private-identifier"', result.stdout)
            self.assertIn('"file": "sample.txt"', result.stdout)
            self.assertNotIn("synthetic-private-marker", result.stdout + result.stderr)

    def test_privacy_refuses_internal_pattern_file_and_external_symlink_to_it(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = self.privacy_fixture(base)
            internal = root / "identifiers.txt"
            internal.write_text("synthetic-private-marker\n")
            link = base / "external.txt"
            link.symlink_to(internal)
            for path in (internal, link):
                with self.subTest(path=path.name):
                    result = self.run_check(base, root, "privacy", "--private-patterns", str(path))
                    self.assertEqual(2, result.returncode)
                    self.assertIn("outside the candidate", result.stderr)
                    self.assertNotIn("synthetic-private-marker", result.stdout + result.stderr)

    def test_pattern_option_cannot_be_silently_ignored(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = self.privacy_fixture(base)
            for check in ("tests", "syntax", "inventory", "privacy"):
                with self.subTest(check=check):
                    result = self.run_check(base, root, check, "--private-patterns", "missing.txt")
                    self.assertEqual(2, result.returncode)
                    self.assertIn("existing file" if check == "privacy" else "only supported", result.stderr)

    def test_inventory_accepts_exact_file_list(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "FILES.txt").write_text("FILES.txt\nitem.txt\n")
            (root / "item.txt").write_text("ok\n")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(0, module.inventory(root))

    def test_inventory_rejects_unlisted_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "FILES.txt").write_text("FILES.txt\n")
            (root / "unlisted.txt").write_text("no\n")
            with redirect_stderr(io.StringIO()):
                self.assertEqual(1, module.inventory(root))
