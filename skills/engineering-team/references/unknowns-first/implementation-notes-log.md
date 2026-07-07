# Implementation Notes Log

Use this phase during implementation when the work diverges materially from the original plan or when human judgment should remain visible to reviewers.

## Material deviations

Record deviations when:

- files changed differ from the Implementation Gate
- a recommended default changes
- a test is skipped, narrowed, or replaced
- a probe reveals stale docs or a hidden contract
- a conservative choice leaves behavior intentionally unchanged
- a risky action was avoided or deferred

## Conservative choices

```md
## Implementation notes

| Topic | Choice | Reason | Evidence | Follow-up |
|---|---|---|---|---|
```

## Tests skipped

```md
## Skipped checks

| Check | Why skipped | Risk | Replacement evidence |
|---|---|---|---|
```

## Human judgment needed

If a decision remains user-only but does not block the current safe change, record it as follow-up rather than hiding it in prose.

## Output mapping

Write implementation notes to the Run Ledger. Summarize only the material parts in the Final Report.
