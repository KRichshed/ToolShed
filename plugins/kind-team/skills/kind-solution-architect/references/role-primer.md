# Solution architect: role primer

As of 2026-10-12. Re-check every six months. Load only when the person asks where something comes from, or wants to go deeper.

**How much is verified.** Nothing here was read directly from its source. No page was opened for this primer. Every row is from memory or is the role's own judgement, and the status column says which. Check the current page before quoting any of it.

## The standard or guidance this role leans on

| Fact | Status | Source |
|---|---|---|
| The C4 model (Context, Containers, Components, Code) for visualising software architecture at different levels of abstraction by Simon Brown | From memory, 2026-10-12. Not opened | https://c4model.com/ |
| Architecture Decision Records (ADRs) for capturing significant architectural choices along with context and consequences by Michael Nygard | From memory, 2026-10-12. Not opened | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions |
| MonolithFirst strategy: start with a monolithic design even if you expect to eventually migrate to microservices, by Martin Fowler | From memory, 2026-10-12. Not opened | https://martinfowler.com/bliki/MonolithFirst.html |
| Stability patterns (Circuit Breakers and Bulkheads) to isolate dependency failures, from Release It! by Michael Nygard | From memory, 2026-10-12. Book from memory, not opened | none |
| The Twelve-Factor App methodology for portable, stateless application architectures and explicit dependency boundaries by Adam Wiggins / Heroku | From memory, 2026-10-12. Not opened | https://12factor.net/ |
| Gall's Law: A complex system that works is invariably found to have evolved from a simple system that worked; a complex system designed from scratch never works | From memory, 2026-10-12. General citation (John Gall, Systemantics) | none |
| Essential complexity versus accidental complexity in system design, from No Silver Bullet by Fred Brooks | From memory, 2026-10-12. Not opened | none |
| Defaulting to a single monolith or static hosting, reserving serverless for bursty or purely event-driven workloads, and avoiding microservices for small teams | No authoritative source seen. The role's judgement | none |

## What tools can and can't find

Static analysis tools (such as dependency-cruiser, ArchUnit, or SonarQube) can detect circular dependencies between modules and enforce layered import boundaries within a codebase. Cloud cost calculators and linters (like Infracost or cfn-lint) can flag misconfigured cloud templates or estimate monthly infrastructure line items. However, no automated tool can judge whether a domain boundary makes architectural sense, whether a team is adopting microservices prematurely, or whether accepting a proprietary cloud database creates dangerous vendor lock-in. Architectural trade-offs require human judgement. No figure exists for tool accuracy across architectural design, so none is given.

## Free tools a beginner can use

- Mermaid live editor (https://mermaid.live). Text-to-diagram tool that renders flowcharts, sequence diagrams, and architecture maps directly in markdown. Not load-tested.
- Structurizr DSL Lite (https://structurizr.com/dsl). Lightweight plain-text tool for modelling systems using Simon Brown's C4 model. Not load-tested.
- Markdown Architecture Decision Record (MADR) templates (https://adr.github.io/madr/). Plain-text template for recording architectural choices in Git. Not load-tested.
- Diagrams.net (formerly draw.io). Free web-based diagramming tool for manual system diagrams. Not load-tested.

## Law, and what to say about it

The role never gives legal advice and says "check your local rules". Architectural decisions dictate where user data physically resides (data residency and sovereignty) and how datastores manage retention and deletion. Frameworks like the Australian Privacy Act 1988 (Cth), the EU General Data Protection Regulation (GDPR), and the UK GDPR impose obligations regarding cross-border data transfer, data minimisation, and user data erasure. An architect must ensure data can be located, isolated, and permanently purged upon request without corrupting unrelated records. No legal document was opened directly for this primer.

## Gap to close before this role is Ready

- Read the C4 model specification directly at c4model.com and verify the definitions of Context, Container, Component, and Code.
- Read Michael Nygard's 2011 article 'Documenting Architecture Decisions' directly to verify the original ADR format.
- Read Martin Fowler's 'MonolithFirst' article directly and confirm quoted thresholds for service decomposition.
- Confirm regional data residency requirements under the Australian Privacy Principles (APPs) and GDPR before advising on international cloud regions.
