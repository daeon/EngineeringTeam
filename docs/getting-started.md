# Getting Started

This guide helps you install EngineeringTeam, invoke the skill, and understand the first outputs you should expect.

## Install The Plugin

EngineeringTeam is a single repository that exposes different manifest files for different agent harnesses.

Use the harness-specific install path:

- Claude Code: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
- Codex: `.codex-plugin/plugin.json`
- Cursor: `.cursor-plugin/plugin.json`
- Gemini CLI: `gemini-extension.json`
- OpenCode: `.opencode/plugins/engineering-team.js`

After installation, the skill name is `engineering-team`.

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

## Expected First Outputs

EngineeringTeam should not jump straight into editing. For non-trivial work, expect:

1. Intake and risk classification.
2. Agent or role routing.
3. Repo orientation.
4. Component brief.
5. Contract graph for behavior changes.
6. Evidence ledger.
7. Implementation gate.
8. Verification plan.

Small tasks may use a lighter version of the same flow.

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

EngineeringTeam is working when the agent can answer these questions before editing:

- Where does this behavior enter the system?
- Where is it transformed?
- Where does it leave the system?
- Which contracts and consumers are affected?
- What evidence supports the diagnosis or design?
- What will prove the change works?
- What should not be changed?

If those answers are missing, ask the agent to continue the EngineeringTeam mapping phase before implementation.
