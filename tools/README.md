# Verification Tools

Automated checks that keep ToolShed's skills, SVG cards, and newcomer guides honest, readable, and accessible.

## Running the checks

Run the main checker from the repository root:

```bash
python3 tools/check_skills.py
```

Run the companion test suites:

```bash
python3 -m unittest discover -s tools -p "test_*.py" -v
```

## What `check_skills.py` checks

1. **Skill frontmatter & boundaries:** Every `skills/*/SKILL.md` file has valid frontmatter, Level 1 Operator autonomy boundaries, and required sections.
2. **Readability:** Every README, glossary, contributing guide, changelog, companion note, and doc in `docs/` measures at or below Flesch-Kincaid Grade 6.5.
3. **KRichshed v2 design tokens & contrast:** Every SVG card and Mermaid diagram uses approved KRichshed v2 colours with text contrast at or above 4.5:1, `<title>` and `<desc>` tags, `role="img"`, and zero clipped text.
4. **Honest labels & Australian spelling:** Every SVG card with sample numbers or quotes displays an `EXAMPLE` badge, uses Australian spelling, and contains zero banned words, zero personal paths, and zero unreleased role references.
