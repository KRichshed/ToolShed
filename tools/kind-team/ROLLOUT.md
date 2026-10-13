# How a kind team role goes from idea to ready

Three levels. Every role is described by the highest level it has earned, with the evidence listed. A role that passed its tests but hasn't been used on real work is a **Bone**, and never "ready".

## The three levels

| Level | What it means | Evidence |
|---|---|---|
| **Bone** | It exists, loads when it should, and behaves on its scenarios. Safe to try, not yet safe to rely on. | The checker passes. The plugin validator passes in strict mode. It loads on at least 4 of its 5 should-trigger prompts over 3 runs each, and on none of its should-not prompts. Each scenario was read and behaves. The primer says honestly what is and isn't verified. A privacy and secrets scan is clean. |
| **Ready** | Its sources were read directly, and it has been used once on real work and held up. | Everything in Bone, plus: a blind comparison with and without the role, which it wins on at least 2 of 3 scenarios. Every source in the primer is marked "read on <date>", or the gap is stated. One real trial, with its findings re-checked by an independent tool or person, and any disagreement explained. A log entry written. |
| **Proven** | It has been used repeatedly, and retros have fed back into it. | At least three real uses with a retro, and the open issues from each trial closed. |

## The steps, in order

1. **Start from the skeleton.** `python3 tools/kind-team/new_role.py kind-example "Example"`. It copies the shared contract text in exactly.
2. **Research the sources,** and note honestly what you read and what you only saw summarised.
3. **Fill in the placeholders.** Check as you go with `python3 tools/kind-team/check_roles.py --draft kind-example`.
4. **Run the checker without `--draft`.** All placeholders must be gone.
5. **Run the plugin validator:** `claude plugin validate plugins/kind-team --strict`, and the same on the repo root.
6. **Run the test harness:** `python3 tools/kind-team/run_role_tests.py kind-example --reps 3 --baseline --blind`.
7. **Read the replies and grade them blind.** Give the A and B files to a grader who doesn't know which is which, then open the key.
8. **Fix what the tests found, and re-run only what changed.** Common fixes: the description doesn't mention a phrase people really use, parked findings have no label, jargon isn't explained.
9. **Open one pull request** using `PULL_REQUEST_ROLE.md`. Say the level plainly.
10. **Trial it on real work,** with a hand-off pack. Re-check its top findings with a tool or a person. Write down where they differ.
11. **Move it to Ready** when the evidence is in, and say so in a new pull request or an update to the role ticket.

## The readiness line

Every role ticket carries one line, kept up to date:

> **Level:** Bone · **Sources:** search summaries only · **Trial:** not run · **Open:** <the one or two things still blocking Ready>

## Rules that never change

- The shared contract text in every role stays identical. Change it in one place, then copy it. The checker enforces this.
- Frontmatter uses only the six standard fields.
- No personal details, secrets, real keys or private project material in any role, example or test. Use made-up examples and obviously fake keys.
- Trial notes about a real project stay private. They are never added to this repository.
- Nothing is committed, pushed or published without the owner's yes. One pull request per milestone.

## Where each role stands

As of 11 October 2026. Update this table in the pull request that changes a role's level.

| Role | Level | What's still needed for Ready |
|---|---|---|
| kind-product-manager | Bone | Sources read directly, a blind comparison on the current version, and a logged real use |
| kind-chief-of-staff | Bone (v0.2, KT-29) | A real trial, and a fix so parked roles are marked "not installed yet" |
| kind-accessibility-specialist | Bone, trial done | Sources read directly, and the follow-up from the trial |
| kind-security-specialist | Bone | Sources read directly, and a real trial |
| kind-delivery-manager | Bone | Sources read directly, a real trial on a launch checklist, and a way to explain DNS words without jargon |
| kind-red-team | Bone | Sources read directly, the git recipes tried on a throw-away repository, and a real run of the privacy check |
| kind-qa-tester | Bone | Sources read directly, and a real trial on a form that has been built |
| kind-learning-log | Bone | Sources read directly, the two-logs and four-entry scenarios fixed, and a real use on a live log |
| kind-content-designer | Bone | Sources read directly, preview length rules checked, and a real trial on real copy |
| kind-setup-guide | Bone | Plan and price rows verified from the official pages, an install run on a real Mac and Windows machine, and a real first-run trial |
| kind-motion-designer | Bone | Sources read directly, shorter replies, and a real trial on a real motion spec |
| kind-ux-designer | Bone | Sources read directly, flow and sketch before findings every time, no final wording, and a real trial on a real flow |
| kind-marketing-comms | Bone | Sources read directly (platform limits and local advertising rules), shorter replies, and a real trial on a real launch post |
| kind-ui-designer | Bone | Sources read directly, contrast checking tool integration verified, and a real trial on a component design system |
| kind-mobile-designer | Bone | Sources read directly, responsive device testing on real mobile browsers, and a real trial on small screens |
| kind-solution-architect | Bone | Sources read directly, C4 diagram visual verification, and a real trial on a system boundary design |
| kind-archivist | Bone | Sources read directly, relative markdown link verification, and a real trial on a repository cleanup |
