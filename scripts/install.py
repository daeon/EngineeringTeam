#!/usr/bin/env python3
"""Install EngineeringTeam into a target coding-agent harness.

Idempotent: existing files are skipped unless --force is passed.

Usage:
  python3 scripts/install.py --target codex --scope project --repo .
  python3 scripts/install.py --target codex --scope user
  python3 scripts/install.py --target github --scope project --repo .
  python3 scripts/install.py --target claude --scope project --repo .
  python3 scripts/install.py --target cursor --scope project --repo .
  python3 scripts/install.py --target opencode --scope project --repo .
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

POST_INSTALL_PROMPT = (
    "Use engineering-team to review this repo. Map the repo first, identify the "
    "highest-risk contracts, and produce a concise evidence-backed improvement "
    "plan before editing."
)


def copy_files(sources: list[Path], target_dir: Path, force: bool) -> int:
    target_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    skipped: list[str] = []
    for src in sources:
        dst = target_dir / src.name
        if dst.exists() and not force:
            skipped.append(dst.name)
            continue
        shutil.copy2(src, dst)
        copied.append(dst.name)

    print(f"Target directory: {target_dir}")
    if copied:
        print("Copied:")
        for name in copied:
            print(f"  - {name}")
    if skipped:
        print("Skipped existing files; pass --force to overwrite:")
        for name in skipped:
            print(f"  - {name}")
    if not copied and not skipped:
        print("No source files found to install.")
        return 1
    return 0


def install_codex(scope: str, repo: str, force: bool) -> int:
    script = REPO_ROOT / "skills" / "engineering-team" / "scripts" / "install-custom-agents.py"
    if not script.exists():
        print(f"Missing installer: {script}", file=sys.stderr)
        return 1
    args = [sys.executable, str(script), "--scope", scope]
    if scope == "project":
        args += ["--repo", repo]
    if force:
        args.append("--force")
    return subprocess.run(args, cwd=REPO_ROOT).returncode


def install_github(scope: str, repo: str, force: bool) -> int:
    if scope != "project":
        print(
            "GitHub custom agents are repository-scoped. "
            "Re-run with --scope project --repo <path>."
        )
        return 1
    sources = sorted((REPO_ROOT / ".github" / "agents").glob("*.md"))
    target_dir = Path(repo).resolve() / ".github" / "agents"
    return copy_files(sources, target_dir, force)


def install_claude(scope: str, repo: str, force: bool) -> int:
    print("Claude Code installs from a local marketplace, not by copying files.")
    print("From this repository root, run inside Claude Code:")
    print()
    print("  /plugin marketplace add .")
    print("  /plugin install engineering-team@engineering-team-dev")
    return 0


def install_cursor(scope: str, repo: str, force: bool) -> int:
    print("Cursor installs from a local plugin source that points at this repository.")
    print("Add this repository as a local plugin source, then enable the")
    print("`engineering-team` plugin. Cursor reads:")
    print()
    print("  .cursor-plugin/plugin.json")
    print("  skills/engineering-team/")
    print("  agents/*.md")
    return 0


def install_opencode(scope: str, repo: str, force: bool) -> int:
    plugin = REPO_ROOT / ".opencode" / "plugins" / "engineering-team.js"
    print("OpenCode loads a plugin file directly. Plugin path:")
    print()
    print(f"  {plugin}")
    print()
    print(f"See {REPO_ROOT / '.opencode' / 'INSTALL.md'} for setup details.")
    return 0


INSTALLERS = {
    "codex": install_codex,
    "github": install_github,
    "claude": install_claude,
    "cursor": install_cursor,
    "opencode": install_opencode,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Install EngineeringTeam for a harness.")
    parser.add_argument("--target", required=True, choices=sorted(INSTALLERS))
    parser.add_argument("--scope", choices=["project", "user"], default="project")
    parser.add_argument("--repo", default=".", help="Target repo root for project scope")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    result = INSTALLERS[args.target](args.scope, args.repo, args.force)

    if result == 0:
        print()
        print("Next, run this prompt in your coding agent:")
        print()
        print(f"  {POST_INSTALL_PROMPT}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
