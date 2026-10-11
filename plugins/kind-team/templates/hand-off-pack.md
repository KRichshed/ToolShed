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

## Tips

- **Put tool output in the pack.** A role ranks findings better when it can see what a checker found.
- **Say what done means in numbers where you can.** "Looks good" can't be checked.
- **Never put real keys, passwords or other people's details in a pack.**
- **Roles never need your logins.** If one asks for a password or a key, don't give it.
