---
name: debugging-forensics
description: "Use for read-only debugging and root-cause investigation: reproduce or reason about failures, build hypothesis matrices, identify next probes, and avoid edits until a fix is requested."
---

# Debugging Forensics

Use when the user asks to investigate, debug, triage, or explain a failure without yet asking for a fix.

## Default posture

Read-only by default. Inspect code, tests, configs, stack traces, and diagnostic output; do not patch code, rewrite tests, or change runtime state beyond safe local diagnostics unless implementation is authorized.

## Workflow

1. Capture symptom, expected vs observed behavior, environment, and timeline.
2. Map the failure path from entry point to output/error boundary.
3. Build `../engineering-team/templates/debugging-hypothesis-matrix.md`.
4. Rank hypotheses by evidence, blast radius, and falsifiability.
5. Design `../engineering-team/templates/next-probe-plan.md`.
6. Separate facts, contradictions, assumptions, and proposed fixes.

## Useful specialists

Use runtime tracing for stack/call/async/state paths, reproduction engineering for deterministic probes, and Evidence Skeptic to disprove weak-but-attractive hypotheses.

## Required output

Return a hypothesis matrix plus next-probe plan. If the user later asks for a fix, hand off the confirmed root cause, affected contract, and verification plan to `engineering-team` implementation mode.
