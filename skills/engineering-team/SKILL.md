---
name: engineering-team
description: "Use for non-trivial software engineering: map the repo before edits, classify risk, route the smallest useful EngineeringTeam, trace contract graphs, require evidence, implement safely, verify changes, and preserve reusable repo knowledge."
---

# EngineeringTeam

Use this skill for non-trivial software engineering. Do not rely on it as a giant memory file — load references only when needed.

Invocation: mention `engineering-team` in the prompt, choose it from `/skills`, or let a harness select it based on task type.

## Non-negotiable rule

Move from broad to narrow before editing:

```text
repo map → component map → feature map → contract graph → focused files → change plan → implementation → verification
```

Never edit until the owning component, affected contract, call path, risk level, and verification strategy are clear.

## When to use

Any task involving:

- debugging, regressions, flaky tests, crashes, root-cause analysis
- feature implementation or behavior changes
- refactoring that may alter design, ownership, contracts, or tests
- architecture, APIs, interfaces, module boundaries, dependency direction
- security-sensitive code: trust boundaries, auth, permissions, inputs, secrets, shell/filesystem/network access, dependency risk
- performance: latency, throughput, memory, CPU, IO, caching, batching, polling, locking, concurrency, scalability
- migration, compatibility, legacy behavior, schema/config/API translation, imports/exports, upgrades
- release, rollout, rollback, observability, production behavior, operational risk
- PR or diff review requiring multiple lenses
- codebase audit, analysis, feedback, or improvement planning
- user asks for agents, teams, deliberation, debate, review board, red team, or coordination

## When not to use a full team

- typo, formatting fix, or obvious local edit in one file
- sequential work with no cross-file risk
- user asked only for a concise answer

Perform minimal repo orientation even for small tasks.

## Required mental model

Before implementation, answer:

1. Where does this behavior enter the system?
2. Where is it transformed?
3. Where does it leave?
4. Which contracts and consumers are affected?
5. What evidence supports the diagnosis or design?
6. What proves the change works?

If any answer is unclear, keep mapping.

## Workflow

```text
Task
  → classify risk and autonomy   references/intake-risk.md       ← produce Intake block first, before any tool calls
  → align on intent if needed    references/alignment-audit.md
  → select specialists           references/agent-routing.md
  → build Repo Atlas             references/repo-atlas.md
  → build Component Brief        references/component-brief.md
  → trace Contract Graph         references/contract-graph.md
  → create Evidence Ledger       references/evidence-ledger.md
  → run Advisor Gate if needed   references/advisor-gate.md
  → pass Implementation Gate     references/implementation-gate.md  ← output gate block before any file write
  → implement
  → verify                       references/verification-loop.md
  → GC context                   references/context-garbage-collection.md  ← always required, even with no updates
  → final report                 references/final-report.md        ← use the template, not a PR summary
```

**L0 fast path:** Classify risk → Repo Atlas → Analysis Report → Context GC. Skip agent routing, contract graph, evidence ledger, Advisor Gate, implementation gate, and verification loop. Use Advisor Consultant only at defined risk gates.

## Required artifacts

| Artifact | When required | Reference |
|---|---|---|
| Intake block | All tasks | `references/intake-risk.md` |
| Repo Atlas | L2+ | `references/repo-atlas.md` |
| Component Brief | L2+ | `references/component-brief.md` |
| Contract Graph | L3+ | `references/contract-graph.md` |
| Evidence Ledger | L3+ | `references/evidence-ledger.md` |
| Advisor Decision Receipt | L4+ or gate triggered | `references/advisor-gate.md` |
| Implementation Gate | L2+ | `references/implementation-gate.md` |
| Verification Report | L2+ | `references/verification-loop.md` |
| Analysis Report | L0 only | `references/output-contracts.md` |
| Final Report | L2+ | `references/final-report.md` |

## Load references only when needed

| Need | Load |
|---|---|
| classify task risk and autonomy | `references/intake-risk.md` |
| resolve ambiguous user intent | `references/alignment-audit.md` |
| choose and score specialists | `references/agent-routing.md` |
| map the repository | `references/repo-atlas.md` |
| identify owner and component | `references/component-brief.md` |
| trace behavior and contracts | `references/contract-graph.md` |
| verify claims with evidence | `references/evidence-ledger.md` |
| gate high-risk decisions | `references/advisor-gate.md` |
| decide whether editing is allowed | `references/implementation-gate.md` |
| run and interpret tests | `references/verification-loop.md` |
| preserve durable knowledge | `references/context-garbage-collection.md` |
| write final handoff | `references/final-report.md` |

## Key failure modes

- Editing before understanding the repo
- Fixed-team spawning regardless of task
- Many agents agreeing without independent evidence
- Evidence Skeptic becoming decorative
- Searching only exact user terms
- Fixing symptoms instead of interaction boundaries
- Missing generated-code conventions
- Trusting stale docs over code
- Reporting success without verification
- Skipping the Intake block — it is always required as the routing receipt
- Producing an implementation Final Report for a read-only L0 task
