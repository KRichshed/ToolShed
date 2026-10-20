---
name: learning-capture
description: Turn raw material from something you attended or studied (slide photos, whiteboard shots, handwritten notes, recordings, transcripts, links) into a structured report that separates speaker quotes from your own thoughts, a concept mind map, and a sized action list with #1 marked. Use for 'turn these conference slides into notes', 'summarise this talk recording', 'organise my workshop notes', 'what are my action items from this event', or after any talk, course, webinar or book.
license: MIT
metadata:
  author: KRichshed
  version: "0.2.0"
  autonomy: "Level 1 Operator: suggests, never acts. You decide."
---

# Learning capture

Raw notes in, something you'll actually use out.

## Steps
1. **Inventory the inputs.** List every file or link and what it is. Flag anything unreadable (blurry photo, missing audio) and ask for a better copy if it matters.
2. **Extract.** Pull out text from images, transcribe audio, note speakers and timestamps. Keep direct quotes marked as quotes with who said them.
3. **Separate what was said from what you think.** Two columns in your notes: *source says* and *my reaction*. Don't blend them.
4. **Find the structure.** Group into 3-5 themes. Note where speakers agree, disagree, or leave a gap.
5. **Write the report** (1-2 pages): the point in one paragraph, then each theme with its evidence and quotes.
6. **Draw the mind map**: centre = the topic, branches = themes, leaves = specific points. Text outline is fine if no drawing tool is available.
7. **Action list**: concrete next steps, each with an owner (you, someone else) and a size (5 minutes, an afternoon, a project). Mark the one thing to do first.
8. **Offer extras**: a short share post, slide outline, flashcards or a reading list. Don't produce them unasked.

## Output

Every run produces four coordinated artefacts:

### 1. `report.md` (Synthesis)
- **Session context**: [Event / Course name], [Speaker / Author], [Date], [Topic]
- **Core premise**: [One clear paragraph explaining the single overarching idea]
- **Key themes (3–5 themes)**:
  - **Theme heading**: [Descriptive title]
  - *Source says*: "[Direct quote or grounded finding]" (Speaker, Slide/Timestamp)
  - *My reaction*: [Attendee commentary, operational context, team relevance]
  - *Gaps & open questions*: [Unresolved points or missing counterarguments]

### 2. `mind-map` (Structural Hierarchy)
A clean outline or Mermaid diagram mapping concepts from core to branch:
- **Central topic**: [Event / Workshop focus]
  - **Theme 1**: [Primary takeaway]
    - [Grounded finding A]
    - [Grounded finding B]
  - **Theme 2**: [Secondary takeaway]
    - [Grounded finding C]

### 3. `actions.md` (Prioritised Next Steps)
| Action item | Priority | Owner | Time appetite | Unblocks |
| --- | --- | --- | --- | --- |
| [Immediate task] | #1 (Start here) | You | 15 mins | [Downstream team work] |
| [Follow-up review] | #2 | You | 1 hour | [Strategy document] |
| [Delegated check] | #3 | [Colleague / Team] | Half day | [Implementation plan] |

### 4. Gaps and unverified claims
- Missing recordings, cut-off slides or illegible handwriting
- Unverified numbers or studies cited by speakers (flagged for verification)

## Handoffs

List your own destinations here so distilled learnings move directly into action:

| Signal in synthesised notes | Hand off to |
| --- | --- |
| Takeaways feel overwhelming or pull in competing directions | `intent-mirror` (for prioritising takeaways and setting one clear next step) |
| Speaker cited specific numbers, surveys or studies | `claim-to-chart` (for primary source tracing and chart generation) |
| Slide photos contain distinct visual styling to emulate | `design-system-from-notes` (for extracting palette and type tokens) |
| A lasting insight, milestone or decision worth logging permanently | Your project learning log or decision notes |
| Action items require project scoping and problem framing | Your project scoping template or task board |

If nothing fits, say so and provide the output directly. Never invent a destination to fill the line.

## Guardrails
- Paraphrase from audio, don't present it as a verbatim record. Say "unofficial notes" if you share it.
- Get permission before attributing a quote publicly.
- If a stat was cited, mark it *unchecked* (or run it through claim-to-chart).
