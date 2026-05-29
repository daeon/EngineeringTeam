#!/usr/bin/env python3
"""Lightweight validation for the EngineeringTeam multi-harness package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    require(path.exists(), f"missing {path}")
    return json.loads(path.read_text())


def main() -> int:
    plugin_root = Path(__file__).resolve().parents[3]
    skill_path = plugin_root / "skills" / "engineering-team" / "SKILL.md"

    manifests = [
        plugin_root / ".codex-plugin" / "plugin.json",
        plugin_root / ".claude-plugin" / "plugin.json",
        plugin_root / ".cursor-plugin" / "plugin.json",
        plugin_root / "gemini-extension.json",
        plugin_root / "package.json",
    ]
    for manifest_path in manifests:
        manifest = load_json(manifest_path)
        for key in ["name", "version"]:
            require(key in manifest, f"{manifest_path} missing {key}")

    codex_manifest = load_json(plugin_root / ".codex-plugin" / "plugin.json")
    require(codex_manifest.get("skills") == "./skills/", 'Codex manifest skills must be "./skills/"')

    claude_manifest = load_json(plugin_root / ".claude-plugin" / "plugin.json")
    require(claude_manifest.get("skills") == "./skills/", 'Claude manifest skills must be "./skills/"')
    require(claude_manifest.get("agents") == "./agents/", 'Claude manifest agents must be "./agents/"')

    cursor_manifest = load_json(plugin_root / ".cursor-plugin" / "plugin.json")
    require(cursor_manifest.get("skills") == "./skills/", 'Cursor manifest skills must be "./skills/"')
    require(cursor_manifest.get("agents") == "./agents/", 'Cursor manifest agents must be "./agents/"')

    marketplace = load_json(plugin_root / ".claude-plugin" / "marketplace.json")
    require(marketplace.get("plugins", [{}])[0].get("source") == "./", 'Claude marketplace source must be "./"')

    require(skill_path.exists(), f"missing {skill_path}")
    skill = skill_path.read_text()
    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    require(frontmatter is not None, "SKILL.md missing frontmatter")
    require("name:" in frontmatter.group(1), "SKILL.md missing name")
    require("description:" in frontmatter.group(1), "SKILL.md missing description")

    for agent_dir, pattern, minimum in [
        (plugin_root / "skills" / "engineering-team" / "assets" / "agents", "*.toml", 8),
        (plugin_root / ".codex" / "agents", "*.toml", 8),
        (plugin_root / "agents", "*.md", 8),
        (plugin_root / ".github" / "agents", "*.md", 8),
    ]:
        require(agent_dir.exists(), f"missing agent directory: {agent_dir}")
        require(len(list(agent_dir.glob(pattern))) >= minimum, f"expected at least {minimum} files in {agent_dir}")

    for path in [
        plugin_root / "AGENTS.md",
        plugin_root / "CLAUDE.md",
        plugin_root / "GEMINI.md",
        plugin_root / ".opencode" / "plugins" / "engineering-team.js",
    ]:
        require(path.exists(), f"missing {path}")

    print("OK: multi-harness plugin package structure is valid")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
