# Analysis Report

Canonical deliverable for L0 evaluative tasks: audits, feedback requests,
"what could be improved", risk reviews, and PR/diff reviews that produce
findings only. Replaces the Final Report when no code edits are planned.
Produce it after a lightweight Repo Atlas, then run Context GC.

For descriptive "understand/map how this repo works" requests, use the
Codebase Analysis Report (`templates/codebase-analysis-report.md`) via the
`codebase-analysis` skill instead.

Every finding must reference a file path, line number, command output, or
documented behavior. Label unverified claims as assumptions.

> Anti-pattern: listing vague impressions with no evidence, or mixing in an
> implementation plan that belongs in an L2+ Final Report.

## What works well
<!-- Concrete, evidence-backed observations. Path + reason. -->
<!-- e.g. "scripts/generate-agents.py --check catches drift in CI: confirmed by .github/workflows/validate.yml line 20." -->

## Key findings

| Finding | Severity | Evidence | Location |
|---|---|---|---|
| <!-- short description --> | <!-- high / medium / low --> | <!-- file:line, command output, doc quote --> | <!-- path or component --> |

<!-- Severity: high = correctness / security / trust; medium = maintainability / DX; low = style / optional -->

## Improvement candidates
<!-- Prioritized list. One line each: what, why it matters, rough effort. -->
<!-- e.g. "1. Fix SECURITY.md contradiction with hooks.json — high trust impact, one-paragraph edit." -->

## Verification performed
<!-- Commands run and their results. Evidence that findings are real, not guesses. -->
<!-- e.g. "python3 scripts/doctor.py → 12/12 OK; npm run validate → clean." -->

## Follow-ups
<!-- Open questions, deferred investigations, or work that would require L2+ autonomy. -->
