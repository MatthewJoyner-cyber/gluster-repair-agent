# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Privacy boundary checks use only disposable, synthetic files."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
def module(name):
    spec = importlib.util.spec_from_file_location(name, BASE / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result
audit = module("audit_tree")
init = module("init_private")

class PrivacyTests(unittest.TestCase):
    def test_scans_comments_and_ledgers_without_echoing_matches(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "code.py").write_text("# private-node-secret\n")
            (root / "notes.md").write_text("private-node-secret\n")
            result = audit.scan(root, ["private-node-secret"], set())
            self.assertEqual(2, len(result))
            self.assertNotIn("private-node-secret", str(result))

    def test_approved_contact_is_scoped_to_maintainer_document(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            address = "maintainer" + "@" + "example.invalid"
            (root / "MAINTAINERS.md").write_text(address)
            (root / "code.py").write_text("# " + address)
            result = audit.scan(root, [], {address})
            self.assertEqual(["code.py"], [row["file"] for row in result])

    def test_approved_alias_does_not_allow_private_identity_in_code(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "MAINTAINERS.md").write_text("Alias: ExampleAlias")
            (root / "code.py").write_text("# ExampleAlias")
            result = audit.scan(root, ["ExampleAlias"], {"ExampleAlias"})
            self.assertEqual(["code.py"], [row["file"] for row in result])

    def test_approved_copyright_holder_is_scoped_to_exact_notice(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            holder = "Example Author"
            (root / "code.py").write_text(
                "# Copyright 2026 Example Author\n# Example Author\n"
            )
            result = audit.scan(root, [holder], set(), {holder})
            self.assertEqual(["code.py"], [row["file"] for row in result])
            self.assertEqual(2, result[0]["line"])

    def test_rejects_symlink_and_binary(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "data.bin").write_bytes(bytes([255, 254]))
            (root / "link").symlink_to("/nonexistent-example")
            self.assertEqual({"symlink", "unreviewed-binary-or-unreadable"}, {x["kind"] for x in audit.scan(root, [], set())})

    def test_private_init_is_non_destructive_and_private(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            root = home / ".private"
            created = init.initialize(home, root, BASE / "templates")
            self.assertEqual(5, len(created))
            self.assertTrue((root / "ledger/RUNS.md").is_file())
            self.assertTrue((root / "steering/REMOTE_OPERATION.md").is_file())
            marker = root / "ledger/LEDGER.md"
            marker.write_text("existing personal note")
            self.assertEqual([], init.initialize(home, root, BASE / "templates"))
            self.assertEqual("existing personal note", marker.read_text())
            self.assertEqual(0o700, root.stat().st_mode & 0o777)
            self.assertEqual(0o600, marker.stat().st_mode & 0o777)

    def test_private_init_refuses_repository_and_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            repo = home / "repo"
            (repo / ".git").mkdir(parents=True)
            (repo / ".git/HEAD").write_text("ref: refs/heads/main\n")
            with self.assertRaises(ValueError):
                init.initialize(home, repo / "private", BASE / "templates")
            (home / "link").symlink_to(repo, target_is_directory=True)
            with self.assertRaises(ValueError):
                init.initialize(home, home / "link/private", BASE / "templates")

if __name__ == "__main__":
    unittest.main()
