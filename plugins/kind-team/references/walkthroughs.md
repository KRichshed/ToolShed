# Kind Team & Superpowers Reference Walkthroughs: End-to-End Circuits for Non-Technical Creators

## 1. Overview & Architectural Foundations

### 1.1 Purpose of this Reference Guide
This document provides three complete, end-to-end reference walkthroughs demonstrating how the **Kind Team** human-centred collaboration system and **Superpowers** engineering disciplines work together in practice.

Every walkthrough illustrates the complete collaborative circuit for a non-technical creator:
1. **Creator Prompt**: An authentic, plain-English request from someone building a real project.
2. **Mission Preview Card**: A transparent "trip meter" produced by `kind-chief-of-staff` estimating crew, effort, turns, time, token tier, and reversibility before any work begins.
3. **Human Checkpoint Confirmation**: An explicit pause asking *"Shall we start?"* enforcing Level 1 Operator boundaries.
4. **Project Card & Implementation Plan Mapping**: Translation from product appetite and `Given / When / Then` acceptance criteria (including unhappy paths) into right-sized engineering tasks (`superpowers:writing-plans`).
5. **Draft Implementation**: Clean, accessible, minimal code and artefacts produced by specialist roles.
6. **Stage 1 Spec Review Gate**: A 4-part Hand-Off Pack evaluated by `kind-accessibility-specialist` (or interaction specialist) checking interface compliance.
7. **Severity & Attribution Findings**: Review outcomes classified under the 4-tier severity scale (`Blocker`, `Fix before launch`, `Nice to fix`, `Paper tiger`) and 3-label attribution scale (`[checked]`, `[found by a tool]`, `[my judgement]`).
8. **Stage 2 Code Quality & Security Gate**: A 4-part Hand-Off Pack evaluated by `kind-qa-tester`, `kind-security-specialist`, or `kind-red-team`.
9. **Verification-Before-Completion Gate**: The uncompromising 4-step gate (Identify, Run, Read, Verify) with verbatim terminal evidence and exit codes.
10. **Ticket Update Note & Learning Log Entry**: A copy-pasteable status note for project tracking and a reflective learning log entry.

### 1.2 The Three Calibrated Scenarios
To cover the full spectrum of software creation, the walkthroughs span three distinct sizes and domains:

| Walkthrough | Effort Tier | Duration | Context Tier | Domain & Deliverable | Starting Crew |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Walkthrough 1 (Small)** | Small (1–2 turns) | ~5–10 mins | Light (<15k tokens) | Single-page accessible contact form with validation & spam honeypot | `kind-product-manager` ──▶ `kind-accessibility-specialist` |
| **Walkthrough 2 (Medium)** | Medium (3–6 turns) | ~15–30 mins | Moderate (15k–50k tokens) | Design token extraction from rough notes & mobile button component audit | `kind-ui-designer` ──▶ `kind-accessibility-specialist` ──▶ `kind-mobile-designer` |
| **Walkthrough 3 (Large)** | Large (7+ turns) | ~45–90 mins | Deep (50k+ tokens) | Pre-launch open-source repository privacy, secrets & hygiene audit | `kind-red-team` ──▶ `kind-security-specialist` ──▶ `kind-archivist` |

### 1.3 Core Operating Principles
- **Tool-Agnostic & Zero AI Attribution**: All workflows use standard POSIX commands, standard Git, HTML/CSS/JavaScript, and Markdown. No third-party AI attribution tags (`Co-Authored-By`), marketing footers, or session links are permitted.
- **Level 1 Operator Autonomy**: Automated roles suggest and prepare; they never push commits, deploy code, or execute destructive commands without explicit human sign-off.
- **Australian English Standards**: All documentation, notes, and user-facing copy strictly use Australian English (`colour`, `prioritise`, `categorise`, `judgement`, `artefact`, `rigour`, `centre`, `defence`).
- **Cognitive Overwhelm Shields**: At most 3 active roles in the crew; at most 3 actionable findings presented at once; technical jargon explained once in plain English.

---

## 2. Walkthrough 1 (Small): Single-Page Accessible Contact Form with Validation

### 2.1 The Scenario & Creator Prompt
**Context**: A community pottery studio in Castlemaine, Victoria, runs a static website. The studio organiser needs a simple contact form so prospective students can send enquiries. The organiser has never coded before, wants to make sure people using screen readers or keyboards can use the form, and wants to prevent automated spambots without forcing visitors to solve annoying puzzles.

#### Creator Prompt (Turn 1)
```text
I run a small community pottery club website. I need to add a simple contact form
with name, email, and message fields, plus some basic validation. I really want to
make sure anyone using a screen reader or keyboard can submit it easily, and I'd
like to stop spambots without those annoying image puzzles. I'm not a programmer.
Who on the kind team should help, and how do we do this?
```

---

### 2.2 Chief of Staff Mission Preview Card
`kind-chief-of-staff` intercepts the prompt, evaluates the scope against sizing heuristics, selects a minimal 2-role crew, and presents a transparent Mission Preview card.

```markdown
### 🧭 Mission Preview · Accessible Contact Form
- **Crew:** kind-product-manager ──▶ kind-accessibility-specialist
- **Effort Scope:** Small (1–2 turns)
- **Time & Turns:** 2 turns · ~5–10 mins of your time
- **Context Tier:** Light (<15k tokens) · a quick read of 1–2 form files
- **Safety & Reversibility:** Level 1 Operator · Suggests only · Nothing committed or pushed without human sign-off · Easily undoable

#### Flow
kind-product-manager (Define form fields & validation rules) ──▶ kind-accessibility-specialist (Audit keyboard tab order & label associations) ──▶ You (Review & Sign-off)
- **Done means:** All 3 form inputs have explicit visual and aria labels; form submits and surfaces validation errors with keyboard alone; zero Blocker findings.

Parked: kind-security-specialist (server spam defence for later), kind-ui-designer (custom brand styling)

Shall we start? (Reply "yes", suggest changes, or say "just tell me" for a direct answer)
```

---

### 2.3 Human Checkpoint Confirmation
The creator reviews the estimated time and crew, and confirms sign-off.

#### Creator Response
```text
Yes, that sounds great! Let's start.
```

---

### 2.4 Project Card & Implementation Plan Mapping

#### Step A: Kind Team Project Card (`kind-product-manager`)
`kind-product-manager` scopes the deliverable and records the project card:

```markdown
Project card · 2026-10-13

Making: Single-page accessible contact form with client-side validation and honeypot spam defence
For: Pottery studio visitors sending enquiries, including keyboard and screen reader users
Size: Small (single component)
Time it's worth: 2 hours maximum
Starting from: Existing static HTML site template in index.html
Tools: Vanilla HTML5, CSS3, JavaScript, Vitest
Region: Australia (Australian Privacy Principles, Australian English)
How you like to work: Step by step, explain new terms once, plain English

Starting crew
| Role | Why now | Teaching level |
| kind-product-manager | Scopes acceptance criteria and protects appetite | Show me |
| kind-accessibility-specialist | Audits keyboard navigation, focus, and screen reader labels | Show me |

Building blocks
1. Accessible HTML form structure · done when passes WCAG 2.1 AA keyboard and label checks · kind-accessibility-specialist
2. Client validation with honeypot · done when invalid inputs and spambots are trapped safely · kind-accessibility-specialist

Parked: Server-side database integration, recaptcha widgets, file attachments
Next step: Review acceptance criteria and generate implementation plan
```

#### Step B: Acceptance Criteria (Given / When / Then)
`kind-product-manager` formulates acceptance criteria covering both happy and unhappy paths:
- **Happy Path**:
  - `Given` a user enters valid name, email (`student@example.com.au`), and message,
  - `When` they click Submit or press Enter on the submit button,
  - `Then` the form validates successfully and displays an accessible confirmation message.
- **Unhappy Path 1 (Missing Fields)**:
  - `Given` any required field is empty or whitespace-only,
  - `When` submission is attempted,
  - `Then` submission halts, focus moves to the first invalid input, and an inline error message linked via `aria-describedby` is announced.
- **Unhappy Path 2 (Malformed Email)**:
  - `Given` a user types `invalid-email-address` in the email input,
  - `When` focus leaves the field or submit is pressed,
  - `Then` an error message reads "Please enter a valid email address (e.g. name@example.com.au)".
- **Unhappy Path 3 (Spambot Trap)**:
  - `Given` an automated bot fills in the hidden `website_hp` honeypot field,
  - `When` the form is submitted,
  - `Then` the submission is discarded quietly without error or sending mail.

#### Step C: Superpowers Implementation Plan Mapping
The project card translates into a structured `superpowers:writing-plans` specification:

```markdown
# Accessible Contact Form Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a lightweight, single-page contact form with semantic markup, client validation, and an invisible spam honeypot.
**Architecture:** Semantic HTML5 form controls; CSS custom properties for high-contrast focus rings; vanilla JavaScript validation module; JSDOM test harness.
**Tech Stack:** HTML5, CSS3, JavaScript (ES2022), Vitest.
**Spec:** `plugins/kind-team/references/walkthroughs.md` § 2.4

## Global Constraints
- Level 1 Operator boundaries apply: suggest and prepare only; no automated git commits or pushes without human sign-off.
- 100% tool-agnostic: zero AI attribution trailers or "Generated with" footers.
- Strict Australian English spelling in all user-facing strings (`enquiry`, `programme`, `centre`).
- File boundaries: work strictly within `src/contact/` and `tests/contact/`.
- Accessibility baseline: WCAG 2.1 AA (contrast >= 4.5:1, visible focus ring >= 3:1, explicit `<label>` tags).

## Review Focus
1. Keyboard accessibility: all inputs and buttons reachable and operable via Tab, Shift+Tab, and Enter.
2. Screen reader announcements: error messages connected via `aria-describedby` and `aria-live="polite"`.
3. Honeypot invisibility: honeypot field hidden from assistive tech (`tabindex="-1"`, `aria-hidden="true"`).
4. Unhappy paths: empty submission, malformed email, and honeypot tripping handled gracefully.
5. Contrast & Zoom: focus indicators clearly visible at 200% zoom and against background colours.

## Tasks

### Task 1: Semantic Accessible Form Markup
- [ ] Write failing test in `tests/contact/form-markup.test.js` asserting form controls have matching `<label for="...">` elements and submit button has discernible text.
- [ ] Run test to verify failure: `npx vitest run tests/contact/form-markup.test.js` (fails as expected).
- [ ] Implement semantic HTML in `src/contact/form.html`.
- [ ] Run test to verify pass: `npx vitest run tests/contact/form-markup.test.js` (exit code 0).
- [ ] Execute Stage 1 Spec Review Gate (`kind-accessibility-specialist` Hand-Off Pack).

### Task 2: Client-Side Validation and Honeypot Defence
- [ ] Write failing test in `tests/contact/validation.test.js` covering valid submit, empty field focus, invalid email syntax, and honeypot silent rejection.
- [ ] Run test to verify failure: `npx vitest run tests/contact/validation.test.js` (fails as expected).
- [ ] Implement validation logic in `src/contact/validator.js` and styles in `src/contact/styles.css`.
- [ ] Run test to verify pass: `npx vitest run tests/contact/validation.test.js` (exit code 0).
- [ ] Execute Stage 2 Code Quality Gate (`kind-security-specialist` Hand-Off Pack).

## Deferred & Out-of-Scope
- Backend email dispatch microservice.
- Cloud database submission logging.
- Third-party analytics trackers.
```

---

### 2.5 Draft Implementation

#### File: `src/contact/form.html`
```html
<section class="contact-card" aria-labelledby="contact-heading">
  <h2 id="contact-heading">Send us an enquiry</h2>
  <p id="form-instructions">All fields marked with an asterisk (<span aria-hidden="true">*</span>) are required.</p>

  <form id="contact-form" action="/enquiry" method="POST" novalidate>
    <!-- Invisible Honeypot Spam Trap: Hidden from sighted users and screen readers -->
    <div class="hp-wrapper" aria-hidden="true">
      <label for="pottery-website-hp">Leave this field blank</label>
      <input type="text" id="pottery-website-hp" name="website_hp" tabindex="-1" autocomplete="off">
    </div>

    <!-- Name Field -->
    <div class="form-group">
      <label for="contact-name">Your Name <span class="required" aria-hidden="true">*</span></label>
      <input type="text" id="contact-name" name="name" required autocomplete="name" aria-describedby="name-error">
      <p id="name-error" class="error-message" role="alert" aria-live="polite"></p>
    </div>

    <!-- Email Field -->
    <div class="form-group">
      <label for="contact-email">Email Address <span class="required" aria-hidden="true">*</span></label>
      <input type="email" id="contact-email" name="email" required autocomplete="email" aria-describedby="email-error">
      <p id="email-error" class="error-message" role="alert" aria-live="polite"></p>
    </div>

    <!-- Message Field -->
    <div class="form-group">
      <label for="contact-message">Message <span class="required" aria-hidden="true">*</span></label>
      <textarea id="contact-message" name="message" rows="5" required aria-describedby="message-error"></textarea>
      <p id="message-error" class="error-message" role="alert" aria-live="polite"></p>
    </div>

    <div class="form-actions">
      <button type="submit" id="submit-btn" class="btn-primary">Send Enquiry</button>
    </div>

    <div id="status-message" class="status-banner" role="status" aria-live="polite"></div>
  </form>
</section>
```

#### File: `src/contact/styles.css`
```css
/* Accessible High-Contrast Form Styles */
:root {
  --colour-bg: #FFFFFF;
  --colour-text: #212529;
  --colour-primary: #8C4320; /* Terracotta brand colour (WCAG AA: 5.8:1 on white) */
  --colour-primary-hover: #6D3418;
  --colour-error: #B02A37;   /* Accessible red (WCAG AA: 4.8:1 on white) */
  --colour-focus: #005A9C;   /* High-contrast focus blue (WCAG AA: 7.2:1 on white) */
  --colour-border: #6C757D;
}

.contact-card {
  max-width: 540px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: var(--colour-bg);
  color: var(--colour-text);
  border: 1px solid var(--colour-border);
  border-radius: 8px;
}

.hp-wrapper {
  position: absolute;
  left: -9999px;
  width: 1px;
  height: 1px;
  overflow: hidden;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--colour-text);
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1.5px solid var(--colour-border);
  border-radius: 4px;
  box-sizing: border-box;
}

/* Explicit high-visibility focus indicator */
input:focus-visible,
textarea:focus-visible,
button:focus-visible {
  outline: 3px solid var(--colour-focus);
  outline-offset: 2px;
}

.error-message {
  color: var(--colour-error);
  font-size: 0.875rem;
  margin-top: 0.35rem;
  min-height: 1.25rem;
  font-weight: 500;
}

.btn-primary {
  background-color: var(--colour-primary);
  color: #FFFFFF;
  padding: 0.85rem 1.75rem;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: var(--colour-primary-hover);
}
```

#### File: `src/contact/validator.js`
```javascript
// Lightweight, accessible client-side form validator
export function initialiseContactForm(formElement) {
  if (!formElement) return;

  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  formElement.addEventListener('submit', (event) => {
    event.preventDefault();
    clearErrors(formElement);

    const honeypot = formElement.querySelector('#pottery-website-hp');
    if (honeypot && honeypot.value.trim() !== '') {
      // Quietly reject spambots without processing or throwing errors
      displayStatus(formElement, 'Thank you for your enquiry. We will respond shortly.', 'success');
      formElement.reset();
      return;
    }

    const nameInput = formElement.querySelector('#contact-name');
    const emailInput = formElement.querySelector('#contact-email');
    const messageInput = formElement.querySelector('#contact-message');

    let firstErrorField = null;

    if (!nameInput.value.trim()) {
      showError(nameInput, 'name-error', 'Please enter your name.');
      firstErrorField = firstErrorField || nameInput;
    }

    if (!emailInput.value.trim()) {
      showError(emailInput, 'email-error', 'Please enter your email address.');
      firstErrorField = firstErrorField || emailInput;
    } else if (!emailRegex.test(emailInput.value.trim())) {
      showError(emailInput, 'email-error', 'Please enter a valid email address (e.g. name@example.com.au).');
      firstErrorField = firstErrorField || emailInput;
    }

    if (!messageInput.value.trim()) {
      showError(messageInput, 'message-error', 'Please enter your message.');
      firstErrorField = firstErrorField || messageInput;
    }

    if (firstErrorField) {
      firstErrorField.focus();
    } else {
      displayStatus(formElement, 'Thank you! Your enquiry has been received.', 'success');
      formElement.reset();
    }
  });
}

function showError(inputElement, errorElementId, message) {
  inputElement.setAttribute('aria-invalid', 'true');
  const errorElement = document.getElementById(errorElementId);
  if (errorElement) {
    errorElement.textContent = message;
  }
}

function clearErrors(formElement) {
  const inputs = formElement.querySelectorAll('input, textarea');
  inputs.forEach((input) => input.removeAttribute('aria-invalid'));
  const errorParagraphs = formElement.querySelectorAll('.error-message');
  errorParagraphs.forEach((p) => { p.textContent = ''; });
}

function displayStatus(formElement, message, type) {
  const statusBanner = formElement.querySelector('#status-message');
  if (statusBanner) {
    statusBanner.textContent = message;
    statusBanner.className = `status-banner status-${type}`;
  }
}
```

---

### 2.6 Stage 1 Spec Review Gate (`kind-accessibility-specialist`)

#### Hand-Off Pack
```markdown
Hand-off pack.

Ticket: Review contact form markup and styling for WCAG 2.1 AA keyboard, label, and focus compliance.

Files to read:
- src/contact/form.html
- src/contact/styles.css
- src/contact/validator.js

What done means:
- 0 Blocker findings and 0 Fix before launch findings.
- Every form field reachable and operable with keyboard alone.
- Visible focus rings with at least 3:1 contrast against adjacent background.
- Error messages explicitly associated with inputs via `aria-describedby`.
- Honeypot safely excluded from tab navigation and screen reader accessibility tree.

What not to touch:
- Everything. This is a read-only review.
```

#### Stage 1 Review Findings
`kind-accessibility-specialist` inspects the implementation:

1. **`[Fix before launch]` `[checked]`**: Error message containers initially lacked the `aria-live="polite"` attribute, preventing immediate auditory announcement in certain screen readers upon submission.
   - *Fix applied*: Added `aria-live="polite"` and `role="alert"` directly to error text elements.
2. **`[Nice to fix]` `[checked]`**: The focus indicator outline offset was 1px; increased to 2px for improved visual separation against dark borders.
3. **`[Paper tiger]` `[found by a tool]`**: An automated static HTML linter issued a warning that `#pottery-website-hp` lacked a user-visible `<label>`.
   - *Assessment*: Safely dismissed. The field is intentionally excluded from the accessibility tree via `aria-hidden="true"` and excluded from keyboard navigation via `tabindex="-1"`.
- **Summary**: Exactly 0 Blocker and 0 Fix before launch findings remain.

---

### 2.7 Stage 2 Code Quality & Security Gate (`kind-security-specialist`)

#### Hand-Off Pack
```markdown
Hand-off pack.

Ticket: Audit contact form validation and honeypot for spam resilience and input sanitisation.

Files to read:
- src/contact/validator.js
- src/contact/form.html

What done means:
- Honeypot safely discards automated bot submissions without surfacing false errors.
- Client validation regex is safe against catastrophic backtracking (ReDoS).
- Header injection characters (`\r` and `\n`) cannot pollute email dispatch metadata.
- Zero credentials or tracking tokens hardcoded in client scripts.

What not to touch:
- Everything. This is a read-only audit.
```

#### Stage 2 Review Findings
1. **`[Fix before launch]` `[checked]`**: Client validation regex `/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/` verified safe against catastrophic backtracking. However, message textarea content should strip carriage-return/newline characters if later bound to an email Subject line.
   - *Mitigation*: Validator confirms Subject line is fixed on the server; client input safely trimmed.
2. **`[Nice to fix]` `[checked]`**: Add double-click protection (disable submit button for 3 seconds post-submit) to prevent duplicate submissions on slow mobile connections.
3. **`[Paper tiger]` `[found by a tool]`**: Scanner flagged the HTML `action="/enquiry"` attribute as an unresolved relative URL in local offline testing. Expected behaviour for standalone component prototypes.
- **Summary**: 0 Blocker and 0 Fix before launch findings remain.

---

### 2.8 Verification-Before-Completion Gate
Following the mandatory 4-step gate (Identify, Run, Read, Verify):

1. **IDENTIFY**:
   Command to execute: `npx vitest run tests/contact/` to test markup, keyboard handling, happy paths, unhappy paths, and honeypot behaviour.
2. **RUN**:
   Execute the test runner freshly in the workspace terminal.
3. **READ**:
   Inspect complete terminal output and exit code:
   ```text
    RUN  v1.6.0 /Users/kimberly/Documents/antigravity/wonderful-fermi/toolshed-staging

    ✓ tests/contact/form-markup.test.js (3 tests)
      ✓ semantic form controls have explicit label associations
      ✓ honeypot input is hidden from tab navigation and accessibility tree
      ✓ submit button contains discernible text
    ✓ tests/contact/validation.test.js (4 tests)
      ✓ valid inputs trigger success banner and reset form
      ✓ empty fields trigger inline error messages and focus first invalid input
      ✓ malformed email triggers descriptive validation error
      ✓ populated honeypot silently swallows submission without processing

    Test Files  2 passed (2)
         Tests  7 passed (7)
      Duration  218ms

   Exit code: 0
   ```
4. **VERIFY**:
   All 7 tests passed cleanly with exit code 0. Zero Blocker or Fix before launch findings. Verification criteria completely satisfied.

---

### 2.9 Deliverable Ticket Update & Learning Log Entry

#### Ticket Update Note
```markdown
### 📋 Ticket Update · kind-accessibility-specialist · 2026-10-13
- **Target:** Single-page accessible contact form (`src/contact/`)
- **Status:** Ready
- **Top Findings:**
  1. [Nice to fix] [checked]: Focus ring outline offset increased from 1px to 2px for enhanced visibility on high-resolution displays.
  2. [Nice to fix] [checked]: Added submit button debounce to prevent accidental multi-submissions.
  3. [Paper tiger] [found by a tool]: Automated checker warned on unlabeled honeypot input; verified safely marked `aria-hidden="true"` and `tabindex="-1"`.
- **Parked:** Server-side SMTP dispatch and database storage deferred to future backend sprint.
- **Audit Handoff:** Complete. All Stage 1 and Stage 2 gates verified with exit code 0.
```

#### Learning Log Entry
```markdown
## Milestone
- Date: 2026-10-13
- What shipped: Accessible contact form with client validation and bot honeypot for pottery studio site.
- For whom: Studio visitors sending enquiries, including keyboard and screen reader users.
- Evidence it worked: All 7 automated unit and accessibility tests passed (Vitest exit code 0); Tab navigation runs cleanly through all controls.

## Decision
- Date: 2026-10-13
- Role: learning log
- Context: Protecting contact form against automated spam without confusing real visitors.
- In the context of the pottery studio website, facing automated form spam, I decided to implement a hidden honeypot field, to achieve quiet bot rejection, accepting that sophisticated targeted human scrapers require backend rate limiting later.
- Options I considered: Captcha puzzle widgets, third-party cloud spam beacons, invisible honeypot field.
- Why: Honeypot creates zero friction for real users and requires zero tracking cookies.
- Confidence: 3 (could teach it)
- Revisit on: 2027-01-13

## Word
- Date: 2026-10-13
- Word: Honeypot
- What it means, in plain English: A hidden form field that real people cannot see, but automated spam robots fill in by mistake, letting us quietly ignore their spam.
- Where I met it: Building the pottery studio contact form.
```

---

## 3. Walkthrough 2 (Medium): Design Token Extraction and Component Audit from Rough Notes

### 3.1 The Scenario & Creator Prompt
**Context**: A community environmental advocacy group in New South Wales ("Solar Neighbours") wants to build a consistent web application. The volunteer coordinator has rough notes scribbled during a branding workshop, photos of a campaign banner, two hex colour codes, and some loose spacing ideas. They need to extract a reusable design system of CSS tokens (`design-system.md` and `tokens.css`) and audit mobile button components for colour contrast, tap target sizing (44x44px), and 320px viewport reflow.

#### Creator Prompt (Turn 1)
```text
I have rough notes from our community solar group's branding workshop: two brand colours
(a gumleaf green #2B6B4F and a bright wattle yellow #F4C430), charcoal text, and some
typography notes. I want to turn these into clean CSS design tokens so our pages look
consistent, and I need to make sure our mobile buttons have good contrast and are easy
to tap on phones. Who can help me turn my notes into a system and check the buttons?
```

---

### 3.2 Chief of Staff Mission Preview Card
`kind-chief-of-staff` sizes the multi-component task as Medium and configures a 3-role sequence.

```markdown
### 🧭 Mission Preview · Design Token & Mobile Button Audit
- **Crew:** kind-ui-designer ──▶ kind-accessibility-specialist ──▶ kind-mobile-designer
- **Effort Scope:** Medium (3–6 turns)
- **Time & Turns:** 3–4 turns · ~15–25 mins of your time
- **Context Tier:** Moderate (15k–50k tokens) · a couple of CSS files and button components
- **Safety & Reversibility:** Level 1 Operator · Suggests only · Nothing committed or pushed without human sign-off · Easily undoable

#### Flow
kind-ui-designer (Extract CSS tokens for palette, typography & spacing) ──▶ kind-accessibility-specialist (Audit contrast ratios) ──▶ kind-mobile-designer (Audit tap targets & 320px reflow) ──▶ You (Review & Sign-off)
- **Done means:** Clean CSS token stylesheet generated; button components achieve 4.5:1 text contrast and minimum 44px tap targets; zero Blocker findings.

Parked: kind-motion-designer (button hover micro-interactions), kind-archivist (design token documentation)

Shall we start? (Reply "yes", suggest changes, or say "just tell me" for a direct answer)
```

---

### 3.3 Human Checkpoint Confirmation
#### Creator Response
```text
Yes, let's start! I'm ready.
```

---

### 3.4 Lifting Tokens with `skills/design-system-from-notes`

#### Step A: Confidence Labelling
Applying `skills/design-system-from-notes`, the raw inputs are extracted and categorised by confidence:
- **Gumleaf Green** (`#2B6B4F`): *measured* (exact hex provided in workshop notes).
- **Wattle Yellow** (`#F4C430`): *measured* (exact hex provided in banner spec).
- **Charcoal Text** (`#22252A`): *estimated* (sampled from slide photo).
- **Canvas Off-White** (`#F8F9FA`): *estimated* (sampled from background).
- **Heading Font** ("Outfit", fallback sans-serif): *substitute* (accessible geometric font matching poster feel).
- **Body Font** ("Inter", system sans-serif): *substitute* (high legibility UI font).

#### Step B: Palette Balance & Grid Architecture
`kind-ui-designer` establishes the standard system:
1. **60-30-10 Palette Balance**:
   - 60% Canvas/Neutral: Off-white canvas (`#F8F9FA`), pure white cards (`#FFFFFF`), charcoal text (`#22252A`).
   - 30% Structural Brand: Gumleaf Green (`#2B6B4F`) for headers, primary buttons, borders.
   - 10% Focal Accent: Wattle Yellow (`#F4C430`) reserved strictly for call-to-action badges and secondary highlights.
2. **4px / 8px Spacing Grid**:
   - `4px` (`--space-1`), `8px` (`--space-2`), `16px` (`--space-3`), `24px` (`--space-4`), `32px` (`--space-5`), `48px` (`--space-6`).
3. **Five Interactive Component States**:
   - `Default`, `Hover`, `Focus`, `Active`, `Disabled`.

#### Step C: Generated `tokens.css`
```css
/* Solar Neighbours Community Design Tokens */
:root {
  /* Palette Tokens */
  --colour-canvas: #F8F9FA;
  --colour-surface: #FFFFFF;
  --colour-text-main: #22252A;
  --colour-text-muted: #5A626A;
  --colour-brand-green: #2B6B4F;
  --colour-brand-green-hover: #21523C;
  --colour-brand-green-active: #183C2C;
  --colour-accent-yellow: #F4C430;
  --colour-accent-yellow-hover: #E0B020;
  --colour-border: #DDE2E5;
  --colour-focus-ring: #005A9C;

  /* Typography Scale */
  --font-family-heading: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-family-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;      /* 16px */
  --font-size-lg: 1.25rem;     /* 20px */
  --font-size-xl: 1.75rem;     /* 28px */
  --font-weight-regular: 400;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Spacing Scale (4px/8px Grid) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 1rem;     /* 16px */
  --space-4: 1.5rem;   /* 24px */
  --space-5: 2rem;     /* 32px */
  --space-6: 3rem;     /* 48px */

  /* Radii & Elevation */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-full: 9999px;
}
```

#### Step D: Button Component Styles (`buttons.css`)
```css
/* Button Component with 5 Interactive States */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-family-body);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-md);
  padding: var(--space-2) var(--space-4);
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.15s ease, border-color 0.15s ease;
  border: 2px solid transparent;
  /* Minimum tap target boundary for touch devices */
  min-height: 44px;
  min-width: 44px;
  box-sizing: border-box;
}

/* Primary Button: Gumleaf Green with White Text */
.btn-primary {
  background-color: var(--colour-brand-green);
  color: #FFFFFF;
}
.btn-primary:hover {
  background-color: var(--colour-brand-green-hover);
}
.btn-primary:active {
  background-color: var(--colour-brand-green-active);
}
.btn-primary:focus-visible {
  outline: 3px solid var(--colour-focus-ring);
  outline-offset: 3px;
}
.btn-primary:disabled {
  background-color: #A3C2B4;
  color: #FFFFFF;
  cursor: not-allowed;
}

/* Accent Button: Wattle Yellow with Charcoal Text */
.btn-accent {
  background-color: var(--colour-accent-yellow);
  color: var(--colour-text-main); /* Strict 8.2:1 contrast */
}
.btn-accent:hover {
  background-color: var(--colour-accent-yellow-hover);
}
.btn-accent:active {
  background-color: #CC9E15;
}
.btn-accent:focus-visible {
  outline: 3px solid var(--colour-focus-ring);
  outline-offset: 3px;
}
.btn-accent:disabled {
  background-color: #F8E5A0;
  color: #7A7258;
  cursor: not-allowed;
}

/* Responsive Button Layout for 320px Reflow */
.button-group {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
}

@media (max-width: 480px) {
  .button-group {
    flex-direction: column;
    width: 100%;
  }
  .button-group .btn {
    width: 100%;
  }
}
```

---

### 3.5 Stage 1 Spec Review Gate A: Accessibility Contrast Audit (`kind-accessibility-specialist`)

#### Hand-Off Pack
```markdown
Hand-off pack.

Ticket: Audit design tokens and button component states for WCAG 2.1 AA colour contrast compliance.

Files to read:
- tokens.css
- buttons.css
- design-system.md

What done means:
- All body text and button labels achieve at least 4.5:1 contrast against adjacent background.
- Large headings achieve at least 3:1 contrast.
- Focus rings achieve at least 3:1 contrast against both component and page background.
- 0 Blocker and 0 Fix before launch findings.

What not to touch:
- Everything. This is a read-only review.
```

#### Stage 1 Review Findings (A11y)
1. **`[Blocker]` `[checked]`**: Initial draft tested Wattle Yellow background (`#F4C430`) with white text (`#FFFFFF`), yielding a disastrous contrast ratio of **1.4:1** (failing WCAG AA 4.5:1).
   - *Fix applied*: Paired Wattle Yellow buttons exclusively with Charcoal text (`#22252A`), delivering an outstanding **8.2:1** contrast ratio. White text is strictly restricted to Gumleaf Green (`#2B6B4F`), which yields **5.6:1** (fully compliant).
2. **`[Nice to fix]` `[checked]`**: Muted text token `#5A626A` measured 4.6:1 on white; acceptable for body text but close to threshold. Recommend bumping to `#4A525A` (5.8:1) for safety in outdoor mobile sunlight.
3. **`[Paper tiger]` `[found by a tool]`**: Contrast scanner reported 1.8:1 for disabled button state text.
   - *Assessment*: Dismissed. WCAG 2.1 Success Criterion 1.4.3 explicitly exempts inactive/disabled user interface controls.
- **Summary**: Contrast failure discovered and resolved. Exactly 0 Blocker and 0 Fix before launch findings remain.

---

### 3.6 Stage 1 Spec Review Gate B: Mobile Layout Audit (`kind-mobile-designer`)

#### Hand-Off Pack
```markdown
Hand-off pack.

Ticket: Audit button components for mobile touch target sizing (44x44px) and 320px viewport reflow.

Files to read:
- buttons.css
- tokens.css

What done means:
- All interactive controls have minimum computed touch target dimensions of 44x44px.
- Layout reflows cleanly down to 320px viewport width without horizontal scrollbars or truncated labels.
- Focus outline remains visible within narrow viewport boundaries.
- 0 Blocker and 0 Fix before launch findings.

What not to touch:
- Everything. This is a read-only audit.
```

#### Stage 1 Review Findings (Mobile)
1. **`[Fix before launch]` `[checked]`**: Initial button padding (`8px 16px`) produced a computed height of only 38px on standard line-heights, failing the 44px touch target minimum.
   - *Fix applied*: Added explicit `min-height: 44px; min-width: 44px; display: inline-flex; align-items: center; justify-content: center;` to `.btn`.
2. **`[Fix before launch]` `[checked]`**: Side-by-side `.button-group` caused horizontal overflow at 320px viewport width when longer button text ("Join Community Workshop") was rendered.
   - *Fix applied*: Added mobile media query at 480px collapsing `.button-group` to full-width vertical stack.
3. **`[Nice to fix]` `[checked]`**: Add `:active` scale micro-feedback (`transform: scale(0.98)`) for tactile mobile reassurance.
- **Summary**: Touch targets and 320px reflow fixed. 0 Blocker and 0 Fix before launch findings remain.

---

### 3.7 Verification-Before-Completion Gate

1. **IDENTIFY**:
   Command to execute: `npm test tests/design-tokens.test.js` checking contrast calculations, computed CSS properties, and mobile viewport assertions.
2. **RUN**:
   Execute the automated test suite freshly in the workspace terminal.
3. **READ**:
   Inspect full terminal output and verify exit code 0:
   ```text
    RUN  v1.6.0 /Users/kimberly/Documents/antigravity/wonderful-fermi/toolshed-staging

    ✓ tests/design-tokens.test.js (6 tests)
      ✓ gumleaf green with white text achieves 5.6:1 contrast (>= 4.5:1)
      ✓ wattle yellow with charcoal text achieves 8.2:1 contrast (>= 4.5:1)
      ✓ focus ring blue achieves 7.2:1 contrast against canvas
      ✓ button touch target computes to >= 44px height and >= 44px width
      ✓ 4px/8px spacing grid tokens are mathematically consistent
      ✓ button group stacks vertically below 480px viewport width

    Test Files  1 passed (1)
         Tests  6 passed (6)
      Duration  184ms

   Exit code: 0
   ```
4. **VERIFY**:
   All 6 automated checks pass with exit code 0. Both Stage 1 audit gates verified with empirical evidence.

---

### 3.8 Deliverable Ticket Update & Learning Log Entry

#### Ticket Update Note
```markdown
### 📋 Ticket Update · kind-ui-designer · 2026-10-13
- **Target:** Solar Neighbours Design Tokens and Mobile Buttons (`tokens.css`, `buttons.css`, `design-system.md`)
- **Status:** Ready
- **Top Findings:**
  1. [Blocker fixed] [checked]: Wattle Yellow button text changed from white (1.4:1 fail) to Charcoal `#22252A` (8.2:1 pass).
  2. [Fix before launch fixed] [checked]: Button min-height set to 44px to satisfy mobile tap target standards.
  3. [Fix before launch fixed] [checked]: Added 320px reflow media query so button groups stack cleanly without horizontal overflow.
- **Parked:** Dark mode theme tokens and button micro-animations deferred to subsequent design milestone.
- **Audit Handoff:** Complete. Passed accessibility and mobile design audit gates.
```

#### Learning Log Entry
```markdown
## Milestone
- Date: 2026-10-13
- What shipped: Design tokens and accessible mobile button components for Solar Neighbours.
- For whom: Community volunteers and website visitors, especially people using mobile phones and outdoors in bright sunlight.
- Evidence it worked: 6 automated tests passed (exit code 0); computed 44px touch targets; verified 8.2:1 and 5.6:1 contrast ratios.

## Decision
- Date: 2026-10-13
- Role: learning log
- Context: Yellow brand colours in web user interfaces.
- In the context of the Solar Neighbours brand system, facing low contrast when white text is placed on wattle yellow buttons, I decided to pair wattle yellow exclusively with dark charcoal text `#22252A`, to achieve WCAG AA contrast (8.2:1), accepting that white button text is reserved for gumleaf green backgrounds.
- Options I considered: Darkening wattle yellow to mustard brown, using white text anyway, pairing yellow with dark charcoal text.
- Why: Pairing yellow with charcoal keeps the cheerful brand yellow while protecting readability for everyone.
- Confidence: 3 (could teach it)
- Revisit on: 2027-04-13

## Learned
- Date: 2026-10-13
- Role: learning log
- In my own words: A button that looks bright to my eyes can still be impossible to read if the text colour is too close to the background. Contrast is maths, not guesswork.

## Word
- Date: 2026-10-13
- Word: Design token
- What it means, in plain English: A single named setting for a colour, font size, or spacing value that you save in one place so your whole website stays consistent.
- Where I met it: Extracting the Solar Neighbours brand system from workshop notes.
```

---

## 4. Walkthrough 3 (Large): Open-Source Repo Pre-Launch Privacy and Hygiene Audit

### 4.1 The Scenario & Creator Prompt
**Context**: A small non-profit research team in Canberra has built an open-source mapping application ("Bushfire Alert Visualiser NSW"). They have been working in a private Git repository for six months with local volunteers and university students. They are preparing to flip the repository visibility from Private to Public on GitHub. The project lead is anxious: did someone commit an API token or AWS secret three months ago? Are personal student emails or confidential partner names in git commit logs? Is the licence clear, and is the documentation clean?

#### Creator Prompt (Turn 1)
```text
We are about to open-source our bushfire mapping tool on GitHub. We've been working
on this privately for six months. I'm really nervous about flipping the repository from
private to public because I don't know if someone accidentally committed an API key,
a password, or personal student email addresses in the commit history months ago.
Also, we need to make sure our licence, README, and files are tidy. Can the kind team
help us do a complete pre-launch privacy and hygiene sweep?
```

---

### 4.2 Chief of Staff Mission Preview Card
`kind-chief-of-staff` assesses this architectural, repository-wide undertaking as Large (7+ turns) and outputs the Mission Preview card with Deep context guidance.

```markdown
### 🧭 Mission Preview · Pre-Launch Repo Privacy & Hygiene Audit
- **Crew:** kind-red-team ──▶ kind-security-specialist ──▶ kind-archivist
- **Effort Scope:** Large (7+ turns)
- **Time & Turns:** 7 turns · ~45–60 mins of your time
- **Context Tier:** Deep (50k+ tokens) · sweeping the whole project and git commit log
- **Safety & Reversibility:** Level 1 Operator · Suggests only · Nothing committed or pushed without human sign-off · Easily undoable

*Tip for deep scans: Saving scan reports directly to local files keeps chat memory fresh and prevents context drift.*

#### Flow
kind-red-team (Premortem failure analysis & 5-point git privacy scan) ──▶ kind-security-specialist (Secret scanning & .gitignore audit) ──▶ kind-archivist (Licence, changelog & clean file hygiene) ──▶ You (Review & Sign-off)
- **Done means:** Pre-launch privacy report generated; zero secrets detected in working tree or git history; clean public repository checklist ready for sign-off.

Parked: kind-marketing-comms (public launch announcement), kind-delivery-manager (release tagging)

Shall we start? (Reply "yes", suggest changes, or say "just tell me" for a direct answer)
```

---

### 4.3 Human Checkpoint Confirmation
#### Creator Response
```text
Yes, please! Let's make sure nothing sensitive leaks before we go public.
```

---

### 4.4 `kind-red-team` Job 1: Premortem Failure Analysis
Before scanning files, `kind-red-team` conducts a **Premortem Analysis**:
> *"Imagine it is 3 months after public launch. The open-source release has failed or caused a crisis. Why did it happen?"*

`kind-red-team` identifies the four most probable failure modes and attaches preventative mitigations:
1. **Failure Mode 1: Historical API Secret Leak**:
   - *Scenario*: A developer committed an unencrypted Mapbox access token or SendGrid key in commit `3f8a91c` four months ago. Although deleted in commit `4e12b7a`, automated scanners scrape the historical commit within seconds of the repo going public, incurring thousands of dollars in unauthorised usage.
   - *Mitigation*: Sweep entire git history (`git log -p`), not just the current working tree.
2. **Failure Mode 2: Personal & Work Email Exposure**:
   - *Scenario*: Commits contain government or university workplace email addresses (`researcher@agency.gov.au`), leading to automated spam and unwanted public enquiries.
   - *Mitigation*: Run author/committer audit and guide creator through configuring clean public pseudonyms or GitHub noreply email aliases.
3. **Failure Mode 3: Accidental Inclusion of Confidential Partner Datasets**:
   - *Scenario*: A local test folder `tests/data/` contains unanonymised landholder property coordinates or test telephone numbers.
   - *Mitigation*: Inspect all test fixtures and sample data for private identifiers.
4. **Failure Mode 4: Ambiguous or Missing Open-Source Licence**:
   - *Scenario*: Without an explicit licence, developers cannot safely contribute, and downstream emergency services cannot use the software.
   - *Mitigation*: Hand off to `kind-archivist` to establish an unambiguous MIT licence and clear contribution guidelines.

---

### 4.5 `kind-red-team` Job 2: 5-Point Git Privacy Scan

`kind-red-team` executes the standard 5-point privacy check using standard POSIX shell commands:

#### Point 1: Inspect All Branches
```bash
git branch -a
```
- **Observation**: Discovers stale branch `remotes/origin/experiment/partner-sydney-feed`.
- **Finding `[Fix before launch]` `[checked]`**: Branch contains reference to a proprietary partner staging server.
- **Action**: Advised creator to delete the experimental branch locally and remotely prior to making the repository public (`git branch -D experiment/partner-sydney-feed`).

#### Point 2: Deep Commit History Sweep
```bash
git log -p --full-history -S "AIza" -S "sk-" -S "ghp_" -S "pk_" -S "eyJh"
```
- **Observation**: Commit `3f8a91c` (dated 4 months ago) committed a test file `.env.test` containing an active Mapbox token:
  `pk.eyJ1Ijoic29sYXItdGVzdCIsImEiOiJjbHNm...`
- **Finding `[Blocker]` `[checked]`**: Leaked third-party API key in historical commit!
- **Immediate Mitigation (Kind Contract Rule)**:
  1. *Immediate Line 1 Warning*: Key is treated as compromised. Creator is instructed to log into Mapbox immediately and revoke/rotate the token before proceeding.
  2. *History Remediation Options Presented*:
     - *Option A (Recommended for Newcomers)*: Export current clean files into a fresh repository with a clean initial commit (`git init`). Preserves 100% privacy with zero complex git rebase risk.
     - *Option B (Advanced)*: Run `git-filter-repo` to purge `.env.test` from historical commits, with an explicit backup archive created first.
  - Creator chose Option A for complete safety and simplicity.

#### Point 3: Author & Committer Email Audit
```bash
git log --format='%an <%ae>' | sort -u
```
- **Observation**: Output shows:
  ```text
  Alex Turner <alex.turner@workplace.gov.au>
  Alex Turner <alex@users.noreply.github.com>
  Samira Khan <samira.k@gmail.com>
  ```
- **Finding `[Fix before launch]` `[checked]`**: Creator's institutional workplace email is visible in early commits.
- **Action**: Creator updated local git configuration:
  `git config user.name "Alex Turner"`
  `git config user.email "alex@users.noreply.github.com"`

#### Point 4: Tags and Release Annotations
```bash
git tag -l -n
```
- **Observation**: Tags `v0.1.0-alpha` and `v0.2.0-beta` inspected. Zero internal server URLs or private notes discovered. Verified clean (`[checked]`).

#### Point 5: Test Fixtures and Sample Data
```bash
find tests/fixtures -type f -exec grep -H -i "phone\|email\|address" {} +
```
- **Observation**: Sample coordinates in `tests/fixtures/synthetic-fire-perimeter.geojson` verified to be artificial synthetic boundary data in uninhabited national park land. Zero private citizen data found (`[checked]`).

---

### 4.6 Stage 2 Code Quality & Security Gate (`kind-security-specialist`)

#### Hand-Off Pack
```markdown
Hand-off pack.

Ticket: Conduct repository security hygiene audit: verify .gitignore completeness, scan for hardcoded secrets, and review dependencies.

Files to read:
- .gitignore
- package.json
- src/config/environment.js

What done means:
- Working tree contains zero uncommitted or tracked secret files (`.env`, credentials).
- `.gitignore` includes standard security patterns for node_modules, env files, and OS artefacts.
- Zero high-severity security vulnerabilities reported in dependencies.
- 0 Blocker and 0 Fix before launch findings.

What not to touch:
- Everything. This is a read-only security audit.
```

#### Stage 2 Review Findings
1. **`[Blocker]` `[checked]`**: `.gitignore` was missing patterns for `.env*.local`, `.DS_Store`, and temporary editor files (`*.swp`).
   - *Fix applied*: Updated `.gitignore` with comprehensive exclusions:
     ```text
     # Environment & Secrets
     .env
     .env.*
     !.env.example

     # Dependencies
     node_modules/
     npm-debug.log*

     # Operating System & Editors
     .DS_Store
     Thumbs.db
     *.swp
     .vscode/
     .idea/
     ```
2. **`[Fix before launch]` `[found by a tool]`**: Ran dependency vulnerability audit:
   ```bash
   npm audit --audit-level=high
   ```
   Found 1 high-severity vulnerability in an outdated transitive mapping parser library. Resolved by running `npm update` and regenerating `package-lock.json`.
3. **`[Nice to fix]` `[checked]`**: Created `env.example` documenting required environment variable names with safe placeholder values (`MAPBOX_API_KEY="your_mapbox_key_here"`).
- **Summary**: 0 Blocker and 0 Fix before launch findings remain.

---

### 4.7 Repository Hygiene Hand-Off Pack (`kind-archivist`)

#### Hand-Off Pack
```markdown
Hand-off pack.

Ticket: Prepare repository documentation, licence, changelog, and clean file structure for public release.

Files to read:
- README.md
- LICENSE
- CHANGELOG.md

What done means:
- Valid MIT licence file created with 2026 copyright notice.
- CHANGELOG.md formatted according to Keep a Changelog standards.
- README.md written in plain English with clear setup instructions and Australian spelling.
- 0 Blocker and 0 Fix before launch findings.

What not to touch:
- Source code in src/ and tests/.
```

#### Archivist Deliverables & Review Findings
1. **`[Fix before launch]` `[checked]`**: Repository had no licence file. Added standard `LICENSE` file containing the MIT Licence:
   ```text
   MIT License

   Copyright (c) 2026 Bushfire Alert Visualiser Contributors

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:
   ...
   ```
2. **`[Nice to fix]` `[checked]`**: Created `CHANGELOG.md` following the *Keep a Changelog* convention:
   ```markdown
   # Changelog
   All notable changes to this project will be documented in this file.

   The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
   and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

   ## [1.0.0] - 2026-10-13
   ### Added
   - Interactive GeoJSON bushfire perimeter rendering.
   - High-contrast map layer toggle with WCAG AA compliance.
   - Comprehensive test suite for map projection calculations.
   - Offline synthetic test fixtures.
   ```
3. **`[Nice to fix]` `[checked]`**: Tidied `README.md`, removing internal student notes and adding a 3-step Getting Started guide.
- **Summary**: Hygiene checklist complete. 0 Blocker and 0 Fix before launch findings remain.

---

### 4.8 Verification-Before-Completion Gate

1. **IDENTIFY**:
   Commands to verify clean repository status:
   - Command A: Sweep working tree and git log for any lingering secret patterns.
   - Command B: Verify git status is clean and `.gitignore` ignores `.env`.
   - Command C: Run the test suite to ensure all unit tests pass with exit code 0.
2. **RUN**:
   Execute the verification commands in the workspace terminal:
   ```bash
   # Command A: Secret pattern check
   git log -p -S "AIza" -S "sk-" -S "ghp_" -S "pk_" | wc -l

   # Command B: Git status and ignore verification
   git status --porcelain
   touch .env.test && git status --porcelain .env.test && rm .env.test

   # Command C: Full test suite run
   npm test
   ```
3. **READ**:
   Inspect complete terminal output and exit codes:
   ```text
   $ git log -p -S "AIza" -S "sk-" -S "ghp_" -S "pk_" | wc -l
   0

   $ git status --porcelain
   (clean working directory, output empty)

   $ touch .env.test && git status --porcelain .env.test && rm .env.test
   (output empty - file correctly ignored by .gitignore)

   $ npm test
    RUN  v1.6.0 /Users/kimberly/Documents/antigravity/wonderful-fermi/toolshed-staging

    ✓ tests/map-renderer.test.js (8 tests)
    ✓ tests/geojson-parser.test.js (5 tests)
    ✓ tests/synthetic-fixtures.test.js (3 tests)

    Test Files  3 passed (3)
         Tests  16 passed (16)
      Duration  412ms

   Exit code: 0
   ```
4. **VERIFY**:
   Output confirms:
   - Zero historical secrets detected (`wc -l` = 0).
   - Working tree is clean; `.env.test` is strictly ignored by `.gitignore`.
   - All 16 automated tests pass cleanly with exit code 0.
   - Verified ready for human sign-off before making repository public on GitHub.

---

### 4.9 Deliverable Ticket Update & Learning Log Entry

#### Ticket Update Note
```markdown
### 📋 Ticket Update · kind-red-team · 2026-10-13
- **Target:** Bushfire Alert Visualiser Repository Pre-Launch Privacy & Hygiene Sweep
- **Status:** Ready
- **Top Findings:**
  1. [Blocker resolved] [checked]: Revoked exposed Mapbox token from historical commit 3f8a91c; exported clean repository history for public launch.
  2. [Fix before launch resolved] [checked]: Added comprehensive `.gitignore` rules preventing `.env` and `.DS_Store` leaks.
  3. [Fix before launch resolved] [checked]: Added official MIT LICENSE file and Keep a Changelog CHANGELOG.md.
- **Parked:** Public launch announcement on social media deferred to `kind-marketing-comms` post-release.
- **Audit Handoff:** Complete. All 3 review gates verified. Repository ready for human sign-off to flip visibility to Public.
```

#### Learning Log Entry
```markdown
## Milestone
- Date: 2026-10-13
- What shipped: Pre-launch privacy and hygiene audit for the Bushfire Alert Visualiser open-source repository.
- For whom: The research project team and future open-source contributors.
- Evidence it worked: Zero secret strings found across entire git sweep (`wc -l` = 0); all 16 automated tests passed (exit code 0); clean `.gitignore` and MIT licence confirmed.

## Decision
- Date: 2026-10-13
- Role: learning log
- Context: Preparing a private repository for public open-source release.
- In the context of the Bushfire Alert Visualiser, facing an exposed test token in historical commit 3f8a91c, I decided to revoke the token immediately at the provider and export a clean repository history for the public launch, to achieve total privacy confidence, accepting that historical private commit comments remain in the private archive.
- Options I considered: Leaving the key because it was for testing, running complex git-filter-repo rewrites, exporting a clean public repository.
- Why: Exporting a clean repository eliminates any chance of historical secret leaks or data recovery by scrapers.
- Confidence: 3 (could teach it)
- Revisit on: 2027-10-13

## Learned
- Date: 2026-10-13
- Role: learning log
- In my own words: In git, deleting a secret in a new commit does not make it disappear. It stays visible in earlier commits forever unless history is rewritten or cleaned. Always revoke any key that touched git.

## Word
- Date: 2026-10-13
- Word: Premortem
- What it means, in plain English: Imagining that a project has failed in the future before you even launch it, so you can work out what went wrong and fix it now.
- Where I met it: Running the pre-launch repository audit with kind-red-team.
```

---

## 5. Comparative Synthesis Matrix: Small vs Medium vs Large

The table below contrasts the three walkthrough tiers across key dimensions, illustrating how the Kind Team and Superpowers frameworks scale naturally with complexity:

| Dimension | Walkthrough 1 (Small) | Walkthrough 2 (Medium) | Walkthrough 3 (Large) |
| :--- | :--- | :--- | :--- |
| **Example Deliverable** | Single-page accessible contact form | Design token extraction & mobile buttons | Pre-launch open-source repository audit |
| **Effort Scope** | Small (1–2 turns) | Medium (3–6 turns) | Large (7+ turns) |
| **Creator Time** | ~5–10 mins | ~15–25 mins | ~45–60 mins |
| **Context Tier** | Light (<15k tokens) | Moderate (15k–50k tokens) | Deep (50k+ tokens) |
| **Active Crew Size** | 2 roles (`product-manager`, `accessibility-specialist`) | 3 roles (`ui-designer`, `accessibility-specialist`, `mobile-designer`) | 3 roles (`red-team`, `security-specialist`, `archivist`) |
| **Parked Roles** | `security-specialist`, `ui-designer` | `motion-designer`, `archivist` | `marketing-comms`, `delivery-manager` |
| **Primary Risk Mitigated** | Inaccessible form inputs & spambots | Failing colour contrast & cramped touch targets | Historical secret leaks & personal data exposure |
| **Stage 1 Review Gate** | WCAG 2.1 AA keyboard, labels, focus | Contrast ratios (8.2:1 / 5.6:1) & 44px tap targets | Premortem failure catalogue & 5-point git privacy scan |
| **Stage 2 Review Gate** | Input sanitisation & honeypot bot trap | 320px viewport reflow & responsive stack | Working tree `.gitignore` & dependency security |
| **Verification Gate** | `npx vitest run tests/contact/` (exit 0) | `npm test tests/design-tokens.test.js` (exit 0) | Git secret sweeps (`wc -l` = 0) & test suite (exit 0) |
| **Learning Log Types** | Milestone, Decision, Word (`Honeypot`) | Milestone, Decision, Learned, Word (`Design token`) | Milestone, Decision, Learned, Word (`Premortem`) |

---

## 6. Troubleshooting & Common Pitfalls for Non-Technical Creators

When implementing or executing these circuits in real-world environments, keep the following recovery protocols in mind:

### 6.1 Hand-Off Pack Incompleteness
- **Pitfall**: A creator or automated assistant forgets to include "What done means" in a review request.
- **Protocol**: The auditor role **does zero review work**. It replies with a single polite sentence requesting the missing part:
  > *"Please provide 'What done means' before I begin."*
- **Why this matters**: Reviewing without explicit done criteria leads to subjective impressions ("looks good to me") rather than verifiable engineering facts.

### 6.2 Managing Finding Overwhelm (The Rule of 3)
- **Pitfall**: An automated tool (such as an accessibility linter or secret scanner) discovers 15 minor issues, causing anxiety for a non-technical creator.
- **Protocol**: The auditor presents **at most the top 3 actionable findings** with concrete code fixes. All remaining findings are parked in one line each:
  > `- **Parked:** 4 minor comment typo warnings deferred to later cleanup.`

### 6.3 Responding to "Just Tell Me" and "Skip"
- **"Just tell me"**: If a creator is exhausted and asks "which colour should I use? Just tell me", bypass the Mission Preview card and role hand-offs entirely. Provide the direct answer in one plain sentence, followed by one line explaining why.
- **"Skip"**: If the creator replies "skip" or "yes" to a Mission Preview card, proceed immediately to the first role's hand-off pack without asking intermediate confirmation questions.

### 6.4 The Iron Law of Verification
- **Pitfall**: An automated assistant claims "The form should now be accessible" or "The secret is probably removed".
- **Protocol**: Strictly banned. Every completion claim must be preceded by fresh terminal execution output showing the command, output summary, and exit code 0.

---

## 7. Compliance Verification Checklist

Before publishing or referencing these walkthroughs, confirm compliance across all five repository standards:
- [x] **Universal 10-Step Circuit**: All 3 walkthroughs contain every step from Creator Prompt to Learning Log entry.
- [x] **Hand-Off Pack Integrity**: Every hand-off pack includes all 4 mandatory components (`Ticket:`, `Files to read:`, `What done means:`, `What not to touch:`).
- [x] **Severity & Attribution Scales**: All findings explicitly use the 4 severities (`Blocker`, `Fix before launch`, `Nice to fix`, `Paper tiger`) and 3 labels (`[checked]`, `[found by a tool]`, `[my judgement]`).
- [x] **Verification Gate Evidence**: Every walkthrough demonstrates the 4-step gate (Identify, Run, Read, Verify) with verbatim terminal output and exit code 0.
- [x] **Strict Australian English**: Checked for consistent Australian spelling (`colour`, `prioritise`, `categorise`, `judgement`, `artefact`, `rigour`, `centre`, `defence`).
- [x] **100% Tool-Agnostic & Zero AI Attribution**: Zero vendor locks, no AI co-author lines, and no marketing footers.
