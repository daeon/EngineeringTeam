# Specialist Roles

EngineeringTeam includes specialist roles so the agent can route work through the right engineering lens without turning every task into a committee.

## Routing Principle

Use the smallest useful team. More agents do not automatically create better work. Add a specialist only when it covers a distinct risk area or resolves an uncertainty the lead cannot safely answer alone.

Operational routing rules live in [`skills/engineering-team/references/agent-routing.md`](../skills/engineering-team/references/agent-routing.md), role details live in [`skills/engineering-team/references/role-definitions.md`](../skills/engineering-team/references/role-definitions.md), and context-sharing rules live in [`skills/engineering-team/references/subagent-context-policy.md`](../skills/engineering-team/references/subagent-context-policy.md). The summary below is a public catalog, not the canonical procedure.

## Roles

## Lead Engineer (main session)

The main session owns Lead responsibilities. Lead is not a generated or spawnable specialist; this prevents recursive routing and keeps one decision owner.

Coordinates the work, classifies the task, chooses specialists, resolves contradictions, and produces the final plan.

Use for every EngineeringTeam task.

## Codebase Investigator

Maps unfamiliar repositories, identifies ownership, finds relevant files, and gathers evidence before implementation.

Use when the affected area is unclear or the repo is unfamiliar.

## Evidence Skeptic

Challenges assumptions, checks whether claims are supported, and blocks premature implementation when evidence is thin.

Use for non-trivial behavior changes, unclear root causes, or high-risk work.

## Test Verification Engineer

Designs the verification plan, finds nearby tests, interprets failures, and separates environment issues from product issues.

Use for bug fixes, behavior changes, flaky tests, and CI failures.

## Implementation Engineer

Applies the smallest safe patch after the evidence and implementation gates pass.

Use when code changes are likely and the scope is already understood.

## System Design Architect

Reviews module boundaries, dependency direction, public interfaces, and long-term maintainability.

Use for architecture, broad refactors, public APIs, or cross-component changes.

## Security Analyst

Reviews trust boundaries, auth, authorization, user input, injection risk, secrets, shell/filesystem/network access, and dependency risk.

Use whenever the change touches security-sensitive behavior.

## Optimization Engineer

Reviews performance, latency, throughput, memory, CPU, IO, concurrency, caching, polling, and benchmark validity.

Use when the user asks for speed, scale, resource usage, or performance regression analysis.

## Migration Analyst

Reviews semantic compatibility across versions, schemas, APIs, config formats, imports, exports, and legacy behavior.

Use for migrations, upgrades, compatibility work, or historical behavior preservation.

## Release Rollback Engineer

Reviews rollout safety, observability, feature flags, deployment risk, production behavior, and rollback options.

Use for production-sensitive or operational changes.

## DX Documentation Reviewer

Reviews documentation, CLI behavior, onboarding, examples, error messages, and developer experience.

Use when the change affects how humans learn, run, debug, or operate the project.

## Advisor Consultant

Acts as a gate-only second opinion for high-risk decisions. The advisor is not a default teammate and should receive a curated decision brief, not the full conversation by default.

Use when autonomy is high, evidence conflicts, root cause remains unclear, or decisions affect security, migration, release, production behavior, or rollback.

## Good Routing Examples

- A failing unit test in an unfamiliar module: Lead, Codebase Investigator, Test Verification Engineer, Evidence Skeptic.
- A public API refactor: Lead, Codebase Investigator, System Design Architect, Test Verification Engineer, Evidence Skeptic.
- An auth bug: Lead, Codebase Investigator, Security Analyst, Test Verification Engineer, Evidence Skeptic.
- A performance cliff: Lead, Codebase Investigator, Optimization Engineer, Test Verification Engineer, Evidence Skeptic.
- A production migration: Lead, Migration Analyst, Release Rollback Engineer, Evidence Skeptic, Advisor Consultant.
