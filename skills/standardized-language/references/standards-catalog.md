# Standards Catalog

Use this catalog as a routing aid, not as a substitute for authoritative standard text. Verify editions and organization-specific requirements when formal compliance matters.

## General plain language

### ISO 24495-1 — Plain language: governing principles and guidelines

Use as the default audience-centered profile for written information. Optimize so intended readers can find, understand, and use what they need.

Good fit:

- public and customer communication;
- policies and process explanations;
- mixed-expertise technical explanations;
- general document restructuring.

Weak fit by itself:

- controlled maintenance language;
- formal requirements syntax;
- safety-message classification;
- jurisdiction-specific legal drafting.

### CAN-ASC-3.1 — Plain language

Prefer for Canadian public-facing and accessibility-sensitive communication, especially when organizational or governmental alignment in Canada matters.

Combine with:

- Canada.ca Content Style Guide for federal web/content conventions;
- WCAG and COGA for digital accessibility;
- a domain standard when the content is technical, legal, or safety-critical.

## Domain plain language

### ISO 24495-2 — Legal communication

Use for making legal information easier to find, understand, and use while preserving legal effect.

Use confirmation and legal-review gates for:

- contracts;
- terms and conditions;
- privacy notices;
- rights, duties, consent, remedies, and liability.

Do not treat plain-language editing as legal validation.

### ISO 24495-3 — Science writing

Use for communication of scientific information to specialist or non-specialist audiences.

Preserve:

- evidence strength;
- uncertainty;
- correlation-versus-causation distinctions;
- methodological limitations;
- scope and generalizability.

## Controlled technical language

### ASD-STE100 — Simplified Technical English

Use when controlled vocabulary and constrained grammar are valuable, especially for maintenance, aerospace, defence, manufacturing, multilingual operations, and translation-ready procedures.

Good fit:

- maintenance instructions;
- operational procedures;
- repeated technical actions;
- documentation used by readers with varied English proficiency.

Potential cost:

- prose can become mechanical;
- strict vocabulary can remove nuance;
- domain terminology still needs controlled approval.

Do not claim STE conformance without the applicable issue, approved dictionary decisions, and a proper checking process.

## Product and software information

### IEC/IEEE 82079-1 — Preparation of information for use

Use for product instructions and information throughout the information-development lifecycle.

Focus on:

- target groups;
- task and product analysis;
- structure and media;
- warnings and instructions;
- evaluation of information quality.

Use as a document-system profile rather than a sentence-style guide.

### ISO/IEC/IEEE 26514 — Design and development of information for users

Use for software user information such as:

- tutorials;
- how-to guides;
- concepts;
- references;
- troubleshooting;
- release and migration guidance.

Combine with a concrete editorial guide such as Google or Microsoft for word-level conventions.

## Requirements and specifications

### ISO/IEC/IEEE 29148 — Requirements engineering

Use for stakeholder, system, and software requirements.

Check that requirements are:

- necessary;
- unambiguous;
- singular or appropriately decomposed;
- feasible;
- verifiable;
- traceable;
- consistent;
- bounded by explicit conditions and actors.

Do not invent acceptance thresholds merely to make a requirement measurable. Flag missing thresholds.

### RFC 2119 and RFC 8174

Use for Internet, API, and interoperability specifications that define uppercase normative keywords.

Control:

- MUST / MUST NOT;
- SHOULD / SHOULD NOT;
- MAY.

Preserve the distinction between absolute obligation, recommended behavior with valid exceptions, and permission.

### ISO/IEC Directives, Part 2

Use for ISO-like drafting and standards-style normative language.

Control:

- shall: requirement;
- should: recommendation;
- may: permission;
- can: possibility or capability.

Do not mix this system casually with RFC uppercase keywords.

## Terminology

### ISO 704 — Terminology work: principles and methods

Use to build and govern concepts, definitions, preferred terms, admitted terms, deprecated terms, and concept relations.

Best use with AI:

- provide an authoritative glossary;
- require one term per concept where practical;
- distinguish a concept from the label used for it;
- flag synonym drift and circular definitions.

### ISO 30042 — TermBase eXchange (TBX)

Use when terminology must move between authoring, translation, localization, and language-technology systems.

This is primarily an interchange format, not a writing style.

## Translation and post-editing

### ISO 18587 — Post-editing of machine translation output

Use to define human post-editing processes and competence expectations for machine-translated content.

With generative AI, adapt it cautiously:

- preserve source meaning;
- use approved terminology;
- detect omissions and additions;
- validate numbers, units, names, and normative force;
- require human review appropriate to consequence.

Do not imply that general AI rewriting is identical to a certified translation workflow.

## Accessibility

### WCAG 2.2

Use for web and digital content accessibility. Language-related concerns include readable language, meaningful labels and headings, consistent interactions, understandable errors, and assistance for task completion.

WCAG is broader than writing style. Coordinate content changes with design, semantics, interaction, and implementation.

### W3C COGA Content Usable

Use as supporting guidance for cognitive and learning accessibility.

Useful principles include:

- clear purpose;
- familiar words and patterns;
- manageable steps;
- visible help and recovery;
- reduced memory burden;
- avoidance of unnecessary distraction.

Treat it as guidance unless a governing policy gives it normative force.

## Safety communication

### ANSI Z535.6 and Z535.7

Use when the applicable product, organization, or jurisdiction follows ANSI safety-message conventions in manuals or electronic media.

Preserve:

- signal word or severity classification;
- hazard;
- consequence;
- avoidance action;
- placement and visibility.

Never choose or downgrade hazard severity from prose alone. Escalate to the responsible safety professional.

Other industries and jurisdictions may require different ISO, IEC, regulatory, or company-specific systems. The applicable governing framework overrides this catalog.

## Public editorial guides

### Google Developer Documentation Style Guide

Use for developer-facing documentation, APIs, code examples, command lines, and technical terminology. It is practical and publicly accessible but is not an ISO compliance standard.

### Microsoft Writing Style Guide

Use for software UI, procedures, help, errors, and general technology communication. Particularly useful for consistent interaction language and user-facing terminology.

### GOV.UK content guidance

Use for strongly task-oriented public web content and content design. Focus on user needs, scanning, and completion of public-service tasks.

### Canada.ca Content Style Guide

Use for Canadian federal public content conventions, plain language, inclusive wording, spelling, dates, links, and web presentation.

## Selection patterns

| Task | Recommended profile stack |
|---|---|
| general public explanation | ISO 24495-1; add jurisdictional style guide |
| Canadian public web page | CAN-ASC-3.1 + Canada.ca + WCAG/COGA |
| API tutorial | ISO/IEC/IEEE 26514 + Google developer style + WCAG if web-based |
| UI error message | Microsoft style + WCAG/COGA + product terminology |
| software requirements | ISO/IEC/IEEE 29148 + RFC 2119/8174 or ISO Directives Part 2 |
| maintenance procedure | IEC/IEEE 82079-1 + ASD-STE100 + applicable safety system |
| terminology cleanup | ISO 704 + approved glossary; TBX when exchanging data |
| privacy notice | ISO 24495-2 + jurisdiction-specific legal review + accessibility profile |
| research summary | ISO 24495-3 + field reporting requirements |
| translation source content | ISO 24495-1 or ASD-STE100 + ISO 704 terminology + ISO 18587 review process |

## Conflict precedence

When selected profiles conflict, use this order:

1. law, regulation, contract, and governing publication rules;
2. safety and preservation of factual or normative meaning;
3. authoritative organization terminology and product contracts;
4. domain/document standard;
5. accessibility requirements;
6. general plain-language principles;
7. editorial preferences.

Report the conflict rather than silently blending incompatible rules.
