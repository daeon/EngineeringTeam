#!/usr/bin/env python3
"""Generate native agent definitions from agents-src/*.yaml.

The YAML subset used here is intentionally tiny so the plugin stays
dependency-free across harnesses.
"""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AGENT_SOURCE_DIR = REPO_ROOT / "agents-src"


GENERATED_DIRS = [
    Path("agents"),
    Path(".codex") / "agents",
    Path("skills") / "engineering-team" / "assets" / "agents",
    Path("skills") / "engineering-team" / "references" / "codex-custom-agents",
    Path(".github") / "agents",
]

GENERATED_SUFFIXES = ("*.md", "*.toml")


def parse_scalar(value: str) -> str | None:
    value = value.strip()
    if value == "null":
        return None
    if value.startswith('"') and value.endswith('"'):
        inner = value[1:-1]
        return inner.replace('\\"', '"').replace("\\\\", "\\")
    return value


def parse_agent(path: Path) -> dict:
    lines = path.read_text().splitlines()
    agent: dict = {"claude": {}, "codex": {}, "instructions": ""}
    section: str | None = None
    list_key: str | None = None
    instruction_lines: list[str] = []
    in_instructions = False

    for raw in lines:
        if in_instructions:
            if raw.startswith("  "):
                instruction_lines.append(raw[2:])
            elif raw == "":
                instruction_lines.append("")
            else:
                raise ValueError(f"{path}: unexpected content after instructions block: {raw!r}")
            continue

        if raw == "claude:":
            section = "claude"
            list_key = None
            continue
        if raw == "codex:":
            section = "codex"
            list_key = None
            continue
        if raw == "instructions: |":
            in_instructions = True
            section = None
            list_key = None
            continue

        stripped = raw.strip()
        if not stripped:
            continue

        if list_key and stripped.startswith("- "):
            agent[section][list_key].append(parse_scalar(stripped[2:]))
            continue

        if ":" not in raw:
            raise ValueError(f"{path}: unsupported line: {raw!r}")

        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()

        target = agent[section] if section else agent
        if section and value == "":
            target[key] = []
            list_key = key
        elif section and value == "[]":
            target[key] = []
            list_key = None
        else:
            target[key] = parse_scalar(value)
            list_key = None

    agent["instructions"] = "\n".join(instruction_lines).strip() + "\n"
    for key in ["name", "description", "instructions"]:
        if not agent.get(key):
            raise ValueError(f"{path}: missing {key}")
    return agent


def toml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def toml_multiline(value: str) -> str:
    return '"""' + value.replace('"""', '\\"\\"\\"').rstrip() + '\n"""'


def codex_name(agent_name: str) -> str:
    return agent_name.replace("-", "_")


def render_markdown(agent: dict) -> str:
    claude = agent["claude"]
    return "\n".join(
        [
            "---",
            f"name: {agent['name']}",
            f"description: {agent['description']}",
            f"tools: {claude.get('tools', 'Read, Grep, Glob, Bash')}",
            f"model: {claude.get('model', 'sonnet')}",
            f"color: {claude.get('color', 'blue')}",
            "---",
            "",
            agent["instructions"].rstrip(),
            "",
        ]
    )


def title_case_role(name: str) -> str:
    return " ".join(word.capitalize() for word in name.split("-"))


def render_github_markdown(agent: dict) -> str:
    name = agent["name"]
    sandbox = agent["codex"].get("sandbox_mode", "read-only")
    if sandbox == "workspace-write":
        edit_boundary = (
            "- May edit files, but only after the evidence gate is satisfied.\n"
            "- Make the smallest safe change; preserve existing contracts, style, and conventions.\n"
            "- Do not perform broad rewrites or unrelated refactors.\n"
            "- Require human approval for destructive or production-sensitive actions."
        )
    else:
        edit_boundary = (
            "- Read-only. Do not edit files.\n"
            "- Investigate and report; the lead agent merges your findings.\n"
            "- Do not treat guesses as facts or perform side effects."
        )
    return "\n".join(
        [
            "---",
            f"name: {name}",
            f"description: {agent['description']}",
            "---",
            "",
            f"# {title_case_role(name)}",
            "",
            "## When to use",
            "",
            agent["description"],
            "",
            "## How to operate",
            "",
            agent["instructions"].rstrip(),
            "",
            "## Evidence requirements",
            "",
            "- Tie every claim to a file path, symbol, test result, command output, or documented behavior.",
            "- Label unproven claims as assumptions; do not present guesses as facts.",
            "- Prefer existing repo patterns and tests over generic best practices.",
            "",
            "## Safety and edit boundaries",
            "",
            edit_boundary,
            "",
        ]
    )


def render_toml(agent: dict) -> str:
    codex = agent["codex"]
    name = codex_name(agent["name"])
    wrapper = (
        f"You are the Codex custom agent `{name}` for the EngineeringTeam workflow.\n\n"
        "Operate as a specialist. Keep results compact and evidence-backed. "
        "If you are read-only, do not edit files. Return concise artifacts the lead agent can merge into the final plan.\n\n"
    )
    instructions = wrapper + agent["instructions"].rstrip() + "\n"

    lines = [
        f"name = {toml_string(name)}",
        f"description = {toml_string(agent['description'])}",
    ]
    if codex.get("model"):
        lines.append(f"model = {toml_string(codex['model'])}")
    lines.extend(
        [
            f"model_reasoning_effort = {toml_string(codex.get('model_reasoning_effort', 'high'))}",
            f"sandbox_mode = {toml_string(codex.get('sandbox_mode', 'read-only'))}",
            "nickname_candidates = ["
            + ", ".join(toml_string(item) for item in codex.get("nickname_candidates", []))
            + "]",
            f"developer_instructions = {toml_multiline(instructions)}",
            "",
        ]
    )
    return "\n".join(lines)


def output_paths(agent: dict) -> list[tuple[Path, str]]:
    md = render_markdown(agent)
    toml = render_toml(agent)
    github_md = render_github_markdown(agent)
    name = agent["name"]
    underscore = codex_name(name)
    return [
        (REPO_ROOT / "agents" / f"{name}.md", md),
        (REPO_ROOT / ".codex" / "agents" / f"{underscore}.toml", toml),
        (REPO_ROOT / "skills" / "engineering-team" / "assets" / "agents" / f"{underscore}.toml", toml),
        (REPO_ROOT / "skills" / "engineering-team" / "references" / "codex-custom-agents" / f"{underscore}.toml", toml),
        (REPO_ROOT / ".github" / "agents" / f"{name}.md", github_md),
    ]


def generated_dirs() -> list[Path]:
    return [REPO_ROOT / rel for rel in GENERATED_DIRS]


def generated_files() -> set[Path]:
    files: set[Path] = set()
    for rel_dir in GENERATED_DIRS:
        directory = REPO_ROOT / rel_dir
        if not directory.exists():
            continue
        for suffix in GENERATED_SUFFIXES:
            for path in directory.glob(suffix):
                files.add(path.relative_to(REPO_ROOT))
    return files


def expected_outputs(agents: list[dict]) -> dict[Path, str]:
    expected: dict[Path, str] = {}
    for agent in agents:
        for path, content in output_paths(agent):
            expected[path.relative_to(REPO_ROOT)] = content
    return expected


def generate() -> None:
    agents = [parse_agent(path) for path in sorted(AGENT_SOURCE_DIR.glob("*.yaml"))]
    if not agents:
        raise SystemExit("No agent source files found")

    for directory in generated_dirs():
        directory.mkdir(parents=True, exist_ok=True)
        for suffix in GENERATED_SUFFIXES:
            for existing in directory.glob(suffix):
                existing.unlink()

    for agent in agents:
        for path, content in output_paths(agent):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)


def check() -> int:
    agents = [parse_agent(path) for path in sorted(AGENT_SOURCE_DIR.glob("*.yaml"))]
    if not agents:
        raise SystemExit("No agent source files found")

    expected = expected_outputs(agents)
    expected_paths = set(expected)
    actual_paths = generated_files()
    mismatches: list[str] = []

    for missing in sorted(expected_paths - actual_paths):
        mismatches.append(f"missing generated file: {missing}")

    for extra in sorted(actual_paths - expected_paths):
        mismatches.append(f"extra stale generated file: {extra}")

    for rel, generated_text in sorted(expected.items()):
        actual = REPO_ROOT / rel
        if not actual.exists():
            continue
        actual_text = actual.read_text()
        if actual_text != generated_text:
            diff = "\n".join(
                difflib.unified_diff(
                    actual_text.splitlines(),
                    generated_text.splitlines(),
                    fromfile=str(rel),
                    tofile=f"{rel} (generated)",
                    lineterm="",
                )
            )
            mismatches.append(diff)

    if mismatches:
        print("Generated agent files are out of date:")
        print("\n\n".join(mismatches))
        return 1

    print("Generated agent files are up to date.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()

    if args.check:
        return check()
    generate()
    print("Generated native agent definitions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
