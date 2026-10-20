#!/usr/bin/env python3
"""Empirical test suite for ToolShed written skill checks (CHECKS.md) and installer.

Validates that all skills have 3-5 Given/When/Then checks in CHECKS.md,
covering happy path, messy/ambiguous input, and failure/guardrail cases, with
all unexecuted checks strictly marked 'not run' and zero false 'passed' claims.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO / "skills"
STANDALONE_SKILLS = ["claim-to-chart", "design-system-from-notes", "intent-mirror", "learning-capture"]

sys.path.insert(0, str(REPO / "tools"))
import check_skills as checker


class TestQAChecksStructureAndCoverage(unittest.TestCase):
    """Test suite for CHECKS.md files across skills."""

    def test_all_checks_files_exist(self):
        """Verify CHECKS.md exists in each standalone skill folder."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            self.assertTrue(checks_path.is_file(), f"Missing CHECKS.md for skill {skill}")
            self.assertGreater(checks_path.stat().st_size, 100, f"CHECKS.md too small for {skill}")

    def test_checks_count_between_3_and_5(self):
        """Verify each skill has between 3 and 5 testable checks."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            content = checks_path.read_text(encoding="utf-8")
            check_headings = re.findall(r"^## Check (\d+):[^\n]+", content, re.MULTILINE)
            self.assertGreaterEqual(
                len(check_headings), 3,
                f"Skill {skill} has fewer than 3 checks ({len(check_headings)})"
            )
            self.assertLessEqual(
                len(check_headings), 5,
                f"Skill {skill} has more than 5 checks ({len(check_headings)})"
            )
            # Verify numbering starts at 1 and is contiguous
            numbers = [int(n) for n in check_headings]
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)), f"Non-contiguous check numbers in {skill}")

    def test_given_when_then_and_status_in_every_check(self):
        """Verify every check has Given, When, Then, and Status clauses."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            content = checks_path.read_text(encoding="utf-8")
            sections = re.split(r"^## Check \d+:", content, flags=re.MULTILINE)[1:]
            for idx, sec in enumerate(sections, 1):
                self.assertIn("- **Given:**", sec, f"{skill} Check {idx} missing Given clause")
                self.assertIn("- **When:**", sec, f"{skill} Check {idx} missing When clause")
                self.assertIn("- **Then:**", sec, f"{skill} Check {idx} missing Then clause")
                self.assertIn("- **Status:**", sec, f"{skill} Check {idx} missing Status clause")

                # Verify clauses have substantive content (>10 chars)
                given_match = re.search(r"-\s+\*\*Given:\*\*\s+([^\n]+)", sec)
                when_match = re.search(r"-\s+\*\*When:\*\*\s+([^\n]+)", sec)
                then_match = re.search(r"-\s+\*\*Then:\*\*\s+([^\n]+)", sec)
                self.assertIsNotNone(given_match, f"{skill} Check {idx} Given parse failed")
                self.assertIsNotNone(when_match, f"{skill} Check {idx} When parse failed")
                self.assertIsNotNone(then_match, f"{skill} Check {idx} Then parse failed")

                self.assertGreater(len(given_match.group(1).strip()), 10)
                self.assertGreater(len(when_match.group(1).strip()), 10)
                self.assertGreater(len(then_match.group(1).strip()), 10)

    def test_honest_execution_status_not_run(self):
        """Verify all unexecuted checks are honestly marked 'not run' and zero claim 'passed'."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            content = checks_path.read_text(encoding="utf-8")

            # Check that Status line contains 'not run'
            status_lines = re.findall(r"-\s+\*\*Status:\*\*\s+([^\n]+)", content)
            self.assertEqual(len(status_lines), 4, f"{skill} should have exactly 4 status lines")
            for idx, status in enumerate(status_lines, 1):
                clean_status = status.strip().rstrip(".").lower()
                self.assertEqual(
                    clean_status, "not run",
                    f"{skill} Check {idx} status is '{status}', expected 'not run'"
                )

            # Ensure word 'passed' never appears in CHECKS.md
            self.assertEqual(
                len(re.findall(r"\bpassed\b", content, re.IGNORECASE)), 0,
                f"{skill} CHECKS.md contains forbidden claim 'passed'"
            )

    def test_scenario_coverage_happy_messy_failure(self):
        """Verify each skill covers happy path, messy/ambiguous input, and failure/guardrail case."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            content = checks_path.read_text(encoding="utf-8")
            headings = re.findall(r"^## Check \d+:\s*([^\n]+)", content, re.MULTILINE)
            headings_lower = " ".join(headings).lower()

            # Must cover happy path
            self.assertTrue(
                "happy path" in headings_lower or "verified" in headings_lower or "clean" in headings_lower,
                f"{skill} missing happy path scenario: {headings}"
            )
            # Must cover messy/ambiguous input
            self.assertTrue(
                "messy" in headings_lower or "disputed" in headings_lower or "sketch" in headings_lower or "overwhelm" in headings_lower,
                f"{skill} missing messy/ambiguous input scenario: {headings}"
            )
            # Must cover failure/guardrail case
            self.assertTrue(
                "failure" in headings_lower or "guardrail" in headings_lower or "failing" in headings_lower or "rumour" in headings_lower,
                f"{skill} missing failure/guardrail scenario: {headings}"
            )

    def test_readme_links_to_checks_md(self):
        """Verify every skill README.md links to CHECKS.md and the link resolves."""
        for skill in STANDALONE_SKILLS:
            readme_path = SKILLS_DIR / skill / "README.md"
            content = readme_path.read_text(encoding="utf-8")
            self.assertIn("CHECKS.md", content, f"{skill}/README.md does not reference CHECKS.md")
            # Verify markdown link format
            self.assertTrue(
                re.search(r"\[[^\]]+\]\(CHECKS\.md\)", content),
                f"{skill}/README.md does not contain markdown link to CHECKS.md"
            )

    def test_checks_md_banned_words_and_australian_spelling(self):
        """Verify zero banned words and Australian spelling throughout CHECKS.md files."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            content = checks_path.read_text(encoding="utf-8")

            # Banned words
            banned_matches = checker.BANNED_WORDS_PATTERN.findall(content)
            self.assertEqual(
                banned_matches, [],
                f"{skill}/CHECKS.md contains banned terms: {banned_matches}"
            )

            # Australian spelling check
            for pattern, aus in checker.AMERICAN_TO_AUS.items():
                m = re.findall(pattern, content, re.IGNORECASE)
                self.assertEqual(
                    m, [],
                    f"{skill}/CHECKS.md contains US spelling '{m}' (expected '{aus}')"
                )

    def test_checks_md_readability_metrics(self):
        """Verify CHECKS.md meets Flesch-Kincaid Grade Level <= 6.5 and ASL <= 18.0."""
        for skill in STANDALONE_SKILLS:
            checks_path = SKILLS_DIR / skill / "CHECKS.md"
            content = checks_path.read_text(encoding="utf-8")
            fkgl, asl, wc, sc = checker.calculate_readability(content)
            self.assertLessEqual(
                fkgl, 6.5,
                f"{skill}/CHECKS.md FKGL {fkgl:.2f} exceeds 6.5 threshold"
            )
            self.assertLessEqual(
                asl, 18.0,
                f"{skill}/CHECKS.md ASL {asl:.2f} exceeds 18.0 threshold"
            )


class TestOneStepInstallerBundle(unittest.TestCase):
    """Test suite for skills/install-skills.sh (SK-7 / #61)."""

    def test_installer_dry_run_install_backup_and_remove(self):
        """Verify dry-run, clean install, collision backup, and removal."""
        import subprocess
        import tempfile

        installer = SKILLS_DIR / "install-skills.sh"
        self.assertTrue(installer.exists(), "skills/install-skills.sh must exist")

        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "custom-skills"

            # 1. Dry-run should not create target dir
            res_dry = subprocess.run(
                ["bash", str(installer), "--dry-run", "--target", str(target)],
                capture_output=True, text=True, check=True
            )
            self.assertIn("[dry-run]", res_dry.stdout)
            self.assertFalse(target.exists())

            # 2. Clean install copies all 4 standalone skills
            res_inst = subprocess.run(
                ["bash", str(installer), "--target", str(target)],
                capture_output=True, text=True, check=True
            )
            for skill in STANDALONE_SKILLS:
                self.assertTrue((target / skill / "SKILL.md").exists(), f"Missing installed {skill}/SKILL.md")

            # 3. Re-running backs up existing skill folders before replacing
            marker = target / "intent-mirror" / "custom-marker.txt"
            marker.write_text("user customization", encoding="utf-8")
            res_reinst = subprocess.run(
                ["bash", str(installer), "--target", str(target)],
                capture_output=True, text=True, check=True
            )
            self.assertIn("Backed up existing intent-mirror", res_reinst.stdout)
            backups = list(target.glob("intent-mirror.backup-*"))
            self.assertEqual(len(backups), 1)
            self.assertTrue((backups[0] / "custom-marker.txt").exists())

            # 4. --remove deletes the 4 installed standalone skills
            res_rem = subprocess.run(
                ["bash", str(installer), "--remove", "--target", str(target)],
                capture_output=True, text=True, check=True
            )
            for skill in STANDALONE_SKILLS:
                self.assertFalse((target / skill).exists(), f"{skill} should be removed")


if __name__ == "__main__":
    unittest.main()

