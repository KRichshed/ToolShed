# Motion designer: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Nothing here was read directly from its source. No standards site was opened while writing this role. Every row is "from memory" and says so. Where a number is the role's judgement, the row says that too. Treat every row as a lead and check the current page before relying on it.

## The standard or guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| WCAG 2.2 is a W3C Recommendation, published in October 2023 | From memory, 2026-10-11 | https://www.w3.org/TR/WCAG22/ (check the current page) |
| 2.2.2 Pause, Stop, Hide (level A). Moving, blinking or scrolling information that starts automatically, lasts more than five seconds and is shown with other content needs a way to pause, stop or hide it, unless it is essential. The exact wording was not checked | From memory, 2026-10-11 | https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html (check the current page) |
| 2.3.1 Three Flashes or Below Threshold (level A). Nothing flashes more than three times in any one second, or the flash is below the defined thresholds | From memory, 2026-10-11 | https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html (check the current page) |
| 2.3.3 Animation from Interactions (level AAA). Motion animation triggered by an interaction can be turned off, unless it is essential. Level AAA, so not part of the usual AA target | From memory, 2026-10-11 | https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html (check the current page) |
| The `prefers-reduced-motion` media query lets a page detect that the person asked their device for less movement. Its values are `no-preference` and `reduce` | From memory, 2026-10-11 | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion (check the current page) |
| Animating `transform` and `opacity` is usually cheaper than animating layout properties such as `width`, `height`, `top` and `left`, because the browser can often skip redoing layout | From memory, 2026-10-11. Browser behaviour changes, so check the current page | Search for "browser rendering performance animations" on MDN or web.dev |
| At 60 frames a second each frame has about 16.7 milliseconds | Arithmetic (1000 divided by 60), not a source. Screens at other refresh rates have a different budget, and the browser uses part of each frame | none |
| Timing ranges of roughly 100 to 200 ms for a tiny acknowledgement, 200 to 300 ms for a small change and 300 to 500 ms for a larger one | **No authoritative source read.** The role's judgement from common design practice. Published guides differ | none |
| Ease-out for arriving, ease-in for leaving | **No single source.** Common practice, the role's judgement | none |
| Some people with vestibular disorders feel dizzy or unwell from on-screen movement | From memory, 2026-10-11 | https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html (check the current page) |

## What tools can and can't find

Automated accessibility checkers can sometimes spot missing reduced-motion rules or auto-playing media, but they cannot judge whether a movement has a purpose, whether it flashes too fast, or how it feels. Browser developer tools can record how a page performs while it animates, which is how a real frame rate is found. No reliable figure for how much these tools find was seen, so the role gives none. Any result is "found by a tool" with the tool and date.

## Free tools a beginner can use

- The performance recording panel in a browser's built-in developer tools. Not load-tested here. Search for the browser's name and "performance panel".
- The reduce-motion setting in the device's own accessibility settings, to see what still moves. The menu name varies by device and version. Check the current menu.
- A free photosensitivity analyser for flashing is a hand-off to the accessibility specialist. None was tried here.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Some places require websites to meet WCAG at a certain level, and which level differs by place and by who runs the site. No regional source was read. The role never says anything is compliant.

## Gap to close before this role is Ready

- Read WCAG 2.2 criteria 2.2.2, 2.3.1 and 2.3.3 and their Understanding pages directly, and confirm the wording and levels.
- Read the MDN page for `prefers-reduced-motion` directly and note its date.
- Find a rendering-performance page from a browser vendor and read it directly for the transform and opacity claim.
- Find an authoritative source for duration and easing ranges, or keep them labelled as judgement.
- Try a real performance recording in a browser and record the tool and date.
