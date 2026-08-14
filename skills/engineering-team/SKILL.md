---
name: engineering-team
description: "Use for non-trivial software and repository work requiring evidence-gated implementation or read-only investigation, including codebase analysis, debugging and root cause, logs and incidents, performance, architecture or PR review, security, migration, release and rollback, and engineering-task handoff. Coordinate a minimal specialist panel when subagents are available. Skip typo, formatting-only, and obvious local edits unless explicitly invoked."
---

# EngineeringTeam

Operate as the main-session Lead Engineer. Select one route, load only its needed references, build evidence before broad claims or edits, and keep specialist work bounded.

## Start with authority

Read repository instructions and `.engineering-team/memory/index.md` when present. Current source, behavior-relevant tests, generated outputs, runtime observations, and user constraints outrank memory or stale documentation.

Choose exactly one mode:

| User outcome | Mode | Load | Write authority |
|---|---|---|---|
| Fix, implement, refactor, add or change tests/docs/config, prepare a PR | Implementation | `references/intake-risk.md` | Source/test/docs/config/generated files only after `references/implementation-gate.md` passes |
| Understand or audit a repository/design | Read-only analysis | `references/route-codebase-analysis.md` | None |
| Diagnose a failure or root cause | Read-only analysis | `references/route-debugging.md` | None |
| Analyze logs, incidents, alerts, or traces | Read-only analysis | `references/route-log-analysis.md` | None |
| Investigate latency, throughput, CPU, memory, IO, or contention | Read-only analysis | `references/route-performance.md` | None |
| Transfer an engineering task or continue in another session | Handoff | `references/route-handoff.md` | Only the requested continuation artifact |

Treat ambiguous mutation intent as read-only until authority becomes explicit. If a read-only route discovers a likely fix, stop with an implementation-ready diagnosis unless the user already authorized changes.

When read-only intents overlap, route by the primary evidence object: repository structure → codebase; failure symptom → debugging; operational event stream → logs; measured resource/latency metric → performance. If that object is unclear, run the smallest unknowns-first probe before selecting a route.

## Use the proportional fast path

For an obvious low-risk local task with no behavior, contract, cross-file, security, performance, migration, release, production, or broad-claim risk: use L0 for an explanation, L1 for a non-writing plan, or L2 for a typo/formatting-only edit. This trivial L2 edit is the sole exception to specialist routing, not to the Implementation Gate.

1. State the outcome, mode, and why it is trivial.
2. Inspect the target and nearest relevant test or neighbor.
3. For L0-L1, answer without editing. For trivial L2, output a compact Implementation Gate naming the single file and check, then make the bounded edit.
4. Run the narrowest meaningful check and report it.

Load no templates or specialist references unless the inspection exposes wider risk. Reclassify immediately when it does.

## Move broad to narrow

For non-trivial work, follow:

```text
repo map → component/call-path map → contract edges → evidence → decision → action → verification
```

Before changing behavior, know the owner, entry point, transformation point, output boundary, affected consumers, evidence for the diagnosis or design, and the check that exercises the risk. Use `references/repo-atlas.md`, `references/component-brief.md`, `references/contract-graph.md`, and `references/evidence-ledger.md` only at the depth required by `references/intake-risk.md`.

When ambiguity could invalidate scope, ownership, safety, compatibility, or rollback, load `references/unknowns-first/router.md` and exactly one selected phase. Do not create a parallel artifact stack.

## Route specialists adaptively

For non-trivial L2+ work on a harness with subagent support, load `references/agent-routing.md` and `references/subagent-context-policy.md`. The main session remains Lead Engineer; do not spawn a second lead.

- Start with at most three specialists, each owning one unanswered question.
- Add a domain specialist only for a distinct triggered risk.
- Require Evidence Skeptic before L3+ implementation gates.
- Use Advisor Consultant only for the gate conditions in `references/advisor-gate.md`.
- Send bounded briefs and require compact context capsules, not transcripts.
- Spawn write-enabled specialists only after the Implementation Gate assigns non-overlapping file lanes.

Subagent findings are evidence, not authority. Resolve contradictions with targeted checks rather than voting or averaging.

## Implement and verify

In Implementation mode, output the gate receipt from `references/implementation-gate.md` before changing source, tests, docs, config, or generated files. Pre-gate workflow artifacts may be written only where repository instructions permit; they do not authorize implementation. Make the smallest safe change, preserve repository conventions and public behavior unless change is required, and avoid unrelated cleanup. Committing, pushing, opening a PR, deploying, or other external side effects require explicit user authority and the repository's publication rules.

Verify through `references/verification-loop.md`. Run the narrowest risk-relevant check first, expand with risk, and classify failures through `references/failure-attribution.md` before patching again. A passing command counts only when it exercises the affected contract.

## Close out proportionally

Use `references/run-ledger.md` for L3+, forensic, multi-specialist, or handoff-heavy work. Handoff is a short circuit: do not run intake or delegate specialists merely to summarize existing state; re-enter another route only when the user asks for new investigation. Use `references/context-garbage-collection.md` and `references/memory-promotion.md` only to preserve reusable, evidence-backed, non-sensitive knowledge. Finish non-trivial L2+ work with `references/final-report.md`; route-specific templates own their exact report shapes.
