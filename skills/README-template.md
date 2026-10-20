# Skill page template

Copy this into `skills/<skill-name>/README.md` and fill it in. Each skill folder has two files:

- `README.md`: the page people read first. It tells them how to use the skill.
- `SKILL.md`: the instructions they give their AI tool.

## Writing rules for every skill page

- Write for someone who has never used an AI tool beyond chatting with it.
- Short sentences. One idea each.
- Explain any word a non-technical friend would ask about, or don't use it.
- Use real examples from testing, showing what went in and what came back.
- Every diagram gets an "In words" version underneath, and a title and description for screen readers.
- Put long examples and questions in click-to-open sections so the page stays short.
- Say plainly what it can't do yet.

---

# [Skill name]

**[One sentence: what it does for you, in everyday words.]**

[One line on who it's for. Link to the notes page for the story behind it.]

<details>
<summary><b>New to this? Words you'll see on this page</b></summary>

- **AI tool**: a chat app you type or talk to, like ChatGPT, Claude, Gemini or Copilot.
- **Skill**: a set of written instructions you give your AI tool so it handles one kind of job the same way every time.
- [Any other word this page uses.]

</details>

## What it does

- [What you give it]
- [What you get back]
- [The one thing that makes it different]

## How it works

[A simple diagram, written in Mermaid so GitHub draws it. Start it with `accTitle:` and `accDescr:` lines for screen readers.]

**In words:** [The same diagram as two or three sentences.]

## How to use it

### Step 1. Copy the instructions

Open [SKILL.md](SKILL.md). Click the **Copy raw file** button near the top right of the file (two overlapping squares).

### Step 2. Give them to your AI tool

[How to add a skill](../how-to-add-a-skill.md) has steps for Claude, Google Gemini and ChatGPT.

In a hurry? Start a new chat, paste the instructions in as your first message and send it. Then carry on in the next message. This works in any AI tool.

### Step 3. [What to send it]

### Step 4. [What you'll get back and what to check]

### Step 5. [How to reply or what happens next]

## What you'll get back

[One real example: what went in, what came back, and a table explaining each part.]

## More examples

[Three to five real examples in click-to-open sections. Include at least one messy or awkward input.]

## Tips

- [Three or four short tips.]

## How I tested it

[What you tried, a small results table, and an honest line on how small the test was.]

## What's next

Ideas, not promises:

- [Known gaps and planned improvements.]

## Questions

[Click-to-open answers. Always include: Which AI tools does it work with? Does it send my information anywhere? Can I change it?]

## What's in this folder

| File | What it is |
|---|---|
| README.md | This page |
| SKILL.md | The instructions you give your AI tool |
| CHECKS.md | Written Given/When/Then test cases you can run yourself |
| Notes | Why I built it and what changed |
