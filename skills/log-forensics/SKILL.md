---
name: log-forensics
description: "Use for read-only log analysis: parse log samples, reconstruct timelines, identify signals, correlate symptoms, and produce evidence-backed forensic reports without editing files."
---

# Log Forensics

Use when the user provides logs or asks to analyze operational traces, incidents, alerts, metrics excerpts, or error streams.

## Default posture

Read-only by default. Treat logs as sensitive: redact secrets, tokens, and private data; summarize high-volume logs instead of pasting them.

## Workflow

1. Identify sources, time windows, services, request IDs, hosts, versions, and gaps.
2. Normalize events into a timeline.
3. Classify errors, warnings, retries, latency, saturation, deploy changes, dependency failures, and user impact.
4. Correlate events with code paths or operational boundaries when repo context exists.
5. Record confidence and missing probes.
6. Return `../engineering-team/templates/log-forensics-report.md`; add a next-probe plan when evidence is incomplete.

## Useful specialists

Use log forensics for timeline/signal extraction, observability review for telemetry gaps and alert quality, and Evidence Skeptic for correlation-versus-causation checks.

## Required output

Return a concise report with timeline, findings, evidence snippets or references, likely failure modes, ruled-out causes, redactions applied, and next probes. Avoid long verbatim log dumps.
