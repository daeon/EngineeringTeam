# Context Budget Modes

Use this reference when selecting EngineeringTeam depth, subagent fan-out, and artifact scope. The goal is to make context spend intentional instead of letting every task expand into full forensics.

## Mode table

| Mode | Typical depth | Use when | Context posture | Required proof |
|---|---:|---|---|---|
| lean | L0-L1 | local explanation, typo, obvious one-file change | minimal lookup and local inspection | cite the inspected file or explain local basis |
| balanced | L2-L3 | normal feature, bug, refactor, or repo analysis | brain-first lookup, focused atlas, component brief, evidence-backed plan | relevant source/test/docs evidence |
| deep | L4-L5 | multi-component, protected boundary, migration, release, architecture, high-risk PR | full repo/component/contract/evidence/impact path | contract graph, impact map when needed, verification strategy |
| forensics | L3-L5 | debugging, log analysis, performance, flaky behavior, production-like failures | hypothesis matrix, probes, evidence ledger, run ledger | falsifiable probes and failure attribution |
| handoff | L2-L5 | transfer to another session or agent | compress decisions, evidence, risks, next actions | continuation-ready state and open gaps |

## Selection rules

- Start lean only when no cross-file behavior, contract, performance, security, migration, release, or production claim is involved.
- Escalate to balanced when the task needs repo orientation or a behavior-changing edit.
- Escalate to deep when multiple components, public contracts, generated files, migrations, security boundaries, releases, or rollback risk are involved.
- Use forensics when the task is about why something failed, not just what to change.
- Use handoff when the most important output is continuity rather than a patch.

## Artifact expectations

| Mode | Minimum artifacts |
|---|---|
| lean | Intake note, lightweight source basis, Analysis Report when read-only |
| balanced | Brain-First Lookup, Repo Atlas, Component Brief, Evidence, Implementation Gate or read-only report, Verification, Gap Analysis |
| deep | Balanced artifacts plus Contract Graph, Impact Map when multi-component, Advisor Decision Receipt when triggered, Run Ledger |
| forensics | Brain-First Lookup, Run Ledger, hypothesis matrix, probes, Evidence Ledger, Failure Attribution, Gap Analysis |
| handoff | Handoff document, Run Ledger if available, Gap Analysis, Memory Candidates |

## Token discipline

- Load narrow references only when needed.
- Delegate noisy search or large logs to subagents that return compact context capsules.
- Prefer source paths, symbols, and command summaries over pasted transcripts.
- Keep raw logs out of memory; keep reusable findings as memory candidates.
- Report when deeper inspection was intentionally not done and why.

## Escalation triggers

Escalate the context budget when any of these appear:

- unclear owner or call path
- contradictory evidence
- stale or missing memory that affects the conclusion
- public API or persisted data contract
- generated-code convention
- security, privacy, auth, or permission boundary
- performance, concurrency, memory, or IO risk
- migration, compatibility, release, rollback, or production blast radius
