#!/usr/bin/env python3
"""Print a quick repo snapshot: key files, directory shape, git status.

Portable replacement for the former repo_snapshot.sh; runs anywhere Python 3 runs.
Usage: python3 repo_snapshot.py [root]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

KEY_FILE_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "package.json",
    "pnpm-lock.yaml",
    "go.mod",
    "Cargo.toml",
    "pyproject.toml",
    "Makefile",
    ".gitignore",
    "pom.xml",
}
KEY_FILE_PREFIXES = ("README", "CONTRIBUTING", "build.gradle")
KEY_FILE_SUFFIXES = (".sln",)


def is_key_file(name: str) -> bool:
    return (
        name in KEY_FILE_NAMES
        or name.startswith(KEY_FILE_PREFIXES)
        or name.endswith(KEY_FILE_SUFFIXES)
    )


def walk_limited(root: Path, max_depth: int):
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if len(rel.parts) > max_depth or ".git" in rel.parts:
            continue
        yield rel, path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print("# Repo Snapshot\n")
    print("## Root")
    print(root)

    print("\n## Top-level files")
    for rel, path in walk_limited(root, 2):
        if path.is_file() and is_key_file(rel.name):
            print(rel.as_posix())

    print("\n## Directories")
    dirs = [rel.as_posix() for rel, path in walk_limited(root, 2) if path.is_dir()]
    for line in dirs[:200]:
        print(line)

    print("\n## Git status")
    try:
        result = subprocess.run(
            ["git", "status", "--short"], cwd=root, capture_output=True, text=True
        )
        print(result.stdout, end="")
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
