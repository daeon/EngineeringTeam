"""Contract tests for EngineeringTeam subagent routing language."""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class SubagentRoutingContractTest(unittest.TestCase):
    def test_codex_compatibility_requires_subagent_routing_when_available(self):
        text = (
            REPO_ROOT
            / "skills"
            / "engineering-team"
            / "references"
            / "codex-compatibility.md"
        ).read_text()

        self.assertIn("must route through subagents", text)
        self.assertIn("fallback", text)
        self.assertNotIn("only spawns subagents when explicitly asked", text)
        self.assertNotIn("Single-session mode", text)
        self.assertNotIn("when explicitly requested", text)

    def test_agent_routing_has_mandatory_team_creation_policy(self):
        text = (
            REPO_ROOT
            / "skills"
            / "engineering-team"
            / "references"
            / "agent-routing.md"
        ).read_text()

        self.assertIn("## Mandatory subagent routing", text)
        self.assertIn("spawn the selected specialists", text)
        self.assertIn("Fallback is only for harnesses without subagent support", text)
        self.assertNotIn("not warranted", text)
        self.assertNotIn("not worth the overhead", text)


if __name__ == "__main__":
    unittest.main()
