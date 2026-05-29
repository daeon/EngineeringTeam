# Output Contracts

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

| Agent | Why not spawned yet | Spawn trigger |
|---|---|---|
```

## Repo Atlas

```md
# Repo Atlas

## System Type
## Main Languages / Frameworks
## Runtime / Build Model
## Main Components
## Entry Points
## Test Surfaces
## Domain Context
## Relevant ADRs
## Generated Code Rules
## Config / Schema Sources
## External Integration Points
## Known High-Risk Areas
## Repo-Specific Instructions
## Build / Test Commands
## Last Verified
```

## Component Brief

```md
# Component Brief

## Relevant Component
## Responsibility
## Important Files
## Relevant Symbols
## Main Call Path
## Related Tests
## Similar Existing Patterns
## Inputs / Outputs
## Side Effects
## Open Questions
## Evidence
```

## Contract Graph

```md
# Contract Graph

| Edge | Producer | Contract / Data Shape | Consumer | Side Effect | Failure Mode | Coverage | Risk |
|---|---|---|---|---|---|---|---|
```

## Evidence Ledger

```md
# Evidence Ledger

| Claim | Evidence | Confidence | Impact |
|---|---|---:|---|
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

## Verification Report

```md
# Verification Report

| Command | Result | Relevant Output | Related? | Next Action |
|---|---|---|---|---|

## Failure Attribution
## Coverage Gaps
## Unverified Risks
```

## Analysis Report (L0 tasks)

```md
# Analysis Report

## What works well

## Key findings

| Finding | Severity | Evidence | Location |
|---|---|---|---|

## Improvement candidates

## Verification performed

## Follow-ups
```

Severity: `high` (correctness, security, trust), `medium` (maintainability, DX), `low` (style, optional). Every finding must reference a file path, line number, command output, or documented behavior. Unverified claims must be labeled as assumptions.

## Final report (L2+ tasks)

```md
## Result

## Agent routing

## Repo mental model

## Focused component

## Contract graph

## Evidence

## Changes

## Verification

## Risks

## Rollback

## Context updates

## Follow-ups
```
