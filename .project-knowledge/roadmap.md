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

## Track 1 — Make it installable ✅ DONE (2026-10-19)

The 24 Egypt skills existed on disk but were **invisible to the plugin system**:
`marketplace.json` had **0** Egypt entries and is generated upstream.

**Decision — append to `marketplace.json`, driven by an idempotent generator.**
A "separate manifest" is not possible: Claude Code discovers a marketplace only at
`.claude-plugin/marketplace.json`, at the repo root, one per repo. So the entries must
go in that file — and the durability problem is solved by script instead.

- [x] **`.project-knowledge/scripts/register-egypt.py`** injects the 12 entries.
      **Idempotent** — re-run it after any `upstream/main` merge and the entries are
      restored, with no duplicates and upstream order untouched. Verified byte-identical
      on re-run. Has `--check` for a dry run. Refuses to run if a skill directory is
      missing or the upstream file's shape has changed. *(done: 2026-10-19)*
- [x] **Edits text, not JSON.** `json.dumps(indent=2)` does NOT reproduce the upstream
      file (243 KB vs 235 KB — the real file keeps `skills` arrays inline). A round-trip
      would reformat all 264 upstream entries. Injection produces a **+156 / −0** diff.
      *(done: 2026-10-19)*
- [x] **Granularity: 12 plugins, each listing both `skills/egy-x` and `skills/egy-x-ar`.**
      One install serves both languages, and skill selection is per-frontmatter, so an
      English prompt never loads the Arabic skill even though it is installed.
      *(done: 2026-10-19)*
- [x] **Categories reuse the upstream 26**, with **one addition: `Property Law`** — a
      residential lease is not commercial law, and the planned `egy-real-estate-purchase`
      needs the same bucket. *(done: 2026-10-19)*
- [x] **Plugin names = the EN directory names.** Upstream convention is
      `<topic>-<author>`, but `egy-` is already unique against all 264 upstream names and
      is far clearer in a plugin list. *(done: 2026-10-19)*
- [ ] ⚠️ **Still to verify the merge assumption** by reading how `lawve-ai` ships its
      sync. The generator makes a conflict survivable rather than fatal, so this is now
      low priority. *(added: 2026-10-19)*

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

- [x] **`.project-knowledge/scripts/validate.py`** — all five checks in one runnable
      script, exit 1 on failure, safe to wire into CI. Run it before every commit.
      *(done: 2026-10-19)*
- [x] **The EN↔AR parity check is now a script**, not a chat transcript. It caught two
      real defects the moment it ran (see `history.md`). *(done: 2026-10-19)*
- [ ] Consider a minimal CI workflow that runs `validate.py`. `.github/workflows/` does
      not exist in this fork. Note that CI here would be **advisory only** — the sync
      arrives by merge, so nothing upstream reads it. *(added: 2026-10-19)*

### ⚠️ Read this before "fixing" a validator warning

`validate.py` splits findings into **FAIL** (unambiguously wrong, always fixable) and
**WARN**. Warnings are `review:` (a human should glance) or `drift:` (mention-count
differences, usually stylistic).

**A warning is not proof of a defect.** The extractor reads Arabic that inflects,
prefixes and abbreviates, so it has documented blind spots:

| Blind spot | Example seen in this repo |
|---|---|
| Article ranges with no preceding article word | `٣٩–٤٨ من القانون رقم ٤٩ لسنة ١٩٧٧` |
| Limbs written as Arabic prose, not a Latin letter | `البند ٣ من الفقرة الأولى من المادة ٣١` (EN: `Art. 31(1)(3)`) |
| List constructions naming "law" only once | `القوانين رقم ٤٩ لسنة ١٩٧٧ ورقم ١٣٦ لسنة ١٩٨١` — the later numbers have no `قانون` to anchor on |
| Ranges split differently between languages | EN `224–232` vs AR `224–225` |

**Never edit the Arabic to silence a warning without confirming against the source that
something is genuinely missing.** A confident wrong fix is worse than the warning,
because nobody re-checks a thing that now looks right. This is the same failure mode as
the overturned-facts table in `EGYPT-EDITION.md`.

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
