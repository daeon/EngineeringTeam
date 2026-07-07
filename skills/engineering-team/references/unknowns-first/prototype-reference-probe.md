# Prototype Reference Probe

Use this phase when a concrete option can be tested cheaply before committing to implementation.

## When to prototype

Prototype only when it reduces a real uncertainty:

- two implementation approaches have different compatibility or maintenance risks
- a library, generated output, schema, or harness behavior is unclear
- the task depends on a behavior that docs describe but tests do not cover
- a small throwaway fixture can expose an edge case faster than reasoning alone

Do not prototype as a substitute for reading the owning component.

## Probe rules

- Keep probes disposable and outside production paths.
- Prefer existing test fixtures, examples, scripts, and check modes.
- Do not leave experimental files unless they become intentional tests or docs.
- Mark any non-production artifact clearly in the Run Ledger.
- If a probe requires network, destructive actions, or external services, use the normal approval and safety gates first.

## Reference comparison

```md
## Reference probe

| Option | Evidence checked | Result | Trade-off | Decision |
|---|---|---|---|---|
```

## Output mapping

- Component Brief: options considered, similar existing patterns, and relevant files.
- Evidence Ledger: probe result and confidence.
- Run Ledger: temporary artifacts, cleanup, and any skipped probes.
- Verification strategy: the smallest check that exercises the chosen behavior.
