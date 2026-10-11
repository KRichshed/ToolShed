# Setup guide: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** The Claude Code pages below were opened with a fetch tool on 2026-10-11. That tool returns the page text after a small model has processed it, so each row says "read on 2026-10-11". The pricing page came back as a short summary only. Pages not opened are marked. No command was run on a real computer: the install commands were copied from the docs, not tried here. Prices live in `prices-and-limits.md`.

## The guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| Install commands: macOS, Linux and WSL use `curl -fsSL https://claude.ai/install.sh \| bash`. Windows PowerShell uses `irm https://claude.ai/install.ps1 \| iex`. CMD has its own command. Homebrew and WinGet also work. `claude --version` shows a version number if it worked. The role sends people to the page rather than quoting these | Read on 2026-10-11 | https://code.claude.com/docs/en/setup |
| Requirements: macOS 13+, Windows 10 1809+, 4 GB+ RAM, internet. A Pro, Max, Team, Enterprise or Console account is needed. The free claude.ai plan does not include Claude Code | Read on 2026-10-11 | https://code.claude.com/docs/en/setup |
| `claude doctor` prints install checks. Login happens in the browser when `claude` first runs | Read on 2026-10-11 | https://code.claude.com/docs/en/setup |
| Quickstart: `cd` into a project, run `claude`, log in, ask a question | Read on 2026-10-11 | https://code.claude.com/docs/en/quickstart |
| Plugins: `/plugin marketplace add <owner>/<repo>`, `/plugin install <plugin>@<marketplace>`, or the `claude plugin ...` versions in a terminal. The `@` name is the marketplace's registered name. `claude plugin list` lists installed plugins. `claude plugin details <name>` shows what a plugin adds each session. The docs say a plugin can run hooks and servers, so read it before installing | Read on 2026-10-11. The `claude plugin validate` command was taken from the build brief, not seen on this page | https://code.claude.com/docs/en/discover-plugins |
| Cloud sessions: run on an Anthropic-managed machine, need GitHub for code, private unless shared, count toward plan limits | Read on 2026-10-11 | https://code.claude.com/docs/en/claude-code-on-the-web |
| Costs: `/usage` shows usage, `/clear` between tasks helps, long sessions use more, Pro and Max users can set a usage-credit spend limit | Read on 2026-10-11 | https://code.claude.com/docs/en/costs |
| Why too many skills cost attention and usage: skill and plugin descriptions are loaded into context. The costs page says skills load on demand, and the plugins page shows a per-plugin "every turn" cost estimate | Read on 2026-10-11 (partly the role's judgement) | https://code.claude.com/docs/en/costs |
| `.gitignore` and keeping `.env` out of git | From memory. Standard git practice, no page opened | https://git-scm.com/docs/gitignore |
| Keeping keys out of chats | The role's judgement, in line with general secrets practice | none |
| ChatGPT and Gemini setup | Parked, not researched | none |

## What tools can and can't find

`claude doctor` checks the install and settings. It cannot tell whether a plugin is worth keeping or whether a key has leaked. No reliable figure for either was found, so the role gives none.

## Free tools a beginner can use

`claude --version`, `claude doctor`, `/usage` and `claude plugin list`, all built in. Links were not load-tested.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Claude Code is only available in some countries (the docs link a supported list; the list was not opened).

## Gap to close before this role is Ready

- Run the install recipe on a real Mac and a real Windows laptop with a new person.
- Open the pricing and limits pages directly, without a summarising tool, and replace the "summarised" marks.
- Read the plugin security page, the terminal guide and the troubleshooting page.
- Confirm `claude plugin validate` on the plugin docs page.
- Find a source for how skill descriptions affect usage.
- Research Gemini and ChatGPT setup if they are ever added.
