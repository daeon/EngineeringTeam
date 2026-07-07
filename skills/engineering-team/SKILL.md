---
name: engineering-team
description: "Use for software work with real risk or breadth: multi-file or behavior/contract changes, unknown root causes, security/performance/migration/release concerns, PR-level review, or whole-repo investigation. Acts as lead engineer: selects a minimal expert panel, builds evidence, gates edits, verifies. Skip for typo-level or obvious single-file edits."
---

# EngineeringTeam

Lead-engineer workflow for non-trivial software engineering. Keep this file as the router: load the narrow reference you need, build evidence before edits, and avoid treating the skill as long-term memory.

Invocation: mention `engineering-team`, choose it from `/skills`, or let the harness select it.

## Decide the route (in order)

1. **Trivial?** Single known file, no behavior, contract, cross-file, security, performance, migration, release, or production claim → take the fast path below. Load no reference files.
2. **Unknowns-first needed?** For non-trivial ambiguous, risky, unfamiliar, architecture-sensitive, security-sensitive, production-impacting, or assumption-heavy work, load `references/unknowns-first/router.md` and only the smallest useful phase it selects. Skip this layer for tiny obvious edits.
3. **Outcome?** Change code → Implementation mode. Understand, audit, debug, inspect logs, or profile without requested changes → Read-only analysis: load `references/analysis-routing.md` and route to `codebase-analysis`, `debugging-forensics`, `log-forensics`, or `performance-forensics`. Transfer the task elsewhere → `handoff` skill.
4. **Depth?** Classify L0-L5 and risk mode with `references/intake-risk.md`. Read-only work is classified by depth, not edit posture. Unknowns-first can inform the intake, but `references/intake-risk.md` owns the final autonomy and risk decision.
5. **Load only what that depth requires** — the artifact table below maps depth to references. Do not preload the rest.

In Implementation mode, edit only after the gate in `references/implementation-gate.md` passes. In read-only mode, never edit; if the work reveals a likely fix, stop with a handoff-ready diagnosis unless the user explicitly asks for implementation.

## Fast path (L0-L1)

For trivial work, the entire process is:

1. State a one-line intake: task, mode, level, and why it is trivial.
2. Orient minimally (the file and its nearest neighbors or tests).
3. Answer, or make the small edit and run the narrowest relevant check.
4. State what you checked. Stop.

No panel, no reference loads, no templates. If step 2 surfaces a cross-file, behavior, or contract claim, reclassify at L2+ and continue below.

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
  → optional unknowns-first   references/unknowns-first/router.md
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

L0-L1 work uses the fast path above instead of this workflow.

## Run Ledger and memory

Use `references/run-ledger.md` for L3+, read-only forensics, handoff-heavy work, or any run needing a reviewable trace of route decisions, probes, verification, residual risk, or memory candidates. A Run Ledger may feed curated memory candidates; it is not memory.

When `.engineering-team/memory/index.md` exists, read it before EngineeringTeam work. During closeout, use `references/memory-promotion.md` and `templates/memory-candidates.md` before updating `.engineering-team/memory/`. Promote only reusable, evidence-backed knowledge; never store secrets, private data, temporary logs, or speculation.

## Required artifacts

| Artifact | When required | Reference |
|---|---|---|
| Intake block | L2+ (one-line form on the fast path) | `references/intake-risk.md` |
| Unknowns-first route | Optional for ambiguous/risky/assumption-heavy work | `references/unknowns-first/router.md` |
| Run Ledger | L3+, forensics, handoff-heavy, reviewer trace | `references/run-ledger.md` |
| Repo Atlas | L2+ | `references/repo-atlas.md` |
| Component Brief | L2+ | `references/component-brief.md` |
| Contract Graph | L3+ | `references/contract-graph.md` |
| Evidence Ledger | L3+ | `references/evidence-ledger.md` |
| Advisor Decision Receipt | L4+ or gate trigger | `references/advisor-gate.md` |
| Impact Map | L4+ multi-component | `references/impact-map.md` |
| Implementation Gate | L2+ | `references/implementation-gate.md` |
| Verification Report | L2+ | `references/verification-loop.md` |
| Analysis Report | L0-L1 read-only answers that need structure | `references/output-contracts.md` |
| Memory Candidates | Reusable closeout knowledge | `templates/memory-candidates.md` / `references/memory-promotion.md` |
| Final Report | L2+ | `references/final-report.md` |

## Load references only when needed

| Need | Load |
|---|---|
| classify risk/autonomy | `references/intake-risk.md` |
| expose ambiguity before intake | `references/unknowns-first/router.md`, then one selected unknowns-first phase reference |
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

For L2+ work on a harness with subagent support, delegate the selected specialist panel with `references/subagent-context-policy.md`; subagents return context capsules, not transcripts. Use fallback simulation only when subagents are unavailable or fail to spawn.

## Key failure modes

- Editing before repo/component/contract understanding.
- Skipping subagent routing for L2+ work on a harness that supports it.
- Spawning a fixed team instead of routing by risk and evidence.
- Letting Evidence Skeptic become decorative.
- Searching only exact user terms or trusting stale docs over code.
- Fixing symptoms instead of interaction boundaries.
- Missing generated-code conventions.
- Reporting success without behavior-relevant verification.
- Treating read-only mode as automatically L0 or editing during read-only analysis.
- Treating Run Ledgers as durable memory instead of promoting curated memory candidates.
