#!/usr/bin/env python3
"""List durable context files and recently changed sources to spot stale docs.

Portable replacement for the former stale_context_check.sh.
Usage: python3 stale_context_check.py [root]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SKIP_DIRS = {"node_modules", "vendor", ".git", "__pycache__"}
CONTEXT_NAMES = {"AGENTS.md", "CLAUDE.md", "README.md"}
CONTEXT_KEYWORDS = ("architecture", "design")
MAX_RESULTS = 300


def is_context_file(rel: Path) -> bool:
    name = rel.name
    if name in CONTEXT_NAMES or any(keyword in name.lower() for keyword in CONTEXT_KEYWORDS):
        return True
    return name == "SKILL.md" and "skills" in rel.parts


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print("# Stale Context Check\n")
    print("## Candidate durable context files")
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if len(rel.parts) > 4 or SKIP_DIRS.intersection(rel.parts) or not path.is_file():
            continue
        if is_context_file(rel):
            print(rel.as_posix())

    print("\n## Recently changed source files")
    try:
        result = subprocess.run(
            ["git", "log", "--name-only", "--pretty=format:", "--since=90 days ago"],
            cwd=root,
            capture_output=True,
            text=True,
        )
        changed = sorted({line for line in result.stdout.splitlines() if line.strip()})
        print("\n".join(changed[:MAX_RESULTS]))
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
