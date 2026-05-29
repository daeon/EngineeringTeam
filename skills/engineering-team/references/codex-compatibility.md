# Codex Compatibility Notes

## Skill loading

Codex discovers skills from `.agents/skills`, `~/.agents/skills`, admin skill paths, system skills, and installed plugins. This package can be used either as a plugin or by copying `skills/engineering-team` into one of those skill locations.

## Invocation

Use `engineering-team` or select it from `/skills` when you want explicit activation.

## AGENTS.md

Codex reads `AGENTS.md` before work. Keep repo-level `AGENTS.md` short and use it for routing and durable repo rules. Keep detailed procedures in skills, references, and scripts.

## Subagents

Codex only spawns subagents when explicitly asked. The skill therefore supports two modes:

1. Single-session mode: simulate specialist roles in the main session.
2. Team mode: when explicitly requested, spawn bounded Codex subagents or custom agents.

Custom agent TOML files live under `.codex/agents/` (and a copy bundled in the skill at `skills/engineering-team/assets/agents/`). All are generated from `agents-src/*.yaml`; do not hand-edit them.

## Context hygiene

Do not load all references at once. Load only the schema, template, script, or custom-agent definition needed for the current task.
