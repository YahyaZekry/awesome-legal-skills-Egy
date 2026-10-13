---
name: egy-tax-and-einvoicing
description: Egyptian tax and e-invoicing for a business — income tax and the tax card, VAT registration and VAT Law 67/2016, the ETA e-invoicing and e-receipt system and its integration deadline, what invoices must carry, revenue stamp, and keeping records that survive an audit. Use when setting up tax in Egypt, issuing invoices, integrating e-invoicing, or preparing for an ETA audit or clearance certificate. Triggers on "tax Egypt", "VAT", "e-invoicing", "tax card", "tax registration", "tax clearance", "ETA", "invoice requirements", "ضريبة", "ضريبة القيمة المضافة", "فاتورة إلكترونية", "البطاقة الضريبية", "السجل الضريبي", "إقرار ضريبي".
metadata:
  author: Egypt Edition (Lawve catalog)
  license: CC-BY-4.0
  version: 2026.10.12
---

# Tax and e-invoicing in Egypt

**Not legal advice, and this is the area where being wrong is expensive.** Get an
Egyptian accountant for registrations and for anything with a penalty attached.
Say so once.

## The statute and the portals

- **VAT Law No. 67 of 2016** (قانون ضريبة القيمة المضافة) and its **Executive
  Regulations** — English PDFs published by the ETA, with the VAT return forms
  and the prescribed invoice content
- **Commercial Registry Law No. 34 of 1976** — also on the ETA server
- **ETA** — مصلحة الضرائب المصرية, `eta.gov.eg`; electronic tax services at
  `eservice.incometax.gov.eg/ETax/`; **e-invoicing** at `invoicing.eta.gov.eg/`
  and the integration SDK at `sdk.invoicing.eta.gov.eg/start/`
- **Ministry of Finance** — `mof.gov.eg`

⚠️ Two authoritative mirrors exist for some texts (ETA and the GAFI server), which
is useful when one host is down.

## The registrations are separate acts

⚠️ **Registering for income tax is not registering for VAT.** They are distinct
registrations with distinct numbers. Businesses assume one covers the other.

| What | Arabic |
|---|---|
| Tax number / **tax card** | **الرقم الضريبي / البطاقة الضريبية** |
| **VAT registration** | تسجيل ضريبة القيمة المضافة |
| Commercial-register extract | **مستخرج السجل التجاري** |

⚠️ The **tax card (البطاقة الضريبية) is a physical document** with a number on it —
it is **not** a "tax certificate" and **not** a "tax ID" in the loose sense. Use the
Arabic.

## E-invoicing — the part with a deadline attached

⚠️ **From 1 July 2023, expenses in the tax return are accepted only via the
electronic invoice.** This is the ETA's own published notice on the electronic
services landing page.

→ **If your business deducts costs without e-invoices, it cannot claim them.** This
is not a future obligation. It is the current rule, and it is quietly reducing
businesses' deductible costs.

**The system** — the ETA operates an **eInvoice / eReceipt** platform with a
developer **SDK** for ERP and point-of-sale integration, and an **eSeal X.509
certificate** for signing. Integration is technical work: the SDK, a certificate,
and a system that can produce the prescribed document format.

## What an invoice must carry

⚠️ **Consumer Protection Law 181/2018 Art. 10** — the supplier must give the
consumer an invoice proving the transaction, containing in particular:

- the **tax registration number**
- transaction **date**
- **price**
- **specifications**
- **nature, type and quantity**
- plus any other data the Executive Regulations specify

**Art. 5** — the invoice must be **in Arabic**, in clear legible script, bearing the
supplier's **address, contact methods, commercial-register registration data and
trade licence** if any.

**Art. 11** — ⚠️ **if the invoice is not issued as required, the consumer may prove
the product's specifications and all other contract elements by any means of
proof.** A defective invoice does not lose you the sale. It loses you the evidence
and hands the customer the argument.

**Art. 7** — prices must be displayed **inclusive of legally imposed taxes and
other financial charges**. So **VAT-inclusive** pricing, not "from EGP X + VAT".

## Revenue stamp — not a postmark

⚠️ **دمغة / ضريبة الدمغة** is a **tax**, and in the cheque context it is **paid at
the bank**. It has nothing to do with **الختم البريدي** (the postal stamp) and
nothing to do with the **الختم الإلكتروني** (the electronic seal). Three different
things that a naive translation merges into one.

## Records

Keep, and be able to produce on request:

- The **tax card** and registration confirmations
- **VAT** returns and payment confirmations
- **Electronic invoices** for every sale and every claimed expense — ⚠️ this is the
  set that matters, given the 1 July 2023 rule
- **Bank statements** covering the periods
- The **commercial registry extract**
- **Social insurance** records — NOSI, `www.nosi.gov.eg`

⚠️ **A screenshot is not a record. A bank statement is.** Where a transaction was
material, the statement is what proves it.

## Where to go

| What | Where |
|---|---|
| Tax card, VAT, returns, clearance | **ETA** — `eta.gov.eg` |
| Electronic registration, returns, unified TIN | `eservice.incometax.gov.eg/ETax/` |
| E-invoicing integration | `invoicing.eta.gov.eg/` · `sdk.invoicing.eta.gov.eg/start/` |
| Your local office | ⚠️ **مأمورية الضرائب** — a specific ETA **district** office. There is **no clean English equivalent**: write "your local tax office (مأمورية)" and keep the Arabic |
| Physical counter | ⚠️ **الشباك** — the service window. "counter" works; "desk" does not |

## Unverified

- 🟡 **Current VAT and income-tax rates and thresholds**, and the registration
  thresholds that determine who must register for VAT. Not retrieved — **do not
  quote a rate from this skill.**
- 🟡 The **current penalties** for late filing or non-registration
- 🟡 Whether the **e-invoicing integration** has further staged mandates beyond the
  expense-deduction rule
- 🟡 The **tax clearance certificate** procedure and its current validity period

If someone needs a **rate or a penalty**, that is a primary-source question against
the ETA or the VAT Law itself. This skill tells you where to look and what the
structural rules are; it does not carry the numbers.

## References

- `research/egyptian-corpus/02-data-protection-privacy-consumer.md` — VAT Law
  67/2016 and Executive Regulations with the English PDFs, Art. 5/7/10/11
- `research/egyptian-corpus/04-practical-operations-egypt.md` — the portals, and
  the 1 July 2023 e-invoice rule
- `skills/egy-context-operations/references/PORTALS.md` — every URL, HTTP-tested
- `skills/egy-ecommerce-compliance/` — the consumer-facing side
- `skills/egy-invoice-and-payment-terms/` — payment terms and debt recovery