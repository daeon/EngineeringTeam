# Security Policy

EngineeringTeam is a workflow layer for AI coding agents. Its safety posture is
deliberately conservative.

## 🛡️ Safety posture

- **No unpinned remote execution.** The package does not download or execute
  remote code. All scripts are local and dependency-free.
- **No session-start shell behavior.** Installing the package does not register
  any hook that runs shell commands when a session starts. The workflow is
  invoked manually with `engineering-team`.
- **No hidden persistence.** The package does not write outside the repository
  or a user-chosen install target. Install scripts never overwrite existing
  files unless you pass `--force`.
- **No automatic production mutation.** The workflow never deploys, mutates
  production systems, or runs destructive commands on its own.
- **Human approval for destructive or production-sensitive actions.** The skill
  requires explicit human approval before live-system mutation, irreversible
  data/file changes, broad generated-file rewrites, or release/rollback
  decisions.
- **Least-privilege tool guidance.** Specialist agents declare read-only vs
  edit boundaries. Investigation and review agents are read-only; only the
  implementation, test, and documentation roles may edit, and only after the
  evidence gate.
- **Plugin install transparency.** Installation copies clearly named files into
  visible locations (`.codex/agents/`, `.github/agents/`) or prints exact
  manual steps for marketplace-based harnesses.

## 📜 Scripts that run locally

- `scripts/validate-codex-package.py`, `skills/engineering-team/scripts/validate-package.py` — read and validate manifests.
- `scripts/generate-agents.py` — regenerates agent files from `agents-src/`.
- `scripts/doctor.py` — runs the read-only validators and reports health.
- `scripts/install.py`, `skills/engineering-team/scripts/install-custom-agents.py` — copy agent files into a chosen target; idempotent unless `--force`.

## 🚨 Reporting a vulnerability

Open a private security advisory on the repository, or email the maintainer
listed in `.claude-plugin/plugin.json`. Please do not file public issues for
sensitive reports. Include reproduction steps and the affected files.
