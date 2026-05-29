# EngineeringTeam

[![Validate](https://github.com/daeon/EngineeringTeam/actions/workflows/validate.yml/badge.svg)](https://github.com/daeon/EngineeringTeam/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Multi-harness](https://img.shields.io/badge/harness-Claude%20%7C%20Codex%20%7C%20Cursor%20%7C%20Gemini%20%7C%20OpenCode%20%7C%20GitHub-blue)
![Repo-first](https://img.shields.io/badge/workflow-repo--first-orange)
![Evidence-gated](https://img.shields.io/badge/edits-evidence--gated-purple)

**Make your AI coding agent behave like a senior engineering team.**

EngineeringTeam is a repo-first workflow layer for AI coding agents. It makes the agent map the repo, trace contracts, gather evidence, route specialists selectively, gate implementation, verify changes, and hand off reviewable artifacts before claiming success.

> Stop vibe-coding legacy repos. Make the agent prove it understands the code before it edits.

## ⚡ In thirty seconds

Most coding agents are fast, but speed is not judgment. On a real codebase the hard part is not typing code — it is finding the owning component, understanding the call path, preserving contracts, choosing the smallest safe change, and proving the change works.

EngineeringTeam turns that discipline into a reusable skill that works across the agent you already use. It does not add a runtime service, network calls, or session-start magic. You invoke `engineering-team` when a task deserves a rigorous workflow, and the agent produces compact, human-reviewable artifacts as it goes.

Use `handoff` when you want the current task transferred to another agent or a fresh session. It compacts the work into a continuation document with decisions, evidence, open questions, artifact links, suggested skills, and next actions.

Specialist agents (security, architecture, performance, migration, release, verification, evidence skepticism) are **selective, not mandatory**. The workflow routes only the ones a task actually needs.

## 📏 The rule

No non-trivial edit until the agent can answer:

1. Where does this behavior enter the system?
2. Where is it transformed?
3. Where does it leave?
4. Which contracts and consumers are affected?
5. What evidence supports the diagnosis or design?
6. What proves the change works?

If those are unanswered, the agent keeps mapping instead of editing.

## 🛑 When your agent should not edit yet

Hold off on editing — and let EngineeringTeam map first — when:

- The root cause is not yet backed by evidence.
- The owning component or call path is unknown.
- The change crosses a contract, public API, or module boundary.
- Source, tests, docs, or logs disagree.
- The change touches auth, secrets, shell, filesystem, network, migrations, or release behavior.
- There is no verification path yet.

## 🚀 Quick start

```bash
git clone https://github.com/daeon/EngineeringTeam
cd EngineeringTeam
python3 scripts/doctor.py
npm run validate
```

Then, in your coding agent:

```text
Use engineering-team to investigate this bug. Map the repo first, find the owning component, trace the affected contract graph, and propose the smallest safe fix with verification.
```

To transfer work to another agent or session:

```text
Use handoff to summarize this task for a fresh agent. Focus the next session on finishing verification and preparing the PR.
```

## 🎬 Demo

See the worked, runnable example and the talking points:

- `examples/buggy-python-service/` — a small service with a real bug, the raw-agent prompt, the EngineeringTeam prompt, and filled-in expected artifacts.
- `docs/demo-script.md` — 60-second and 5-minute demo scripts, plus a raw-agent vs EngineeringTeam comparison.
- `docs/prompt-cards.md` — copy-paste prompts for bug investigation, PR review, performance, security, migration, release, architecture, test strategy, and handoff.

## 🔌 Supported harnesses

| Harness | Reads | Status |
|---|---|---|
| Claude Code | `.claude-plugin/plugin.json`, `agents/*.md`, `skills/` | Supported |
| Codex | `.codex-plugin/plugin.json`, `.codex/agents/*.toml`, `skills/` | Supported |
| Cursor | `.cursor-plugin/plugin.json`, `agents/*.md`, `skills/` | Supported |
| Gemini CLI | `gemini-extension.json`, `GEMINI.md`, `AGENTS.md` | Supported |
| OpenCode | `.opencode/plugins/engineering-team.js` | Supported |
| GitHub Copilot | `.github/agents/*.md` | Experimental |

All harnesses point at the same canonical skill bundle: `skills/engineering-team/SKILL.md`. Native agent definitions are generated from one source of truth (`agents-src/*.yaml`) — see `docs/harness-support.md`.

## 🗂️ What the artifacts look like

EngineeringTeam makes the agent produce compact, reviewable artifacts before and after implementation:

- **Repo Atlas** — system type, entry points, build/test commands, generated-code rules, high-risk areas.
- **Component Brief** — owning component, key files/symbols, related tests, inputs, outputs, side effects.
- **Contract Graph** — producer, contract/data shape, consumer, failure mode, coverage, risk.
- **Evidence Ledger** — claim, evidence, confidence, impact.
- **Verification Report** — command, result, important output, failure attribution, residual risk.
- **Handoff Document** — continuation context for another agent or session, with decisions, evidence, artifact links, open questions, risks, suggested skills, and next actions.

These make the agent's reasoning inspectable: a reviewer can see whether it understood the code path, not just whether the diff looks plausible. Filled-in samples live in `examples/buggy-python-service/expected-artifacts/`.

## 📦 Install

One command validates the package; one command installs for a target harness.

### Codex custom agents

```bash
python3 scripts/install.py --target codex --scope project --repo .
# or globally:
python3 scripts/install.py --target codex --scope user
```

### GitHub Copilot custom agents

```bash
python3 scripts/install.py --target github --scope project --repo /path/to/repo
```

### Claude Code

```bash
/plugin marketplace add .
/plugin install engineering-team@engineering-team-dev
```

### Cursor / Gemini CLI / OpenCode

```bash
python3 scripts/install.py --target cursor --scope project --repo .
python3 scripts/install.py --target opencode --scope project --repo .
```

Gemini CLI installs as an extension:

```bash
gemini extensions install /path/to/EngineeringTeam
```

Installs are idempotent: existing files are skipped unless you pass `--force`.

## Keeping main context clean

EngineeringTeam uses the main agent as the Lead Engineer. Broad search, noisy test output, and specialist review can be delegated to subagents. Subagents receive bounded briefs and return compact context capsules, not transcripts. This keeps the main session focused on evidence, decisions, implementation gates, and final handoff.

## ✅ Validation

```bash
npm run validate
python3 scripts/doctor.py
```

`npm run validate` runs the same checks as CI: JSON manifests, TOML agents, generated-agent drift including stale generated files, version consistency, OpenCode JS syntax, package structure, no session-start hook regression, and the worked example test suite. The same command runs in GitHub Actions via `.github/workflows/validate.yml`.

## 📚 Documentation

Full docs page: https://github.com/daeon/EngineeringTeam/tree/main/docs

- `docs/design.md` — architecture, design principles, harness boundaries, and adoption model.
- `docs/why-engineeringteam.md` — product value, target users, positioning.
- `docs/getting-started.md` — install, first prompts, expected outputs.
- `docs/workflow.md` — detailed workflow, dataflow, and gates.
- `docs/specialists.md` — specialist role catalog and routing guidance.
- `docs/harness-support.md` — per-harness packaging notes.
- `docs/demo-script.md` — demo scripts and comparison.
- `docs/prompt-cards.md` — copy-paste prompts by task type.

## 🤝 Contributing

See `CONTRIBUTING.md` for how to edit agent sources, regenerate native agents, and validate changes. Security posture is documented in `SECURITY.md`. Planned work is in `ROADMAP.md`.

## ⚖️ License

MIT License. See `LICENSE`.
