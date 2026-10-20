#!/usr/bin/env python3
"""Check standalone skills against KRichshed v2 standards, accessibility, and readability.

Usage:
  python3 tools/check_skills.py             # verify all standalone skills and READMEs
  python3 tools/check_skills.py <skill>     # verify single skill (e.g. claim-to-chart)
  python3 tools/check_skills.py --verbose   # print detailed readability metrics

Exit code 0 means all checks passed. Exit code 1 means one or more checks failed.
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path
import re
import sys
from typing import Dict, List, Tuple

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is needed: pip install pyyaml")

REPO = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO / "skills"
NOTES_DIR = REPO / "notes"
STANDALONE_SKILLS = ["claim-to-chart", "design-system-from-notes", "intent-mirror", "learning-capture"]

EXPECTED_SVG_ASSETS = {
    "claim-to-chart": "assets/example-chart.svg",
    "design-system-from-notes": "assets/example-specimen.svg",
    "intent-mirror": "assets/example-mirror.svg",
    "learning-capture": "assets/example-map.svg",
}

LEGACY_TEAL_CODES = ["#d5f7f2", "#1aa898", "#0a7068"]
KRICHSHED_V2_REGISTER = [
    "#FBF7EC", "#1C1D38", "#52CFDE", "#D2EE63", "#848499", "#FF8F5E", "#9E0147",
    "#31AE7C", "#091831", "#171B16",
]

BANNED_WORDS_PATTERN = re.compile(
    r"\b(compliant|guaranteed|on track|synthesized|standalone skill|standalone skills|four standalone|Co-Authored-By|Generated with|kind-team|kind team|kind workforce|kind-chief-of-staff|kind-product-manager|kind-content-designer|kind-qa-tester|kind-accessibility-specialist|kind-delivery-manager|kind-red-team|kind-security-specialist|kind-ux-designer|kind-ui-designer|kind-motion-designer|kind-marketing-comms|kind-learning-log)\b|/Users/kimberly|plugins/kind-team|\.claude-plugin",
    re.IGNORECASE,
)

AMERICAN_TO_AUS = {
    r"\bcolor\b": "colour",
    r"\bcolors\b": "colours",
    r"\bsummarize\b": "summarise",
    r"\bsummarizes\b": "summarises",
    r"\bsummarizer\b": "summariser",
    r"\bsummarizers\b": "summarisers",
    r"\bsummarized\b": "summarised",
    r"\bsummarizing\b": "summarising",
    r"\bprioritize\b": "prioritise",
    r"\bprioritizes\b": "prioritises",
    r"\bprioritized\b": "prioritised",
    r"\bprioritizing\b": "prioritising",
    r"\borganize\b": "organise",
    r"\borganizes\b": "organises",
    r"\borganized\b": "organised",
    r"\borganizing\b": "organising",
    r"\bbehavior\b": "behaviour",
    r"\bbehaviors\b": "behaviours",
    r"\banalyze\b": "analyse",
    r"\banalyzes\b": "analyses",
    r"\banalyzed\b": "analysed",
    r"\banalyzing\b": "analysing",
}


def count_syllables(word: str) -> int:
    """Estimate syllable count for a word using vowel-group heuristics."""
    word = word.lower().strip()
    if not word:
        return 0
    clean = re.sub(r"[^a-z]", "", word)
    if not clean:
        return 0
    if len(clean) <= 3:
        return 1
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for char in clean:
        is_vowel = char in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if clean.endswith("e") and not clean.endswith("le") and count > 1:
        count -= 1
    if clean.endswith("ed") and not clean.endswith("ted") and not clean.endswith("ded") and count > 1:
        count -= 1
    return max(1, count)


def extract_prose(text: str) -> str:
    """Extract readable prose from markdown, stripping code, tables, and markup."""
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove HTML tags, keep text inside
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove images
    text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", text)
    # Remove markdown link URLs, keep anchor text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Remove markdown tables
    lines = []
    for line in text.splitlines():
        trimmed = line.strip()
        if trimmed.startswith("|") and trimmed.endswith("|"):
            continue
        lines.append(line)
    return "\n".join(lines)


def calculate_readability(text: str) -> Tuple[float, float, int, int]:
    """Calculate Flesch-Kincaid Grade Level (FKGL) and Average Sentence Length (ASL)."""
    prose = extract_prose(text)
    cleaned = re.sub(r"\b(e\.g\.|i\.e\.|vs\.|v2\.)", lambda m: m.group(0).replace(".", "@"), prose)
    raw_sentences = [s.strip() for s in re.split(r"[.!?]+(?:\s+|\n+|$)", cleaned) if s.strip()]

    total_words = 0
    total_syllables = 0
    valid_sentences = 0

    for s in raw_sentences:
        s = s.replace("@", ".")
        words = [w for w in re.findall(r"\b[a-zA-Z]+\b", s) if w]
        if not words:
            continue
        valid_sentences += 1
        total_words += len(words)
        for w in words:
            total_syllables += count_syllables(w)

    if valid_sentences == 0 or total_words == 0:
        return 0.0, 0.0, 0, 0

    asl = total_words / valid_sentences
    asw = total_syllables / total_words
    fkgl = 0.39 * asl + 11.8 * asw - 15.59
    return fkgl, asl, total_words, valid_sentences


def check_skill_frontmatter(skill_name: str) -> List[str]:
    """Verify 6-field YAML frontmatter and Handoffs section in SKILL.md."""
    errors = []
    skill_file = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_file.is_file():
        return [f"missing SKILL.md in skills/{skill_name}"]

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ["SKILL.md frontmatter must start with --- on line 1"]
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ["SKILL.md frontmatter block not properly closed with ---"]

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return [f"SKILL.md frontmatter YAML error: {exc}"]

    # 6 standard fields verification
    if fm.get("name") != skill_name:
        errors.append(f"frontmatter 'name' is {fm.get('name')!r}, expected {skill_name!r}")
    desc = str(fm.get("description", "")).strip()
    if not desc:
        errors.append("frontmatter 'description' is empty")
    elif len(desc) > 1024:
        errors.append(f"frontmatter 'description' length ({len(desc)}) exceeds 1024 chars")
    if fm.get("license") != "MIT":
        errors.append(f"frontmatter 'license' must be 'MIT', got {fm.get('license')!r}")

    meta = fm.get("metadata")
    if not isinstance(meta, dict):
        errors.append("frontmatter 'metadata' must be a dictionary")
    else:
        if meta.get("author") != "KRichshed":
            errors.append(f"metadata 'author' must be 'KRichshed', got {meta.get('author')!r}")
        version = str(meta.get("version", ""))
        if not re.match(r"^\d+\.\d+\.\d+$", version):
            errors.append(f"metadata 'version' must be valid semver (e.g. 0.2.0), got {version!r}")
        autonomy = str(meta.get("autonomy", ""))
        if "Level 1 Operator" not in autonomy:
            errors.append(f"metadata 'autonomy' must state Level 1 Operator boundaries, got {autonomy!r}")

    # Body handoffs check
    body = parts[2]
    if not re.search(r"#+\s*Handoffs", body) and "Handoffs" not in body:
        errors.append("SKILL.md missing 'Handoffs' section or table")

    return errors


def check_skill_readme(skill_name: str) -> List[str]:
    """Verify README.md structure, worked example, details, assets, and notes link."""
    errors = []
    readme_path = SKILLS_DIR / skill_name / "README.md"
    if not readme_path.is_file():
        return [f"missing README.md in skills/{skill_name}"]

    text = readme_path.read_text(encoding="utf-8")

    # Required template sections
    required_sections = [
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
    for sec in required_sections:
        if sec not in text:
            errors.append(f"README.md missing section: {sec!r}")

    # Check for worked example section
    has_worked_example = any(h in text for h in [
        "## What you'll get back",
        "## What the mirror looks like",
        "## What the verdict and chart look like",
        "## What the mini design system looks like",
    ])
    if not has_worked_example:
        errors.append("README.md missing worked example section (e.g. '## What you'll get back')")
    else:
        worked_found = False
        for h in [
            "## What you'll get back",
            "## What the mirror looks like",
            "## What the verdict and chart look like",
            "## What the mini design system looks like",
        ]:
            if h in text:
                m = re.search(rf"{re.escape(h)}([\s\S]*?)(?:\n##\s+|$)", text)
                if m and "|" in m.group(1):
                    worked_found = True
                    break
        if not worked_found:
            errors.append("README.md worked example section must include an explanation table")

    # Check for details examples under More examples
    more_examples_match = re.search(r"## More examples([\s\S]*?)## Tips", text)
    if more_examples_match:
        examples_block = more_examples_match.group(1)
        details_count = examples_block.count("<details>")
        if details_count < 3:
            errors.append(f"README.md 'More examples' has {details_count} <details> examples, requires at least 3")
    else:
        errors.append("could not parse 'More examples' section between '## More examples' and '## Tips'")

    # Check for similar skills comparison table
    similar_match = re.search(r"## Similar skills([\s\S]*?)## What's in this folder", text)
    if similar_match:
        similar_block = similar_match.group(1)
        if "|" not in similar_block:
            errors.append("README.md 'Similar skills' section must include a comparison table")
    else:
        errors.append("could not parse 'Similar skills' section")

    # Check SVG asset existence and embedding
    expected_svg = EXPECTED_SVG_ASSETS.get(skill_name)
    if expected_svg:
        svg_path = SKILLS_DIR / skill_name / expected_svg
        if not svg_path.is_file():
            errors.append(f"missing visual asset: skills/{skill_name}/{expected_svg}")
        else:
            svg_content = svg_path.read_text(encoding="utf-8")
            if "<svg" not in svg_content or "</svg>" not in svg_content:
                errors.append(f"visual asset {expected_svg} is not valid SVG XML")
            has_numbers = bool(re.search(r"\d", svg_content))
            has_quotes = bool(re.search(r'["“”\'‘’]|&quot;|&apos;', svg_content))
            if (has_numbers or has_quotes) and "EXAMPLE" not in svg_content:
                errors.append(f"visual asset {expected_svg} contains numbers or quotes but is missing required 'EXAMPLE' label")
        # Check embed in README
        svg_filename = Path(expected_svg).name
        embed_match = re.search(rf"!\[([^\]]*)\]\([^)]*{re.escape(svg_filename)}[^)]*\)", text)
        if not embed_match:
            img_match = re.search(rf'<img[^>]+src="[^"]*{re.escape(svg_filename)}"[^>]*alt="([^"]+)"', text)
            if not img_match:
                errors.append(f"README.md does not embed visual asset {expected_svg}")
            else:
                alt_text = img_match.group(1).strip()
                if len(alt_text) <= 10:
                    errors.append(f"README.md SVG embed has insufficient alt text (<= 10 chars): {alt_text!r}")
        else:
            alt_text = embed_match.group(1).strip()
            if len(alt_text) <= 10:
                errors.append(f"README.md SVG embed has insufficient alt text (<= 10 chars): {alt_text!r}")

    # Check companion notes link
    note_link_pattern = rf"\[.*?\]\((?:\.\./\.\./)?notes/{re.escape(skill_name)}\.md(?:#[^\)]*)?\)"
    if not re.search(note_link_pattern, text):
        errors.append(f"README.md does not link to companion note 'notes/{skill_name}.md'")

    return errors


def check_mermaid(file_path: Path) -> List[str]:
    """Verify Mermaid diagrams satisfy accessibility and KRichshed v2 styling rules."""
    errors = []
    text = file_path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"```mermaid([\s\S]*?)```", text))
    if not matches:
        return []

    for i, match in enumerate(matches, 1):
        b = match.group(1)
        end_pos = match.end()

        if "accTitle:" not in b:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} missing 'accTitle:'")
        if "accDescr:" not in b:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} missing 'accDescr:'")

        # In words check
        following_text = text[end_pos : end_pos + 400]
        if "**In words:**" not in following_text:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} missing following '**In words:**' summary")

        # Colour registers and nodes
        b_upper = b.upper()
        pool_count = b_upper.count("#52CFDE")
        if pool_count != 1:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} must have exactly 1 focal node with pool #52CFDE (found {pool_count})")
        if "#D2EE63" not in b_upper:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} missing outcome node with lime #D2EE63")
        if "✓" not in b:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} missing outcome tick mark '✓'")

        # Text colour and contrast: #1C1D38 required for >= 7:1 contrast
        if "#1C1D38" not in b_upper:
            errors.append(f"Mermaid diagram #{i} in {file_path.name} missing text/stroke colour #1C1D38 (required for >= 7:1 contrast)")
        if "COLOR:#FFFFFF" in b_upper.replace(" ", "") or "COLOR:#FFF" in b_upper.replace(" ", ""):
            errors.append(f"Mermaid diagram #{i} in {file_path.name} contains white text (must use #1C1D38 for >= 7:1 contrast)")

    return errors


def check_no_legacy_teal() -> List[str]:
    """Scan all markdown files in skills/ for banned legacy teal hex codes."""
    errors = []
    for md in sorted(SKILLS_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            line_lower = line.lower()
            for code in LEGACY_TEAL_CODES:
                if code in line_lower:
                    errors.append(f"legacy teal code {code} found in {md.relative_to(REPO)}:{line_no}")
    return errors


def check_notes() -> List[str]:
    """Verify companion notes existence and bidirectional link integrity."""
    errors = []
    readme = NOTES_DIR / "README.md"
    if not readme.is_file():
        errors.append("missing notes/README.md")
    else:
        text = readme.read_text(encoding="utf-8")
        for s in STANDALONE_SKILLS:
            if f"{s}.md" not in text:
                errors.append(f"notes/README.md missing link to {s}.md")

    for s in STANDALONE_SKILLS:
        note_file = NOTES_DIR / f"{s}.md"
        if not note_file.is_file():
            errors.append(f"missing companion note: notes/{s}.md")
        else:
            c = note_file.read_text(encoding="utf-8")
            if f"skills/{s}/SKILL.md" not in c and f"skills/{s}" not in c:
                errors.append(f"notes/{s}.md does not link to its skill: skills/{s}/SKILL.md")
    return errors


def check_banned_terms(skill_name: str | None = None) -> List[str]:
    """Scan markdown prose and SVG text for banned terms."""
    errors = []
    targets: List[Path] = []
    if skill_name:
        targets.extend(SKILLS_DIR.glob(f"{skill_name}/**/*.md"))
        targets.extend(SKILLS_DIR.glob(f"{skill_name}/**/*.svg"))
    else:
        for r_file in ["README.md", "CONTRIBUTING.md", "GLOSSARY.md", "CHANGELOG.md"]:
            p = REPO / r_file
            if p.is_file():
                targets.append(p)
        targets.extend(SKILLS_DIR.glob("**/*.md"))
        targets.extend(SKILLS_DIR.glob("**/*.svg"))
        targets.extend(NOTES_DIR.glob("*.md"))
        docs_dir = REPO / "docs"
        if docs_dir.is_dir():
            targets.extend(docs_dir.glob("**/*.md"))
        for extra_dir in ["agents", "prompts"]:
            ed = REPO / extra_dir
            if ed.is_dir():
                targets.extend(ed.glob("**/*.md"))
        assets_dir = REPO / "assets"
        if assets_dir.is_dir():
            targets.extend(assets_dir.glob("**/*.svg"))

    for target in targets:
        if not target.is_file():
            continue
        text = target.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            m = BANNED_WORDS_PATTERN.search(line)
            if m:
                errors.append(f"banned word {m.group(0)!r} found in {target.relative_to(REPO)}:{line_no}")
    return errors


def check_australian_spelling(file_path: Path) -> List[str]:
    """Scan prose in markdown file for American spellings."""
    errors = []
    if not file_path.is_file():
        return []
    text = file_path.read_text(encoding="utf-8")
    prose = re.sub(r"```[\s\S]*?```", "", text)
    prose = re.sub(r"`[^`]+`", "", prose)
    prose = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", prose)
    prose = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", prose)
    prose = re.sub(r"<[^>]+>", " ", prose)

    for pattern, aus in AMERICAN_TO_AUS.items():
        for m in re.finditer(pattern, prose, re.IGNORECASE):
            errors.append(f"American spelling {m.group(0)!r} found in {file_path.relative_to(REPO)} (expected {aus!r})")
    return errors


def relative_luminance(hex_code: str) -> float:
    """Calculate WCAG relative luminance for a 3-digit or 6-digit hex color."""
    hex_code = hex_code.lstrip("#")
    if len(hex_code) == 3:
        hex_code = "".join(c * 2 for c in hex_code)
    r_val = int(hex_code[0:2], 16) / 255.0
    g_val = int(hex_code[2:4], 16) / 255.0
    b_val = int(hex_code[4:6], 16) / 255.0

    def adjust(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * adjust(r_val) + 0.7152 * adjust(g_val) + 0.0722 * adjust(b_val)


def contrast_ratio(hex1: str, hex2: str) -> float:
    """Calculate WCAG contrast ratio between two hex colors."""
    l1 = relative_luminance(hex1)
    l2 = relative_luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def check_social_preview() -> List[str]:
    """Verify assets/social-preview.svg dimensions, KRichshed v2 colours, contrast >= 4.5:1, text boundaries [40, 1240], and a11y tags."""
    errors = []
    svg_path = REPO / "assets" / "social-preview.svg"
    if not svg_path.is_file():
        return ["missing assets/social-preview.svg"]

    content = svg_path.read_text(encoding="utf-8")

    # Dimensions check
    if 'width="1280"' not in content or 'height="640"' not in content or 'viewBox="0 0 1280 640"' not in content:
        errors.append("assets/social-preview.svg missing required dimensions (width=1280, height=640, viewBox='0 0 1280 640')")

    # Accessibility tags: role="img", aria-labelledby, title, desc
    if 'role="img"' not in content:
        errors.append("assets/social-preview.svg missing role='img'")
    if 'aria-labelledby=' not in content:
        errors.append("assets/social-preview.svg missing aria-labelledby attribute")
    if not re.search(r'<title\s+id=["\']title["\']>[^<]+</title>', content):
        errors.append("assets/social-preview.svg missing <title id='title'> tag with content")
    if not re.search(r'<desc\s+id=["\']desc["\']>[^<]+</desc>', content):
        errors.append("assets/social-preview.svg missing <desc id='desc'> tag with content")

    # Colours: All hex codes must belong to KRichshed v2 register and no legacy teals
    krichshed_v2_upper = [c.upper() for c in KRICHSHED_V2_REGISTER]
    hex_colors = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', content)
    for h in hex_colors:
        full_hex = f"#{h.upper()}"
        if full_hex.lower() in [tc.lower() for tc in LEGACY_TEAL_CODES]:
            errors.append(f"assets/social-preview.svg contains legacy teal colour: {full_hex}")
        if full_hex not in krichshed_v2_upper and full_hex != "#FFFFFF":
            errors.append(f"assets/social-preview.svg colour {full_hex} is outside KRichshed v2 register")

    # Text boundaries [40, 1240]
    for m in re.finditer(r"<text\s+([^>]*?)>(.*?)</text>", content, re.DOTALL):
        attrs, text = m.group(1), m.group(2).strip()
        text_clean = html.unescape(re.sub(r"<[^>]+>", "", text))
        xm = re.search(r'x=["\']([\d\.]+)["\']', attrs)
        fsm = re.search(r'font-size=["\']([\d\.]+)["\']', attrs)
        anchor_m = re.search(r'text-anchor=["\'](\w+)["\']', attrs)
        letter_spacing_m = re.search(r'letter-spacing=["\']([\d\.]+)["\']', attrs)
        ls = float(letter_spacing_m.group(1)) if letter_spacing_m else 0.0

        if xm and fsm:
            x = float(xm.group(1))
            fs = float(fsm.group(1))
            anchor = anchor_m.group(1) if anchor_m else "start"
            est_w = len(text_clean) * (fs * 0.55 + ls)
            if anchor == "middle":
                left_x = x - est_w / 2
                right_x = x + est_w / 2
            elif anchor == "end":
                left_x = x - est_w
                right_x = x
            else:
                left_x = x
                right_x = x + est_w
            if left_x < 40 or right_x > 1240:
                errors.append(f"assets/social-preview.svg: text {text_clean[:30]!r}... overflows bounds [40, 1240] (left={left_x:.1f}, right={right_x:.1f})")

    # Contrast ratio >= 4.5:1
    rects = []
    for m in re.finditer(r"<rect\s+([^>]*?)/?>", content):
        attrs = m.group(1)
        fill_m = re.search(r'fill=["\'](#?[A-Za-z0-9]+)["\']', attrs)
        fill = fill_m.group(1) if fill_m else "#000000"
        if fill.lower() in ("none", "transparent"):
            continue
        rx = float(re.search(r'x=["\']([\d\.]+)["\']', attrs).group(1)) if "x=" in attrs else 0.0
        ry = float(re.search(r'y=["\']([\d\.]+)["\']', attrs).group(1)) if "y=" in attrs else 0.0
        rw = float(re.search(r'width=["\']([\d\.]+)["\']', attrs).group(1)) if "width=" in attrs else 1280.0
        rh = float(re.search(r'height=["\']([\d\.]+)["\']', attrs).group(1)) if "height=" in attrs else 640.0
        rects.append((rx, ry, rw, rh, fill))

    for m in re.finditer(r"<text\s+([^>]*?)>(.*?)</text>", content, re.DOTALL):
        attrs, text = m.group(1), m.group(2).strip()
        text_clean = html.unescape(re.sub(r"<[^>]+>", "", text)).strip()
        xm = re.search(r'x=["\']([\d\.]+)["\']', attrs)
        ym = re.search(r'y=["\']([\d\.]+)["\']', attrs)
        fill_m = re.search(r'fill=["\'](#?[A-Za-z0-9]+)["\']', attrs)
        if not xm or not ym or not fill_m:
            continue
        tx = float(xm.group(1))
        ty = float(ym.group(1))
        tfill = fill_m.group(1)

        if 'class="hand"' in attrs and tfill.upper() == "#FF8F5E":
            continue
        enclosing_fill = None
        min_area = float("inf")
        for rx, ry, rw, rh, rfill in rects:
            if rx <= tx <= rx + rw and ry <= ty <= ry + rh:
                area = rw * rh
                if area <= min_area:
                    min_area = area
                    enclosing_fill = rfill
        bg_fill = enclosing_fill if enclosing_fill else "#FBF7EC"
        ratio = contrast_ratio(tfill, bg_fill)
        if ratio < 4.5:
            errors.append(f"assets/social-preview.svg: text {text_clean[:25]!r} (fill {tfill}) on background {bg_fill} has contrast ratio {ratio:.2f}:1 (< 4.5:1)")

    return errors


def check_svg_boundaries() -> Tuple[List[str], str]:
    """Report status of rendering check and flag heuristic coordinate overflow."""
    errors = []
    status_msg = "SVG text boundaries (pixel rendering): not run by tool (headless rendering engine not installed)"

    for skill, svg_rel in EXPECTED_SVG_ASSETS.items():
        svg_file = SKILLS_DIR / skill / svg_rel
        if not svg_file.is_file():
            continue
        content = svg_file.read_text(encoding="utf-8")
        for m in re.finditer(r"<text\s+([^>]*?)>(.*?)</text>", content, re.DOTALL):
            attrs, text = m.group(1), m.group(2).strip()
            text_clean = html.unescape(re.sub(r"<[^>]+>", "", text))
            xm = re.search(r'x=["\'](\d+)["\']', attrs)
            fsm = re.search(r'font-size=["\']([\d\.]+)["\']', attrs)
            anchor_m = re.search(r'text-anchor=["\'](\w+)["\']', attrs)
            if xm and fsm:
                x = float(xm.group(1))
                fs = float(fsm.group(1))
                anchor = anchor_m.group(1) if anchor_m else "start"
                est_w = len(text_clean) * fs * 0.55
                if anchor == "middle":
                    right_x = x + est_w / 2
                elif anchor == "end":
                    right_x = x
                else:
                    right_x = x + est_w
                if right_x > 780:
                    errors.append(f"{svg_file.relative_to(REPO)}: text {text_clean[:30]!r}... likely clips outside card boundary (x={x}, est_end={right_x:.0f} > 780)")

    return errors, status_msg


def check_front_door(require: bool = False) -> Tuple[List[str], str]:
    """Verify repository front-door files and newcomer sections (R4)."""
    errors = []
    front_door_files = ["CONTRIBUTING.md", "GLOSSARY.md", "CHANGELOG.md"]
    existing_files = [f for f in front_door_files if (REPO / f).is_file()]

    root_readme = REPO / "README.md"
    readme_text = root_readme.read_text(encoding="utf-8") if root_readme.is_file() else ""
    has_new_here = "New here?" in readme_text

    should_enforce = require or bool(existing_files) or has_new_here

    if not should_enforce:
        status_msg = "Front door: pending M2 implementation (CONTRIBUTING.md, GLOSSARY.md, CHANGELOG.md, and 'New here?' not yet present)"
        return [], status_msg

    status_msg = "Front door: checking newcomer sections and repository help files"

    if not has_new_here:
        errors.append("README.md missing 'New here?' newcomer section")
    else:
        readme_lower = readme_text.lower()
        if not ("copy a skill" in readme_lower or "standalone" in readme_lower):
            errors.append("README.md missing newcomer path: copy a skill")
        if not ("read the stories" in readme_lower or "notes/" in readme_lower):
            errors.append("README.md missing newcomer path: read the stories (notes/)")
        if not ("how a repo works" in readme_lower or "glossary" in readme_lower):
            errors.append("README.md missing newcomer path: learn how a repo works / glossary")

    for req_file in front_door_files:
        p = REPO / req_file
        if not p.is_file():
            errors.append(f"missing required repository front door file: {req_file}")

    return errors, status_msg


def check_all_readability(verbose: bool) -> Tuple[List[str], Dict[str, Tuple[float, float, int, int]]]:
    """Verify readability metrics across root README, skills/README, standalone skill READMEs, and front door."""
    errors = []
    metrics = {}
    target_files = [
        REPO / "README.md",
        SKILLS_DIR / "README.md",
        SKILLS_DIR / "how-to-add-a-skill.md",
        *[SKILLS_DIR / s / "README.md" for s in STANDALONE_SKILLS],
    ]
    for extra in ["GLOSSARY.md", "CONTRIBUTING.md"]:
        p = REPO / extra
        if p.is_file():
            target_files.append(p)

    notes_dir = REPO / "notes"
    if notes_dir.is_dir():
        for note in sorted(notes_dir.glob("*.md")):
            target_files.append(note)

    docs_dir = REPO / "docs"
    if docs_dir.is_dir():
        for doc in ["LAUNCH-CHECKLIST.md", "SPECIALIST-AUDIT-REPORT.md", "NEXT-ROUND-SCOPE.md"]:
            target_files.append(docs_dir / doc)

    for f in target_files:
        if not f.is_file():
            errors.append(f"readability target file missing: {f.relative_to(REPO)}")
            continue
        text = f.read_text(encoding="utf-8")
        fkgl, asl, words, sents = calculate_readability(text)
        metrics[str(f.relative_to(REPO))] = (fkgl, asl, words, sents)
        if fkgl > 6.5:
            errors.append(f"{f.relative_to(REPO)} FKGL={fkgl:.2f} exceeds limit of 6.5")
        if asl > 18.0:
            errors.append(f"{f.relative_to(REPO)} ASL={asl:.2f} exceeds limit of 18.0 words")
    return errors, metrics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skill", nargs="?", help="Optional single standalone skill to check")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print detailed metrics")
    parser.add_argument("--require-front-door", action="store_true", help="Enforce presence of all R4 front-door files and sections")
    args = parser.parse_args()

    skills_to_check = [args.skill] if args.skill else STANDALONE_SKILLS
    all_errors: List[str] = []

    print("Checking standalone skills...")

    for skill in skills_to_check:
        if skill not in STANDALONE_SKILLS:
            sys.exit(f"Unknown standalone skill: {skill!r}. Must be one of {STANDALONE_SKILLS}")
        fm_errs = check_skill_frontmatter(skill)
        rm_errs = check_skill_readme(skill)
        readme_file = SKILLS_DIR / skill / "README.md"
        mm_errs = check_mermaid(readme_file) if readme_file.is_file() else []
        sp_errs = check_australian_spelling(readme_file) if readme_file.is_file() else []
        bt_errs = check_banned_terms(skill) if args.skill else []

        skill_errs = fm_errs + rm_errs + mm_errs + sp_errs + bt_errs
        status = "FAIL" if skill_errs else "ok"
        print(f"skills/{skill}: {status}")
        for e in skill_errs:
            print(f"   error: {e}")
        all_errors.extend(skill_errs)

    if args.skill:
        # Check single skill readability
        skill_readme = SKILLS_DIR / args.skill / "README.md"
        if skill_readme.is_file():
            fkgl, asl, words, sents = calculate_readability(skill_readme.read_text(encoding="utf-8"))
            if args.verbose:
                print(f"\nReadability Metrics:")
                print(f"  {str(skill_readme.relative_to(REPO)):35}: FKGL={fkgl:5.2f} (<=6.5), ASL={asl:5.2f} (<=18.0), Words={words:4d}, Sents={sents:3d}")
            if fkgl > 6.5:
                e = f"{skill_readme.relative_to(REPO)} FKGL={fkgl:.2f} exceeds limit of 6.5"
                print(f"   error: {e}")
                all_errors.append(e)
            if asl > 18.0:
                e = f"{skill_readme.relative_to(REPO)} ASL={asl:.2f} exceeds limit of 18.0 words"
                print(f"   error: {e}")
                all_errors.append(e)

    # Repository-level checks (when checking all skills)
    if not args.skill:
        # Check diagrams in root and skills/ README
        for r in [REPO / "README.md", SKILLS_DIR / "README.md"]:
            if r.is_file():
                rmm_errs = check_mermaid(r)
                if rmm_errs:
                    for e in rmm_errs:
                        print(f"   error ({r.name}): {e}")
                    all_errors.extend(rmm_errs)

        # Legacy teal check
        teal_errs = check_no_legacy_teal()
        if teal_errs:
            for e in teal_errs:
                print(f"   error: {e}")
            all_errors.extend(teal_errs)

        # Banned terms check across repository
        banned_errs = check_banned_terms()
        if banned_errs:
            for e in banned_errs:
                print(f"   error: {e}")
            all_errors.extend(banned_errs)

        # Australian spelling check across READMEs and docs
        for rmd in [REPO / "README.md", SKILLS_DIR / "README.md"]:
            if rmd.is_file():
                rmd_sp_errs = check_australian_spelling(rmd)
                if rmd_sp_errs:
                    for e in rmd_sp_errs:
                        print(f"   error ({rmd.name}): {e}")
                    all_errors.extend(rmd_sp_errs)

        docs_dir = REPO / "docs"
        if docs_dir.is_dir():
            for doc in ["LAUNCH-CHECKLIST.md", "SPECIALIST-AUDIT-REPORT.md", "NEXT-ROUND-SCOPE.md"]:
                dp = docs_dir / doc
                if dp.is_file():
                    dsp_errs = check_australian_spelling(dp)
                    if dsp_errs:
                        for e in dsp_errs:
                            print(f"   error ({dp.name}): {e}")
                        all_errors.extend(dsp_errs)

        # Social preview checks
        social_errs = check_social_preview()
        if social_errs:
            for e in social_errs:
                print(f"   error (social-preview): {e}")
            all_errors.extend(social_errs)

        # SVG text boundaries check & reporting
        svg_bound_errs, svg_status_msg = check_svg_boundaries()
        print(f"{svg_status_msg}")
        if svg_bound_errs:
            for e in svg_bound_errs:
                print(f"   error: {e}")
            all_errors.extend(svg_bound_errs)

        # Front door checks
        fd_errs, fd_status_msg = check_front_door(require=args.require_front_door)
        print(f"{fd_status_msg}")
        if fd_errs:
            for e in fd_errs:
                print(f"   error: {e}")
            all_errors.extend(fd_errs)

        # Notes check
        note_errs = check_notes()
        if note_errs:
            for e in note_errs:
                print(f"   error: {e}")
            all_errors.extend(note_errs)

        # Readability check
        read_errs, metrics = check_all_readability(args.verbose)
        if args.verbose or read_errs:
            print("\nReadability Metrics:")
            for p, (fkgl, asl, words, sents) in metrics.items():
                print(f"  {p:35}: FKGL={fkgl:5.2f} (<=6.5), ASL={asl:5.2f} (<=18.0), Words={words:4d}, Sents={sents:3d}")
        if read_errs:
            for e in read_errs:
                print(f"   error: {e}")
            all_errors.extend(read_errs)

    if all_errors:
        print(f"\nCompleted with {len(all_errors)} error(s).")
        sys.exit(1)
    else:
        print("\nAll standalone skills and documentation checks passed with 0 errors.")
        sys.exit(0)


if __name__ == "__main__":
    main()

