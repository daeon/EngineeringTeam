# Changelog

## Unreleased

Public-launch polish.

- Added optional unknowns-first pre-intake references for ambiguous, risky, unfamiliar, architecture-sensitive, security-sensitive, production-impacting, or assumption-heavy EngineeringTeam work.
- Documented unknowns-first routing, artifact mapping, and fused workflow examples while keeping `engineering-team` as the primary router.
- Extended package validation for unknowns-first reference files, required headings, reference links, router uniqueness, and startup/hook regression checks.
- Removed session-start bootstrap behavior: deleted `hooks/`, removed the Cursor manifest hook entry, and retired `skills/using-engineering-team/` so the package matches the documented no-session-start-magic posture.
- Hardened validation to fail if session-start hooks or bootstrap skills reappear while the public security posture says they are absent.
- Hardened generated-agent drift checks to detect stale extra generated files after source-agent renames or removals.
- Added the worked example suite to `npm run validate` and `scripts/doctor.py`.
- Softened Intake ordering so minimal repo discovery is allowed when needed to classify scope accurately before deep routing or implementation.
- Fixed package correctness: added `license`, `skills`, and `agents` fields to `.claude-plugin/plugin.json` so `validate-package.py` passes.
- Added `npm run validate`, `generate:agents`, and `check:agents` scripts so local and CI validation share one command.
- Added GitHub Copilot custom-agent generation under `.github/agents/*.md` (experimental), wired into generation, drift checks, and package validation.
- Added `scripts/doctor.py` (environment + package health check) and `scripts/install.py` (idempotent per-harness installer).
- Rewrote `README.md` for a public audience: hero, thirty-second pitch, the rule, when-not-to-edit, copy-paste quick start, supported-harness table, and badges.
- Added a runnable worked example (`examples/buggy-python-service/`) with a hidden-contract bug, raw-agent vs EngineeringTeam prompts, and filled-in expected artifacts.
- Added `docs/demo-script.md` and `docs/prompt-cards.md`.
- Upgraded artifact templates with compact instructions, one example each, and anti-pattern warnings.
- Added `CONTRIBUTING.md`, `SECURITY.md`, `ROADMAP.md`, and `docs/release-checklist.md`, `docs/launch-post.md`.
- Hardened CI to run `npm run validate` on Node 22.
- Hardened the agent generator: pure-Python schema validation of `agents-src/*.yaml` (allowed keys, `sandbox_mode`, `model_reasoning_effort`, name/filename match), a `GENERATED FILE - DO NOT EDIT` banner on every output, and unit tests (`tests/test_generate_agents.py`) wired into `npm run validate` and `scripts/doctor.py`.
- Made `CLAUDE.md` generated from `AGENTS.md` via `scripts/sync-docs.py` (with `--check` in validation) to remove byte-identical duplication.
- Reduced generated Codex TOMLs from three copies to two by dropping the redundant `references/codex-custom-agents/` reference mirror; `.codex/agents/` (runtime) and the skill-bundled `assets/agents/` remain.
- Deduplicated the context-budget table (owned by `references/subagent-context-policy.md`) and the failure taxonomy (owned by `references/failure-attribution.md`).
- Wired previously orphaned references into `SKILL.md` and added `references/impact-map.md` to make the L4 Impact Map requirement actionable.
- Added a role-differentiation section (Lead vs Investigator/Architect, Skeptic vs Advisor) and a write-agent file-ownership matrix (Implementation → source, Verification → tests, DX → docs).

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
