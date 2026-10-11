# Delivery manager: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Every page here was tried with a direct fetch on 2026-10-11 and the fetch was blocked in the build environment, so no page was read directly. What is below comes from web search summaries on that date, or from memory where stated. Nothing here is marked "read on" because nothing was.

## Planning ideas this role leans on

| Fact | Status | Source |
|---|---|---|
| Appetite is a time budget set first, which then shapes the design, the opposite of an estimate made afterwards | Search summary only | https://basecamp.com/shapeup/1.2-chapter-03 |
| "Fixed time, variable scope": hold the time, cut the scope to fit | Search summary only | https://basecamp.com/shapeup/1.2-chapter-03 |
| Small batches of about one to two weeks, big batches of about six weeks | Search summary only. The summary mixed the book with secondary sources, so treat the numbers as the book's example, not a rule for this role | https://basecamp.com/shapeup/1.2-chapter-03 |
| Work in progress limits: fewer things at once finish sooner | From memory (common Kanban practice). No source opened | none |
| Rollback, one guard per risk, and the order of dependencies | The role's judgement from common practice. No authoritative source found | none |

## Domains and transfers

| Fact | Status | Source |
|---|---|---|
| A change of registrant (the owner details) normally triggers a 60-day transfer lock, which some registrars let you opt out of | Search summary only. ICANN pages from 2015 and 2017 were named in results | https://www.icann.org/resources/pages/about-transfer-policy-2017-10-10-en |
| A new registration, or a domain just transferred, may also be locked for 60 days | **Sources disagree.** One registrar blog calls it required, another page calls it a permitted reason for the registrar to refuse. Check ICANN's current text | none |
| A transfer needs an authorization code from the current registrar, and it should be requested through a trusted channel, never shared publicly | Search summary only, thin | none |
| A page dated September 2026 said ICANN approved transfer policy review recommendations in June 2026, not yet in force | Third-party page only, **not confirmed** | none |
| The registrar transfer lock is a switch the owner turns off before a transfer | From memory. No source opened | none |
| DNS changes spread over minutes to a day or two; the "time to live" setting lowers how long old answers are kept | From memory, plus one third-party guide in a search summary saying up to 24 to 48 hours but often minutes | none |

## Hosting

| Fact | Status | Source |
|---|---|---|
| Cloudflare Pages: a subdomain can be pointed with a CNAME record at your DNS provider. An apex (bare) domain needs the domain added to Cloudflare with its nameservers pointed at Cloudflare | Search summary only | https://developers.cloudflare.com/pages/configuration/custom-domains/ |
| A guide's claim that only Cloudflare supports CNAME flattening | Third-party claim, not in Cloudflare's docs. The role does not repeat it | none |

## What tools can and can't find

Nothing automated can tell you whether a plan is realistic. A free DNS lookup shows what a name points to at that moment. It cannot show what will be true later. No reliable figure on how often launches slip was found, so the role gives none.

## Free tools a beginner can use

Any public DNS lookup website, and the registrar's own help pages. None were load-tested.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Rules about domain ownership, privacy lookups and country-specific domain endings differ by country and by registry.

## Gap to close before this role is Ready

- Read the Shape Up chapters on appetite and scope directly.
- Read ICANN's current Transfer Policy and settle the 60-day rules and the June 2026 claim.
- Read Cloudflare's current custom domain page and its guide on moving nameservers.
- Find a source for propagation and time to live.
- Run one real launch plan through the role and re-check its findings with a person.
