# Routing Examples

## Flaky test

Main session: Lead Engineer

Spawn:
- Codebase Investigator
- Test / Verification Engineer
- Evidence Skeptic

Defer:
- Optimization Engineer unless timing/concurrency/performance appears
- Security Analyst unless auth/input/security appears
- Architect unless design boundaries are implicated

## New auth middleware

Main session: Lead Engineer

Spawn before the gate:
- System Design Architect
- Codebase Investigator
- Test / Verification Engineer
- Security Analyst
- Evidence Skeptic

Spawn after the gate:
- Implementation Engineer with explicit source-file ownership

Defer:
- Optimization Engineer unless middleware is on hot path
- Release / Rollback Engineer unless rollout risk exists

## Slow endpoint

Main session: Lead Engineer

Spawn:
- Codebase Investigator
- Optimization Engineer
- Test / Verification Engineer
- Evidence Skeptic

Add later:
- Architect if fix changes boundaries or APIs
- Security Analyst if hot path touches auth/user input

## Legacy migration bug

Main session: Lead Engineer

Spawn:
- Codebase Investigator
- Migration Analyst
- Test / Verification Engineer
- Evidence Skeptic

Add later:
- Architect if conversion model is wrong
- Security Analyst if security semantics are affected
- Optimization Engineer only if scale/performance matters

## Tiny typo

Main session: Lead Engineer. Do not spawn a team.
