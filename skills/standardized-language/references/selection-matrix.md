# Selection Matrix

Use this matrix to classify the task before choosing a language profile.

## 1. Purpose

| Purpose | Routing implication |
|---|---|
| explain or educate | prioritize audience understanding and concept sequencing |
| instruct or troubleshoot | prioritize task completion, action order, prerequisites, feedback, and recovery |
| specify requirements | preserve normative force, atomicity, verifiability, conditions, and actors |
| warn or protect | preserve hazard, consequence, avoidance, urgency, and severity |
| establish rights or duties | preserve legal effect, jurisdiction, exceptions, definitions, and remedies |
| communicate science | preserve uncertainty, evidence strength, methods, limitations, and causal boundaries |
| localize or translate | control terminology, ambiguity, sentence structure, and post-editing workflow |
| label an interface | prioritize brevity, consistency, accessibility, and exact UI behavior |

## 2. Audience

Classify the least-expert intended reader who must act correctly.

- general public
- customer or end user
- software developer
- operator or technician
- engineer or architect
- regulator or auditor
- lawyer or contracting party
- scientist or specialist
- translator or multilingual reader
- cognitively diverse or accessibility-sensitive audience

Record:

- domain knowledge;
- language proficiency;
- reading conditions;
- urgency and stress;
- device or channel;
- cost of misunderstanding.

## 3. Document type

| Document type | Strong candidates |
|---|---|
| public notice, form, policy explanation | ISO 24495-1; CAN-ASC-3.1 in Canada; WCAG/COGA for digital content |
| maintenance or operating procedure | IEC/IEEE 82079-1 + ASD-STE100; add safety framework when hazards exist |
| software help, tutorial, CLI or API guide | ISO/IEC/IEEE 26514 + Google or Microsoft style; WCAG for web delivery |
| PRD, SRS, acceptance criteria, protocol | ISO/IEC/IEEE 29148 + one normative keyword system |
| standard or formal specification | ISO Directives Part 2 or the governing standards body's drafting rules |
| RFC or interoperability protocol | RFC 2119 + RFC 8174 |
| contract, privacy notice, terms, legal explanation | ISO 24495-2 + jurisdiction-specific legal review |
| scientific summary or research communication | ISO 24495-3 + field-specific reporting guidance |
| warning, caution, safety manual | ANSI Z535.6/Z535.7 or applicable product/jurisdiction framework |
| terminology list or ontology | ISO 704; use TBX/ISO 30042 when machine exchange matters |
| translated or machine-translated text | ISO 18587 + terminology profile + source-language profile |
| UI strings and error messages | Microsoft style or product-specific UI guide + WCAG/COGA |

## 4. Normative force

Determine whether the text:

- describes facts;
- recommends behavior;
- permits behavior;
- imposes a requirement;
- prohibits behavior;
- declares capability or possibility;
- defines a term;
- gives a non-normative example.

If normative force exists, select and enforce one keyword system.

### RFC system

Use for Internet, API, interoperability, and software protocol specifications when the document defines RFC 2119/8174 usage.

- MUST / MUST NOT
- SHOULD / SHOULD NOT
- MAY

### ISO-style system

Use for standards-like documents and formal specifications following ISO drafting conventions.

- shall: requirement
- should: recommendation
- may: permission
- can: possibility or capability

Do not infer that ordinary lowercase uses are normative unless the document defines them that way.

## 5. Consequence

| Consequence | Routing behavior |
|---|---|
| low: cosmetic or preference | choose automatically |
| moderate: user confusion, support cost, failed task | choose automatically; report assumptions |
| high: outage, data loss, financial impact, security exposure | preserve technical precision; include audit report and human review recommendation |
| critical: injury, legal rights, regulated compliance, emergency response | trigger confirmation gate and qualified human review |

## 6. Domain

Check for domain overlays:

- aerospace, defence, maintenance: ASD-STE100 may be appropriate;
- software user information: ISO/IEC/IEEE 26514;
- product instructions: IEC/IEEE 82079-1;
- requirements engineering: ISO/IEC/IEEE 29148;
- public administration in Canada: CAN-ASC-3.1 and Canada.ca guidance;
- web accessibility: WCAG 2.2 and COGA guidance;
- legal communication: ISO 24495-2;
- scientific communication: ISO 24495-3;
- safety communication: applicable ANSI, ISO, IEC, regulatory, or organizational safety framework.

## 7. Channel

Account for:

- printed manual;
- PDF;
- responsive web page;
- mobile UI;
- terminal or CLI;
- API reference;
- chatbot response;
- email or notification;
- spoken script;
- translation source text.

Channel affects length, navigation, visibility of warnings, step structure, link wording, and accessibility.

## 8. Localization

Ask internally:

- Is English a source language for translation?
- Are readers non-native speakers?
- Is machine translation expected?
- Is a termbase available?
- Are locale, units, date formats, and regulatory terms controlled?

If yes, add terminology control and reduce avoidable ambiguity. Do not erase culturally or legally necessary distinctions.

## 9. Evidence available

Classify the governing material:

- authoritative standard text supplied;
- licensed excerpt supplied;
- organization checklist supplied;
- approved glossary supplied;
- public official guidance available;
- only public summaries or model knowledge available.

The weaker the evidence, the weaker the compliance claim must be.

## Candidate scoring

Rank each candidate profile against these factors:

| Factor | Weight |
|---|---:|
| direct match to document purpose | 3 |
| direct match to domain/document type | 3 |
| protects high-consequence meaning | 3 |
| matches audience and channel | 2 |
| supports terminology/localization need | 2 |
| authoritative material is available | 2 |
| introduces unnecessary restriction | -2 |
| overlaps another selected profile | -1 |
| conflicts with governing framework | eliminate |

Use the score to structure judgment, not to manufacture mathematical certainty.

## Tie-breaking

When candidates are close:

1. prefer the profile required by contract, regulator, organization, or publication venue;
2. otherwise prefer the profile closest to the document type;
3. otherwise prefer the profile that protects the highest-cost failure;
4. otherwise use a general plain-language profile as primary and a focused style guide as support;
5. ask for confirmation only when the remaining difference is material.
