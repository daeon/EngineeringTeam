# Failure Attribution

When verification fails, classify before patching.

## Canonical failure triage

This file owns the reusable failure classes, attribution loop, and rules for responding to failed verification. Other verification references should link here instead of restating the full class list or loop.

For bug investigations, build or refresh the feedback loop from `diagnosis-loop.md` before changing code. A failure is actionable only when it reproduces the user-described symptom or proves a directly relevant contract risk.

## Failure classes

- wrong implementation
- wrong test expectation
- missing dependency
- environment issue
- flaky test
- incomplete repo understanding
- hidden contract violation
- generated-code mismatch
- stale documentation
- permission/tooling issue

## Loop

```text
failure → attribution → new evidence → revised plan → focused patch → rerun
```

For uncertain root cause, expand the loop:

```text
feedback loop → reproduce → ranked falsifiable hypotheses → targeted probe → attribution → focused patch → rerun original loop
```

## Rules

- Do not blindly patch failing tests.
- Do not rewrite broad areas to chase one failure.
- Separate unrelated environmental failures from behavior failures.
- If a test is misleading, say exactly why.
- Temporary debug instrumentation must be tagged with a unique `[DEBUG-...]` prefix and removed before completion.
- If no correct regression seam exists, report that as a testability or architecture finding instead of adding a shallow test.
