# Verification Loop

Run the narrowest useful verification first, then expand as risk requires.

## Verification order

1. Fast static checks
2. Targeted unit tests
3. Regression tests near changed behavior
4. Integration or system tests
5. Security, performance, migration, or manual checks when relevant
6. Broader suite only when risk justifies it

## Bug and regression work

For bug investigations, regressions, flaky behavior, crashes, or performance regressions, build a fast deterministic feedback loop before fixing. See `references/diagnosis-loop.md` to reproduce the exact symptom, rank falsifiable hypotheses, instrument one prediction at a time, and convert the minimized repro into a regression signal.

## Test-first work

For new behavior or regression coverage, see `references/tdd-discipline.md`: avoid horizontal "all tests then all implementation" slicing, prefer one vertical tracer bullet at a time, and reject tests that do not exercise the real public contract.

## Command capture

For every verification command, record:

- command
- result
- important output
- whether failures are related
- next action

## Failure attribution

If verification fails, classify the failure before patching. `references/failure-attribution.md` owns the canonical failure classes and triage loop; record the selected class and next action in the Verification Report instead of restating the full taxonomy here.

## Artifact: Verification Report

```md
# Verification Report

| Command | Result | Relevant Output | Related? | Next Action |
|---|---|---|---|---|

## Failure Attribution
## Coverage Gaps
## Unverified Risks
```

If tests cannot be run, explain why and provide the exact commands a maintainer should run.
