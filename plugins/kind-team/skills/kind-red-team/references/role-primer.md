# Red team: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** No page could be opened from the build environment (every fetch failed with a network error), so nothing here was read directly from its source. Every row says whether it comes from a search summary or from memory.

## The premortem

| Fact | Status | Source |
|---|---|---|
| Gary Klein, "Performing a Project Premortem", Harvard Business Review 85(9), September 2007, pages 18 to 19 | Search summary only. Citation details seen in Wikipedia and a Psychology Today reference list, not the article | https://en.wikipedia.org/wiki/Pre-mortem |
| The method assumes the project has already failed and asks why it did | Search summary only | https://en.wikipedia.org/wiki/Pre-mortem |
| Group version: each person writes reasons for failure on their own first, then the group compiles a list | Search summary only, from a Psychology Today piece by Klein | https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method |
| The idea rests on "prospective hindsight" research | Search summary only | none opened |
| Claim that well-known economists endorse it | Seen on one commercial site only. Not used by the role | not verified |
| The three-item cut, and the three kinds of guard (stop, spot early, soften) | **No source.** The role's own judgement | none |
| An AI playing a customer is rehearsal, not evidence | **No source.** The role's own judgement | none |

## Looking in a repository's history

| Fact | Status | Source |
|---|---|---|
| `git log --all --format=...` with `%an %ae %cn %ce`, `git log -S"word"`, `git branch -a`, `git tag` | From memory. Not run here and not looked up. The lead should test them on a throw-away repository | none |
| gitleaks is open source, MIT licensed, fast, matches patterns and does not check whether a key still works | Search summary only (third-party comparison sites) | https://appsecsanta.com/gitleaks-vs-trufflehog |
| trufflehog has many typed detectors, can check whether a key is still live, and its licence is AGPL-3.0 per one summary | Search summary only. Its live checks send the key to the issuing service | https://appsecsanta.com/gitleaks-vs-trufflehog |
| Both can scan git history | Search summary only | https://pypi.org/project/git-secret-scanner/0.3.3 |
| GitHub secret scanning is free on public repositories. For private repositories it needs GitHub Secret Protection, on Team or Enterprise Cloud plans | Search summary of GitHub docs pages. Whether a personal private repository can use it was not settled, so the role says "some accounts" | https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/secret-security/about-secret-scanning |
| GitHub secret scanning looks through the whole history on all branches | Search summary, Enterprise Cloud docs only | same page |
| Whether GitHub's scanning covers issue and pull request comments on public repositories | Search summary only, "additional scanning is free for public repositories" | same page |
| Rewriting history changes every later commit's identity. Tools such as git filter-repo exist for it | From memory. Not looked up | none |
| A committed secret should be treated as leaked even after removal | From memory, widely repeated practice | none |

## What tools can and can't find

Pattern scanners find secrets shaped like known keys. They do not find a person's name, an employer in a commit message, a health detail or a copied paragraph, and they miss odd formats. No reliable percentage was found, so the role gives none.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Publishing other people's personal details, or work done for an employer or client, can carry duties that differ by country and by contract. Nothing was looked up.

## Gap to close before this role is Ready

- Read every source above directly and replace "search summary only" with "read on <date>".
- Run every recipe on a throw-away repository and fix any that fail.
- Read GitHub's own pages on secret scanning for personal private repositories, and what it covers in issues and pull requests.
- Read the gitleaks and trufflehog project pages for current licences and options.
- Read Klein's article or the Psychology Today piece directly.
- Check how git filter-repo and GitHub's own guidance describe removing data, and what stays behind in forks and caches.
- Run one real trial with a hand-off pack, and re-check its findings with a tool or a person.
