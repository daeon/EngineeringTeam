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
        "## Canonical gate ownership",
        "## Required output: Intake artifact",
    ],
    "references/agent-routing.md": [
        "# Agent Routing",
        "## Context budget policy",
        "## Proactive subagent triggers",
        "## Delegation envelope",
        "## Context capsule rule",
    ],
    "references/route-codebase-analysis.md": [
        "# Codebase Analysis Route",
        "## Authority",
        "## Workflow",
        "## Output",
    ],
    "references/route-debugging.md": [
        "# Debugging Route",
        "## Authority",
        "## Workflow",
        "## Output",
    ],
    "references/route-log-analysis.md": [
        "# Log Analysis Route",
        "## Authority",
        "## Workflow",
        "## Output",
    ],
    "references/route-performance.md": [
        "# Performance Route",
        "## Authority",
        "## Workflow",
        "## Output",
    ],
    "references/route-handoff.md": [
        "# Handoff Route",
        "## Authority",
        "## Workflow",
        "## Output",
    ],
    "references/run-ledger.md": [
        "# Run Ledger",
        "## When to create it",
        "## Separation from memory",
        "## Promotion handoff",
    ],
    "references/memory-promotion.md": [
        "# Memory Promotion",
        "## Canonical memory anchors",
        "## Promotion rules",
        "## Target files",
        "## Required metadata",
    ],
    "references/subagent-context-policy.md": [
        "# Subagent Context Policy",
        "## Canonical delegation anchors",
        "## Main agent owns",
        "## Subagents own",
        "## Delegate when",
        "## Fallback when",
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
        "## Canonical contract anchors",
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
    "references/failure-attribution.md": [
        "# Failure Attribution",
        "## Canonical failure triage",
        "## Failure classes",
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

UNKNOWNS_FIRST_REFERENCE_CONTRACTS: dict[str, list[str]] = {
    "references/unknowns-first/router.md": [
        "# Unknowns-First Router",
        "## Trigger rules",
        "## Skip rules",
        "## Smallest useful phase",
        "## Artifact mapping",
        "## Output",
    ],
    "references/unknowns-first/blindspot-pass.md": [
        "# Blindspot Pass",
        "## Known knowns",
        "## Known unknowns",
        "## Unknown knowns",
        "## Unknown unknowns",
        "## Hidden assumptions",
        "## Cheap probes",
    ],
    "references/unknowns-first/architecture-interview.md": [
        "# Architecture Interview",
        "## One-question protocol",
        "## Decision ladder",
        "## Recommended defaults",
        "## Output",
    ],
    "references/unknowns-first/prototype-reference-probe.md": [
        "# Prototype Reference Probe",
        "## When to prototype",
        "## Probe rules",
        "## Reference comparison",
        "## Output mapping",
    ],
    "references/unknowns-first/risk-first-plan.md": [
        "# Risk-First Plan",
        "## Decisions table",
        "## Risk ordering",
        "## Invalidating discoveries",
        "## Output mapping",
    ],
    "references/unknowns-first/implementation-notes-log.md": [
        "# Implementation Notes Log",
        "## Material deviations",
        "## Conservative choices",
        "## Tests skipped",
        "## Human judgment needed",
        "## Output mapping",
    ],
    "references/unknowns-first/change-explainer-quiz.md": [
        "# Change Explainer Quiz",
        "## Reviewer-ready explainer",
        "## Optional quiz",
        "## Output mapping",
    ],
    "references/unknowns-first/risk-score.md": [
        "# Risk Score",
        "## Scoring rubric",
        "## Score interpretation",
        "## Output",
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

CANONICAL_CONCEPTS: dict[str, dict[str, set[str]]] = {
    "Implementation Gate": {
        "allowed_paths": {"references/implementation-gate.md"},
        "heading_aliases": {"Implementation Gate", "Implementation gate"},
    },
    "Advisor Gate": {
        "allowed_paths": {"references/advisor-gate.md"},
        "heading_aliases": {"Advisor Gate", "Advisor gate"},
    },
    "Run Ledger": {
        "allowed_paths": {"references/run-ledger.md", "templates/run-ledger.md"},
        "heading_aliases": {"Run Ledger"},
    },
    "memory promotion": {
        "allowed_paths": {"references/memory-promotion.md"},
        "heading_aliases": {"Memory Promotion"},
    },
    "generated-code rules": {
        "allowed_paths": {"references/repo-atlas.md", "templates/repo-atlas.md"},
        "heading_aliases": {"Generated Code Rules", "Generated-code rules"},
    },
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

FORBIDDEN_UNKNOWNS_FIRST_PATTERNS = [
    r"(?i)session-start",
    r"(?i)\bhooks?\b",
    r"(?i)\bautoload\b",
    r"(?i)\bstartup\b",
    r"(?i)\bbootstrap\b",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    require(path.exists(), f"missing {path}")
    return json.loads(path.read_text())


def parse_frontmatter(text: str, label: str) -> str:
    frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    require(frontmatter is not None, f"{label} missing frontmatter")
    return frontmatter.group(1)


def linked_reference_sources(plugin_root: Path, skill_dir: Path) -> list[Path]:
    return [
        skill_dir / "SKILL.md",
        *skill_dir.joinpath("references").rglob("*.md"),
    ]


def resolve_skill_doc_link(source_path: Path, link: str, skill_dir: Path) -> Path:
    if link.startswith(("references/", "templates/")):
        return skill_dir / link
    return (source_path.parent / link).resolve()


def validate_backticked_doc_links(plugin_root: Path, skill_dir: Path) -> None:
    """Validate every backticked references/templates Markdown link in skill/reference docs."""

    link_pattern = re.compile(r"`([^`\n]*(?:references|templates)/[^`\n]+\.md)`")
    for source_path in sorted(linked_reference_sources(plugin_root, skill_dir)):
        if not source_path.exists():
            continue
        text = source_path.read_text()
        for link in sorted(set(link_pattern.findall(text))):
            target = resolve_skill_doc_link(source_path, link, skill_dir)
            require(
                target.exists(),
                f"{source_path.relative_to(plugin_root)} links missing skill doc: {link}",
            )


def validate_single_skill_contract(plugin_root: Path, canonical_skill: Path) -> None:
    skills_dir = plugin_root / "skills"
    skill_paths = sorted(skills_dir.rglob("SKILL.md"))
    require(
        skill_paths == [canonical_skill],
        "EngineeringTeam must expose exactly one discoverable skill: "
        f"expected {[str(canonical_skill.relative_to(plugin_root))]}, "
        f"found {[str(path.relative_to(plugin_root)) for path in skill_paths]}",
    )
    top_level_entries = sorted(path.name for path in skills_dir.iterdir())
    require(
        top_level_entries == ["engineering-team"],
        "skills/ must contain only the engineering-team bundle; "
        f"found {top_level_entries}",
    )


def validate_no_spawnable_lead(plugin_root: Path) -> None:
    forbidden = [
        plugin_root / "agents-src" / "lead-engineer.yaml",
        plugin_root / "agents" / "lead-engineer.md",
        plugin_root / ".codex" / "agents" / "lead_engineer.toml",
        plugin_root / ".github" / "agents" / "lead-engineer.md",
        plugin_root / "skills" / "engineering-team" / "assets" / "agents" / "lead_engineer.toml",
    ]
    present = [str(path.relative_to(plugin_root)) for path in forbidden if path.exists()]
    require(not present, f"main-session Lead must not remain spawnable: {present}")


def normalize_heading(text: str) -> str:
    text = text.strip().lower().replace("-", " ")
    return re.sub(r"\s+", " ", text)


def validate_canonical_concept_owners(skill_dir: Path) -> None:
    """Fail if canonical workflow concepts gain duplicate definition headings."""

    heading_pattern = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
    sources = [
        skill_dir / "SKILL.md",
        *skill_dir.joinpath("references").glob("*.md"),
        *skill_dir.joinpath("templates").glob("*.md"),
    ]
    alias_to_concept: dict[str, tuple[str, set[str]]] = {}
    for concept, config in CANONICAL_CONCEPTS.items():
        for alias in config["heading_aliases"]:
            alias_to_concept[normalize_heading(alias)] = (concept, config["allowed_paths"])

    for source_path in sorted(sources):
        rel_path = source_path.relative_to(skill_dir).as_posix()
        for line_no, line in enumerate(source_path.read_text().splitlines(), 1):
            match = heading_pattern.match(line)
            if match is None:
                continue
            heading = normalize_heading(match.group(2))
            if heading not in alias_to_concept:
                continue
            concept, allowed_paths = alias_to_concept[heading]
            require(
                rel_path in allowed_paths,
                f"duplicate-risk heading for canonical concept {concept!r} in {rel_path}:{line_no}; "
                f"canonical owner is {', '.join(sorted(allowed_paths))}",
            )


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


def validate_unknowns_first_references(skill_dir: Path) -> None:
    unknowns_dir = skill_dir / "references" / "unknowns-first"
    require(unknowns_dir.exists(), "missing references/unknowns-first directory")

    expected_paths = set(UNKNOWNS_FIRST_REFERENCE_CONTRACTS)
    actual_paths = {
        path.relative_to(skill_dir).as_posix()
        for path in unknowns_dir.glob("*.md")
    }
    require(
        expected_paths == actual_paths,
        "unknowns-first references must match expected files: "
        f"expected {sorted(expected_paths)}, found {sorted(actual_paths)}",
    )

    router_headings: list[str] = []
    for rel_path, required_headings in UNKNOWNS_FIRST_REFERENCE_CONTRACTS.items():
        full_path = skill_dir / rel_path
        require(full_path.exists(), f"missing unknowns-first reference: {rel_path}")
        text = full_path.read_text()
        for heading in required_headings:
            require(heading in text, f"{rel_path} missing required heading: {heading}")
        if re.search(r"^#\s+.*router.*$", text, re.I | re.M):
            router_headings.append(rel_path)
        for pattern in FORBIDDEN_UNKNOWNS_FIRST_PATTERNS:
            require(
                re.search(pattern, text) is None,
                f"{rel_path} contains unsafe startup/hook/session reference: {pattern}",
            )

    require(
        router_headings == ["references/unknowns-first/router.md"],
        "unknowns-first must have exactly one top-level router concept in references/unknowns-first/router.md",
    )


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
    frontmatter = parse_frontmatter(skill, "SKILL.md")
    require("name:" in frontmatter, "SKILL.md missing name")
    require("description:" in frontmatter, "SKILL.md missing description")

    skill_dir = skill_path.parent

    validate_single_skill_contract(plugin_root, skill_path)
    validate_no_spawnable_lead(plugin_root)

    validate_backticked_doc_links(plugin_root, skill_dir)
    validate_unknowns_first_references(skill_dir)

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

    validate_canonical_concept_owners(skill_dir)

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
