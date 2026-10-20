# Changelog

All notable changes to ToolShed are documented on this page.
This project uses plain English release notes written for human readers, newest first.

## [v0.3.0] — October 2026

### Evergreen skills audit and newcomer front door

- **Newcomer paths:** Added a "New here?" section to the main `README.md` with three clear pathways for copying skills, reading the companion stories, and learning repository basics.
- **Prompts to skills to agents:** Added a plain-English hierarchy diagram showing how prompts ladder into skills and skills ladder into agents.
- **Repository glossary:** Created `GLOSSARY.md` explaining key Git and AI terms using everyday pictures and simple words.
- **Helping out:** Added `CONTRIBUTING.md` and friendly GitHub issue templates so anyone can ask questions or suggest ideas without needing terminal commands.
- **Honest skill cards:** Audited visual previews in `skills/*/assets/` so sample numbers, quotes, and sources are clearly labelled as made-up demo examples with high-contrast dark ink (`15.3:1`).
- **Written checks:** Added testable Given/When/Then checks to each skill in `skills/*/CHECKS.md` covering happy paths, messy inputs, and failure cases.
- **Folder signposts:** Added clear signposts to `agents/` and `prompts/` explaining how prompts ladder into skills and agents.
- **Automated verification:** Added `tools/check_skills.py` to check for honest labels, Australian spelling, front-door guides, readability, and card boundaries.

## [v0.2.0] — October 2026

### KRichshed v2 design tokens and accessible architecture

- **Design tokens:** Aligned all visual cards and diagrams with the KRichshed v2 palette (`#FBF7EC` paper, `#1C1D38` indigo text, `#52CFDE` pool focal accent, and `#D2EE63` lime outcome badge).
- **Accessible diagrams:** Added `accTitle:`, `accDescr:`, and following `**In words:**` text summaries to all Mermaid diagrams. Removed legacy teal colours.
- **Companion stories:** Published companion notes in `notes/` explaining why each skill was built, how it was tested, and lessons learned.
- **Decision table:** Added a "Which skill do I need?" table to `skills/README.md` linking each task to the right tool.
- **Standard frontmatter:** Standardised frontmatter across skills with explicit Level 1 Operator boundaries.

## [v0.1.0] — October 2026

### Initial release of skills

- **Initial skills:** Launched four tools for people getting started with AI: `intent-mirror` (goal clarification), `learning-capture` (event notes organisation), `claim-to-chart` (data verification), and `design-system-from-notes` (style extraction).
- **Setup guide:** Added `skills/how-to-add-a-skill.md` with step-by-step install instructions for Claude, Google Gemini, and ChatGPT.
