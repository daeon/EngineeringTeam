# Contracts Memory

Durable producer/consumer contract notes go here.

Use this format:

```md
## <contract>

- Status: current | needs-verification | stale
- Producer:
- Contract/data shape:
- Consumer:
- Failure mode:
- Evidence/source paths:
- Origin run:
- Last verified:
- Confidence: high | medium | low
- Review trigger:
```

## Agent source -> generated native agents

- Status: current
- Producer: `agents-src/*.yaml` (hand-authored) via `scripts/generate-agents.py`. Sources are schema-validated (`validate_agent`) before rendering.
- Contract/data shape: Each of 11 specialist YAML sources produces 4 outputs: `agents/<name>.md` (Claude/Cursor), `.codex/agents/<name_with_underscores>.toml` (Codex), `.github/agents/<name>.md` (Copilot), plus one bundled TOML copy under `skills/engineering-team/assets/agents/`. All outputs carry a `GENERATED FILE - DO NOT EDIT` banner. Lead belongs to the main session and must have no source or generated output.
- Consumer: Claude Code / Cursor read `agents/*.md`; Codex reads `.codex/agents/*.toml`; GitHub Copilot reads `.github/agents/*.md`; the skill bundle ships `assets/agents/*.toml`.
- Failure mode: Hand-editing a generated file is silently overwritten on next generate; an invalid source (unknown key, bad `sandbox_mode`/`model_reasoning_effort`, name/filename mismatch) raises `ValueError`; CI fails via `generate-agents.py --check` and `tests/test_generate_agents.py`.
- Evidence/source paths: `scripts/generate-agents.py`, `tests/test_generate_agents.py`, `package.json` (`check:agents`, `test:scripts`), `.github/workflows/validate.yml`
- Last verified: 2026-08-13

## AGENTS.md -> CLAUDE.md (doc sync)

- Status: current
- Producer: `AGENTS.md` (single source) via `scripts/sync-docs.py`.
- Contract/data shape: `CLAUDE.md` must be byte-identical to `AGENTS.md`.
- Consumer: Claude Code reads `CLAUDE.md`; other harnesses read `AGENTS.md`; `validate-package.py` requires both to exist; `sync-docs.py --check` requires them identical.
- Failure mode: Hand-editing `CLAUDE.md` (or editing `AGENTS.md` without re-syncing) fails `npm run validate`.
- Evidence/source paths: `scripts/sync-docs.py`, `package.json`, `AGENTS.md`, `CLAUDE.md`
- Last verified: 2026-05-29

## Version sync across manifests

- Status: current
- Producer: `scripts/bump-version.py` driven by `.version-bump.json`.
- Contract/data shape: A single version string kept identical across 7 JSON targets (plugin + marketplace manifests for each harness + `package.json`). Currently 0.2.0.
- Consumer: `bash scripts/bump-version.py --check` in `npm run validate`.
- Failure mode: Editing a version in one manifest without the others fails `--check`. OpenCode plugin JS and agent files carry no version field.
- Evidence/source paths: `.version-bump.json`, `scripts/bump-version.py`, `package.json`
- Last verified: 2026-08-13

## SKILL.md reference links -> reference files

- Status: current
- Producer: `` `references/*.md` `` links written in `skills/engineering-team/SKILL.md`.
- Contract/data shape: Every backticked `references/<file>.md` token in the main skill or any bundled reference must resolve; selected references/templates must contain required headings. The five mode routes must be linked directly from the main skill.
- Consumer: `validate-package.py` recursive link checks plus `REFERENCE_CONTRACTS`/`TEMPLATE_CONTRACTS` heading checks.
- Failure mode: A missing route/reference, broken link, additional `skills/**/SKILL.md`, extra top-level entry under `skills/`, or reintroduced Lead agent fails CI.
- Evidence/source paths: `skills/engineering-team/scripts/validate-package.py`, `skills/engineering-team/SKILL.md`
- Last verified: 2026-08-13
