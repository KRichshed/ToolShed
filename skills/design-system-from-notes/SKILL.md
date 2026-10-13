---
name: design-system-from-notes
description: Lift a colour and type pairing off a real photo, slide or screenshot, write it down as a small reusable design system, then apply it consistently to everything built afterwards. Use when someone has a source image (slide photo, brand sheet, event signage) and wants matching visuals, or says "make it look like this".
---

# Design system from notes

Turn one real visual reference into a mini design system so everything you make afterwards looks like it belongs together.

## When to use
- You have a photo, slide, screenshot or brand sheet and want new material to match it.
- You're making several assets (carousel, charts, one-pagers) and they keep drifting apart.

## Steps
1. **Look at the source.** Name what you can actually see: background, text colour, one or two accent colours, heading font style, body font style, any repeated shapes or spacing habits.
2. **Pick values, say how sure you are.** From a photo you can only estimate hex values and fonts. Mark each as *measured* (given by the user or a file), *estimated* (read off an image) or *substitute* (a free font close to the original). Never claim an exact match you can't verify.
3. **Write the mini system.** Keep it to one screen:
   - Colours: background, text, muted text, 1-2 accents, plus a "do not use" note
   - Type: heading, body, sizes for small / medium / large
   - Shape and spacing: corner radius, padding, grid, border style
   - Voice of the visuals: three adjectives
4. **Check legibility.** Text on every background pair needs enough contrast (aim for WCAG AA: 4.5:1 for body, 3:1 for large text). Fix the pair, not the rule.
5. **Save it as a file** (`design-system.md` or tokens in your tool's format) and reference it at the top of every later task.
6. **Apply, don't reinvent.** For each new asset, use only the saved values. If something is missing, add it to the system first, then use it.

## Output
- `design-system.md` with the values, their confidence labels and a contrast table
- One sample tile showing the palette and type, so the person can confirm it looks right before you build more

## Guardrails
- Don't copy someone else's logo, artwork or distinctive mascots. Take colour and type feel, not protected marks.
- Ask the person to confirm the sample before building a large set.
- If the source image is blurry or has odd lighting, say so and ask for a better one or a hex code.
