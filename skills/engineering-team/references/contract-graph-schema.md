# Contract Graph Schema

Trace behavior as contracts, not just files.

Preferred shape:

```text
source → adapter → contract → domain operation → side effect → observable output → verification
```

## Table format

```md
# Contract Graph

| Edge | Producer | Contract / Data Shape | Consumer | Side Effect | Failure Mode | Coverage | Risk |
|---|---|---|---|---|---|---|---|
```

## Edge questions

For each boundary, answer:

- Who produces this value or event?
- What exact data shape or protocol is expected?
- Who consumes it?
- What side effect happens?
- What breaks if the contract changes?
- What test, log, metric, or check observes the behavior?
- Is compatibility required?

## Important boundaries

- API routes / RPC handlers
- CLI commands
- public interfaces
- config/schema definitions
- persistence boundaries
- file system/network/shell boundaries
- auth/permission checks
- generated-code inputs and outputs
- external service calls
- logs, metrics, traces
