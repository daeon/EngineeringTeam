# Codebase Analysis Route

Use for read-only repository understanding: architecture, components, ownership, entry points, call paths, contracts, risks, and improvement opportunities.

Use L1 only for a bounded orientation with no repository-wide claims; use L2 for one component/workflow, L3 when behavioral contracts cross boundaries, and L4 for repository-wide architecture or multi-component conclusions.

## Authority

Remain read-only. Do not edit source, tests, docs, generated files, configuration, or project memory. A broad analysis may still require L2-L4 rigor; read-only does not imply L0.

## Workflow

1. Define the question, scope, and non-goals.
2. Build the Repo Atlas: system type, instructions, entry points, build/test commands, generated-code rules, and major components.
3. Narrow to the owning component: files, symbols, call paths, inputs, outputs, side effects, and nearby tests.
4. Trace producer-to-consumer contracts when the requested claim depends on behavior across a boundary.
5. Record each major claim with a path, symbol, command, test, or documented behavior and confidence.
6. Use Codebase Investigator for unknown ownership, System Design Architect for boundary/design judgment, and Evidence Skeptic when evidence conflicts or broad conclusions matter.

## Output

Return `templates/codebase-analysis-report.md`: scope, repo/component map, call paths and contracts, evidence-backed findings, risks, unknowns, confidence, and next probes. Keep descriptive mapping separate from implementation recommendations.
