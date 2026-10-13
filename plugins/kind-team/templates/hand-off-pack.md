# Hand-off pack

Use this when you want a kind team role to review or check something. Fill in all four parts. A role that gets a pack with a part missing will ask for that one part before doing anything.

Copy the block below into the chat, after naming the role, for example: "Use the kind-accessibility-specialist skill."

```
Hand-off pack.

Ticket: <one sentence: what you want checked or made>

Files to read:
- <path or pasted text>
- <path or pasted text>
- <any tool output you already have, such as a checker's results>
- <every file a check depends on, such as the styles>

What done means:
- <something you can count or tick, for example: no Blocker or Fix before launch findings in the keyboard and form checks>
- <a target number if there is one, for example: text contrast of 7 to 1>

What not to touch:
- <for a review, usually: everything. The role only reads>
```

## What you get back

The role replies with the outcome first, then its top three findings. Each finding has a severity (Blocker, Fix before launch, Nice to fix, or Paper tiger) and a label (checked, found by a tool, or my judgement). Smaller findings are parked in one line each. It ends by saying what it could not check, and one next step.

## A small example

```
Hand-off pack.

Ticket: Check the sign-up form for problems that would stop someone using it.

Files to read:
- The form's HTML and CSS, pasted below.

What done means:
- No Blocker findings.
- Every field can be reached and used with the keyboard alone.

What not to touch:
- Everything. This is a read-only review.
```

## Deliverable and ticket update note

When a role completes a review or task, it leaves a clean, copy-pasteable note formatted for your GitHub issue, pull request or project board card:

```markdown
### 📋 Ticket Update · [Role Name] · [Date]
- **Target:** [What was checked or built]
- **Status:** [Ready | Blocker Found | Needs Revision]
- **Top Findings:**
  1. [Blocker | Fix before launch | Nice to fix] [Label]: [Summary and fix]
  2. ...
- **Parked:** [1-line summary of smaller items deferred to prevent overwhelm]
- **Audit Handoff:** [Next Auditor Role] (Hand-off pack attached below)
```

## Inter-skill audit circuits

Skills do not work in isolation. When one role finishes drafting, it recommends and pre-fills an Audit Hand-Off Pack for its reviewing counterpart:

| Primary Working Role | Recommended Auditor Role | Audit Criteria ("What Done Means") |
| :--- | :--- | :--- |
| **`kind-ux-designer`** | `kind-accessibility-specialist` | Keyboard tab order, no modal traps, screen reader landmarks. |
| **`kind-ui-designer`** | `kind-accessibility-specialist` + `kind-mobile-designer` | 4.5:1 text contrast, 3:1 boundary contrast, 44px tap targets, 320px reflow. |
| **`kind-motion-designer`** | `kind-accessibility-specialist` + `kind-qa-tester` | `prefers-reduced-motion` compliance, vestibular safety, 16.7ms frame stability. |
| **`kind-solution-architect`** | `kind-security-specialist` + `kind-red-team` | Zero hardcoded keys, explicit trust boundaries, pre-mortem failure mode catalogue. |
| **`kind-marketing-comms`** | `claim-to-chart` + `kind-content-designer` | All cited metrics traced to primary source; no hyperbole; Australian spelling. |
| **`kind-content-designer`** | `kind-accessibility-specialist` | Plain language grade level <= 8, descriptive link text, alt text presence. |
| **`intent-mirror`** | `kind-chief-of-staff` | Confirmed intent routes directly into a 3-role starting crew card. |

## Tips

- **Put tool output in the pack.** A role ranks findings better when it can see what a checker found.
- **Say what done means in numbers where you can.** "Looks good" can't be checked.
- **Never put real keys, passwords or other people's details in a pack.**
- **Roles never need your logins.** If one asks for a password or a key, don't give it.

