# Archivist: role primer

As of 2026-10-12. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Nothing here was read directly from its source during this session. No page was opened for this primer. Every row is from memory or is the role's own judgement, and the status column says which. Check the current standards and project documentation before quoting any of it.

## The standard or guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| Keep a Changelog 1.1.0 conventions: changelog entries grouped by version, latest first, using categories Added, Changed, Deprecated, Removed, Fixed, Security, with ISO 8601 dates (YYYY-MM-DD) and an Unreleased section at the top | From memory, 2026-10-12. Not opened | https://keepachangelog.com/en/1.1.0/ |
| Semantic Versioning 2.0.0 (SemVer): version numbers formatted as MAJOR.MINOR.PATCH, incrementing MAJOR for breaking changes, MINOR for backwards-compatible features, and PATCH for backwards-compatible bug fixes | From memory, 2026-10-12. Not opened | https://semver.org/spec/v2.0.0.html |
| ISO 8601 date format: standard representation of calendar dates as YYYY-MM-DD for unambiguous ordering and international clarity | From memory, 2026-10-12. Not opened | https://www.iso.org/iso-8601-date-and-time-format.html |
| Web and POSIX file slug naming conventions: lowercase alphanumeric characters separated by hyphens (kebab-case), avoiding spaces, uppercase letters, and punctuation to prevent URL-encoding and command-line escaping bugs | Common industry practice, 2026-10-12. No single official specification | none |
| Deprecation notices and tombstone patterns: placing prominent notices at the top of obsolete files with deprecation date, reason, and replacement pointer, or leaving stub files when paths are moved to prevent broken links | Common archival and software practice, 2026-10-12. The role's judgement | none |
| Safe archiving over deletion: retaining historical context by moving obsolete drafts to an archive folder or relying on version control history rather than permanently erasing unrecorded context | Common archival practice, 2026-10-12. The role's judgement | none |
| README indexing and directory navigation: root and subfolder README files serving as entry points, tables of contents, and signposts for repository navigation | Common repository practice, 2026-10-12. The role's judgement | none |

## What tools can and can't find

Automated tools (such as markdown link checkers or linter scripts) can check whether relative file paths resolve, detect broken URLs, flag inconsistent heading levels, or check date regexes. They cannot judge whether a directory structure makes sense to a new reader, whether a changelog entry accurately describes the human impact of a change, whether a document should be archived or kept active, or whether a deprecation notice is clear. If a tool is used (for example markdown-link-check), label the finding "found by a tool" with the tool name and date.

## Free tools a beginner can use

- `markdown-link-check`: Open-source tool to check for broken links in markdown files. Run locally or via command line. Not load-tested in this session. https://github.com/tcort/markdown-link-check
- Standard version control commands (`git mv`, `git log`): Built-in commands to rename and move files while preserving commit history.
- Plain text search (`grep`, `rg`, or editor search): Simple search across files to find all inbound references before renaming or moving a file. No link needed.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Record keeping, document retention periods, statutory archives (such as financial, tax, corporate records, or health data), and privacy deletion obligations (such as GDPR right-to-be-forgotten or Australian Privacy Principles) have formal legal requirements that vary by jurisdiction. Never claim a repository structure or archiving plan meets statutory legal retention rules.

## Gap to close before this role is Ready

- Read Keep a Changelog 1.1.0 directly and verify all standard section names and guidelines.
- Read SemVer 2.0.0 directly and verify exact definitions for pre-release and metadata notation.
- Check whether any project-specific link-checker tools or linter rules are configured in the workspace.
- Add specific regional statutory retention references if working with corporate or personal data.
