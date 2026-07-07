#!/usr/bin/env python3
from pathlib import Path
import importlib.util as _ilu
import json
import re
import sys
import tomllib


def _load_advisor_source_codex() -> dict:
    spec = _ilu.spec_from_file_location("gen_agents", root / "scripts" / "generate-agents.py")
    gen = _ilu.module_from_spec(spec)
    spec.loader.exec_module(gen)
    return gen.parse_agent(root / "agents-src" / "advisor-consultant.yaml")["codex"]

root = Path(__file__).resolve().parents[1]
errors = []

manifest = root / ".codex-plugin" / "plugin.json"
if not manifest.exists():
    errors.append("missing .codex-plugin/plugin.json")
else:
    data = json.loads(manifest.read_text())
    for key in ["name", "version", "description", "skills"]:
        if key not in data:
            errors.append(f"manifest missing {key}")
    if data.get("skills") != "./skills/":
        errors.append('manifest skills should be "./skills/"')

skill = root / "skills" / "engineering-team" / "SKILL.md"
if not skill.exists():
    errors.append("missing skills/engineering-team/SKILL.md")
else:
    text = skill.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        errors.append("SKILL.md missing YAML-style frontmatter")
    else:
        fm = m.group(1)
        if "name: engineering-team" not in fm:
            errors.append("SKILL.md missing name: engineering-team")
        if "description:" not in fm:
            errors.append("SKILL.md missing description")
    for forbidden in ["$ARGUMENTS", "disable-model-invocation", ".claude-plugin"]:
        if forbidden in text:
            errors.append(f"SKILL.md contains Claude-specific token: {forbidden}")

agent_dirs = [
    root / ".codex" / "agents",
    root / "skills" / "engineering-team" / "assets" / "agents",
]

for agent_dir in agent_dirs:
    if not agent_dir.exists():
        errors.append(f"missing agent directory: {agent_dir}")
        continue
    for p in sorted(agent_dir.glob("*.toml")):
        data = tomllib.loads(p.read_text())
        for key in ["name", "description", "developer_instructions"]:
            if key not in data:
                errors.append(f"{p} missing {key}")

advisor = root / ".codex" / "agents" / "advisor_consultant.toml"
if not advisor.exists():
    errors.append("missing .codex/agents/advisor_consultant.toml")
else:
    data = tomllib.loads(advisor.read_text())
    advisor_yaml = root / "agents-src" / "advisor-consultant.yaml"
    if not advisor_yaml.exists():
        errors.append("missing agents-src/advisor-consultant.yaml (needed to validate advisor_consultant model fields)")
    else:
        src = _load_advisor_source_codex()
        expected_model = src.get("model")
        expected_effort = src.get("model_reasoning_effort", "high")
        expected_sandbox = src.get("sandbox_mode", "read-only")
        if data.get("model") != expected_model:
            errors.append(f"advisor_consultant model should be {expected_model!r} (from agents-src/advisor-consultant.yaml)")
        if data.get("model_reasoning_effort") != expected_effort:
            errors.append(f"advisor_consultant model_reasoning_effort should be {expected_effort!r}")
        if data.get("sandbox_mode") != expected_sandbox:
            errors.append(f"advisor_consultant sandbox_mode should be {expected_sandbox!r}")

# "Advisor Consultant" must anchor in the SKILL.md entrypoint.
if skill.exists():
    text = skill.read_text()
    if "Advisor Consultant" not in text:
        errors.append("SKILL.md missing required anchor: Advisor Consultant")

# Detailed advisor contract lives in references/advisor-gate.md.
advisor_gate = root / "skills" / "engineering-team" / "references" / "advisor-gate.md"
if not advisor_gate.exists():
    errors.append("missing references/advisor-gate.md")
else:
    gate_text = advisor_gate.read_text()
    for required in [
        "## Decision Needed",
        "## Go / No-Go",
        "## Advisor Decision Receipt",
    ]:
        if required not in gate_text:
            errors.append(f"references/advisor-gate.md missing advisor contract text: {required}")

# Context budget policy lives in references/agent-routing.md.
agent_routing = root / "skills" / "engineering-team" / "references" / "agent-routing.md"
if not agent_routing.exists():
    errors.append("missing references/agent-routing.md")
else:
    routing_text = agent_routing.read_text()
    if "Default Advisor Consultant to `brief-only`" not in routing_text:
        errors.append("references/agent-routing.md missing context budget policy")
    if "## Mandatory subagent routing" not in routing_text:
        errors.append("references/agent-routing.md missing mandatory subagent routing policy")
    if "Fallback is only for harnesses without subagent support" not in routing_text:
        errors.append("references/agent-routing.md missing limited fallback policy")

codex_compat = root / "skills" / "engineering-team" / "references" / "codex-compatibility.md"
if not codex_compat.exists():
    errors.append("missing references/codex-compatibility.md")
else:
    compat_text = codex_compat.read_text()
    if "must route through subagents" not in compat_text:
        errors.append("references/codex-compatibility.md missing mandatory Codex subagent routing")
    forbidden_codex_phrases = [
        "only spawns subagents when explicitly asked",
        "Single-session mode",
        "when explicitly requested",
    ]
    for phrase in forbidden_codex_phrases:
        if phrase in compat_text:
            errors.append(f"references/codex-compatibility.md contains stale optional-routing phrase: {phrase}")

if not (root / "AGENTS.md").exists():
    errors.append("missing AGENTS.md")

if errors:
    print("Codex package validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Codex package validation passed.")
