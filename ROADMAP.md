# Roadmap

Planned and aspirational work, grouped by area. This is a direction document,
not a commitment.

## 🔁 Core workflow

- Keep the repo-first gate (atlas → component → contract → evidence → verify)
  the stable center of the skill.
- Sharper alignment/grilling prompts for ambiguous tasks.
- Tighter failure-attribution loop guidance.

## 🔌 Harness support

- Promote GitHub Copilot custom agents from experimental to supported once the
  format stabilizes.
- Track changes to Codex, Claude Code, Cursor, Gemini, and OpenCode agent
  formats and keep generation in sync.
- Evaluate additional harnesses as they add custom-agent surfaces.

## 🧪 Examples

- Add a second worked example in another language (e.g. a TypeScript service).
- Add a refactor example and a migration/compatibility example.
- Record short demo captures referenced from `docs/demo-script.md`.

## ✅ Validation

- Optional Python version matrix (3.11, 3.12) in CI.
- Optional, low-noise markdown link checking.
- Schema-level checks for agent source YAML.

## 🔒 Safety

- Keep the no-remote-execution, no-session-shell, human-approval posture in
  `SECURITY.md` as the package grows.
- Document tool-permission expectations per harness.

## 🏪 Marketplace / distribution

- Smoother local marketplace install flows for Claude Code and Cursor.
- Clear, copy-paste install for each harness from one script (`scripts/install.py`).
- Launch materials kept current in `docs/launch-post.md` and `docs/prompt-cards.md`.
