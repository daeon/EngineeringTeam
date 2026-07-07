#!/usr/bin/env python3
"""Summarize the changed surface of the working tree.

Portable replacement for the former changed_surface.sh.
Usage: python3 changed_surface.py [root]
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PUBLIC_SURFACE_PATTERN = re.compile(
    r"^(\+|-)\s*(export |public |interface |type |class |func |def |function |const )"
)


def git(root: Path, *args: str) -> str:
    try:
        result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
        return result.stdout
    except OSError:
        return ""


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print("# Changed Surface\n")
    print("## Changed files")
    print(git(root, "diff", "--name-only"), end="")
    print("\n## Staged files")
    print(git(root, "diff", "--cached", "--name-only"), end="")
    print("\n## Public-surface-looking changes")
    for line in git(root, "diff", "--unified=0").splitlines():
        if PUBLIC_SURFACE_PATTERN.match(line):
            print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
