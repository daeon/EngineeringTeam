# Repo Atlas Memory

Durable repository map entries go here.

Use this format:

```md
## <area or workflow>

- Status: current | needs-verification | stale
- Summary:
- Evidence/source paths:
- Origin run:
- Last verified:
- Confidence: high | medium | low
- Review trigger:
```

## System type and shape

- Status: current
- Summary: Not a runtime/service. This repo is a multi-harness *workflow skill* for AI coding agents (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, GitHub Copilot). Deliverables are Markdown skills + generated agent definitions + Python/Bash packaging scripts. No network, no session-start hooks, MIT licensed.
- Evidence/source paths: `README.md`, `package.json`, `SECURITY.md`, `skills/engineering-team/SKILL.md`
- Last verified: 2026-05-29

## Canonical skill bundle

- Status: current
- Summary: All harnesses point at `skills/`, which contains exactly one discoverable skill: `skills/engineering-team/SKILL.md`. It selects implementation, read-only analysis, or handoff authority and directly links focused codebase, debugging, log, performance, and handoff route references. Deeper procedures and artifact templates remain lazily loaded inside the bundle.
- Evidence/source paths: `skills/engineering-team/SKILL.md`, `skills/engineering-team/references/route-*.md`, `skills/engineering-team/templates/`, `skills/engineering-team/scripts/validate-package.py`
- Last verified: 2026-08-13

## Generated-code rules (do not hand-edit)

- Status: current
- Summary: Eleven spawnable specialist agents have a single source of truth in `agents-src/*.yaml`, schema-validated before rendering. The main session owns Lead responsibility and no Lead agent definition is generated. `scripts/generate-agents.py` renders each specialist to `agents/*.md`, `.codex/agents/*.toml`, `.github/agents/*.md`, and a bundled Codex copy under `skills/engineering-team/assets/agents/`. Every output carries a `GENERATED FILE - DO NOT EDIT` banner. `CLAUDE.md` is generated from `AGENTS.md` via `scripts/sync-docs.py`.
- Evidence/source paths: `agents-src/*.yaml`, `scripts/generate-agents.py`, `scripts/sync-docs.py`, `tests/test_generate_agents.py`, `agents/`, `.codex/agents/`, `.github/agents/`, `CONTRIBUTING.md`
- Last verified: 2026-08-13

## Build / test / install commands

- Status: current
- Summary: `npm run validate` runs the full CI gate; `python3 scripts/doctor.py` is a local health superset; `npm run generate:agents` regenerates agents; `npm run check:agents` is drift-only; `python3 scripts/install.py --target <harness>` installs/prints per-harness setup. No npm/pip runtime deps.
- Evidence/source paths: `package.json` (scripts), `scripts/doctor.py`, `scripts/install.py`, `.github/workflows/validate.yml`
- Last verified: 2026-05-29
