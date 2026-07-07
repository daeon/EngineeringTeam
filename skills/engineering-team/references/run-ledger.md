# Run Ledger

Use this reference when a task needs a compact, reviewable trace of how EngineeringTeam handled the run.

The Run Ledger is task-scoped evidence, not durable memory. It records what happened during one investigation or implementation so reviewers and future agents can understand the route, claims, probes, decisions, verification, and remaining risk.

When unknowns-first phases run, record only the useful outputs here: route decision, blind spots, assumptions, probes, material deviations, skipped checks, and residual risk. Do not paste phase templates wholesale.

## When to create it

Create a Run Ledger proportionally:

| Risk / mode | Run Ledger expectation |
|---|---|
| L0 obvious local task | Optional or tiny final summary only |
| L1-L2 bounded task | Route decision, evidence summary, memory candidates |
| L3-L5 risky task | Full Run Ledger using `templates/run-ledger.md` |
| Read-only debugging, logs, or performance forensics | Full enough to preserve hypotheses, probes, evidence, and next action |
| Handoff-heavy work | Full enough for another agent to resume safely |

Do not create large transcript dumps. Capture compact facts, links, commands, outcomes, assumptions, and risks.

## Separation from memory

Run Ledger entries answer: what happened in this run?

Memory entries answer: what reusable repo knowledge should future runs start from?

Keep them separate:

- Store task-scoped traces under `.engineering-team/runs/` only when the user or harness wants persisted run artifacts.
- Store durable reusable knowledge under `.engineering-team/memory/` only after Context GC and memory promotion.
- Do not put raw logs, failed hypotheses, temporary paths, private data, secrets, or one-off decisions into memory.

## Required sections

Use `templates/run-ledger.md` for full runs. At minimum, record:

- task and mode / route decision
- optional unknowns-first phase used and why
- agents or skills used
- files, commands, logs, or artifacts inspected
- claims with evidence and confidence
- hypotheses and probes, if applicable
- edits and verification, if implementation happened
- handoff state and residual risk
- memory candidates, not direct memory writes

## Promotion handoff

At Context GC, copy only reusable, evidence-backed items into `templates/memory-candidates.md` and apply `references/memory-promotion.md` before updating `.engineering-team/memory/`.
