#!/usr/bin/env python3
"""Generate native agent definitions from agents-src/*.yaml.

The YAML subset used here is intentionally tiny so the plugin stays
dependency-free across harnesses.
"""

from __future__ import annotations

import argparse
import difflib
import shutil
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AGENT_SOURCE_DIR = REPO_ROOT / "agents-src"


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
    name = agent["name"]
    underscore = codex_name(name)
    return [
        (REPO_ROOT / "agents" / f"{name}.md", md),
        (REPO_ROOT / ".codex" / "agents" / f"{underscore}.toml", toml),
        (REPO_ROOT / "skills" / "engineering-team" / "assets" / "agents" / f"{underscore}.toml", toml),
        (REPO_ROOT / "skills" / "engineering-team" / "references" / "codex-custom-agents" / f"{underscore}.toml", toml),
    ]


def generated_dirs() -> list[Path]:
    return [
        REPO_ROOT / "agents",
        REPO_ROOT / ".codex" / "agents",
        REPO_ROOT / "skills" / "engineering-team" / "assets" / "agents",
        REPO_ROOT / "skills" / "engineering-team" / "references" / "codex-custom-agents",
    ]


def generate() -> None:
    agents = [parse_agent(path) for path in sorted(AGENT_SOURCE_DIR.glob("*.yaml"))]
    if not agents:
        raise SystemExit("No agent source files found")

    for directory in generated_dirs():
        directory.mkdir(parents=True, exist_ok=True)
        for suffix in ("*.md", "*.toml"):
            for existing in directory.glob(suffix):
                existing.unlink()

    for agent in agents:
        for path, content in output_paths(agent):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)


def check() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp) / "engineering-team"

        for rel_dir in [
            Path("agents"),
            Path(".codex") / "agents",
            Path("skills") / "engineering-team" / "assets" / "agents",
            Path("skills") / "engineering-team" / "references" / "codex-custom-agents",
        ]:
            src = REPO_ROOT / rel_dir
            dst = tmp_root / rel_dir
            if src.exists():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

        agents = [parse_agent(path) for path in sorted(AGENT_SOURCE_DIR.glob("*.yaml"))]
        if not agents:
            raise SystemExit("No agent source files found")

        for agent in agents:
            for path, content in output_paths(agent):
                rel = path.relative_to(REPO_ROOT)
                dst = tmp_root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(content)

        mismatches: list[str] = []
        for generated in sorted(tmp_root.rglob("*")):
            if not generated.is_file():
                continue
            rel = generated.relative_to(tmp_root)
            actual = REPO_ROOT / rel
            if not actual.exists():
                mismatches.append(f"missing generated file: {rel}")
                continue
            actual_text = actual.read_text()
            generated_text = generated.read_text()
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
