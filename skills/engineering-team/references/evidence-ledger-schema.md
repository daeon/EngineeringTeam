# Evidence Ledger Schema

Every major engineering claim must map to evidence.

```md
# Evidence Ledger

| Claim | Evidence | Confidence | Impact |
|---|---|---:|---|
```

## Accepted evidence

- source file path
- symbol/function/class reference
- test result
- command output
- log excerpt
- API contract
- documented behavior when code agrees
- reproducible observation

## Claim classification

1. Proven
2. Plausible but unproven
3. Contradicted
4. Irrelevant
5. Risky assumption

## Rules

- Do not present assumptions as facts.
- Do not treat passing unrelated tests as proof.
- Prefer direct evidence over inferred evidence.
- Highlight contradictions instead of smoothing them over.
