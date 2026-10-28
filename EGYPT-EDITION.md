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
| `egy-client-explanation` | ✅ | ✅ |
| `egy-chronology-builder` | ✅ | ✅ |
| `egy-criminal-procedure` | ✅ | ✅ |
| `egy-ip-registration` | ✅ | ✅ |
| `egy-family-law` | ✅ | ✅ |
| `egy-real-estate-purchase` | ✅ | ✅ |
| `egy-debt-recovery` | ✅ | ✅ |

**19 skills × 2 languages = 38 directories, 76 markdown files, 15,683 lines.**
**Verified corpus: 10 files, 12,902 lines.**

All ten corpus files are complete and committed — every one mechanically checked
(no dangling section references, proper ending) and content-verified against
retrieved primary text. `07-family-law-egypt.md` — the most misinformation-heavy
topic — carries a dated re-check line: as of **28 October 2026** there is still
**no new consolidated personal-status law**; three bills sit in a joint committee.
`09-real-estate-purchase-egypt.md` and `10-debt-recovery-egypt.md` are built on the
**2026-10-28** source pass (Law 151/2026's transfer tax, Law 3/2026's property-tax
exemption, the CPC full text and the Commercial Code consolidated cheque block).

Final validation: 0 pairing orphans, 0 frontmatter/reference failures, 0 contamination.

### Shared foundation
| Skill | Covers |
|---|---|
| `egy-context-operations` | EGP, national ID / commercial-registry / tax formats, governorates, phone formats, portals (GAFI, customs, tax, social insurance, NTRA, CBE), e-signature & electronic seal, cheques, mobile wallets, what gets filed online vs in person, EN↔AR glossary |
| `egy-legal-research` | The two-gazette distinction (الجريدة الرسمية vs الوقائع المصرية), the source ladder from `elpai.idsc.gov.eg` and the MoJ encyclopedia to WIPO Lex, the portal false friends, Court of Cassation principles and why they are **not binding precedent**, how a citation gets verified |

### Method — how to do the work, not what the law says
| Skill | Covers |
|---|---|
| `egy-client-explanation` | Turning dense legal material into advice a non-lawyer can act on. ⚠️ **Explaining across a register, not a language** — the Arabic version is written, not translated. The gap between winning and collecting (execution is a separate stage). The numbers you must not honestly give |
| `egy-chronology-builder` | Building a chronology the matter can be argued from, **with every entry attributed to the document it came from**. ⚠️ Its upstream core was English **CPR 31.22** — replaced, since Egypt has no equivalent rule |

### Business
| Skill | Covers |
|---|---|
| `egy-company-setup` | GAFI incorporation (JSC / LLC / branches), free zones, the actual document list, what's notarised, realistic elapsed time vs official time |
| `egy-commercial-contract-review` | Clause-by-clause review under Egyptian law. NDAs, services, supply, distribution, SaaS. Parties, scope, price in EGP, delivery, penalties, penalty clauses, force majeure, governing law, dispute resolution, court vs arbitration |
| `egy-employment-contract` | Labour Law **14/2025** contract types (**which repealed 12/2003**), probation, hours, leave, social insurance 148/2019, the no-penalty cases, termination |
| `egy-invoice-and-payment-terms` | EGP invoicing, cheques & promissory notes, due dates, late payment, collection, keeping the evidence |
| `egy-ecommerce-compliance` | Consumer Protection 181/2018 mandatory disclosures, returns, data protection 151/2020 for an online shop |
| `egy-tax-and-einvoicing` | Tax registration, VAT, ETA e-invoicing, record-keeping |
| `egy-ip-registration` | Trademarks, patents, utility models, designs, copyright and trade secrets — **organised by goal, not by Book**. ⚠️ **Owns the Art. 185 recordal rule**: copyright protection is automatic, but **your licence or assignment binds nobody until it is recorded**. ⚠️ **Quotes no trademark fee without a date, because no current published schedule exists** |

### Personal
| Skill | Covers |
|---|---|
| `egy-legal-notice` | Drafting إنذار and demands — notices to vacate, debt demands, employment warnings. Tone, required content, what it legally starts, delivery |
| `egy-rental-agreement` | Lease review, old vs new lease, rent increases, renewal, eviction grounds, utility and maintenance split |
| `egy-employment-dispute` | Labour Court route, time limits, what evidence to gather, drafting a claim |
| `egy-court-filing-guide` | Court structure, which court has which case, the **EGP 40,000 / 5,000 / 100,000** limits, why the 2024–25 fee tariffs are **not statutory**, service deadlines, execution. ⚠️ **Law 172/2018 is a Customs amendment, not e-litigation** |
| `egy-criminal-procedure` | Arrest, the constitutional **24-hour rule**, the **mandatory lawyer** (Arts. 124–125), interrogation, pretrial detention and its **exact ceilings**, bail and its alternatives, **محضر vs بلاغ vs شكوى**, limitation, the victim's civil claim, and the appeal clocks. ⚠️ **The code in force is still Law 150/1950** — Law 174/2025 applies from **1 October 2027** |
| `egy-family-law` | The four divorce routes and how to choose, the money a divorcée is owed, maintenance and its **one-year arrears bar** plus the four-step collection ladder, custody and visitation (**never enforced by force**), the children's housing and its **two SCC subtractions**, inheritance and wills, the **Law 219/2017 withholding offence**, and the family courts. ⚠️ **Opens with the two structural traps**: there is **no new consolidated family law** (three bills in committee as of 28 Oct 2026), and personal status is **confessional** — cite promulgating Art. 3 of Law 1/2000, never the repealed Law 462/1955 |
| `egy-real-estate-purchase` | What a signed contract actually gives you (**not ownership** — registration at the الشهر العقارى passes title), the registry check, the **وعد بيع** and **POA-for-sale** traps, the Art. 35 مكرر utilities refusal, the possession route (Law 9/2022 Art. 10 مكررا, ≤500 EGP), real registration fees (tiers, **max 3,900 EGP**, ≤37 days), the **2.5% transfer tax** (Law 151/2026 Art. 43, 60-day window, unregistered contracts and heirs included), the property-tax **100,000 EGP exemption** (Law 3/2026), foreign buyers (Law 230/1996), restricted lands (agricultural, desert, **Sinai = void without approvals**), and the **one-year defect bar vs the ten-year structural guarantee** (CC Arts. 449/452/651) |
| `egy-debt-recovery` | The rule that **nothing can be taken except through a سند تنفيذي** (Art. 280), the **أمر الأداء** five-step route (Arts. 201–210) with its garnishment combo (Art. 210), conservatory attachment and garnishment at third parties (**the 15-day تقرير, the 8-day notice, the 3-year state-body renewal trap** — Arts. 316–352), what **cannot** be attached (Arts. 305–309 — **wages at one quarter**), every limitation clock in one table (15y/5y/7y/10y-judgment/1y-3y cheque/3y cheque-crime), the **bounced-cheque toolkit** (Art. 518 bank statement, Art. 525 attachment without bond, **Art. 534 crime and the صلح that extinguishes it**), the execution book (Arts. 274–488), and the debtor's side — the substitute-deposit release (Arts. 302/303) and protected assets |

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
| Marriage age sits in the Child Law | **Art. 31 bis of the Civil Status Law 143/1994** (added by Law 126/2008) — and its sanction is **disciplinary against the registrar only**; ❌ no "16 with the guardian's consent" exception exists |
| "أنتِ طالق ثلاثاً" = three divorces | **One** — Law 25/1929 Art. 3: a divorce coupled with a number falls once |
| The Art. 293 maintenance fine is EGP 500 | **EGP 5,000 since Law 6/2020** — the 500 text is pre-2020; **EGP 500/month** is the Family Insurance Fund's payment cap, a different thing entirely |
| Custody reverts to the father when the boy turns 15 | Custody ends at **15 for girl and boy alike** (Law 4/2005); **the child then chooses**, and from 15 there is **no custody wage** |
| "الوصية لوارث باطلة" | **One-third is valid to an heir** — Law 71/1946 Art. 37; only the excess waits for the heirs' consent after death |
| A visitation order is enforced with the police | **«ولا ينفذ حكم الرؤية قهراً»** — never by force; the sanction is temporary transfer of custody |
| "Egypt's new family law has passed" | **Not as of 28 October 2026** — three bills (Muslim family law, Christian family law, the solidarity Fund) sit in a joint parliamentary committee; the "EGP 200,000 child-marriage penalty" belongs to a 2022 draft that never became law |

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
touching a paywalled database. ⚠️ **It has been serving HTTP 500 since late
October 2026** — while it is down, the working substitutes are the Official
Gazette page scans at `moj.gov.eg:73/Doc/001/<id>.pdf` (needs `curl -k`, port 73;
they are images — read them as rendered pages) and `lawhub.info/eg/?p=NNNN` for
verbatim statute text.

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