#!/usr/bin/env python3
"""Lightweight validation for the EngineeringTeam multi-harness package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REFERENCE_CONTRACTS: dict[str, list[str]] = {
    "references/intake-risk.md": [
        "# Intake and Risk Classification",
        "## Required output: Intake artifact",
    ],
    "references/agent-routing.md": [
        "# Agent Routing",
        "## Context budget policy",
        "## Proactive subagent triggers",
        "## Delegation envelope",
        "## Context capsule rule",
    ],
    "references/analysis-routing.md": [
        "# Read-Only Analysis Routing",
        "## Mode selection",
        "## Routing graph",
        "## Read-only analysis rules",
    ],
    "references/run-ledger.md": [
        "# Run Ledger",
        "## When to create it",
        "## Separation from memory",
        "## Promotion handoff",
    ],
    "references/memory-promotion.md": [
        "# Memory Promotion",
        "## Promotion rules",
        "## Target files",
        "## Required metadata",
    ],
    "references/subagent-context-policy.md": [
        "# Subagent Context Policy",
        "## Main agent owns",
        "## Subagents own",
        "## Delegate when",
        "## Do not delegate when",
        "## Context budgets",
    ],
    "references/repo-atlas.md": [
        "# Repo Atlas",
        "## Artifact: Repo Atlas",
    ],
    "references/component-brief.md": [
        "# Component Brief",
        "## Artifact: Component Brief",
    ],
    "references/contract-graph.md": [
        "# Contract Graph",
        "## Artifact: Contract Graph",
    ],
    "references/evidence-ledger.md": [
        "# Evidence Ledger",
        "## Artifact: Evidence Ledger",
    ],
    "references/advisor-gate.md": [
        "# Advisor Gate",
        "## Advisor brief contract",
    ],
    "references/implementation-gate.md": [
        "# Implementation Gate",
        "## Gate output",
    ],
    "references/impact-map.md": [
        "# Impact Map",
        "## Artifact: Impact Map",
    ],
    "references/verification-loop.md": [
        "# Verification Loop",
        "## Artifact: Verification Report",
    ],
    "references/context-garbage-collection.md": [
        "# Context Garbage Collection",
        "## Memory promotion flow",
        "## Artifact: Context GC output",
    ],
    "references/final-report.md": [
        "# Final Report",
        "## Final Report template",
    ],
}

TEMPLATE_CONTRACTS: dict[str, list[str]] = {
    "templates/subagent-brief.md": [
        "# Subagent Brief",
        "## Role",
        "## Mission",
        "## Context budget",
        "## Required output",
        "## Do not",
    ],
    "templates/context-capsule.md": [
        "# Context Capsule",
        "## Scope",
        "## Findings",
        "## Recommended next action",
    ],
    "templates/run-ledger.md": [
        "# Run Ledger",
        "## Task",
        "## Mode / Route Decision",
        "## Memory Candidates",
        "## Residual Risk",
    ],
    "templates/memory-candidates.md": [
        "# Memory Candidates",
        "## Candidate Table",
        "## Promotion Summary",
        "## Rejection Notes",
    ],
    "templates/codebase-analysis-report.md": [
        "# Codebase Analysis Report",
        "## Scope",
        "## Repo / Component Map",
        "## Call Paths and Contracts",
    ],
    "templates/debugging-hypothesis-matrix.md": [
        "# Debugging Hypothesis Matrix",
        "## Symptom",
        "## Hypotheses",
        "## Current conclusion",
    ],
    "templates/log-forensics-report.md": [
        "# Log Forensics Report",
        "## Scope and Data Handling",
        "## Timeline",
        "## Findings",
    ],
    "templates/performance-forensics-report.md": [
        "# Performance Forensics Report",
        "## Measurement Frame",
        "## Hot Path Map",
        "## Bottleneck Hypotheses",
    ],
    "templates/next-probe-plan.md": [
        "# Next-Probe Plan",
        "## Goal",
        "## Probes",
        "## Stop conditions",
    ],
}

READ_ONLY_SKILL_CONTRACTS: dict[str, list[str]] = {
    "codebase-analysis": [
        "name: codebase-analysis",
        "## Default posture",
        "Read-only by default",
        "## Required output",
    ],
    "debugging-forensics": [
        "name: debugging-forensics",
        "## Default posture",
        "Read-only by default",
        "## Required output",
    ],
    "log-forensics": [
        "name: log-forensics",
        "## Default posture",
        "Read-only by default",
        "## Required output",
    ],
    "performance-forensics": [
        "name: performance-forensics",
        "## Default posture",
        "Read-only by default",
        "## Required output",
    ],
}

MEMORY_CONTRACTS: dict[str, list[str]] = {
    "index.md": [
        "# EngineeringTeam Memory Index",
        "## Guardrails",
        "## Entry Template",
        "Origin run:",
        "Confidence: high | medium | low",
        "Review trigger:",
    ],
    "repo-atlas.md": [
        "# Repo Atlas Memory",
        "Evidence/source paths:",
        "Origin run:",
        "Confidence: high | medium | low",
        "Review trigger:",
    ],
    "component-briefs.md": [
        "# Component Briefs Memory",
        "Evidence/source paths:",
        "Origin run:",
        "Confidence: high | medium | low",
        "Review trigger:",
    ],
    "contracts.md": [
        "# Contracts Memory",
        "Evidence/source paths:",
        "Origin run:",
        "Confidence: high | medium | low",
        "Review trigger:",
    ],
    "verification.md": [
        "# Verification Memory",
        "Evidence/source paths:",
        "Origin run:",
        "Confidence: high | medium | low",
        "Review trigger:",
    ],
    "gotchas.md": [
        "# Gotchas Memory",
        "Evidence/source paths:",
        "Origin run:",
        "Confidence: high | medium | low",
        "Review trigger:",
    ],
}

FORBIDDEN_MEMORY_PATTERNS = [
    r"(?i)password\s*=",
    r"(?i)token\s*=",
    r"(?i)secret\s*=",
    r"BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY",
]

CONTEXT_DISCIPLINE_PHRASES = [
    "compact evidence-backed context capsules",
    "Context discipline",
]

NO_SESSION_START_PHRASES = [
    "No session-start shell behavior",
    "session-start magic",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    require(path.exists(), f"missing {path}")
    return json.loads(path.read_text())


def validate_no_session_start_hooks(plugin_root: Path, cursor_manifest: dict) -> None:
    """Keep code and docs aligned with the public no-startup-injection promise."""

    require(
        "hooks" not in cursor_manifest,
        "Cursor manifest must not define hooks while docs promise no session-start magic",
    )
    require(
        not (plugin_root / "hooks").exists(),
        "hooks/ directory exists while docs promise no session-start shell behavior",
    )
    require(
        not (plugin_root / "skills" / "using-engineering-team").exists(),
        "session-start bootstrap skill still exists after hooks were removed",
    )

    readme = plugin_root / "README.md"
    security = plugin_root / "SECURITY.md"
    require(readme.exists(), "missing README.md")
    require(security.exists(), "missing SECURITY.md")
    combined_docs = readme.read_text() + "\n" + security.read_text()
    for phrase in NO_SESSION_START_PHRASES:
        require(phrase in combined_docs, f"missing no-session-start documentation phrase: {phrase}")


def validate_memory_contracts(plugin_root: Path) -> None:
    memory_dir = plugin_root / ".engineering-team" / "memory"
    require(memory_dir.exists(), "missing .engineering-team/memory directory")

    for rel_path, required_phrases in MEMORY_CONTRACTS.items():
        full_path = memory_dir / rel_path
        require(full_path.exists(), f"missing memory file: {rel_path}")
        text = full_path.read_text()
        for phrase in required_phrases:
            require(phrase in text, f"memory/{rel_path} missing required phrase: {phrase}")
        for pattern in FORBIDDEN_MEMORY_PATTERNS:
            require(
                re.search(pattern, text) is None,
                f"memory/{rel_path} appears to contain forbidden sensitive pattern: {pattern}",
            )


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

    cursor_manifest = load_json(plugin_root / ".cursor-plugin" / "plugin.json")
    require(cursor_manifest.get("skills") == "./skills/", 'Cursor manifest skills must be "./skills/"')
    require(cursor_manifest.get("agents") == "./agents/", 'Cursor manifest agents must be "./agents/"')
    validate_no_session_start_hooks(plugin_root, cursor_manifest)

    marketplace = load_json(plugin_root / ".claude-plugin" / "marketplace.json")
    require(marketplace.get("plugins", [{}])[0].get("source") == "./", 'Claude marketplace source must be "./"')

    require(skill_path.exists(), f"missing {skill_path}")
    skill = skill_path.read_text()
    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    require(frontmatter is not None, "SKILL.md missing frontmatter")
    require("name:" in frontmatter.group(1), "SKILL.md missing name")
    require("description:" in frontmatter.group(1), "SKILL.md missing description")

    skill_dir = skill_path.parent

    for rel in sorted(set(re.findall(r"`(references/[^`]+\.md)`", skill))):
        require((skill_dir / rel).exists(), f"SKILL.md links missing reference: {rel}")

    for rel_path, required_headings in REFERENCE_CONTRACTS.items():
        full_path = skill_dir / rel_path
        require(full_path.exists(), f"missing required reference: {rel_path}")
        text = full_path.read_text()
        for heading in required_headings:
            require(heading in text, f"{rel_path} missing required heading: {heading}")

    for rel_path, required_headings in TEMPLATE_CONTRACTS.items():
        full_path = skill_dir / rel_path
        require(full_path.exists(), f"missing required template: {rel_path}")
        text = full_path.read_text()
        for heading in required_headings:
            require(heading in text, f"{rel_path} missing required heading: {heading}")

    validate_memory_contracts(plugin_root)

    for skill_name, required_phrases in READ_ONLY_SKILL_CONTRACTS.items():
        read_only_skill_path = plugin_root / "skills" / skill_name / "SKILL.md"
        require(read_only_skill_path.exists(), f"missing read-only analysis skill: {skill_name}")
        text = read_only_skill_path.read_text()
        require(text.startswith("---\n"), f"{skill_name} missing frontmatter")
        for phrase in required_phrases:
            require(phrase in text, f"{skill_name} missing required phrase: {phrase}")

    generated_agents_dir = skill_dir / "assets" / "agents"
    require(generated_agents_dir.exists(), f"missing generated agents dir: {generated_agents_dir}")
    for agent_file in sorted(generated_agents_dir.glob("*.toml")):
        agent_text = agent_file.read_text()
        has_discipline = any(phrase in agent_text for phrase in CONTEXT_DISCIPLINE_PHRASES)
        require(has_discipline, f"generated agent missing context-discipline language: {agent_file.name}")

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
