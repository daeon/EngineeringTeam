# Gap Analysis

Use this reference near verification, final reporting, and Context GC to make unknowns explicit. A gap is not a failure; it is an unverified claim, missing proof, stale memory, contradiction, or untested risk that should not be hidden inside prose.

## When to produce it

Produce gap analysis for L2+ final reports, failed or partial verification, read-only investigations, handoffs, stale memory findings, and any task where the conclusion depends on incomplete evidence.

For L0 tasks, include a one-line gap note only when a material unknown remains.

## Gap types

| Type | Meaning |
|---|---|
| missing-evidence | A claim lacks source, test, log, command, or artifact support |
| stale-memory | Repo memory exists but needs re-verification |
| contradiction | Sources disagree, such as docs vs code or memory vs tests |
| coverage-gap | Verification does not exercise the affected behavior |
| environment-gap | Required dependency, service, fixture, permission, or platform is unavailable |
| scope-gap | Related component or consumer was not inspected |
| rollback-gap | Safe rollback, abandon condition, or blast radius is unclear |
| security-gap | Protected boundary, secret handling, auth, privacy, or abuse risk is unresolved |
| performance-gap | Measurement frame, baseline, hot path, or regression proof is incomplete |

## Artifact: Gap Analysis

```md
# Gap Analysis

| Gap | Type | Evidence / reason | Risk | Next probe | Owner |
|---|---|---|---|---|---|
|  | missing-evidence / stale-memory / contradiction / coverage-gap / environment-gap / scope-gap / rollback-gap / security-gap / performance-gap |  | low / medium / high |  | agent / user / maintainer |
```

## Rules

- Prefer concrete next probes over vague follow-ups.
- Do not classify a gap as low risk just because it is inconvenient to check.
- Do not let stale memory silently pass as evidence.
- When evidence contradicts memory, trust current source/test/runtime evidence and create a memory candidate for update or rejection.
- If verification cannot run, record the exact command that should be run and why it could not be run now.
- Final reports should distinguish accepted residual risk from unresolved blockers.
