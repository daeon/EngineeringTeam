# Subagent Brief

## Role

`<agent_name>`

## Mission

One bounded question the subagent must answer.

## Context budget

`brief-only | component-context | artifact-context | full-context`

## Allowed tools

- Read/search only
- Command execution allowed / not allowed
- File edits allowed / not allowed

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

| Finding | Evidence | Confidence | Follow-up |
|---|---|---:|---|

## Do not

- Do not edit files unless explicitly assigned as Implementation Engineer after the implementation gate.
- Do not include raw file dumps.
- Do not summarize unrelated repo areas.
- Do not claim ownership without evidence from paths, symbols, callers, tests, or docs.
- Do not expand scope without reporting the trigger.
