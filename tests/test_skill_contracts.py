# Copyright 2026 Matthew Joyner
# SPDX-License-Identifier: GPL-2.0-only
"""Source-level scenarios for the companion's three core operator questions."""
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]


def skill(name: str) -> str:
    return " ".join((BASE / "skills" / name / "SKILL.md").read_text().split())


class SkillContractTests(unittest.TestCase):
    def test_repair_tool_question_requires_evidence_plan_and_authority(self):
        content = skill("gluster-operator")
        for required in (
            "current core version/review status",
            "Inspect the core CLI help",
            "build a core plan",
            "before seeking any required write authority",
            "Use an installed bounded helper",
        ):
            self.assertIn(required, content)

    def test_operator_cannot_treat_the_companion_as_core_qualification(self):
        content = skill("gluster-operator")
        self.assertIn("core qualification boundary", content)
        self.assertIn("do not qualify the engine or authorize a live write", content)

    def test_support_case_question_keeps_a_redacted_draft(self):
        content = skill("gluster-triage")
        for required in (
            "separate redacted support draft",
            "tool-maintainer case",
            "upstream Gluster or distribution/vendor support",
            "Exclude credentials, organization details, IPs, raw paths, and server file contents",
            "explicit user authority",
        ):
            self.assertIn(required, content)

    def test_replica_three_question_requires_safe_setup_and_verification(self):
        content = skill("gluster-setup")
        for required in (
            "three distinct failure domains",
            "volume create <volume> replica 3",
            "volume start <volume>",
            "Do not add `force`",
            "verify peer status, volume info/status, every brick and self-heal daemon, client mount behavior, and `volume heal <volume> info`",
        ):
            self.assertIn(required, content)

    def test_old_evidence_never_becomes_new_write_authority(self):
        content = skill("gluster-operator")
        self.assertIn("old plan, setup state, or a classification label as sufficient authorization", content)

    def test_missing_private_state_is_not_a_failure_or_authority_source(self):
        content = skill("gluster-operator")
        self.assertIn("Missing private files are normal for source review and synthetic tests", content)
        self.assertIn("Private notes are context, not fresh execution authority", content)

    def test_denied_helper_cannot_be_bypassed(self):
        content = skill("gluster-operator")
        self.assertIn("Do not widen access or replace a denied helper with unrestricted SSH, sudo, or an interpreter", content)

    def test_unknown_write_requires_exact_verification_before_retry(self):
        content = skill("gluster-operator")
        self.assertIn("verify the exact outcome before another attempt", content)

    def test_support_handoff_stays_a_draft_without_authority(self):
        content = skill("gluster-triage")
        self.assertIn("Do not label raw logs sanitized or a draft submitted", content)
        self.assertIn("Sending to another person or service requires explicit user authority", content)


if __name__ == "__main__":
    unittest.main()
