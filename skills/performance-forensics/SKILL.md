---
name: performance-forensics
description: "Use for read-only performance investigation: establish measurements, identify hot paths, rank hypotheses, and recommend probes before any optimization changes."
---

# Performance Forensics

Use this skill when the user asks to investigate latency, throughput, memory, CPU, IO, caching, batching, polling, locks, concurrency, or scalability without immediately implementing an optimization.

## Default posture

Read-only by default. Prefer measurements over intuition. Do not optimize, refactor, tune configs, or edit code until the user asks for implementation and the bottleneck is evidence-backed.

## Workflow

1. Define the performance question, target metric, baseline, workload, environment, and acceptable variance.
2. Map the suspected hot path and resource boundary.
3. Gather or request measurements: benchmark output, profiles, traces, metrics, logs, or focused diagnostic commands.
4. Build a ranked hypothesis matrix: bottleneck, evidence, counter-evidence, next measurement, expected impact.
5. Return a performance forensics report using `../engineering-team/templates/performance-forensics-report.md` and a next-probe plan.

## Useful specialists

- Performance Investigator for measurement design and bottleneck ranking.
- Runtime Trace Analyst for call paths and concurrency/state transitions.
- Observability Architect for metrics, tracing, and production signal quality.
- Evidence Skeptic for confounders and benchmark validity.

## Required output

Return baseline/measurement notes, hot-path evidence, ranked bottleneck hypotheses, confidence, next probes, and implementation candidates only after labeling them as unimplemented recommendations.
