# Repo Atlas Memory

Durable repository map entries go here.

Use this format:

```md
## <area or workflow>

- Status: current | needs-verification | stale
- Summary:
- Evidence/source paths:
- Last verified:
```

## System type and shape

- Status: current
- Summary: Not a runtime/service. This repo is a multi-harness *workflow skill* for AI coding agents (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, GitHub Copilot). Deliverables are Markdown skills + generated agent definitions + Python/Bash packaging scripts. No network, no session-start hooks, MIT licensed.
- Evidence/source paths: `README.md`, `package.json`, `SECURITY.md`, `skills/engineering-team/SKILL.md`
- Last verified: 2026-05-29

## Canonical skill bundle

- Status: current
- Summary: All harnesses point at `skills/`. `skills/engineering-team/SKILL.md` (~145 lines) is the router with two modes (implementation, read-only analysis) and a lazy-load table. Depth lives in `skills/engineering-team/references/` (24 files) and `skills/engineering-team/templates/` (13 files). Five satellite skills: `codebase-analysis`, `debugging-forensics`, `log-forensics`, `performance-forensics`, `handoff`.
- Evidence/source paths: `skills/engineering-team/SKILL.md`, `skills/engineering-team/references/`, `skills/engineering-team/templates/`, `skills/*/SKILL.md`
- Last verified: 2026-05-29

## Generated-code rules (do not hand-edit)

- Status: current
- Summary: Specialist agents have a single source of truth in `agents-src/*.yaml` (12 files), schema-validated before rendering. `scripts/generate-agents.py` renders them to `agents/*.md` (Claude/Cursor), `.codex/agents/*.toml` (Codex; names use `_`), `.github/agents/*.md` (Copilot), plus one bundled Codex copy under `skills/engineering-team/assets/agents/` (2 TOML locations total). Every output carries a `GENERATED FILE - DO NOT EDIT` banner. `CLAUDE.md` is likewise generated from `AGENTS.md` via `scripts/sync-docs.py`. Edit the source, then `npm run generate:agents` / `npm run sync:docs`. CI fails on drift via `--check`; the generator is unit-tested in `tests/`.
- Evidence/source paths: `agents-src/*.yaml`, `scripts/generate-agents.py`, `scripts/sync-docs.py`, `tests/test_generate_agents.py`, `agents/`, `.codex/agents/`, `.github/agents/`, `CONTRIBUTING.md`
- Last verified: 2026-05-29

## Build / test / install commands

- Status: current
- Summary: `npm run validate` runs the full CI gate; `python3 scripts/doctor.py` is a local health superset; `npm run generate:agents` regenerates agents; `npm run check:agents` is drift-only; `python3 scripts/install.py --target <harness>` installs/prints per-harness setup. No npm/pip runtime deps.
- Evidence/source paths: `package.json` (scripts), `scripts/doctor.py`, `scripts/install.py`, `.github/workflows/validate.yml`
- Last verified: 2026-05-29
