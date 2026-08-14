# Component Briefs Memory

Reusable component ownership and call-path notes go here.

Use this format:

```md
## <component>

- Status: current | needs-verification | stale
- Owner/scope:
- Key files/symbols:
- Evidence/source paths:
- Origin run:
- Last verified:
- Confidence: high | medium | low
- Review trigger:
```

## Agent generation pipeline

- Status: current
- Owner/scope: Single-source-of-truth compiler that turns `agents-src/*.yaml` into per-harness native agent files.
- Key files/symbols: `scripts/generate-agents.py` — `parse_agent()` (custom YAML-subset parser), `render_markdown()` (Claude/Cursor), `render_toml()` (Codex), `render_github_markdown()` (Copilot), `generate()`, `check()` (drift via `--check`). `generate()` deletes then rewrites all `*.md`/`*.toml` in generated dirs.
- Evidence/source paths: `scripts/generate-agents.py`, `agents-src/*.yaml`, `agents/`, `.codex/agents/`, `.github/agents/`
- Last verified: 2026-08-13

## Skill router

- Status: current
- Owner/scope: The only discoverable skill; selects implementation, read-only analysis, or handoff authority and lazily loads route-specific references.
- Key files/symbols: `skills/engineering-team/SKILL.md` — mode table, authority boundaries, L0/L1 fast path, broad-to-narrow workflow, delegation and closeout rules.
- Evidence/source paths: `skills/engineering-team/SKILL.md`, `skills/engineering-team/references/route-*.md`, `skills/engineering-team/references/intake-risk.md`
- Last verified: 2026-08-13

## Package validators

- Status: current
- Owner/scope: CI gates that enforce manifest shape, skill/reference/template heading contracts, generated-agent presence, and the no-session-start-hooks promise.
- Key files/symbols: `skills/engineering-team/scripts/validate-package.py` — `REFERENCE_CONTRACTS`, `TEMPLATE_CONTRACTS`, `validate_single_skill_contract()`, `validate_no_spawnable_lead()`, `validate_no_session_start_hooks()`, and recursive reference-link checks. `scripts/validate-codex-package.py` adds Codex-specific checks.
- Evidence/source paths: `skills/engineering-team/scripts/validate-package.py`, `scripts/validate-codex-package.py`
- Last verified: 2026-08-13
