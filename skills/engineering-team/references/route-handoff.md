# Handoff Route

Use when transferring an engineering task, investigation, plan, branch, or session to another agent or a fresh session.

## Authority

Preserve and compress existing context. Do not broaden the investigation or edit implementation files. You may write only the requested continuation artifact.

## Workflow

1. Identify the target audience, destination, and next focus.
2. Use the user-provided path. Otherwise use `.agent-state/handoffs/<task>.md` for an explicitly repo-local artifact or the OS temporary directory for a session-only handoff.
3. Read an existing target before replacing it. If writes are unavailable, return the handoff inline and mark it unsaved.
4. Collect only continuation-critical context: intent, repository/branch/PR/issue, decisions, relevant files and symbols, verified commands, evidence, open questions, risks, blockers, rollback, and exact next action.
5. Reference existing artifacts by path, URL, commit, or command rather than copying long transcripts or logs.
6. Redact secrets, credentials, private data, and environment-specific sensitive values.

## Output

Use `templates/handoff.md`. Include current state, decisions, evidence and confidence, relevant artifacts, affected contracts, verification status, open questions, risks, suggested EngineeringTeam mode or specialists, next actions, and work not to repeat. Finish with the artifact location and one ready-to-paste continuation prompt.
