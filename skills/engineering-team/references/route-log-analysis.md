# Log Analysis Route

Use for read-only analysis of logs, incidents, alerts, metrics excerpts, operational traces, request flows, and noisy diagnostic output.

## Authority

Remain read-only. Treat logs as sensitive: redact secrets, credentials, tokens, private data, and unnecessary identifiers. Summarize high-volume evidence instead of reproducing raw dumps.

## Workflow

1. Identify sources, time windows, clocks/time zones, services, hosts, versions, request IDs, deployments, and missing intervals.
2. Normalize events into a timeline without erasing uncertainty or clock skew.
3. Classify errors, warnings, retries, latency, saturation, dependency failures, deploy changes, and user impact.
4. Correlate signals with code or operational boundaries when repository context exists.
5. Distinguish correlation from causation; load `references/diagnosis-loop.md` before making root-cause claims.
6. Use Release Rollback Engineer for production/observability concerns, Security Analyst for sensitive-data exposure, Optimization Engineer for saturation/latency, and Evidence Skeptic for causal claims.

## Output

Return `templates/log-forensics-report.md`: scope and redactions, timeline, findings, evidence references, likely failure modes, ruled-out claims, gaps, confidence, and next probes. Add `templates/next-probe-plan.md` when evidence cannot discriminate the leading explanations.
