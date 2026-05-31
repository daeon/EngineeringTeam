---
name: handoff
description: "Use when handing the current task, investigation, plan, branch, or session to another agent or a fresh session. Produces a compact continuation document with decisions, evidence, open questions, artifact links, suggested skills, and next actions."
argument-hint: "What should the next agent or session focus on?"
---

# Handoff

Use when the user wants work handed to another agent, tool harness, or fresh session (`handoff`, `hand over`, `continue elsewhere`, `delegate`, `pick this up later`).

## Default posture

Preserve and compress existing context; do not broaden scope, investigate unrelated areas, edit implementation files, or create durable memory unless the user explicitly requests that work. Prefer references to existing artifacts over copying long content.

## Goal

Create a compact continuation document with decisions, evidence, artifact links, risks, blockers, and the next concrete move. Reference existing plans, PRDs, ADRs, issues, commits, diffs, logs, or test output by path/URL/branch/commit instead of copying them.

## Output location

- Use the path the user gives.
- Otherwise create `mktemp -t handoff-XXXXXX.md`.
- For repo-local handoffs, use `.agent-state/handoffs/<short-task-slug>.md`.
- Read an existing target before overwriting; if writes are unavailable, output the handoff inline and mark it unsaved.

## Workflow

1. Identify the target audience, destination path, and intended next focus.
2. Collect only the context the next agent needs.
3. Prefer links to existing artifacts, paths, commits, issues, commands, and verification output over transcript excerpts.
4. Write or return the handoff using the template below.
5. Finish with the completion response and one concise continuation prompt.

## Before writing

Collect only continuation-critical context: user intent, repo/branch/PR/issue/artifact location, decisions, relevant paths/symbols/tests/commands/logs/docs, verified and unverified claims, risks/blockers/assumptions, and suggested skills or specialist agents. Do not run broad repo analysis unless the conversation lacks safe minimum context.

## Handoff document template

```md
# Handoff: <task-or-focus>

## Purpose for next agent
<What the next agent/session should accomplish.>

## Current state
<Repo, branch, PR/issue, artifacts, and whether changes exist.>

## Decisions made
- <Decision> — <reason/evidence>

## Relevant artifacts
| Artifact | Why it matters |
|---|---|
| `<path-or-url>` | <short reason> |

## Files and symbols worth keeping in context
- `<path>`: <why it matters>

## Evidence and confidence
| Claim | Evidence | Confidence |
|---|---|---:|
| <claim> | <path/command/log/artifact> | <High/Medium/Low> |

## Open questions / blockers
- <question or blocker>

## Risks / failure modes
- <risk and how to avoid it>

## Suggested skills / agents
- `<skill-or-agent>`: <why>

## Next actions
1. <first concrete step>
2. <second concrete step>
3. <verification or stopping condition>

## Do not repeat
- <work already done or ruled out>
```

## EngineeringTeam-specific handoff

Include risk level/autonomy, Implementation Gate status, affected contracts/consumers, commands and verification status, residual risks/rollback notes, and context-GC or memory-update decisions. For subagent delegation, include the smallest safe context budget (`brief-only`, `component-context`, `artifact-context`, or `full-context`) and prefer a context capsule over transcript excerpts.

## Required output

A compact handoff document saved to the selected path or returned inline, plus a completion response that names the handoff location and gives one ready-to-paste continuation prompt. The handoff must include decisions, evidence, open questions, risks, relevant artifacts, and concrete next actions.

## Completion response

Reply with the created path and one concise prompt the user can paste into the next agent/session.
