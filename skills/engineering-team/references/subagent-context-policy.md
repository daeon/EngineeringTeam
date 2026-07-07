# Subagent Context Policy

Use subagents to protect the main session from broad, noisy, or specialist-heavy work.

## Canonical delegation anchors

This file owns the reusable subagent rules for main/subagent ownership, delegation triggers, context budgets, and context capsules. Other routing references should link here instead of restating those rules.

## Main agent owns

- user intent
- task classification
- risk mode
- current plan
- implementation gate
- final decision
- final report
- context garbage collection

## Subagents own

- bounded investigation
- broad search
- test/build execution
- log summarization
- focused specialist critique
- independent falsification
- narrow verification checks

## Delegate when

- more than 5 files may be relevant
- ownership is unknown
- the same term appears in multiple components
- generated code may be involved
- public API, config, schema, or contract boundary may be touched
- command output, logs, or test failures may be long
- a specialist needs different tool permissions
- the work is read-only and self-contained
- independent areas can be inspected in parallel

For L2+ EngineeringTeam work on a harness with subagent support, the selected specialist panel is mandatory. The triggers above determine which specialists to spawn, not whether delegation is allowed.

## Fallback when

- the task is tiny and local
- user intent requires back-and-forth
- implementation needs continuous shared context
- same-file edit conflicts are likely
- the harness has no subagent support
- custom-agent definitions are unavailable
- spawning fails or is blocked by tool/safety constraints

## Context budgets

Every subagent receives one of:

| Budget | Use for | Contents |
|---|---|---|
| `brief-only` | advisor, skeptic, narrow review | task brief + decision needed |
| `component-context` | focused investigation | component brief + relevant paths/symbols |
| `artifact-context` | multi-step review or verification | repo atlas + component brief + contract graph + evidence ledger |
| `full-context` | rare fallback | only when a compact brief is unsafe; state why |

Default to the smallest useful context budget.

## Hard rule

Subagents return context capsules, not transcripts.

The main agent should not ingest full logs, full test output, raw search dumps, or broad file summaries unless the capsule is insufficient.
