---
name: codebase-analysis
description: "Use for read-only repository understanding: map architecture, components, ownership, call paths, contracts, risks, and improvement opportunities without editing files."
---

# Codebase Analysis

Use when the user asks to understand, audit, explain, or map a codebase without a requested code change.

## Default posture

Read-only by default. Do not edit source, tests, docs, generated files, configs, or memory unless the user changes the task to implementation mode.

## Workflow

1. Confirm the question and non-goals.
2. Map repo shape: system type, entry points, build/test commands, generated-code rules, major components.
3. Map the focused component: owners, files, symbols, call paths, inputs/outputs, side effects, nearby tests.
4. Trace contracts: producer, shape, consumer, failure mode, evidence.
5. Record claims with source paths, line numbers, commands, and confidence.
6. Return `../engineering-team/templates/codebase-analysis-report.md`.

## Useful specialists

Use a cartographer for broad maps, System Design Architect for boundaries/design risk, and Evidence Skeptic for inference, stale docs, or conflict.

## Required output

A compact, evidence-backed report with scope, architecture/component map, call paths/contracts, risks/unknowns/confidence, and next probes or optional implementation follow-ups. Label assumptions and prefer file/command evidence over prose confidence.
