# AGENTS.md

## Repository Workflow

Use this file as repo-level guidance for any coding agent. Keep it short. Put detailed procedures in the installed `engineering-team` skill.

## Project-Scoped Memory

Before EngineeringTeam work, read `.engineering-team/memory/index.md` when it exists. Treat project memory as advisory: current source code, tests, and generated outputs win over memory. Do not store secrets, credentials, private user information, temporary logs, or speculation. Durable memory entries should include evidence/source paths.

## Default Engineering Rule

For non-trivial software work, use the EngineeringTeam workflow:

```text
repo map -> component map -> feature map -> contract graph -> focused files -> change plan -> implementation -> verification
```

Do not edit code until the owning component, affected contract, call path, risk level, and verification strategy are clear.

## Required Artifacts For Non-Trivial Work

Produce compact, task-scoped artifacts before implementation:

- Repo Atlas: system type, main components, entry points, tests, build commands, generated-code rules.
- Component Brief: focused owner, files, symbols, call path, nearby tests, similar patterns.
- Contract Graph: producer -> contract -> consumer -> failure mode -> coverage.
- Evidence Ledger: claim -> evidence -> confidence -> impact.
- Verification Report: command -> result -> failure attribution -> remaining risk.

Prefer temporary artifacts under `.agent-state/` unless the repo already has a convention.

## Agent-Team Policy

Spawn specialist agents only when a proactive trigger is met, the work is bounded, and the output can be returned as a compact context capsule. Keep fan-out small. If subagents are unavailable or not worth the overhead, simulate the role in the main session.

Recommended specialists, when installed:

- `codebase_investigator`: read-only repo mapping and evidence gathering.
- `evidence_skeptic`: read-only falsification and implementation gate review.
- `test_verification_engineer`: test strategy, targeted commands, failure attribution.
- `implementation_engineer`: smallest safe patch after the evidence gate.
- `security_analyst`: trust boundaries, auth, inputs, secrets, dependency risk.
- `optimization_engineer`: measurement-backed performance work.
- `migration_analyst`: compatibility and semantic migration risks.
- `release_rollback_engineer`: rollout, observability, rollback.
- `system_design_architect`: module boundaries and long-term shape.
- `dx_documentation_reviewer`: docs, CLI ergonomics, developer experience.
- `advisor_consultant`: gate-only second opinion for L4/L5, conflicting-evidence, production-sensitive, or assumption-heavy decisions.

If custom specialists are not installed, use the harness-native exploration and implementation tools while preserving the same evidence gates.

## Implementation Gate

Before modifying files, state:

- files to change
- evidence for the diagnosis or requirement
- contract edges affected
- tests to add or run
- rollback path for risky changes
- advisor decision receipt when the advisor gate was used

Prefer the smallest safe change. Avoid unrelated cleanup, broad rewrites, and style churn.

## Verification Rule

Run the narrowest meaningful check first, then expand only when risk justifies it. A passing test is useful only if it exercises the changed behavior or affected contract.

When a command fails, classify the failure before patching again:

- wrong implementation
- wrong test expectation
- missing dependency
- environment issue
- flaky test
- incomplete repo understanding
- hidden contract violation
- generated-code mismatch
- stale documentation
- permission/tooling issue

## Context Hygiene Rule

Keep the main session focused on decisions. Use subagents for broad search, long command output, and specialist critique. Subagents must receive bounded briefs and return context capsules, not transcripts.

## Durable Context Rule

Update durable repo instructions only when the discovery is reusable:

- architecture rule
- build/test command
- generated-code convention
- component ownership
- integration contract
- recurring failure mode

Do not add one-off task details to this file.
