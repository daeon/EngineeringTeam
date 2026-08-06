# Output Contract

Choose the smallest output that satisfies the task.

## Route only

Use when the user asks which standard to use.

```markdown
## Recommended profile

**Primary:** <standard/profile>
**Supporting:** <zero to two profiles>
**Confidence:** High | Medium | Low

**Why:** <task-specific reason>
**Material trade-off:** <what this profile optimizes and what it constrains>

## Alternative

<Only include when meaningfully different.>

## Confirmation

<Only include when the confirmation gate applies.>
```

## Rewrite

Return the usable revised content first. Then include only the notes needed for trust and review.

```markdown
## Revised content

<finished text>

## Applied profile

- Primary: ...
- Supporting: ...

## Review notes

- Assumptions: ...
- Unresolved ambiguities: ...
- Terminology gaps: ...
- Human review required: yes/no and why
```

Do not clutter simple low-risk rewrites with a long compliance report.

## Audit

```markdown
## Audit summary

- Selected profile: ...
- Evidence basis: authoritative text supplied | organization checklist | public guidance | profile-level review only
- Overall result: ...
- Compliance claim: not assessed | candidate alignment only | checked against supplied authoritative profile

## Findings

| ID | Severity | Classification | Location | Finding | Evidence/rule | Proposed correction | Confidence |
|---|---|---|---|---|---|---|---|

## Unresolved decisions

- ...

## Human review

- ...
```

### Severity

- **Critical** — likely change to safety, legal obligation, security, or essential normative meaning.
- **Major** — likely ambiguity, incorrect action, failed task, inconsistent requirement, or inaccessible path.
- **Moderate** — significant clarity, terminology, structure, or localization issue.
- **Minor** — low-cost consistency or editorial issue.
- **Suggestion** — preference, not a violation.

### Classification

Use exactly one:

- confirmed issue;
- candidate issue;
- content ambiguity;
- domain decision;
- preference.

## Rewrite + audit

Return:

1. revised content;
2. profile selection;
3. compact table of material changes;
4. unresolved ambiguities and human-review needs.

Do not repeat every minor edit. Group similar changes.

## Profile builder

Use when the user supplies standards, organization rules, examples, terminology, or templates and wants a reusable AI profile.

```markdown
# <Profile name>

## Scope

- Intended content:
- Audience:
- Exclusions:
- Governing sources:
- Source precedence:

## Required rules

1. ...

## Terminology

| Concept | Preferred | Allowed | Forbidden/deprecated | Definition/source |

## Normative language

- System:
- Defined keywords:
- Examples:

## Structure

- ...

## Accessibility and localization

- ...

## Safety/legal escalation

- ...

## Output and audit behavior

- ...

## Positive examples

- ...

## Negative examples

- ...

## Validation checklist

- ...
```

## Confirmation wording

When confirmation is required, make the choice easy:

```markdown
I recommend **A: <profile>** because <reason>.

**B: <alternative>** is better when <condition>.

The material difference is <effect on obligations, safety, nuance, or compliance scope>.

Please choose **A** or **B** before I produce the final rewrite/audit.
```

Do not ask broad questions such as “What style do you want?” when the task evidence supports two concrete choices.

## Claims language

Use accurate labels:

| Evidence available | Permitted claim |
|---|---|
| public principles only | “edited using an <X>-informed profile” |
| user-supplied checklist | “checked against the supplied <X> checklist” |
| authoritative excerpt for relevant clauses | “checked against the supplied clauses” |
| full authoritative material plus required validation | “conformance assessment performed” — still state scope and reviewer limits |
| no authoritative evidence | never say compliant, certified, passed, or fully conformant |

## Final quality check

Before returning output, verify:

- meaning, obligations, permissions, prohibitions, conditions, exceptions, and sequence are preserved;
- selected profiles are not redundant or incompatible;
- terminology matches supplied authoritative sources;
- normative keywords follow one defined system;
- warnings retain hazard, consequence, and avoidance action;
- claims do not exceed the available evidence;
- ambiguities are surfaced rather than silently invented away;
- output is usable in the user's requested channel.
