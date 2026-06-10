# Subagent Brief

Use the quick form for routine read-only delegations. Use the full form when the mission is L3+, has many inputs or exclusions, or grants edit or command permissions.

## Quick form

```md
- Role: <agent_name>
- Mission: <one bounded question>
- Context budget: brief-only | component-context
- Boundaries: read-only; no raw dumps; stay in scope; report scope-expansion triggers
- Return: context capsule, max <N> words
```

## Role

`<agent_name>`

## Mission

One bounded question the subagent must answer, and what a complete answer looks like.

## Context budget

`brief-only | component-context | artifact-context | full-context`

## Allowed tools

- Read/search: allowed
- Command execution: allowed | not allowed
- File edits: allowed | not allowed

## Inputs

- User task:
- Current risk mode:
- Relevant paths:
- Relevant artifacts:
- Known constraints:
- Exclusions:

## Output limit

Return max `<N>` words plus required tables.

## Required output

A context capsule (`templates/context-capsule.md`) whose findings are evidence-backed:

| Finding | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  |  |  |  |

## Do not

- Do not edit files unless explicitly assigned as Implementation Engineer after the implementation gate.
- Do not include raw file dumps; summarize with citations.
- Do not summarize unrelated repo areas.
- Do not claim ownership without evidence from paths, symbols, callers, tests, or docs.
- Do not expand scope without reporting the trigger first.
