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
✅ **DONE (2026-10-19).** All five candidates were read before deciding; two were
ported, one became an extension, and two were rejected.

| Candidate | Outcome |
|---|---|
| `client-explanation-translator` | ✅ **Ported** → `egy-client-explanation` (EN+AR). Fully jurisdiction-neutral *method*, and it serves the actual user — a non-lawyer. Egyptian value-add: the register problem, winning-vs-collecting, the imported mental model, and the honesty rules for the four numbers clients ask for |
| `chronology-builder` | ✅ **Ported** → `egy-chronology-builder` (EN+AR). Its core safety mechanism was **CPR 31.22**, which is England-only, so that section was replaced rather than translated — Egypt has no disclosure regime for an implied undertaking to attach to |
| `contract-risk-analyzer` | ⚠️ **Extended, not ported.** >40% covered by `egy-commercial-contract-review`, so it became `references/RISK-GRID.md` (EN+AR) on the **existing** skill — the founder-facing half of the flagship. Stated the three Egyptian ceilings that change what a signed number is worth |
| `disclosure-list` | ❌ **Rejected.** CPR PD 57AD Models A–E, form N265. Egypt has no disclosure regime, so an Egyptian rewrite would be **inventing a procedure** |
| `case-briefer` | ❌ **Rejected.** US law-school education (memory jogger, LaTeX casebook chapters). Worse: it presumes **binding precedent**, and Egyptian Cassation principles are not binding |

⚠️ **Both new skills are deliberately method-first** — they assert almost no new
Egyptian law and instead point at skills that have verified it. That is why they were
cheap to add safely, and it is the shape a port should take.

- [x] **Register the new skills** in `register-egypt.py` and re-run it. Now **15**
      plugins / 279 total, re-verified byte-identical on re-run. *(done: 2026-10-19)*
- [ ] ⚠️ **Do not port** US-state procedure, tribunal, or ISO/NIST/SOC 2 skills. An
      Egyptian version of an international criminal tribunal skill is worse than the
      original. Already recorded in `EGYPT-EDITION.md`. *(added: 2026-10-19)*

## Track 3 — New Egypt-native topics ⬅️ in progress

Categories in the upstream catalog with **no Egypt coverage at all**: Criminal Law,
Family / Personal Status, Intellectual Property, Immigration, Real Estate purchase.

🔬 **Three corpus-research agents launched 2026-10-19** (criminal procedure, family law,
IP). They write **only** `research/egyptian-corpus/06-`, `07-` and `08-`; the skills are
written afterwards, from the finished corpus. **Do not write a skill for a topic whose
corpus file is still being written** — every legal proposition must trace to it.

- [ ] `egy-criminal-procedure` — arrest, custody, bail, complaint, public prosecution.
      Corpus: `06-criminal-procedure-egypt.md` 🔬 *building*
- [ ] `egy-family-law` — marriage, divorce, khul', custody, maintenance, inheritance.
      Corpus: `07-family-law-egypt.md` 🔬 *building*. ⚠️ **The most
      misinformation-heavy topic in Egyptian law** — most-discussed by non-lawyers and
      by campaigning organisations with a position. Expect heavy `🟡`. The key
      verification: **whether a new consolidated personal status law has actually
      passed**, since a reform was under active debate through 2024–2026
- [ ] `egy-ip-registration` — trademark, patent, copyright. Corpus:
      `08-intellectual-property-egypt.md` 🔬 *building*. **WIPO Lex carries verified
      English translations of Egyptian IP law**, so this is the best-sourced topic
      available. Note `RISK-GRID.md` §3 deliberately does **not** state IP scope and
      defers to this skill
- [ ] `egy-real-estate-purchase` — buying property, registry, notarisation, title
      check. ⚠️ Medium overlap with `egy-rental-agreement` on الشهر العقاري mechanics;
      consider extending that skill's `references/` instead. *(added: 2026-10-19)*
- [ ] `egy-debt-recovery` — enforcing a debt. ⚠️ Medium overlap on both sides
      (`egy-invoice-and-payment-terms` for the contract, `egy-court-filing-guide` for
      execution). Needs a clear boundary before building. *(added: 2026-10-19)*

**Rule:** if a candidate is more than ~40% covered by an existing skill, extend that
skill's `references/` rather than creating a new directory.

## Track 4 — Engineering / infrastructure

- [x] **`.project-knowledge/scripts/validate.py`** — all six checks in one runnable
      script, exit 1 on failure, safe to wire into CI. Run it before every commit.
      *(done: 2026-10-19)*
- [x] **The EN↔AR parity check is now a script**, not a chat transcript. It caught two
      real defects the moment it ran (see `history.md`). *(done: 2026-10-19)*
- [x] **`.github/workflows/validate.yml`** — runs `validate.py` and
      `register-egypt.py --check` on push to `egypt-edition`/`main` and on PRs.
      ⚠️ Warnings do **not** fail the build, deliberately: gating on a heuristic
      extractor would train everyone to ignore it, and then the real defect hides in
      the noise. Only FAILURES exit 1. Advisory only — the sync arrives by merge, so
      nothing upstream reads this. *(done: 2026-10-19)*
- [x] **Heading-structure parity** in `validate.py` — the level sequence of every file
      present in both languages must match exactly. It is the **only parity sub-check
      that is a hard failure**, because it is *structural*: it extracts nothing from
      inflected Arabic, so it has **no false-positive mode**. That is the shape to aim
      for in any future check. It found a real asymmetry within the hour.
      ⚠️ Its fence handling is load-bearing — every skill's "Output format" block
      contains a `#` heading inside a ```markdown template, so counting those would
      report a phantom mismatch on nearly every pair. *(done: 2026-10-19)*
- [ ] ⚠️ **Figures are still not verified — the largest remaining hole.** EGP amounts,
      deadlines, percentages and thresholds are compared by eye across 14 pairs. They
      are exactly the class of thing that is both **load-bearing** (a wrong deadline or
      a wrong 7% cap is a real defect) and **extractable** (numerals and dates are not
      prose). Highest-value check left to write, and it should be structural like the
      heading check rather than heuristic. *(added: 2026-10-19)*
- [ ] ⚠️ **"Heading agrees with its own body" should stay manual** — it compares a
      heading's *claim* against the list beneath it, which no extractor here can do.
      Still the highest-yield manual check: it found *"three hard rules"* over a
      **four**-item list, and *"the one-year cure"* over a body saying five years.
      *(added: 2026-10-19)*

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
- [x] ✅ ~~**Exact day-precise tenancy sunset dates**~~ — **RESOLVED 2026-10-19.** They are
      **computed, not printed** in the statute, and are now carried with that caveat:
      **5 Aug 2032** residential (Art. 2) · **5 Aug 2030** non-residential natural
      persons · **6 Aug 2032** repeal of Laws 49/1977, 136/1981, 6/1997 (Art. 9 —
      deliberately the *next* day, «من اليوم التالى») · **7 Mar 2027** expiry /
      **8 Mar 2027** vacate for the **Law 10/2022** track. ⚠️ The old «≈ April 2027»
      figure was **wrong by a month** and is corrected.
- [x] ✅ ~~**Whether the 15% rent increase began 1 September 2026**~~ — **RESOLVED
      2026-10-19: YES.** It is **self-executing** (Law 164/2025 Art. 6 read with Art. 4);
      no implementing instrument was ever needed. ⚠️ It runs on the **new** legal rent,
      not the pre-reform rent: 250 → **287.50**, 400 → **460**, 1,000 → **1,150**.
- [x] ✅ ~~**The Law 164/2025 Art. 8 alternative-unit window**~~ — **RESOLVED 2026-10-19:
      there was never a conflict.** It was a chain of three-month extensions, and the
      window **closed on 12 Oct 2026**. PM Decisions 53/2025 → 12 Jan 2026 · **4/2026**
      (Gazette 2 bis «ج») → 12 Apr 2026 · **24/2026** → 12 Jul 2026 · **59/2026**
      (Gazette 33, 13 Aug 2026) → 12 Oct 2026. ~102,000 applications. **No further
      extension found as of 2026-10-19. Do not tell a client a window is open.**
- [x] ✅ ~~**Whether Arts. 25 and 26 of Law 49/1977 bind leases newly signed after
      August 2025**~~ — **RESOLVED 2026-10-19: no.** On **SCC Case 85 of year 17
      دستورية (22 Mar 1997)**, for premises within Law 4/1996 Art. 1 the Civil Code
      applies alone. ⚠️ But a **continuation** lease (e.g. under Law 49/1977 Art. 29)
      is still an old-system lease, and there the two articles do bite until 6 Aug 2032.
      *(Added 2026-10-12)*
- [ ] 🟡 **The two Supreme Court judgments of 12 April 2025** (Cases 105/Y30 and
      273/Y24) — only the listing was found, not the holdings. They may matter.
      *(added: 2026-10-12)*
- [ ] 🟡 **Whether Law 159/1981 (Companies) has been amended after Law 4/2018.**
      Affects `egy-company-setup`. *(added: 2026-10-12)*

### ⚠️ Live challenge to the tenancy reform — new

- [ ] 🟡 **The 2026 constitutional challenges to Law 164/2025 are pending and unruled.**
      Cases **34/Y47** (Arts. 2, 7), **37/Y47** (Arts. 2, 4, 5, 6, 7), **38/Y47**,
      **43/Y47** (whole law, especially Art. 7) and a reported **21/Y48** are before the
      Commissioners; next session **8 Nov 2026**. ~1,700 annulment actions are pending in
      the administrative courts. **No merits ruling as of 2026-10-19.** ⚠️ A pending
      challenge does **not** suspend the statute — the standing warning in both
      `egy-rental-agreement` skills. *(added: 2026-10-19)*

### Worth closing

- [x] ✅ ~~**Criminal penalty for a landlord who cuts utilities or changes locks**~~ —
      **RESOLVED 2026-10-19, as a negative.** There is **no tenancy-specific penal
      article**, and the citation everyone uses is **wrong**: **Penal Code Art. 375
      bis** is the **البلطجة** article, and the widely-quoted wording «تعمد قطع المياه
      أو الكهرباء…» **is not in it** — it is a fabrication of the commentary layer.
      Also ruled out: **Art. 162 bis** (damage to *public* electricity lines) and
      **Law 49/1977 Art. 76** (closed list that **excludes** Art. 28). The remedies are
      **civil** — **Law 49/1977 Art. 28** plus Civil Code **Arts. 564/567/568/571/575**.
      ⚠️ Two further corrections: **Law 49/1977 Art. 77** is «بالحبس … **و**غرامة» —
      **imprisonment *and* a fine of double the amount, plus mandatory restitution**;
      both the "or" version and the "no restitution clause" claim are wrong. And
      **Law 136/1981 Art. 24** abolished the custodial limb, so on the Arts. 25/26
      limb the **fine** is the live sanction. ✅ Bonus verified: **Law 49/1977 Art. 81**
      is the landlord-side criminal article (acts endangering a building to have it
      treated as آيل للسقوط). *(added: 2026-10-12)*
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
