# Intent mirror: why I built it and what changed

The skill lives in [`skills/intent-mirror/SKILL.md`](../skills/intent-mirror/SKILL.md).

## What it does

Intent mirror is a plain-English AI skill that sits between your brain dump and your AI tool doing anything with it. It reads a messy prompt or voice transcript, mirrors back what you want in your own words in under 200 words, and stops. Nothing gets built until you say yes.

## Why I built it

I have ADHD. My best thinking comes out sideways: voice notes, half sentences, and three ideas tangled into one. That is how I think, and it works fine for me.

The trouble starts when I hand that mess to an AI tool. It picks the most likely meaning and runs with that guess fast and with confidence. I end up with a neat draft of the wrong thing, and now I am untangling the draft and my own thoughts at once.

Working out what I mean and doing the work are two separate jobs. I get stuck when I try to do both at the same time. So this skill splits them. First it mirrors, and I check the mirror. Then it does the work.

## Who it is for

I built this for my ADHD brain, and it is tuned to how I work. Good access tools rarely help only the people they were built for. Voice typing is the classic example: it began as an access tool, and now makes things easier for everyone. If you are not ADHD and want a calmer way to start a task, help yourself.

## If you came from the CWA post

I used this skill at Connected Women Australia's 2026 event after giving an AI agent a rough audio transcript recorded in my pocket and a handful of slide photos. Before it built anything, the mirror played back what I had asked for: a public notes page and a short post about the workflow. It asked three simple questions, including whether to name the AI tool. One short reply and we were off.

## How it evolved

Version 1 came out of a session where I built a handful of skills with an AI tool. It had six fixed sections (what you want, goals, constraints, ambiguities, not-asks, and next step), a hard gate, and a table that routed confirmed work to my other tools. Later, I added an overwhelm mode that picks the top three actions right now instead of a long list.

The gate worked well. Testing it against seven messy inputs showed me five slow spots:

- **Open questions:** It asked broad questions where I had to stop and write long answers. That was the effort the skill was meant to save.
- **Clear asks got a mirror anyway:** A simple one-line ask got a "Go ahead?" check first. One extra round trip for nothing.
- **Venting became a ticket:** A vent got a canned "noted as context" reply and an empty goals list. It felt cold.
- **Edits re-sent everything:** Fix one word and the whole 170-word mirror came back.
- **Overwhelm mode felt heavy:** It added six sections and a question, which was what it was meant not to do.

## What changed in version 2

I looked at how other people handle "what do you mean?": requirements engineers, counsellors, Clean Language facilitators, Jobs to Be Done, and published AI skills. I kept only what made the mirror sharper, faster, or kinder.

- **Your words, not mine:** If I say "untangle", the mirror says "untangle", not "streamline". This comes from **David Grove's Clean Language** and reflective listening. Your own words land faster and show the AI heard you.
- **Questions come with a default:** Each question is a numbered choice with a recommended pick first, so "yes" accepts the lot and "1B" changes one. Borrowed from **ClarifyGPT** (Mu et al.) and **Jesse Vincent's (`obra`) Superpowers** brainstorming skill.
- **Only ask what changes the work:** If both answers lead to the same draft, skip the question. Small gaps become an "Assuming" line I can veto. In testing, most mirrors asked one question or none.
- **The need behind the fix:** If I say "make a deck", it mirrors what the deck is for and can offer a lighter option. From **Karl Wiegers** on software requirements and **Jobs to Be Done**.
- **Mixed requests, said kindly:** "You want it thorough, and you want it out today." It names both sides without blame, then sets a default for which one wins. From the double-sided reflection in **William R. Miller and Stephen Rollnick's Motivational Interviewing**.
- **A "Heard" mode for venting:** One sentence back, then one question: what would you like to have happen, or did you just need to get it out? Both choices are fine.
- **Corrections show only what changed:** The mirror prints only the updated lines.
- **Clear asks skip the mirror:** It only checks first when a task is costly to redo or hard to undo.
- **Overwhelm mode gives three steps:** Three lines and a parking spot, with no questions. Urgent tasks that unblock others go to the top.
- **A reply line at the end:** Shows you how to reply in one word.

I left out "5 whys" and "Is there anything else?" prompts because both invite another round of rambling. I also skipped asking one question per message to save turns, and kept trade-off lists for the work itself rather than the mirror.

## How I tested it

I ran seven test inputs through the old and new versions side by side: a rambling voice dump, an overwhelmed dump, a clear one-line ask, a vent, a mixed request, one that names a solution, and a correction to an earlier mirror.

| Test | Version 1 | Version 2 |
| --- | --- | --- |
| Rambling dump | 225 words, two open questions | 196 words, two questions with defaults |
| Overwhelmed | 204 words, six sections and a question | 54 words, three things and a parking spot |
| Clear ask | "Go ahead?" | Just did it |
| Venting | Empty goals list | One sentence back, one question |
| Contradiction | Three open questions | Both sides named, defaults set |
| Named solution | Three open questions | Outcome first, one-pager as default |
| Correction | Whole mirror again (174 words) | What changed (54 words) |

One model, one run each, graded by me. Treat it as a sanity check.

## Use it yourself

Copy [`skills/intent-mirror/SKILL.md`](../skills/intent-mirror/SKILL.md) into whatever AI tool you use. Fill in the Handoffs table with your own tools or templates, then try it on your messiest voice note.

## Sources and credits

- **David Grove** — Clean Language: [Wikipedia](https://en.wikipedia.org/wiki/Clean_language), and [Clean Learning](https://cleanlearning.co.uk/blog/discuss/clean-language-questions).
- **William R. Miller & Stephen Rollnick** — Motivational interviewing, reflections and summaries: [UNC CFAR on summaries](https://www.med.unc.edu/cfar/2025/11/conversations-about-change-summaries).
- **Karl Wiegers** — Asking about needs, not solutions: [InformIT](https://informit.com/articles/article.aspx?p=3172445).
- **Alan Klement & Intercom** — Job stories: [Intercom](https://www.intercom.com/blog/accidentally-invented-job-stories/).
- **Fangwen Mu et al.** — ClarifyGPT: [arXiv paper](https://ar5iv.labs.arxiv.org/html/2310.10996).
- **Jesse Vincent (`obra`)** — Superpowers brainstorming skill: [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md).
- **Matt Pocock** — Grilling (`grill-me`) skill: [mattpocock/skills](https://skills.sh/mattpocock/skills/grilling).
