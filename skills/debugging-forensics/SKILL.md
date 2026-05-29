---
name: debugging-forensics
description: "Use for read-only debugging and root-cause investigation: reproduce or reason about failures, build hypothesis matrices, identify next probes, and avoid edits until a fix is requested."
---

# Debugging Forensics

Use this skill when the user asks to investigate, debug, triage, or explain a failure without yet asking for a fix.

## Default posture

Read-only by default. You may inspect code, tests, configs, stack traces, and command output. Do not patch code, rewrite tests, or change runtime state beyond safe local diagnostic commands unless the user explicitly authorizes implementation.

## Workflow

1. Capture the symptom, expected behavior, observed behavior, environment, and timeline.
2. Map the failure path from entry point to output or error boundary.
3. Build a hypothesis matrix using `../engineering-team/templates/debugging-hypothesis-matrix.md`.
4. Rank hypotheses by evidence strength, blast radius, and falsifiability.
5. Design the smallest next-probe plan using `../engineering-team/templates/next-probe-plan.md`.
6. Separate confirmed facts, contradictions, assumptions, and proposed fixes.

## Useful specialists

- Runtime Trace Analyst for stack traces, call paths, async flows, and state transitions.
- Reproduction Engineer for minimal repro and deterministic diagnostic commands.
- Evidence Skeptic for disproving attractive but weak hypotheses.

## Required output

Return a hypothesis matrix plus next-probe plan. If the user later asks for a fix, hand off the confirmed root cause, affected contract, and verification plan to `engineering-team` implementation mode.
