# Context Garbage Collection

At task completion, decide whether durable context should change.

Update durable knowledge only for reusable facts:

- architecture rule
- build/test command
- generated-code convention
- recurring failure mode
- component ownership
- integration contract
- verification command

Do not retain:

- one-off task details
- transient logs
- failed hypotheses
- temporary file paths
- user-specific scratch context unless explicitly requested

If durable context is stale, report it instead of silently trusting it.
