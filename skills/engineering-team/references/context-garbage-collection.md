# Context Garbage Collection

**Always run this step at task end, even when no durable updates are needed.** Produce the artifact to confirm — a silent skip looks like forgetting.

At task completion, decide whether durable context should change.

Update durable knowledge only for reusable facts:

- architecture rule
- build/test command
- generated-code convention
- recurring failure mode
- component ownership
- integration contract
- verification command
- resolved domain term for `CONTEXT.md`
- hard-to-reverse decision that meets the ADR test

Do not retain:

- one-off task details
- transient logs
- failed hypotheses
- temporary file paths
- user-specific scratch context unless explicitly requested

If durable context is stale, report it instead of silently trusting it.

Create context lazily. Do not create `CONTEXT.md` or ADR files just because they are missing.

## Repo-scoped memory

When `.engineering-team/memory/index.md` exists, Context GC / session closeout may create or update repo-scoped memory files under `.engineering-team/memory/` for reusable, evidence-backed knowledge. Memory is advisory: current source code, tests, and generated outputs win over memory. Do not store secrets, credentials, private user information, temporary logs, or speculation. Every durable memory entry should include evidence/source paths.

Use `CONTEXT.md` only for domain language:

- canonical terms
- short definitions
- relationships between terms
- aliases or overloaded words to avoid
- resolved ambiguities

Offer an ADR only when the decision is hard to reverse, surprising without context, and the result of a real trade-off.

## Artifact: Context GC output

```md
## Context garbage collection

- Durable knowledge to update:
- Stale context found:
- One-off details not retained:
```
