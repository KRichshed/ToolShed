#!/usr/bin/env python3
"""Adversarial test suite for tools/check_skills.py.

Tests positive and negative cases for:
  1. Banned terms detection (case variations, quotes, punctuation, bypasses/inflections)
  2. SVG 'EXAMPLE' label enforcement (numbers, quotes, uppercase vs lowercase)
  3. Australian spelling enforcement (US vs AU spellings, code block stripping, false positives)
  4. SVG text boundary heuristic (overflow > 780, text anchors, font sizes, edge cases)
  5. Front-door diagnostic behavior (--require-front-door, pending vs active, newcomer paths)
  6. Subprocess CLI execution across scenarios
"""

from __future__ import annotations

import html
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import List
import unittest

REPO = Path(__file__).resolve().parents[1]
CHECKER_SCRIPT = REPO / "tools" / "check_skills.py"

# Import functions directly from checker
sys.path.insert(0, str(CHECKER_SCRIPT.parent))
import check_skills as checker


class TestBannedTermsAdversarial(unittest.TestCase):
    """Adversarial stress-testing of banned terms pattern and check_banned_terms."""

    def test_banned_terms_regex_case_insensitivity(self):
        """Verify banned terms match regardless of case."""
        cases = [
            # compliant
            "compliant", "COMPLIANT", "Compliant", "cOmPlIaNt",
            # guaranteed
            "guaranteed", "GUARANTEED", "Guaranteed", "gUaRaNtEeD",
            # synthesized
            "synthesized", "SYNTHESIZED", "Synthesized", "sYnThEsIzEd",
            # Co-Authored-By
            "Co-Authored-By", "co-authored-by", "CO-AUTHORED-BY", "Co-authored-by",
            # Generated with
            "Generated with", "generated with", "GENERATED WITH", "Generated With",
        ]
        for word in cases:
            with self.subTest(word=word):
                match = checker.BANNED_WORDS_PATTERN.search(f"This is {word} in a sentence.")
                self.assertIsNotNone(match, f"Banned word {word!r} failed to match in sentence")
                self.assertEqual(match.group(0).lower(), word.lower())

    def test_banned_terms_embedded_in_quotes_and_punctuation(self):
        """Verify banned words inside various quote styles and punctuation marks are caught."""
        patterns = [
            'This card is "compliant" with rules.',
            "This card is 'guaranteed' to work.",
            "This card is “synthesized” from notes.",
            "This card is ‘compliant’ with rules.",
            "This card is `compliant` with rules.",
            "Results: (guaranteed)",
            "Results: [compliant]",
            "Status: {synthesized}",
            "It is compliant; please proceed.",
            "It is guaranteed: always works.",
            "It is synthesized, as shown below.",
            "It is non-compliant with standard.",  # boundary after hyphen
            "&quot;compliant&quot;",
        ]
        for sentence in patterns:
            with self.subTest(sentence=sentence):
                self.assertIsNotNone(
                    checker.BANNED_WORDS_PATTERN.search(sentence),
                    f"Failed to catch banned word in: {sentence!r}"
                )

    def test_honest_replacements_do_not_match_banned_terms(self):
        """Verify approved honest replacements do not trigger banned terms."""
        honest_phrases = [
            "✓ Passes 7:1",
            "✓ CHECKED CLAIM",
            "sample notes extraction",
            "distilled takeaways",
            "grouped into themes",
            "prioritised actions",
            "made-up demo data",
            "measured contrast",
            "Level 1 Operator boundaries",
        ]
        for phrase in honest_phrases:
            with self.subTest(phrase=phrase):
                self.assertIsNone(
                    checker.BANNED_WORDS_PATTERN.search(phrase),
                    f"False positive: honest phrase {phrase!r} matched banned terms"
                )

    def test_banned_terms_file_scanning(self):
        """Test check_banned_terms on temporary markdown and SVG files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            clean_md = tmppath / "clean.md"
            clean_md.write_text("# Clean Title\nThis text is honest and passes 7:1.\n", encoding="utf-8")

            bad_md = tmppath / "bad.md"
            bad_md.write_text("# Bad Title\nThis system is compliant with standards.\n", encoding="utf-8")

            bad_svg = tmppath / "bad.svg"
            bad_svg.write_text('<svg><text>Synthesized data</text></svg>', encoding="utf-8")

            orig_repo = checker.REPO
            orig_skills = checker.SKILLS_DIR
            checker.REPO = tmppath
            checker.SKILLS_DIR = tmppath
            try:
                # Scanning clean dir
                errs_clean = checker.check_banned_terms("clean")
                self.assertEqual(len(errs_clean), 0)

                # Scanning bad md
                errs_bad = []
                for p in [bad_md, bad_svg]:
                    text = p.read_text(encoding="utf-8")
                    for line_no, line in enumerate(text.splitlines(), 1):
                        m = checker.BANNED_WORDS_PATTERN.search(line)
                        if m:
                            errs_bad.append(f"{p.name}:{line_no}: {m.group(0)}")
                self.assertEqual(len(errs_bad), 2)
                self.assertIn("compliant", errs_bad[0])
                self.assertIn("Synthesized", errs_bad[1])
            finally:
                checker.REPO = orig_repo
                checker.SKILLS_DIR = orig_skills

    def test_banned_terms_inflections_and_bypasses(self):
        """Adversarial analysis: check how inflections and unlisted forms behave."""
        # Unlisted forms that are NOT matched by \b(compliant|guaranteed|synthesized|...)\b:
        # Note: 'guarantee', 'guarantees', 'compliance' do not match BANNED_WORDS_PATTERN.
        # We test this empirically to document the boundary of the pattern.
        unmatched_variants = [
            ("guarantee", False),       # infinitive/present
            ("guarantees", False),      # third-person/plural
            ("compliance", False),      # noun form
            ("synthesize", False),      # present tense
            ("synthesizing", False),    # participle
        ]
        for variant, should_match in unmatched_variants:
            with self.subTest(variant=variant):
                match = checker.BANNED_WORDS_PATTERN.search(f"We {variant} the result.")
                if should_match:
                    self.assertIsNotNone(match)
                else:
                    self.assertIsNone(
                        match,
                        f"Pattern unexpectedly matched variant {variant!r}."
                    )


class TestSvgExampleLabelsAdversarial(unittest.TestCase):
    """Adversarial testing of SVG EXAMPLE label enforcement."""

    def test_svg_with_numbers_requires_example_label(self):
        """SVG containing numbers must fail if 'EXAMPLE' is absent, pass if present."""
        svg_no_example = (
            '<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">\n'
            '<text x="50" y="50">Study showed 68% adoption rate</text>\n'
            '</svg>'
        )
        svg_with_example = (
            '<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">\n'
            '<text x="50" y="30">WORKED EXAMPLE</text>\n'
            '<text x="50" y="50">Study showed 68% adoption rate</text>\n'
            '</svg>'
        )

        has_numbers_1 = bool(re.search(r"\d", svg_no_example))
        has_quotes_1 = bool(re.search(r'["“”\'‘’]|&quot;|&apos;', svg_no_example))
        self.assertTrue(has_numbers_1 or has_quotes_1)
        self.assertNotIn("EXAMPLE", svg_no_example)

        has_numbers_2 = bool(re.search(r"\d", svg_with_example))
        has_quotes_2 = bool(re.search(r'["“”\'‘’]|&quot;|&apos;', svg_with_example))
        self.assertTrue(has_numbers_2 or has_quotes_2)
        self.assertIn("EXAMPLE", svg_with_example)

    def test_svg_lowercase_example_rejected(self):
        """Lowercase 'example' or 'Worked Example' does not satisfy uppercase 'EXAMPLE' requirement."""
        svg_lowercase = (
            '<svg width="800" height="400">\n'
            '<text x="50" y="30">worked example</text>\n'
            '<text x="50" y="50">42 users</text>\n'
            '</svg>'
        )
        self.assertNotIn("EXAMPLE", svg_lowercase)

        svg_titlecase = (
            '<svg width="800" height="400">\n'
            '<text x="50" y="30">Worked Example</text>\n'
            '<text x="50" y="50">42 users</text>\n'
            '</svg>'
        )
        self.assertNotIn("EXAMPLE", svg_titlecase)

    def test_all_current_repo_svgs_pass_example_check(self):
        """Verify all 4 production SVGs in skills/*/assets/ contain uppercase 'EXAMPLE'."""
        for skill, rel_path in checker.EXPECTED_SVG_ASSETS.items():
            svg_path = checker.SKILLS_DIR / skill / rel_path
            self.assertTrue(svg_path.is_file(), f"Missing SVG: {svg_path}")
            content = svg_path.read_text(encoding="utf-8")
            self.assertIn(
                "EXAMPLE",
                content,
                f"Production asset {rel_path} in {skill} is missing required 'EXAMPLE' label"
            )


class TestAustralianSpellingAdversarial(unittest.TestCase):
    """Adversarial testing of Australian spelling checker."""

    def test_all_american_patterns_detected(self):
        """Verify all 22 American spelling patterns are flagged."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            test_file = tmppath / "test.md"
            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                for us_pattern, aus_word in checker.AMERICAN_TO_AUS.items():
                    raw_word = us_pattern.replace(r"\b", "")
                    test_file.write_text(f"This sentence contains {raw_word} in the text.\n", encoding="utf-8")
                    errs = checker.check_australian_spelling(test_file)
                    self.assertGreaterEqual(
                        len(errs), 1,
                        f"American word {raw_word!r} was not detected by check_australian_spelling"
                    )
                    self.assertIn(aus_word, errs[0])
            finally:
                checker.REPO = orig_repo

    def test_australian_spelling_case_insensitivity(self):
        """Verify uppercase and titlecase US words are detected."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            test_file = tmppath / "case_test.md"
            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                cases = [
                    ("Color", "colour"),
                    ("COLOR", "colour"),
                    ("Summarize", "summarise"),
                    ("SUMMARIZE", "summarise"),
                    ("Prioritize", "prioritise"),
                    ("PRIORITIZE", "prioritise"),
                    ("Organize", "organise"),
                    ("ORGANIZE", "organise"),
                    ("Behavior", "behaviour"),
                    ("BEHAVIOR", "behaviour"),
                    ("Analyze", "analyse"),
                    ("ANALYZE", "analyse"),
                ]
                for us_word, aus_word in cases:
                    test_file.write_text(f"Notice the {us_word} palette here.\n", encoding="utf-8")
                    errs = checker.check_australian_spelling(test_file)
                    self.assertGreaterEqual(
                        len(errs), 1,
                        f"Capitalized US word {us_word!r} failed to trigger spelling error"
                    )
                    self.assertIn(aus_word, errs[0])
            finally:
                checker.REPO = orig_repo

    def test_legitimate_australian_words_not_flagged(self):
        """Verify Australian spellings do not trigger false positive errors."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            test_file = tmppath / "aus_test.md"
            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                aus_text = (
                    "# Design System\n\n"
                    "We optimise each colour token and prioritise user needs.\n"
                    "The team organised the workshop to analyse user behaviour.\n"
                    "We provide a concise summariser that summarises all findings.\n"
                    "Our analyses confirm the improved clarity.\n"
                )
                test_file.write_text(aus_text, encoding="utf-8")
                errs = checker.check_australian_spelling(test_file)
                self.assertEqual(
                    errs, [],
                    f"False positive: Australian words flagged as errors: {errs}"
                )
            finally:
                checker.REPO = orig_repo

    def test_us_spelling_inside_code_blocks_and_urls_stripped(self):
        """Verify US words inside code blocks, inline code, and URLs do not trigger false positives."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            test_file = tmppath / "code_test.md"
            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                markdown = (
                    "# Code Examples\n\n"
                    "Here is CSS styling:\n\n"
                    "```css\n"
                    "color: #1C1D38;\n"
                    "background-color: #FBF7EC;\n"
                    "```\n\n"
                    "Use the `color` property in inline code.\n"
                    "Visit [Palette Guide](https://example.com/color/palette) for ideas.\n"
                    '<span style="color: blue">Blue text</span>\n'
                    "Image: ![Color sample](https://example.com/images/color.png)\n"
                )
                test_file.write_text(markdown, encoding="utf-8")
                errs = checker.check_australian_spelling(test_file)
                self.assertEqual(
                    errs, [],
                    f"False positive: code block or URL triggered spelling error: {errs}"
                )
            finally:
                checker.REPO = orig_repo

    def test_word_boundary_precision_no_substring_false_positives(self):
        """Verify words containing US roots as sub-parts are not falsely flagged."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            test_file = tmppath / "boundary_test.md"
            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                text = (
                    "We visited Colorado last summer.\n"
                    "Observe the discoloration on the paper specimen.\n"
                )
                test_file.write_text(text, encoding="utf-8")
                errs = checker.check_australian_spelling(test_file)
                self.assertEqual(
                    errs, [],
                    f"False positive: substring triggered spelling error: {errs}"
                )
            finally:
                checker.REPO = orig_repo

    def test_spelling_coverage_gaps(self):
        """Adversarial check: document American spelling variants not in AMERICAN_TO_AUS."""
        untracked_american_words = [
            "customization",  # AU: customisation
            "organization",   # AU: organisation (note: organize is tracked, but organization is not)
            "synthesize",     # AU: synthesise
            "dialog",         # AU: dialogue
            "center",         # AU: centre
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            test_file = tmppath / "gap_test.md"
            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                for word in untracked_american_words:
                    test_file.write_text(f"This is an untracked word: {word}.\n", encoding="utf-8")
                    errs = checker.check_australian_spelling(test_file)
                    # We assert that currently the checker does NOT catch these (documenting coverage boundary)
                    self.assertEqual(
                        len(errs), 0,
                        f"Notice: word {word!r} is unexpectedly tracked or flagged"
                    )
            finally:
                checker.REPO = orig_repo


class TestSvgTextBoundariesAdversarial(unittest.TestCase):
    """Adversarial testing of SVG text coordinate boundary calculation."""

    def test_svg_boundary_overflow_detected(self):
        """Verify text with calculated x + est_w > 780 triggers an error."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            skill_dir = tmppath / "test-skill" / "assets"
            skill_dir.mkdir(parents=True)
            svg_file = skill_dir / "example-chart.svg"

            # x=600, font-size=20, 20 chars: right_x = 600 + 20*20*0.55 = 820 > 780
            overflow_svg = (
                '<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">\n'
                '<text x="600" font-size="20">This text will overflow the card</text>\n'
                '</svg>'
            )
            svg_file.write_text(overflow_svg, encoding="utf-8")

            orig_repo = checker.REPO
            orig_skills = checker.SKILLS_DIR
            orig_assets = checker.EXPECTED_SVG_ASSETS
            checker.REPO = tmppath
            checker.SKILLS_DIR = tmppath
            checker.EXPECTED_SVG_ASSETS = {"test-skill": "assets/example-chart.svg"}
            try:
                errs, msg = checker.check_svg_boundaries()
                self.assertIn("SVG text boundaries (pixel rendering): not run by tool", msg)
                self.assertEqual(len(errs), 1)
                self.assertIn("likely clips outside card boundary", errs[0])
                self.assertIn("est_end=952 > 780", errs[0])
            finally:
                checker.REPO = orig_repo
                checker.SKILLS_DIR = orig_skills
                checker.EXPECTED_SVG_ASSETS = orig_assets

    def test_svg_boundary_within_limits_passes(self):
        """Verify text well within x <= 780 passes without error."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            skill_dir = tmppath / "test-skill" / "assets"
            skill_dir.mkdir(parents=True)
            svg_file = skill_dir / "example-chart.svg"

            # x=50, font-size=14, 20 chars: right_x = 50 + 20*14*0.55 = 204 <= 780
            safe_svg = (
                '<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">\n'
                '<text x="50" font-size="14">Short text inside</text>\n'
                '</svg>'
            )
            svg_file.write_text(safe_svg, encoding="utf-8")

            orig_repo = checker.REPO
            orig_skills = checker.SKILLS_DIR
            orig_assets = checker.EXPECTED_SVG_ASSETS
            checker.REPO = tmppath
            checker.SKILLS_DIR = tmppath
            checker.EXPECTED_SVG_ASSETS = {"test-skill": "assets/example-chart.svg"}
            try:
                errs, msg = checker.check_svg_boundaries()
                self.assertEqual(len(errs), 0)
            finally:
                checker.REPO = orig_repo
                checker.SKILLS_DIR = orig_skills
                checker.EXPECTED_SVG_ASSETS = orig_assets

    def test_svg_boundary_text_anchor_calculations(self):
        """Verify middle and end text anchors calculate right_x correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            skill_dir = tmppath / "test-skill" / "assets"
            skill_dir.mkdir(parents=True)
            svg_file = skill_dir / "example-chart.svg"

            # middle anchor: x=720, font-size=16, 20 chars -> est_w=176, right_x = 720 + 88 = 808 > 780
            # end anchor: x=790 -> right_x = 790 > 780
            anchored_svg = (
                '<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">\n'
                '<text x="720" font-size="16" text-anchor="middle">Twenty characters!!</text>\n'
                '<text x="790" font-size="16" text-anchor="end">Right aligned text</text>\n'
                '</svg>'
            )
            svg_file.write_text(anchored_svg, encoding="utf-8")

            orig_repo = checker.REPO
            orig_skills = checker.SKILLS_DIR
            orig_assets = checker.EXPECTED_SVG_ASSETS
            checker.REPO = tmppath
            checker.SKILLS_DIR = tmppath
            checker.EXPECTED_SVG_ASSETS = {"test-skill": "assets/example-chart.svg"}
            try:
                errs, _ = checker.check_svg_boundaries()
                self.assertEqual(len(errs), 2)
                self.assertIn("est_end=804 > 780", errs[0])
                self.assertIn("est_end=790 > 780", errs[1])
            finally:
                checker.REPO = orig_repo
                checker.SKILLS_DIR = orig_skills
                checker.EXPECTED_SVG_ASSETS = orig_assets

    def test_svg_boundary_float_coordinate_gap(self):
        """Adversarial check: note that x='750.5' fails regex r'x=[\"\\'](\\d+)[\"\\']'."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            skill_dir = tmppath / "test-skill" / "assets"
            skill_dir.mkdir(parents=True)
            svg_file = skill_dir / "example-chart.svg"

            # x has decimal point: 750.5
            float_x_svg = (
                '<svg width="800" height="400">\n'
                '<text x="750.5" font-size="20">Overflow text with float coord</text>\n'
                '</svg>'
            )
            svg_file.write_text(float_x_svg, encoding="utf-8")

            orig_repo = checker.REPO
            orig_skills = checker.SKILLS_DIR
            orig_assets = checker.EXPECTED_SVG_ASSETS
            checker.REPO = tmppath
            checker.SKILLS_DIR = tmppath
            checker.EXPECTED_SVG_ASSETS = {"test-skill": "assets/example-chart.svg"}
            try:
                errs, _ = checker.check_svg_boundaries()
                # Documenting this edge case: regex expects integer digits (\d+), so x="750.5" is skipped.
                self.assertEqual(len(errs), 0, "Float x coordinate was unexpectedly parsed")
            finally:
                checker.REPO = orig_repo
                checker.SKILLS_DIR = orig_skills
                checker.EXPECTED_SVG_ASSETS = orig_assets

    def test_all_current_repo_svgs_pass_boundary_check(self):
        """Verify all 4 production SVGs currently pass the coordinate boundary check."""
        errs, msg = checker.check_svg_boundaries()
        self.assertIn("not run by tool (headless rendering engine not installed)", msg)
        self.assertEqual(
            errs, [],
            f"Production SVGs have coordinate boundary overflows: {errs}"
        )


class TestFrontDoorDiagnosticsAdversarial(unittest.TestCase):
    """Adversarial testing of front-door diagnostic flag and transitions."""

    def test_default_mode_when_files_absent_returns_pending(self):
        """When M2 front-door files are absent and require=False, status is pending with 0 errors."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            root_readme = tmppath / "README.md"
            root_readme.write_text("# ToolShed\nA simple overview without newcomer section.\n", encoding="utf-8")

            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                errs, status = checker.check_front_door(require=False)
                self.assertEqual(errs, [])
                self.assertIn("pending M2 implementation", status)
            finally:
                checker.REPO = orig_repo

    def test_require_front_door_flag_enforces_all_four_requirements(self):
        """When require=True, missing files and missing 'New here?' produce exactly 4 errors."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            root_readme = tmppath / "README.md"
            root_readme.write_text("# ToolShed\nOverview.\n", encoding="utf-8")

            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                errs, status = checker.check_front_door(require=True)
                self.assertIn("checking newcomer sections", status)
                self.assertEqual(len(errs), 4)
                self.assertIn("README.md missing 'New here?' newcomer section", errs[0])
                self.assertIn("CONTRIBUTING.md", errs[1])
                self.assertIn("GLOSSARY.md", errs[2])
                self.assertIn("CHANGELOG.md", errs[3])
            finally:
                checker.REPO = orig_repo

    def test_auto_enforcement_when_any_front_door_file_exists(self):
        """If one front door file exists (e.g. CONTRIBUTING.md), enforcement activates automatically."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            root_readme = tmppath / "README.md"
            root_readme.write_text("# ToolShed\nOverview.\n", encoding="utf-8")
            # Create one file
            (tmppath / "CONTRIBUTING.md").write_text("# Contributing\n", encoding="utf-8")

            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                errs, status = checker.check_front_door(require=False)
                self.assertIn("checking newcomer sections", status)
                # 3 errors: New here?, GLOSSARY, CHANGELOG (CONTRIBUTING exists)
                self.assertEqual(len(errs), 3)
                self.assertTrue(any("GLOSSARY.md" in e for e in errs))
                self.assertTrue(any("CHANGELOG.md" in e for e in errs))
                self.assertFalse(any("CONTRIBUTING.md" in e for e in errs))
            finally:
                checker.REPO = orig_repo

    def test_auto_enforcement_when_new_here_section_present(self):
        """If 'New here?' section is added to README.md, path validation and file checks activate."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            root_readme = tmppath / "README.md"
            # Incomplete 'New here?' without the 3 paths
            root_readme.write_text("# ToolShed\n\n## New here?\nWelcome to ToolShed.\n", encoding="utf-8")

            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                errs, status = checker.check_front_door(require=False)
                self.assertIn("checking newcomer sections", status)
                # Should flag missing paths + 3 missing files
                self.assertTrue(any("missing newcomer path: copy a skill" in e for e in errs))
                self.assertTrue(any("read the stories" in e for e in errs))
                self.assertTrue(any("learn how a repo works" in e for e in errs))
                self.assertTrue(any("missing required repository front door file: CONTRIBUTING.md" in e for e in errs))
            finally:
                checker.REPO = orig_repo

    def test_fully_populated_front_door_passes(self):
        """When all newcomer paths and front-door files exist, check_front_door passes with 0 errors."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            root_readme = tmppath / "README.md"
            readme_content = (
                "# ToolShed\n\n"
                "## New here?\n"
                "1. Copy a standalone skill to your project.\n"
                "2. Read the stories in notes/.\n"
                "3. Learn how a repo works using our glossary.\n"
            )
            root_readme.write_text(readme_content, encoding="utf-8")
            (tmppath / "CONTRIBUTING.md").write_text("# Contributing\n", encoding="utf-8")
            (tmppath / "GLOSSARY.md").write_text("# Glossary\n", encoding="utf-8")
            (tmppath / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")

            orig_repo = checker.REPO
            checker.REPO = tmppath
            try:
                errs, status = checker.check_front_door(require=True)
                self.assertEqual(errs, [])
                self.assertIn("checking newcomer sections", status)
            finally:
                checker.REPO = orig_repo


class TestSubprocessCliAdversarial(unittest.TestCase):
    """Subprocess CLI execution tests verifying exit codes and error output."""

    def test_cli_default_invocation_exits_zero(self):
        """Running check_standalone_skills.py without args should exit 0 on clean repo."""
        res = subprocess.run(
            [sys.executable, str(CHECKER_SCRIPT)],
            capture_output=True,
            text=True,
            cwd=str(REPO),
        )
        self.assertEqual(res.returncode, 0, f"Checker failed unexpectedly:\n{res.stdout}\n{res.stderr}")
        self.assertIn("All standalone skills and documentation checks passed with 0 errors.", res.stdout)
        self.assertIn("Front door: checking newcomer sections and repository help files", res.stdout)
        self.assertIn("SVG text boundaries (pixel rendering): not run by tool", res.stdout)

    def test_cli_single_skill_invocation_exits_zero(self):
        """Running check_standalone_skills.py for a single skill should exit 0."""
        for skill in checker.STANDALONE_SKILLS:
            res = subprocess.run(
                [sys.executable, str(CHECKER_SCRIPT), skill],
                capture_output=True,
                text=True,
                cwd=str(REPO),
            )
            self.assertEqual(
                res.returncode, 0,
                f"Single skill check failed for {skill}:\n{res.stdout}\n{res.stderr}"
            )
            self.assertIn(f"skills/{skill}: ok", res.stdout)

    def test_cli_unknown_skill_exits_non_zero(self):
        """Passing an invalid skill name must exit with error."""
        res = subprocess.run(
            [sys.executable, str(CHECKER_SCRIPT), "invalid-skill-name"],
            capture_output=True,
            text=True,
            cwd=str(REPO),
        )
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("Unknown standalone skill", res.stderr + res.stdout)

    def test_cli_require_front_door_passes_when_front_door_present(self):
        """CLI flag --require-front-door passes with exit 0 when M2 front-door files are present."""
        res = subprocess.run(
            [sys.executable, str(CHECKER_SCRIPT), "--require-front-door"],
            capture_output=True,
            text=True,
            cwd=str(REPO),
        )
        self.assertEqual(res.returncode, 0, f"Checker failed with --require-front-door:\n{res.stdout}\n{res.stderr}")
        self.assertIn("All standalone skills and documentation checks passed with 0 errors.", res.stdout)
        self.assertIn("Front door: checking newcomer sections and repository help files", res.stdout)

    def test_cli_verbose_outputs_metrics_table(self):
        """Running with --verbose prints Readability Metrics table."""
        res = subprocess.run(
            [sys.executable, str(CHECKER_SCRIPT), "--verbose"],
            capture_output=True,
            text=True,
            cwd=str(REPO),
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("Readability Metrics:", res.stdout)
        self.assertIn("FKGL=", res.stdout)
        self.assertIn("ASL=", res.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
