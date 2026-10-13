# Egypt Edition — build conventions

An Egyptian-law edition of the Lawve skill catalog. English and Arabic ship as
**separate skills**, not one skill with a language toggle, because the agent
selects a skill by its `name` + `description` in the frontmatter. Two directories
means an English prompt and an Arabic prompt each trigger the right one.

## Two things the sync will destroy

`.claude-plugin/marketplace.json` and the README block between
`<!-- LAWVE_SYNC_START -->` / `<!-- LAWVE_SYNC_END -->` are **generated** by the
Lawve sync job, which runs on its own schedule (`chore: sync public Lawve skills`).

1. **Never edit an existing upstream skill directory.** `assets/.lawve-sync.json`
   tracks each one by UUID + digest and overwrites it wholesale. An edit to
   `skills/nda-reviewer-jamie-tso` survives exactly until the next sync. All
   Egypt work lives in new `egy-*` directories, which are not in the tracked map.
2. **Never add Egypt skills to the synced README block** — the next sync deletes
   them. The Egypt edition gets its own section below `LAWVE_SYNC_END`, and its
   own `EGYPT-EDITION.md` (this file).

Consequence for `marketplace.json`: append the Egypt plugins at the end of the
`plugins` array, and expect upstream to rewrite that file. The Egypt edition is
therefore also registered in `EGYPT-EDITION.md` as the source of truth.

## Layout

```
skills/egy-context-operations/       EN  shared operational context (currency, IDs, portals, payments)
skills/egy-context-operations-ar/    AR  same, Arabic
skills/egy-<topic>/                  EN  one skill
skills/egy-<topic>-ar/               AR  its Arabic twin
```

`<topic>` is kebab-case, describes the task not the statute
(`egy-commercial-contract-review`, not `egy-law-72-2017`).

## Pairing rule

Every `egy-x` has exactly one `egy-x-ar`. They are **not** translations of each
other — they are the same skill written natively:

- The Arabic skill's `description` carries **Arabic trigger words** (راجع، عقد،
  إيجار، توظيف، شركة، شكوى) because that is what a user actually types.
- The English skill's `description` carries English triggers plus the common
  Arabic ones only where a bilingual user would plausibly mix.
- Body text, checklists, output templates and tables are written natively in each
  language. Legal citations keep the official Arabic name alongside the English
  translation in **both** languages — `قانون حماية البيانات الشخصية 151 لسنة 2020`
  never appears as "Law 151/2020" alone in the Arabic skill.

## Citation rule (non-negotiable)

Every legal proposition carries its citation, and every citation traces to
`research/egyptian-corpus/`. If the corpus marks something `UNVERIFIED`, the
skill must not state it as fact — it says so and tells the user to confirm with
the authority or an Egyptian lawyer. Egyptian law is amended often and a stale
article number is a real harm, not a cosmetic error.

## Roster

Each entry ships as two skills: `egy-x` (EN) and `egy-x-ar` (AR).

### Status — COMPLETE

| Skill | EN | AR |
|---|:--:|:--:|
| `egy-context-operations` | ✅ | ✅ |
| `egy-legal-research` | ✅ | ✅ |
| `egy-commercial-contract-review` | ✅ | ✅ |
| `egy-employment-contract` | ✅ | ✅ |
| `egy-employment-dispute` | ✅ | ✅ |
| `egy-company-setup` | ✅ | ✅ |
| `egy-invoice-and-payment-terms` | ✅ | ✅ |
| `egy-ecommerce-compliance` | ✅ | ✅ |
| `egy-legal-notice` | ✅ | ✅ |
| `egy-rental-agreement` | ✅ | ✅ |
| `egy-tax-and-einvoicing` | ✅ | ✅ |
| `egy-court-filing-guide` | ✅ | ✅ |

**12 skills × 2 languages = 24 directories, 54 markdown files, 8,860 lines.**
**Verified corpus: 5 files, 6,356 lines.**

Final validation: 0 pairing orphans, 0 frontmatter/reference failures, 0 contamination.

### Shared foundation
| Skill | Covers |
|---|---|
| `egy-context-operations` | EGP, national ID / commercial-registry / tax formats, governorates, phone formats, portals (GAFI, customs, tax, social insurance, NTRA, CBE), e-signature & electronic seal, cheques, mobile wallets, what gets filed online vs in person, EN↔AR glossary |
| `egy-legal-research` | AlQalam, the Egyptian Gazette, Court of Cassation seasonal principles, NTLEX, gazette-notice discipline, how a citation gets verified |

### Business
| Skill | Covers |
|---|---|
| `egy-company-setup` | GAFI incorporation (JSC / LLC / branches), free zones, the actual document list, what's notarised, realistic elapsed time vs official time |
| `egy-commercial-contract-review` | Clause-by-clause review under Egyptian law. NDAs, services, supply, distribution, SaaS. Parties, scope, price in EGP, delivery, penalties, penalty clauses, force majeure, governing law, dispute resolution, court vs arbitration |
| `egy-employment-contract` | Labour Law 12/2003 contract types, probation, hours, leave, social insurance 148/2019, the no-penalty cases, termination |
| `egy-invoice-and-payment-terms` | EGP invoicing, cheques & promissory notes, due dates, late payment, collection, keeping the evidence |
| `egy-ecommerce-compliance` | Consumer Protection 181/2018 mandatory disclosures, returns, data protection 151/2020 for an online shop |
| `egy-tax-and-einvoicing` | Tax registration, VAT, ETA e-invoicing, record-keeping |

### Personal
| Skill | Covers |
|---|---|
| `egy-legal-notice` | Drafting إنذار and demands — notices to vacate, debt demands, employment warnings. Tone, required content, what it legally starts, delivery |
| `egy-rental-agreement` | Lease review, old vs new lease, rent increases, renewal, eviction grounds, utility and maintenance split |
| `egy-employment-dispute` | Labour Court route, time limits, what evidence to gather, drafting a claim |
| `egy-court-filing-guide` | Court structure, which court has which case, fees, electronic litigation 172/2018, first appearance, Cassation |

## What the research overturned

Recorded because it is the argument for building the corpus first. Research
corrected **30+ widely-repeated facts** about Egyptian law — and **four of the
first ones were in my own initial briefs**, written from memory. Had the skills
been written from recall, roughly one claim in six would have been wrong and all
of them would have sounded authoritative.

| Common belief | Reality |
|---|---|
| Commercial Code 12/1943 | **17/1999** |
| Arbitration Law 34/1988 | **27/1994** |
| E-Signature Law 15/2020 | **15/2004** (regs: Ministerial Decree **109/2005**) |
| AML Law 40/2018 + Regs 1317/2018 | **80/2002** + PM Decree **951/2003** |
| Law 172/2018 is e-litigation | It amends the **Customs Law 66/1963** |
| Labour Law 12/2003 is current | **Repealed** — Labour Law **14/2025**, in force 1 Sept 2025 |
| A "Supreme Labour Court" exists | Specialised circuits inside the Court of Cassation |
| Egypt is FATF grey-listed | **It isn't** — MENAFATF enhanced follow-up |
| A "Cairo Convention 1994" on arbitration | **Doesn't exist** — confusion with the UNCITRAL Model Law adoption |
| A "Unified Arbitration Law 2023" | **Doesn't exist** |
| The regulator is a Data Protection "Authority" | The Personal Data Protection **Center** |
| Civil Code lease chapter is Arts. 543–587 | **Arts. 558–634** |
| Law 4/1996 carved out furnished leases | It did the **opposite** — "خالية **أو مفروشة**" |
| Egypt caps rent increase generally | **No Civil Code cap**; the old regime's formula is replaced by **+15% annually by statute** |
| Egypt has no postal code | It **does** — optional, inconsistent coverage |
| The CBE runs "CIPS" | That's **China**; Egypt runs IPN/InstaPay, ACH, RTGS, SWIFT, Meeza |
| Egypt's weekend is Fri–Sat | Government offices: **Sunday–Thursday** |
| `gcc.gov.eg` is the Official Gazette | It's the **Cultural Development Fund**, and returns HTTP 200 |
| `alqalam.idsc.gov.eg` is Egypt's legislation DB | **No DNS record** — use `elpai.idsc.gov.eg` |
| National ID has a published Luhn check digit | **Not published** — that's folklore |
| **Egyptian law has no hardship clause, like English law** | **Civil Code Art. 147(2)** has one, and voids any agreement to the contrary |
| District Court limit is EGP 200,000 | **EGP 40,000** (amended by Laws 191/2020, 157/2024) |

Two more that changed whole skills:

- **Law 164/2025 and Law 165/2025** (4 Aug 2025) sunset the old tenancy regime on a
  statutory clock and created Egypt's **first mandatory rent index**, +15% annually
  by statute, not subject to contract
- **A lease expiring is not an eviction.** Civil Code Art. 598 ends it automatically
  at term end, and Law 136/1981 Art. 18's closed list expressly excludes expiry

## A finding worth carrying forward

**Firecrawl's query mode silently returned the wrong articles twice** on the
official Arabic Civil Code PDF. Both times the output looked plausible and nothing
flagged it.

→ Download Arabic legal PDFs and extract the text locally. Verify against the
surrounding articles. If a retrieved article reads oddly, assume the tool is wrong
until you have checked the raw file.

The best single source found was the **Ministry of Justice legislation encyclopedia
at `serviceapi.egyptianlaws.com`**, which carries **Supreme Constitutional Court
rulings annotated inline** — two tenancy statutes were obtained from it without
touching a paywalled database.

## What gets an Egypt edition

| Class | Action |
|---|---|
| Jurisdiction-neutral (legal-ops methodology, verification, Office tooling) | No port. Optionally add a one-line `egy-context-*` pointer in `README.md`. |
| Generic workflow with a governing-law slot (contract review, NDA, DPIA, employment) | **Egypt edition.** |
| Subject is a specific foreign system (California bar, ICTY, `icelandic-*`) | No port. Never. |
| International standard (ISO, NIST, SOC 2, PCI) | No port; the standard is the same everywhere. |

The last two rows are not laziness. `california-bar-complete` teaches the MBE and
the California bar exam — an "Egyptian version" of it is a different and much
poorer skill. Rewriting the ICTY skills to Egyptian law would destroy them.

## Registering

Per the sync warning above, the Egypt edition is registered in **this file**, not
in the generated files. Append Egypt plugins to the end of `.claude-plugin/marketplace.json`
so they install from this repo today, and re-apply after any upstream sync wipes
them. The Egypt README section goes below `LAWVE_SYNC_END`.

When publishing: upstream Lawve only accepts submissions through
`lawve.ai/new/skill`, and every skill is manually reviewed. An Egypt edition that
derives from an existing upstream skill also needs that author's licence respected
— check `metadata.license` in the source `SKILL.md` (`AGPL-3.0`, `CC-BY-4.0`,
`Apache-2.0`, `MIT` and `CC-BY-NC-ND` carry different obligations, and the repo
itself is `CC BY-NC-ND`).