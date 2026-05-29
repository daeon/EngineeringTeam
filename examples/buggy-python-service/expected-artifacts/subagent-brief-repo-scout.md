# Subagent Brief

## Role

`codebase_investigator`

## Mission

Find where discount handling enters the service, where it is transformed, and which component owns the boundary.

## Context budget

`component-context`

## Allowed tools

Read/search only. No edits.

## Inputs

- User task: investigate checkout discount bug
- Known symptom: non-zero discount raises `ValueError`
- Relevant paths: `examples/buggy-python-service/`
- Exclusions: do not inspect unrelated repo package files

## Output limit

Max 300 words.

## Required output

| Finding | Evidence | Confidence | Follow-up |
|---|---|---:|---|
