# UI designer: role primer

As of 2026-10-12. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Nothing here was read directly from its source during this session. No page was opened for this primer. Every row is from memory or is the role's own judgement, and the status column says which. Check the current page before quoting any of it.

## The standard or guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| WCAG 2.2 contrast minimums: 4.5:1 for normal body text, 3:1 for large text (at least 24px regular or 18px bold) and user interface components (such as form field borders and button boundaries) | From memory, 2026-10-12. Not opened | https://www.w3.org/WAI/WCAG22/quickref/#contrast-minimum |
| The 60-30-10 colour distribution rule (60% dominant neutral background, 30% secondary structure/cards, 10% accent) as a visual balance guideline | From memory, 2026-10-12. Classical interior and graphic design convention, no single URL | none |
| Modular typography scales using consistent geometric ratios (Major Third 1.25, Minor Third 1.2, Perfect Fourth 1.333) to determine proportional heading and body sizes | From memory, 2026-10-12. Standard typographic practice based on Bringhurst's Elements of Typographic Style | https://type-scale.com/ |
| 4px and 8px spacing grids: snapping layout margins, padding, and component heights to multiples of 4px and 8px | From memory, 2026-10-12. Standard in design systems including Material Design and Apple HIG | https://m3.material.io/foundations/layout/understanding-layout/spacing |
| Interactive component states: five standard states (default, hover, focus, active, disabled) and visible focus indicator requirements | From memory, 2026-10-12. W3C WAI-ARIA Authoring Practices Guide and WCAG 2.2 criterion 2.4.7 Focus Visible | https://www.w3.org/WAI/ARIA/apg/ |
| Dark mode surface elevation and contrast: using dark grey/slate tonal surfaces (#121212) rather than pure #000000, and off-white text to prevent halation and eye fatigue | From memory, 2026-10-12. Material Design dark theme specification | https://m2.material.io/design/color/dark-theme.html |
| Gestalt principles of visual perception (proximity, similarity, figure-ground) underpinning visual hierarchy and spacing | From memory, 2026-10-12. Foundational psychology of perception | none |

## What tools can and can't find

Automated tools can calculate mathematical colour contrast ratios between two known hexadecimal or RGB values on flat, solid backgrounds. However, automated tools cannot judge whether visual hierarchy leads the eye effectively, whether an interface element has sufficient affordance (looks clickable), whether spacing creates logical grouping (proximity), or how semi-transparent layers, gradients, or background images alter legibility in practice. If a tool is ever used to calculate contrast or check tokens, label the finding as "found by a tool" with the tool name and date.

## Free tools a beginner can use

- WebAIM Contrast Checker (https://webaim.org/resources/contrastchecker/): Free browser tool to check contrast ratios between foreground and background colours. Not load-tested.
- WhoCanUse (https://whocanuse.com/): Free tool showing how colour combinations appear to people with varied vision impairments and in direct sunlight. Not load-tested.
- Type Scale (https://type-scale.com/): Free visual calculator for previewing and choosing modular typography scales. Not load-tested.
- Coolors (https://coolors.co/): Free palette generator with built-in contrast checkers and colour blindness simulators. Not load-tested.
- Pen, paper, and browser inspect tool: The fastest way to inspect spacing, padding, and font sizes on any live HTML element.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Colour contrast ratios (WCAG Level AA 4.5:1 and 3:1) and visible focus indicators are often codified into statutory accessibility laws for public sector and commercial websites, including the European Accessibility Act (Directive 2019/882), Section 508 in the United States, and the Disability Discrimination Act in Australia. Non-compliance can carry legal penalties in certain jurisdictions. No regional statutory source was read directly.

## Gap to close before this role is Ready

- Read the WCAG 2.2 Contrast (Minimum 1.4.3, Non-text Contrast 1.4.11, Focus Appearance 2.4.13) specifications directly to confirm technical wording.
- Read the Material Design 3 spacing and elevation guidelines directly to confirm current surface elevation recommendations.
- Verify whether 60-30-10 or 8pt grid systems have formal published research papers or remain industry consensus rules of thumb.
- Add specific regional statutory citations for accessibility requirements across the US, UK, EU, and Australia.
