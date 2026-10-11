# Working in this repo

ToolShed is a public repo of tools for people building with AI. The kind team lives in `plugins/kind-team`. Start with `tools/kind-team/README.md`, then `tools/kind-team/ROLLOUT.md`.

## Hard rules

1. **Nothing is committed, pushed, merged or opened as a PR until Kimberly says so.** Show the change first.
2. **Never commit to `main`.** Work on the branch for the ticket (now `kind-team-v0-1`). One PR per milestone. She merges.
3. **This repo is going public.** No personal details, secrets, health details, employer or client names, or anything copied from private repos. Use made-up examples.
4. **Ask for no credentials.** Roles never need them. Roles draft and recommend. They never commit, push, deploy or change DNS or Cloudflare.
5. **Never change a repo's visibility.**
6. **SKILL.md frontmatter uses only six fields:** name, description, license, compatibility, metadata, allowed-tools.
7. **The kind contract is identical in every role.** Change it in one place, then run `python3 tools/kind-team/check_roles.py`.
8. **Plain English and Australian spelling.** Name any new word once.
9. **Tool-agnostic: no AI attribution.** No Co-Authored-By lines for AI tools, no "Generated with" footers and no session links, in commits, pull requests, issues or files. Claude pushes branches; Kimberly opens pull requests and issues herself, because the GitHub connection adds its own footer.

## How she wants to work

- One thing at a time. Park extras visibly.
- Reply shape: outcome first, what changes, one line to learn, at most three decisions (recommended first, with what happens if she does nothing and whether it can be undone), one next step, and an access note when an account, secret or public visibility is touched.
- After each ticket, offer one Learning Log line (milestone, decision, learned or word).
- At most 3 cards in progress on the board: https://github.com/users/KRichshed/projects/2

## Checks before showing a change

    python3 tools/kind-team/check_roles.py
    claude plugin validate --strict plugins/kind-team
