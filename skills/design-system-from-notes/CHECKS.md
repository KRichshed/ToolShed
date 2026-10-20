# Written checks: design-system-from-notes

These test cases check that the skill extracts design tokens carefully and checks contrast.
You can run these checks by hand in any AI tool that supports images.
For each check, attach the image to your tool and compare what comes back.

## Check 1: Happy path (clean keynote slide with clear brand colours)

- **Given:** A crisp photo of a keynote slide with dark text on warm paper.
- **When:** You ask the tool to extract a mini design system.
- **Then:** The tool returns a one-page token sheet with hex codes. It labels values as `*measured*` or `*estimated*`. It verifies that text contrast passes 7:1. It outputs a sample specimen tile.
- **Status:** not run.

## Check 2: Messy input (phone photo with spotlight glare)

- **Given:** A phone photo of an event banner with a bright spotlight glare spot in the centre.
- **When:** You ask the tool to pull brand colours.
- **Then:** The tool samples from the clean corner to avoid the glare. It notes the glare in the source check. It marks all sampled colours as `*estimated*`.
- **Status:** not run.

## Check 3: Failure case (low-contrast colour pairing)

- **Given:** A slide that pairs white text on light lemon yellow (`1.2:1` contrast ratio).
- **When:** You ask the tool to check the colours and build social cards.
- **Then:** The tool flags the failing contrast ratio. It adds white text on yellow to the "Do not use" list. It substitutes a high-contrast charcoal ink (`14.8:1`).
- **Status:** not run.

## Check 4: Rough sketch (hand-drawn ink notes in a journal)

- **Given:** A photo of a rough outline drawn with a fountain pen in a paper notebook.
- **When:** You ask the tool to turn the sketch into a slide theme.
- **Then:** The tool separates hand-drawn ink lines from token values. It selects free system fonts as substitutes. It draws a clean specimen tile.
- **Status:** not run.
