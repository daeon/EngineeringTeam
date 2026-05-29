---
name: codebase-analysis
description: "Use for read-only repository understanding: map architecture, components, ownership, call paths, contracts, risks, and improvement opportunities without editing files."
---

# Codebase Analysis

Use this skill when the user asks to understand, audit, explain, or map a codebase without requesting a code change.

## Default posture

Read-only by default. Do not edit source, tests, docs, generated files, configs, or memory unless the user explicitly changes the task to implementation mode.

## Workflow

1. Confirm the analysis question and non-goals.
2. Build a repo map: system type, entry points, build/test commands, generated-code rules, and major components.
3. Build a component map for the requested area: owners, files, symbols, call paths, inputs, outputs, side effects, and nearby tests.
4. Trace important contracts: producer, data/API/config shape, consumer, failure mode, and evidence.
5. Record claims in an evidence ledger with source paths, line numbers, commands, and confidence.
6. Return a codebase analysis report using `../engineering-team/templates/codebase-analysis-report.md`.

## Useful specialists

- Codebase Cartographer for broad repository mapping.
- System Design Architect for boundaries, dependency direction, and long-term design risks.
- Evidence Skeptic when claims depend on inference, stale docs, or conflicting sources.

## Required output

A compact, evidence-backed report with:

- scope and question answered
- architecture/component map
- key call paths and contracts
- risks, unknowns, and confidence
- suggested next probes or optional implementation follow-ups

Label unverified claims as assumptions. Prefer citations to files and commands over prose confidence.
