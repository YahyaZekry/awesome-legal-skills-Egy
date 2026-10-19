# History

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> **Append-only.** Never delete entries. Mark removals with ~~strikethrough~~.

---

## Removed

- ~~Egyptian versions of `california-bar-complete`, `icelandic-*`, ICTY / ECCC /
  Kosovo / Nuremberg tribunal skills, and the ISO / NIST / SOC 2 set~~ — never built.
  Rewriting an international criminal tribunal skill to Egyptian law produces
  something **worse than the original**, not a translation of it. Recorded in
  `EGYPT-EDITION.md` instead. *(decided: 2026-10-12)*

---

## Fixed

- **`EGYPT-EDITION.md` lines 86–108 — stale per-skill description tables.** Three
  entries contradicted the research that followed and were corrected:
  - *"Labour Law 12/2003 contract types"* → now **14/2025, which repealed 12/2003**
  - *"electronic litigation 172/2018"* → now flags that **Law 172/2018 is a Customs
    amendment**, not e-litigation
  - *"AlQalam… NTLEX"* → replaced with the actual source ladder (الجريدة الرسمية vs
    الوقائع المصرية, `elpai.idsc.gov.eg`, the MoJ encyclopedia, WIPO Lex) and the
    point that Cassation principles are **not binding precedent**

  Found by a structural scan during project-knowledge initialisation — the roster
  table and corrected sections were accurate; only these summary tables lagged.
  *(fixed: 2026-10-19)*

- **`egy-legal-notice/references/TEMPLATES.md`** — heading read *"The three hard
  rules"* over a **four-item** list. Corrected to "The four hard rules" in **both**
  EN and AR (`القواعد الأربع الصارمة`). *(fixed: 2026-10-13)*

- **`egy-court-filing-guide/SKILL.md`** — contained the corrupted string
  `**Economic Courts (محاكم ECONEconomic)**`, a generation artifact that shipped.
  Now `محاكم الاقتصادية`. *(fixed: 2026-10-13)*

- **`egy-rental-agreement/SKILL.md`** — heading read *"Arrears — and the one-year
  cure"* while its own body said the cure reaches arrears **worth more than five
  years**. Corrected to "the statutory cure". The Arabic agent rendered it without
  asserting either figure rather than propagating the contradiction.
  *(fixed: 2026-10-13)*

- **`skills/egy-context-operations/references/GLOSSARY-EN-AR.md` row 60** — the
  furnished-lease rule was **inverted**. Law 4/1996 Art. 2 applies the Civil Code to
  places *«خالية **أو مفروشة**»* — furnished leases were **not** carved out. The
  special regime (Law 49/1977 Arts. 39–48) touched **old-system** furnished leases
  only. *(fixed: 2026-10-12)*

- **`research/egyptian-corpus/03-employment-courts-aml-banking.md`** — judicial fee
  figures corrected to **≤ EGP 40,000 / ≤ 5,000 / ≤ 100,000** (Laws 191/2020,
  157/2024). *(fixed: 2026-10-12)*

- **`egy-legal-notice`** eviction guidance — corrected the conflation of lease expiry
  with eviction. A lease expiring is not an eviction: Civil Code **Art. 598** ends it
  automatically. *(fixed: 2026-10-12)*

- **`skills/egy-context-operations-ar/references/PORTALS.md`** — typo'd ITIDA domain,
  `itda.gov.eg` → `itida.gov.eg` (3 occurrences). ⚠️ **The first fix made it worse:** a
  blanket replace also "corrected" `itda.gov.eg/registry.aspx` and
  `itda.gov.eg/sgl.aspx`, which are **genuine working paths**. Caught by diffing URL
  sets against the English file and reverted. *(fixed: 2026-10-13)*

- Five **text-corruption incidents** in Arabic generation, repaired before shipping:
  stray Cyrillic / CJK / Portuguese fragments, repeated digit runs, duplicated words,
  and half-finished sentences. Arabic **blockquote templates** are the highest-risk
  region. *(fixed across 2026-10-12 → 10-13)*

---

## Decisions

- **Egypt skills are original work under `CC-BY-4.0`, not edits of upstream skills.**
  The repo is `CC BY-NC-ND 4.0` and some upstream skills are `AGPL-3.0`. Editing
  upstream directories would breach the licence **and** be silently reverted by the
  next sync. *(2026-10-12)*

- **All Egypt work lives in new `egy-*` directories.** `assets/.lawve-sync.json`
  tracks 264 upstream skills by UUID + digest and replaces them wholesale. Nothing
  under an existing directory is ever touched. *(2026-10-12)*

- **EN and AR ship as separate directories, not a language toggle.** The agent selects
  a skill purely on frontmatter `name` + `description`, so two directories is what
  makes an Arabic prompt resolve to an Arabic skill. *(2026-10-12)*

- **Arabic `description` must use YAML `>-` folded block style.** A single-line Arabic
  description containing a colon breaks YAML parsing and makes the skill invisible.
  Hit during the build. *(2026-10-12)*

- **Corpus-first: no skill is written before the law is retrieved and recorded.**
  Research overturned **30+ widely-repeated facts**, four of them in the operator's
  own initial briefs. Writing from recall would have made roughly **one claim in six**
  wrong, all sounding authoritative. *(2026-10-12)*

- **`egy-tax-and-einvoicing` carries no tax rates, deliberately.** Rates, thresholds
  and penalties are marked `UNVERIFIED` and the skill says so plainly. A rate quoted
  from memory into a tax document is worse than a gap. *(2026-10-13)*

- **Employment ships as two skills, not one** — `egy-employment-contract` (employer)
  and `egy-employment-dispute` (employee). A merged skill would give an employee the
  employer's framing, which is how someone talks themselves out of a claim.
  *(2026-10-13)*

- **Arabic twins for `egy-legal-notice` and others inherit the English sibling's
  reference paths** so the citation graph stays intact; `-ar` references/ exist only
  where the material is language-dependent (glossary, templates, audit grids).
  *(2026-10-13)*

- **Build Arabic twins sequentially, not in parallel.** Launching three simultaneous
  subagents hit rate limits **three separate times**. *(2026-10-13)*

- **`EGYPT-EDITION.md` is the roster's source of truth**, because
  `.claude-plugin/marketplace.json` is generated upstream and will be rewritten.
  *(2026-10-12)*

- **`.project-knowledge/` created** to carry build conventions, validators, the
  trigger map and the research backlog across sessions. *(2026-10-19)*

---

## The measurement worth remembering

Three shipped defects — a miscounted heading, a corrupted Arabic/Latin string, and a
heading contradicting its own body — all lived in **English** files and all survived
schema validation, contamination scanning, and a direct read-through.

**Each was caught by an Arabic agent reading the translation back against its
source.** That is the strongest argument in this project for building bilingually
rather than translating at the end: a single-language review catches content errors,
but it does not catch a file disagreeing with itself.
