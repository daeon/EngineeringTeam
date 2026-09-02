---
name: unslop
description: Remove mechanical AI-writing patterns while preserving meaning, technical precision, and a natural human voice. Use for documentation, explanations, PR text, reviews, and other prose that feels generic, inflated, repetitive, or machine-shaped.
---

# Unslop

Make prose sound like a competent person wrote it for a real reader. Remove AI tells without flattening the text into sterile corporate copy.

## Priorities

1. Preserve facts, constraints, obligations, uncertainty, and technical meaning.
2. Cut words and structure that add no information.
3. Prefer concrete nouns, verbs, numbers, symbols, paths, and examples.
4. Match the intended channel and author voice.
5. Keep some rhythm and opinion when the genre allows it.

## Common patterns to remove

### Empty importance

Cut ceremonial framing such as "it is important to note," "a pivotal step," "in today's landscape," "serves as," or generic conclusions that could fit any project.

### Vague authority

Replace "experts say," "industry reports suggest," and similar attributions with a named source or remove the claim.

### Inflated vocabulary

Prefer the ordinary precise word. Use `use` instead of `utilize`, `help` instead of `facilitate`, `move` instead of metaphorical verbs, and the repository's real term instead of an invented synonym.

### Generic abstraction

Replace claims such as "improves robustness" with the mechanism or observation: retries stop after three attempts; a schema mismatch fails validation; median startup drops from 410 ms to 300 ms.

### Formulaic structure

Watch for forced trios, repeated "not only X but Y" constructions, identical paragraph rhythms, unnecessary headings, excessive bold lead-ins, and lists created only to make the answer look organized.

### Mechanical hedging

Reduce stacked qualifiers. Keep uncertainty that matters, but say `may`, `likely`, or `unknown` once rather than wrapping the claim in several layers of caution.

### Punctuation habits

Avoid relying on em dashes, colons, parentheses, or semicolons as a repeated structural crutch. Do not ban punctuation that is natural to the author's style; fix repetition and ambiguity rather than enforcing a gimmick.

### Chatbot residue

Remove canned phrases such as "Great question," "Certainly," "I hope this helps," automatic praise, and invitations that add nothing to the requested artifact.

## Add human signal

After cutting slop, check that the prose still has a point of view appropriate to the genre.

- Vary sentence length naturally.
- State tradeoffs instead of listing symmetrical pros and cons when evidence supports a judgment.
- Use first person when the author owns a recommendation or observation.
- Prefer a specific example over a generic adjective.
- Repeat the same technical term when it names the same thing; do not synonym-cycle for variety.

## Workflow

1. Identify the audience, channel, and non-negotiable meaning.
2. Mark generic, inflated, repetitive, vague, or mechanically structured passages.
3. Rewrite with concrete language and fewer words.
4. Check that terminology, numbers, constraints, links, and normative force did not drift.
5. Read once for voice. Restore useful texture if cleanup made the prose unnaturally flat.

## Output rule

Return the revised prose, not a lecture about the rules, unless the user asks for a critique or change log.
