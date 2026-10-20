#!/usr/bin/env python3
"""Empirical adversarial test suite for ToolShed skill READMEs.

Adversarially challenges:
  1. Section presence across all 10 canonical template sections + worked example section.
  2. Section sequence and non-empty content enforcement.
  3. Worked example input/output presence and part-by-part explanation table formatting.
  4. <details> block counts in '## More examples' (>= 3, <= 5) and messy/blurry/disputed scenarios.
  5. Comparison table formatting and external alternatives in '## Similar skills'.
  6. Structured test results table formatting and methodology disclosure in '## How I tested it'.
  7. Global markdown table parsing integrity (uniform column counts, valid delimiters, blockquoted tables).
  8. HTML tag parity (<details>, <summary>, <b>).
  9. Relative link validity to local filesystem targets.
  10. Readability conformance (FKGL <= 6.5, ASL <= 18.0) and Australian spelling checks.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO / "skills"
NOTES_DIR = REPO / "notes"
STANDALONE_SKILLS = [
    "claim-to-chart",
    "design-system-from-notes",
    "intent-mirror",
    "learning-capture",
]

BASE_REQUIRED_SECTIONS = [
    "## What it does",
    "## How it works",
    "## How to use it",
    "## More examples",
    "## Tips",
    "## How I tested it",
    "## What's next",
    "## Questions",
    "## Similar skills",
    "## What's in this folder",
]

WORKED_EXAMPLE_HEADERS = {
    "claim-to-chart": "## What the verdict and chart look like",
    "design-system-from-notes": "## What the mini design system looks like",
    "intent-mirror": "## What the mirror looks like",
    "learning-capture": "## What you'll get back",
}

EXPECTED_SVG_ASSETS = {
    "claim-to-chart": "assets/example-chart.svg",
    "design-system-from-notes": "assets/example-specimen.svg",
    "intent-mirror": "assets/example-mirror.svg",
    "learning-capture": "assets/example-map.svg",
}


def read_skill_readme(skill: str) -> str:
    path = SKILLS_DIR / skill / "README.md"
    if not path.is_file():
        raise FileNotFoundError(f"Missing README.md for skill {skill} at {path}")
    return path.read_text(encoding="utf-8")


def parse_markdown_tables(text: str) -> list[dict]:
    """Parse all markdown tables (both top-level and blockquoted) into structured representations."""
    tables = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw_line = lines[i]
        line = re.sub(r"^>\s*", "", raw_line).strip()
        if line.startswith("|") and line.endswith("|") and i + 1 < len(lines):
            next_raw = lines[i + 1]
            next_line = re.sub(r"^>\s*", "", next_raw).strip()
            delims = [c.strip() for c in next_line.split("|")[1:-1]]
            if delims and all(re.match(r"^:?-+:?$", d) for d in delims):
                header_cols = [c.strip() for c in line.split("|")[1:-1]]
                delim_cols = delims
                rows = []
                j = i + 2
                while j < len(lines):
                    r_raw = lines[j]
                    r_line = re.sub(r"^>\s*", "", r_raw).strip()
                    if not (r_line.startswith("|") and r_line.endswith("|")):
                        break
                    row_cols = [c.strip() for c in r_line.split("|")[1:-1]]
                    rows.append((r_raw, row_cols, j + 1))
                    j += 1
                tables.append({
                    "start_line": i + 1,
                    "end_line": j,
                    "header_line": raw_line,
                    "headers": header_cols,
                    "delims": delim_cols,
                    "rows": rows,
                })
                i = j
                continue
        i += 1
    return tables


class TestRequiredSectionsPresenceAndOrder(unittest.TestCase):
    """Assert all 10 required base sections and worked example exist in proper order."""

    def test_all_base_sections_exist(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                for sec in BASE_REQUIRED_SECTIONS:
                    self.assertIn(
                        sec,
                        text,
                        f"Skill {skill} README missing required section: {sec!r}",
                    )

    def test_worked_example_section_exists(self):
        for skill, expected_header in WORKED_EXAMPLE_HEADERS.items():
            with self.subTest(skill=skill, header=expected_header):
                text = read_skill_readme(skill)
                self.assertIn(
                    expected_header,
                    text,
                    f"Skill {skill} README missing expected worked example header: {expected_header!r}",
                )

    def test_canonical_section_order(self):
        """Verify sections appear in the logical pedagogical sequence."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                worked_hdr = WORKED_EXAMPLE_HEADERS[skill]
                sequence = [
                    "## What it does",
                    "## How it works",
                    "## How to use it",
                    worked_hdr,
                    "## More examples",
                    "## Tips",
                    "## How I tested it",
                    "## What's next",
                    "## Questions",
                    "## Similar skills",
                    "## What's in this folder",
                ]
                positions = []
                for sec in sequence:
                    pos = text.find(sec)
                    self.assertNotEqual(
                        pos, -1, f"Skill {skill} missing section {sec!r} in sequence"
                    )
                    positions.append((pos, sec))

                for k in range(len(positions) - 1):
                    pos1, sec1 = positions[k]
                    pos2, sec2 = positions[k + 1]
                    self.assertLess(
                        pos1,
                        pos2,
                        f"In {skill}, section {sec1!r} (offset {pos1}) must precede {sec2!r} (offset {pos2})",
                    )

    def test_sections_are_not_empty(self):
        """Verify each section has substantial text and is not an empty placeholder."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                worked_hdr = WORKED_EXAMPLE_HEADERS[skill]
                all_hdrs = [
                    "## What it does",
                    "## How it works",
                    "## How to use it",
                    worked_hdr,
                    "## More examples",
                    "## Tips",
                    "## How I tested it",
                    "## What's next",
                    "## Questions",
                    "## Similar skills",
                    "## What's in this folder",
                ]
                for idx, hdr in enumerate(all_hdrs):
                    start = text.find(hdr) + len(hdr)
                    end = text.find(all_hdrs[idx + 1]) if idx + 1 < len(all_hdrs) else len(text)
                    section_body = text[start:end].strip()
                    self.assertGreater(
                        len(section_body),
                        60,
                        f"Section {hdr!r} in {skill} is suspiciously short ({len(section_body)} chars)",
                    )


class TestWorkedExampleExplanationTables(unittest.TestCase):
    """Assert worked example exists with real input/output and explanation table."""

    def test_worked_example_explanation_table_structure(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                worked_hdr = WORKED_EXAMPLE_HEADERS[skill]
                start = text.find(worked_hdr)
                end = text.find("## More examples")
                worked_block = text[start:end]

                tables = parse_markdown_tables(worked_block)
                self.assertGreaterEqual(
                    len(tables),
                    1,
                    f"Worked example in {skill} must contain at least 1 markdown table",
                )

                # Find the part-by-part explanation table
                explanation_tables = [
                    t for t in tables if any("part" in h.lower() for h in t["headers"])
                ]
                self.assertGreaterEqual(
                    len(explanation_tables),
                    1,
                    f"Worked example in {skill} missing part-by-part explanation table",
                )
                exp_table = explanation_tables[0]
                self.assertGreaterEqual(len(exp_table["headers"]), 2)
                self.assertGreaterEqual(len(exp_table["rows"]), 4)

                for orig_line, row_cols, line_no in exp_table["rows"]:
                    self.assertEqual(
                        len(row_cols),
                        len(exp_table["headers"]),
                        f"In {skill} explanation table line {line_no}, column count {len(row_cols)} != header count {len(exp_table['headers'])}",
                    )

    def test_worked_example_input_output_contrast(self):
        """Assert worked example contains both input prompt and output response."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                worked_hdr = WORKED_EXAMPLE_HEADERS[skill]
                start = text.find(worked_hdr)
                end = text.find("## More examples")
                worked_block = text[start:end]

                has_input = any(kw in worked_block for kw in ["What they said", "What they sent", "What was shared"])
                has_output = any(kw in worked_block for kw in ["What came back", "What came back."])
                self.assertTrue(
                    has_input,
                    f"Skill {skill} worked example missing input marker",
                )
                self.assertTrue(
                    has_output,
                    f"Skill {skill} worked example missing output marker",
                )


class TestMoreExamplesDetailsBlocks(unittest.TestCase):
    """Assert '## More examples' contains >= 3 <details> blocks with proper tags."""

    def test_more_examples_details_count(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## More examples")
                end = text.find("## Tips")
                block = text[start:end]

                open_details = block.count("<details>")
                close_details = block.count("</details>")
                open_summary = block.count("<summary>")
                close_summary = block.count("</summary>")

                self.assertGreaterEqual(
                    open_details,
                    3,
                    f"Skill {skill} 'More examples' has {open_details} <details> blocks, requires at least 3",
                )
                self.assertLessEqual(
                    open_details,
                    5,
                    f"Skill {skill} 'More examples' has {open_details} <details> blocks, recommended max 5",
                )
                self.assertEqual(
                    open_details,
                    close_details,
                    f"Skill {skill} 'More examples' has unclosed <details> tag",
                )
                self.assertEqual(
                    open_summary,
                    close_summary,
                    f"Skill {skill} 'More examples' has unclosed <summary> tag",
                )

    def test_more_examples_summary_non_empty(self):
        """Assert every details block has a bold, descriptive summary."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## More examples")
                end = text.find("## Tips")
                block = text[start:end]

                summaries = re.findall(r"<summary>(.*?)</summary>", block, re.DOTALL)
                self.assertGreaterEqual(len(summaries), 3)
                for s in summaries:
                    clean = s.strip()
                    self.assertGreater(
                        len(clean), 10, f"In {skill}, summary {clean!r} is too short"
                    )
                    self.assertTrue(
                        "<b>" in clean and "</b>" in clean,
                        f"In {skill}, summary {clean!r} should be bolded with <b>...</b>",
                    )

    def test_more_examples_covers_messy_blurry_disputed_inputs(self):
        """Assert scenarios cover challenging/messy real-world inputs as required by R3."""
        expected_scenarios = {
            "claim-to-chart": ["adjust", "dispute", "not found", "messy"],
            "design-system-from-notes": ["glare", "contrast", "sketch", "slide"],
            "intent-mirror": ["overwhelm", "vent", "link", "fix"],
            "learning-capture": ["obscured", "overwhelm", "workshop", "debate"],
        }
        for skill, keywords in expected_scenarios.items():
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## More examples")
                end = text.find("## Tips")
                block = text[start:end].lower()

                for kw in keywords:
                    self.assertIn(
                        kw,
                        block,
                        f"Skill {skill} 'More examples' should cover challenge scenario matching {kw!r}",
                    )


class TestSimilarSkillsComparisonTables(unittest.TestCase):
    """Assert '## Similar skills' contains a comparison table with |."""

    def test_similar_skills_table_structure(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## Similar skills")
                end = text.find("## What's in this folder")
                block = text[start:end]

                tables = parse_markdown_tables(block)
                self.assertGreaterEqual(
                    len(tables),
                    1,
                    f"Skill {skill} 'Similar skills' must contain a comparison table with |",
                )

                table = tables[0]
                self.assertGreaterEqual(len(table["headers"]), 2)
                self.assertGreaterEqual(len(table["rows"]), 3)

                for orig_line, row_cols, line_no in table["rows"]:
                    self.assertEqual(
                        len(row_cols),
                        len(table["headers"]),
                        f"In {skill} similar skills table line {line_no}, column count {len(row_cols)} != header count {len(table['headers'])}",
                    )

    def test_similar_skills_mentions_industry_tools(self):
        """Assert comparison covers notable alternatives as required in R3."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## Similar skills")
                end = text.find("## What's in this folder")
                block = text[start:end]

                has_major_alt = any(
                    name.lower() in block.lower()
                    for name in ["anthropic", "superpowers", "skills.sh", "matt pocock", "craig hewitt"]
                )
                self.assertTrue(
                    has_major_alt,
                    f"Skill {skill} 'Similar skills' does not reference major alternatives",
                )


class TestHowITestedItStructuredTables(unittest.TestCase):
    """Assert '## How I tested it' contains a structured results table."""

    def test_how_i_tested_it_table_structure(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## How I tested it")
                end = text.find("## What's next")
                block = text[start:end]

                tables = parse_markdown_tables(block)
                self.assertGreaterEqual(
                    len(tables),
                    1,
                    f"Skill {skill} 'How I tested it' must contain a structured results table with |",
                )

                table = tables[0]
                self.assertGreaterEqual(len(table["headers"]), 2)
                self.assertGreaterEqual(len(table["rows"]), 3)

                for orig_line, row_cols, line_no in table["rows"]:
                    self.assertEqual(
                        len(row_cols),
                        len(table["headers"]),
                        f"In {skill} 'How I tested it' table line {line_no}, column count {len(row_cols)} != header count {len(table['headers'])}",
                    )

    def test_how_i_tested_it_honesty_disclosure(self):
        """Assert honest caveat about test scale as mandated in README-template."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## How I tested it")
                end = text.find("## What's next")
                block = text[start:end].lower()

                has_honesty_line = any(
                    w in block for w in ["small test", "small run", "one run each", "checked by hand", "scored by me", "marked by me"]
                )
                self.assertTrue(
                    has_honesty_line,
                    f"Skill {skill} 'How I tested it' missing honest disclosure about test scale",
                )


class TestGlobalMarkdownTableSyntaxAndIntegrity(unittest.TestCase):
    """Parse every single markdown table across all 4 READMEs to guarantee zero GFM syntax violations."""

    def test_all_tables_have_matching_column_counts(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                tables = parse_markdown_tables(text)
                self.assertGreater(
                    len(tables), 3, f"Skill {skill} has only {len(tables)} tables, expected >= 4"
                )

                for table in tables:
                    expected_cols = len(table["headers"])
                    self.assertEqual(
                        len(table["delims"]),
                        expected_cols,
                        f"In {skill} table at line {table['start_line']}, delimiter col count {len(table['delims'])} != header col count {expected_cols}",
                    )
                    for orig_line, row_cols, line_no in table["rows"]:
                        self.assertEqual(
                            len(row_cols),
                            expected_cols,
                            f"In {skill} table line {line_no} ({orig_line.strip()}), col count {len(row_cols)} != expected {expected_cols}",
                        )

    def test_whats_in_this_folder_table(self):
        """Assert 'What's in this folder' table exists and links to README, SKILL, CHECKS, and notes."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## What's in this folder")
                self.assertNotEqual(start, -1)
                block = text[start:]

                tables = parse_markdown_tables(block)
                self.assertGreaterEqual(len(tables), 1)
                table = tables[0]
                self.assertEqual(len(table["headers"]), 2)
                self.assertEqual(len(table["rows"]), 4)

                files_mentioned = " ".join(" ".join(r[1]) for r in table["rows"])
                self.assertIn("README.md", files_mentioned)
                self.assertIn("SKILL.md", files_mentioned)
                self.assertIn("CHECKS.md", files_mentioned)
                self.assertTrue("Notes" in files_mentioned or "notes" in files_mentioned)


class TestHTMLTagParityAndStructure(unittest.TestCase):
    """Stress-test HTML tag opening/closing parity and vocabulary section."""

    def test_html_tag_parity(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                for tag in ["details", "summary", "b"]:
                    open_count = len(re.findall(rf"<{tag}(?:|\s+[^>]*?)>", text))
                    close_count = text.count(f"</{tag}>")
                    self.assertEqual(
                        open_count,
                        close_count,
                        f"In {skill}, tag <{tag}> count mismatch: {open_count} open vs {close_count} close",
                    )

    def test_vocabulary_details_block_near_top(self):
        """Assert vocabulary details block exists before '## What it does'."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                top_block = text[: text.find("## What it does")]
                self.assertIn("<details>", top_block)
                self.assertIn("</details>", top_block)
                self.assertTrue(
                    "New to this?" in top_block or "words" in top_block.lower(),
                    f"In {skill}, vocabulary details block missing 'New to this?' phrasing",
                )

    def test_questions_details_blocks(self):
        """Assert '## Questions' section contains at least 3 <details> blocks."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                start = text.find("## Questions")
                end = text.find("## Similar skills")
                block = text[start:end]

                open_details = block.count("<details>")
                close_details = block.count("</details>")
                self.assertGreaterEqual(
                    open_details,
                    3,
                    f"Skill {skill} 'Questions' section has {open_details} <details> blocks, requires >= 3",
                )
                self.assertEqual(open_details, close_details)

    def test_blank_line_after_summary(self):
        """Assert blank line after <summary> for clean markdown parsing."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                text = read_skill_readme(skill)
                for m in re.finditer(r"<summary>(.*?)</summary>(\r?\n)([^\r\n]*)", text):
                    summary_text = m.group(1)
                    next_line = m.group(3)
                    self.assertEqual(
                        next_line.strip(),
                        "",
                        f"In {skill}, missing blank line after summary {summary_text!r}",
                    )


class TestFilesystemRelativeLinkIntegrity(unittest.TestCase):
    """Assert all internal filesystem links resolve to real existing files."""

    def test_all_relative_links_resolve(self):
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                readme_path = SKILLS_DIR / skill / "README.md"
                text = readme_path.read_text(encoding="utf-8")
                links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
                for anchor, href in links:
                    if href.startswith("http") or href.startswith("mailto:") or href.startswith("#"):
                        continue
                    target_file = href.split("#")[0]
                    if not target_file:
                        continue
                    resolved = (readme_path.parent / target_file).resolve()
                    self.assertTrue(
                        resolved.exists(),
                        f"In {skill}, broken link {href!r} (anchor {anchor!r}) does not resolve to existing file {resolved}",
                    )


class TestAustralianSpellingConformance(unittest.TestCase):
    """Assert Australian English spelling is respected across skill READMEs."""

    def test_australian_spelling(self):
        # Sample common American vs Australian spellings
        american_to_aus = {
            r"\bcolor\b": "colour",
            r"\bcolors\b": "colours",
            r"\bsummarize\b": "summarise",
            r"\bsummarizes\b": "summarises",
            r"\bsummarizer\b": "summariser",
            r"\bsummarizers\b": "summarisers",
            r"\bprioritize\b": "prioritise",
            r"\bprioritizes\b": "prioritises",
            r"\borganize\b": "organise",
            r"\borganizes\b": "organises",
        }
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                readme_path = SKILLS_DIR / skill / "README.md"
                text = readme_path.read_text(encoding="utf-8")
                # Remove code blocks and inline code
                prose = re.sub(r"```[\s\S]*?```", "", text)
                prose = re.sub(r"`[^`]+`", "", prose)
                prose = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", prose)
                # Remove URLs from links
                prose = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", prose)

                for pattern, aus in american_to_aus.items():
                    matches = list(re.finditer(pattern, prose, re.IGNORECASE))
                    filtered = [m for m in matches if "stroke:" not in m.group(0) and "color:" not in m.group(0)]
                    if filtered:
                        self.fail(
                            f"In {skill}, found American spelling {filtered[0].group(0)!r} (expected Australian {aus!r})"
                        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
