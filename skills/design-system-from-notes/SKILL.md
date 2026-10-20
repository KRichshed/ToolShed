---
name: design-system-from-notes
description: Lift a colour and type pairing off a real photo, slide or screenshot, label each value by confidence (measured, estimated or substitute), check WCAG contrast, and write a one-screen reusable design system (`design-system.md`) plus a sample specimen tile. Use for 'make it look like this', 'pull the colours and fonts from this slide', 'match this screenshot', 'turn this photo into a style guide', or when multiple visuals keep drifting apart.
license: MIT
metadata:
  author: KRichshed
  version: "0.2.0"
  autonomy: "Level 1 Operator: suggests, never acts. You decide."
---

# Design system from notes

Turn one real visual reference into a mini design system so everything you make afterwards looks like it belongs together.

## When to use
- You have a photo, slide, screenshot or brand sheet and want new material to match it.
- You're making several assets (carousel, charts, one-pagers) and they keep drifting apart.

## Steps
1. **Look at the source.** Name what you can actually see: background, text colour, one or two accent colours, heading font style, body font style, any repeated shapes or spacing habits.
2. **Pick values, say how sure you are.** From a photo you can only estimate hex values and fonts. Mark each as *measured* (given by the user or a file), *estimated* (read off an image) or *substitute* (a free font close to the original). Never claim an exact match you can't verify.
3. **Write the mini system.** Keep it to one screen:
   - Colours: background, text, muted text, 1-2 accents, plus a "do not use" note
   - Type: heading, body, sizes for small / medium / large
   - Shape and spacing: corner radius, padding, grid, border style
   - Voice of the visuals: three adjectives
4. **Check legibility.** Text on every background pair needs enough contrast (aim for WCAG AA: 4.5:1 for body, 3:1 for large text). Fix the pair, not the rule.
5. **Save it as a file** (`design-system.md` or tokens in your tool's format) and reference it at the top of every later task.
6. **Apply, don't reinvent.** For each new asset, use only the saved values. If something is missing, add it to the system first, then use it.

## Output

Every run produces two clear deliverables:

### 1. `design-system.md` (Token Specification)
- **Source reference**: [Brief description of reference image, slide photo, or screenshot, plus lighting or glare notes]
- **Voice of the visuals**: [Three adjectives describing the source feel, e.g. "warm, editorial, crisp"]
- **Colours** (extracted from the user's source image):
  | Role | Hex | Confidence | Notes |
  | --- | --- | --- | --- |
  | Ground / Paper | `[#HEX from source, e.g. #FBF7EC]` | `*measured*` or `*estimated*` | [Primary background role and feel] |
  | Ink / Text | `[#HEX from source, e.g. #1C1D38]` | `*measured*` or `*estimated*` | [Primary heading and body text] |
  | Accent / Focal | `[#HEX from source, e.g. #52CFDE]` | `*measured*` or `*estimated*` | [Single focal highlight] |
  | Secondary / Outcome | `[#HEX from source, e.g. #D2EE63]` | `*measured*` or `*estimated*` | [Secondary accent or status badge] |
  | Alert / Stop | `[#HEX from source, e.g. #9E0147]` | `*estimated*` or `*substitute*` | [High-contrast alert or error indicator] |
  | Muted / Border | `[#HEX from source, e.g. #848499]` | `*estimated*` or `*substitute*` | [Borders, dividers, or offset layers] |
- **Do not use**: [Banned colours or low-contrast pairings spotted in the source, e.g. white text on pale yellow or cyan]
- **Contrast audit**:
  | Foreground on Background | Ratio | Target | Status |
  | --- | --- | --- | --- |
  | `[Ink #HEX]` on `[Ground #HEX]` | `[X.X:1]` | >= 4.5:1 | Pass / Adjusted |
  | `[Ink #HEX]` on `[Accent #HEX]` | `[X.X:1]` | >= 4.5:1 | Pass / Adjusted |
  | `[Ink #HEX]` on `[Secondary #HEX]` | `[X.X:1]` | >= 4.5:1 | Pass / Adjusted |
- **Typography hierarchy**:
  - Heading font: `[Detected font or free *substitute*, e.g. Bricolage Grotesque or system sans-serif]`
  - Body font: `[Detected font or free *substitute*, e.g. system sans-serif]`
  - Monospace: `[Detected font or free *substitute*, e.g. JetBrains Mono]`
  - Scale: Small (`14px`), Body (`18px`), Subheading (`24px`), Title (`36px`), Display (`56px`)
- **Shapes & Spacing**:
  - Corner radius: `[Observed radius from source, e.g. 0px crisp corners or 8px rounded]`
  - Spacing scale: `8px`, `16px`, `24px`, `48px`
  - Border & depth: `[Observed border width and shadow/offset style]`

### 2. Sample specimen tile
A single visual specimen preview demonstrating the extracted heading, body copy, colour chips, and high-contrast pairing for human approval before building full sets.

## Handoffs

List your own destinations here so the extracted tokens can flow cleanly into production:

| Signal in design system output | Hand off to |
| --- | --- |
| Palette includes quantitative data tokens or chart requirements | `claim-to-chart` (for charting tokens and accessible data visuals) |
| Slide notes also include talk takeaways or event recordings | `learning-capture` (for synthesising talk notes and action lists) |
| Scope or target use for the design system is still fuzzy | `intent-mirror` (for clarifying the goal before building screens) |
| Colour pairings need further contrast or screen-reader checks | Your accessibility and contrast checker |
| Extracted design decisions need recording in a project log | Your project log or decision notes |

If nothing fits, say so and provide the output directly. Never invent a destination to fill the line.

## Guardrails
- Don't copy someone else's logo, artwork or distinctive mascots. Take colour and type feel, not protected marks.
- Ask the person to confirm the sample before building a large set.
- If the source image is blurry or has odd lighting, say so and ask for a better one or a hex code.
