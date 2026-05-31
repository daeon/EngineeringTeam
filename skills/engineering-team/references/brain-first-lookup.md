# Brain-First Lookup

Use this reference immediately after intake and before broad repo discovery. The goal is to reuse curated, repo-scoped knowledge before spending context on fresh exploration.

Brain-first lookup is advisory. Source code, tests, generated outputs, and current runtime evidence always override memory.

## When to run

Run this step for L2+ EngineeringTeam work and for any task involving an unfamiliar component, repeated failure mode, recurring validation command, generated-code rule, architecture decision, contract boundary, handoff, or memory candidate.

For L0 fast-path tasks, do a minimal lookup only when `.engineering-team/memory/index.md` exists and the task name or component is obvious.

## Lookup order

1. Read `.engineering-team/memory/index.md` when it exists.
2. Load only the narrow memory files named by the index or task scope.
3. Check component, contract, verification, and gotcha memory before broad search.
4. Mark any stale, contradictory, or weak memory as a gap instead of silently trusting it.
5. Continue with fresh repo inspection when memory does not answer the task.

## Artifact: Brain-First Lookup

```md
# Brain-First Lookup

| Question | Memory consulted | Result | Confidence | Next action |
|---|---|---:|---|---|
| What prior repo knowledge applies? |  | found / missing / stale / contradicted | high / medium / low |  |
| Which files or contracts should guide exploration? |  |  |  |  |
| Which memory entries should not be trusted yet? |  |  |  |  |
```

## Guardrails

- Do not treat memory as a source of truth when current code, tests, generated outputs, or command output disagree.
- Do not load every memory file by default; load the smallest relevant set.
- Do not promote task-only details during lookup. Promotion happens during Context GC.
- Do not store or repeat secrets, credentials, private data, raw customer logs, or speculative claims.
- Record stale or missing memory in `references/gap-analysis.md` so the omission is visible.

## Common outcomes

| Outcome | Meaning | Next action |
|---|---|---|
| found | Memory gives a reusable orientation shortcut | Use it as a starting hypothesis and verify against source |
| missing | No relevant memory exists | Build fresh repo/component/contract evidence |
| stale | Memory has an old verification date or unclear trigger | Verify before relying on it |
| contradicted | Current source/evidence disagrees with memory | Trust current evidence and create a memory candidate to update or reject |
