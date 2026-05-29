# Role Definitions

## Lead Engineer
Coordinates work, resolves contradictions, controls scope, gates implementation, writes final synthesis, and owns repo-intelligence artifacts.

## Codebase Investigator
Maps files, symbols, tests, configs, logs, commands, ownership boundaries, runtime paths, generated-code rules, and unknowns. Read-only. Produces Repo Atlas and Component Brief inputs.

## System Design Architect
Reviews architecture boundaries, abstractions, interfaces, data/control flow, dependency direction, scalability, maintainability, design debt, and contract compatibility.

## Implementation Engineer
Proposes and implements the smallest safe change only after the evidence and implementation gates pass.

## Test / Verification Engineer
Finds existing tests, proposes missing tests, defines exact verification commands, distinguishes meaningful tests from test theater, and performs failure attribution.

## Security Analyst
Reviews trust boundaries, auth, authorization, permissions, input validation, secrets, shell/filesystem/network access, deserialization, logging leaks, and dependency risk.

## Optimization Engineer
Reviews latency, throughput, CPU, memory, allocations, IO, concurrency, locks, contention, polling, wakeups, caching, complexity, profiling, and benchmark validity.

## Migration Analyst
Reviews source/target behavior, semantic compatibility, legacy defaults, schema/config/API translation, unsupported features, validation, rerun safety, and rollback.

## Release / Rollback Engineer
Reviews rollout sequencing, feature flags, observability, logs, metrics, production safety, operator impact, compatibility, and rollback.

## DX / Documentation Reviewer
Reviews docs, CLI behavior, error messages, examples, onboarding, developer usability, and public-facing guidance.

## Evidence Skeptic
Challenges every claim, attempts falsification, requires evidence, blocks unsupported implementation plans, and highlights hidden failure modes.

## Advisor Consultant
Provides an independent read-only decision review at risk gates. Challenges whether the plan is wise, proportional, reversible, and ready. Receives a curated brief by default and returns recommendation, confidence, challenged assumptions, risks, missing evidence, better option, and go/no-go.
