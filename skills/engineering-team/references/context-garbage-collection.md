# Context Garbage Collection

**Always run this step at task end, even when no durable updates are needed.** Produce the artifact to confirm — a silent skip looks like forgetting.

At task completion, decide whether durable context should change. Apply the canonical promotion and rejection rules in `references/memory-promotion.md`; this file owns the closeout flow, not the full memory taxonomy.

If durable context is stale, report it instead of silently trusting it.

Create context lazily. Do not create `CONTEXT.md` or ADR files just because they are missing.

## Repo-scoped memory

When `.engineering-team/memory/index.md` exists, Context GC / session closeout may create or update repo-scoped memory files under `.engineering-team/memory/`. Memory is advisory: current source code, tests, and generated outputs win over memory.

Do not copy a Run Ledger into memory. A Run Ledger is task-scoped trace evidence. Use `references/memory-promotion.md` and `templates/memory-candidates.md` to promote only durable, reusable, non-sensitive findings with required metadata.

## Memory promotion flow

1. Inspect the final report, evidence ledger, verification report, Run Ledger, and context capsules.
2. Extract candidate learnings into `templates/memory-candidates.md`.
3. Apply `references/memory-promotion.md`.
4. Promote, reject, defer, or mark needs-verification.
5. Update `.engineering-team/memory/` only for promoted or explicitly needs-verification entries.
6. Report rejected and deferred candidates so the omission is intentional.

Use the required metadata from `references/memory-promotion.md` for every promoted entry.

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

- Durable knowledge candidates:
- Promoted to memory:
- Marked needs-verification:
- Rejected candidates:
- Deferred candidates:
- Stale context found:
- One-off details not retained:
```
