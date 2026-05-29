# Prompt Cards

Copy-paste prompts by task type. Most prompts invoke `engineering-team` and ask
for the repo-first workflow: map before editing, route specialists only when
useful, require evidence, and verify. Use `handoff` when transferring active work
to another agent or fresh session.


## Read-only codebase analysis

```text
Use engineering-team in read-only analysis mode to understand this codebase.
Route to codebase-analysis, build a repo/component map, identify entry points,
contracts, generated-code rules, and risk areas, and return an evidence-backed
codebase analysis report. Do not edit files.
```

## Read-only debugging forensics

```text
Use engineering-team in read-only analysis mode to debug this issue without
patching yet. Route to debugging-forensics, map the failing path, build a
hypothesis matrix with supporting and counter-evidence, and produce the next
probe plan needed to confirm or reject the likely root cause.
```

## Read-only log forensics

```text
Use engineering-team in read-only analysis mode to analyze these logs. Route to
log-forensics, redact sensitive values, reconstruct the timeline, identify
correlated signals and likely failure modes, and return a log forensics report
with next probes. Do not dump raw logs back to me.
```

## Bug investigation

```text
Use engineering-team to investigate this bug. Map the repo first, find the
owning component, trace the affected contract graph from input to output, and
identify the violated contract. Do not edit until you can show the evidence.
Then propose the smallest safe fix at the correct seam and add a regression test.
```

## PR / branch review

```text
Use engineering-team to review this branch. Build a quick repo atlas, map the
changed surface, and route to security, architecture, performance, migration,
and verification lenses only where the diff warrants. Return an evidence-backed
review with risks, missing tests, and a go/no-go.
```

## Read-only performance forensics

```text
Use engineering-team in read-only analysis mode to investigate this performance
regression. Route to performance-forensics, define the target metric and
baseline, map the suspected hot path, rank bottleneck hypotheses from evidence,
and produce the next measurement plan. Do not optimize or edit files yet.
```

## Performance implementation

```text
Use engineering-team to implement a performance fix after the bottleneck is
evidence-backed. Establish a deterministic measurement first, identify the hot
path with evidence, make the smallest safe change, show before/after numbers,
and confirm no behavior change.
```

## Security-sensitive change

```text
Use engineering-team for this security-sensitive change. Map the trust
boundaries, inputs, auth, secrets, and shell/filesystem/network access involved.
Route the security analyst and evidence skeptic. Require human approval before
any destructive or production-sensitive action. Verify with focused tests.
```

## Migration / compatibility review

```text
Use engineering-team to review this migration for compatibility. Compare old
and new behavior across the boundary (schema/config/API), enumerate edge cases
and irreversible steps, and propose a reversible rollout. Show evidence for each
compatibility claim.
```

## Release / rollback planning

```text
Use engineering-team to plan this release. Identify production-sensitive
behavior, observability, feature flags, and the rollback path. Require human
approval before sensitive side effects. Produce a release checklist with a clear
rollback trigger.
```

## Architecture review

```text
Use engineering-team for an architecture review. Map the system boundaries,
dependency direction, and key interfaces. Identify long-term maintainability and
scalability risks with evidence. Recommend the smallest set of changes that move
the design in the right direction.
```

## Test strategy

```text
Use engineering-team to design a test strategy for this component. Map the
existing test surfaces and coverage gaps, identify the public contracts that
need protection, and propose vertical tracer-bullet tests that exercise the real
path rather than implementation details.
```

## Handoff to another agent

```text
Use handoff to prepare this task for another agent or fresh session. Create a
compact continuation document with current state, decisions made, relevant
artifacts, files and symbols worth keeping in context, evidence confidence, open
questions, risks, suggested skills or agents, next actions, and work that should
not be repeated.
```
