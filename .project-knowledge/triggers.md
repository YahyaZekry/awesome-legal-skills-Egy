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
| Registering a brand, logo, patent, design; what IP costs in Egypt | `egy-ip-registration` | Organised by **goal**, not by Book. ⚠️ **Refuses to quote a fee without a date** |
| Someone is copying you — counterfeit goods, pirated software, a stolen brand | `egy-ip-registration` → `egy-criminal-procedure` | IP first (the 8/15-day post-seizure deadlines, customs), then the criminal mechanics |
| A book, album, film or software is being licensed, published or assigned | `egy-ip-registration` | ⚠️ **Owns the Art. 185 recordal rule** — protection is automatic, but the *deal* binds nobody until recorded |
| Marriage or its documentation — the 18 rule, mahr, قائمة المنقولات, عرفي marriages | `egy-family-law` | ⚠️ **Opens by correcting the home of the rule**: Art. 31 bis of **Law 143/1994**, ❌ not the Child Law; sanction is **disciplinary**. عرفي: divorce and نسب reachable, money usually lost on denial |
| "He said you're divorced" — طلاق, مراجعة, the paperwork | `egy-family-law` | Owns **Art. 3** (three-in-one = ONE divorce), the **30-day documentation duty**, and the proof rules of Law 1/2000 Art. 21 |
| A wife wants out — choosing between خلع and judicial تطليق | `egy-family-law` | The route table is the answer: خلع costs **her own financial rights** and is **بائن**, non-appealable, **children's rights survive**; the non-maintenance divorce is **رجعي** — the trap |
| Maintenance — claiming it, the arrears bar, the collection ladder, the criminal complaint | `egy-family-law` → `egy-criminal-procedure` | Owns the **one-year arrears bar** and the **four-step ladder in its order** (Fund → deduction → Art. 76 bis 30-day imprisonment → Penal Code Art. 293 complaint **last**). ⚠️ **The fine is EGP 5,000 since 2020**, ❌ not 500 — and 500/month is the **Fund cap**, a different thing |
| Custody, visitation, the children's housing | `egy-family-law` | Owns the **15-year rule** (girl and boy alike, then the child **chooses**, no custody wage from 15), «**ولا ينفذ حكم الرؤية قهراً**», and the **two SCC subtractions** on housing |
| Someone died — inheritance, wills, the withholding offence | `egy-family-law` | Shares need the **full family tree**. **الوصية الواجبة** in the same application. ⚠️ The withholding offence is **Law 77/1943 Art. 49 (Law 219/2017)**, ❌ not the Penal Code; ❌ no DNA statute |
| "The new family law" — is it law yet? | `egy-family-law` | **No — as of 28 Oct 2026** three bills sit in a joint committee. ⚠️ Also owns the confessional-structure rule: cite **promulgating Art. 3 of Law 1/2000**, never the repealed Law 462/1955 |

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
| `egy-debt-recovery` | enforcing a debt, execution, garnishment | ⚠️ Medium — overlaps `egy-invoice-and-payment-terms` (contract side) and `egy-court-filing-guide` (execution side). Would need a clear boundary |
| `egy-real-estate-purchase` | buying property, registry, notarisation, title check | ⚠️ Medium — overlaps `egy-rental-agreement` on the الشهر العقاري mechanics |

**Rule for new topics:** if a candidate is more than ~40% covered by an existing
skill, extend that skill's `references/` instead of creating a new directory.
