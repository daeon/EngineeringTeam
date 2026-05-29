#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import tomllib

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
    root / "skills" / "engineering-team" / "references" / "codex-custom-agents",
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
    if data.get("model") != "gpt-5.5":
        errors.append("advisor_consultant model should be gpt-5.5")
    if data.get("model_reasoning_effort") != "xhigh":
        errors.append("advisor_consultant model_reasoning_effort should be xhigh")
    if data.get("sandbox_mode") != "read-only":
        errors.append("advisor_consultant sandbox_mode should be read-only")

if skill.exists():
    text = skill.read_text()
    for required in [
        "Advisor Consultant",
        "Default Advisor Consultant to `brief-only`",
        "## Decision Needed",
        "## Go / No-Go",
        "## Advisor Decision Receipt",
    ]:
        if required not in text:
            errors.append(f"SKILL.md missing advisor contract text: {required}")

if not (root / "AGENTS.md").exists():
    errors.append("missing AGENTS.md")

if errors:
    print("Codex package validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Codex package validation passed.")
