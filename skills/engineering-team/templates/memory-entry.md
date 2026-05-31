# Memory Entry

Use this template for durable repo-scoped memory entries. Memory is curated advisory context, not a transcript, run archive, or substitute for source code.

## Entry

```md
### <short durable fact>

- Type: component / contract / command / failure-mode / generated-rule / test-surface / architecture-decision / perf-hotpath / gotcha
- Status: current / needs-verification / stale
- Evidence/source paths:
  - `<path or command>`
- Origin run:
- Last verified:
- Confidence: high / medium / low
- Review trigger:
- Summary:
- How to use:
- Do not use when:
```

## Type guide

| Type | Use for |
|---|---|
| component | Owning area, key files, symbols, call paths |
| contract | Producer/consumer boundary, data shape, API, side effect, failure mode |
| command | Reusable validation, test, build, lint, or diagnostic command |
| failure-mode | Recurring bug pattern or investigation trap |
| generated-rule | Generated files, source-of-truth files, regeneration command |
| test-surface | Tests or fixtures that prove specific behavior |
| architecture-decision | Durable design choice or hard-to-reverse trade-off |
| perf-hotpath | Known latency, memory, throughput, locking, IO, or allocation path |
| gotcha | Stale-context warning or recurring repo-specific pitfall |

## Rejection checks

Do not create a memory entry when the candidate is task-only, speculative, contradicted by current source, missing evidence, likely to go stale without a trigger, or contains secrets, credentials, private data, customer-specific raw logs, or transient logs.
