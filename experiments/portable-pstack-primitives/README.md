# Portable pstack primitives

Experimental, harness-neutral adaptations of six skills from Cursor's `pstack` plugin:

- `how`
- `why`
- `blast-radius`
- `arena`
- `unslop`
- `technical-writing`

These are deliberately staged under `experiments/` rather than promoted into EngineeringTeam. The goal is to preserve the strongest mechanics while removing Cursor-specific model slugs, transcript paths, mode assumptions, and dependencies on other pstack skills.

## Design rules

1. Keep each skill independently useful and composable.
2. Prefer evidence and runnable checks over persuasive prose.
3. Use role-based delegation (`explorer`, `judge`, `candidate`) rather than hard-coded model names.
4. Keep tools capability-bounded. Read-only investigations should use read-only access when the harness supports it.
5. Do not duplicate ThoughtLoop responsibilities. These are specialist primitives, not another router.
6. Do not promote from `experiments/` until the evaluation plan has concrete evidence.

## Relationship to existing owned skills

- `how` complements `investigate` with a focused subsystem-explanation contract.
- `why` adds historical rationale reconstruction across multiple evidence systems.
- `blast-radius` is a candidate mode or companion for `review`.
- `arena` is a competing-artifact bakeoff, distinct from an expert-opinion panel.
- `unslop` is a prose cleanup primitive and should be compared against existing anti-AI-slop skills before promotion.
- `technical-writing` is for ordinary developer documentation. `standard-english` remains authoritative when formal standards, normative language, regulated wording, accessibility, or conformance claims are involved.

See `UPSTREAM.md` for attribution and `EVAL_PLAN.md` for the promotion gate.
