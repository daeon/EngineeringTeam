---
name: blast-radius
description: Determine what a change could break beyond the visible diff and prove the key safety invariant with runnable evidence. Use for risky small changes, hidden coupling, compatibility concerns, or "what else could this break?"
---

# Blast radius

Find downstream breakage that a symbol search alone will miss. The deliverable is not a long risk list. It is a small set of real risks plus executable evidence for the fact the change depends on.

## Core question

Ask:

> What single invariant, if false, would make this change unsafe?

Examples:

- a cleanup callback runs only after all readers have released the object;
- a renamed field never crosses the public wire format;
- a cache invalidation removes only entries already unreachable to callers;
- callers never observe the temporary intermediate state.

Find that invariant and prove it as strongly as practical.

## Evidence ladder

For each material safety claim, report the strongest level reached:

1. **Claimed.** Reasoning only. Not sufficient for a merge-critical fact.
2. **Located.** Concrete source, schema, version, or contract evidence.
3. **Failure path traced.** The bad case was walked end to end and shown to terminate or remain unreachable.
4. **Executed.** A focused script or test exercised the real production path and failed loudly if the invariant was false.
5. **Live.** The behavior was reproduced in the running product or realistic integration environment.

Do not silently round level 2 or 3 up to "verified." If an important claim cannot reach executable evidence cheaply, mark it `UNPROVEN`.

## Workflow

1. **Read the change.** Identify changed symbols, deleted behavior, new ordering, new state, and assumptions not obvious from the diff.
2. **Map visible dependents.** Find direct callers, consumers, tests, schemas, feature flags, config, generated code, and versions.
3. **Look where grep stops.** Trace serialized data, database columns, network formats, dynamic registration, reflection, framework lifecycle, other languages, asynchronous ordering, external library semantics, and downstream jobs.
4. **Name the safety invariant.** Prefer one or two decisive facts over ten vague worries.
5. **Try to falsify it.** Construct the cheapest realistic bad case. Read dependency source or pinned versions when behavior depends on third-party semantics.
6. **Run the proof.** Prefer a script or focused test that uses the same code path the product uses. Keep the proof artifact when it will help review or regression prevention.
7. **Classify risks.** Separate confirmed risks, plausible-but-unproven risks, and cleared concerns.
8. **Escalate breadth when justified.** For a wide or one-way-door change, run independent reviewers or an `arena`-style analysis and merge only evidence-backed findings.

## Output

- **What changed.** Include non-obvious semantic changes.
- **Safety invariant.** The one or two facts the change depends on, with evidence level and proof.
- **Risks.** Mechanism, likelihood, impact, evidence, and cheapest check.
- **Cleared concerns.** Things investigated and why they are safe.
- **Before merge.** The smallest repeatable check that would catch the real failure.

A convincing explanation without a runnable check is not proof.
