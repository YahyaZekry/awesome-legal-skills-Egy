# Roadmap

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> **Pre-flight check: read this before starting any task.**

## Current Goal

Take the Egypt edition beyond the 12 completed EN/AR pairs: **port more upstream
skills, add Egypt-native topics the catalog doesn't cover (criminal procedure, family
law, IP registration), and make the skills installable as a plugin.** Alongside that,
close the **25 open UNVERIFIED legal items** below, since several would change a
skill's advice if wrong.

---

## Track 1 — Make it installable ⬅️ highest leverage

The 24 Egypt skills exist on disk but are **invisible to the plugin system**:
`marketplace.json` has **0** Egypt entries and is generated upstream.

- [ ] **Create a separate, non-sync-managed plugin manifest** so Egypt registration
      survives an upstream merge. Preferred over editing the generated file.
      *(added: 2026-10-19)*
- [ ] **OR** append 12 plugin entries to `.claude-plugin/marketplace.json` — viable
      because there is no CI in this fork (the sync arrives by merge), but expect a
      conflict on the next `upstream/main` merge. *(added: 2026-10-19)*
- [ ] **Verify the merge assumption** by reading how `lawve-ai` ships its sync, before
      committing to either approach. *(added: 2026-10-19)*
- [ ] Decide the plugin granularity: **24 separate plugins** (one per language) vs
      **12 plugins each listing both** `skills/egy-x` and `skills/egy-x-ar`.
      Recommend 12 — a plugin listing both directories lets one install serve both
      languages. *(added: 2026-10-19)*
- [ ] Assign a `category` per plugin — reuse the upstream 26 categories where possible
      (`Commercial Law`, `Corporate Law`, `Employment Law`, `Data Protection`,
      `Litigation`) rather than inventing a parallel taxonomy. *(added: 2026-10-19)*

## Track 2 — Port more upstream skills

264 sync-tracked upstream skills exist; 12 are ported. Before building any of these,
check `triggers.md` for overlap.

- [ ] Survey the 264 for candidates that are **jurisdiction-neutral or Egyptian-law
      compatible** — many are US-state-specific (e.g. `california-bar-complete`,
      `connecticut-divorce-planner`) and would be actively wrong for Egypt.
      *(added: 2026-10-19)*
- [ ] Highest-value likely ports: `contract-risk-analyzer`, `case-briefer`,
      `chronology-builder`, `disclosure-list`, `client-explanation-translator` —
      method skills rather than jurisdiction skills. *(added: 2026-10-19)*
- [ ] ⚠️ **Do not port** US-state procedure, tribunal, or ISO/NIST/SOC 2 skills. An
      Egyptian version of an international criminal tribunal skill is worse than the
      original. Already recorded in `EGYPT-EDITION.md`. *(added: 2026-10-19)*

## Track 3 — New Egypt-native topics

Categories in the upstream catalog with **no Egypt coverage at all**: Criminal Law,
Family / Personal Status, Intellectual Property, Immigration, Real Estate purchase.

- [ ] `egy-criminal-procedure` — arrest, bail, criminal complaint, police report.
      Zero overlap with existing skills. *(added: 2026-10-19)*
- [ ] `egy-family-law` — marriage, divorce, custody, inheritance, personal status.
      Zero overlap. Large and sensitive; expect heavy `🟡` marking. *(added: 2026-10-19)*
- [ ] `egy-ip-registration` — trademark, patent, copyright. **WIPO Lex carries
      verified English translations of Egyptian IP law**, so this is one of the
      best-sourced topics available. *(added: 2026-10-19)*
- [ ] `egy-real-estate-purchase` — buying property, registry, notarisation, title
      check. ⚠️ Medium overlap with `egy-rental-agreement` on الشهر العقاري mechanics;
      consider extending that skill's `references/` instead. *(added: 2026-10-19)*
- [ ] `egy-debt-recovery` — enforcing a debt. ⚠️ Medium overlap on both sides
      (`egy-invoice-and-payment-terms` for the contract, `egy-court-filing-guide` for
      execution). Needs a clear boundary before building. *(added: 2026-10-19)*

**Rule:** if a candidate is more than ~40% covered by an existing skill, extend that
skill's `references/` rather than creating a new directory.

## Track 4 — Engineering / infrastructure

- [ ] **Check in the five validators** as `scripts/validate.py`. Today they exist only
      in this folder and the session history — nothing enforces them on a new commit.
      *(added: 2026-10-19)*
- [ ] Add a **parity-check script** EN↔AR that runs on demand. This is the check that
      caught real shipped defects; it should not live in a chat transcript.
      *(added: 2026-10-19)*
- [ ] Consider a minimal CI workflow that runs frontmatter + contamination + parity.
      Note: `.github/workflows/` does not exist in this fork. *(added: 2026-10-19)*

---

## Known Bugs

- [ ] ⚠️ **`egy-employment-contract/references/` does not exist**, but its Arabic twin
      (`egy-employment-contract-ar/references/TEMPLATES.md`) does. Deliberate
      asymmetry or gap? Decide and document. *(found: 2026-10-19)*
- [ ] ⚠️ **README attribution fragility.** The `.project-knowledge` attribution block
      sits after `LAWVE_SYNC_END`, which should be safe — but `README.md` is a
      sync-managed file. Re-check after any upstream merge. *(found: 2026-10-19)*
- [ ] **Licence question unresolved.** Egypt skills are `CC-BY-4.0` while the repo is
      `CC BY-NC-ND 4.0` and some upstream skills are `AGPL-3.0`. Egypt skills were
      written as **original work** rather than edits precisely for this reason, but
      publishing publicly still needs a per-source licence check.
      *(found: 2026-10-12)*

---

## Research backlog — 25 open UNVERIFIED items

All are marked `🟡`/`⚠️` in their skill and **must not be stated as fact** until
checked against a primary source. Preferred source: the Ministry of Justice
encyclopedia at `serviceapi.egyptianlaws.com` (it carries SCC rulings inline), then
the ELP at `elpai.idsc.gov.eg`, then the relevant authority.

### Would change advice if wrong — prioritise

- [ ] 🟡 **VAT and income-tax rates, thresholds, and VAT registration thresholds.**
      `egy-tax-and-einvoicing` carries **no rates at all** because of this.
      *Source: ETA / VAT Law 67/2016.* *(added: 2026-10-12)*
- [ ] 🟡 **The current judicial fee schedule in practice**, and the 2024–25 Court of
      Appeal administrative tariffs **under challenge in ECESR Case 51843/79**.
      Affects `egy-court-filing-guide` and `egy-invoice-and-payment-terms`.
      *(added: 2026-10-12)*
- [ ] 🟡 **Exact day-precise tenancy sunset dates.** The statute says "7 years from
      entry into force"; the skill computes ≈5 Aug 2032 from 5 Aug 2025.
      *(added: 2026-10-12)*
- [ ] 🟡 **Whether the 15% rent increase began 1 September 2026.** Today is
      **2026-10-19** — this date has now passed, so it is checkable today.
      *(added: 2026-10-12)*
- [ ] 🟡 **The Law 164/2025 Art. 8 alternative-unit window** — press reports conflict
      (**1 July 2026** vs **12 April 2026**). Both dates have now passed. Verify with
      the Cabinet before advising anyone a window is open. *(added: 2026-10-12)*
- [ ] 🟡 **Whether Arts. 25 and 26 of Law 49/1977 bind leases newly signed after
      August 2025.** *(added: 2026-10-12)*
- [ ] 🟡 **The two Supreme Court judgments of 12 April 2025** (Cases 105/Y30 and
      273/Y24) — only the listing was found, not the holdings. They may matter.
      *(added: 2026-10-12)*
- [ ] 🟡 **Whether Law 159/1981 (Companies) has been amended after Law 4/2018.**
      Affects `egy-company-setup`. *(added: 2026-10-12)*

### Worth closing

- [ ] 🟡 **Criminal penalty for a landlord who cuts utilities or changes locks** — no
      tenancy-specific penal article found. Do not assert one. *(added: 2026-10-12)*
- [ ] 🟡 **Current penalties for late tax filing / non-registration.**
      *(added: 2026-10-12)*
- [ ] 🟡 **Whether e-invoicing integration has further staged mandates** beyond the
      expense-deduction rule. *(added: 2026-10-12)*
- [ ] 🟡 **Tax clearance certificate procedure and current validity period.**
      *(added: 2026-10-12)*
- [ ] 🟡 **Execution-judge article numbers within Law 13/1968.**
      *(added: 2026-10-12)*
- [ ] 🟡 **A verified e-litigation statute** — the commonly cited Law 172/2018 is a
      Customs amendment. *(added: 2026-10-12)*
- [ ] 🟡 **Current appeal and cassation time limits**, generally and for employment
      claims specifically. *(added: 2026-10-12)*
- [ ] ⚠️ **Overtime and penalty rates on bounced cheques** under CBE rules — the
      mechanism exists but the schedule was not retrieved. *(added: 2026-10-12)*
- [ ] ⚠️ **Prescription for rent** in the tenancy context. *(added: 2026-10-12)*
- [ ] ⚠️ **Whether the social insurance number equals the national ID** — widely
      asserted, **not confirmed**. Query NOSI using the national ID.
      *(added: 2026-10-12)*
- [ ] 🟡 **The social insurance transition** from Law 79/1975 to Law 148/2019 is by
      **category and progressive inclusion**, not a single date — check per employer.
      *(added: 2026-10-12)*

### Company-setup gaps (PARTIAL, not unverified)

- [ ] ⚠️ **Minimum-capital figures** are Chambers/practitioner sources, not article
      text. *(added: 2026-10-12)*
- [ ] ⚠️ **Operative incorporation-mechanics article numbers** in Law 159/1981.
      *(added: 2026-10-12)*
- [ ] ⚠️ **Realistic incorporation elapsed times** — practitioners contradict GAFI's
      published figures. *(added: 2026-10-12)*

---

## Deferred

- [ ] Truncated text in **Art. 125** (consequence of written refusal) retrieved from
      the employment corpus — re-fetch the full article. *(added: 2026-10-12)*
- [ ] **Rotate the Firecrawl API key** if this repo is ever published with session
      history attached — a key was pasted in plaintext in an earlier session.
      *(added: 2026-10-19)*
