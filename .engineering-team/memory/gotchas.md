# Gotchas Memory

Evidence-backed recurring pitfalls and stale-context warnings go here.

Use this format:

```md
## <gotcha>

- Status: current | needs-verification | stale
- Summary:
- Impact:
- Mitigation:
- Evidence/source paths:
- Origin run:
- Last verified:
- Confidence: high | medium | low
- Review trigger:
```

## Generated agent files are overwritten

- Status: current
- Summary: `agents/*.md`, `.codex/agents/*.toml`, `.github/agents/*.md`, and the bundled TOML copy under `skills/engineering-team/assets/agents/` are generated from `agents-src/*.yaml`. `generate()` deletes then rewrites them. Each carries a `GENERATED FILE - DO NOT EDIT` banner.
- Impact: Hand-edits are lost and CI fails on drift.
- Mitigation: Edit `agents-src/*.yaml`, then `npm run generate:agents`. Never edit generated files directly. Sources are schema-validated (allowed keys, `sandbox_mode`, `model_reasoning_effort`) so typos fail fast.
- Evidence/source paths: `scripts/generate-agents.py`, `tests/test_generate_agents.py`, `CONTRIBUTING.md`
- Last verified: 2026-05-29

## CLAUDE.md is generated from AGENTS.md

- Status: current
- Summary: `AGENTS.md` is the single source; `CLAUDE.md` is written from it by `scripts/sync-docs.py` and must stay identical (`--check` enforces this in `npm run validate`). `GEMINI.md` is a thin wrapper that imports `@AGENTS.md`.
- Impact: Editing `CLAUDE.md` by hand drifts from the source and fails CI.
- Mitigation: Edit `AGENTS.md`, then run `python3 scripts/sync-docs.py` (or `npm run sync:docs`).
- Evidence/source paths: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `scripts/sync-docs.py`, `package.json`
- Last verified: 2026-05-29

## Codex agent TOMLs exist in two generated locations

- Status: current
- Summary: Each generated Codex TOML is written to `.codex/agents/` (Codex runtime) and `skills/engineering-team/assets/agents/` (bundled in the skill) — 12 agents x 2 = 24 files. The former third "reference mirror" copy (`references/codex-custom-agents/`) was removed.
- Impact: Bypassing the generator in one location causes silent divergence.
- Mitigation: Only change via `agents-src/*.yaml` + generator; the `GENERATED` banner and `--check` guard against hand-edits.
- Evidence/source paths: `scripts/generate-agents.py`, `scripts/validate-codex-package.py`, `.codex/agents/`, `skills/engineering-team/assets/agents/`
- Last verified: 2026-05-29

## install.py is file-copy only for Codex and GitHub

- Status: current
- Summary: `scripts/install.py` copies files for `codex` and `github`; `claude`, `cursor`, `opencode` (and `gemini`) print manual setup steps and return 0 without copying.
- Impact: "Installed" output can be mistaken for a file install on marketplace/extension harnesses.
- Mitigation: Read each target's printed instructions; for Claude use the local marketplace, for Gemini use `gemini extensions install .`.
- Evidence/source paths: `scripts/install.py`, `README.md`, `docs/getting-started.md`
- Last verified: 2026-05-29

## No-session-start-hooks promise is CI-enforced

- Status: current
- Summary: The package promises no session-start shell behavior. `validate_no_session_start_hooks()` asserts the Cursor manifest has no `hooks`, no `hooks/` dir exists, the removed `skills/using-engineering-team` bootstrap stays absent, and that the no-session-start phrases remain in README + SECURITY.
- Impact: Adding hooks, a `hooks/` dir, or removing the documented phrases breaks CI.
- Mitigation: Keep the conservative posture; do not reintroduce session-start automation.
- Evidence/source paths: `skills/engineering-team/scripts/validate-package.py`, `SECURITY.md`, `README.md`
- Last verified: 2026-05-29
