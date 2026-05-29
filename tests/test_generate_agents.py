"""Unit tests for scripts/generate-agents.py.

The generator is the single source-of-truth pipeline for every harness, so it
gets direct coverage: parser, schema validation, the three renderers, the
generated banner, and the no-drift round trip. Stdlib only (no third-party deps).
"""

from __future__ import annotations

import importlib.util
import tempfile
import tomllib
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "gen_agents", REPO_ROOT / "scripts" / "generate-agents.py"
)
gen = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(gen)


def base_agent() -> dict:
    return {
        "name": "sample-agent",
        "description": "Sample agent for tests.",
        "claude": {"tools": "Read", "model": "sonnet", "color": "blue"},
        "codex": {
            "model": None,
            "model_reasoning_effort": "high",
            "sandbox_mode": "read-only",
            "nickname_candidates": ["Sample"],
        },
        "instructions": "Do the thing.\n",
    }


SAMPLE_SOURCE = Path("agents-src/sample-agent.yaml")


class ParseScalarTest(unittest.TestCase):
    def test_null(self):
        self.assertIsNone(gen.parse_scalar("null"))

    def test_quoted_with_escapes(self):
        self.assertEqual(gen.parse_scalar('"a\\"b"'), 'a"b')

    def test_plain(self):
        self.assertEqual(gen.parse_scalar("plain"), "plain")


class CodexNameTest(unittest.TestCase):
    def test_hyphens_become_underscores(self):
        self.assertEqual(gen.codex_name("a-b-c"), "a_b_c")


class ParseAgentTest(unittest.TestCase):
    def test_parses_valid_source(self):
        yaml = (
            "name: sample-agent\n"
            'description: "Sample agent for tests."\n'
            "claude:\n"
            '  tools: "Read"\n'
            '  model: "sonnet"\n'
            '  color: "blue"\n'
            "codex:\n"
            "  model: null\n"
            '  model_reasoning_effort: "high"\n'
            '  sandbox_mode: "read-only"\n'
            "  nickname_candidates:\n"
            '    - "Sample"\n'
            "instructions: |\n"
            "  Do the thing.\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample-agent.yaml"
            path.write_text(yaml)
            agent = gen.parse_agent(path)
            gen.validate_agent(agent, path)
        self.assertEqual(agent["name"], "sample-agent")
        self.assertEqual(agent["claude"]["model"], "sonnet")
        self.assertIsNone(agent["codex"]["model"])
        self.assertEqual(agent["codex"]["nickname_candidates"], ["Sample"])
        self.assertTrue(agent["instructions"].startswith("Do the thing."))


class ValidateAgentTest(unittest.TestCase):
    def test_valid_passes(self):
        gen.validate_agent(base_agent(), SAMPLE_SOURCE)

    def test_name_must_match_filename(self):
        agent = base_agent()
        agent["name"] = "other-name"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)

    def test_unknown_top_level_key(self):
        agent = base_agent()
        agent["bogus"] = "x"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)

    def test_unknown_claude_key(self):
        agent = base_agent()
        agent["claude"]["bogus"] = "x"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)

    def test_unknown_codex_key(self):
        agent = base_agent()
        agent["codex"]["bogus"] = "x"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)

    def test_bad_reasoning_effort(self):
        agent = base_agent()
        agent["codex"]["model_reasoning_effort"] = "ultra"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)

    def test_bad_sandbox_mode(self):
        agent = base_agent()
        agent["codex"]["sandbox_mode"] = "full-access"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)

    def test_nicknames_must_be_list(self):
        agent = base_agent()
        agent["codex"]["nickname_candidates"] = "Sample"
        with self.assertRaises(ValueError):
            gen.validate_agent(agent, SAMPLE_SOURCE)


class RenderMarkdownTest(unittest.TestCase):
    def test_contains_frontmatter_banner_and_body(self):
        out = gen.render_markdown(base_agent())
        self.assertIn("name: sample-agent", out)
        self.assertIn("model: sonnet", out)
        self.assertIn("GENERATED FILE - DO NOT EDIT", out)
        self.assertIn("Do the thing.", out)
        self.assertTrue(out.startswith("---\n"))


class RenderTomlTest(unittest.TestCase):
    def test_banner_underscore_name_and_valid_toml(self):
        out = gen.render_toml(base_agent())
        self.assertTrue(out.startswith("# GENERATED FILE - DO NOT EDIT"))
        self.assertIn('name = "sample_agent"', out)
        self.assertNotIn("model =", out)  # model is null -> omitted
        self.assertIn('sandbox_mode = "read-only"', out)
        parsed = tomllib.loads(out)
        self.assertEqual(parsed["name"], "sample_agent")
        self.assertIn("developer_instructions", parsed)

    def test_model_emitted_when_present(self):
        agent = base_agent()
        agent["codex"]["model"] = "gpt-5.5"
        out = gen.render_toml(agent)
        self.assertIn('model = "gpt-5.5"', out)


class RenderGithubMarkdownTest(unittest.TestCase):
    def test_read_only_boundary(self):
        out = gen.render_github_markdown(base_agent())
        self.assertIn("Read-only. Do not edit files.", out)
        self.assertIn("GENERATED FILE - DO NOT EDIT", out)

    def test_workspace_write_boundary(self):
        agent = base_agent()
        agent["codex"]["sandbox_mode"] = "workspace-write"
        out = gen.render_github_markdown(agent)
        self.assertIn("May edit files", out)


class NoDriftRoundTripTest(unittest.TestCase):
    def test_check_reports_clean_tree(self):
        self.assertEqual(gen.check(), 0)

    def test_every_output_path_matches_disk(self):
        for agent in gen.load_agents():
            for path, content in gen.output_paths(agent):
                self.assertTrue(path.exists(), f"missing generated file: {path}")
                self.assertEqual(
                    path.read_text(), content, f"stale generated file: {path}"
                )


if __name__ == "__main__":
    unittest.main()
