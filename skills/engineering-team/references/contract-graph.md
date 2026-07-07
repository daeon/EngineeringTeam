# Contract Graph

Trace behavior as contracts, not just files.

## Canonical contract anchors

This file owns boundary and edge modeling: producer, contract/data shape, consumer, side effect, failure mode, coverage, and risk. Mapping references that discuss cross-component blast radius should reuse these edge terms rather than inventing parallel schemas.

## Preferred shape

```text
source → adapter → contract → domain operation → side effect → observable output → verification
```

## Edge model

For every important boundary, capture:
- producer
- consumer
- contract / data shape
- ownership
- error behavior
- compatibility risk
- observability/logging/metrics
- existing coverage
- missing coverage
- failure mode

## Edge questions

For each boundary, answer:
- Who produces this value or event?
- What exact data shape or protocol is expected?
- Who consumes it?
- What side effect happens?
- What breaks if the contract changes?
- What test, log, metric, or check observes the behavior?
- Is compatibility required?

## Important interaction points to check

- public interfaces, function/class/module boundaries
- API routes or RPC handlers
- CLI commands
- config files, data models, schemas
- database or persistence access
- event/message queues
- external service calls
- file system reads/writes
- feature flags
- permission/auth checks
- error handling paths
- logging/metrics/tracing
- tests and fixtures
- generated code or codegen inputs

## Artifact: Contract Graph

```md
# Contract Graph

| Edge | Producer | Contract / Data Shape | Consumer | Side Effect | Failure Mode | Coverage | Risk |
|---|---|---|---|---|---|---|---|
```
