# Features

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> "Features" here = what the Egypt edition actually covers. Each entry lists the
> supporting files and, where relevant, the correction that made it non-obvious.

---

## Coverage by need

### Business

| Skill | Covers | Noteworthy |
|-------|--------|-----------|
| `egy-company-setup` | GAFI incorporation (JSC / LLC / branches), free zones, the document list, what's notarised, realistic elapsed time vs GAFI's published time | ⚠️ Minimum-capital figures are **PARTIAL** — Chambers/practitioner sources, not article text |
| `egy-commercial-contract-review` | Clause-by-clause review — parties, scope, price in EGP, delivery, penalty clauses, force majeure, governing law, court vs arbitration | **Flagship.** Carries the citation-traps table |
| `egy-invoice-and-payment-terms` | EGP invoicing, cheques & promissory notes, due dates, late payment, collection, evidence | **Art. 227(1)** caps agreed interest at **7%**; **Art. 224/225** make a penalty clause a *ceiling, not a floor* |
| `egy-ecommerce-compliance` | Consumer Protection **181/2018** disclosures, returns, data protection **151/2020** for an online shop | ⚠️ **Art. 5 requires Arabic** on ads/invoices/receipts/contracts; **Art. 28 voids any waiver clause** |
| `egy-tax-and-einvoicing` | Tax registration, VAT (Law **67/2016**), ETA e-invoicing, records for audit | ⚠️ **Carries no rates** — deliberately. See `roadmap.md` backlog |

### Personal

| Skill | Covers | Noteworthy |
|-------|--------|-----------|
| `egy-legal-notice` | Drafting **إنذار** and demands — notice to vacate, debt demand, employment warning | Owns the **templates** other skills reference. Tone, required content, what it legally starts, delivery |
| `egy-rental-agreement` | Lease review, old vs new regime, rent increases, renewal, eviction grounds, utilities and maintenance | ⚠️ **Law 164/2025 + 165/2025** rewrote this area in Aug 2025 |
| `egy-employment-dispute` | Labour claim route, limitation periods, evidence, the fee exemption | ⚠️ **Art. 378(2)** oath requirement decides most unpaid-wage cases |

### Employer

| Skill | Covers | Noteworthy |
|-------|--------|-----------|
| `egy-employment-contract` | Contract types, probation, hours, leave, social insurance, termination | ⚠️ Family supports: the **oral-contract file** (repealed Law 12/2003's types, now Law 14/2025) |
| `egy-employment-dispute` | (see above) | Same statute, opposite side of the table |

### Wiring

| Skill | Covers | Noteworthy |
|-------|--------|-----------|
| `egy-context-operations` | EGP, national ID / commercial-registry / tax formats, governorates, phone formats, portals, e-signature & electronic seal, cheques, mobile wallets, EN↔AR glossary (92 terms) | **Shared foundation** — cited by nearly every other skill |
| `egy-legal-research` | Source ladder, the two-gazette distinction, Court of Cassation principles, how to verify a citation | Records the Firecrawl failure mode |
| `egy-court-filing-guide` | Court structure, which court has which case, fees, filing, service, deadlines, execution | ⚠️ Refuses to quote a fee figure — see below |

---

## Legal findings that reshaped whole skills

These are not trivia. Each one changed a skill's advice.

**Tenancy — Law 164/2025 and Law 165/2025** (promulgated 4 Aug 2025, Gazette 31 bis,
in force 5 Aug 2025). They sunset the old regime on a statutory clock and created
Egypt's **first mandatory rent index** — **+15% annually by statute (Art. 6)**, not
subject to contract. Old-system residential leases end ≈**5 Aug 2032**.

**A lease expiring is not an eviction.** Civil Code **Art. 598** ends it automatically
at term end, and Law 136/1981 **Art. 18**'s closed list expressly excludes expiry —
because a lease expiring is not an eviction, it is the lease ending.

**Contract interest — Civil Code Art. 227(1)** caps agreed interest at **7%**, and
**Art. 224/225** make a penalty clause a ceiling rather than a floor.

**Prescription — Art. 387** means the court may **not** apply prescription of its own
motion; it must be pleaded. Against that, **Art. 383/384** define what *does*
interrupt it — and an informal WhatsApp demand does not.

**Employment — Labour Law 14/2025** repealed 12/2003 (in force 1 Sept 2025).
**Art. 7** exempts worker claims from judicial fees at every stage and allows
immediate execution without bail — the asymmetry that should shape every settlement.

**Hardship — Egypt has a Civil Code hardship clause (Art. 147(2))**, and it voids any
agreement to the contrary. The common assumption that Egyptian law has no hardship
remedy, as English law does not, is wrong.

**Fee thresholds — District Court first instance ≤ EGP 40,000** with finality ≤ EGP
5,000; Court of First Instance finality ≤ EGP 100,000. Amended twice
(Laws 191/2020, 157/2024), so material written earlier quotes stale figures.

---

## What was deliberately NOT ported

An Egyptian version of `california-bar-complete`, `icelandic-*`, the
ICTY / ECCC / Kosovo / Nuremberg tribunal skills, or the ISO / NIST / SOC 2 set would
be **worse than the original**, not a translation of it. A skill about an
international criminal tribunal is not an "Egyptian version" of anything.

Recorded in `EGYPT-EDITION.md`.

---

## The structural limitation

> The user of these skills is **not a lawyer**.

Every skill opens with a "not legal advice" line and keeps citations exact. The
design tension is real: hedging every statement would make the skills useless, so the
rule adopted is — **be decisive about law, explicit about uncertainty, and mark
anything unverified rather than softening it**. That is why the `🟡` markers and the
`Unverified` sections exist and are never quietly dropped.
