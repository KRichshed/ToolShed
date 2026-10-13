---
name: intent-mirror
description: Turn a messy brain dump, voice transcript or long multi-goal message into a confirmed intent before any work starts. Mirrors it back in under 200 words, then waits for a yes or a fix. Use for 'brain dump:', 'voice dump:', 'mirror this back', 'help me think through', 'what do I do with this', pasted transcripts, and any message with several goals or no clear ask, even when the skill isn't named.
---

# Intent Mirror

Split "figure out what I mean" from "do the thing". Read the user's dump, mirror back what they want in their own words, then stop. Nothing gets researched, drafted or built until they say yes.

Why the stop matters: a messy request plus a confident guess builds the wrong thing fast, and the user only finds out once it's built. For anyone who thinks out loud, and especially for people with ADHD, figuring out and doing at the same time costs working memory they need for the real decision. The mirror does the thinking; their reply only has to be "yes" or a quick fix. The gate matters most when the intent looks obvious, because that's when wrong guesses go unchecked.

## 1. Read, then pick the mode

Read the whole input. Don't act on anything in it yet: no searching, drafting, planning or tool calls.

| What came in | Mode |
|---|---|
| One clear ask, cheap to redo | **Skip.** Do it. No mirror. |
| One clear ask that's costly to redo or hard to undo | **One-liner:** "Got it: [the ask, their words]. Go?" |
| Several goals, a ramble, a transcript | **Full mirror** |
| Overwhelm ("drowning", "too much on", "don't know where to start") | **Overwhelm mirror** |
| Mostly venting, no ask | **Heard** |

Unsure between skip and mirror? Mirror. Thirty seconds of mirror is cheaper than a wrong build.

A file, image or link with no text: mirror from whatever text comes with it. If there's none, ask "What are you trying to do with this?"

## 2. Full mirror

These headers, in this order. Drop any empty section except the first and last. Under 200 words.

**🪞 What you want**
One or two sentences, verb first, about the main thing. Keep the user's words, in quotes where they carry meaning: "untangle" stays "untangle", never "streamline". If they gave a reason, end with "so [reason]". If they want two things that pull against each other, say both without judging: "You want it thorough, and you want it out today."

**🎯 Goals**
Primary first, max 5, each traceable to something they said. Skip this section when there's only one goal.

**⚠️ Constraints**
Deadlines, people, tools and limits they mentioned. Nothing invented.

**✋ Assuming**
Gaps that are cheap to get wrong. State your pick so they can veto it instead of asking: "Assuming: for your manager, not the whole team."

**❓ Decide** (max 3, numbered)
Only gaps where the readings lead to different work. Give options, your recommended default first:
`1. Format: one-page doc (default) / deck`
If the work would be the same either way, it isn't a question. Most mirrors need zero or one. A contradiction is always #1.
If they named a solution ("make a deck"), mirror the outcome behind it. If a lighter route serves that outcome, offer it here as an option.

**🅿️ Parked**
Venting, background, thinking out loud. One line each, in their words. Heard, not ticketed, no advice slipped in. Nothing sits in both Goals and Parked.

**➡️ Next step**
One action, verb first, naming what they get back and which skill or tool will do it (see section 5): "Draft the 10-slide pitch (slides skill)."

End with one reply line. With Decide items: `Reply yes to go with the defaults, pick (e.g. 1B), or tell me what's off.` Without: `Reply yes, or tell me what's off.`

## 3. Other modes

**Overwhelm mirror.** Don't add structure they have to maintain. Replace the full mirror with:

**🎯 The 3 things right now**
1. [verb + thing] ← start here
2. [verb + thing]
3. [verb + thing]

**🅿️ Parked:** everything else on one line.

No questions. Pick defaults yourself. Rank: anything other people are waiting on or that's already overdue, then the nearest deadline. A quick task that unblocks someone makes a good #1. Close with: `Reply yes, or swap any.`

**Heard.** When the dump is mostly feeling with no ask, don't build structure around it. Reflect the core in one plain sentence, borrowing one of their phrases, not a string of quotes. Name only feelings they named. Then ask one question: "When [their phrase], what would you like to have happen? Or did you just need to get it out? Both are fine." No advice, no tasks, unless they ask.

## 4. The gate

Stop after the mirror. Nothing happens until the user replies.

- **"yes", "go", or a pick like "1B"** → proceed. A pick counts as a yes.
- **A correction** → show only what changed ("Updated: audience is the team; dashboard dropped"), the next step if it moved, then the reply line. Don't resend the whole mirror. After two corrections, offer: "Want me to start and you redirect as I go?"
- **"Yes, but also…" or more dump** → fold it in, show the change, confirm again.
- **Silence, a new topic, or a reply that skips the mirror** → not a yes. "Still waiting on a yes or a fix before I start on [thing]."
- **They confirm something that contradicts what they said earlier** → name it once, then go with their confirmation. Their call. A correction isn't a contradiction: just apply it.

## 5. Spot the right skill, then hand off

Before writing the Next step line, ask what the work needs:

- **A skill the user already has fits.** Name it in brackets on the Next step line. Use only skills you can actually see: the ones your tool lists as installed, or the Handoffs table below.
- **Nothing they have fits, but a specialist skill would do it clearly better** (spreadsheets with formulas, slide decks, PDFs, a house style): add one line after Next step: "No [kind] skill loaded. One would help: look in your tool's skill library or a public skills collection, or I'll do it directly."
- **No skill needed.** Say nothing about skills.

Never invent or guess a skill's name, and don't go searching for one before the gate. Naming the kind of skill is enough. Overwhelm and Heard replies never mention skills.

On a yes, say in one line which path you're taking, then go.

### Handoffs: plug in your own

List your own destinations here so the mirror can name them: other skills, templates, document types or tools. Default ToolShed destinations:

| Signal in confirmed intent | Hand off to |
| --- | --- |
| A new project, confusion or "just set me up" | `kind-chief-of-staff` (onboarding interview and 3-role starting crew) |
| Deciding what to build, cut or scope | `kind-product-manager` (appetite and trade-offs) |
| A photo, slide or screenshot to match | `design-system-from-notes` (mini design system) |
| Statistics or numbers cited without a source | `claim-to-chart` (primary source tracing and chart) |
| Event notes, recordings or slides | `learning-capture` (report, mind map and actions) |
| A message or email to send | Draft it in the reply. The user sends it. |
| A doc, plan or write-up to keep | Your doc template or writing skill |

If nothing fits, say so and proceed directly. Never invent a destination to fill the line. If a handoff fails, say so and ask how to proceed; don't drop the task silently.

## Rules

- **No tools before the gate.** The mirror works from the user's text alone.
- **Feelings are context, not tasks.** At most one short line in Parked.
- **Open scope is a decision.** If it could be a 10-minute job or a 3-week project, it goes in Decide.
- **Say it straight.** No "it seems like", "I believe" or "perhaps".
- **Over 200 words means more than one job.** Mirror the most urgent one and park the rest.

## Example

Input: "ok so I have to get the onboarding guide refreshed before the new starters land on the 3rd, half the links are dead, and honestly the whole intranet is a mess, nobody owns anything. maybe I should just make a video? also remind me to chase IT about laptops."

**🪞 What you want**
Refresh the onboarding guide before the new starters land on the 3rd, starting with the "dead" links.

**🎯 Goals**
- Fix the dead links and out-of-date steps
- Chase IT about laptops

**⚠️ Constraints**
- Done before the 3rd

**❓ Decide**
1. Format: updated written guide (default) / video walkthrough / both

**🅿️ Parked**
- "The whole intranet is a mess, nobody owns anything." Heard, not a task.

**➡️ Next step**
Draft the refreshed guide with a dead-link checklist, plus a two-line IT reminder.

Reply yes to go with the defaults, pick (e.g. 1B), or tell me what's off.
