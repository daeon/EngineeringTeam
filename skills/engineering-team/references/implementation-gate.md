# Implementation Gate

**You must output the `## Implementation gate` block below before writing any file.** If any checklist item fails, resolve it first — do not skip and edit anyway.

## Gate checklist

Before editing, verify:

- [ ] problem scope is clear
- [ ] Repo Atlas exists (or unnecessary due to tiny scope)
- [ ] Component Brief exists
- [ ] Contract Graph exists for L3+ work
- [ ] Evidence Ledger contains the key claims
- [ ] affected files are identified
- [ ] root-cause or design evidence exists
- [ ] architecture/security/performance/migration/release constraints are known when relevant
- [ ] Evidence Skeptic reviewed the plan for non-trivial work
- [ ] Advisor Consultant reviewed the plan when the advisor gate requires it (see `references/advisor-gate.md`)
- [ ] tests or verification commands are defined
- [ ] rollback path is understood
- [ ] same-file edit conflicts are avoided

If any item fails, continue investigation or spawn the missing specialist.

See `references/autonomy-ladder.md` for the full L0–L5 gate requirements.

## Gate output

```md
## Implementation gate

- Gate status: Pass / Blocked
- Missing evidence:
- Files allowed to change:
- Files inspected but not changing:
- Verification required:
- Rollback path:
```

## Implementation rules

During implementation:

- Make the smallest safe change.
- Preserve existing style and conventions.
- Prefer repo conventions over generic best practices.
- Avoid unrelated refactors and broad rewrites.
- Keep changes close to the target behavior.
- Preserve public contracts unless explicitly required to change them.
- Add comments only for non-obvious reasoning.
- Update tests close to the changed behavior.
- For test-first work, use vertical tracer-bullet cycles: one behavior test, minimal implementation, repeat. See `references/tdd-discipline.md`.
- Tests should verify behavior through public interfaces, not private implementation details.
- Track every changed file.
- Avoid concurrent edits to the same file.
- If generated code is involved, determine whether to modify source definitions, generated outputs, or both according to repo convention.

Prefer mechanically enforced rules over prose: test, linter, static check, schema validation, type-level constraint, CI check, scripted verifier — in that order.
