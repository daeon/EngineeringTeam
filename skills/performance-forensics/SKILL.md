---
name: performance-forensics
description: "Use for read-only performance investigation: establish measurements, identify hot paths, rank hypotheses, and recommend probes before any optimization changes."
---

# Performance Forensics

Use when the user asks to investigate latency, throughput, memory, CPU, IO, caching, batching, polling, locks, concurrency, or scalability before implementing optimization.

## Default posture

Read-only by default. Prefer measurements over intuition. Do not optimize, refactor, tune configs, or edit code until implementation is requested and the bottleneck is evidence-backed.

## Workflow

1. Define question, metric, baseline, workload, environment, and acceptable variance.
2. Map suspected hot path and resource boundary.
3. Gather or request benchmarks, profiles, traces, metrics, logs, or focused diagnostics.
4. Rank hypotheses by bottleneck, evidence, counter-evidence, next measurement, and expected impact.
5. Return `../engineering-team/templates/performance-forensics-report.md` plus a next-probe plan.

## Useful specialists

Use performance investigation for measurement design, runtime tracing for call/concurrency paths, observability review for production signals, and Evidence Skeptic for confounders or invalid benchmarks.

## Required output

Return baseline/measurement notes, hot-path evidence, ranked bottleneck hypotheses, confidence, next probes, and implementation candidates only when labeled as unimplemented recommendations.
