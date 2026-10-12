# Official portals — Egypt

Every URL here was **HTTP-tested on 2026-10-12**. `❌` = did not respond from
that test environment.

## Read this before trusting any URL in this file

**HTTP 200 does not mean the page exists.** Three separate traps:

1. **`gcc.gov.eg` returns 200 and is the Cultural Development Fund**, not the
   Official Gazette.
2. **GAFI was rebuilt as a JavaScript SPA.** Legacy `/English/StartaBusiness/...`
   HTML paths now redirect to a styled 404 page that returns **200**. A "200"
   proves nothing. Deep-link to `gafi.gov.eg/en` and navigate, or use
   `portal.gafi.gov.eg`.
3. **CBE intermittently serves a "Request Rejected" WAF page** to non-browser
   clients. A blocked fetch is not evidence the content is gone.

Substantive citations below were retrieved by full content, not status code alone.

## The false friends

| People send users to | Actually is | Use instead |
|---|---|---|
| `gcc.gov.eg` for the Official Gazette | **Cultural Development Fund** | `alamiria.com` (المطابع الأميرية), `dspace.id.com.eg` |
| `ntra.gov.eg` | Resolves in DNS, **never answers HTTP** | **`tra.gov.eg`** |
| `alqalam.idsc.gov.eg` | **No DNS record** | **`elpai.idsc.gov.eg`** — the Egyptian Legislation Portal (ELP) |
| `ela.gov.eg`, `www.alqalam.gov.eg` | **No DNS record** | `elpai.idsc.gov.eg` |
| `mota.gov.eg` | Trade & Industry ministry (industrial licensing) | Correct, but see below |
| `moiic.gov.eg` | Supply & Internal Trade ministry (traditional Commercial Registry) | Correct, but see below |
| `nosi.gov.eg` | No response without `www` | **`www.nosi.gov.eg`** |
| `www.digital.egypt.gov.eg` | No response | **`digital.gov.eg`** |
| `digital.gov.eg/en/` | **404 — no English UI exists** | `digital.gov.eg` (Arabic) |
| `www.cbe.org.eg/en/exchange-rates` | **404 — no live-rate page** | CBE Historical Data page |
| `meeza.gov.eg`, `meeza-nbe.com.eg` | No response | `meeza-eg.com`, and the Egyptian Banks Association |

⚠️ **`mota.gov.eg` and `moiic.gov.eg` are two different ministries with similar
names.** Conflating them sends a company-formation question to the wrong body.
Both are real; neither is a prefix typo.

## Company formation and investment

| Body | URL | Status | What you file there |
|---|---|---|---|
| **GAFI** — الهيئة العامة للاستثمار والمناطق الحرة | `gafi.gov.eg/en` | ✅ 200 | Investment regimes, incentives, free zones |
| **GAFI e-services** | `portal.gafi.gov.eg/services/eServices` | ✅ 200 | **Incorporation, licence applications, post-incorporation services** |
| GAFI incorporation procedures (PDF) | `gafi.gov.eg/English/Documents/Companies Incorporation Procedures.pdf` | ✅ 200 | Official procedure document |
| **Golden Licence** | `goldenlicense.gov.eg/default_en.aspx` | ✅ 200 | The single strategic-licence route |
| **Investment Zones** | `izones.gafi.gov.eg/default_en.aspx` | ✅ 200 | Investment-zone project licensing |
| Invest in Egypt | `investinegypt.gov.eg/English/Pages/exploreMap.aspx` | ✅ 200 | Sector map |
| **SCZONE** — Suez Canal Economic Zone | `sczone.eg` · `www.sczone.eg/en` | ✅ 200 | **Separate authority with its own register — not GAFI's** |

⚠️ **Two different GAFI-hosted applications**, constantly confused:
`portal.gafi.gov.eg/services/eServices` vs `goldenlicense.gov.eg`. And
**GAFI, SCZONE and GOEIC are three different bodies.**

⚠️ **GAFI's published service levels are marketing claims, not an SLA:**
"1 Business Day to Incorporate Companies", "2 Hours E-incorporation for Sole
Proprietorship", "20 Business Days to Issue Permits". Practitioner reports are
consistently slower. Mark any timeline as an **estimate**.

**Company forms and minimum capital** ⚠️ PARTIAL (Chambers and practitioner
sources):

| Form | Arabic | Minimum |
|---|---|---|
| Limited Liability Company | ش.ذ.م.م | **no statutory minimum** for most activities |
| One-Person Company | ش.ش.و | **EGP 50,000** |
| Closed Joint Stock Company | ش.م.م (مقفلة) | **EGP 250,000** issued capital |
| Public Joint Stock Company | ش.م.م (مطروحة) | listed-market requirements |
| Foreign branch / rep office | فرع / مكتب تمثيلي | via GAFI; restricted activities |

## Commercial register — two tracks, and a 2026 change

⚠️ **There are two registers and they are not the same thing:**
- **GAFI** — companies formed under the investment law and in free zones
- **Traditional commercial registry** — under the Ministry of Supply & Internal
  Trade (`moiic.gov.eg`, ❌ unresponsive at test time)

**A counterparty checked against the wrong register has not been checked.**

⚠️ **A commercial-registry number is meaningless without its issuing governorate.**
Numbering is sequential *per governorate*, so the number alone identifies nothing.
Always ask which governorate issued it.

✅ **From 1 January 2026, nine commercial-registry services became exclusive to
Digital Egypt:** updating registry data; adding an establishment outside the
"شركاتي" (My Companies) system; **enquiring about a commercial register**;
inferring registration status; transferring an individual establishment within
the governorate; obtaining a **commercial register extract**; a data certificate;
an extract for Ministry of Foreign Affairs authentication; and a **negative
certificate**.

> **Agent rule: for any of those nine, send the user to Digital Egypt — not to a
> registry office.**

| Body | URL | Status |
|---|---|---|
| **Digital Egypt** — commercial-registry services now run here | `digital.gov.eg/` | ✅ 200 |
| ITDA — Commercial Register services | `itda.gov.eg/registry.aspx` | ✅ 200 |
| ITDA — Commercial Register & legislation | `itda.gov.eg/sgl.aspx` | ✅ 200 |
| Misr Services Centre — مركز خدمات مصر | `khadamatmisr.gov.eg/serviceslist` | ✅ 200 |

## Tax

| Body | URL | Status | What you file there |
|---|---|---|---|
| **ETA** — مصلحة الضرائب المصرية | `eta.gov.eg` (→ `/ar/home`) | ✅ 200 | Tax card, VAT, returns, clearance |
| ETA taxpayer services | `eta.gov.eg/en/node/67` · new taxpayer: `/en/node/15` | ✅ 200 | Registration |
| **ETA electronic tax services** | `eservice.incometax.gov.eg/ETax/` | ✅ 200 | Registration, returns, unified TIN |
| **eInvoice / eReceipt SDK** | `sdk.invoicing.eta.gov.eg/start/` · `invoicing.eta.gov.eg/` | ✅ 200 | ERP/POS integration; eSeal X.509 certificate |
| VAT Law 67/2016 (EN PDF) | `eta.gov.eg/sites/default/files/2024-02/Law-english-no.67-2016.pdf.pdf` | ✅ 200 | Primary text |
| VAT Executive Regulations (EN PDF) | `eta.gov.eg/sites/default/files/2024-02/VAT-Executive-Regulations-English.pdf` | ✅ 200 | Forms 1–4 VAT, invoice content |
| Commercial Registry Law 34/1976 (EN PDF) | `eta.gov.eg/sites/default/files/2024-10/law-34-1976.pdf` | ✅ 200 | Primary text |
| Ministry of Finance | `mof.gov.eg/en` | ✅ 200 | Fiscal policy, MoF decrees |

⚠️ **ETA's own notice: from 1 July 2023, expenses in the tax return are accepted
only via the electronic invoice.** If a business deducts costs without
e-invoices, it cannot claim them.

⚠️ VAT registration is a **separate act** from income-tax registration.
Registering for one is not registering for the other.

**Commercial Registry Law 34/1976 is mirrored on the GAFI server** (✅ 200) —
useful when one host is down.

## Customs

| Body | URL | Status | What you file there |
|---|---|---|---|
| **Egyptian Customs Authority** — مصلحة الجمارك المصرية | `customs.gov.eg/` | ✅ 200 | Declarations, tariffs, e-services |
| Customs declarations | `customs.gov.eg/Services/Declartion` | ✅ 200 | Register and manage declarations at the point of entry |
| **NAFEZA** — Advance Cargo Information | `nafeza.gov.eg/en` · `/en/pages/15` | ✅ 200 | **Pre-shipment declaration system** |

⚠️ The declarations path contains a **real misspelling** — `Declartion`. Do not
"fix" it.

✅ **NAFEZA (from NAFEZA's own site):** Advance Cargo Information (ACI) requires
cargo data and documents — **pro-forma invoice and draft bill of lading if it
exists** — **at least 48 hours before shipment** from the export country, so the
state can run its Risk Management System. Phase 1 pilot 1 April 2021;
**mandatory from 1 October 2021.** The importer registers on the NAFEZA portal,
obtains an **electronic signature pad** to access it, lists the advance cargo data
and obtains the **ACID** before import operations begin. The overseas exporter
sends shipment documents to NAFEZA via supply-chain networks on **blockchain**,
on vessel departure.

> **This is a hard 48-hour deadline set by the exporter's country of shipment, and
> it bites before anyone in Egypt can act on it.** If a client is importing,
> raise NAFEZA early — before the shipment, not after arrival.

## Social insurance, labour

| Body | URL | Status |
|---|---|---|
| **NOSI** — National Organisation for Social Insurance | **`www.nosi.gov.eg`** (no-`www` fails) | ✅ 200 |
| Ministry of Labour and Social Insurance | `hrss.gov.eg` | ⚠️ verify |

## Telecommunications

| Body | URL | Status |
|---|---|---|
| **NTRA** — National Telecom Regulatory Authority | **`tra.gov.eg`** | ✅ 200 |

⚠️ Do **not** send users to `ntra.gov.eg`. It resolves in DNS but does not answer.

## Digital government, e-signature, Post

| Body | URL | Status | Note |
|---|---|---|---|
| **Digital Egypt** | **`digital.gov.eg`** | ✅ 200 | Arabic only — `/en/` is 404 |
| **ITIDA** — هيئة تنمية صناعة تكنولوجيا المعلومات | `itida.gov.eg` | ✅ 200 | E-signature, accredited CAs |
| **Egypt Post / Barai'idy (بريديد)** | `egyptpost.com` | ✅ 200 | `egyptpost.com/Bareedi` returns 200 but is a **JS shell** — Bareedi's live function could not be confirmed, only its 2022 launch |

## Legislation databases

| Body | URL | Status |
|---|---|---|
| **ELP — Egyptian Legislation Portal** (Cabinet) | **`elpai.idsc.gov.eg`** | ✅ 200 |
| Official Gazette printing — alamiria.com | `alamiria.com` | ✅ |
| Gazette archive — dspace.id.com.eg | `dspace.id.com.eg` | ✅ |
| WIPO Lex | `wipo.int/wipolex` | ✅ — **has English translations of Egyptian IP and arbitration law** |

❌ `alqalam.idsc.gov.eg`, `ela.gov.eg`, `www.alqalam.gov.eg` — **no DNS record.**
These are widely cited and do not resolve.

## Courts, police, real estate

❌ Several Egyptian court and real-estry registry portals did not respond at test
time, and no English UI was confirmed. Do not invent a URL — direct the user to
the competent **محكمة** by name and governorate, and to a local lawyer for the
filing route.

## Other unverified

| URL | Status |
|---|---|
| `www.moiic.gov.eg` | No response |
| `www.id.gov.eg`, `www.passport.gov.eg` | No response (DNS OK) |
| `www.cde.org.eg` | No response — could not confirm as the Commercial Registry portal |
| `www.fsc.gov.eg`, `merca.org.eg`, `prim.gov.eg`, `telecom.gov.eg` | No response |
| `enationality.moi.gov.eg` (passports) | Not testable; practitioner source reports a maintenance page |
| `msit.gov.eg/?p=7073` | **HTTP 500** — content verified via indexed text only |
| `sczone.eg/en`, `customs.gov.eg/en` | 200 / 500 respectively |