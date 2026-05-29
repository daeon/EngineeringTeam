# Contributing to EngineeringTeam

Thanks for helping improve EngineeringTeam. The package is intentionally
dependency-free and driven by one source of truth, so most changes are small
and validated by a single command.

## 🛠️ Prerequisites

- Python 3.11+ (the Codex validator uses the stdlib `tomllib` module).
- Node 22 (only needed for the OpenCode JS syntax check).

## ✅ One-command validation

```bash
npm run validate
```

This runs the same checks as CI:

- JSON manifests parse.
- TOML agent files parse and carry required fields.
- Generated agents are not stale.
- `CLAUDE.md` is in sync with `AGENTS.md`.
- Versions are in sync across manifests.
- The OpenCode plugin JS has valid syntax.
- The generator unit tests pass (`tests/`).
- Package structure matches the validators.

A broader health check is available with:

```bash
python3 scripts/doctor.py
```

## 🤖 Editing specialist agents

Agents have **one** source of truth: `agents-src/*.yaml`. Do not hand-edit the
generated files (each carries a `GENERATED FILE - DO NOT EDIT` banner). Sources
are schema-validated on every generate/check (allowed keys, `sandbox_mode`, and
`model_reasoning_effort` values), so a typo fails fast. After changing a source
file, regenerate:

```bash
python3 scripts/generate-agents.py
```

Generation writes, for each agent:

```text
agents/<name>.md                                  Claude / Cursor
.codex/agents/<name>.toml                         Codex
skills/engineering-team/assets/agents/<name>.toml Codex (bundled in the skill)
.github/agents/<name>.md                          GitHub Copilot
```

CI fails if generated files drift from source (`python3 scripts/generate-agents.py --check`).
The generator itself is covered by `tests/test_generate_agents.py` (`npm run test:scripts`).

## 📄 AGENTS.md and CLAUDE.md

`AGENTS.md` is the single source for repo-level agent guidance. `CLAUDE.md` is
generated from it (Claude Code reads `CLAUDE.md`; other harnesses read
`AGENTS.md`). After editing `AGENTS.md`, run:

```bash
python3 scripts/sync-docs.py
```

CI fails if the two drift (`python3 scripts/sync-docs.py --check`).

## 🏷️ Versioning

Version-bearing files are declared in `.version-bump.json`. Bump every declared
file at once:

```bash
python3 scripts/bump-version.py 0.2.0
python3 scripts/bump-version.py --check
```

## ✏️ Editing the skill or docs

- The canonical workflow is `skills/engineering-team/SKILL.md`. Some validator
  checks assert specific advisor-contract text exists there; run `npm run
  validate` after editing it.
- Keep templates under `skills/engineering-team/templates/` concise; they should
  be usable on their own without reading the whole skill.

## 🔀 Pull requests

1. Run `npm run validate` and `python3 scripts/doctor.py`.
2. Keep changes scoped; avoid unrelated refactors.
3. Update `CHANGELOG.md` under the `Unreleased` heading.
4. If you changed behavior, say how you verified it.
