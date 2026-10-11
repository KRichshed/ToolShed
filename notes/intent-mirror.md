# Intent mirror: why I built it and what changed

The skill: [`skills/intent-mirror/SKILL.md`](../skills/intent-mirror/SKILL.md)

## What it does

Intent mirror sits between my brain dump and the AI doing anything with it. It reads the mess, tells me back what I want in under 200 words, then stops. Nothing gets built until I say yes.

## Why I built it

I have ADHD. My best thinking comes out sideways: voice notes, half sentences, three ideas tangled into one. That's how I think, and it's fine.

The trouble starts when I hand that mess to an AI tool. It picks the most likely meaning and runs with it, quickly and confidently. I end up with a polished draft of the wrong thing, and now I'm untangling the draft and my own thinking at once.

Working out what I mean and doing the thing are two separate jobs. I come unstuck when I try to do both at the same time. So the skill splits them. First it mirrors, and I check the mirror. Then it does the work.

## Who it's for

I built this for my ADHD brain, and it's tuned to how I work. But I work in this space, and I know accessible solutions rarely help only the people they were built for. Voice input is the classic example: an accessibility feature that makes things easier for everyone. If you're not ADHD and just want some things I know work, help yourself.

## If you came from the CWA post

I used this at Connected Women Australia's 2026 event, after feeding an AI agent a transcript recorded in my pocket and a handful of slide photos. Before it built anything, the mirror played back what I'd asked for: a public notes page and a post about the workflow. It asked three questions, including whether to name the AI tool. One short reply and we were off.

## How it evolved

Version 1 came out of a session where I built a handful of skills with an AI. It had six fixed sections (what you want, goals, constraints, ambiguities, not-asks, next step), a hard gate, a table that routed confirmed work to my other tools, and a late addition: an overwhelm mode that gives you the three things to do right now instead of a list.

The gate worked. Testing it against seven messy inputs showed me where it was slow:

- **Open questions:** it asked things like "Rough draft, or do you already have sessions to slot in?" I'd have to stop and compose answers, which is the effort the skill was meant to save.
- **Clear asks got a mirror anyway:** "turn these bullets into a Slack message" got "Got it… go ahead?" One extra round trip for nothing.
- **Venting became a ticket:** a vent got a canned "That sounds frustrating; noted as context" and an empty goals list. Technically correct and a bit cold.
- **Corrections re-sent everything:** fix one word and the whole 170-word mirror came back.
- **Overwhelm mode added structure:** six sections and a question, which is what it was meant not to do.

## What changed in version 2

I looked at how other people handle "what do you mean?": requirements engineers, counsellors, Clean Language facilitators, Jobs to Be Done, and published AI prompts and skills. I kept only what made the mirror sharper, faster or kinder.

- **Your words, not mine:** if I say "untangle", the mirror says "untangle", not "streamline". This comes from Clean Language and reflective listening. Your own words land faster and show the AI heard you.
- **Questions come with a default:** each one is a numbered either/or with a recommended pick first, so "yes" accepts the lot and "1B" changes one. Borrowed from ClarifyGPT and the Superpowers brainstorming skill.
- **Only ask what changes the work:** if both answers lead to the same draft, it's not a question. Small gaps become an "Assuming" line I can veto. In testing, most mirrors asked one question or none.
- **The need behind the solution:** if I say "make a deck", it mirrors what the deck is for and can offer a lighter option. From Karl Wiegers on requirements, and Jobs to Be Done.
- **Contradictions, said kindly:** "You want it thorough, and you want it out today." Both sides, no judgement, then a default for which one wins. From the double-sided reflection in motivational interviewing.
- **A "Heard" mode for venting:** one sentence back, then one question: what would you like to have happen, or did you just need to get it out? Both are fine.
- **Corrections show only what changed.**
- **Clear asks skip the mirror:** it only checks first when the job is costly to redo or hard to undo.
- **Overwhelm mode is three lines and a parking spot:** no questions, and anything other people are waiting on goes near the top.
- **A reply line at the end,** so I never have to work out how to answer.

What I didn't take: "5 whys" and "Is there anything else?", because both invite another round of dumping. One question per message, because it's too many turns. Options with trade-offs, because that's the work, not the mirror.

## How I tested it

Seven test inputs, run through the old and new versions side by side: a rambling voice dump, an overwhelmed dump, a clear one-line ask, a vent, a request that contradicts itself, one that names a solution, and a correction to an earlier mirror.

| Test | Version 1 | Version 2 |
|---|---|---|
| Rambling dump | 225 words, two open questions | 196 words, two questions with defaults |
| Overwhelmed | 204 words, six sections and a question | 54 words, three things and a parking spot |
| Clear ask | "Go ahead?" | Just did it |
| Venting | Empty goals list | One sentence back, one question |
| Contradiction | Three open questions | Both sides named, defaults set |
| Named solution | Three open questions | Outcome first, one-pager as default |
| Correction | Whole mirror again (174 words) | What changed (54 words) |

One model, one run each, graded by me. Treat it as a sanity check.

## Use it yourself

Copy `SKILL.md` into whatever AI tool you use. Fill in the handoffs section with your own destinations: your doc template, your writing skill, or "just draft it here". Then try it on your messiest voice note.

## Sources

- Clean Language: [Wikipedia](https://en.wikipedia.org/wiki/Clean_language), [Clean Learning](https://cleanlearning.co.uk/blog/discuss/clean-language-questions)
- Motivational interviewing, reflections and summaries: [UW CHAMP OARS guide](https://champ.psychiatry.uw.edu/wp-content/uploads/2023/10/MI-OARS100523.pdf), [UNC CFAR on summaries](https://www.med.unc.edu/cfar/2025/11/conversations-about-change-summaries)
- Karl Wiegers on asking about needs, not solutions: [InformIT](https://informit.com/articles/article.aspx?p=3172445)
- Job stories: [Intercom](https://www.intercom.com/blog/accidentally-invented-job-stories/)
- ClarifyGPT: [paper](https://ar5iv.labs.arxiv.org/html/2310.10996)
- Superpowers brainstorming skill: [obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)
