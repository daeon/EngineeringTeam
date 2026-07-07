# Output Contracts

Agent-level report formats. For phase artifact templates, see the dedicated reference files.

## Agent selection report

```md
## Task classification

- Primary task type:
- Secondary task types:
- Risk dimensions:
- Autonomy level:

## Alignment

- Resolved decisions:
- Recommended defaults accepted:
- Open user decisions:
- Acceptance criteria:
- Non-goals:
- Repo-answerable questions checked:

## Selected agents

| Agent | Score | Reason | Initial question |
|---|---:|---|---|

## Deferred agents

| Agent | Why deferred | Spawn trigger |
|---|---|---|

## Fallbacks

| Role | Reason subagent was not spawned | Compensating check |
|---|---|---|
```

## Individual agent report

```md
## Findings

## Evidence

## Assumptions

## Risks

## Recommended next action

## What should not change
```

## Evidence skeptic report

```md
## Accepted evidence

## Rejected claims

## Unproven assumptions

## Contradictions

## Required checks

## Highest-risk failure mode

## Recommendation
```

## Analysis Report (L0 evaluative tasks)

L0 has two deliverables; pick by intent:

| L0 intent | Deliverable | Canonical template |
|---|---|---|
| Evaluative: audit, feedback, "what could be improved", risk/PR review | Analysis Report | `templates/analysis-report.md` |
| Descriptive: "understand / map how this repo works" | Codebase Analysis Report | `templates/codebase-analysis-report.md` (via the `codebase-analysis` skill) |

Use the templates above as the single source of truth — do not redefine the report shape here. Severity for Analysis Report findings: `high` (correctness, security, trust), `medium` (maintainability, DX), `low` (style, optional). Every finding must reference a file path, line number, command output, or documented behavior. Unverified claims must be labeled as assumptions.

## Phase artifact templates

| Artifact | Canonical reference |
|---|---|
| Unknowns-first route | `references/unknowns-first/router.md` |
| Unknowns-first phase outputs | Map into the existing artifacts below; do not create a parallel report family. |
| Repo Atlas | `references/repo-atlas.md` |
| Component Brief | `references/component-brief.md` |
| Contract Graph | `references/contract-graph.md` |
| Evidence Ledger | `references/evidence-ledger.md` |
| Verification Report | `references/verification-loop.md` |
| Advisor Decision Receipt | `references/advisor-gate.md` |
| Final Report (L2+) | `references/final-report.md` |
