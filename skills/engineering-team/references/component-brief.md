# Component Brief

Find the component or feature area relevant to the task.

## Layered search strategy

```text
1. Search exact user terms.
2. Search related domain terms.
3. Search error strings or log messages.
4. Search public interfaces.
5. Search tests and fixtures.
6. Search callers/callees.
7. Search config/schema references.
```

Do not assume ownership from filenames alone. Verify through call paths, tests, interfaces, and runtime/config references.

## Artifact: Component Brief

```md
# Component Brief

## Relevant Component
## Responsibility
## Important Files
## Relevant Symbols
## Main Call Path
## Related Tests
## Similar Existing Patterns
## Inputs / Outputs
## Side Effects
## Open Questions
## Evidence
```
