---
name: standardized-language
description: "Select and apply the smallest useful language-standard profile for technical, public, legal, scientific, requirements, safety, accessibility, localization, and product-documentation tasks. Route by audience, document type, consequence, normative force, domain, and evidence. Ask for confirmation only when competing profiles materially change meaning, obligations, safety, or compliance scope. Never claim formal compliance without authoritative source material and human review."
---

# Standardized Language

Route writing, rewriting, drafting, review, and audit tasks to the most appropriate language standard or style profile. Use the smallest combination that covers the real communication risks. Do not stack standards merely because they are related.

Invocation: mention `standardized-language`, choose it from `/skills`, or let the harness select it for language-standard, controlled-language, plain-language, requirements-writing, safety-writing, documentation-style, accessibility, or terminology tasks.

## Default posture

Select the smallest authoritative profile that preserves meaning and serves the reader. Make routine routing decisions automatically. Ask for confirmation only when competing profiles materially change obligations, safety, normative force, or compliance scope.

## Core rule

Select standards from the task, not from the user's vocabulary alone.

Before writing, classify:

```text
purpose → audience → document type → normative force → consequence → domain → channel → localization → evidence available
```

Then choose:

1. one **primary profile** that governs the communication outcome;
2. zero or one **domain profile** for the document type;
3. zero or one **constraint profile** for terminology, accessibility, safety, translation, or normative keywords.

Use more than three profiles only when the task clearly spans independent risks. Explain the extra profile briefly.

## Fast path

Apply automatically when all of these are clear:

- the document type is explicit;
- one profile is an obvious primary fit;
- the profile will not change legal obligations, safety meaning, or normative force;
- no formal compliance claim is requested;
- enough source content and context are available.

State the selected profile in one line, then perform the task.

Example:

```text
Selected profile: ISO 24495-1 principles + Google developer-documentation conventions, because this is task-oriented API guidance for software developers.
```

## Confirmation gate

Do not ask for confirmation merely because several standards could improve the text. Recommend and proceed with the best-fit profile when differences are stylistic or low consequence.

Recommend a ranked choice and ask the user to confirm before rewriting or auditing when any of these are true:

- legal rights, duties, liability, consent, or regulatory interpretation may change;
- safety wording, hazard severity, prohibited action, or emergency action may change;
- the choice between RFC-style and ISO-style normative keywords changes requirement interpretation;
- the user requests formal compliance or certification;
- a controlled-language profile could remove technically necessary nuance;
- jurisdiction, regulated industry, or intended audience is materially unclear;
- two top profiles score nearly equally but produce meaningfully different output;
- the authoritative standard text, licensed excerpt, internal checklist, or approved glossary is unavailable and the user wants a conformance audit.

Use this compact confirmation format:

```text
Recommended: <profile A> — <reason>.
Alternative: <profile B> — <when it is better>.
Material difference: <what changes>.
Confirm which profile to apply: A or B.
```

If the user does not respond and the task must still progress, produce a clearly labeled recommendation or sample. Do not present it as the final compliant rewrite.

## Confidence model

Score the routing decision internally:

- **High confidence** — one profile clearly dominates and no material-risk gate applies: select and execute.
- **Medium confidence** — one profile is best but a secondary profile is plausible: recommend the best profile, state the assumption, and execute unless a material-risk gate applies.
- **Low confidence** — missing information could change obligations, safety, normative interpretation, or compliance scope: recommend ranked options and request confirmation.

Do not expose numeric pseudo-precision. Use High, Medium, or Low only when useful.

## Workflow

1. Identify the user's intended outcome: draft, rewrite, simplify, standardize, translate, review, audit, compare, or build a reusable rule profile.
2. Extract task dimensions using `./references/selection-matrix.md`.
3. Select candidate profiles from `./references/standards-catalog.md`.
4. Eliminate profiles that are redundant, unavailable, jurisdictionally inappropriate, or too restrictive.
5. Choose the primary, domain, and constraint profiles.
6. Apply the confirmation gate.
7. Execute using `./references/output-contract.md`.
8. Report unresolved ambiguity, terminology gaps, and any rule conflicts.

## Default routing priorities

When no special domain dominates, prefer this order:

1. preserve technical, legal, and safety meaning;
2. satisfy the intended reader's task;
3. use authoritative terminology consistently;
4. make information findable, understandable, and usable;
5. make requirements testable and normative force explicit;
6. improve accessibility and localization readiness;
7. improve brevity and style.

Never simplify at the cost of precision.

## Standard families

Load `./references/standards-catalog.md` for the full catalog. The main families are:

| Need | Typical primary or supporting profile |
|---|---|
| general plain language | ISO 24495-1; CAN-ASC-3.1 for Canadian public communication |
| controlled technical English | ASD-STE100 |
| product instructions and manuals | IEC/IEEE 82079-1 |
| software user documentation | ISO/IEC/IEEE 26514 plus a developer style guide |
| requirements and specifications | ISO/IEC/IEEE 29148 plus RFC 2119/8174 or ISO Directives Part 2 |
| terminology control | ISO 704; TBX/ISO 30042 for exchange formats |
| accessible digital content | WCAG 2.2; W3C COGA guidance |
| legal communication | ISO 24495-2 plus jurisdiction-specific legal review |
| scientific communication | ISO 24495-3 |
| safety messages | ANSI Z535.6/Z535.7 or the applicable jurisdictional/product safety framework |
| translation post-editing | ISO 18587 plus an approved terminology resource |
| Canadian public content | CAN-ASC-3.1 and Canada.ca guidance |
| developer documentation | Google Developer Documentation Style Guide or Microsoft Writing Style Guide |

## Normative-language rule

Choose one normative keyword system for a document unless an external contract requires another:

- Internet and software protocol specifications: RFC 2119 + RFC 8174 using uppercase `MUST`, `SHOULD`, and `MAY`.
- ISO-like standards and formal specifications: ISO Directives Part 2 using `shall`, `should`, `may`, and `can` with distinct meanings.

Do not silently convert between systems. Flag mixed systems as a defect unless the document explicitly defines both.

## Source and compliance boundary

Many standards are copyrighted, licensed, revised, or domain-specific. Model memory and public summaries are not authoritative conformance sources.

Therefore:

- Apply publicly known principles and user-provided rules as a **profile**.
- Use the user's licensed excerpt, approved checklist, glossary, or organization policy when available.
- Do not reproduce substantial copyrighted standard text.
- Do not claim `compliant`, `certified`, or `conformant` unless the required authoritative material and validation process are available.
- Prefer wording such as `edited using`, `aligned with`, `checked against the supplied profile`, or `candidate violations`.
- For safety, legal, regulated, or high-consequence content, require qualified human review in the final report.

## Glossary authority

When a glossary, termbase, schema, API definition, UI string catalog, or product taxonomy is supplied, treat it as authoritative unless it conflicts with a higher-order legal or safety source.

For each concept:

- use one preferred term;
- preserve exact product, API, command, field, and UI labels;
- list deprecated, forbidden, or ambiguous synonyms;
- do not invent expansions for acronyms;
- flag new terms rather than normalizing them silently.

## Rewrite discipline

During rewriting:

- preserve facts, conditions, exceptions, thresholds, actors, permissions, prohibitions, and sequence;
- separate instructions from explanations;
- use one primary action per procedural step;
- replace vague modifiers with measurable criteria when evidence exists;
- flag ambiguity when evidence does not exist;
- never manufacture requirements, definitions, warnings, or guarantees;
- keep examples visibly non-normative unless the source says otherwise;
- retain necessary technical terms and define them for the audience instead of deleting them.

## Audit discipline

An audit must distinguish:

1. **confirmed issue** — directly supported by the supplied rule profile or authoritative text;
2. **candidate issue** — likely under the selected profile but requires authoritative verification;
3. **content ambiguity** — the source meaning is unclear;
4. **domain decision** — a subject-matter expert must decide;
5. **preference** — optional style improvement, not a violation.

Do not inflate preference differences into compliance failures.

## Required output

Always identify the selected profile or recommendation, preserve source meaning, and surface unresolved ambiguity. Use the output mode that matches the user request.

## Output modes

Use the matching mode from `./references/output-contract.md`:

- **Route only** — recommend standards and explain material differences.
- **Rewrite** — return revised text plus assumptions and unresolved ambiguities.
- **Audit** — return findings with severity, evidence, proposed correction, and confidence.
- **Rewrite + audit** — return the clean text first, then a compact change report.
- **Profile builder** — produce a reusable organization-specific rule profile from authoritative inputs.

## Failure modes

- Selecting ASD-STE100 for all technical writing even when audience usability is the real problem.
- Applying plain language to normative requirements without preserving obligation strength.
- Combining RFC `MUST` with ISO `shall` without defining precedence.
- Claiming formal compliance from memory or public summaries.
- Treating sentence length or readability scores as proof of clarity.
- Removing legal, safety, scientific, or technical nuance to make text shorter.
- Ignoring the channel: UI text, API documentation, maintenance procedures, policies, and warnings need different profiles.
- Asking the user to choose when the difference is immaterial; the skill should make routine routing decisions itself.
- Failing to ask when the choice materially changes obligations, safety, or compliance scope.
