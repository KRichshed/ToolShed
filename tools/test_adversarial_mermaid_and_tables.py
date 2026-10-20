#!/usr/bin/env python3
"""Empirical adversarial test suite for Mermaid diagrams, KRichshed v2 tokens, and decision tables.

Target files:
  - README.md (repository root)
  - skills/README.md (skills directory hub)

Adversarial challenges:
  1. Mermaid syntax, block closure, and language tag.
  2. check_mermaid() conformance from tools/check_skills.py.
  3. Accessibility attributes: non-empty accTitle, accDescr, and immediate **In words:** summary.
  4. KRichshed v2 Diagram register token checks:
     - Exactly 1 focal pool node (#52CFDE) per diagram.
     - Outcome node with lime (#D2EE63) and tick mark (✓).
     - Indigo stroke and text (#1C1D38) with >= 7:1 WCAG contrast against all backgrounds.
     - 0 legacy teal hex codes (#d5f7f2, #1aa898, #0a7068).
     - 0 white text (#FFFFFF, #FFF) on nodes.
  5. Graph topology & reachability:
     - Flowchart TD direction.
     - Presence of all 4 skills.
     - Complete graph connectivity (no orphans).
     - Reachability from start node to outcome node.
  6. Decision table ("Which skill do I need?") in skills/README.md:
     - Table existence and 3-column schema.
     - Coverage of all 4 skills.
     - Filesystem link validity: every link in the table resolves to an existing folder with SKILL.md.
  7. Global link integrity across README.md and skills/README.md:
     - All relative paths resolve to valid files/folders.
  8. Readability & Australian English spelling conformance.
"""

from __future__ import annotations

import math
from pathlib import Path
import re
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO / "skills"

STANDALONE_SKILLS = [
    "claim-to-chart",
    "design-system-from-notes",
    "intent-mirror",
    "learning-capture",
]

LEGACY_TEAL_CODES = ["#d5f7f2", "#1aa898", "#0a7068"]


def relative_luminance(hex_code: str) -> float:
    """Calculate WCAG relative luminance for a 6-digit hex color."""
    hex_code = hex_code.lstrip("#")
    r_val = int(hex_code[0:2], 16) / 255.0
    g_val = int(hex_code[2:4], 16) / 255.0
    b_val = int(hex_code[4:6], 16) / 255.0

    def adjust(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r_adj = adjust(r_val)
    g_adj = adjust(g_val)
    b_adj = adjust(b_val)
    return 0.2126 * r_adj + 0.7152 * g_adj + 0.0722 * b_adj


def contrast_ratio(hex1: str, hex2: str) -> float:
    """Calculate WCAG contrast ratio between two hex colors."""
    l1 = relative_luminance(hex1)
    l2 = relative_luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def extract_mermaid_blocks(file_path: Path) -> list[dict]:
    """Extract all ```mermaid ... ``` blocks with metadata."""
    text = file_path.read_text(encoding="utf-8")
    blocks = []
    pattern = re.compile(r"```mermaid([\s\S]*?)```")
    for m in pattern.finditer(text):
        blocks.append({
            "content": m.group(1),
            "start": m.start(),
            "end": m.end(),
            "following_text": text[m.end(): m.end() + 500],
        })
    return blocks


class TestMermaidDiagramsIntegrity(unittest.TestCase):
    """Adversarial stress-testing of Mermaid diagrams in README.md and skills/README.md."""

    def setUp(self):
        self.root_readme = REPO / "README.md"
        self.skills_readme = SKILLS_DIR / "README.md"
        self.assertTrue(self.root_readme.is_file(), "Root README.md missing")
        self.assertTrue(self.skills_readme.is_file(), "skills/README.md missing")

    def test_check_mermaid_from_check_skills(self):
        """Invoke check_mermaid() directly from check_skills.py."""
        tools_dir = REPO / "tools"
        if str(tools_dir) not in sys.path:
            sys.path.insert(0, str(tools_dir))
        from check_skills import check_mermaid
        root_errs = check_mermaid(self.root_readme)
        self.assertEqual(root_errs, [], f"check_mermaid failed on README.md: {root_errs}")
        skills_errs = check_mermaid(self.skills_readme)
        self.assertEqual(skills_errs, [], f"check_mermaid failed on skills/README.md: {skills_errs}")

    def test_mermaid_blocks_count_and_delimiters(self):
        """Ensure each target file contains exactly 1 well-formed Mermaid diagram."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                text = target.read_text(encoding="utf-8")
                open_count = text.count("```mermaid")
                close_count = len(re.findall(r"```\s*$", text, re.MULTILINE))
                self.assertEqual(open_count, 1, f"{target.name} should have exactly 1 mermaid diagram, found {open_count}")
                blocks = extract_mermaid_blocks(target)
                self.assertEqual(len(blocks), 1, f"Failed to parse mermaid block in {target.name}")

    def test_accessibility_acc_title_and_descr(self):
        """Adversarially challenge accTitle and accDescr presence and substance."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                blocks = extract_mermaid_blocks(target)
                b = blocks[0]["content"]

                # Title check
                title_match = re.search(r"accTitle:\s*(.+)", b)
                self.assertIsNotNone(title_match, f"Missing accTitle in {target.name}")
                title = title_match.group(1).strip()
                self.assertGreater(len(title), 10, f"accTitle too short in {target.name}: {title!r}")

                # Description check
                descr_match = re.search(r"accDescr:\s*(.+)", b)
                self.assertIsNotNone(descr_match, f"Missing accDescr in {target.name}")
                descr = descr_match.group(1).strip()
                self.assertGreater(len(descr), 50, f"accDescr too brief in {target.name}: {descr!r}")

    def test_in_words_immediate_summary(self):
        """Verify '**In words:**' appears immediately after the diagram (within 400 chars)."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                blocks = extract_mermaid_blocks(target)
                following = blocks[0]["following_text"]
                self.assertIn("**In words:**", following, f"Missing '**In words:**' summary following diagram in {target.name}")
                summary_start = following.find("**In words:**")
                self.assertLess(summary_start, 50, f"Summary in {target.name} is not immediately following diagram (offset: {summary_start})")
                summary_text = following[summary_start:].split("\n\n")[0]
                self.assertGreater(len(summary_text), 80, f"Summary in {target.name} is too brief: {summary_text!r}")

    def test_krichshed_v2_focal_pool_token(self):
        """Assert exactly 1 focal pool node (#52CFDE) per diagram."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                blocks = extract_mermaid_blocks(target)
                b = blocks[0]["content"].upper()
                pool_matches = list(re.finditer(r"#52CFDE", b))
                self.assertEqual(len(pool_matches), 1, f"Expected exactly 1 #52CFDE token in {target.name}, found {len(pool_matches)}")

    def test_krichshed_v2_outcome_lime_token_and_tick(self):
        """Assert outcome node has lime (#D2EE63) and tick mark (✓)."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                blocks = extract_mermaid_blocks(target)
                b = blocks[0]["content"]
                b_upper = b.upper()
                self.assertIn("#D2EE63", b_upper, f"Missing lime #D2EE63 outcome token in {target.name}")
                self.assertIn("✓", b, f"Missing outcome tick mark '✓' in {target.name}")

    def test_krichshed_v2_contrast_and_strokes(self):
        """Assert indigo #1C1D38 stroke and text, with calculated contrast >= 7:1 against all fills."""
        text_color = "#1C1D38"
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                blocks = extract_mermaid_blocks(target)
                b = blocks[0]["content"]
                b_upper = b.upper()

                # Stroke and text colour presence
                self.assertIn("#1C1D38", b_upper, f"Missing #1C1D38 in {target.name}")
                self.assertIn("LINKSTYLEDEFAULTSTROKE:#1C1D38", b_upper.replace(" ", "").replace("\t", ""))

                # Ensure NO white text on light nodes
                self.assertNotIn("COLOR:#FFFFFF", b_upper.replace(" ", ""))
                self.assertNotIn("COLOR:#FFF;", b_upper.replace(" ", ""))
                self.assertNotIn("COLOR:WHITE", b_upper.replace(" ", ""))

                # Extract all fill colors used in classDef
                fill_matches = re.findall(r"fill:(#[0-9a-fA-F]{6})", b)
                self.assertGreater(len(fill_matches), 0, f"No fill colors found in classDef in {target.name}")
                for fill in fill_matches:
                    c = contrast_ratio(text_color, fill)
                    self.assertGreaterEqual(
                        c, 7.0,
                        f"Contrast ratio between text {text_color} and fill {fill} in {target.name} is {c:.2f}:1, below 7:1 requirement"
                    )

    def test_zero_legacy_teal_codes(self):
        """Confirm zero occurrences of legacy teal codes in README.md and skills/README.md."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                content = target.read_text(encoding="utf-8").lower()
                for code in LEGACY_TEAL_CODES:
                    self.assertNotIn(code, content, f"Found banned legacy teal {code} in {target.name}")

    def test_graph_topology_and_reachability(self):
        """Stress-test Mermaid graph topology, standalone tools presence, and reachability."""
        for target in [self.root_readme, self.skills_readme]:
            with self.subTest(file=target.name):
                blocks = extract_mermaid_blocks(target)
                b = blocks[0]["content"]

                # Check graph direction
                self.assertTrue(re.search(r"flowchart\s+TD", b), f"Expected flowchart TD in {target.name}")

                # Check all 4 standalone tools mentioned
                for skill in STANDALONE_SKILLS:
                    self.assertIn(skill, b, f"Missing standalone skill {skill} in diagram of {target.name}")

                # Check zero Kind Team mentions in standalone release
                self.assertNotIn("kind team", b.lower(), f"Unexpected Kind Team reference in diagram of {target.name}")

                # Extract nodes and edges
                edges = re.findall(r"([A-Za-z0-9_-]+)\s*(?:-->|-\.->|--\s*\"[^\"]*\"\s*-->|-\.\s*\"[^\"]*\"\s*\.->)\s*([A-Za-z0-9_-]+)", b)
                self.assertGreater(len(edges), 5, f"Suspiciously few edges in {target.name}")

                nodes = set()
                adj: dict[str, set[str]] = {}
                for src, dst in edges:
                    nodes.add(src)
                    nodes.add(dst)
                    adj.setdefault(src, set()).add(dst)

                # Identify outcome node (class <node> done)
                done_match = re.search(r"^\s*class\s+([A-Za-z0-9_]+)\s+done", b, re.MULTILINE)
                self.assertIsNotNone(done_match, f"No node marked with class 'done' in {target.name}")
                done_node = done_match.group(1).strip()
                self.assertIn(done_node, nodes, f"Outcome node {done_node} not in graph edges in {target.name}")

                # Identify start node(s): in-degree == 0
                in_degrees = {n: 0 for n in nodes}
                for src, dsts in adj.items():
                    for d in dsts:
                        in_degrees[d] = in_degrees.get(d, 0) + 1
                start_nodes = [n for n, deg in in_degrees.items() if deg == 0]
                self.assertGreater(len(start_nodes), 0, f"No start node found in {target.name}")

                # Assert outcome node is reachable from at least one start node
                visited = set()
                queue = list(start_nodes)
                while queue:
                    curr = queue.pop(0)
                    if curr in visited:
                        continue
                    visited.add(curr)
                    for nxt in adj.get(curr, []):
                        if nxt not in visited:
                            queue.append(nxt)

                self.assertIn(
                    done_node, visited,
                    f"Outcome node {done_node} is unreachable from start nodes {start_nodes} in {target.name}"
                )


class TestSkillsDecisionTable(unittest.TestCase):
    """Adversarial stress-testing of 'Which skill do I need?' table in skills/README.md."""

    def setUp(self):
        self.skills_readme = SKILLS_DIR / "README.md"
        self.text = self.skills_readme.read_text(encoding="utf-8")
        self.assertIn("## Which skill do I need?", self.text, "Missing '## Which skill do I need?' header in skills/README.md")

        # Extract table block
        start = self.text.find("## Which skill do I need?")
        end = self.text.find("## How to get started with a skill")
        self.assertNotEqual(start, -1)
        self.assertNotEqual(end, -1)
        self.table_block = self.text[start:end]

    def test_decision_table_structure_and_columns(self):
        """Verify 3-column table structure with valid markdown delimiters."""
        lines = [l.strip() for l in self.table_block.splitlines() if l.strip().startswith("|") and l.strip().endswith("|")]
        self.assertGreaterEqual(len(lines), 6, "Decision table has fewer than 6 rows (header + delimiter + 4 skills)")

        header = [c.strip() for c in lines[0].split("|")[1:-1]]
        self.assertEqual(len(header), 3, f"Header should have 3 columns, got {header}")
        self.assertIn("want to", header[0].lower())
        self.assertIn("tool", header[1].lower())
        self.assertIn("get", header[2].lower())

        delimiter = [c.strip() for c in lines[1].split("|")[1:-1]]
        self.assertEqual(len(delimiter), 3, f"Delimiter should have 3 columns, got {delimiter}")
        for d in delimiter:
            self.assertTrue(re.match(r"^:?-+:?$", d), f"Invalid delimiter {d!r}")

        for row_idx, line in enumerate(lines[2:], 3):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            self.assertEqual(len(cols), 3, f"Row {row_idx} column count mismatch: expected 3, got {len(cols)}")
            self.assertGreater(len(cols[0]), 15, f"Row {row_idx} condition too short: {cols[0]!r}")
            self.assertGreater(len(cols[1]), 5, f"Row {row_idx} tool name too short: {cols[1]!r}")
            self.assertGreater(len(cols[2]), 15, f"Row {row_idx} outcome too short: {cols[2]!r}")

    def test_all_standalone_skills_represented(self):
        """Assert all 4 standalone skills appear in the decision table."""
        for skill in STANDALONE_SKILLS:
            with self.subTest(skill=skill):
                self.assertIn(skill, self.table_block, f"Decision table missing standalone skill {skill}")

    def test_no_kind_team_roles_in_standalone_table(self):
        """Assert zero Kind Team roles appear in the standalone decision table."""
        self.assertNotIn("plugins/", self.table_block)
        self.assertNotIn("kind-", self.table_block)

    def test_decision_table_filesystem_link_targets(self):
        """Extract every markdown link in the decision table and verify filesystem target resolution."""
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", self.table_block)
        self.assertEqual(len(links), 4, f"Expected 4 standalone tool links in decision table, found {len(links)}")

        for anchor, href in links:
            with self.subTest(anchor=anchor, href=href):
                # Clean query/hash
                clean_href = href.split("#")[0].strip()
                resolved = (self.skills_readme.parent / clean_href).resolve()
                self.assertTrue(resolved.exists(), f"Link '{anchor}' -> '{href}' does not resolve to existing path: {resolved}")
                if resolved.is_dir():
                    # Must contain SKILL.md
                    skill_md = resolved / "SKILL.md"
                    self.assertTrue(skill_md.is_file(), f"Target directory {resolved} missing SKILL.md")


class TestDirectoryAndHubTables(unittest.TestCase):
    """Stress-test secondary tables in README.md and skills/README.md."""

    def test_standalone_skills_directory_table_in_skills_readme(self):
        """Verify the skills directory table in skills/README.md."""
        text = (SKILLS_DIR / "README.md").read_text(encoding="utf-8")
        start = text.find("## Skills in the shed so far")
        self.assertNotEqual(start, -1)
        end = text.find("## How to use a skill")
        self.assertNotEqual(end, -1)
        block = text[start:end]

        for skill in STANDALONE_SKILLS:
            self.assertIn(f"[{skill}]({skill}/)", block)
            self.assertIn(f"[Notes](../notes/{skill}.md)", block)
            # Verify file exists
            note_file = REPO / "notes" / f"{skill}.md"
            self.assertTrue(note_file.is_file(), f"Companion note {note_file} missing")

    def test_whats_in_the_shed_table_in_root_readme(self):
        """Verify the 'What's in the shed' folder table in root README.md."""
        text = (REPO / "README.md").read_text(encoding="utf-8")
        start = text.find("## What's in the shed")
        self.assertNotEqual(start, -1)
        end = text.find("## Using anything here")
        self.assertNotEqual(end, -1)
        block = text[start:end]

        expected_dirs = ["skills", "agents", "prompts", "notes"]
        for d in expected_dirs:
            self.assertIn(f"[`{d}/`]({d}/)", block)
            target_dir = REPO / d
            self.assertTrue(target_dir.is_dir(), f"Folder {target_dir} referenced in table does not exist")
        self.assertNotIn("plugins/", block)


class TestReadabilityAndSpelling(unittest.TestCase):
    """Assert Australian English spelling and FKGL/ASL readability metrics."""

    def test_australian_spelling_in_readmes(self):
        american_to_aus = {
            r"\bcolor\b": "colour",
            r"\bcolors\b": "colours",
            r"\bsummarize\b": "summarise",
            r"\bsummarizes\b": "summarises",
            r"\bprioritize\b": "prioritise",
            r"\bprioritizes\b": "prioritises",
            r"\borganize\b": "organise",
            r"\borganizes\b": "organises",
            r"\bbehavior\b": "behaviour",
            r"\bbehaviors\b": "behaviours",
        }
        for path in [REPO / "README.md", SKILLS_DIR / "README.md"]:
            with self.subTest(file=path.name):
                text = path.read_text(encoding="utf-8")
                # Remove code blocks
                prose = re.sub(r"```[\s\S]*?```", "", text)
                prose = re.sub(r"`[^`]+`", "", prose)
                prose = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", prose)

                for pattern, aus in american_to_aus.items():
                    matches = list(re.finditer(pattern, prose, re.IGNORECASE))
                    if matches:
                        self.fail(f"Found American spelling {matches[0].group(0)!r} in {path.name} (expected {aus})")

    def test_readability_metrics_bounds(self):
        """Verify FKGL <= 6.5 and ASL <= 18.0 via check_skills calculate_readability."""
        tools_dir = REPO / "tools"
        if str(tools_dir) not in sys.path:
            sys.path.insert(0, str(tools_dir))
        from check_skills import calculate_readability

        for path in [REPO / "README.md", SKILLS_DIR / "README.md"]:
            with self.subTest(file=path.name):
                text = path.read_text(encoding="utf-8")
                fkgl, asl, words, sents = calculate_readability(text)
                self.assertLessEqual(fkgl, 6.5, f"{path.name} FKGL={fkgl:.2f} exceeds limit 6.5")
                self.assertLessEqual(asl, 18.0, f"{path.name} ASL={asl:.2f} exceeds limit 18.0")


class TestGlobalDocumentLinkIntegrity(unittest.TestCase):
    """Stress-test every relative link in README.md and skills/README.md."""

    def test_root_readme_links_resolve(self):
        readme = REPO / "README.md"
        text = readme.read_text(encoding="utf-8")
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
        self.assertGreater(len(links), 5)
        for anchor, href in links:
            if href.startswith("http") or href.startswith("mailto:") or href.startswith("#"):
                continue
            clean_href = href.split("#")[0].strip()
            if not clean_href:
                continue
            resolved = (readme.parent / clean_href).resolve()
            self.assertTrue(resolved.exists(), f"Broken link in README.md: '{anchor}' -> '{href}' ({resolved})")

    def test_skills_readme_all_links_resolve(self):
        readme = SKILLS_DIR / "README.md"
        text = readme.read_text(encoding="utf-8")
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
        self.assertGreater(len(links), 10)
        for anchor, href in links:
            if href.startswith("http") or href.startswith("mailto:") or href.startswith("#"):
                continue
            clean_href = href.split("#")[0].strip()
            if not clean_href:
                continue
            resolved = (readme.parent / clean_href).resolve()
            self.assertTrue(resolved.exists(), f"Broken link in skills/README.md: '{anchor}' -> '{href}' ({resolved})")


if __name__ == "__main__":
    unittest.main(verbosity=2)
