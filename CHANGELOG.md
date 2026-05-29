# Changelog

## 0.1.0

Initial release of the EngineeringTeam multi-harness plugin.

- Added 12 specialist agents (lead-engineer, implementation-engineer, codebase-investigator, evidence-skeptic, advisor-consultant, security-analyst, optimization-engineer, migration-analyst, release-rollback-engineer, system-design-architect, test-verification-engineer, dx-documentation-reviewer).
- Added YAML generation pipeline (`agents-src/` → `agents/*.md`, `.codex/agents/*.toml`, skill assets) so all harness outputs share a single source of truth.
- Added session-start bootstrap hook (`hooks/`) that injects the `using-engineering-team` skill on session open for Claude Code and Cursor.
- Added `skills/using-engineering-team/SKILL.md` describing when and how to invoke the engineering-team skill.
- Added multi-harness plugin manifests: Claude Code (`.claude-plugin/`), Cursor (`.cursor-plugin/`), Codex (`.codex-plugin/`), OpenCode (`.opencode/`), Gemini (`gemini-extension.json`).
- Added Codex marketplace wrapper (`.agents/plugins/marketplace.json`).
- Added `scripts/generate-agents.py` with `--check` mode to detect agent drift in CI.
- Added `scripts/bump-version.sh` with `--check` and `--audit` support to keep version fields in sync across manifests.
- Added `scripts/validate-codex-package.py` and `skills/engineering-team/scripts/validate-package.py` for structural package validation.
