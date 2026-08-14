"""Architecture contracts for the consolidated EngineeringTeam skill."""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class SingleSkillContractTest(unittest.TestCase):
    def test_exactly_one_discoverable_skill(self):
        paths = sorted(
            path.relative_to(REPO_ROOT).as_posix()
            for path in (REPO_ROOT / "skills").rglob("SKILL.md")
        )
        self.assertEqual(paths, ["skills/engineering-team/SKILL.md"])
        self.assertEqual(
            sorted(path.name for path in (REPO_ROOT / "skills").iterdir()),
            ["engineering-team"],
        )

    def test_route_references_preserve_distinct_authority(self):
        references = REPO_ROOT / "skills" / "engineering-team" / "references"
        read_only_routes = [
            "route-codebase-analysis.md",
            "route-debugging.md",
            "route-log-analysis.md",
            "route-performance.md",
        ]
        for name in read_only_routes:
            text = (references / name).read_text()
            self.assertIn("## Authority", text)
            self.assertIn("Remain read-only", text)
            self.assertIn("## Output", text)

        handoff = (references / "route-handoff.md").read_text()
        self.assertIn("only the requested continuation artifact", handoff)
        self.assertIn("templates/handoff.md", handoff)

    def test_lead_is_not_spawnable(self):
        forbidden = [
            "agents-src/lead-engineer.yaml",
            "agents/lead-engineer.md",
            ".codex/agents/lead_engineer.toml",
            ".github/agents/lead-engineer.md",
            "skills/engineering-team/assets/agents/lead_engineer.toml",
        ]
        for relative in forbidden:
            self.assertFalse((REPO_ROOT / relative).exists(), relative)

    def test_skill_core_stays_compact(self):
        skill = (REPO_ROOT / "skills" / "engineering-team" / "SKILL.md").read_text()
        body = skill.split("---", 2)[-1]
        self.assertLessEqual(len(body.split()), 900)

    def test_pre_gate_artifacts_do_not_grant_implementation_authority(self):
        skill = (REPO_ROOT / "skills" / "engineering-team" / "SKILL.md").read_text()
        gate = (
            REPO_ROOT
            / "skills"
            / "engineering-team"
            / "references"
            / "implementation-gate.md"
        ).read_text()
        self.assertIn("Pre-gate workflow artifacts", skill)
        self.assertIn("they are evidence, not implementation authority", gate)
        self.assertIn("require explicit user authority", skill)

    def test_fast_path_and_read_only_diagnostics_are_consistent(self):
        skill = (REPO_ROOT / "skills" / "engineering-team" / "SKILL.md").read_text()
        diagnosis = (
            REPO_ROOT
            / "skills"
            / "engineering-team"
            / "references"
            / "diagnosis-loop.md"
        ).read_text()
        self.assertIn("typo/formatting-only edit", skill)
        self.assertIn("sole exception to specialist routing, not to the Implementation Gate", skill)
        self.assertIn("output a compact Implementation Gate", skill)
        self.assertIn("In read-only mode, use existing commands/tests", diagnosis)
        self.assertIn("applies only after the user authorizes Implementation mode", diagnosis)


if __name__ == "__main__":
    unittest.main()
