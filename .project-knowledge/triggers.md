# Trigger & Routing Map

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> The "routes" of this project. Selection happens entirely on frontmatter
> `description`, so this is the full routing surface.
>
> **Check here before writing a new skill** — overlap between two descriptions means
> the wrong skill loads, or neither does.

---

## Routing table

| A user asking about… | Loads | Notes |
|---|---|---|
| Money formats, national ID, governorates, ports of filing, cheques, wallets | `egy-context-operations` | **Shared foundation.** Other skills cite it |
| Finding a statute, whether a law is current, Cassation principles, verifying a citation | `egy-legal-research` | Read this before asserting any citation |
| Reviewing a commercial contract clause by clause | `egy-commercial-contract-review` | The flagship. Parties, price, penalties, force majeure, forum |
| Setting up a company, GAFI, free zones, incorporation documents | `egy-company-setup` | |
| Hiring, employment contracts, probation, leave, termination | `egy-employment-contract` | **Employer side** |
| Unpaid wages, unlawful dismissal, severance, filing a labour claim | `egy-employment-dispute` | **Employee side.** Same law, different entry |
| Invoices, payment terms, late payment, cheques, collection | `egy-invoice-and-payment-terms` | |
| Online shop, consumer disclosures, returns, e-commerce Arabic rule | `egy-ecommerce-compliance` | |
| Drafting an إنذار, demand letter, notice to vacate, employment warning | `egy-legal-notice` | Supplies the *templates* other skills reference |
| Lease review, rent increase, old vs new tenancy, eviction grounds | `egy-rental-agreement` | |
| Tax registration, VAT, ETA e-invoicing, records for audit | `egy-tax-and-einvoicing` | Carries **no rates** by design |
| Which court, fees, filing, service, appeal, enforcement | `egy-court-filing-guide` | |
| Explaining legal material to a non-lawyer, client updates, plain Arabic, "what does this mean for me" | `egy-client-explanation` | Owns the **register** rules. ⚠️ States no law itself |
| Building a chronology or timeline from a matter file, statement of facts, date disputes | `egy-chronology-builder` | Owns date provenance and deadline computation |
| Deciding whether to **sign** a commercial contract (not reviewing it) | `egy-commercial-contract-review` → `references/RISK-GRID.md` | The founder-facing half of the flagship. **Not** a separate skill — see the 40% rule in `roadmap.md` |
| Arrest, police custody, bail, pretrial detention, "how long can they hold him" | `egy-criminal-procedure` | ⚠️ **The one skill that must open by saying the law is mid-change** — Law 150/1950 governs; Law 174/2025 applies **1 Oct 2027** |
| Report a crime, محضر vs بلاغ vs شكوى, complaint deadlines, the victim's civil claim | `egy-criminal-procedure` | ⚠️ Owns the **three clocks**. Cross-references `egy-chronology-builder` for date provenance |
| Criminal appeal, cassation, felony appeal after conviction | `egy-criminal-procedure` → `egy-court-filing-guide` | Criminal first (the 10/40/60-day clocks), then the filing mechanics |

---

## Deliberate adjacencies (not duplicates)

Two pairs look like overlap and are not:

**`egy-employment-contract` vs `egy-employment-dispute`** — same statute
(Law 14/2025), opposite side of the table. One is "how do I hire and terminate
lawfully", the other is "I was dismissed / I'm owed wages". Keep them separate: a
merged skill would give an employee the employer's framing, which is how someone
talks themselves out of a claim.

**`egy-legal-notice` vs `egy-rental-agreement` / `egy-employment-contract`** — the
notice skill owns the **templates**. The others reference it rather than duplicating
a template. If you add a new notice type, it goes in `egy-legal-notice`, not in the
calling skill.

---

## Cross-skill citation graph

`egy-context-operations` and `egy-legal-research` are cited by nearly every other
skill. Changes to either propagate widely — grep before editing.

References point at **the English sibling by default**, including from Arabic skills,
because `references/` only exists in EN for most topics. The Arabic twins carry their
own `references/` only where the material is language-dependent (glossary, templates,
audit grids, clause checks, risk grids). Five AR twins have their own today:
`egy-commercial-contract-review-ar` (3), `egy-context-operations-ar` (3),
`egy-ecommerce-compliance-ar` (2), `egy-employment-contract-ar` (1),
`egy-legal-notice-ar` (1).

---

## Planned skills — proposed routing

> For the porting work in `roadmap.md`. **Check against the table above before
> building** — several candidates partly overlap existing skills.

| Candidate | Would load on | Overlap risk |
|---|---|---|
| `egy-nda-review` | "review this NDA", confidentiality clauses | ⚠️ High — `egy-commercial-contract-review` already covers NDAs. Add only if the NDA material outgrows a reference file |
| `egy-family-law` | marriage, divorce, custody, inheritance, personal status | None — empty category today |
| `egy-ip-registration` | trademark, patent, copyright registration in Egypt | None — WIPO Lex has verified EN translations |
| `egy-debt-recovery` | enforcing a debt, execution, garnishment | ⚠️ Medium — overlaps `egy-invoice-and-payment-terms` (contract side) and `egy-court-filing-guide` (execution side). Would need a clear boundary |
| `egy-real-estate-purchase` | buying property, registry, notarisation, title check | ⚠️ Medium — overlaps `egy-rental-agreement` on the الشهر العقاري mechanics |

**Rule for new topics:** if a candidate is more than ~40% covered by an existing
skill, extend that skill's `references/` instead of creating a new directory.
