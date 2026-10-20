---
name: claim-to-chart
description: Check a statistic someone cited (in a talk, article or post), trace it to primary sources, give an honest verdict (Confirmed, Adjusted, Disputed or Not found), find adjacent research, then chart the result with an accessible colour-blind safe palette and visible caveats. Use for 'is this stat true', 'fact-check this number', 'find the primary source for this quote', 'check this claim and make a chart', or whenever a cited number sounds important and needs verifying before sharing.
license: MIT
metadata:
  author: KRichshed
  version: "0.2.0"
  autonomy: "Level 1 Operator: suggests, never acts. You decide."
---

# Claim to chart

Verify first, then visualise. A tidy chart of an unverified number is worse than no chart.

## Steps
1. **Capture the claim exactly.** Who said it, where, what number, what it was said to show. Quote it; don't paraphrase yet.
2. **Trace it to a primary source.** Find the original study, dataset or report, not a blog that repeats it. Record: authors, year, sample, method, and the exact figure.
3. **Compare with the claim.** Label the result:
   - **Confirmed**: source says the same thing
   - **Adjusted**: real, but the number or scope differs (state the difference)
   - **Disputed**: credible sources disagree (list them)
   - **Not found**: couldn't locate a primary source. Say so, don't guess.
4. **Look sideways.** Find 2-4 adjacent studies on the same question, including ones that cut against the claim. Note sample size, region and date for each.
5. **Decide what the chart should say.** One sentence. If the evidence supports several messages, pick the one it supports best and show the caveat on the chart.
6. **Build the chart.**
   - Pick the form from the data's job (compare, trend, part-of-whole, spread)
   - Use a palette tested for colour-blind readers: check that every pair of colours stays distinguishable under colour-blindness simulation and meets contrast against the background
   - Never rely on colour alone: add direct labels, patterns or shapes
   - Label units, source and year on the chart itself
   - Add alt text that states the finding, not "a bar chart"
7. **Run the checks.** Colours distinguishable, text contrast OK, numbers match the source, axis doesn't mislead, caveat visible.

## Output

Every run produces four clear artefacts:

### 1. Claim card
- **Original claim**: "[Exact quote as heard or read]" — [Speaker / Source], [Context / Event], [Year]
- **Verdict**: Confirmed / Adjusted / Disputed / Not found
- **Primary source**: [Lead author / Organisation], *[Study / Report Title]*, [Publication / Journal], [Year], [DOI or URL]
- **What the source actually found**: [1–2 plain sentences stating the exact verified measurement and scope]

### 2. Evidence table
| Source / Study | Year | Sample / Method | Finding | Agreement |
| --- | --- | --- | --- | --- |
| [Primary study] | [Year] | [Sample size & method] | [Exact metric] | Primary source |
| [Adjacent study 1] | [Year] | [Sample size & method] | [Comparison metric] | Agrees / Qualifies |
| [Adjacent study 2] | [Year] | [Sample size & method] | [Counter metric] | Disagrees / Differs |

### 3. Chart specification & visual
- **Chart form**: [Bar / Trend / Part-of-whole / Range]
- **Palette tokens**: Use the user's accessible palette if provided; otherwise default to warm paper background (`#FBF7EC`), indigo text and axes (`#1C1D38`), focal series (`#52CFDE`), comparison series (`#D2EE63`), and disputed/stop indicator (`#9E0147`).
- **Direct labels**: Every bar/line has data labels in dark ink; does not rely on colour alone.
- **Alt text**: "[Short description stating the exact finding, comparison, and primary source citation]"
- **One-line caveat**: [Visible qualification or scope limitation displayed directly below the chart]

### 4. What couldn't be verified
- [Specific gap, e.g., missing raw dataset, unverified sub-sample, or paywalled methodology notes]

## Handoffs

List your own destinations here so the verified claim and chart can flow into downstream work:

| Signal in verified claim | Hand off to |
| --- | --- |
| Visual chart needs to match an existing slide or brand palette | `design-system-from-notes` (for matching visual palette and token sheet) |
| Claim is verified and needs to be incorporated into a talk recap | `learning-capture` (for talk synthesis and key takeaways) |
| Goal or audience for the chart is still unclear | `intent-mirror` (for clarifying what the chart needs to show first) |
| Claim phrasing or slide copy needs plain-English polishing | Your writing or slide copy checklist |
| User wants to record the verified fact in a personal log | Your project log or decision notes |

If nothing fits, say so and provide the output directly. Never invent a destination to fill the line.

## Guardrails
- Say "not found" rather than fill a gap with a plausible number.
- Keep the person's original quote and your verified version side by side.
- Don't strip a caveat to make the chart cleaner.
