# Repo Atlas

Build a shallow repo map before focusing on the requested area.

## What to look for

- `AGENTS.md`, `CLAUDE.md`, repo-local skill docs, harness instructions
- `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/adr/` for domain language and prior decisions
- `README.md`, `CONTRIBUTING.md`, architecture docs
- build files, package manifests, dependency files
- test configuration and CI configuration
- source roots, scripts, tools, codegen definitions
- route/entry-point files
- config/schema files

## Domain docs and ADRs

Treat domain docs as a soft dependency: use them when present, do not block work when absent. If `CONTEXT.md` defines project terms, use that vocabulary in artifacts, plans, tests, and final reports. If ADRs exist near the touched area, respect them unless current evidence justifies reopening the decision. See `references/domain-context.md` for glossary and ADR rules.

## Structured intelligence over raw reads

Prefer:
- file tree summary
- symbol index
- import/dependency graph
- test map
- route/handler map
- config/schema map
- generated-code map
- external integration map

## Artifact: Repo Atlas

Required for L2+ tasks. For L0 analysis tasks, a concise prose summary with file-path-backed evidence is sufficient.

```md
# Repo Atlas

## System Type
## Main Languages / Frameworks
## Runtime / Build Model
## Main Components
## Entry Points
## Test Surfaces
## Domain Context
## Relevant ADRs
## Generated Code Rules
## Config / Schema Sources
## External Integration Points
## Known High-Risk Areas
## Repo-Specific Instructions
## Build / Test Commands
## Last Verified
```

## Rules

- Keep the atlas concise.
- Prefer code and executable commands over stale docs.
- Cite file paths and symbols for every important claim.
- Expand context only when it reduces implementation or verification risk.
- Do not persist one-off task details as durable repo knowledge.
