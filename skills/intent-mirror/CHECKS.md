# Written checks: intent-mirror

These test cases check that the skill clarifies goals and stops at the confirmation gate.
You can run these checks by hand in any AI tool.
For each check, paste the message into your tool and compare what comes back.

## Check 1: Happy path (rambling voice note with multiple tasks)

- **Given:** A voice note transcript mixing slides, quarterly figures, and feeding the cat.
- **When:** You send the transcript to your AI tool.
- **Then:** The tool returns a mirror under 200 words. It separates project goals from personal chores. It provides numbered choices with safe defaults. It pauses for your approval before doing any work.
- **Status:** not run.

## Check 2: Messy input (overwhelmed user feeling stuck)

- **Given:** A message expressing stress, fatigue, and too many competing deadlines.
- **When:** You send the message to your AI tool.
- **Then:** The tool detects the overwhelm state. It skips the long mirror. It gives you three immediate actions with a parking spot. It asks zero questions and waits for your reply.
- **Status:** not run.

## Check 3: Failure case (raw link sent with no instructions)

- **Given:** A single web address sent with no prompt or context.
- **When:** You send the link to your AI tool.
- **Then:** The tool pauses at once. It asks what you want to do with the link. It does not guess or invent actions.
- **Status:** not run.

## Check 4: Correction turn (updating an earlier plan)

- **Given:** An active mirror where you say: "not a flyer, do a message for the group chat".
- **When:** You send this correction back to your tool.
- **Then:** The tool sends back only what changed, in under 60 words. It pauses again for your sign-off.
- **Status:** not run.
