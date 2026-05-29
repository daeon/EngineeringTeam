---
name: log-forensics
description: "Use for read-only log analysis: parse log samples, reconstruct timelines, identify signals, correlate symptoms, and produce evidence-backed forensic reports without editing files."
---

# Log Forensics

Use this skill when the user provides logs or asks to analyze operational traces, incidents, alerts, metrics excerpts, or error streams.

## Default posture

Read-only by default. Treat logs as potentially sensitive. Do not expose secrets, tokens, private user data, or raw high-volume logs in the final response. Redact sensitive values and summarize patterns.

## Workflow

1. Identify log sources, time windows, services, request IDs, hosts, versions, and sampling gaps.
2. Normalize events into a timeline.
3. Classify signals: errors, warnings, retries, latency, saturation, deployment changes, dependency failures, and user-visible impact.
4. Correlate events with code paths or operational boundaries when repository context is available.
5. Record confidence and missing probes.
6. Return a log forensics report using `../engineering-team/templates/log-forensics-report.md` and a next-probe plan when evidence is incomplete.

## Useful specialists

- Log Forensics Analyst for timeline reconstruction and signal extraction.
- Observability Architect for telemetry gaps, metrics/traces, and alert quality.
- Evidence Skeptic for correlation-versus-causation checks.

## Required output

Return a concise report with timeline, findings, evidence snippets or references, likely failure modes, ruled-out causes, redactions applied, and next probes. Avoid long verbatim log dumps.
