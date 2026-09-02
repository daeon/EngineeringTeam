---
name: technical-writing
description: Write or review developer-facing docs, RFCs, READMEs, PR descriptions, commit messages, and operational guides using task-appropriate structure, plain technical language, and ambiguity-resistant sentences. Use `standard-english` first when formal standards or conformance govern the wording.
---

# Technical writing

Write for a tired engineer who needs to understand the point on the first read.

This skill handles ordinary developer-facing prose. If the task involves formal standards, controlled language, normative keywords, regulated wording, accessibility conformance, legal obligations, localization governance, or a named profile, route through `standard-english` first. Governing standards outrank this style layer.

## Pick the document mode first

Use one primary mode per document and split when purposes conflict:

- **Tutorial:** learning by doing. Every step produces visible progress.
- **How-to:** accomplish a concrete task. Assume competence and keep background brief.
- **Reference:** facts for lookup. Mirror the structure of the system and avoid persuasion.
- **Explanation:** build understanding of one bounded topic, including tradeoffs and rationale.

Do not bury reference catalogs in tutorials or turn reference pages into essays.

## Sentence rules

- Address the reader directly when giving instructions.
- Use active voice when the actor matters.
- Put conditions before the step they control.
- Use commands for procedures.
- Keep one main instruction or claim per sentence when splitting improves clarity.
- Prefer present tense for current behavior.
- Use the repository's exact symbols, commands, fields, filenames, and UI labels.
- Use one term for one concept. Avoid synonym cycling.
- Put `only`, `not`, and similar modifiers next to what they modify.
- Make pronoun references unambiguous; repeat the noun when needed.
- Break long noun stacks into clauses.
- Prefer periods to punctuation-heavy sentences when a sentence carries several logical turns.

## Information design

- Lead with what changes for the reader before implementation detail.
- Put the common path before exceptions.
- Use numbered lists only for sequences. Use bullets for genuinely parallel items.
- Make headings carry information, not just topic labels.
- Show expected output or observable state for procedures when practical.
- Link to deeper explanation rather than interrupting a task guide with background.
- Generate factual catalogs from source when possible so they stay synchronized.

## Precision rules

Cut any word that does no work, but do not shorten away conditions, exceptions, thresholds, or obligations.

Prefer:

- concrete mechanisms over adjectives;
- measured deltas over adverbs such as "significantly";
- exact paths and symbols over vague descriptions;
- explicit actors over passive constructions that hide responsibility;
- examples that expose a real failure mode over generic examples.

Do not call a task easy, simple, obvious, or quick merely because the author understands it.

## Repository prose

PR descriptions and commit messages are technical writing too. They should state:

- the problem or behavior change;
- the important design choice or invariant;
- how it was verified;
- any residual risk or deliberate non-goal.

Do not churn unchanged wording merely to sound different.

## Workflow

1. Identify audience, goal, document mode, and governing sources.
2. Gather the real symbols, commands, behavior, and constraints from the repository or supplied evidence.
3. Draft the information structure before polishing sentences.
4. Apply the sentence and precision rules.
5. Run `unslop` if available, but preserve technical meaning and the selected document mode.
6. Validate commands, paths, links, examples, counts, and claims against the current artifact when practical.

## Review checklist

- Does the document have one clear primary mode?
- Can the reader find the action or fact they came for quickly?
- Does each instruction say exactly what to do and under what condition?
- Are names, commands, symbols, and counts real at this revision?
- Did any simplification change a constraint, exception, or obligation?
- Does the same concept keep the same name?
- Can any sentence be read in two materially different ways?
- Did `unslop` improve the prose without making it sterile?
