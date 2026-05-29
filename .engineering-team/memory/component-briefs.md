# Component Briefs Memory

Reusable component ownership and call-path notes go here.

Use this format:

```md
## <component>

- Status: current | needs-verification | stale
- Owner/scope:
- Key files/symbols:
- Evidence/source paths:
- Last verified:
```

## Agent generation pipeline

- Status: current
- Owner/scope: Single-source-of-truth compiler that turns `agents-src/*.yaml` into per-harness native agent files.
- Key files/symbols: `scripts/generate-agents.py` — `parse_agent()` (custom YAML-subset parser), `render_markdown()` (Claude/Cursor), `render_toml()` (Codex), `render_github_markdown()` (Copilot), `generate()`, `check()` (drift via `--check`). `generate()` deletes then rewrites all `*.md`/`*.toml` in generated dirs.
- Evidence/source paths: `scripts/generate-agents.py`, `agents-src/lead-engineer.yaml`, `agents/lead-engineer.md`, `.codex/agents/lead_engineer.toml`
- Last verified: 2026-05-29

## Skill router

- Status: current
- Owner/scope: Entry point all harnesses load; routes implementation vs read-only analysis and lazily loads references.
- Key files/symbols: `skills/engineering-team/SKILL.md` — "Two operating modes" table, "Workflow" chain, "Required artifacts" table, "Load references only when needed" lazy-load table, "L0 fast path".
- Evidence/source paths: `skills/engineering-team/SKILL.md`, `skills/engineering-team/references/analysis-routing.md`, `skills/engineering-team/references/intake-risk.md`
- Last verified: 2026-05-29

## Package validators

- Status: current
- Owner/scope: CI gates that enforce manifest shape, skill/reference/template heading contracts, generated-agent presence, and the no-session-start-hooks promise.
- Key files/symbols: `skills/engineering-team/scripts/validate-package.py` — `REFERENCE_CONTRACTS`, `TEMPLATE_CONTRACTS`, `READ_ONLY_SKILL_CONTRACTS`, `validate_no_session_start_hooks()`, and a regex existence-check of `` `references/*.md` `` links in SKILL.md (line ~235). `scripts/validate-codex-package.py` adds Codex-specific checks (incl. hardcoded advisor model/sandbox).
- Evidence/source paths: `skills/engineering-team/scripts/validate-package.py`, `scripts/validate-codex-package.py`
- Last verified: 2026-05-29
