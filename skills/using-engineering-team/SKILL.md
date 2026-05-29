---
name: using-engineering-team
description: Use at session start to teach coding agents when and how to invoke the EngineeringTeam workflow for non-trivial software engineering work.
---

# Using EngineeringTeam

You have access to the `engineering-team` skill.

Use it for non-trivial software engineering work where a bad decision could come from missing repository evidence, choosing the wrong specialist, skipping verification, or editing before the impact is understood.

Invoke `engineering-team` before implementation when the task involves:

- bug investigation, regressions, flaky tests, crashes, or root-cause analysis
- feature implementation or behavior changes
- architecture, API, interface, module-boundary, or dependency decisions
- security-sensitive code, trust boundaries, auth, permissions, inputs, secrets, shell/filesystem/network access, or dependency risk
- performance, latency, throughput, memory, CPU, IO, caching, batching, polling, locking, concurrency, or scalability
- migration, compatibility, legacy behavior, schema/config/API translation, imports/exports, or upgrades
- release, rollout, rollback, observability, production behavior, or operational risk
- PR review requiring several lenses
- user requests for agents, teams, deliberation, debate, review board, red team, or coordination

Do not use the full team workflow for tiny typo fixes, obvious local edits, or work that is clearly sequential and isolated to one file.

Default workflow:

1. Classify the task.
2. Route the smallest useful specialist set.
3. Gather repository evidence before editing.
4. Require an evidence gate before implementation.
5. Make the smallest safe change.
6. Verify with focused commands and report dataflow, inputs, outputs, risks, and rollback.

If native subagents are unavailable, simulate the roles in the main session while preserving the same evidence gate.
