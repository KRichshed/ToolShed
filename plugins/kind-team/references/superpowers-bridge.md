# Kind Team & Superpowers Workflow Bridge: Interoperability Specification

## 1. Architectural Foundations: Human-Centric Contracts & Engineering Rigour

### 1.1 The Bridge Philosophy
Kind Team and Superpowers embody complementary strengths in modern software creation:
- **Kind Team** protects the creator. It provides emotional safety, non-technical plain English communication, cognitive overwhelm shields, structured role boundaries, and strict Level 1 Operator autonomy ("suggests, never acts; you decide").
- **Superpowers** protects the software. It enforces disciplined software engineering through granular implementation plans (`superpowers:writing-plans`), strict test-driven development (TDD), two-stage review gates, and empirical proof before completion claims (`superpowers:verification-before-completion`).

This specification establishes an interoperability bridge between both frameworks. By mapping Kind Team human-centric contracts directly to Superpowers execution loops, non-technical creators gain the safety and engineering rigour of world-class software teams without cognitive exhaustion, obscure terminal jargon, or loss of control.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           THE COLLABORATIVE BRIDGE                          │
│                                                                             │
│   KIND TEAM (Human-Centric)                 SUPERPOWERS (Engineering)      │
│   ─────────────────────────                 ─────────────────────────      │
│   Mission Preview Card        ──Translates──▶ Implementation Plan Header    │
│   Appetite & Sizing (S/M/L)   ──Calibrates──▶ Task Granularity & Budgets   │
│   Given / When / Then (Unhappy)──Generates──▶ TDD Red / Green Test Suites   │
│   Hand-Off Pack (4 Parts)     ──Configures──▶ Stage 1 Spec Review Gate      │
│   Severity (4-tier) & Source  ──Configures──▶ Stage 2 Quality Review Gate   │
│   Level 1 Operator Boundary   ──Enforces────▶ Checkpoint Pauses & Approvals │
│   Evidence Before Claims      ──Harmonises──▶ Verification Before Completion│
│   Learning Log Entry          ──Captures────▶ Retrospective Milestones      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Level 1 Operator Boundaries & Emotional Safety
Every automated worker operating under this bridge remains strictly bounded by Level 1 Operator constraints:
1. **Suggests and Prepares Only**: Workers generate plans, draft code, write tests, and run non-destructive verification. Workers never push commits, deploy code, execute destructive system alterations, or delete files without explicit human sign-off.
2. **Mandatory Human Checkpoint Pauses**: Execution pauses at every major boundary. Autonomous run-ahead execution across task boundaries is prohibited.
3. **Patience and Kindness**: Critique is directed solely at the work, never the creator. Workers ban condescending fillers ("just", "simply", "obviously") and present technical options with trade-offs rather than directives.
4. **Secrets and Privacy Protection**: Zero hardcoded secrets, tokens, or personal identifiers in code, chat transcripts, or commit metadata.

### 1.3 Tool-Agnosticism & Zero AI Attribution Mandate
In strict accordance with repository standards:
- **Vendor Neutrality**: The bridge specifies universal protocols compatible with standard Git, POSIX shells, text editors, browser-based environments, and local command-line tools. No proprietary tool locks are permitted.
- **Zero AI Attribution**: Commit histories, pull requests, issue notes, code comments, and documentation must contain zero third-party AI attribution. Specifically:
  - Banned: `Co-Authored-By: Claude <...>` or similar bot co-authorship trailers.
  - Banned: "Generated with AI", "Created by Claude Code", or equivalent marketing footers.
  - Banned: Sharing session links, prompt transcript URLs, or telemetry identifiers in commits or issues.

### 1.4 Strict Australian English Standards
All project artefacts, generated plans, review notes, and documentation adhere strictly to Australian English conventions:
- `colour` (not color)
- `prioritise`, `prioritised`, `prioritising` (not prioritize)
- `standardise`, `standardised`, `standardisation` (not standardize)
- `categorise`, `categorised` (not categorize)
- `behaviour`, `behaviours` (not behavior)
- `rigour` (not rigor)
- `artefact`, `artefacts` (not artifact)
- `judgement` (not judgment)
- `centre`, `centred` (not center)
- `defence` (not defense)
- `catalogue` (not catalog)

---

## 2. Section 1: Mapping Project Cards into Implementation Plans

### 2.1 Conceptual Translation Architecture
When a creator defines a feature with `kind-product-manager` (or `kind-chief-of-staff`), the outcome is a human-readable **Project Card**. To execute this work through Superpowers, the card is translated into a `superpowers:writing-plans` Markdown document. This translation bridges product appetite into granular, verifiable engineering tasks without discarding the original problem context or safety boundaries.

### 2.2 Comprehensive Field Mapping Table

| Kind Team Project Card Field | Superpowers Writing-Plan Section | Translation Rule & Semantic Bridge |
| :--- | :--- | :--- |
| **`Making`** (Problem statement & core purpose) | **`Goal`** & Plan Title | Formulated as a concise one-sentence objective defining what is built and the concrete problem solved. |
| **`For`** (Audience, outcome, and primary signal) | **`Review Focus`** | Top 5 failure modes or human risk classes most likely to disrupt the target user (e.g. keyboard traps, screen reader omissions, silent validation failures). |
| **`Size`** & **`Time it's worth`** (Appetite: hours, weekend, weeks) | **Task Granularity & Budget** | Calibrates task breakdown and time allocation: Small (1–2 tasks), Medium (3–5 tasks), Large (split into subsystem plans). |
| **`Starting from`** & **`Tools`** | **`Tech Stack`** & **`Architecture`** | Documents existing codebase assets, frameworks, test harnesses, and structural boundaries. |
| **`Given / When / Then`** Acceptance Criteria | **Task TDD Sequences** | Each criterion maps to a concrete test suite step: `Write failing test` ──▶ `Verify failure` ──▶ `Implement minimal code` ──▶ `Verify pass`. |
| Unhappy Paths ("Given network drops...", "Given invalid email...") | Error Handling Test Cases | Explicit edge case test tasks ensuring negative input validation and defensive error recovery are built before happy path styling. |
| **`What not to touch`** & Role Boundaries | **`Global Constraints`** | Verbatim directory boundaries, immutable contracts, protected files, accessibility baselines, and spelling rules. |
| **`Building blocks`** (Numbered 1 to 5) | **Task Decomposition (`Task 1`, `Task 2`, ...)** | Ordered, right-sized engineering units carrying discrete commit targets and verification gates. |
| **`Parked`** (Roles and features deferred) | **`Deferred & Out-of-Scope`** | Preserves deferred ideas visibly, guarding against scope creep and cognitive overwhelm during execution. |

### 2.3 Task Right-Sizing & Appetite Calibration
Superpowers requires tasks to be right-sized: small enough to implement in a short cycle (typically 2 to 5 minutes of focused execution), with an unambiguous pass/fail test condition, followed by an immediate review gate.
- **Small Appetite (1–2 turns / quick fix)**: 1–2 discrete tasks. Single component or file modification. Self-contained unit tests.
- **Medium Appetite (3–6 turns / multi-component)**: 3–5 discrete tasks. Incremental TDD sequence: data/model validation ──▶ UI component implementation ──▶ accessibility & integration audit.
- **Large Appetite (7+ turns / architectural)**: Decomposed into multiple milestone plans. Each plan addresses a single subsystem with its own verification suite.

### 2.4 Acceptance Criteria to TDD Sequences (Unhappy Paths Included)
Every acceptance criterion written by `kind-product-manager` must include at least one **unhappy path**. In the writing plan, each criterion is broken down into four atomic sub-steps:
1. **Write failing test**: Add an automated test (or executable test script) asserting the expected behaviour.
2. **Verify test failure**: Run the test runner to observe expected failure (confirming the test is not a false positive).
3. **Implement minimal code**: Write only the necessary code required to satisfy the failing test.
4. **Verify test pass**: Run the test suite to observe clean execution (exit code 0).

### 2.5 Scope Protection via Parked Artefacts
Non-technical creators frequently suffer from silent scope creep initiated by over-eager assistants suggesting "while we are here..." enhancements. The bridge enforces that any suggestion outside the active card's building blocks is immediately routed to the `Deferred & Out-of-Scope` section. Work on parked items is strictly prohibited until the primary plan completes verification.

### 2.6 Complete Worked Example: From Project Card to Writing Plan

#### Source Kind Team Project Card
```markdown
Project card · 2026-10-13

Making: Accessible newsletter signup card with instant email validation and spam honeypot
For: Independent creators who want readers to subscribe without data tracking or broken forms
Size: Small (weekend experiment)
Time it's worth: 2 hours maximum
Starting from: Clean HTML/CSS template in assets/
Tools: Vanilla HTML, CSS, JavaScript, Vitest
Region: Australia (Privacy Act compliance, Australian English)
How you like to work: Step by step, explain new terms once, plain English

Starting crew
| Role | Why now | Teaching level |
| kind-product-manager | Scopes acceptance criteria and protects appetite | Some |
| kind-accessibility-specialist | Audits keyboard navigation, contrast, and screen reader labels | New |
| kind-security-specialist | Audits honeypot spam defence and input sanitisation | New |

Building blocks
1. Accessible HTML structure · done when passes WCAG 2.1 AA keyboard and label checks · kind-accessibility-specialist
2. Client validation with honeypot · done when invalid emails and bot traps are caught · kind-security-specialist

Parked: Database integration, multi-step preferences, analytics beacons
Next step: Review acceptance criteria and generate implementation plan
```

#### Translated Superpowers Implementation Plan
```markdown
# Accessible Newsletter Signup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an accessible, privacy-respecting newsletter subscription form featuring client-side email validation and an invisible bot honeypot.
**Architecture:** Vanilla web component pattern; semantic HTML5 form controls; zero external tracking scripts; inline SVG icons for state feedback.
**Tech Stack:** HTML5, Modern CSS (custom properties), Vanilla JavaScript (ES2022), Vitest, JSDOM.
**Spec:** `plugins/kind-team/references/superpowers-bridge.md` § 2.6

## Global Constraints
- Level 1 Operator boundaries apply: suggest and prepare only; no automated git commits or pushes without human sign-off.
- 100% tool-agnostic: zero AI attribution trailers or "Generated with" headers.
- Strict Australian English in all user-facing strings (`personalised`, `favour`, `programme`).
- File boundaries: work strictly within `src/components/newsletter/` and `tests/components/newsletter/`.
- Accessibility baseline: WCAG 2.1 AA (contrast >= 4.5:1, visible focus ring >= 3:1, explicit `<label>` association, 320px reflow).

## Review Focus
1. Keyboard accessibility: entire interaction navigable without pointer device; no focus traps.
2. Screen reader announcements: validation errors connected via `aria-describedby` and `aria-live`.
3. Honeypot invisibility: honeypot field hidden from sighted users and assistive technology (`tabindex="-1"`, `aria-hidden="true"`), but enticing to automated scrapers.
4. Unhappy path handling: malformed email inputs, whitespace-only submissions, and rapid multi-clicks handled gracefully.
5. Contrast and zoom: text contrast compliant at 200% browser zoom; layout does not break at 320px viewport width.

## Tasks

### Task 1: Semantic Accessible Form Markup
- [ ] Write failing test in `tests/components/newsletter/form-markup.test.js` asserting form contains `<label for="email">`, `<input id="email" type="email" required>`, and submit `<button>` with discernible text.
- [ ] Run test to verify failure: `npm test tests/components/newsletter/form-markup.test.js` (observe fail due to missing markup).
- [ ] Implement semantic HTML template in `src/components/newsletter/template.html`.
- [ ] Run test to verify pass: `npm test tests/components/newsletter/form-markup.test.js` (exit code 0).
- [ ] Execute Stage 1 Spec Review Gate (`kind-accessibility-specialist` hand-off pack).

### Task 2: Client-Side Validation & Unhappy Path Error Handling
- [ ] Write failing test in `tests/components/newsletter/validation.test.js` covering:
  - Happy path: `user@example.com.au` returns valid state.
  - Unhappy path 1: `invalid-email` triggers error message linked via `aria-describedby="email-error"`.
  - Unhappy path 2: empty or whitespace submission halts form submission and focuses error container.
- [ ] Run test to verify failure: `npm test tests/components/newsletter/validation.test.js` (observe fail).
- [ ] Implement validation logic in `src/components/newsletter/validator.js`.
- [ ] Run test to verify pass: `npm test tests/components/newsletter/validation.test.js` (exit code 0).
- [ ] Execute Stage 2 Code Quality Gate (`kind-qa-tester` hand-off pack).

### Task 3: Invisible Honeypot Spam Defence
- [ ] Write failing test in `tests/components/newsletter/honeypot.test.js` asserting honeypot field `website_hp` is present, excluded from tab order (`tabindex="-1"`), hidden from accessibility tree (`aria-hidden="true"`), and if populated on submission, discards submission silently without processing.
- [ ] Run test to verify failure: `npm test tests/components/newsletter/honeypot.test.js` (observe fail).
- [ ] Implement honeypot input and handler in `src/components/newsletter/honeypot.js`.
- [ ] Run test to verify pass: `npm test tests/components/newsletter/honeypot.test.js` (exit code 0).
- [ ] Execute Stage 2 Security Review Gate (`kind-security-specialist` hand-off pack).

## Deferred & Out-of-Scope
- Server-side database integration (Supabase / Postgres).
- Multi-topic subscription checkboxes.
- Third-party analytics beacons or tracking pixels.
```

---

## 3. Section 2: Two-Stage Review Gates Invoking Kind Team Specialist Roles

### 3.1 Two-Stage Review Gate Architecture
Superpowers organises quality enforcement through **Two-Stage Review Gates**:
1. **Stage 1 (Spec Compliance Gate)**: Validates that the built artefact matches the declared specification, accessibility standards, user contract, and design tokens without omissions or unauthorised additions.
2. **Stage 2 (Code Quality & Security Gate)**: Validates implementation robustness, test suite thoroughness, code cleanliness, secrets handling, input sanitisation, and edge-case resilience.

The bridge configures these gates by mapping them directly to Kind Team installed specialist roles using the standard 4-part **Hand-Off Pack**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TWO-STAGE REVIEW GATE WORKFLOW                        │
│                                                                             │
│   [ Implementation Task Complete ]                                          │
│                  │                                                          │
│                  ▼                                                          │
│   STAGE 1: SPEC COMPLIANCE GATE                                             │
│   Auditor: kind-accessibility-specialist (+ kind-content-designer)          │
│   Contract: 4-part Hand-Off Pack                                            │
│   Checks: Keyboard, Contrast, Focus, Reflow, Screen Reader Labels           │
│   Pass Rule: 0 Blocker, 0 Fix before launch                                 │
│                  │                                                          │
│        [ PASS ]  └──────────────────────────────┐ [ FAIL ]                  │
│           │                                     ▼                           │
│           ▼                              Revise Code & Re-test              │
│   STAGE 2: CODE QUALITY & SECURITY GATE                                     │
│   Auditor: kind-qa-tester & kind-security-specialist                        │
│   Contract: 4-part Hand-Off Pack                                            │
│   Checks: Test Pass Evidence, Unhappy Paths, Secrets, Sanitisation          │
│   Pass Rule: Fresh Exit 0, 0 Leaks, 0 Unhandled Paths                       │
│                  │                                                          │
│        [ PASS ]  └──────────────────────────────┐ [ FAIL ]                  │
│           │                                     ▼                           │
│           ▼                              Revise Code & Re-test              │
│   PRE-LAUNCH GATE (Final Release)                                           │
│   Auditor: kind-red-team                                                    │
│   Checks: Premortem Failure Catalogue & 5-Point Git Privacy Scan            │
│                  │                                                          │
│                  ▼                                                          │
│   [ Human Checkpoint Sign-Off & Ticket Update ]                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Stage 1: Spec Compliance Gate (`kind-accessibility-specialist` & `kind-content-designer`)
- **Assigned Roles**: `kind-accessibility-specialist` for interaction and interface specs; `kind-content-designer` for copy, labels, and plain language readability.
- **Mandatory Hand-Off Pack Structure**:
  ```markdown
  Hand-off pack.

  Ticket: Review newsletter signup component for WCAG 2.1 AA spec compliance.

  Files to read:
  - src/components/newsletter/template.html
  - src/components/newsletter/styles.css
  - tests/components/newsletter/form-markup.test.js

  What done means:
  - 0 Blocker and 0 Fix before launch findings.
  - Keyboard accessible: complete flow navigable with Tab, Shift+Tab, Enter, Space.
  - Visible focus indicators with at least 3:1 contrast against adjacent background.
  - Text colour contrast meets at least 4.5:1 for standard text and 3:1 for large text.
  - Explicit form labels associated with inputs via `for`/`id`.
  - Reflow validated at 320px width without horizontal scrollbars or truncated text.

  What not to touch:
  - Everything. This is a read-only audit.
  ```
- **Gate Pass Criteria**:
  - Exactly **0 Blocker** findings.
  - Exactly **0 Fix before launch** findings.
  - If any Blocker or Fix before launch finding is discovered, execution halts immediately and returns to implementation revision.

### 3.3 Stage 2: Code Quality & Security Gate (`kind-qa-tester` & `kind-security-specialist`)
- **Assigned Roles**: `kind-qa-tester` for test harness verification, happy/unhappy path execution, and performance budgets; `kind-security-specialist` for input sanitisation, honeypots, secrets hygiene, and least privilege.
- **Mandatory Hand-Off Pack Structure**:
  ```markdown
  Hand-off pack.

  Ticket: Validate code quality, test suite rigour, and security defence in newsletter component.

  Files to read:
  - src/components/newsletter/validator.js
  - src/components/newsletter/honeypot.js
  - tests/components/newsletter/validation.test.js
  - tests/components/newsletter/honeypot.test.js
  - Fresh test execution log with full command output.

  What done means:
  - Test runner exits with code 0; all test assertions pass.
  - Both happy and unhappy paths (malformed email, empty input, network failure) tested.
  - Zero hardcoded API keys, tokens, or personal identifiers in code or tests.
  - Server-side or client-side input validation regex is safe against catastrophic backtracking (ReDoS).
  - Honeypot safely traps automated scripts without hindering assistive tech.

  What not to touch:
  - Everything. This is a read-only audit.
  ```
- **Gate Pass Criteria**:
  - Fresh automated test execution log confirming 100% test pass with exit code 0.
  - Zero unhandled unhappy paths or crash vectors.
  - Zero leaked secrets or security vulnerabilities.

### 3.4 Pre-Launch Final Gate: Premortem & Privacy (`kind-red-team`)
Prior to merging into production or public release, `kind-red-team` executes the final pre-launch gate:
1. **Job 1: Premortem ("It is 3 months after launch and failed, why?")**:
   - Identifies the top failure modes: spam flooding, broken email deliverability, accessibility complaint, confusing error states.
   - Recommends concrete preventative mitigations for the top failure modes.
2. **Job 2: 5-Point Git Privacy & Hygiene Check**:
   - Point 1: All local and remote branches inspected for untracked debug code or temporary files.
   - Point 2: Full commit history scanned for accidental secret commits, API keys, or `.env` files.
   - Point 3: Committer and author emails verified (no unintended work or personal email exposure).
   - Point 4: Tags and release notes checked for sensitive server paths or client names.
   - Point 5: Test fixtures and sample data inspected to ensure zero real user data is present.

### 3.5 Finding Classification: 4-Tier Severity & 3-Label Attribution
All audit findings reported across review gates must strictly follow Kind Team's standard scales:

#### The 4-Tier Severity Scale
1. **`Blocker`**: Prevents basic operation, violates core privacy/security, or completely excludes a group of users (e.g. keyboard focus trap, exposed secret key, form cannot be submitted). Must be fixed immediately.
2. **`Fix before launch`**: Serious barrier or defect that degrades experience significantly (e.g. colour contrast fails 4.5:1, missing error message for invalid email, unhandled network disconnect). Must be resolved prior to release.
3. **`Nice to fix`**: Polish, optimisation, or minor enhancement (e.g. improved touch padding, clearer placeholder copy). Deferrable to a subsequent sprint.
4. **`Paper tiger`**: Looks alarming in an automated scan but has zero negative impact on real users or security in context (e.g. linter warning on an intentional honeypot layout hack). Safe to dismiss with a brief note.

#### The 3-Label Attribution Scale
Every finding must cite its evidence origin:
1. **`[checked]`**: Directly verified and observed by the reviewer (e.g. manually tabbed through form, reviewed regex syntax).
2. **`[found by a tool]`**: Produced by an automated test runner or static analysis scanner (e.g. Vitest output, axe-core log, ESLint report).
3. **`[my judgement]`**: Professional opinion, architectural recommendation, or design assessment based on experience.

### 3.6 Hand-Off Pack & Ticket Update Deliverables
Upon concluding an audit, the reviewing role produces a copy-pasteable **Ticket Update Note** for project tracking:

```markdown
### 📋 Ticket Update · kind-accessibility-specialist · 2026-10-13
- **Target:** Accessible newsletter signup component (`src/components/newsletter/`)
- **Status:** Ready
- **Top Findings:**
  1. [Nice to fix] [checked]: Focus ring outline offset is 1px; increasing to 2px enhances visibility on dark backgrounds.
  2. [Paper tiger] [found by a tool]: Automated HTML validator warned on hidden honeypot input lacking a visual label; safely marked `aria-hidden="true"` and excluded from assistive tree.
- **Parked:** High-contrast theme toggle deferred to future design token milestone.
- **Audit Handoff:** kind-security-specialist (Hand-off pack attached below)
```

---

## 4. Section 3: Standardising Verification-Before-Completion Across Review Loops

### 4.1 The Iron Law: Evidence Before Claims, Always
Adapted from `superpowers:verification-before-completion`, the bridge establishes an uncompromising standard:

> **NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**
> Any assertion that work is complete, functional, accessible, or bug-free must be preceded by fresh, verbatim empirical evidence. Unverified claims are treated as critical system failures.

### 4.2 The 4-Step Verification Gate Function
Before any role or worker generates a completion note or claims a task is done, it must execute the **4-Step Verification Gate**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    4-STEP VERIFICATION GATE FUNCTION                        │
│                                                                             │
│   [ 1. IDENTIFY ]  Determine exact test command or inspection recipe that   │
│                    empirically proves the "What done means" criteria.       │
│                           │                                                 │
│                           ▼                                                 │
│   [ 2. RUN ]       Execute the complete command freshly. Do not rely on     │
│                    stale terminal history or partial runs.                  │
│                           │                                                 │
│                           ▼                                                 │
│   [ 3. READ ]      Inspect full stdout/stderr, verify exit code is 0, and   │
│                    confirm test failure count is exactly zero.              │
│                           │                                                 │
│                           ▼                                                 │
│   [ 4. VERIFY ]    Confirm output satisfies all criteria. Quote verbatim    │
│                    evidence before declaring status.                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

1. **IDENTIFY**: Pinpoint the precise command, automated test, or inspection script that proves the claim.
2. **RUN**: Execute the full, fresh command in the project environment. No cached assumptions.
3. **READ**: Read the entire output. Inspect the exit code, test pass counts, and any residual warnings.
4. **VERIFY**: Evaluate output against the criteria. If tests fail or residuals exist, state actual status with failures. Only if 100% verified, state completion **with the verbatim evidence quoted**.

### 4.3 Banned Red-Flag Phrases & Dangerous Language
To prevent false assurance and uphold rigorous integrity, the following phrases are strictly banned from completion claims and review notes:

| Banned Red-Flag Phrase | Why It Is Dangerous | Required Compliant Alternative |
| :--- | :--- | :--- |
| *"Should work now"* | Expresses unverified hope rather than tested fact. | Run the test, inspect output, and quote the result: `"Ran npm test; all 4 tests passed (exit code 0)."` |
| *"Probably fine"* | Guesswork masquerading as assurance; conceals unverified regressions. | Execute verification: `"Executed keyboard navigation check; Tab traverses all 3 controls without trap."` |
| *"Seems fixed"* | Speculative assertion without reproducible evidence. | State empirical confirmation: `"Re-ran test suite; previously failing assertion at line 42 now passes."` |
| *"Looks good to me"* | Subjective impression; ignores accessibility, security, and edge cases. | Cite objective checks: `"Checked contrast ratios (4.8:1), keyboard tab sequence, and form error states."` |
| *"Fully compliant"* | No automated or static check can prove 100% WCAG compliance. | Specify scope: `"Meets tested WCAG 2.1 AA criteria for keyboard navigation, labels, contrast, and reflow."` |
| *"Completely secure" / "Safe"* | Security is a continuous posture of managed risk, never an absolute state. | Detail verified defences: `"Zero hardcoded secrets detected; server-side regex tested against ReDoS attacks."` |
| *"All tests pass"* (without log) | Unsubstantiated claim; easily hides skipped or disabled test suites. | Provide verbatim evidence: Quote test suite summary, exit code 0, and duration timestamp. |

### 4.4 Human-in-the-Loop Verification Recipes (Non-Terminal Environments)
When creators interact with Kind Team in non-CLI environments (e.g. web chats, desktop interfaces) where the automated worker cannot execute terminal commands directly, the worker must never guess or pretend tests passed.

Instead, the worker provides an accessible **5-Minute Verification Recipe**:
1. Numbered, step-by-step instructions written in plain English.
2. Explicit physical actions (e.g. "Press your Tab key 3 times", "Disconnect Wi-Fi and click Submit").
3. What to observe and what constitutes a pass or fail.
4. The worker pauses and awaits the creator's reported outcome before logging status. Findings are attributed as `[checked against your description]`.

---

## 5. Section 4: Operationalising the Bridge for Non-Technical Creators

### 5.1 End-to-End Collaboration Circuit
The bridge operationalises a complete, predictable lifecycle that guides a newcomer from an initial rough idea to verified, production-ready software:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       END-TO-END COLLABORATION CIRCUIT                      │
│                                                                             │
│   Step 1: User Brief / Brain Dump                                           │
│           Creator describes goal in plain English.                          │
│           │                                                                 │
│           ▼                                                                 │
│   Step 2: Mission Preview Card (Chief of Staff)                             │
│           Transparent trip meter: Crew (1-3), Effort, Turns, Tokens, Flow.  │
│           │                                                                 │
│           ▼                                                                 │
│   Step 3: Human Checkpoint Pause                                            │
│           "Shall we start?" ──▶ Creator signs off before any action.        │
│           │                                                                 │
│           ▼                                                                 │
│   Step 4: Project Card & Acceptance Criteria (Product Manager)              │
│           Defines Appetite, Outcome, Given/When/Then (Unhappy Paths), Cut.  │
│           │                                                                 │
│           ▼                                                                 │
│   Step 5: Superpowers Writing Plan Translation                              │
│           Converts card into right-sized TDD tasks and review focus.        │
│           │                                                                 │
│           ▼                                                                 │
│   Step 6: TDD Task Execution Loop                                           │
│           Failing test ──▶ Verify fail ──▶ Code ──▶ Verify pass.            │
│           │                                                                 │
│           ▼                                                                 │
│   Step 7: Stage 1 Spec Review Gate                                          │
│           Hand-Off Pack ──▶ kind-accessibility-specialist.                  │
│           │                                                                 │
│           ▼                                                                 │
│   Step 8: Stage 2 Code Quality & Security Gate                              │
│           Hand-Off Pack ──▶ kind-qa-tester / kind-security-specialist.      │
│           │                                                                 │
│           ▼                                                                 │
│   Step 9: Verification Evidence Capture                                     │
│           4-step gate function quotes verbatim exit code 0 evidence.        │
│           │                                                                 │
│           ▼                                                                 │
│   Step 10: Ticket Update & Learning Log Recording                           │
│            Copy-pasteable card update + Milestone/Decision learning log.    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Cognitive Overwhelm Shields: The Rule of 3
To safeguard creators with varying technical experience from cognitive exhaustion, the bridge applies strict cognitive shields:
1. **Starting Crew Discipline**: The active starting crew is restricted to **at most 3 roles**. All other specialised roles are parked visibly by name.
2. **Finding Cap**: When presenting audit outcomes, workers present **at most 3 actionable findings** with concrete solutions. Any secondary issues are parked in a single-line summary (`Parked: ...`) to prevent anxiety.
3. **Plain English & Jargon Discipline**: Any new technical term (e.g. `honeypot`, `reflow`, `TDD`) must be explained in plain English the first time it is introduced.

### 5.3 Execution Modes: Subagent Spawning vs In-Session Role Switching
The bridge supports two operational runtime modes:
- **Mode A: Subagent Execution (Multi-Worker Systems)**:
  - Where the host environment supports autonomous subagent dispatch (e.g. Superpowers `subagent-driven-development`), each task and audit gate is assigned to an isolated worker thread.
  - Workers communicate via structured Markdown files in designated agent directories.
  - A coordinating parent oversees checkpoints and integrates ticket updates.
- **Mode B: In-Session Role Switching (Single-Thread Systems)**:
  - In standard chat sessions or single-agent CLIs, the assistant explicitly switches persona and context between turns using the Hand-Off Pack headers.
  - The assistant announces role transitions clearly: *"Now putting on the kind-accessibility-specialist hat to audit keyboard navigation."*
  - The same 4-part Hand-Off Pack and 4-step verification gate apply without deviation.

### 5.4 Edge Case Protocols & Recovery Procedures

| Scenario / Edge Case | System Hazard | Mandatory Bridge Protocol |
| :--- | :--- | :--- |
| **Incomplete Hand-Off Pack** | Reviewer conducts audit on missing assumptions, causing invalid conclusions. | The reviewing role performs **zero review**. It halts and outputs a single polite sentence requesting the missing component: *"Please provide 'What done means' before I begin."* |
| **Accidental Secret Paste** | Creator accidentally pastes API key, database URL, or password into chat. | Line 1 immediate warning. Treat secret as compromised. Instruct creator to revoke and rotate immediately. Refuse to repeat the secret. Continue review using `SAMPLE_REDACTED_KEY`. |
| **Automated Tool Returns 0 Errors** | Creator falsely assumes 100% perfection and accessibility compliance. | Role explicitly clarifies: *"Found 0 automated errors via tool (found by a tool), but automated tools detect only ~30% of accessibility barriers. Keyboard navigation and screen reader checks were performed separately."* |
| **Scope Creep ("While We're Here")** | Assistant or creator attempts to add extra features mid-task. | Role immediately moves item to `Parked:`, reminds creator of the fixed appetite budget, and returns focus to completing the current task. |
| **Failing Verification at Gate** | Code passes linter but fails behavioural test assertion. | Role blocks task completion. Halts progress, quotes verbatim test failure output, identifies root cause, and plans a minimal code fix. Never bypasses test. |

---

## 6. Summary Checklist for Bridge Implementers

Before declaring Milestone 3 implementation complete, verify compliance across all five bridge dimensions:
- [x] **Contract Integrity**: All hand-offs conform to the 4-part pack (`Ticket:`, `Files to read:`, `What done means:`, `What not to touch:`).
- [x] **Severity & Attribution**: Findings are explicitly tagged with one of 4 severities (`Blocker`, `Fix before launch`, `Nice to fix`, `Paper tiger`) and one of 3 labels (`checked`, `found by a tool`, `my judgement`).
- [x] **Verification Discipline**: The 4-step gate (Identify, Run, Read, Verify) is enforced; all banned red-flag phrases are eliminated.
- [x] **Language & Style**: Strict Australian English spelling applied consistently across all documentation and templates.
- [x] **Zero AI Attribution**: 100% tool-agnostic; no `Co-Authored-By` lines, no "Generated with" footers, and no vendor lock-in.
