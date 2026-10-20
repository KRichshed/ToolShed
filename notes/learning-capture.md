# Field Note: Learning Capture

**Skill:** [`skills/learning-capture/`](../skills/learning-capture/README.md)  
**Author:** Kimberly Richards (`@KRichshed`)  
**Status:** v0.3.0

---

## Why I built this

After a big event, a workshop, or a week of talks, I always end up with the same pile of messy notes. I have forty photos of slides on my phone, three voice notes from the train ride home, a page of scribbled quotes, and two long talk transcripts.

When you dump that whole pile into a standard AI chat and ask it to sum up your notes, you usually get a flat bullet list. Even worse, the AI blends the speaker's claims with your own thoughts. It rewrites messy quotes in stiff office speak and invents action items you never planned to do. Two weeks later, when you try to share what you learned with your team, the spark of why those talks mattered is gone.

I built **Learning Capture** to turn raw event notes, slide photos, and talk transcripts into a report worth keeping and sharing. It separates what the speakers said from what you think. Then it pairs that report with a visual map that shows how the big ideas fit together.

---

## How the design works

### 1. Keep three voices separate

The main rule in **Learning Capture** is that not every line in your notes has the same weight. As the skill reads through your transcript, slide photos, and voice notes, it sorts what it finds into three clear buckets.

First, **direct quotes (`"..."`)** hold the exact words a speaker said or showed on a slide. Each quote is tagged with who said it and where it came from. What if a quote in your voice note is only half-remembered? The skill marks it as a `[paraphrase]` instead of pretending it is word for word.

Second, **speaker claims (`[Source: ...]`)** hold facts, numbers, or models from the talk. If a slide cites a stat without naming the study behind it, the skill flags it as `[unverified in source notes]`. That way, you know to check it before you repeat it.

Third, **your own thoughts (`[My takeaway]`)** hold the questions, doubts, and ideas you jotted down in the margins about your own work. Keeping those three layers apart means you can trust the report weeks later. You can quote a speaker or pitch a change to your team with confidence.

### 2. Group by theme, not by clock order

When people go to three or four talks in a day, the best insights usually live in the links *between* sessions. Two speakers might back up the same point, or one talk might challenge another. Instead of writing a play-by-play of each talk in clock order, the skill pulls out **3 to 5 core themes** across everything you shared.

Under each theme, it pairs the big idea with the exact speaker quotes and slide notes that back it up. Then it draws a high-contrast Mermaid map (and an optional SVG card). A reader can scan the whole event in ten seconds before reading the detail.

### 3. Honest actions and open questions

Most event summaries end with a fake list of ten huge projects nobody will ever start. **Learning Capture** ends with two small, honest blocks.

The **Open questions & gaps** block lists what the speaker did not answer. It also notes what was cut off on a blurry slide photo. The **Concrete next steps** block lists one to three small actions pulled straight from your own notes, written as *Who / What / When*. If you did not mention any next steps in your notes, the skill offers two gentle ideas and marks them `[Suggested next step]`. They never look like promises you already made.

---

## How it compares with a standard prompt

Here is how a standard prompt compares with **Learning Capture** across three common piles of notes:

| Input pile | Standard prompt without this skill | With Learning Capture |
| :--- | :--- | :--- |
| **A talk transcript + your own margin notes** | Mixes the speaker's views with your notes so you cannot tell who said what. | Labels every quote (`[Source: Slide 4]`) and keeps your own ideas marked as `[My takeaway]`. |
| **Three talks from the same event** | Sums up Talk 1, Talk 2, and Talk 3 one by one with flat bullet points. | Pulls out 3 to 5 shared themes across all three talks and draws a Mermaid map showing how they link up. |
| **A blurry slide photo or a half-remembered quote** | Quietly guesses the missing words or invents a clean quote. | Marks partial quotes as `[paraphrase]` and lists unreadable slide bits under **Open questions & gaps**. |

---

## Credits and inspirations

**Walter Pauk** created the **Cornell Note-Taking System** in *How to Study in College* (1962). His three-part page layout puts themes on the left, notes on the right, and a short summary at the bottom. That layout shaped how this skill sets out every report.

**Sönke Ahrens** wrote *How to Take Smart Notes* (2017). His book shared Niklas Luhmann's *Zettelkasten* slip-box method. It shaped the habit of keeping quick notes, source notes, and your own takeaways apart.

**Tony Buzan** and **Joseph D. Novak** led the way on mind maps and concept maps. Their work shaped the visual theme map that sits at the top of every report.

---

## Known limits

If you have a two-hour video or audio file, turn it into text first (using Whisper, MacWhisper, or your meeting tool). Then pass the text into the skill.

Most AI tools read neat handwriting and printed slides well. Messy cursive or faint whiteboard ink may still need a human check. The skill flags any word it cannot read clearly as `[unreadable in photo]`.
