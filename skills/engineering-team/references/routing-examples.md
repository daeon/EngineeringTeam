# Routing Examples

## Flaky test

Spawn:
- Lead Engineer
- Codebase Investigator
- Test / Verification Engineer
- Evidence Skeptic

Defer:
- Optimization Engineer unless timing/concurrency/performance appears
- Security Analyst unless auth/input/security appears
- Architect unless design boundaries are implicated

## New auth middleware

Spawn:
- Lead Engineer
- System Design Architect
- Codebase Investigator
- Implementation Engineer
- Test / Verification Engineer
- Security Analyst
- Evidence Skeptic

Defer:
- Optimization Engineer unless middleware is on hot path
- Release / Rollback Engineer unless rollout risk exists

## Slow endpoint

Spawn:
- Lead Engineer
- Codebase Investigator
- Optimization Engineer
- Test / Verification Engineer
- Evidence Skeptic

Add later:
- Architect if fix changes boundaries or APIs
- Security Analyst if hot path touches auth/user input

## Legacy migration bug

Spawn:
- Lead Engineer
- Codebase Investigator
- Migration Analyst
- Test / Verification Engineer
- Evidence Skeptic

Add later:
- Architect if conversion model is wrong
- Security Analyst if security semantics are affected
- Optimization Engineer only if scale/performance matters

## Tiny typo

Spawn:
- Lead Engineer only

Do not create a team.

