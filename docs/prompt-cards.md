# Prompt Cards

Copy-paste prompts by task type. Each one invokes `engineering-team` and asks
for the repo-first workflow: map before editing, route specialists only when
useful, require evidence, and verify.

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

## Performance investigation

```text
Use engineering-team to investigate this performance regression. Establish a
deterministic measurement first, identify the hot path with evidence, rank
falsifiable hypotheses, and only then propose a change. Show before/after
numbers and confirm no behavior change.
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
