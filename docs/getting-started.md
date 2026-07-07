# Getting Started

This guide helps you install EngineeringTeam, invoke the skill, and understand the first outputs you should expect.

## Install The Plugin

EngineeringTeam targets multiple agent harnesses from one skill bundle. `scripts/install.py` is the single entry point: two targets **copy files**, the rest **print exact manual setup steps** (nothing is copied).

```bash
# Copies files into the harness config:
python3 scripts/install.py --target codex --scope project --repo .
python3 scripts/install.py --target github --scope project --repo .

# Prints manual setup steps (marketplace / extension / plugin path):
python3 scripts/install.py --target claude
python3 scripts/install.py --target cursor
python3 scripts/install.py --target gemini
python3 scripts/install.py --target opencode
```

| Harness | Install path | Reads |
|---|---|---|
| Claude Code | local marketplace: `/plugin marketplace add .` then `/plugin install engineering-team@engineering-team-dev` | `.claude-plugin/`, `agents/*.md`, `skills/` |
| Codex | `install.py --target codex` (file copy) | `.codex-plugin/plugin.json`, `.codex/agents/*.toml`, `skills/` |
| Cursor | add this repo as a local plugin source | `.cursor-plugin/plugin.json`, `agents/*.md`, `skills/` |
| Gemini CLI | `gemini extensions install .` | `gemini-extension.json`, `GEMINI.md`, `AGENTS.md` |
| OpenCode | plugin path in `.opencode/INSTALL.md` | `.opencode/plugins/engineering-team.js` |
| GitHub Copilot | `install.py --target github` (file copy) | `.github/agents/*.md` |

Validate the package first with `python3 scripts/doctor.py` and `npm run validate`. After installation, the skill name is `engineering-team`.

## First Prompt

Start with a prompt that names the skill and the outcome:

```text
Use engineering-team to investigate this regression. Map the repo first, find the owning component, trace the affected contract graph, and propose the smallest safe fix with verification.
```

For implementation work:

```text
Use engineering-team to implement this feature. Do not edit files until the component brief, evidence ledger, and verification plan are clear.
```

For review work:

```text
Use engineering-team to review this branch. Focus on bugs, regressions, missing tests, security risks, and rollout risk.
```

For read-only analysis (no edits):

```text
Use engineering-team in read-only analysis mode to understand this repository. Route to codebase-analysis, map the main components and contracts, and return an evidence-backed report without editing files.
```

Read-only mode changes the edit posture, not the rigor level. A trivial file explanation can be L0, but broad codebase analysis, debugging forensics, performance analysis, security review, migration review, or release planning should be assigned L2-L5 depth according to complexity and risk.

To transfer work to another agent or a fresh session:

```text
Use handoff to summarize this task for a fresh agent. Focus the next session on finishing verification and preparing the PR.
```

## Expected First Outputs

EngineeringTeam should not jump straight into editing. For non-trivial work, expect a short intake/routing note followed by compact artifacts such as a Repo Atlas, Component Brief, Contract Graph, Evidence Ledger, Implementation Gate, and Verification Report when they are relevant. The exact operational checklist is maintained in [`skills/engineering-team/SKILL.md`](../skills/engineering-team/SKILL.md) and linked from [`docs/workflow.md`](workflow.md).

Small tasks may use a lighter path. L0 is reserved for trivial local explanation, simple summary, or obvious one-file inspection with no broad claims.

## Run Ledgers And Memory

For high-risk, forensics, or handoff-heavy work, EngineeringTeam may produce a Run Ledger. The Run Ledger records what happened during one task: route decisions, agents used, evidence, probes, verification, handoff state, and residual risk.

Run Ledgers are not durable memory. During closeout, Context GC extracts memory candidates and promotes only reusable, evidence-backed knowledge into `.engineering-team/memory/`.

## Optional Codex Custom Agents

Codex custom agents can be installed into a project or user config:

```bash
python3 skills/engineering-team/scripts/install-custom-agents.py --scope project --repo .
```

```bash
python3 skills/engineering-team/scripts/install-custom-agents.py --scope user
```

Recommended Codex config:

```toml
[agents]
max_threads = 6
max_depth = 1
```

## How To Tell It Is Working

EngineeringTeam is working when the agent pauses before a non-trivial edit or broad read-only conclusion, names what it knows from the repository, identifies what remains uncertain, and ties the final change or diagnosis to evidence and verification. If it skips that map/gate/verify rhythm, ask it to continue the EngineeringTeam workflow and cite the relevant source paths before proceeding.
