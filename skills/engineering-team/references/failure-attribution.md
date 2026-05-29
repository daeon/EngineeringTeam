# Failure Attribution

When verification fails, classify before patching.

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

## Rules

- Do not blindly patch failing tests.
- Do not rewrite broad areas to chase one failure.
- Separate unrelated environmental failures from behavior failures.
- If a test is misleading, say exactly why.
