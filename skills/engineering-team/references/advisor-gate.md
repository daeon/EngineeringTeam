# Advisor Gate

Use Advisor Consultant as a decision gate, not a default teammate.

## When to invoke

Invoke before implementation when any of these are true:

- autonomy is L4 or L5 and the plan changes behavior across components
- root cause remains unclear after investigation
- source evidence and runtime evidence conflict
- the decision affects security, migration, compatibility, release, production behavior, or rollback
- completion confidence depends on assumptions rather than direct evidence
- Evidence Skeptic returns `Blocked`, `No-Go`, or unresolved contradictions

Do not invoke for `low-risk-local` work or routine L2/L3 work where evidence and verification path are clear.

Also do not invoke for obvious one-line edits, simple shell answers, routine low-risk docs, or cases where local evidence already proves the next action.

## Advisor brief contract

```md
## Decision Needed

## Current Plan

## Relevant Evidence

## Constraints

## Alternatives Considered

## Uncertainty

## Requested Output
```

Default Advisor Consultant to `brief-only` with `fork_context: false`. See `references/agent-routing.md` for the full context budget policy.

## Advisor output contract

```md
## Recommendation

## Confidence

## Assumptions Challenged

## Risks Found

## Missing Evidence

## Better Option

## Go / No-Go
```

## Lead follow-through

- Treat the advisor response as evidence to reconcile, not automatic authority.
- If the advisor returns `No-Go`, do not implement until the missing evidence or safer option is addressed.
- If advisor confidence is below `Medium`, pause for user approval before sensitive side effects.
- Record an Advisor Decision Receipt in the final report whenever the advisor runs.

## Human approval triggers

Pause and confirm with the user before proceeding when any of these are true:

- live DUT or production-like system mutation
- destructive commands or irreversible data/file changes
- broad generated-file rewrites
- production-sensitive workaround or release/rollback decision
- Advisor Consultant returns `No-Go`
- Advisor Consultant confidence is below `Medium`

## Artifact: Advisor Decision Receipt

```md
## Advisor Decision Receipt

- Decision:
- Evidence used:
- Advisor recommendation:
- Lead decision:
- Why accepted / rejected:
- Follow-up checks:
```
