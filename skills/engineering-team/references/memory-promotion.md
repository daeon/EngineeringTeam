# Memory Promotion

Use this reference during Context GC to decide whether Run Ledger findings become durable repo-scoped memory.

Memory is curated advisory context. It is not a session archive, transcript, scratchpad, or raw evidence store.

## Promotion rules

Promote a candidate only when all are true:

- reusable across future EngineeringTeam runs
- evidence-backed with source paths, commands, logs, or generated artifacts
- non-sensitive and safe to keep in the repository
- not a one-off task detail
- not raw log content or private user data
- not speculation disguised as fact
- current source code, tests, and generated outputs do not contradict it

Reject a candidate when any are true:

- useful only for the current task
- based on weak inference or unresolved contradiction
- includes secrets, credentials, private data, tokens, or customer-specific raw logs
- duplicates source code without adding reusable orientation value
- likely to become stale without a clear review trigger

## Target files

| Candidate type | Target memory file |
|---|---|
| repo shape, entry points, commands, generated-code rules | `.engineering-team/memory/repo-atlas.md` |
| component ownership, files, symbols, call paths | `.engineering-team/memory/component-briefs.md` |
| producer/consumer contracts, data shapes, failure modes | `.engineering-team/memory/contracts.md` |
| reusable validation commands, expected results, environment constraints | `.engineering-team/memory/verification.md` |
| recurring pitfalls, stale-context warnings, mitigations | `.engineering-team/memory/gotchas.md` |

## Required metadata

Every promoted memory entry should include:

- Status: `current`, `needs-verification`, or `stale`
- Evidence/source paths
- Origin run, if a Run Ledger exists
- Last verified date
- Confidence: `high`, `medium`, or `low`
- Review trigger: what change should cause re-verification

## Context GC output

Context GC should report candidates with one of these decisions:

| Decision | Meaning |
|---|---|
| promote | update the matching memory file |
| needs-verification | keep only if useful and clearly labeled uncertain |
| reject | do not retain beyond the run |
| defer | user or future agent must inspect before memory update |

Use `templates/memory-candidates.md` for the promotion table.
