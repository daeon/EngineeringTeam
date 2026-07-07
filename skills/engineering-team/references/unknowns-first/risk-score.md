# Risk Score

Use this compact score only to decide whether an unknowns-first phase is worth loading. Final autonomy and risk mode still belong to `references/intake-risk.md`.

## Scoring rubric

Score each dimension 0-2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Ambiguity | clear local request | some unclear scope or acceptance criteria | vague, conflicting, or assumption-heavy |
| Blast radius | one local file | one component or tests | public contract, multiple components, or generated code |
| Reversibility | trivial rollback | manageable rollback | irreversible, migration, production, or external side effect |
| Evidence quality | direct code/test evidence | partial docs or inferred evidence | stale, conflicting, or missing evidence |
| Domain sensitivity | routine implementation | compatibility or performance concern | security, release, production, or architecture concern |

## Score interpretation

| Score | Action |
|---:|---|
| 0-2 | Skip unknowns-first unless a new ambiguity appears. |
| 3-5 | Run one focused phase if it reduces a current risk. |
| 6+ | Run the router and record the chosen phase before intake finalization. |

## Output

```md
## Unknowns-first score

- Ambiguity:
- Blast radius:
- Reversibility:
- Evidence quality:
- Domain sensitivity:
- Total:
- Decision:
```
