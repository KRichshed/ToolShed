# Written checks: learning-capture

These test cases check that the skill organises event notes without mixing quotes and thoughts.
You can run these checks by hand in any AI tool.
For each check, attach your notes or files and compare what comes back.

## Check 1: Happy path (conference slide photo and audio recording)

- **Given:** A slide photo and a short audio recording from a conference presentation.
- **When:** You send both items to your AI tool.
- **Then:** The tool returns a summary report that keeps speaker quotes separate from personal notes. It creates a concept mind map and a three-step action list with "#1 Start here" marked.
- **Status:** not run.

## Check 2: Messy input (partially obscured slide)

- **Given:** A phone photo where an attendee's head blocks the lower corner of a slide.
- **When:** You ask the tool to process the slide.
- **Then:** The tool extracts only the visible points. It notes the blocked text under "Gaps". It avoids guessing missing words. It sets Action #1 to ask the speaker for the deck.
- **Status:** not run.

## Check 3: Failure case (unbacked conference statistic)

- **Given:** A presentation slide claiming a "40% drop in review time" with no source study cited.
- **When:** You ask the tool to summarise the talk.
- **Then:** The tool flags the statistic under "Gaps and unchecked claims". It recommends verifying the number through `claim-to-chart` before reuse.
- **Status:** not run.

## Check 4: Messy input (rambling 10-minute voice memo)

- **Given:** A long audio transcript mixing personal complaints, three talk summaries, and eighteen potential tasks.
- **When:** You ask the tool to pull out the key learnings.
- **Then:** The tool moves complaints to personal reflections. It extracts clean talk themes. It trims tasks down to three sized actions, with a quick win marked as "#1 Start here".
- **Status:** not run.
