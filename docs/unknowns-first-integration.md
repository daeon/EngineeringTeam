# Unknowns-First Integration

Unknowns-first brings gapfinder-style ambiguity handling into EngineeringTeam without changing EngineeringTeam's core operating model.

## What Changes

For non-trivial work, the lead engineer may run a short pre-intake pass when ambiguity is itself risky. That pass can identify blind spots, user-only decisions, cheap probes, risky defaults, invalidating discoveries, or reviewer explanations before the normal workflow proceeds.

The canonical order is:

```text
Task
  -> optional unknowns-first pre-intake
  -> intake-risk
  -> alignment/routing
  -> EngineeringTeam artifacts
  -> implementation or read-only report
  -> verification and final report
```

## What Does Not Change

- `skills/engineering-team/SKILL.md` remains the main router.
- `references/intake-risk.md` still owns autonomy level and risk mode.
- Tiny obvious edits still use the fast path.
- Unknowns-first phases do not spawn a fixed committee.
- Unknowns-first phases do not create a parallel artifact system.
- Standalone gapfinder usage remains separate.

## Phase Mapping

| Unknowns-first phase | EngineeringTeam artifact target |
|---|---|
| `references/unknowns-first/router.md` | Route decision and risk mode |
| `blindspot-pass.md` | Repo Atlas notes, Evidence Ledger assumptions, Run Ledger residual risk |
| `architecture-interview.md` | Alignment Audit open decisions and recommended defaults |
| `prototype-reference-probe.md` | Component Brief references, options considered, non-production artifacts |
| `risk-first-plan.md` | Implementation Gate, Impact Map, verification strategy |
| `implementation-notes-log.md` | Run Ledger deviations, skipped checks, follow-ups |
| `change-explainer-quiz.md` | Final Report, rollback, reviewer checklist |
| `risk-score.md` | Intake support only |

## Validation

`skills/engineering-team/scripts/validate-package.py` checks that the unknowns-first references exist, keep their required headings, resolve backticked reference links, preserve one top-level router concept, and do not reintroduce startup or hook-style behavior.
