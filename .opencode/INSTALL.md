# Installing EngineeringTeam for OpenCode

## Prerequisites

- OpenCode installed

## Installation

Add this repository to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["/path/to/EngineeringTeam"]
}
```

Restart OpenCode. The plugin registers the repository's `skills/` directory so OpenCode can discover `engineering-team`.

## Usage

Use OpenCode's native skill workflow to list and load skills, then invoke `engineering-team` for non-trivial software engineering tasks.

## Troubleshooting

1. Confirm the plugin path points to this repository root.
2. Check OpenCode logs for plugin loading errors.
3. Confirm `skills/engineering-team/SKILL.md` exists.
4. Run `node --check .opencode/plugins/engineering-team.js` from this repository.
