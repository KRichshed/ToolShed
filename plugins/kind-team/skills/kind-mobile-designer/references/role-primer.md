# Mobile designer: role primer

As of 2026-10-12. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Nothing here was read directly from its source. No standards site or vendor specification was opened while writing this role primer. Every row is from memory or is the role's own judgement, and the status column says which. Treat every row as a lead and check the current page before quoting any of it.

## The standard or guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| WCAG 2.2 Criterion 2.5.8 Target Size (Minimum) (Level AA): interactive targets are at least 24 by 24 CSS pixels, or have sufficient spacing to clear a 24-pixel diameter circle | From memory, 2026-10-12. Not opened | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html |
| WCAG 2.2 Criterion 2.5.5 Target Size (Enhanced) (Level AAA): interactive targets are at least 44 by 44 CSS pixels, with limited exceptions | From memory, 2026-10-12. Not opened | https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html |
| Apple Human Interface Guidelines: minimum touch target size of 44 by 44 points for touchable controls on iOS and iPadOS | From memory, 2026-10-12. Not opened | https://developer.apple.com/design/human-interface-guidelines/ |
| Google Material Design (M3): minimum touch target size of 48 by 48 density-independent pixels (dp), with at least 8dp spacing between targets | From memory, 2026-10-12. Not opened | https://m3.material.io/foundations/accessible-design/accessibility-basics |
| WCAG 2.2 Criterion 1.4.10 Reflow (Level AA): content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions at a width equivalent to 320 CSS pixels | From memory, 2026-10-12. Not opened | https://www.w3.org/WAI/WCAG22/Understanding/reflow.html |
| Thumb zone ergonomics: research on how people hold and manipulate mobile phones, showing roughly 75% of touches rely on one thumb, dividing screens into natural, stretch, and hard reach areas | From memory, 2026-10-12. Not opened | Steven Hoober, Designing for Touch (UXmatters / A List Apart) |
| Dynamic Viewport Units (`dvh`, `svh`, `lvh`) in CSS Values and Units Module Level 4: introduced to resolve mobile browser address bar expansion and collapse issues seen with `100vh` | From memory, 2026-10-12. Not opened | https://www.w3.org/TR/css-values-4/#viewport-relative-lengths |
| iOS Safari automatic zoom behaviour: form inputs with a `font-size` below 16px trigger page auto-zooming on focus | From memory, 2026-10-12. Not opened | WebKit Safari documentation / standard web development practice |
| Responsive breakpoints at 320px, 375px, 768px, and 1280px as standard viewport tiers | Common industry practice, the role's judgement | none |

## What tools can and can't find

Automated tools such as Lighthouse, axe-core, or browser CSS checkers can flag viewport meta tags, compute layout overflow, and detect touch targets smaller than specified CSS boundaries in headless viewports. However, automated tools cannot test physical hand ergonomics, one-handed thumb strain, how sticky bars interact with virtual keyboards on real hardware, or how comfortably a person can hold and use a device. No reliable percentage for what automated tools catch on mobile layouts exists, so the role gives none. Any tool finding must be labelled "found by a tool" with the tool and date.

## Free tools a beginner can use

- Responsive Design Mode in desktop browsers (Firefox, Chrome, Safari, Edge). Free and built-in. Lets you test viewports at 320px, 375px, and custom widths, and simulate touch events. Not load-tested here.
- Device remote debugging via USB (Safari Web Inspector for iOS, Chrome DevTools for Android). Free and built-in to browser engines. Not load-tested here.
- Browser zoom and viewport testing (Cmd/Ctrl + Minus/Plus, or resizing the browser window down to 320px). No installation needed.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Several jurisdictions mandate web accessibility standards that include mobile-relevant criteria from WCAG 2.1 or 2.2 AA (such as Reflow 1.4.10 and Target Size Minimum 2.5.8), including the European Accessibility Act, Section 508 in the United States, and the Disability Discrimination Act in Australia. No legal text was read directly. The role never promises that any design is legally compliant.

## Gap to close before this role is Ready

- Read WCAG 2.2 criteria 1.4.10, 2.5.5, and 2.5.8 directly on w3.org and confirm the exact wording, levels, and spacing calculation rules.
- Read the Apple Human Interface Guidelines and Google Material Design 3 touch target sections directly and note their current wording.
- Read W3C CSS Values and Units Module Level 4 directly for dynamic viewport units (`dvh`, `svh`, `lvh`) browser support and fallback patterns.
- Read Steven Hoober's published research papers on touch ergonomics directly and verify touch percentage data.
- Test a sample mobile layout in Safari Web Inspector and Chrome DevTools and record the tool and date.
