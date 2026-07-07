# Architecture Interview

Use this phase when the task may change architecture, public contracts, module boundaries, data ownership, security posture, or rollout behavior.

## One-question protocol

Ask at most one question at a time, and only after checking whether the repository can answer it.

Each question must include:

- the decision being made
- why it matters
- the recommended default
- the consequence of accepting the default
- the evidence already checked

Prefer concrete defaults over open-ended surveys.

## Decision ladder

Walk decisions in this order:

```text
intent -> user-facing behavior -> public contract -> ownership boundary -> data shape -> side effects -> compatibility -> observability -> rollout -> verification
```

Stop when the next safe engineering action is clear.

## Recommended defaults

When the user is unavailable and the choice is reversible, record a conservative default and continue. Conservative defaults usually:

- preserve existing public behavior
- keep compatibility unless the user asked to break it
- avoid widening permissions, network access, filesystem access, or secret exposure
- prefer existing repo patterns over new abstractions
- defer broad migrations unless current supported releases require them

## Output

Write this into the Alignment Audit:

```md
## Architecture interview

- Repo-answerable decisions checked:
- Recommended defaults:
- User-only decisions:
- Compatibility constraints:
- Verification signal:
- Stop reason:
```
