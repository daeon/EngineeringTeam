---
name: how
description: Explain how a subsystem, feature flow, module, or runtime path works from source evidence. Use for code walkthroughs, ownership questions, runtime flow, layering, and onboarding mental models. Use `why` for historical motivation.
---

# How

Build a working mental model of the code from evidence. Explain behavior and structure without inventing motivation.

## Modes

- `explain` is the default. Trace the subsystem and explain it clearly.
- `critique` first performs the full explanation, then pressure-tests the architecture.

## Workflow

1. **Frame the target.** State the subsystem, behavior, or ownership question you are answering. If context is ambiguous, choose the most plausible interpretation, state it briefly, and proceed.
2. **Choose exploration depth.** For a narrow module, inspect directly. For a cross-cutting subsystem, split exploration into 2-4 non-overlapping angles such as entry points, state/data model, runtime flow, configuration, or persistence. Use parallel read-only explorers when the harness supports them.
3. **Trace real code.** Start from an entry point and follow callers, callees, types, state transitions, side effects, and external boundaries until the path from trigger to effect is explicit. Read implementations; do not infer behavior from filenames or symbols alone.
4. **Reconcile the model.** Resolve contradictions between explorers against source. Mark unresolved gaps rather than smoothing them over.
5. **Explain for a maintainer.** Prefer the smallest set of concepts needed to work safely in the area. Name concrete files and symbols so the reader can verify the explanation.

## Critique mode

After the explanation is stable, ask independent reviewers to challenge the architecture from the same evidence. Use a common rubric and keep reviewers read-only. The lead categorizes findings as `ACT`, `CONSIDER`, `NOTED`, or `DISMISSED`; model agreement is a signal to inspect, not proof.

Useful critique lenses include ownership, coupling, information leakage, state lifetime, boundary placement, concurrency, testability, interface depth, and change cost.

## Output

Use only the sections that help:

- **Overview.** What the subsystem does and where it fits.
- **Key concepts.** The types, services, data structures, or invariants needed to understand it.
- **How it works.** Trigger-to-effect flow, including decisions and side effects.
- **Where it lives.** The few files or modules that matter most.
- **Gotchas.** Surprising behavior, hidden coupling, lifecycle constraints, or incomplete evidence.
- **Critique.** Only in critique mode; categorized findings with evidence.

Do not answer "why was it designed this way?" from code shape alone. Route that question to `why`.
