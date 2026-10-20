# Written checks: claim-to-chart

These test cases check that the skill verifies claims honestly before drawing charts.
You can run these checks by hand in any AI tool.
For each check, copy the input into your tool and compare what comes back.

## Check 1: Happy path (verified statistic with primary source)

- **Given:** A clear statistic with a known source: "68% of software engineers use AI code tools daily, from the 2026 developer survey".
- **When:** You send this claim to your AI tool with web search turned on.
- **Then:** The tool returns a Confirmed verdict. It cites the primary study. It outputs a chart with high-contrast text (`#1C1D38` on `#FBF7EC`). It lists study limits on the canvas.
- **Status:** not run.

## Check 2: Messy input (voice note mixing trial users and daily users)

- **Given:** A rambling voice transcript that confuses people who tried a tool once (92%) with people who use it daily (46%).
- **When:** You send the transcript to your AI tool.
- **Then:** The tool returns an Adjusted verdict. It separates trial users from daily users. It explains the confusion in plain words. It charts both bars with direct labels.
- **Status:** not run.

## Check 3: Failure case (internet rumour with no primary source)

- **Given:** A common blog statistic with no evidence: "84% of website redesigns fail within six months".
- **When:** You ask the tool to verify the source and draw a chart.
- **Then:** The tool returns a Not found verdict. It explains that the trail ends at dead links. It advises you not to draw a chart.
- **Status:** not run.

## Check 4: Disputed data (conflicting studies on project failure rates)

- **Given:** A statistic where two credible studies disagree (85% failure rate versus 54% stall rate).
- **When:** You ask the tool to check the claim.
- **Then:** The tool returns a Disputed verdict. It plots both studies side by side. It highlights the range rather than picking one winner.
- **Status:** not run.
