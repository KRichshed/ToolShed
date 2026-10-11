# QA tester: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** No page could be opened from the build environment (the fetch tool could not reach the web), so nothing here was read directly from its source. Two web searches were run on 2026-10-11 and their summaries are the only direct evidence. Everything else is from memory and is labelled so. Nothing below should be called verified.

## The standard or guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| Test charter form "Explore <target> with <resources> to discover <information>", from Elisabeth Hendrickson's book Explore It! (2013) | From memory. A search for the template found nothing relevant, so the wording was not confirmed | none found. The book itself is the source |
| Exploratory testing as learning, test design and running at the same time, associated with James Bach and others | From memory. Not searched | none |
| Given / When / Then wording for acceptance criteria, from behaviour-driven development | From memory. Not searched | none |
| Lighthouse performance scores fall in three bands, 0 to 49, 50 to 89 and 90 to 100, and Chrome's documentation says the 90 point is set from HTTP Archive data | Search summary only. One summary said 8th percentile, a third-party page said 10th, so the role does not quote a percentile | https://developer.chrome.com/docs/lighthouse/performance/ |
| Commonly quoted "good" values: Largest Contentful Paint 2.5 seconds or less, Total Blocking Time 200 milliseconds or less, Cumulative Layout Shift 0.1 or less | Search summary only, from third-party pages. The role tells people to set their own budget and does not hardcode these | none official seen |
| Lighthouse metric weights | **Not confirmed.** Sources disagreed, so the role gives none | none |
| Performance budgets (a limit the person sets, checked against a tool) | From memory. The web.dev page could not be opened | https://web.dev/articles/performance-budgets-101 (not opened) |
| Lighthouse scores vary between runs, so run it several times | From memory | none |
| Testing can show problems exist, never that none do | From memory (a classic saying from Edsger Dijkstra) | none |

## What tools can and can't find

No reliable figure was found for how much of a page's quality an automated tool can judge, so the role gives none. The role's stance, from memory: tools measure speed and some mistakes, but whether a page does what the person meant needs a person to try it.

## Free tools a beginner can use

- Lighthouse, in the Audits or Lighthouse tab of Chrome developer tools. Not load-tested.
- Chrome's device toolbar, for a narrow window that imitates a phone. Not load-tested. It is an imitation, not a real phone.
- A real phone and a second browser. Nothing to link.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Nothing legal is named here.

## Gap to close before this role is Ready

- Open and read the Chrome Lighthouse scoring page and the web.dev performance budget page.
- Find the exact Explore It! charter wording, or keep it labelled from memory.
- Find a source for Given / When / Then, and for exploratory testing.
- Find an official source for the good speed values, or leave them out.
- Re-run this research from an environment that can open developer.chrome.com and web.dev.
