# Diagnosis Loop

Use this reference for hard bugs, regressions, flaky behavior, crashes, and performance regressions.

## Core rule

Build a fast, deterministic, agent-runnable pass/fail signal before hypothesizing or fixing.

If you do not have a feedback loop, you are guessing. Spend disproportionate effort creating the loop.

## Feedback loop options

Try these in roughly this order:

1. Failing test at the seam that reaches the bug.
2. HTTP script against a running dev server.
3. CLI invocation with fixture input and stdout/stderr assertion.
4. Headless browser script that asserts DOM, console, or network behavior.
5. Replayed captured trace, request, payload, event log, or fixture.
6. Throwaway harness that exercises the code path with one call.
7. Property or fuzz loop that searches for the failure mode.
8. Bisection harness for commit, data, or version regressions.
9. Differential loop comparing old vs. new behavior or config A vs. config B.
10. Human-in-the-loop script when a person must perform a manual action.

Improve the loop before debugging:

- Make it faster by narrowing setup and scope.
- Make it sharper by asserting the exact symptom.
- Make it more deterministic by pinning time, randomness, filesystem, and network behavior where possible.
- For nondeterministic bugs, raise the reproduction rate with repetition, stress, timing control, or parallel runs.

If no loop is possible, stop and ask for the missing artifact or access: logs, HAR, trace, fixture, core dump, screen recording with timestamps, or permission for temporary instrumentation.

## Hypothesis discipline

Before testing, write 3-5 ranked hypotheses.

Each hypothesis must be falsifiable:

```text
If <cause> is true, then <probe or change> will make <observable outcome> happen.
```

Discard hypotheses that do not predict an observable outcome.

## Instrumentation

Probe one prediction at a time.

Prefer:

1. debugger or REPL inspection
2. targeted boundary logs
3. profiler or measurement harness for performance regressions

Avoid broad "log everything" instrumentation.

Temporary debug logs must use a unique prefix like `[DEBUG-a4f2]` so cleanup is mechanical.

## Fix and regression

Turn the minimized repro into a regression test before the fix when a correct seam exists.

A correct seam exercises the real bug pattern as it occurs at the call site. If no correct seam exists, record that as an architecture or testability finding.

After fixing:

- rerun the minimized regression signal
- rerun the original feedback loop
- remove all `[DEBUG-...]` instrumentation
- delete or clearly mark throwaway harnesses
- record which hypothesis was confirmed

## Post-mortem

Ask: what would have prevented this bug?

If the answer is architectural, capture it as follow-up evidence for component design or context garbage collection. Do not broaden the current fix unless the architecture change is required for correctness.
