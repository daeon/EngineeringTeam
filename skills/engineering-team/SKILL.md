---
name: engineering-team
description: "Use for non-trivial software engineering and read-only investigation: act as lead engineer, select the right expert panel, route implementation, codebase analysis, debugging forensics, log forensics, performance forensics, handoff, evidence gates, verification, run ledgers, and reusable repo knowledge."
---

# EngineeringTeam

Lead-engineer workflow for non-trivial software engineering. Keep this file as the router: load the narrow reference you need, build evidence before edits, and avoid treating the skill as long-term memory.

Invocation: mention `engineering-team`, choose it from `/skills`, or let the harness select it.

## Operating modes

| Mode | Use when | Route | Edit posture |
|---|---|---|---|
| Implementation | Fix, change, implement, refactor, add tests, or prepare PR-ready work | Follow the implementation workflow below | Edit only after the Implementation Gate |
| Read-only analysis | Understand, audit, debug, inspect logs, or profile without requested changes | Load `references/analysis-routing.md`; route to `codebase-analysis`, `debugging-forensics`, `log-forensics`, or `performance-forensics` | No edits; still classify L0-L5 risk |

If read-only work reveals a likely fix, stop with a handoff-ready diagnosis unless the user explicitly asks for implementation.

## Non-negotiable rule

Move broad → narrow before editing:

```text
repo map → component map → feature map → contract graph → focused files → change plan → implementation → verification
```

Do not edit until the owning component, affected contract, call path, risk level, and verification strategy are clear.

## When to use

Use for any task involving debugging, behavior changes, refactoring with contract/design/test risk, architecture or APIs, security-sensitive boundaries, performance, migration/compatibility, release/rollback, PR/diff review, codebase audits, or explicit requests for agents/teams/review.

Use a light path for typos, formatting, obvious one-file local edits, sequential low-risk work, or concise answers; still do minimal repo orientation. Use Advisor Consultant only at defined advisor gates, not as routine fan-out.

## Required mental model

Before implementation, know: entry point, transformation point, output boundary, affected contracts/consumers, evidence for the diagnosis or design, and the check that proves the change.

## Workflow

```text
Task
  → classify risk and autonomy   references/intake-risk.md       ← Intake block first
  → align on intent if needed    references/alignment-audit.md
  → select mode/panel            references/analysis-routing.md / references/agent-routing.md
  → create Run Ledger if useful  references/run-ledger.md        ← task trace, not memory
  → build Repo Atlas             references/repo-atlas.md
  → build Component Brief        references/component-brief.md
  → trace Contract Graph         references/contract-graph.md
  → create Evidence Ledger       references/evidence-ledger.md
  → run Advisor Gate if needed   references/advisor-gate.md
  → pass Implementation Gate     references/implementation-gate.md  ← output before writes
  → implement
  → verify                       references/verification-loop.md
  → GC context / memory          references/context-garbage-collection.md / references/memory-promotion.md
  → final report                 references/final-report.md
```

**L0 fast path:** only for trivial local explanation, simple summary, or obvious one-file inspection with no cross-file, behavior, contract, performance, security, migration, release, or production claim. Use classify risk → lightweight Repo Atlas → Analysis Report → Context GC; skip panel routing, contract graph, evidence ledger, Advisor Gate, Implementation Gate, and verification loop unless needed.

## Run Ledger and memory

Use `references/run-ledger.md` for L3+, read-only forensics, handoff-heavy work, or any run needing a reviewable trace of route decisions, probes, verification, residual risk, or memory candidates. A Run Ledger may feed curated memory candidates; it is not memory.

When `.engineering-team/memory/index.md` exists, read it before EngineeringTeam work. During closeout, use `references/memory-promotion.md` and `templates/memory-candidates.md` before updating `.engineering-team/memory/`. Promote only reusable, evidence-backed knowledge; never store secrets, private data, temporary logs, or speculation.

## Required artifacts

| Artifact | When required | Reference |
|---|---|---|
| Intake block | All tasks | `references/intake-risk.md` |
| Run Ledger | L3+, forensics, handoff-heavy, reviewer trace | `references/run-ledger.md` |
| Repo Atlas | L2+ | `references/repo-atlas.md` |
| Component Brief | L2+ | `references/component-brief.md` |
| Contract Graph | L3+ | `references/contract-graph.md` |
| Evidence Ledger | L3+ | `references/evidence-ledger.md` |
| Advisor Decision Receipt | L4+ or gate trigger | `references/advisor-gate.md` |
| Impact Map | L4+ multi-component | `references/impact-map.md` |
| Implementation Gate | L2+ | `references/implementation-gate.md` |
| Verification Report | L2+ | `references/verification-loop.md` |
| Analysis Report | L0 only | `references/output-contracts.md` |
| Memory Candidates | Reusable closeout knowledge | `templates/memory-candidates.md` / `references/memory-promotion.md` |
| Final Report | L2+ | `references/final-report.md` |

## Load references only when needed

| Need | Load |
|---|---|
| classify risk/autonomy | `references/intake-risk.md` |
| resolve ambiguous intent | `references/alignment-audit.md` |
| choose read-only route | `references/analysis-routing.md` |
| choose/score specialists | `references/agent-routing.md`, `references/role-definitions.md`, `references/routing-examples.md`, `references/routing-evals.md` |
| trace run state | `references/run-ledger.md` |
| map repo/component/contracts/evidence | `references/repo-atlas.md`, `references/component-brief.md`, `references/contract-graph.md`, `references/evidence-ledger.md` |
| scope L4+ impact | `references/impact-map.md` |
| gate decisions/edits | `references/advisor-gate.md`, `references/implementation-gate.md` |
| diagnose or test | `references/diagnosis-loop.md`, `references/tdd-discipline.md`, `references/verification-loop.md`, `references/failure-attribution.md` |
| close out | `references/context-garbage-collection.md`, `references/memory-promotion.md`, `references/final-report.md` |
| special context | `references/visual-review-reports.md`, `references/domain-context.md`, `references/codex-compatibility.md`, `references/subagent-context-policy.md`, `handoff` skill (`skills/handoff/SKILL.md`) |

When work is broad, noisy, or specialist-heavy, delegate with `references/subagent-context-policy.md`; subagents return context capsules, not transcripts.

## Key failure modes

- Editing before repo/component/contract understanding.
- Spawning a fixed team instead of routing by risk and evidence.
- Letting Evidence Skeptic become decorative.
- Searching only exact user terms or trusting stale docs over code.
- Fixing symptoms instead of interaction boundaries.
- Missing generated-code conventions.
- Reporting success without behavior-relevant verification.
- Treating read-only mode as automatically L0 or editing during read-only analysis.
- Treating Run Ledgers as durable memory instead of promoting curated memory candidates.
