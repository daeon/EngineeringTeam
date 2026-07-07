# Codex Compatibility Notes

## Skill loading

Codex discovers skills from `.agents/skills`, `~/.agents/skills`, admin skill paths, system skills, and installed plugins. This package can be used either as a plugin or by copying `skills/engineering-team` into one of those skill locations.

## Invocation

Use `engineering-team` or select it from `/skills` when you want explicit activation.

## AGENTS.md

Codex reads `AGENTS.md` before work. Keep repo-level `AGENTS.md` short and use it for routing and durable repo rules. Keep detailed procedures in skills, references, and scripts.

## Subagents

When Codex exposes subagent tools and the EngineeringTeam skill is active, EngineeringTeam must route through subagents for every L2+ task. The lead stays in the main session, then spawns the selected Codex custom agents from `references/agent-routing.md` using bounded briefs and compact context capsules.

Fallback is limited to harnesses without subagent support, missing custom-agent definitions, or tool failures that prevent spawning. In fallback, label the simulated specialist roles in the main session and report why spawning was unavailable.

Custom agent TOML files live under `.codex/agents/` (and a copy bundled in the skill at `skills/engineering-team/assets/agents/`). All are generated from `agents-src/*.yaml`; do not hand-edit them.

## Context hygiene

Do not load all references at once. Load only the schema, template, script, or custom-agent definition needed for the current task.
