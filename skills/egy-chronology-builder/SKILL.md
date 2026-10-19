---
name: egy-chronology-builder
description: >-
  Build a litigation chronology for an Egyptian matter from the documents
  themselves — every entry attributed to the source document it came from, with a
  professional-secrecy screen, case-theory significance tagging, and the deadlines
  computed rather than narrated. Covers the three Egyptian date problems that break
  chronologies: Arabic-Indic numerals and day/month ordering, Hijri dates sitting
  alongside Gregorian on official documents, and the fact that under Law 25/1968
  Art. 15 some document dates are not provable against third parties at all. Use
  when the user asks to build a chronology or timeline from a matter file, court
  papers, police reports or witness statements, or says "build the chron",
  "what happened when", "statement of facts", "تسلسل زمني", "الوقائع",
  "صحيفة الدعوى", "ترتيب الأحداث", "محضر".
metadata:
  author: Egypt Edition (Lawve catalog)
  license: CC-BY-4.0
  version: 2026.10.19
---

# Building a litigation chronology — Egypt

**Not legal advice.** A chronology is a factual work product. It does not decide
anything, and it must never contain a conclusion it cannot attribute to a document.

## What this skill does

It turns a matter file into a dated, sourced, court-facing sequence. Three things
distinguish this from "make a timeline":

1. **Every entry carries its source document.** No entry exists without one.
2. **A date is not the same as a provable date.** See §2.3 — this is the part that
   makes an Egyptian chronology different, and it is the part people skip.
3. **The chronology is where limitation periods get computed**, so it is also where
   they get computed wrongly. See §5.

## 1. The one rule

> **Every entry cites the document it came from, by name and page. An entry you
> cannot attribute is an entry you cannot use.**

Write it as a column, not a footnote. A chronology whose entries cannot be traced
back is worse than no chronology, because it will be relied on.

If two documents give different dates for the same event, **record both and say
so**. Do not silently pick one. The discrepancy is itself a finding, and it is
often the most useful thing in the file.

## 2. The Egyptian date problem — where chronologies actually break

Three separate traps. All three are silent: the output looks fine.

### 2.1 Arabic-Indic numerals and day/month ordering

Egyptian documents commonly use Arabic-Indic numerals — `١٥/٣/٢٠٢٥`. Two failures
follow:

- **Transcription.** `١٥` is 15, not 15th-of-something-else. Modern OCR and casual
  copy-paste mangle these in both directions. Never retype a date; copy it, then
  verify the digits character by character.
- ⚠️ **Order ambiguity.** `١٥/٣/٢٠٢٥` is **15 March** in Egyptian practice
  (day/month/year). It is not May 3rd. But some bilingual and international
  documents in the same file *do* use month/day, and some use `٢٠٢٥/٣/١٥`.

**Rule:** never let a bare `x/y/zzzz` into the chronology. **Write every date with
the month spelled out** — `15 مارس 2025 (15 March 2025)` — and keep the source's
original string beside it. The spelled month is what makes the entry unambiguous
to a court and to the next person who reads the file.

### 2.2 Hijri dates sit alongside Gregorian on official documents

⚠️ Egyptian official and court documents frequently carry **both** a Gregorian and
a **Hijri (هـ)** date, and they are not always on the same line. This project hit a
worked example during tenancy research: a Cabinet decision of **30 July 2026** was
recorded on the instrument as **16 Safar 1448 H**.

Two consequences:

- **Convert both ways, and check the pair.** If the instrument states a Hijri date
  that does not correspond to the Gregorian date you recorded, one of them is your
  transcription error. The instrument is right.
- **Record the Hijri date in the entry too.** Where a period runs from an
  instrument, the instrument's own date is what matters, and it may be expressed
  only in Hijri.

### 2.3 ⚠️ Some dates are not provable at all — the part that matters most

This is genuinely distinctive and almost always missed. Under Egyptian law, a
document can exist, be genuine, and still **not prove its own date** against third
parties.

- ✅ **Proof Law — Law 25/1968, Art. 15.** An informal instrument (**المحرر
  العرفي**) is evidence of its **date** as against third parties only once it has a
  **fixed date** (**ثابت التاريخ**). A fixed date arises from: (a) registration in
  the register kept for it; (b) proof of its contents in another instrument of fixed
  date; (c) endorsement by a competent public officer; (d) the death of a signatory
  (where that has recognised effect), or the moment it becomes impossible for one of
  them to write or sign; (e) any other event conclusively showing the paper was
  issued before it.
  ⚠️ And the judge may, in the circumstances, decline to apply the article to
  **المخالصات** (advance-payment receipts).
- ✅ **Law 114/1946, Art. 12 bis** — for instruments that **must** be registered,
  **the date cannot be proved at all**: *«لا يقبل إثبات تاريخ المحررات الواجب
  شهرها»*. That is a sharper sanction than "not opposable", and it is stated as
  outright.

**What this means for the chronology:** a column called "date" is not enough. You
need to know, for each entry, **whether the date is provable and by what route.**

| Mark | Meaning |
|:----:|---------|
| ✅ **provable** | Fixed date exists — registered, notarised, or endorsed by a public officer |
| ⚠️ **own date only** | The document is dated but the date is not yet fixed against third parties. Note *how* it could be fixed |
| 🟡 **date contested** | The other side has a reason to dispute the date, or documents conflict |
| ❌ **date not provable** | Falls under Law 114/1946 Art. 12 bis — must be registered and is not |

⚠️ **Do not write "the contract is dated 3 March 2024" as though that ended the
question.** Write "the contract bears the date 3 March 2024; ⚠️ the date is not
fixed against third parties (Law 25/1968 Art. 15) — notarisation would fix it."

✅ **The cheap fix, and it is routinely skipped:** notarising a document gives it
**the force of an executive instrument** (قوة السند التنفيذي) under **Law 4/1996
Art. 2, second paragraph** (added by **Law 137/2006**), and it fixes the date. For a
lease, for a settlement, for an acknowledgment of debt — this is the single cheapest
risk mitigation available and it is the thing the chronology should flag as missing.

## 3. The privilege screen — what replaces the English implied undertaking

⚠️ **There is no Egyptian equivalent of the English CPR 31.22 implied undertaking.**
Do not import it. In England the concern arises because documents are obtained
through a **compulsory disclosure regime** and may then only be used for those
proceedings. Egyptian procedure has no such regime, so the English rule has nothing
to attach to.

The Egyptian concern is different, and it is **professional secrecy
(سرية المهنة)**:

- ✅ Lawyers' professional conduct is **statutory and detailed** under **Advocacy Law
  17/1983, as amended by Law 147 of 2019**. That amendment introduced a national
  qualifying examination (effective January 2021) and a **Code of Professional
  Conduct** approved by the Bar's General Assembly and **published in Al-Waqa'i
  Al-Misriyya — binding on members, with professional liability for breach**.
- ⚠️ **Professional secrecy is not absolute in Egypt.** In the AML context the
  statute expressly provides that a professional-secrecy claim asserted by
  intermediaries such as lawyers, accountants or financial intermediaries **is not
  accepted as grounds for withholding identification data**. Do not advise that
  anything marked privileged is therefore beyond reach.
- ⚠️ **Do not assume a "new Advocacy Law" exists.** The Bar's 2024–2025 advocacy-law
  project was **not enacted** as of this writing. Cite Law 17/1983 as amended by
  147/2019.

**Practical screen:** before an entry goes into a court-facing chronology, ask
whether the document underlying it is one the client is entitled to use in these
proceedings at all. Material a client obtained **through** a lawyer must be reviewed
before it is filed, not after. When in doubt, keep it in a separate annex and flag
it rather than deleting it — a chronology that has been quietly pruned is a
liability.

## 4. Significance tagging — the case-theory column

A chronology is not a list. Each entry carries a **significance tag** tying it to a
fact you must prove:

| Tag | What it supports |
|---|---|
| **Establishes** | The fact directly |
| **Contradicts** | A fact the other side asserts |
| **Fixates a date** | Starts or interrupts a period — see §5 |
| **Notice** | What a party knew, and when |
| **Damage** | Quantum: money out, loss suffered |
| **Gap** | Something that should exist and does not |

⚠️ **The `Gap` tag is the most valuable and the most often omitted.** A chronology
identifying that no written notice exists at all between two dates is often the
whole case. Absence of a document is a finding, and it can only be seen in a
chronology.

## 5. Deadlines — the part with real consequences

⚠️ A chronology is where limitation periods get computed. Getting it wrong here is
not a presentation error; it loses the claim.

- ✅ **Interruption.** Civil Code **Art. 383** — prescription is interrupted by a
  judicial claim, by **formal notice (التنبيه)**, by attachment, by a bankruptcy
  claim, or by any enforcement act during a suit. **Art. 384** — also by the
  debtor's acknowledgment, express or tacit.
- ✅ **Art. 387** — the court may **not** apply prescription of its own motion. The
  debtor must plead it. This is why an interrupted-by-notice entry is worth tagging
  precisely.
- ✅ **Art. 378** — wage claims carry a **one-year** limitation, with an oath
  requirement under **Art. 378(2)** where documentation is incomplete.
- ✅ **Official holidays extend the deadline.** Under **Law 13/1968 Art. 18** a
  period that would expire on an official holiday runs to the next working day.
  ⚠️ Service of process is itself restricted — **no service before 7 a.m., after
  8 p.m., or on an official holiday (Art. 15)**. See `skills/egy-legal-notice/`.

**Compute every deadline twice**, once forward from the trigger and once backward
from the claimed end date, and check the holiday calendar for **both** endpoints.
Record the holiday rule in the entry, so the computation can be audited.

⚠️ **Do not invent a limitation period you have not verified.** If the corpus does
not carry it, mark it 🟡 and say so. A chronology that asserts a wrong limitation
period is a trap for the client, because it looks authoritative.

## 6. Output formats

| Format | Audience | Notes |
|---|---|---|
| **Working** | The team | Every entry, every source, discrepancies preserved, privilege flags intact |
| **Statement of facts** | The court | Only entries supporting pleaded facts; every entry still sourced |
| **Witness** | A single witness | Filtered to what that witness can actually speak to, ⚠️ and to what they knew **at the time**, not what they learned later |
| **Internal risk** | The client | ⚠️ Never filed. Carries the `Gap` tags and the adverse entries |

⚠️ **When filtering to the court-facing format, filter — do not rewrite.** The
working chronology is the record of what you actually know. Editing it to produce
the filed version is how a file loses the ability to answer a question later.

## 7. Workflow

1. **Inventory the documents first.** List them before dating anything, so you know
   what is missing while you still can ask.
2. **Transcribe every date with the month spelled out**, keeping the source's
   original string beside it — §2.1.
3. **Convert Hijri where present**, and check the pair — §2.2.
4. **Mark provability for every entry** — §2.3. Flag missing notarisation.
5. **Run the privilege screen** — §3.
6. **Apply significance tags**, and look deliberately for `Gap` — §4.
7. **Compute the deadlines twice**, against the holiday calendar — §5.
8. **List every discrepancy** between documents as its own section. Do not resolve
   them; surface them.
9. **Then** produce the filtered formats.

## 8. What not to do

- ❌ **Never invent an entry to close a gap in the sequence.** A blank is a fact; a
  plausible invention is a fabrication that will be found.
- ❌ **Never silently prefer one document's date over another's.**
- ❌ **Never write a conclusion into a chronology.** It is a factual work product.
  Conclusions go in the pleading that cites it.
- ❌ **Never let a date appear without its source document.**
- ❌ **Never import English procedure.** No CPR 31.22, no "disclosure list", no
  "without prejudice". Egypt has none of these and using the vocabulary invites the
  wrong analysis.

## Output format

```markdown
# Chronology — [matter] / [الموضوع]

| # | Date (spelled) | Hijri | Event | Source document | Provable? | Tag |
|---|---|---|---|---|---|---|
| 1 | 15 مارس 2025 (15 Mar 2025) | — | ... | محضر / contract p.2 | ⚠️ own date only | Fixates a date |

## Discrepancies between documents
## Gaps — events with no document
## Deadlines computed
## Items flagged for legal review (privilege / usage)
## Documents referenced but not held
```

## References

- `research/egyptian-corpus/05-tenancy-egypt.md` — Law 25/1968 Art. 15 (fixed
  dates), Law 114/1946 Art. 12/12 bis (unprovable dates), Law 4/1996 Art. 2 ¶2
  (notarisation → executive force). **The source for §2.3**
- `research/egyptian-corpus/03-employment-courts-aml-banking.md` — Advocacy Law
  17/1983 as amended by 147/2019, professional secrecy and its limits (AML), Law
  13/1968 procedure
- `research/egyptian-corpus/01-commercial-corporate-contract.md` — Civil Code
  Arts. 383/384, 387, 378, and the interest and penalty-clause limits
- `skills/egy-legal-notice/` — service methods, service hours, the Art. 18 holiday
  extension. **Read before computing any deadline**
- `skills/egy-context-operations/references/GLOSSARY-EN-AR.md` — the EN↔AR
  vocabulary for document names
- `skills/egy-legal-research/` — how to verify a limitation period before asserting it
