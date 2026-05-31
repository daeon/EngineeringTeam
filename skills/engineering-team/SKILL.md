---
name: engineering-team
description: "Use for non-trivial software engineering and read-only investigation: route implementation, codebase analysis, debugging forensics, log forensics, performance forensics, handoff, evidence gates, verification, run ledgers, and reusable repo knowledge."
---

# EngineeringTeam

Use this skill for non-trivial software engineering. Do not rely on it as a giant memory file — load references only when needed.

Invocation: mention `engineering-team` in the prompt, choose it from `/skills`, or let a harness select it based on task type.


## Two operating modes

EngineeringTeam is the main router for two broad modes:

| Mode | Use when | Route | Edit posture |
|---|---|---|---|
| Implementation mode | The user asks to fix, change, implement, refactor, add tests, or prepare PR-ready work | Follow the existing EngineeringTeam implementation workflow | Edits only after the Implementation Gate |
| Read-only analysis mode | The user asks to analyze, understand, investigate, debug, inspect logs, or profile performance without requesting changes | Load `references/analysis-routing.md` and route to `codebase-analysis`, `debugging-forensics`, `log-forensics`, or `performance-forensics` | No file edits; still assign L0-L5 depth by complexity and risk |

If a read-only investigation finds a likely fix, stop at a handoff-ready diagnosis unless the user explicitly asks for implementation.

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
  → select mode and specialists  references/analysis-routing.md / references/agent-routing.md
  → create Run Ledger if useful  references/run-ledger.md        ← task-scoped trace; not durable memory
  → build Repo Atlas             references/repo-atlas.md
  → build Component Brief        references/component-brief.md
  → trace Contract Graph         references/contract-graph.md
  → create Evidence Ledger       references/evidence-ledger.md
  → run Advisor Gate if needed   references/advisor-gate.md
  → pass Implementation Gate     references/implementation-gate.md  ← output gate block before any file write
  → implement
  → verify                       references/verification-loop.md
  → GC context                   references/context-garbage-collection.md / references/memory-promotion.md
  → final report                 references/final-report.md        ← use the template, not a PR summary
```

**L0 fast path:** Use only for trivial local explanation, simple summary, or obvious one-file inspection with no cross-file, behavior, contract, performance, security, migration, release, or production claims. Classify read-only investigations by depth; read-only does not automatically mean L0. L0 uses Classify risk → lightweight Repo Atlas → Analysis Report → Context GC. Skip agent routing, contract graph, evidence ledger, Advisor Gate, implementation gate, and verification loop. Use Advisor Consultant only at defined risk gates.

## Run Ledger and project-scoped memory

Use `references/run-ledger.md` for task-scoped traceability when a run needs reviewable evidence of route decisions, agents/skills used, probes, verification, handoff state, or residual risk. A Run Ledger may feed memory candidates, but it is not memory.

When `.engineering-team/memory/index.md` exists, read it before EngineeringTeam work to discover advisory repo memory. During Context GC / session closeout, use `references/memory-promotion.md` and `templates/memory-candidates.md` before updating files under `.engineering-team/memory/`. Promote only reusable, evidence-backed knowledge. Current source code, tests, and generated outputs always win over memory. Do not store secrets, credentials, private user information, temporary logs, or speculation. Every durable memory entry should include evidence/source paths, origin run when available, confidence, and review trigger.

## Required artifacts

| Artifact | When required | Reference |
|---|---|---|
| Intake block | All tasks | `references/intake-risk.md` |
| Run Ledger | L3+, read-only forensics, handoff-heavy, or reviewer-visible trace needed | `references/run-ledger.md` |
| Repo Atlas | L2+ | `references/repo-atlas.md` |
| Component Brief | L2+ | `references/component-brief.md` |
| Contract Graph | L3+ | `references/contract-graph.md` |
| Evidence Ledger | L3+ | `references/evidence-ledger.md` |
| Advisor Decision Receipt | L4+ or gate triggered | `references/advisor-gate.md` |
| Impact Map | L4+ multi-component change | `references/impact-map.md` |
| Implementation Gate | L2+ | `references/implementation-gate.md` |
| Verification Report | L2+ | `references/verification-loop.md` |
| Analysis Report | L0 only | `references/output-contracts.md` |
| Memory Candidates | When Context GC identifies reusable knowledge | `templates/memory-candidates.md` / `references/memory-promotion.md` |
| Final Report | L2+ | `references/final-report.md` |

When work is broad, noisy, or specialist-heavy, delegate using `references/subagent-context-policy.md`; subagents must return context capsules, not transcripts.

## Load references only when needed

| Need | Load |
|---|---|
| classify task risk and autonomy | `references/intake-risk.md` |
| resolve ambiguous user intent | `references/alignment-audit.md` |
| choose analysis vs implementation route | `references/analysis-routing.md` |
| choose and score specialists | `references/agent-routing.md` |
| understand each specialist's role and boundary | `references/role-definitions.md` |
| see worked routing examples | `references/routing-examples.md` |
| self-check routing decisions | `references/routing-evals.md` |
| keep a reviewable run trace | `references/run-ledger.md` |
| map the repository | `references/repo-atlas.md` |
| identify owner and component | `references/component-brief.md` |
| trace behavior and contracts | `references/contract-graph.md` |
| scope a multi-component (L4+) change | `references/impact-map.md` |
| verify claims with evidence | `references/evidence-ledger.md` |
| gate high-risk decisions | `references/advisor-gate.md` |
| decide whether editing is allowed | `references/implementation-gate.md` |
| run and interpret tests | `references/verification-loop.md` |
| build a fast bug/regression repro loop | `references/diagnosis-loop.md` |
| write behavior-first tests (tracer bullets) | `references/tdd-discipline.md` |
| preserve durable knowledge | `references/context-garbage-collection.md` / `references/memory-promotion.md` |
| write the session final report (L2+) | `references/final-report.md` |
| produce a visual HTML review report | `references/visual-review-reports.md` |
| capture domain and business context | `references/domain-context.md` |
| work within Codex constraints | `references/codex-compatibility.md` |
| hand off work to another agent or a fresh session | `handoff` skill (`skills/handoff/SKILL.md`) |
| delegate context-heavy work | `references/subagent-context-policy.md` |

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
- Treating read-only mode as automatic L0 instead of assigning L0-L5 depth by complexity and risk
- Editing during read-only analysis instead of returning a diagnosis, report, or next-probe plan
- Treating Run Ledger artifacts as durable memory instead of promoting only curated memory candidates
