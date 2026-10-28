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

- **`skills/egy-context-operations-ar/references/PAYMENTS.md`** — the FRA domain had been
  **ejected out of its sentence into a stray fenced code block**, leaving the Arabic
  sentence ending on a dangling `:**` with nothing after it. The English reads *"Check the
  FRA register (`fra.gov.eg`) before naming a licensed lender in anything you write."*
  Restored inline to match. Found by the new URL set-parity check **on its first run** —
  a direct read-through had missed it. *(fixed: 2026-10-19)*

- **`.project-knowledge/scripts/validate.py` — five extractor bugs, all producing false
  failures, found before the checker was trusted.** Recorded because the same traps will
  recur on any Arabic text:
  1. **Arabic-Indic digits were never folded to ASCII.** `٦٧ لسنة ٢٠١٦` vs `67/2016`, so
     *every* law number looked missing from the Arabic side. Made silent by the fact that
     Python's `\d` **does** match Arabic-Indic digits — the extractor captured the
     numerals and they simply never compared equal.
  2. **`README.md` was included in the parity comparison.** It is a human-facing summary
     with no parity contract, and the English ones cite law numbers inline, so it
     manufactured hundreds of false "missing in AR" reports.
  3. **Arabic law numbers carry the law's name between the word and the number** —
     `قانون الإثبات رقم ٢٥ لسنة ١٩٦٨`. A `\s*` gap cannot cross a law's name.
  4. **`\bقانون` can never match inside `القانون`** — Arabic letters are word characters,
     so the *most common* citation form was invisible. The `\b` was the bug.
  5. **`ال?` means "alif, then optional lam", NOT "optional ال".** In `للمادة` the
     preposition's lam **assimilates** into the definite article and the alif disappears
     entirely, so that whole form failed to match — and with it Art. 604.

  Net effect: 29 reported failures, of which **zero** were real content defects.
  *(fixed: 2026-10-19)*

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

⚠️ **`egy-legal-notice/references/TEMPLATES.md` — one language was better, not wrong.**
The Arabic twin carried a `## المراجع` section (cross-links to sibling skills) that the
English lacked. **Fixed by giving the ENGLISH the same cross-links**, not by deleting the
Arabic section. Found by the **heading-structure check** on its first run — see
`validators.md` §3a. *(fixed 2026-10-19)*

⚠️ **`06-criminal-procedure-egypt.md` — a corpus file that looked finished and was not.**
The file ran to **1,102 lines with 177 verified markers** and read as complete. It was
**not**: nine forward references pointed at a **`§16` that did not exist**. *(fixed
2026-10-19)* — and the diagnosis was better the second time. The first read said
*"section 16 is missing"*. The agent sent back to fix it found the real defect: **§16
did exist — it was the Emergency Law section — and the nine references meant the *new
code* material, which was never written at all.** The fix was to **correct the
references and write the missing §17**, not to renumber anything. **A dangling
cross-reference is a numbering error until proven otherwise.** The file is now **1,715
lines / 258 verified**, with §17 covering Law 174/2025 article by article.

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

- **Registering the Egypt skills: append to `.claude-plugin/marketplace.json` through an
  idempotent generator — not a separate manifest.** A separate manifest is **not possible**:
  Claude Code discovers a marketplace only at `.claude-plugin/marketplace.json`, one per
  repo, so the entries have to live in that file. Durability comes from the script instead —
  `register-egypt.py` is re-runnable, restoring the 12 entries after any `upstream/main`
  merge with no duplicates and upstream order untouched (verified byte-identical on re-run).
  *(2026-10-19)*

- **`register-egypt.py` edits the file as text, not as JSON.** `json.dumps(indent=2)` does
  **not** reproduce the upstream file (243 KB vs 235 KB — the real one keeps `skills` arrays
  inline), so a round-trip would reformat all 264 upstream entries. Textual injection gives a
  **+156 / −0** diff for a 12-entry change. *(2026-10-19)*

- **12 plugins, each listing both language directories — not 24.** Skill selection happens on
  frontmatter, so an English prompt never loads the Arabic skill even though it is installed.
  One install serves both languages. *(2026-10-19)*

- **One new category: `Property Law`.** The upstream 26 have no bucket for a residential
  lease, and filing it under "Commercial Law" would be wrong. The planned
  `egy-real-estate-purchase` needs the same bucket, so the addition pays for itself twice.
  *(2026-10-19)*

- **`validate.py` separates FAIL from WARN deliberately.** FAIL is reserved for what is
  unambiguously wrong and always fixable — unparseable frontmatter, dangling references,
  contamination, a missing EN/AR twin, a URL present in only one language, a registration
  entry pointing at nothing. Article- and law-number differences are WARN, because Arabic
  inflects, prefixes, abbreviates and uses list constructions, so the extractor has
  **documented blind spots** and a warning is not proof of a defect. A gate that cries wolf
  teaches everyone to ignore it. *(2026-10-19)*

- **A ported skill must be *method-first*.** Both new Track 2 skills assert almost no new
  Egyptian law; they point at skills that have verified it. That is what makes a port
  cheap to add safely — the risk in porting is not the method, it is the jurisdiction
  assumptions smuggled in with it. `chronology-builder` is the worked example: its
  *method* (source per entry, privilege screen, significance tagging) is neutral, but its
  core safety mechanism was **CPR 31.22**, and translating that would have imported an
  English procedure Egypt does not have. *(2026-10-19)*

- **Port judgment: 2 ported, 1 extended, 2 rejected — and the rejections matter more
  than the ports.** `disclosure-list` was rejected because Egypt has **no disclosure
  regime**, so an Egyptian version would have to *invent* a procedure rather than
  translate one. `case-briefer` was rejected because it is US legal *education* and
  presumes **binding precedent**, which Egyptian Cassation principles are not. A port
  that quietly asserts a procedure or a doctrine Egypt does not have is worse than no
  port, because it looks authoritative. *(2026-10-19)*

- **`contract-risk-analyzer` was extended, not ported.** Its overlap with
  `egy-commercial-contract-review` exceeded the ~40% rule, so it became
  `references/RISK-GRID.md` on the existing skill rather than a 13th directory. The
  Egyptian value-add is the **defaults** column: the Civil Code is supplétive, so
  omitting a clause **chooses the default**, and the default is often worse than what
  could have been negotiated. Art. 226 is the clean example — it sets the default
  interest rate, and it differs between a civil and a commercial agreement.
  *(2026-10-19)*

- **The Arabic twin rule is narrower on disk than the schema says.** `schema.md` calls
  `README.md` REQUIRED, but 11 of 14 AR twins have none — and the AR twins that carry
  their own `references/` are only those whose material is **language-dependent**
  (glossary, templates, audit grids, clause checks, risk grids); the rest cite the EN
  sibling. **Match the disk, not the schema**, and note the discrepancy rather than
  "fixing" 11 directories. *(2026-10-19)*

- **A corpus file is not finished because it is long.** `06-criminal-procedure-egypt.md`
  arrived at 1,102 lines with 177 verified markers and a plausible shape, and was still
  **incomplete and internally inconsistent**. A length-and-markers check would have passed
  it. ⚠️ **Check corpus files for dangling cross-references and a truncated final
  paragraph before using them** — `grep -c '§'` against the actual headings, and read the
  last line. An agent that stops mid-write leaves a file that reads like a finished one.
  *(2026-10-19)*
- **When a cross-reference dangles, suspect the NUMBER, not the missing text.** The
  first diagnosis was *"§16 was never written"*. It was wrong: §16 existed and was
  occupied by a different topic, and the nine references were pointing at unwritten
  material that belonged in a **new §17**. Correcting the references *and* writing §17
  preserved §16's intact subsections; renumbering would have broken them. **Read the
  headings before concluding a section is missing.** *(2026-10-19)*

- **A corpus file that says "I could not verify this" is more useful than one that
  guesses — and it must be *delivered* that way.** `08-intellectual-property-egypt.md`
  ended with **24 `🟡` items, each naming what was searched**, and **22 `❌` findings that
  affirmatively contradict the common citation** — including two amending laws
  (**131/2003**, **5/2010**) that **do not exist**, and a fee schedule that **cannot be
  found because it is not published**. ⚠️ **The skill says so, in the client-facing text,
  rather than quoting a number.** An Egyptian trademark fee quoted without a date is not
  information; giving the **ceiling, the layers and the date** is. *(2026-10-19)*
- **A `❌` finding is a deliverable, not a gap.** The IP file's most valuable content is
  the list of things that **do not exist**: the phantom amending laws, the ITIDA
  free-zone/export exemption, a separate software chapter, a sale or smell mark, a
  geographical-indication register. **Each one is something a model or a website will
  assert confidently**, and each one cost a search to refute. **Search for the
  non-existence of a widely-repeated fact, and record it as a finding.** *(2026-10-19)*

- **Check what survived on disk before re-doing work.** The family-law corpus was
  written during a session that then died on rate limits, twice; the checkpoint
  summary recorded *"nothing on disk"* — yet `07-family-law-egypt.md` surfaced at
  1,810 lines, **complete** (proper §13 trap-list ending, closing paragraph intact).
  The same thing had already happened once with corpus 08. ⚠️ **A lost checkpoint is
  not a lost file**: run `wc -l`, `grep -n '^#'` and read the last line before
  relaunching anything. *(2026-10-28)*

- **The §-reference checker must allow three heading levels.** The family corpus uses
  `### N.N.N` sub-sub-headings legitimately — **11 of them** (e.g. §3.3.3 نشوز,
  §4.5.2 automatic deduction, §4.5.4 the criminal complaint). The first set-diff
  reported three dangling references; the extraction regex was truncating at
  `#{1,2}` and again at a two-dot number pattern. ⚠️ **Fix the checker, not the
  corpus**: a `§N.N.N` citation is an error only when no heading at any level carries
  the number. *(2026-10-28)*

- **Re-check the volatile claim on the file's own as-of date.** The family corpus
  went to disk as of 2026-10-19; committed on 2026-10-28. Rather than silently
  trusting the older date, the single most volatile proposition — *no new
  consolidated personal-status law* — was **re-verified against fresh reporting**
  (24 Oct and 28 Aug 2026 pieces still describing the three bills as drafts), and
  the file carries a **dated re-check line** in §1.2 saying so. ⚠️ **A corpus can
  be committed late without becoming stale — if the staleness question is asked and
  the answer is written into the file.** *(2026-10-28)*

- **Family law is where the confessional structure first becomes load-bearing.**
  Every commercial skill could cite one statute; family law cannot. The corpus
  establishes: personal status is allocated by **promulgating Art. 3 of Law 1/2000**
  (Muslims → statutes + **أرجح الأقوال الحنفية**; non-Muslims → their own shari'a;
  unified for all Egyptians → **inheritance, wills, capacity**), and **Law 462/1955
  was repealed by promulgating Art. 4** — so citing 462/1955 as the current rule is
  a real error, not a stylistic one. The skill refuses to give Hanafi-default
  doctrine (custody disqualifications, بطلان grounds, the wali) article numbers,
  and refuses cross-confessional advice. *(2026-10-28)*

---

## The measurement worth remembering

Three shipped defects — a miscounted heading, a corrupted Arabic/Latin string, and a
heading contradicting its own body — all lived in **English** files and all survived
schema validation, contamination scanning, and a direct read-through.

**Each was caught by an Arabic agent reading the translation back against its
source.** That is the strongest argument in this project for building bilingually
rather than translating at the end: a single-language review catches content errors,
but it does not catch a file disagreeing with itself.

## Added 2026-10-28 (Track 3 close-out)

- **The duplication scanner caught a true-positive that was not a typo.**
  «المواد ٩ و١٠ و١١ و١٢ و١٢ مكرر» — Art. 12 *and* Art. 12 bis written adjacently —
  was flagged as a duplicated word (`و١٢ و١٢`). The content was correct; the scan
  cannot see the بيس distinction. Rephrased («المواد ٩ إلى ١٢ و١٢ مكرر») rather than
  weakening the scanner: the rule stays strict, the prose adapts. *(2026-10-28)*

- **Verify the "current" figure against the amendment footnotes, not the displayed
  text.** The consolidated Commercial Code text shows the cheque presentation period
  as **six months (domestic)** — and its own footnote records that Law 156/2004
  replaced the paragraph. A government page quoting "3 أشهر" is the pre-2004 text.
  Both "the displayed text" and "the memory" were wrong in different ways; the
  footnote chain was the truth. *(2026-10-28)*

- **A phantom instrument can survive two independent searches.** "Law 10/1953"
  (أمر بالإحضار) returned nothing relevant twice, across different query shapes —
  and the phrase itself belongs to the regional CPC family. Treat "could not locate
  the instrument" as a finding to record (❌), not as an excuse to keep searching.
  *(2026-10-28)*

- **One law number, two statutes.** Two Egyptian laws are numbered 143 —
  143/**1981** (desert lands) and 143/**1994** (civil status). A third, "143/2017
  registration law", circulates and does not exist. When a year-and-number citation
  fails to resolve, check whether the *number* belongs to a different year before
  concluding the law does not exist. *(2026-10-28)*

- **Per-plugin versions in the register script.** A single global `VERSION` would
  rewrite seventeen unchanged entries' version strings on every bump. A
  `PLUGIN_VERSIONS` dict keyed by plugin name defaults to the global and lets each
  build stamp only its own plugins — re-runs stay byte-identical for everything
  else. *(2026-10-28)*
