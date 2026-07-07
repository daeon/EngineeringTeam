# Change Explainer Quiz

Use this phase before closeout when the reviewer needs a compact explanation of what changed, what stayed stable, and how to undo it.

## Reviewer-ready explainer

```md
## Change explainer

- Behavior changed:
- Behavior preserved:
- Contracts affected:
- Why this path:
- Alternatives rejected:
- Verification signal:
- Rollback:
```

## Optional quiz

Use the quiz when a change is complex enough that the agent should prove it understands the diff before finalizing.

```md
## Reviewer quiz

| Question | Answer | Evidence |
|---|---|---|
| What user-visible behavior changed? |  |  |
| Which contract edge is most at risk? |  |  |
| What would fail if the assumption is wrong? |  |  |
| Which check actually exercises the change? |  |  |
| How can this be rolled back? |  |  |
```

## Output mapping

Use the explainer to populate the Final Report sections for changes, verification, risks, and rollback. Do not add a separate final-report format.
