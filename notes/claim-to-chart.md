# Field Note: Claim to Chart

**Skill:** [`skills/claim-to-chart/`](../skills/claim-to-chart/README.md)  
**Author:** Kimberly Richards (`@KRichshed`)  
**Status:** v0.3.0

---

## Why I built this

When you write a report or a talk deck, you often have a big claim that needs a chart. You might want to show that AI tools save time on small tasks. Or you might want to show that teams spend too much of their week in meetings.

If you ask a standard AI chat to draw that chart, two things often go wrong. First, if you do not have the numbers on hand, the AI will quietly invent a study and fake percentages so it has something to plot. Second, it often picks bright default colours that clash with your slides and fail text contrast checks.

I wanted a skill that acts like a careful research helper and a calm chart designer at the same time. It looks for real public data first. Then it shows you what it found before it draws a single line, and it never makes up a number.

---

## How the design works

### 1. Ground the claim before drawing

The biggest change in this skill is the pause between Step 2 and Step 3. When you give the skill a claim without your own numbers, it searches for a public source. That can be a peer-reviewed paper, a government report, or a named industry study.

Once it finds a source, it stops. It shows you the exact title, date, link, and numbers. Then it asks whether that source fits what you mean before it builds the chart.

What if no honest public data exists for your claim? Instead of guessing or making up a stat, the skill switches to a **Claim Card**. A Claim Card frames your idea as a clear test statement. It names the gap in plain words and suggests one small way to measure it yourself. That way, you never walk into a room with a fake chart on your slide.

### 2. Pick the simplest chart that fits the data

Most claims do not need a complex diagram. Following the plain-chart habits from Edward Tufte (1983) and Cole Nussbaumer Knaflic (2015), the skill picks the quietest shape that fits your numbers.

A **horizontal bar chart** works best when you compare a few items. A **line or slope chart** works best when you show a change over time. A **flow diagram** works best when you explain a step-by-step process. And a **Claim Card** works best when the numbers do not exist yet.

It skips 3D bars, dual-axis lines, and pie charts with more than three slices. Those shapes make people work harder to read the truth.

### 3. Keep every chart readable and accessible

Every chart the skill makes comes in three parts so you can use it anywhere.

First, you get a **Mermaid block** that renders inside GitHub, Notion, or markdown notes. It includes an `accTitle`, an `accDescr`, and an `**In words:**` summary right underneath for screen readers.

Second, you get a **clean SVG file** with a `<title>` and `<desc>` tag, clear labels, and a source caption at the bottom. If you do not pass your own brand colours, it falls back to the warm cream, ink, and teal palette from my ToolShed tokens.

Third, you get a **short markdown table** of the raw numbers. Anyone can check the maths or copy the values into a sheet.

---

## How it compares with a standard prompt

Here is how a standard one-line prompt compares with **Claim to Chart** across three test cases:

| Scenario | Standard prompt without this skill | With Claim to Chart |
| :--- | :--- | :--- |
| **A claim with no numbers attached** (*"Show that design ops saves time"*) | Often invents percentages or names a vague report with no link. | Searches for a real public study, pauses to let you check the source, or builds a **Claim Card** if no study exists. |
| **A small table of your own survey results** | Draws a chart with default neon colours, tiny labels, and no alt text. | Checks the totals first, picks a horizontal bar chart, adds direct labels, and writes an `**In words:**` summary. |
| **A process claim** (*"How a token moves from Figma to code"*) | Outputs a cramped diagram with low-contrast boxes. | Builds a high-contrast Mermaid flow diagram (`>= 7:1` text contrast) paired with a plain summary. |

---

## Credits and inspirations

**Edward Tufte** wrote *The Visual Display of Quantitative Information* (1983). His work shaped the rule that every drop of ink on a chart should earn its place by showing real data.

**Cole Nussbaumer Knaflic** wrote *Storytelling with Data* (2015). Her book shaped the rules for direct labels, calm background colours, and active chart titles.

**W3C Web Accessibility Initiative (WAI)** published the [WCAG 2.2 Contrast guidelines](https://www.w3.org/TR/WCAG22/) and the [Mermaid Accessibility Guide](https://mermaid.js.org/config/accessibility.html). Those guides shaped the `accTitle`, `accDescr`, and `**In words:**` rules in every output.

---

## Known limits

If your AI tool does not have web search turned on, or if a study sits behind a paywall, the skill cannot read the numbers inside it. It will tell you what it could not reach and ask you to paste the numbers or use a Claim Card.

The skill also caps charts at 7 bars or series so labels stay easy to read on a phone screen. It is not meant for dense dashboards or live data feeds.
