# Debugging Route

Use for read-only failure investigation, regression triage, root-cause analysis, stack traces, crashes, flaky behavior, and inconsistent runtime results.

## Authority

Remain read-only. Safe local diagnostics and reproductions are allowed; code, tests, and runtime configuration changes are not. Do not patch a symptom merely because a plausible fix appears.

## Workflow

1. Capture expected versus observed behavior, environment, timeline, frequency, and reproduction quality.
2. Map the failure path from entry point to output or error boundary.
3. Load `references/diagnosis-loop.md` and rank falsifiable hypotheses.
4. Build `templates/debugging-hypothesis-matrix.md` with supporting evidence, counter-evidence, falsifier, and blast radius.
5. Design the smallest probes that distinguish the leading hypotheses; record stop conditions in `templates/next-probe-plan.md`.
6. Use Codebase Investigator for ownership/call paths, Test Verification Engineer for reproduction signals, domain specialists for triggered boundaries, and Evidence Skeptic before claiming convergence.

## Output

Return the hypothesis matrix and next-probe plan. Separate facts, contradictions, assumptions, rejected hypotheses, likely root cause, and fix readiness. If implementation is later authorized, pass the confirmed evidence, affected contract, proposed file boundary, and verification strategy into Implementation mode.
