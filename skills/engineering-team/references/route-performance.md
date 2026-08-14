# Performance Route

Use for read-only investigation of latency, throughput, CPU, memory, allocations, IO, caching, batching, polling, locks, contention, concurrency, and scalability.

## Authority

Remain read-only and measurement-first. Do not optimize, refactor, tune production configuration, or edit benchmarks until the bottleneck and measurement validity are evidence-backed and implementation is authorized.

## Workflow

1. Define the metric, baseline, workload, environment, variance, comparison point, and acceptable outcome.
2. Validate that the measurement exercises the real path and controls important confounders.
3. Map the suspected hot path and resource boundary. For regressions or causal claims, load `references/diagnosis-loop.md` under its read-only boundary.
4. Gather or design the smallest useful benchmark, profile, trace, metric query, or diagnostic probe.
5. Rank bottleneck hypotheses by evidence, counter-evidence, next measurement, expected impact, and second-order risk.
6. Use Optimization Engineer for measurement and hot-path judgment, Test Verification Engineer for benchmark validity, Release Rollback Engineer for production measurement risk, and Evidence Skeptic for confounders.

## Output

Return `templates/performance-forensics-report.md` plus `templates/next-probe-plan.md` when more evidence is needed. Include baseline quality, hot-path evidence, ranked hypotheses, confidence, measurement gaps, and implementation candidates clearly labeled as unimplemented.
