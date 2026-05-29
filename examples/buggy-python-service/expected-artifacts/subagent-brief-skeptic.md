# Subagent Brief

## Role

`evidence_skeptic`

## Mission

Challenge the proposed fix: verify that converting discount from percent to fraction at the API boundary is the correct and complete fix, and that no other callers or tests depend on the current percent behavior.

## Context budget

`component-context`

## Allowed tools

Read/search only. No edits.

## Inputs

- User task: investigate checkout discount bug
- Current plan: convert `discount` from percent to fraction in `src/api.py` before passing to `pricing.py`
- Relevant paths: `src/api.py`, `src/pricing.py`, `tests/test_api.py`, `tests/test_pricing.py`
- Known constraints: domain contract in `src/pricing.py` expects fraction (0.0–1.0)
- Exclusions: do not inspect unrelated repo package files

## Output limit

Max 300 words.

## Required output

| Finding | Evidence | Confidence | Follow-up |
|---|---|---:|---|

## Do not

- Do not edit files.
- Do not include raw file dumps.
- Do not summarize unrelated repo areas.
- Do not claim ownership without evidence from paths, symbols, callers, tests, or docs.
- Do not expand scope without reporting the trigger.
