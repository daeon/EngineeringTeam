#!/usr/bin/env python3
"""Environment and package health check for EngineeringTeam.

Prints one line per check using OK / WARN / FAIL and exits non-zero if any
check fails. Dependency-free so it runs anywhere Python 3 is available.

Usage:
  python3 scripts/doctor.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

RESULTS: list[tuple[str, str]] = []


def ok(message: str) -> None:
    RESULTS.append(("OK", message))


def warn(message: str) -> None:
    RESULTS.append(("WARN", message))


def fail(message: str) -> None:
    RESULTS.append(("FAIL", message))


def check_python() -> None:
    v = sys.version_info
    if v >= (3, 11):
        ok(f"Python {v.major}.{v.minor}.{v.micro} (>= 3.11)")
    else:
        fail(
            f"Python {v.major}.{v.minor} found; 3.11+ required "
            "(Codex validation uses the stdlib tomllib module)"
        )


def check_node() -> bool:
    if not shutil.which("node"):
        warn("Node not found; OpenCode JS syntax validation will be skipped")
        return False
    try:
        proc = subprocess.run(
            ["node", "--version"], capture_output=True, text=True, timeout=15
        )
        ok(f"Node {proc.stdout.strip()} available (OpenCode JS validation enabled)")
        return True
    except Exception as exc:  # noqa: BLE001 - report and continue
        warn(f"Node present but version check failed: {exc}")
        return False


def check_repo_root() -> bool:
    plugin = REPO_ROOT / ".claude-plugin" / "plugin.json"
    skill = REPO_ROOT / "skills" / "engineering-team" / "SKILL.md"
    if plugin.exists() and skill.exists():
        ok(f"Repo root detected: {REPO_ROOT}")
        return True
    fail(f"Repo root not detected at {REPO_ROOT}")
    return False


def check_manifests() -> None:
    required = [
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        ".codex-plugin/plugin.json",
        ".cursor-plugin/plugin.json",
        "gemini-extension.json",
        "package.json",
        ".version-bump.json",
        ".opencode/plugins/engineering-team.js",
        "skills/engineering-team/SKILL.md",
        "AGENTS.md",
    ]
    missing = [rel for rel in required if not (REPO_ROOT / rel).exists()]
    if missing:
        for rel in missing:
            fail(f"Missing required file: {rel}")
    else:
        ok(f"All {len(required)} required manifests/files present")


def check_harness_dirs() -> None:
    optional = {
        "agents": "Claude / Cursor markdown agents",
        ".codex/agents": "Codex TOML agents",
        ".github/agents": "GitHub Copilot custom agents",
        ".opencode/plugins": "OpenCode plugin",
    }
    for rel, label in optional.items():
        if (REPO_ROOT / rel).exists():
            ok(f"Harness output present: {rel} ({label})")
        else:
            warn(f"Harness output missing: {rel} ({label})")


def run_script(label: str, args: list[str]) -> None:
    try:
        proc = subprocess.run(
            args, cwd=REPO_ROOT, capture_output=True, text=True, timeout=180
        )
    except FileNotFoundError as exc:
        fail(f"{label}: command not found ({exc})")
        return
    if proc.returncode == 0:
        ok(f"{label} passed")
        return
    detail = (proc.stdout + proc.stderr).strip().splitlines()
    first = detail[0] if detail else "no output"
    fail(f"{label} failed: {first}")


def main() -> int:
    check_python()
    has_node = check_node()
    check_repo_root()
    check_manifests()
    check_harness_dirs()

    run_script(
        "Generated-agent drift check",
        [sys.executable, "scripts/generate-agents.py", "--check"],
    )
    run_script(
        "Package structure validation",
        [sys.executable, "skills/engineering-team/scripts/validate-package.py"],
    )
    run_script(
        "Codex package validation",
        [sys.executable, "scripts/validate-codex-package.py"],
    )
    if has_node:
        run_script(
            "OpenCode JS syntax check",
            ["node", "--check", ".opencode/plugins/engineering-team.js"],
        )

    width = max(len(status) for status, _ in RESULTS)
    for status, message in RESULTS:
        print(f"{status.ljust(width)}  {message}")

    failed = sum(1 for status, _ in RESULTS if status == "FAIL")
    warned = sum(1 for status, _ in RESULTS if status == "WARN")
    print()
    print(f"Summary: {failed} failed, {warned} warnings, {len(RESULTS)} checks total")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
