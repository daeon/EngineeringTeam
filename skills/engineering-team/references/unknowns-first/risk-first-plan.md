# Risk-First Plan

Use this phase when implementation can proceed only after risky defaults and invalidating discoveries are explicit.

## Decisions table

```md
## Risk-first decisions

| Decision | Default | Alternatives | Why default | Invalidating discovery | Verification |
|---|---|---|---|---|---|
```

## Risk ordering

Address risks in this order when relevant:

1. User safety, secrets, credentials, permissions, and destructive side effects.
2. Production behavior, rollback, observability, and external service impact.
3. Public API, data shape, compatibility, migrations, and generated-code drift.
4. Correctness and test coverage for the affected path.
5. Maintainability and developer experience.

## Invalidating discoveries

Name discoveries that would change or stop the plan:

- hidden consumer depends on current behavior
- tests reveal a different owner or contract
- generated output is the source of truth, not the edited file
- rollout or rollback path is missing
- user-only decision is irreversible
- narrow verification cannot exercise the changed behavior

## Output mapping

Feed this phase into:

- Implementation Gate: files allowed to change, missing evidence, rollback path.
- Impact Map: cross-component blast radius for L4+ work.
- Verification Loop: checks that would prove or falsify the plan.
- Final Report: alternatives considered and remaining risks.
