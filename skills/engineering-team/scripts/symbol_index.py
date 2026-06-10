#!/usr/bin/env python3
"""Build a lightweight symbol index of likely definition sites.

Portable replacement for the former symbol_index.sh: uses ripgrep when
available, otherwise falls back to a pure-Python scan so it still works on
hosts without rg (including native Windows).
Usage: python3 symbol_index.py [root]
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

DEFINITION_PATTERN = (
    r"^(export |func |type |class |interface |def |const |let |var "
    r"|public |private |protected |static |async function|function )"
)
SKIP_DIRS = {"node_modules", "vendor", "dist", "build", ".git", "__pycache__"}
SOURCE_SUFFIXES = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java", ".kt",
    ".cs", ".rb", ".php", ".swift", ".scala", ".c", ".cc", ".cpp", ".h", ".hpp",
}
MAX_LINES = 2000


def scan_with_rg(root: Path) -> int:
    result = subprocess.run(
        ["rg", "-n", *(f"--glob=!{d}" for d in sorted(SKIP_DIRS - {".git"})), DEFINITION_PATTERN, "."],
        cwd=root,
        capture_output=True,
        text=True,
    )
    print(result.stdout, end="")
    return 0


def scan_pure_python(root: Path) -> int:
    pattern = re.compile(DEFINITION_PATTERN)
    emitted = 0
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if SKIP_DIRS.intersection(rel.parts) or path.suffix not in SOURCE_SUFFIXES or not path.is_file():
            continue
        try:
            lines = path.read_text(errors="replace").splitlines()
        except OSError:
            continue
        for line_no, line in enumerate(lines, 1):
            if pattern.match(line):
                print(f"{rel.as_posix()}:{line_no}:{line}")
                emitted += 1
                if emitted >= MAX_LINES:
                    print(f"... truncated at {MAX_LINES} definitions")
                    return 0
    return 0


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print("# Lightweight Symbol Index\n")
    print("## Likely definitions")
    if shutil.which("rg"):
        return scan_with_rg(root)
    return scan_pure_python(root)


if __name__ == "__main__":
    sys.exit(main())
