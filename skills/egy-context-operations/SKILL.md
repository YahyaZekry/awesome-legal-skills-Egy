---
name: egy-context-operations
description: Practical operating context for Egypt that every other Egyptian-law skill builds on — Egyptian pound and FX risk, national ID and commercial-registry and tax numbers, Egyptian addresses and postal codes, phone and WhatsApp conventions, the official portals that actually work, electronic signature and electronic seal, cheques and mobile wallets and InstaPay, the Egyptian working week and the deadline-extension rule, and an English-Arabic glossary of the terms where naive translation changes the legal meaning. Use before drafting anything for an Egyptian audience, when filling an Egyptian form, when wiring a payment, or when a document needs to be in Arabic for an Egyptian authority. Triggers on "Egypt", "EGP", "Egyptian pound", "national ID", "commercial registry", "GAFI", "e-signature Egypt", "Egyptian cheque", "موظفة", "الجنيه", "السجل التجاري", "التوقيع الإلكتروني".
metadata:
  author: Egypt Edition (Lawve catalog)
  license: CC-BY-4.0
  version: 2026.10.12
---

# Egypt — practical operating context

The mechanical layer. Egyptian law tells you what is right; this tells you what
to actually type, which button to press, and which portal is not a lie.

**Everything here is verified against a live check on 2026-10-12.** Where a fact
was folklore rather than official, it says so. Read the markers — they are the
whole point of this skill:

| Marker | Meaning |
|---|---|
| ✅ **verified** | Checked against a primary or official source, or the URL was tested |
| ⚠️ **partial** | Real but uneven — usable, with a caveat |
| 🟡 **folklore** | Commonly repeated, not confirmed by an official source |
| ❌ **wrong** | A belief that is simply false. Do not repeat it. |

## Five things that are false and will cost you

These are the traps this skill exists to prevent. All are things a capable model
asserts confidently.

1. **Egypt has no postal code.** ❌ False. Egypt Post (بريد مصر) operates a
   national postcode standard — historically 5-digit, with a documented GIS-based
   **7-digit granular** layer. What is true is that **coverage and everyday use are
   inconsistent** and the code is **optional**; Egypt Post routes on
   **governorate + district**. So: don't require the field, and never invent a code.
   If a form forces it, put the district and governorate in full and leave the code
   blank.

2. **The CBE runs "CIPS".** ❌ There is no CIPS in Egypt — that is China's
   Cross-Border Interbank Payment System. Egypt's actual rails are **IPN / InstaPay**,
   **ACH**, **RTGS**, **EFT**, **CCH** (cheque clearing), **SWIFT**, **IBAN**, and the
   **Meeza** domestic card scheme.

3. **"Egypt's weekend is Friday–Saturday."** ❌ Operational error, and the
   correction depends on which institution you mean. **Government offices and most
   private sector: Sunday–Thursday.** Banks: Sunday–Thursday core, some branches
   later or on Friday. **Foreign-currency cheque clearing: Monday–Thursday only.**
   Shops and markets: effectively daily. → **Never compute an Egyptian deadline
   without knowing whose calendar applies.**

4. **The national ID has a published Luhn mod-10 check digit.** 🟡 The 14-digit
   structure is right. **The validation algorithm is not published anywhere official.**
   "Luhn mod-10" is undergraduate folklore from student slides. Do not build a
   validator on it. Governorate codes at positions 8–9 use a **fixed, non-contiguous
   set of 27 codes plus `88`** for births registered abroad — a parser that accepts
   `01–35` will admit codes that do not exist.

5. **`gcc.gov.eg` is the Official Gazette.** ❌ It returns **HTTP 200** and it is
   the **Cultural Development Fund**. A status-code check passes it. See
   `references/PORTALS.md` for what actually works.

## Currency

- **Egyptian pound, EGP, ج.م**, ISO 4217 `EGP` / numeric `818`. Never "Egyptian
  dinar".
- **قرش** (piastre, 1/100) is **dead currency** — nobody prices in it, but it still
  appears on cheque words-lines.
- **Amounts are written twice**: الأرقام (figures) and **بالحروف** (in words). Both
  are used on cheques; the words-line is the controlling one.
- **لا غير** ("and nothing more") closes the words-line on a cheque. **Omit it and
  the line is open to tampering.** This is a real forgery defence, not a formality.
- Writing an amount out in Arabic words is **تفقيط**.

**On FX** — the Egyptian pound has moved violently and recently (a float on
6 March 2024 took it from roughly 30.85 to roughly 49.4 against the USD in a matter
of weeks). **Never hard-code a rate.** In any contract or invoice that mixes
currencies, state: the currency, the rate source, the rate date, and **who bears
movement between the rate date and payment**. If nobody is told, the default is
contested.

## Identifiers you will actually be asked for

| What | Arabic | Note |
|---|---|---|
| National ID | **الرقم القومي** | **14 digits.** The master identifier. Not "civil number", not "national number". |
| Commercial Registry extract | **مستخرج السجل التجاري** | A **مستخرج** is a certified extract, not a copy — it has evidentiary weight of its own |
| Tax number / tax card | **الرقم الضريبي / البطاقة الضريبية** | Individuals and companies are different registrations |
| VAT registration | — | A **separate act** from income-tax registration. Registering for one is not registering for the other. |
| Social insurance number | **الرقم التأميني** | ⚠️ Do not assume it equals the national ID — unverified |
| IBAN | — | ✅ **Egypt uses IBAN.** Format: `EG` + 2 check digits + 3-digit bank code + 4-digit branch + 11 digits + account-holder national ID |
| Employment certificate | **كعب العمل** | Issued via Digital Egypt. Literally "the work's heel" — no English equivalent. Write "employment certificate (كعب العمل)". |

⚠️ **The two-track registry trap.** A company has **both** a **GAFI** registration and a
**traditional commercial-registry** entry, and they are not the same thing. A
commercial-registry number is **meaningless without its issuing governorate** — the
number alone does not identify the company. Ask which registry, and which governorate.

## Addresses

Write addresses the way Egyptians write them: **building number, street name,
floor, apartment, then district/markaz, then governorate, then country.** There is
no reliable unit above the building. Postal code is optional (see trap 1).

The **27 governorates** are in `references/GLOSSARY-EN-AR.md` alongside their
Arabic names — you will need the Arabic spelling, not the English transliteration,
on any form.

## Contact

- **Mobile: `+20 1X XXX XXXX`.** Landline area codes vary by governorate — use the
  international format `+20 X XXX XXXX`.
- **WhatsApp is the default business channel** in Egypt. A phone number given on a
  business card is usually a WhatsApp number. Assume messages there are informal and
  **not** a formal contractual notice — if it has to be a notice, use a channel you
  can prove delivery of.

## E-signature and what must still be signed by hand

✅ **Verified:** e-signatures in Egypt rest on **Law 15 of 2004** (not 15/2020 —
that number belongs to Saudi Arabia's e-commerce law) and the **executive
regulations issued by Ministerial Decree No. 109 of 2005**, dated **15 May 2005**,
published in the Egyptian Gazette (الوقائع المصرية) **issue 115 (Supplement)** on
**25 May 2005**. The operative regulations have since been amended, including by
**Ministerial Decision 361/2020**.

What you are actually obtaining, per ITIDA's own page: validity turns on **qualified
certificates from accredited certification authorities**, a published **RootCA trust
chain**, and the **ETSI technical annex**. It is **not** a general concept of
"electronic signature" that any scan of any signature satisfies.

**Still requires wet signature.** Do not assume a document can be signed
electronically because the portal has an upload button. Some categories stay on
paper — in particular instruments before a **كاتب عدلي** (judicial notary), and
court filings, which follow their own rules. Check the specific instrument; do not
generalise from "Egypt has e-signature law".

## Payments — see `references/PAYMENTS.md`

**Cash is still the centre of gravity.** That is not a preference, it is how the
economy runs, and it changes what evidence you need.

The short version:
- **Cheques are real and structurally different** from other markets. **Cheque
  clearing runs Monday–Thursday only.** Know what makes a cheque bounce.
- **Mobile wallets** — Vodafone Cash, **e&** (rebranded from Etisalat in 2022 — the
  CBE's own register still lists several wallets under legacy names), Orange Cash,
  WE Pay.
- **InstaPay** on the **Instant Payment Network (IPN)** — the default for
  person-to-person now.
- **Meeza** — the domestic card scheme.
- **Keep the evidence.** An **إيصال** (receipt) is proof of payment; a **تذكرة** is
  a ticket or voucher and is **not**. Confusing them loses the claim.

## Dates, deadlines and the rule that saves cases

✅ **Code of Civil and Commercial Procedures (Law 13/1968), Art. 18:**
> Where the final day of a time limit falls on an official holiday, **the time limit
> shall be extended to the first working day thereafter.**

- **Art. 15** — the day of service, or the day the limit starts, is **not counted**.
- Time limits in months or years run on the **Gregorian** calendar unless the law
  says otherwise.
- **Art. 15 (service)** — no service or enforcement may occur **before 7:00 a.m.,
  after 8:00 p.m., or on an official holiday**, except in necessity with the
  written permission of the Judge of Summary Matters.
  → **Never serve a paper on a public holiday.**
- Appearances: **15 days** before First Instance and Appeal, **8 days** before
  District Courts; reducible in necessity to 3 days and 24 hours.

⚠️ **"Working day" means a day that office or court is actually open** — driven by
its calendar and the holiday list, not by the weekday. **Do not compute the first
working day from the weekday alone.**

⚠️ **Never publish a future holiday calendar.** The Egyptian public holiday list is
Hijri-based and the Minister may substitute days. Describe the **rule**, look up the
actual dates for the year in question, and never assume next year's pattern.

## When to stop and get a lawyer

This skill tells you the mechanics. Get a qualified Egyptian lawyer — not a
consultant, not a translator, not this skill — before you:

- sign a **non-compete or exclusivity** clause, or anything restricting your right
  to work;
- accept a **penalty (غرامة) or liability cap** you cannot price;
- deal with **public property (أموال عامة)**, a government counterparty, or a public
  sector contract — arbitration with a state entity needs the **competent
  minister's approval** and is otherwise unenforceable;
- sign anything involving **real property or a registered lease** — the
  **الشهر العقاري** (real-estate registration) is a separate regime from the lease
  itself, and this is a common and expensive gap;
- are asked to make a **statutory declaration or give evidence** in court;
- receive anything that looks like a **legal notice (إنذار)** — the response window
  starts running, and in several contexts it is short.

## References

- `references/PORTALS.md` — every official portal, HTTP-tested, with the ones that
  are **false friends** called out
- `references/PAYMENTS.md` — cheques, wallets, InstaPay, and what evidence to keep
- `references/GLOSSARY-EN-AR.md` — the working vocabulary, with the terms where
  naive translation changes the instruction
- `research/egyptian-corpus/04-practical-operations-egypt.md` — the full verified
  source, including the URL register and what could not be confirmed