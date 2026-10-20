# Field Note: Design System from Notes

**Skill:** [`skills/design-system-from-notes/`](../skills/design-system-from-notes/README.md)  
**Author:** Kimberly Richards (`@KRichshed`)  
**Status:** v0.3.0

---

## Why I built this

Most small projects do not start inside a Figma library. They start with a photo of a desk, a book cover you love, or three lines in a notebook about how you want the page to feel. You might write: *"warm paper, pen ink, quiet studio, not a cold white dashboard."*

When you ask an AI tool to turn that mood into CSS rules and font sizes, two things often go wrong. First, the AI may ignore your photo and hand you a cold blue-and-grey theme. Second, it may pick pale mid-tone colours straight from your photo and use them for text. That leaves you with faint grey words on a cream page that nobody can read without squinting.

I built **Design System from Notes** when I was setting up the look and feel for this ToolShed repo. I wanted a skill that keeps the warmth of your notes or photo. At the same time, it does the hard maths on colour contrast and type sizes so the palette works on a real screen.

---

## How the design works

### 1. Start from mood and texture, then nudge for contrast

When you drop in a photo, a hex code, or a few mood words, the skill starts by naming the **north star** of your palette in plain words. It sets out the mood, the surface feel, and what the design should never look like.

Next, it pulls out six core colour roles: main background, card surface, main ink, muted ink, main accent, and border. Before it locks those hex codes in, it checks the WCAG 2.2 contrast ratio for each text-and-background pair.

Body text (`ink-primary`) on both backgrounds must hit at least **7:1 (AAA)**. Muted captions (`ink-muted`) and accents (`accent-primary`) must hit at least **4.5:1 (AA)**. If you use the accent colour for small text links, it aims for **7:1**.

What happens if a colour from your photo falls short? The skill does not throw your mood away. Instead, it keeps the same hue and warmth. It nudges the lightness up or down until the contrast passes. Then it shows you both the raw swatch and the tuned hex code so you can see why it changed.

### 2. Named tokens instead of mystery hex codes

Rather than giving you a list of unnamed colours like `blue-500` or `grey-200`, the skill groups each value by the **job it does**. It covers surfaces, ink, accents, status colours (`success`, `warning`, `danger`), a 5-step type scale in `rem`, and a base-4 spacing scale.

Every token comes in two copy-ready blocks. First, you get a **`tokens.json` block** that follows the [W3C Design Tokens Group (DTCG)](https://tr.designtokens.org/format/) structure (`$value`, `$type`, `$description`). You can drop this file straight into Figma or a build tool later.

Second, you get a **`:root` CSS block** with plain custom variables (`--bg-primary`, `--ink-primary`, `--space-4`). It also bakes in a `@media (prefers-reduced-motion: reduce)` rule from day one.

### 3. The five anti-bloat guardrails

A starter design system only helps if you use it. Every run ends with five short rules that keep your pages calm.

First, never put raw hex codes in components. Point to a named token instead. Second, never use colour alone to show an error or status. Always pair colour with an icon or a clear text label. Third, keep line lengths between 60 and 75 characters (`65ch`) so text stays easy to scan. Fourth, honour reduced motion for anyone who turns off animations. Fifth, stick to the spacing scale instead of making up one-off pixel gaps.

---

## How it compares with a standard prompt

Here is how a standard prompt compares with **Design System from Notes** across three starting points:

| Starting input | Standard prompt without this skill | With Design System from Notes |
| :--- | :--- | :--- |
| **A photo of a warm desk and a cream notebook** | Picks low-contrast tan text on beige, or outputs `#FFFFFF` and `#3B82F6`. | Keeps the warm cream surface (`#FBF7EC`), deepens the ink to pass `7:1` contrast, and shows each ratio. |
| **Three mood words** (*"calm, tactile, warm"*) | Gives a vague list of hex codes and font names with no sizes or spacing. | Outputs a full `README.md` guide, a `tokens.json` file, a `:root` CSS block, and a visual SVG card. |
| **A brand colour that is too bright for text** | Uses the bright colour for links and buttons anyway, making text hard to read. | Keeps the bright swatch for large badges, and makes a darker shade for text that meets `>= 4.5:1`. |

---

## Credits and inspirations

**Jina Anne & the W3C Design Tokens Group (DTCG)** created design tokens at Salesforce and co-founded the [W3C DTCG format](https://tr.designtokens.org/format/). Their work shaped the named token layout and `tokens.json` output.

**W3C Web Accessibility Initiative (WAI)** published the [WCAG 2.2 Contrast rules](https://www.w3.org/TR/WCAG22/). Those rules set the `4.5:1` and `7:1` maths checks baked into Step 2.

**Heydon Pickering, Andy Bell, James Gilyead, and Trys Mudford** created **Every Layout** and **Utopia**. Their guides shaped the small type and spacing scales (`rem` and `65ch` rules) that work across screen sizes without complex code.

---

## Known limits

The skill builds one theme at a time, either light or dark. If you want both a light mode and a dark mode, run it once for your light surface and a second time for your dark surface.

It also gives you the visual base (colours, fonts, spacing, borders, and motion rules), not pre-built React or Vue buttons.
