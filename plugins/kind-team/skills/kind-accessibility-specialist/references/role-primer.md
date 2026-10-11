# Accessibility specialist: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** The sources below were looked up with web search on 2026-10-11. The pages themselves could not be opened from the build environment, so nothing here was read directly from the standard. The status column says what is confirmed by search, and what is still from memory and needs a direct read.

## The standard

| Fact | Status | Source |
|---|---|---|
| WCAG 2.2 became a W3C Recommendation on 5 October 2023 | Confirmed by search | https://www.w3.org/TR/WCAG22/ |
| WCAG 2.2 is also the international standard ISO/IEC 40500:2025 (W3C announced approval on 21 October 2025) | Search summary only, announcement page not seen | not verified |
| WCAG 3.0 is still a draft (latest listed: March 2026). No WCAG 2.3 found | Confirmed by search | https://www.w3.org/WAI/Technical/Activity |
| WCAG 2.2 adds 9 success criteria and removes 4.1.1 Parsing | Confirmed by search | https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ |
| 2.4.11 Focus Not Obscured (Minimum), level AA | Confirmed by search | same page |
| 2.5.8 Target Size (Minimum), level AA: at least 24 by 24 CSS pixels, with exceptions | Confirmed by search | same page |
| 3.3.8 Accessible Authentication (Minimum), level AA | Confirmed by search | same page |
| 3.3.7 Redundant Entry (A), 2.5.7 Dragging Movements (AA), 3.2.6 Consistent Help (A) | From memory | to verify |
| 1.4.3 Contrast (Minimum), level AA: 4.5 to 1 for normal text, 3 to 1 for large text. Large means 18 point, or 14 point bold, about 24 or 18.5 pixels | Confirmed by search | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html |
| 1.4.11 Non-text Contrast, level AA: 3 to 1 for interface parts and graphics | Supported indirectly | to verify |
| 2.3.3 Animation from Interactions is level AAA. The CSS `prefers-reduced-motion` rule is technique C39, which is informative, not required. There is no AA rule that requires it | Confirmed by search | https://www.w3.org/WAI/WCAG22/Techniques/css/C39 |
| Every other success criterion number and level used in SKILL.md (keyboard, focus, headings, forms, images, zoom, language, status messages) | From memory | to verify against the standard |

## What automated tools can find

| Fact | Source |
|---|---|
| UK Government Digital Service added 142 barriers to a test page and ran 13 tools. The best found 40 percent, the worst 13 percent. All tools together found 71 percent. 42 barriers were missed by every tool. Audit date: 2017 | https://alphagov.github.io/accessibility-tool-audit/results.html |
| The GOV.UK engineering guidance says automated testing finds "around 30 percent" | search summary, page not seen |
| A tool maker's study (Deque) reports automated testing finds 57 percent of issues by volume, across 13,000 pages. It is a vendor study, it covers only part of the AA criteria, and it has not been independently repeated | https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/ |

**Use of these numbers:** tell the person "tools find only part of the problems, roughly a third to a half in independent testing, and none find everything". Never quote a single figure as the answer.

## Free tools a beginner can use

URLs were not load-tested. Check them before quoting.

- axe DevTools, from Deque: https://www.deque.com/axe/
- WAVE, from WebAIM: https://wave.webaim.org/
- Lighthouse: built into Chrome DevTools, under the Lighthouse tab
- Accessibility Insights: https://accessibilityinsights.io/

## Law, and what to say about it

Rules differ by country and by who a site is for. The role never gives legal advice and says "check your local rules".

- The European Accessibility Act applies from 28 June 2025 and covers a list of consumer products and services. A personal, non-commercial site looks out of scope, but no source addressed that directly. Source: https://www.reedsmith.com/our-insights/blogs/viewpoints/102kxnd/the-eu-accessibility-act-is-now-in-force/
- In Australia, the Disability Discrimination Act 1992 covers discrimination in goods and services, and complaints go to the Australian Human Rights Commission. Whether it reaches a personal site: unsure. Source: https://pwd.org.au/about-us/about-disability/key-disability-legislation/

## Gap to close before v1.0

- Read the standard directly for every success criterion in SKILL.md, and fix any level or wording that differs.
- Confirm the full list of the 9 new criteria in 2.2.
- Read the ISO/IEC 40500:2025 announcement.
- Load-test the tool URLs, and add WebAIM and GOV.UK beginner guidance with working links. The W3C WAI "Easy Checks" page is a good first review for non-specialists (https://www.w3.org/WAI/test-evaluate/).
- Add a regional pack for each region the kind team supports. Without one, the role teaches the principle and says to check local rules.
- Re-run this research from an environment that can open w3.org, gov.uk and webaim.org.
