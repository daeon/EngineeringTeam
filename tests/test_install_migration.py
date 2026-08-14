"""Migration tests for obsolete generated Lead agent cleanup."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import hashlib
import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HAND_EDITED_OLD_GENERATED = (
    "# GENERATED FILE - DO NOT EDIT. "
    "Source: agents-src/lead-engineer.yaml.\n# local customization\n"
)


def load_root_installer():
    path = REPO_ROOT / "scripts" / "install.py"
    spec = importlib.util.spec_from_file_location("engineering_team_install", path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InstallMigrationTest(unittest.TestCase):
    def run_install(self, target: str, repo: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "install.py"),
                "--target",
                target,
                "--scope",
                "project",
                "--repo",
                str(repo),
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_exact_hash_cleanup_removes_only_exact_file(self):
        installer = load_root_installer()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "lead-engineer.md"
            content = b"known historical generated file\n"
            target.write_bytes(content)
            expected = hashlib.sha256(content).hexdigest()

            installer.remove_obsolete_generated_lead(target, expected)
            self.assertFalse(target.exists())

    def test_github_install_preserves_custom_lead(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / ".github" / "agents" / "lead-engineer.md"
            target.parent.mkdir(parents=True)
            target.write_text("# My custom lead\n")

            result = self.run_install("github", repo)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(target.read_text(), "# My custom lead\n")
            self.assertIn("Review it manually", result.stdout)

    def test_codex_install_preserves_hand_edited_generated_lead(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / ".codex" / "agents" / "lead_engineer.toml"
            target.parent.mkdir(parents=True)
            target.write_text(HAND_EDITED_OLD_GENERATED)

            result = self.run_install("codex", repo)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(target.read_text(), HAND_EDITED_OLD_GENERATED)
            self.assertIn("Review it manually", result.stdout)

    def test_github_install_preserves_hand_edited_generated_lead(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / ".github" / "agents" / "lead-engineer.md"
            target.parent.mkdir(parents=True)
            target.write_text(HAND_EDITED_OLD_GENERATED)

            result = self.run_install("github", repo)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(target.read_text(), HAND_EDITED_OLD_GENERATED)
            self.assertIn("Review it manually", result.stdout)


if __name__ == "__main__":
    unittest.main()
