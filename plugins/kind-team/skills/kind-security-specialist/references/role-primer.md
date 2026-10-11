# Security specialist: role primer

As of 2026-10-11. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Every row below comes from web search summaries on 2026-10-11. No page could be opened from the build environment, so nothing here was read directly from its source. The status column says what is supported by a search summary, and what was not found.

## The main list of web risks

| Fact | Status | Source |
|---|---|---|
| The OWASP Top 10 2025 is the current edition. It lists broken access control, security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software or data integrity failures, logging and alerting failures, and mishandling of exceptional conditions | Search summary only. One summary called the 2025 document a release candidate, so check it is final | https://owasp.org/Top10/2025/0x00_2025-Introduction/ |
| Server-side request forgery is no longer its own category in 2025 | Secondary sources only | https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/ |

## Guidance this role leans on

| Topic | Status | Source |
|---|---|---|
| Input validation, including a warning against logging rejected input as it came in | Search summary only | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html |
| Cross-site request forgery | Search summary only | https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html |
| Secrets management | Search summary only | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html |
| Cross-site scripting and logging cheat sheets | URLs guessed from the site's naming, not seen | not verified |
| Email header injection: the mechanism is a new line inside a field. OWASP has no page for contact forms, and the nearest pages describe the mechanism only | Search summary only | https://owasp.org/www-community/vulnerabilities/CRLF_Injection |
| The safe pattern the role teaches (fixed From and Subject, visitor's words in the body, validated reply address) | **No authoritative source found.** It's the role's judgement from common practice | none |
| Honeypot fields, and hiding them from screen readers and keyboard users | **No authoritative source found.** Practitioner blogs only. They suggest `aria-hidden`, `tabindex="-1"` and a server-side check | https://blog.openreplay.com/honeypot-fields-stop-bots/ |

## Cloudflare, since many small sites use it

| Fact | Status | Source |
|---|---|---|
| Turnstile: the browser gets a token, and the server must check it with a POST to the siteverify address with the secret key. A token lasts 300 seconds and works once | Search summary only | https://developers.cloudflare.com/turnstile/get-started/server-side-validation/ |
| Workers secrets are added with `wrangler secret put`. Local development uses a `.dev.vars` file. The role teaches keeping that file out of git | Search summary only. The explicit git advice was seen only on a third-party blog | https://developers.cloudflare.com/workers/configuration/secrets/ |
| A rate limiting binding exists for Workers. Counters are per location, and the docs advise against keying on IP addresses | Search summary only | https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/ |
| On Pages, the `_headers` file sets headers on static files, but not on Pages Functions replies | Search summary only | https://developers.cloudflare.com/pages/configuration/headers/ |
| Pages dashboard "encrypted variables", and the WAF rate limiting rules | Not looked up | none |

## Basic headers and free checks

| Fact | Status | Source |
|---|---|---|
| MDN has practical guides for Content-Security-Policy, X-Content-Type-Options, Strict-Transport-Security and Referrer-Policy | Search summary only | https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides |
| The MDN HTTP Observatory launched in July 2024 and replaced Mozilla's older Observatory, which was shut down in October 2024 | Search summary only | https://developer.mozilla.org/en-US/observatory |
| GitHub secret scanning and push protection block pushes that contain recognised secrets | Search summary only. The official page was not returned | not verified |
| `npm audit`, and securityheaders.com | Not looked up | not verified |

## What automated tools can find

OWASP says automating black-box testing "is not (nor will ever be) completely effective", and that business logic mistakes usually need a person (OWASP Web Security Testing Guide and Developer Guide, search summaries only). No reliable percentage was found, so the role gives none.

https://owasp.org/www-project-web-security-testing-guide/v41/2-Introduction/

## Privacy law, and what to say about it

The role never gives legal advice and says "check your local rules".

- **Australia.** The Privacy Act has a small business exemption for businesses with a yearly turnover of $3 million or less, with exceptions such as health service providers and businesses that trade in personal information. A small business can opt in. Whether a personal, non-commercial site is covered: unsure. Source (search summary only, no page date seen): https://www.oaic.gov.au/privacy/privacy-for-organisations/small-business
- **European Union.** The household exemption in GDPR Article 2(2)(c) covers purely personal activity and is read narrowly, and publishing to an unlimited audience falls outside it. This comes from secondary commentary only.

## Gap to close before v1.0

- Read every source above directly, and replace "search summary only" with "read on <date>".
- Find an authoritative source for the safe email pattern and for honeypot and time-trap advice, or keep them labelled as judgement.
- Confirm whether the OWASP Top 10 2025 is final.
- Look up the Cloudflare Pages dashboard variables, the WAF rate limiting rules, `npm audit` and securityheaders.com.
- Read the primary text of the privacy sources, and add a regional pack per region.
- Re-run this research from an environment that can open owasp.org, developers.cloudflare.com, developer.mozilla.org and oaic.gov.au.
