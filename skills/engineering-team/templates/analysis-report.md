# Analysis Report

Canonical deliverable for L0 evaluative tasks: audits, feedback requests,
"what could be improved", risk reviews, and PR/diff reviews that produce
findings only. Replaces the Final Report when no code edits are planned.
Produce it after a lightweight Repo Atlas, then run Context GC.

For descriptive "understand/map how this repo works" requests, use the
Codebase Analysis Report (`templates/codebase-analysis-report.md`) via the
`codebase-analysis` skill instead.

House style: keep tables compact and evidence-first. Prefer columns ordered as
`Item/Claim`, `Evidence`, `Confidence`, `Risk/Impact`, then `Next action`.
Use `Proven`, `Plausible`, or `Assumption` for confidence unless a template
requires a different scale.

Every finding must reference a file path, line number, command output, or
documented behavior. Label unverified claims as assumptions.

> Anti-pattern: listing vague impressions with no evidence, or mixing in an
> implementation plan that belongs in an L2+ Final Report.

## Scope

| Item | Evidence | Confidence | Risk / impact | Next action |
|---|---|---:|---|---|
| Question / review target |  |  |  |  |
| Non-goals |  |  |  |  |
| Files or components inspected |  |  |  |  |

## What works well

| Observation | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  |  |  | Preserve / reuse |

## Key findings

| Finding | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  | Proven / Plausible / Assumption | High / Medium / Low |  |

<!-- Impact: High = correctness / security / trust; Medium = maintainability / DX; Low = style / optional. -->

## Improvement candidates

| Candidate | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  |  |  |  |

## Verification performed

| Check | Evidence | Confidence | Result / risk | Next action |
|---|---|---:|---|---|
|  | Command: `` |  | Pass / Fail / Not run |  |

## Residual risk

| Risk | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  |  |  |  |

## Follow-ups

| Follow-up | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  |  |  |  |
