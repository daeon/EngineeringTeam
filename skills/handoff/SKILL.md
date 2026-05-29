---
name: handoff
description: "Use when handing the current task, investigation, plan, branch, or session to another agent or a fresh session. Produces a compact continuation document with decisions, evidence, open questions, artifact links, suggested skills, and next actions."
argument-hint: "What should the next agent or session focus on?"
---

# Handoff

Use this skill when the user wants the current work handed to another agent, subagent, tool harness, or fresh session.

Common triggers: `handoff`, `hand over`, `transfer this task`, `continue in another agent`, `make a continuation brief`, `summarize this for a fresh session`, `delegate this to another agent`, or `pick this up later`.

## Goal

Create a compact handoff document that lets the next agent continue without rereading the full transcript.

Preserve decisions, evidence, artifacts, paths, risks, blockers, and the next concrete move. Do not copy large plans, PRDs, ADRs, issues, commits, diffs, logs, or test output that already exist elsewhere. Reference them by path, URL, branch, commit, issue, or artifact name instead.

## Output location

- If the user gives a path, write the handoff there.
- Otherwise create a temporary path with `mktemp -t handoff-XXXXXX.md`.
- If the handoff should stay with the repo, use `.agent-state/handoffs/<short-task-slug>.md` and create the directory first.
- Read the target file before writing if it already exists or if the command creates an empty file first.
- If file writes are unavailable, output the handoff inline and clearly label it as unsaved.

## Before writing

Collect only the context the next agent needs:

- user intent and the intended next focus
- current repo, branch, PR, issue, or artifact location
- decisions already made
- source paths, symbols, tests, commands, logs, or docs that matter
- what was verified and what remains unverified
- known risks, blockers, contradictions, or assumptions
- skills or specialist agents the next session should use

Do not run broad repo analysis unless the current conversation lacks the minimum context needed for a safe handoff.

## Handoff document template

```md
# Handoff: <task-or-focus>

## Purpose for next agent

<What the next agent/session should accomplish.>

## Current state

<Where the work stands now. Include repo, branch, PR/issue, and whether changes exist.>

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

- <work already done, commands already run, paths already ruled out>
```

## EngineeringTeam-specific handoff

When handing off EngineeringTeam work, include:

- risk level and autonomy mode from the Intake block
- whether the Implementation Gate passed
- affected contracts or consumers
- commands run and verification status
- residual risks and rollback notes
- context GC or memory updates that were made or intentionally skipped

For subagent delegation, include the smallest safe context budget: `brief-only`, `component-context`, `artifact-context`, or `full-context`. Prefer a context capsule over transcript excerpts.

## Completion response

After writing the handoff, reply with:

```md
Created handoff: `<path>`

Use this next:

<one concise prompt the user can paste into the next agent/session>
```
