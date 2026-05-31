# Subagent Brief

## Role

`<agent_name>`

## Mission

| Mission | Evidence | Confidence | Risk / impact | Next action |
|---|---|---:|---|---|
| One bounded question the subagent must answer |  |  |  |  |

## Context budget

`brief-only | component-context | artifact-context | full-context`

## Allowed tools

| Tool boundary | Evidence | Confidence | Risk | Next action |
|---|---|---:|---|---|
| Read/search only |  |  |  |  |
| Command execution allowed / not allowed |  |  |  |  |
| File edits allowed / not allowed |  |  |  |  |

## Inputs

| Input | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
| User task |  |  |  |  |
| Current risk mode |  |  |  |  |
| Relevant paths |  |  |  |  |
| Relevant artifacts |  |  |  |  |
| Known constraints |  |  |  |  |
| Exclusions |  |  |  |  |

## Output limit

Return max `<N>` words plus required tables.

## Required output

| Finding | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  |  |  |  |

## Do not

| Constraint | Evidence | Confidence | Risk | Next action |
|---|---|---:|---|---|
| Do not edit files unless explicitly assigned as Implementation Engineer after the implementation gate. |  | Proven | Unreviewed edits | Respect boundary |
| Do not include raw file dumps. |  | Proven | Context bloat | Summarize with citations |
| Do not summarize unrelated repo areas. |  | Proven | Scope creep | Stay bounded |
| Do not claim ownership without evidence from paths, symbols, callers, tests, or docs. |  | Proven | Wrong seam | Cite evidence |
| Do not expand scope without reporting the trigger. |  | Proven | Hidden risk | Report trigger first |
