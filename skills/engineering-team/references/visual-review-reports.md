# Visual Review Reports

Use visual reports when a human reviewer benefits from layout, diagrams, side-by-side comparisons, or grouped findings more than from a plain markdown handoff.

Good fits:

- architecture reviews
- complex refactor candidates
- performance investigations with several bottlenecks
- migration impact maps
- release or rollback timelines
- cross-component contract graphs

Do not use a visual report for routine local edits or when the user requested a concise text answer only.

## Output location

Write self-contained reports to the OS temp directory, not the repository, unless the user explicitly asks for a repo artifact.

Use a fresh timestamped filename, for example:

```text
engineering-team-review-20260528-2015.html
```

## Format

The report may use:

- Tailwind via CDN for layout
- Mermaid via CDN for graph-shaped relationships
- small hand-authored HTML/CSS for cards, timelines, and before/after comparisons

Keep it self-contained. Do not require a build step.

## Required sections

```md
## Summary
## Evidence
## Before / After Or Current / Proposed
## Risks
## Recommendation
## Verification Or Follow-up
```

## Dataflow

```text
repo evidence -> grouped findings -> visual relationships -> recommendation -> verification or follow-up
```

Visuals must clarify evidence. Do not add diagrams as decoration.
