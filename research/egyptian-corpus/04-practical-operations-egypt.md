# Egypt — Practical Operations Context Pack

# جمهورية مصر العربية — دليل العمليات العملية

**Scope of this file:** the everyday mechanics an AI agent needs in order to produce an instruction,
checklist, letter or contract that a **real person can actually act on** in Egypt — with GAFI, the
Commercial Registry, ETA, Customs, NOSI, the Ministry of Labour, NTRA, the CBE, the Real Estate
Registry, the traffic units, banks, landlords, employers and the courts.

**This file is NOT about legal doctrine.** Doctrinal material (Civil Code, Commercial Code, Labour
Law, AML, banking law, procedure) lives in files `01`, `02` and `03` of this corpus. Here we care
only about: *what the identifier looks like, where you file it, how long it takes, how you pay, and
what the word actually means in Arabic.*

**As-of date for the whole file: 2026-10-12.** Every portal URL was HTTP-tested on that date.

---

## How to read the markers

| Marker | Meaning |
|---|---|
| ✅ **VERIFIED** | I retrieved the primary text, the official portal, or the regulator's own publication and quote/cite it. |
| ✅ **URL OK** | The URL returned HTTP 200 when tested on 2026-10-12. |
| ⚠️ **PARTIAL** | Verified in a reputable secondary source but not against the primary/official text. |
| 🟡 **UNVERIFIED / FOLKLORE** | Widely repeated — including by Egyptian practitioners — but **not confirmed by any official source I could retrieve**. Do not hard-code. |
| ❌ **WRONG PREMISE** | The commissioning brief asserted something that is false or misleading. Corrected below. |
| 📅 **ESTIMATE (practitioner-reported)** | A timing or cost reported by practitioners. **Never** an official figure. |

**Rule for agents using this file:** if you cannot find a ✅ VERIFIED or ⚠️ PARTIAL marker, write
the instruction so that it *works anyway* (e.g. "confirm the current value with the authority
before relying on it") rather than asserting the number.

---

## Corrections to the commissioning brief (read first)

An agent trained on the brief as given would produce at least six false or misleading statements.

| # | Brief said | Reality | Confidence |
|---|---|---|---|
| 1 | "Egypt has **no national postal-code system**" | **Half wrong.** Egypt Post (بريد مصر) *does* operate a national postcode standard — historically a 5-digit code, with a documented GIS-based **7-digit granular** layer (Egypt Post National Postcode Standard, described in ISO TC211's *Standards in Action*). What is **true** is that coverage and everyday use are inconsistent and that the code is **not required** for delivery — Egypt Post routes on **governorate + district**. See §Addresses. | ✅ VERIFIED (ISO TC211) / ⚠️ PARTIAL (5-digit format) |
| 2 | Central Bank of Egypt — "…mobile wallets, **CIPS**" | **There is no "CIPS" in Egypt.** CIPS is the *Cross-Border Interbank Payment System* operated by China. An agent that writes "the CBE CIPS" is hallucinating. Egypt's actual rails are **IPN / InstaPay**, **ACH**, **RTGS**, **EFT**, **CCH** (cheque clearing), **SWIFT**, **IBAN**, and the **Meeza** domestic card scheme. | ✅ VERIFIED |
| 3 | National ID — "14-digit structure … and validation rules" | The **14-digit** part is right. The **validation rule is not published.** The check-digit algorithm is *not* in any official source; "Luhn mod-10" is an **undergraduate folklore claim** that I found circulating in academic slides and GitHub gists. See §Identifiers. | 🟡 UNVERIFIED (algorithm) |
| 4 | Governorate codes are a simple range | Positions 8–9 use a **fixed, non-contiguous set of 27 codes plus `88`** for births registered abroad. A parser that accepts `01–35` will admit codes that do not exist. | ⚠️ PARTIAL |
| 5 | "NTRA — `ntra.gov.eg`" | `ntra.gov.eg` **resolves in DNS but does not answer HTTP from here**. The regulator's working site is **`tra.gov.eg`** ("National Telecom Regulatory Authority"). Use that. | ✅ URL OK on `tra.gov.eg` |
| 6 | "Etisalat Cash / e&" | Both are right, but note the operator **rebranded from Etisalat to `e&` in 2022**. The CBE's own mobile-wallet register still lists several wallets under the legacy names. Use `e&` for the operator and keep the wallet name as printed on the wallet. | ⚠️ PARTIAL |

---

## 1. Currency

### 1.1 The unit

| Field | Value |
|---|---|
| Name | Egyptian Pound — **جنيه مصري** (junayh masri) |
| ISO 4217 | **EGP**, numeric **818** |
| Symbol | **ج.م** (Arabic); `£`, `E£`, `£E`, `LE` (English) |
| Subunit | 1/100 **piastre** — **قرش** (qirsh), symbol `PT` (from French *piastre tarif*) |
| Historical subunit | 1/1000 **millieme** — **مليم** — withdrawn; do not use in modern documents |
| Issuing bank | Central Bank of Egypt (**البنك المركزي المصري**) |
| Digit usage | Egyptian documents normally use **Arabic-Indic (Hindu-Arabic) numerals ٠١٢٣٤٥٦٧٨٩**, written **left-to-right** even inside RTL text |

⚠️ **PARTIAL** — denomination and unit data per Wikipedia's "Egyptian pound" article and CBE
material. Current banknote denominations in circulation should be confirmed against a CBE
publication before printing them on a form.

### 1.2 Writing amounts in Arabic — the words rule

Egyptian cheques and many contracts carry the amount **twice**: once in numerals and once spelled
out in words. The formula is fixed:

```
فقط  <amount in words>  لا غير
"Only  <amount>  and nothing more"
```

Worked examples (EGP):

| Figures | Words (Arabic) | Words (English) |
|---|---|---|
| 1,250 | فقط ألف ومائتان وخمسون جنيهاً مصرياً لا غير | Only one thousand two hundred fifty Egyptian Pounds |
| 350.75 | فقط ثلاثمائة وخمسون جنيهاً مصرياً وخمسة وسبعون قرشاً لا غير | Only three hundred fifty Egyptian Pounds and seventy-five piastres |
| 1,000,000 | فقط مليون جنيه مصري لا غير | Only one million Egyptian Pounds |

⚠️ **PARTIAL** — the *formula* (`فقط … لا غير`) and the examples are attested on multiple Egyptian
cheque-drafting resources, but I did **not** locate the Commercial Code article in the Arabic
source text that makes the words prevail. 🟡 Treat "the words prevail over the figures" as a
**very strong operational rule** (every Egyptian banker treats it this way) but **cite an article
number only after checking the Arabic Commercial Code yourself.** Do not invent one.

**Agent rule:** if you generate a cheque amount in Arabic, always emit the words line. A cheque
with only the numeral line will be treated as incomplete by most Egyptian bank branches.

### 1.3 Foreign-currency contract amounts — the real problem

Egypt has had a **floating EGP since 6 March 2024**. ✅ VERIFIED (Reuters, 2024-03-06; CBE
statement): the CBE announced it would "allow the exchange rate to be determined by market forces"
and simultaneously raised the overnight lending rate by 600 bps to 28.25% (deposit rate 27.25%).
USD/EGP moved from roughly **30.85** (the defended level for months) to **~49.4–50.7** on the day.
⚠️ The brief's framing of a "recent major currency move" is therefore not recent any more — the
float is two years old. **Do not quote a live rate from memory.** Pull it from the CBE.

Practical consequences for drafting:

1. **State the denomination and the conversion mechanics explicitly.** A contract that says
   "USD 10,000" and nothing else leaves the EGP obligation to an unstated rate source.
2. **Name the rate source, the rate date and the payer.** The workable Egyptian pattern is:
   *"the Client shall pay the EGP equivalent of each invoiced amount, converted at the CBE
   mid-market rate published on the Business Day immediately preceding the date of payment."*
3. **Distinguish a fixed-EGP obligation from a foreign-currency obligation.** A fixed EGP price
   is borne by the Egyptian obligor when the pound moves. A USD-denominated obligation is borne by
   both if you also fix the conversion rate/date. This is the single biggest commercial drafting
   point in Egypt post-2024. ⚠️ PARTIAL — the mechanics are sound; get Egyptian counsel on the
   specific clause.
4. **Customs and tax.** Imported invoices are declared in the transaction currency; customs duty,
   VAT and income tax convert at the customs/ETA rate. Do not convert at your own rate.
5. **CBE reference rate.** ✅ URL OK: `https://www.cbe.org.eg/en/economic-research/statistics/exchange-rates/historical-data`
   (last updated 01 Sep 2026 when checked). Never hard-code a rate.

**Live rate URL note:** I could not confirm a stable, permanent CBE "current mid-market rate" page
path. `https://www.cbe.org.eg/en/exchange-rates` returned **404** when tested. Use the Historical
Data page above, which is stable, and say so in the instruction.

---

## 2. Identifiers and formats

### 2.1 National ID — الرقم القومي (14 digits)

The single most important identifier in Egypt. Issued by the Civil Status Authority under the
Ministry of Interior. Statutory basis: **Law No. 143 of 1994** on Civil Status.

**Structure** ⚠️ PARTIAL (consistent across two independent secondary sources):

| Position | Field | Rule |
|---|---|---|
| 1 | Century of birth | `2` = born 1900–1999; `3` = born 2000–2099. Anything else = malformed. |
| 2–7 | Date of birth | `YYMMDD`, validated as a real calendar date against the century digit. |
| 8–9 | **Governorate of registration** | Fixed, non-contiguous two-digit code (see below). |
| 10–13 | Serial | Separates same-day births in the same governorate. |
| 13 | **Gender** | **Odd = male, even = female.** (Digit 13, not digit 14.) |
| 14 | Check digit | Algorithm **not published**. |

**Governorate codes (positions 8–9)** ⚠️ PARTIAL:

```
01 Cairo            02 Alexandria      03 Port Said       04 Suez
11 Damietta         12 Dakahlia        13 Sharqia         14 Qalyubia
15 Kafr El Sheikh   16 Gharbia         17 Monufia         18 Beheira
19 Ismailia
21 Giza             22 Beni Suef       23 Faiyum          24 Minya
25 Asyut            26 Sohag           27 Qena            28 Aswan
29 Luxor
31 Red Sea          32 New Valley      33 Matruh
34 North Sinai      35 South Sinai
88  Birth registered outside the Arab Republic of Egypt
```

> ⚠️ **Codepoint 8–9 is the governorate of *registration/birth*, not current residence.** An agent
> that uses it as "home governorate" will be wrong for most adults.

**Validation rules — the honest position:**

- ✅ **Offline structural validation is legitimate**: 14 digits, century digit `2` or `3`,
  calendar-valid date in positions 2–7, an existing governorate code, gender parity at digit 13.
- 🟡 **The check digit cannot be validated offline from any official published algorithm.** I found
  the Luhn/mod-10 claim only in academic slides and community gists. **Do not ship a Luhn check as
  if it were official.** If you implement one, label it as an unconfirmed heuristic.
- ✅ **Authoritative confirmation** of the number ↔ card ↔ person is a **record check against the
  Civil Status Authority**, and (for phone-number binding) against **NTRA** ownership data. This is
  what KYC vendors do; it is not something a document or an agent can do.

**Card contents** ⚠️ PARTIAL: full name; date of birth; gender; religion; **residence address**;
issuing office; profession; **husband's name (for women)**; the national number; photo; issue and
expiry dates; a factory/card number.

**Validity** ⚠️ **SOURCES CONFLICT — do not state a number without checking:**
- Wikipedia's "Egyptian National Identity Card" article, citing a 2008 Interior Ministry statement:
  **7 years** validity, set by Interior Ministerial decree.
- The Egyptian Consulate General in Sydney publishes "The national ID card has a validity of **7
  years**" (`https://egyptconsulatesydney.com/en/national-id-card-renewal/`).
- Some secondary sources say **10 years**.
→ **Agent instruction:** "check the expiry date printed on the card itself." Never hard-code a period.

**Numeral warning:** Egyptian identity documents are printed in **Arabic-Indic numerals (٠–٩)**.
Any OCR trained only on Western digits will misread the number and the date blocks *and will not
raise an error*. If your workflow involves scanning Egyptian IDs, this is the single most likely
silent failure.

### 2.2 Commercial Registry — السجل التجاري

| Field | Value |
|---|---|
| Issuing authorities | **Two, and they are different** — see below |
| Governing law | **Law No. 34 of 1976** on the Commercial Register |
| Mandatory disclosure | ✅ Law 34/1976 **Art. 5**: every registered person **shall write on the shopfront and in all correspondence, printed matter and papers relating to the business**, the trade name together with the **registry office and the registration number** |

✅ VERIFIED — Law 34/1976 text, published on both the ETA server
(`https://www.eta.gov.eg/sites/default/files/2024-10/law-34-1976.pdf`) and the GAFI server
(`https://www.gafi.gov.eg/English/StartaBusiness/Laws-and-Regulations/PublishingImages/Pages/TradeLaws/...`).

**The two-track trap — the most commonly confused point in Egyptian company paperwork:**

| Track | Issuer | Who uses it |
|---|---|---|
| **Traditional Commercial Register** | **مصلحة السجل التجاري** under the **Ministry of Trade and Industry / Ministry of Supply and Internal Trade** (التموين والتجارة الداخلية) | Ordinary traders, sole proprietors, partnerships, small and mid-size firms, most retail and service companies |
| **Investment register** | **GAFI** — الهيئة العامة للاستثمار والمناطق الحرا | Companies under **Investment Law 72/2017**, free-zone companies, Suez Canal Economic Zone (SCZONE) companies, many large Egyptian joint-stock companies, banks, insurers |

⚠️ **Both certificates are equally valid before banks, ETA and Customs** (per practitioner
sources). But if your counterparty is a free-zone company and you assumed the *traditional*
register, your due diligence is pointed at the wrong registry.

🟡 **UNVERIFIED / FOLKLORE:** the claim that a traditional CR number is "6–7 digits, up to 8 in
larger governorates". I found this only on a low-quality commercial "CR validator" page. The
**substantively important** point, which is consistent across sources, is:

> **A CR number is meaningless without its issuing office (governorate).** Numbering is
> sequential **within each governorate's registry office**, so Cairo `123456` and Asyut `123456`
> are different companies. Write: *سجل تجاري القاهرة رقم 123456* — "Cairo Commercial Register
> No. 123456".

**GAFI-issued numbers** may be referred to as **"سجل تجاري المستثمرين"** (investors' commercial
register) ⚠️ PARTIAL.

**Verification route** ✅:
- Investment / free-zone companies → GAFI portal (`gafi.gov.eg`), company enquiry service.
- Traditional companies → the Ministry of Supply and Internal Trade portal, or in person at the
  issuing governorate's registry office.

### 2.3 Tax numbers and cards — الرقم الضريبي / البطاقة الضريبية

| Item | Value |
|---|---|
| Authority | **مصلحة الضرائب المصرية — ETA** (Egyptian Tax Authority), `eta.gov.eg` |
| Number length | 🟡 **9 digits**, often displayed masked as `123-456-789`. Attested only by commercial TIN-validator sites; I did **not** find the format in an ETA primary publication. **Do not build a hard validator on 9 digits without confirmation.** |
| What **is** verified | ✅ From the **VAT Executive Regulations**: the **tax invoice must carry** the registrant's name, address and **registration number**, and the buyer's name, address and **tax registration number, or the national ID number where the buyer has no tax registration number**. So: **national ID is a lawful invoice identifier for an unregistered buyer.** |
| Where the number appears | Tax invoices, e-invoices, tax returns, contracts with tax clauses, customs files, bank account-opening KYC |

**VAT — the numbers that actually matter:**

| Item | Value | Source |
|---|---|---|
| Standard rate | **14%** (13% for FY 2016/2017 only, raised to 14% from FY 2017/2018) | ✅ Law 67/2016 text, ETA PDF |
| Registration threshold | **EGP 500,000** of total sales (taxable **and** exempt) in the preceding 12 months, for producers/traders/service providers | ✅ Law 67/2016 text |
| Registration obligation period | Within **30 days** of reaching the threshold | ✅ Law 67/2016 text |
| Mandatory registrants regardless of turnover | **Importers** of taxable goods/services; **exporters**; **distribution agents**; manufacturers/importer**s** of listed Table (1) goods | ✅ Law 67/2016 text |
| Non-registrants | Natural persons who sell no goods and provide no services are **not obliged** to register even if they cross the threshold | ✅ Law 67/2016 text |
| Threshold may be changed | ✅ "by virtue of a Ministerial decree" — i.e. it is not fixed forever |

**E-invoicing:** ✅ **Ministerial Decision No. 188 of 2020** bound the tax community to the
eInvoice system; ETA's platform is at `sdk.invoicing.eta.gov.eg` and `invoicing.eta.gov.eg`
(both URL OK). ETA's portal carries the notice that **from 1 July 2023 expenses in the tax return
are only accepted via the electronic invoice**. ERP/POS integrators need an **eSeal X.509
certificate** configured into the system. ✅ URL OK: `https://sdk.invoicing.eta.gov.eg/start/`

⚠️ **Also verified and operationally important:** individuals who **rent out** a residential unit
or a shop must **notify the competent tax office**, because rental income falls under real-estate
wealth tax; failing to notify exposes the owner to liability. ✅ (ETA portal notice.)

### 2.4 VAT registration as a distinct act

VAT registration is **not** the same as obtaining the tax card. Registration threshold and
importers' mandatory status are set out above. Filing is done at the competent **مأمورية**
(tax office) using **Form No. 1 VAT**; ETA assigns the registration number and issues the
**registration certificate (Form No. 3 VAT)**, notifying via **Form No. 4 VAT**. ✅ (VAT Executive
Regulations, ETA PDF.) Agent instruction: "obtain the VAT registration **certificate**, not merely
the tax card" — they are separate documents.

### 2.5 Passport

| Item | Value |
|---|---|
| Issuer | Passports, Immigration and Nationality Administration, Ministry of Interior |
| Format 🟡 **CONFLICTING** | One commercial validator states **1 uppercase letter + 8 digits** (`A12345678`). Canada's Immigration and Refugee Board, describing the Egyptian booklet via Keesing's document checker, states **"8 digits, preceded by a letter"**. These are the same claim. **Neither is an Egyptian government publication.** Egypt has **not published** an authoritative passport-number format spec. |
| Agent rule | **Accept a permissive pattern** (`^[A-Z]\d{7,9}$`) and validate against the passport's **MRZ**, which is the machine-readable authority. Never hard-reject on a length assumption. |
| Booklet | ⚠️ 52 pages, 125 × 88 mm; personal data in Arabic **and** English; barcode carrying an MRZ; bearer signature on page 3. |
| ⚠️ Egyptian passports are **not e-passports** (as at the research date). Don't assume an NFC chip. |

⚠️ **Portal caution:** `https://www.id.gov.eg/` and `https://www.passport.gov.eg/` did **not**
respond from this environment (DNS resolves, HTTP times out). Practitioner guides report the
specialist **Passports, Emigration and Nationality** portal at `https://enationality.moi.gov.eg/`
was serving a maintenance notice in September 2026. **Verify the live passport portal before
telling a user to go there.**

### 2.6 Driving licence — رخصة القيادة

- Issued by the **local council / traffic unit** (وحدة المرور or المجلس المحلي) in the applicant's
  district — the deciding factor is **residence**, not where you learned to drive.
- The Ministry of Interior's executive regulations for driving licences live at
  ✅ URL OK: `https://traffic.moi.gov.eg/` (e.g. `.../Arabic/OurServices/InfoServices/InteriorMinisterDecision/Pages/licenses-driving-slow-transport-vehicles.aspx`)
- ✅ **From the traffic-unit regulation (Arts. 332–335):** the licence is issued "on the model
  prepared therefor" and is **registered with a serial number for each type** by the issuing council;
  it is **valid for five years from the date of issue**. Renewal requires a **clearance certificate
  for outstanding fines** (شهادة الوفاء بالغرامات) plus proof of identity and residence — and, for
  government employees, a criminal-record certificate from the employing body.
- 🟡 **Licence *number* format is not officially specified in any source I retrieved.** A
  commercial KYC article quotes a real specimen as `1739045` (seven digits) and notes that the
  **national ID also appears on the licence**. **Do not validate licence numbers by length.**
- **New electronic (chip) driving licences** were introduced in Egypt in **early 2024** ⚠️ PARTIAL.
  New licences duplicate the holder's name in Latin script; older ones are Arabic-only. Data
  elements include licence number, national ID number, issuing traffic unit, issue/expiry dates,
  permitted categories, address, nationality and profession.

### 2.7 Social insurance number — الرقم التأميني

- ✅ The insurance number is allocated **sequentially** and is the primary key of the NOSI
  information system, running from birth until retirement. **A worker may not hold more than one
  insurance number**, and the system cannot be operated without it.
  (`https://www.nosi.gov.eg/` — URL OK)
- ⚠️ **It is widely but not officially asserted to be the same 14-digit format as the national ID.**
  A practitioner site explicitly says the NOSI enquiry takes the **national ID + the mother's first
  name in Arabic** — which implies the two are *looked up together*, not that they are identical.
  **UNVERIFIED: "the insurance number equals the national ID."** Write instructions that take the
  national ID as input, never that assume identity of the two numbers.
- **Enquiry service:** ✅ URL OK:
  `https://www.nosi.gov.eg/ar/Services/Pages/Info/GetInsuredDetails.aspx`
  — requires national ID + **mother's first name**, plus a CAPTCHA.
- **Employer file opening:** ✅ NOSI publishes a service `فتح ملف إشتراك منشأة جديدة`, citing **Law
  148 of 2019** and its Executive Regulations.

### 2.8 IBAN — ✅ VERIFIED (CBE)

✅ **Egyptian IBAN = 29 characters**, structured as:

```
EG  XX  BBBB  BBBB  AAAAAAAAAAAAAAAAA
│   │   │     │     └─ 17 digits — customer account number (BBAN core)
│   │   │     └─────── 4 digits — branch code
│   │   └───────────── 4 digits — bank code
│   └───────────────── 2 digits — ISO 7064 Mod-97 check digits
└───────────────────── 2 letters — country code EG (ISO 3166-1)
```

Source: CBE IBAN validator page, ✅ URL OK:
`https://www.cbe.org.eg/en/financial-literacy/financial-tools/iban-validator`
⚠️ Note NBK's own warning: an IBAN *calculator* computes the check digits but **does not check that
the account exists**.

### 2.9 Identifier quick reference

| Document / number | Arabic | Length / shape | Issuer |
|---|---|---|---|
| National ID | الرقم القومي | 14 digits | Civil Status Authority / MoI |
| Commercial Register no. | رقم السجل التجاري | digits, **scoped to issuing office** | GAFI **or** Commercial Registry |
| Tax number / tax card | الرقم الضريبي / البطاقة الضريبية | 🟡 9 digits (unconfirmed) | ETA |
| VAT registration | رقم التسجيل الضريبي | ETA-assigned, separate from tax card | ETA |
| Social insurance no. | الرقم التأميني | 🟡 sequential; relation to national ID unconfirmed | NOSI |
| Passport no. | رقم جواز السفر | 🟡 letter + digits (unconfirmed) | MoI Passports Dept |
| Driving licence no. | رقم رخصة القيادة | 🟡 digits (unconfirmed) | Local traffic unit |
| IBAN | — | 29 chars: `EG` + 2 + 4 + 4 + 17 | Bank / CBE standard |

---

## 3. Addresses and postal conventions

### 3.1 The 27 governorates — ✅ VERIFIED

Cairo, Giza, Alexandria, Qalyubia, Dakahlia, Sharqia, Damietta, Beheira, Beheira-adjacent
Beheira/Gharbia, Monufia, Kafr El Sheikh, Gharbia, Ismailia, Port Said, Suez, Faiyum, Beni Suef,
Minya, Asyut, Sohag, Qena, Luxor, Aswan, Red Sea, New Valley, Matruh, North Sinai, South Sinai.

Canonical list (CAPMAS): ✅ URL OK: `https://capmas.gov.eg/`
القاهرة · الجيزة · الإسكندرية · القليوبية · الدقهلية · الشرقية · دمياط · البحيرة · المنوفية ·
الغربية · كفر الشيخ · الإسماعيلية · بورسعيد · السويس · الفيوم · بني سويف · المنيا · أسيوط ·
سوهاج · قنا · أسوان · الأقصر · البحر الأحمر · الوادي الجديد · مطروح · شمال سيناء · جنوب سيناء

🟡 **Note the sequence:** in the national ID (positions 8–9) the Cairo–Delta–Upper Egypt
governorates are **ordered geographically**, which is why the code list has gaps (05–10, 20, 30).
A naive "code = index in the alphabetical list" mapping will be wrong.

### 3.2 Address style — ✅ VERIFIED (structurally) / ⚠️ (conventions)

**Formal written form** (what a government form wants):

```
<building no.> <street name>, عمارة <n>, الدور <n>, شقة <n>
<district / area>, <city>
<governorate>  [optional 5-digit postcode]
EGYPT
```

The **core administrative chain** that actually delivers a parcel or a courier is:

**street → building → floor → apartment → district/area → city → governorate**

**The words that matter** (Egyptian MSA forms with colloquial equivalents):

| Arabic | Transliteration | Meaning |
|---|---|---|
| شارع | shāriʿ | street |
| عمارة | ʿimāra | apartment block / building (colloquially "ʿamāra") |
| الدور | ad-dawr | floor — ⚠️ **not English "first floor"** |
| الشقة | ash-shaq'a | apartment / flat |
| شقة | | ditto (colloquial) |
| الدور الأرضي | ad-dawr al-arḍi | **ground floor** |
| كل شقة على دور | | colloquial "every apartment per floor" — a layout description |
| بجوار / جنب | bi-jawār / janb | next to / beside |
| أمام | amām | in front of |
| خلف | khalf | behind |
||labeled `عام` | ʿāmm | public / general (street) |
| عبارة | ʿibāra | block (commercial-residential) |
| ⚠️ **Floor-numbering ambiguity — see warning below** | | |

⚠️ **Floor-numbering trap.** Egyptian `الدور الأول` is **not reliably "first floor" in the British
sense.** In a building with a shop at street level, `الدور الأرضي` is the ground floor and
`الدور الأول` is the floor **above** it — so `الدور الأول` in Egypt is usually what an English
speaker calls the *first floor*. But `الور الأول فوق الأرضي ولا يمس الأرضي؟` ("is the first floor
above ground or does it touch the ground?") is a **real question Egyptians ask**, because buildings
with a ground floor at pavement level and buildings where the ground floor is a half-storey do not
agree. **Always ask for the entrance (مدخل / بوابة) and the lift (أسانسير) as well as the floor.**

⚠️ **Street numbers are weak identifiers.** A building may have several entrances, numbers may be
missing or illegible, and **landmarks (مسجد, صيدلية, كنيسة, مدرسة, محطة المترو, ج %) are how
Egyptians actually give directions.** For a written form, give the full administrative chain;
for a courier hand-off, give the landmark.

### 3.3 Postal codes — the honest answer

- ✅ **VERIFIED:** Egypt Post operates a national postcode standard. ISO TC211's *Standards in
  Action* case study on Egypt describes the move from a **traditional 5-digit postcode down to the
  delivery office** to a **GIS-based 7-digit granular postcode** identifying ~20–60 buildings,
  with a hierarchy of **Sector → District → Neighbourhood → Community**, plus components for
  buildings, delivery points and postal addresses, and **no gaps or overlaps**.
  ✅ URL OK: `https://committee.iso.org/sites/tc211/home/standards-in-action/addressing/-egypt,-granular-postcodes.html`
- ⚠️ **PARTIAL:** the **5-digit** format (`e.g. 12411`) is what commercial address-validation
  services report as in use, and they concede that **coverage and everyday use are inconsistent**
  and that many Egyptian senders simply leave the field blank. **Egypt Post routes on governorate
  and district.**
- **Agent rule:**
  - ❌ Never write "Egypt has no postal code" as a factual claim. It is wrong.
  - ✅ Write "Egypt Post postcode coverage is inconsistent; the code is **optional** and routing
    depends on **governorate + district**. Do not require the field, and do not invent a code."
  - If a form forces the field, put the district and governorate in full and leave the code blank
    rather than fabricating one.

---

## 4. Phone and contact conventions

### 4.1 Country and mobile formats — ✅ VERIFIED (ITU / Wikipedia numbering plan)

**Country code `+20`. International access `00`. National long-distance prefix `0`.**
Numbering plan is a **closed** plan under the 2003 Telecom Act; regulator is NTRA.

**Mobile — four operators, four prefixes:**

| Operator | Prefix | Local form | International form |
|---|---|---|---|
| **Vodafone Egypt** | `010` | 010 XXXX XXXX | +20 10 XXXX XXXX |
| **Etisalat / e&** | `011` | 011 XXXX XXXX | +20 11 XXXX XXXX |
| **Orange Egypt** | `012` | 012 XXXX XXXX | +20 12 XXXX XXXX |
| **WE (Telecom Egypt)** | `015` | 015 XXXX XXXX | +20 15 XXXX XXXX |

⚠️ **`015` is dual-use and this is a real trap.** Telecom Egypt received a **4G licence** allowing it
to use the `015` prefix for **mobile** services — but `015` was also historically the area code for
**10th of Ramadan City**. The ITU notified a change of the 10th of Ramadan City area code from
`(15)` to `(55)`. ✅ URL OK:
`https://www.itu.int/dms_pub/itu-t/oth/02/02/T020200003E0004PDFE.pdf`
→ **Disambiguate by length: 10-digit national significant number = mobile; 8-digit = landline.**

### 4.2 Landline area codes — ✅ VERIFIED (ITU / Wikipedia)

| City / area | Code | City / area | Code |
|---|---|---|---|
| Cairo, Giza, Qalyubia | `2` | Ismailia | `64` |
| Alexandria | `3` | Suez | `62` |
| **10th of Ramadan City** | `55` *(changed from 15)* | Red Sea | `65` |
| Damietta | `57` | Arish (North Sinai) | `68` |
| Dakahlia (incl. Mansoura) | `50` | El Tor (South Sinai) | `69` |
| Sharqia (incl. Zagazig) | `55` *| Port Said | `66` |
| Gharbia | `40` | Beni Suef | `82` |
| Kafr El Sheikh | `47` | Faiyum | `84` |
| Monufia (Shibin El Kom) | `48` | Minya | `86` |
| Beheira (Damanhur) | `45` | Asyut | `88` |
| Benha | `13` | Sohag | `93` |
| Qena | `96` | Luxor | `95` |
| Aswan | `97` | New Valley | `92` |
| Matruh | `46` | | |

⚠️ **Sharqia/Zagazig is genuinely ambiguous in secondary tables** — Wikipedia's table shows
"10th of Ramadan `15, 554`" and elsewhere Zagazig at `55`. **Treat `55` as contested and verify
against the ITU numbering plan before printing.** Do not hard-code a landline for Sharqia.

**Format:** landlines are `0<area> <subscriber>`; subscriber length varies (Cairo is
`02-XXXX-XXXX`, i.e. 8 digits after `2`; many Delta/Upper Egypt codes are `0<2-digit> XXX XXXX`,
i.e. 7 digits). **Do not assume a fixed national length for landlines.**

### 4.3 WhatsApp as the default business channel

- ⚠️ **PARTIAL (marketing-analyst sourced, not official):** a widely-cited 2026 industry blog puts
  Egypt's WhatsApp base at **~57 million active users (~54% of population)** and claims **>90% of
  Egyptian businesses** use WhatsApp as a primary customer communication channel, with Cairo at
  ~35% of commercial WhatsApp activity. **These are vendor marketing numbers, not NTRA statistics.
  Do not cite them as statistics.**
- ✅ **What is solid and observable:** mobile-network penetration is effectively universal; WhatsApp
  is the default channel for small merchants, clinics, tutors, landlords, tradespeople, drivers and
  small wholesalers; and it **is not a substitute for a legal notice** (see the glossary: إنذار).
- **Agent rule:** put the WhatsApp number on any instruction that involves a counterparty who is
  likely to be an individual or a micro-business; but for any step that starts a legal process
  (notice, demand, filing), **use a registered/formal channel and keep proof of service.**

---

## 5. Official portals — where things are actually filed

Every URL below was HTTP-tested on **2026-10-12**. `❌` = did not respond from this environment.

### 5.1 Company formation and investment

| Body | URL | Status | What you file there |
|---|---|---|---|
| **GAFI** — الهيئة العامة للاستثمار والمناطق الحرة | `https://gafi.gov.eg/en` | ✅ 200 | Public site: investment regimes, incentives, free zones, "why Egypt" |
| **GAFI e-services portal** | `https://portal.gafi.gov.eg/services/eServices` | ✅ 200 | **Company incorporation, licence applications, post-incorporation services** |
| GAFI incorporation procedures PDF | `https://gafi.gov.eg/English/Documents/Companies%20Incorporation%20Procedures.pdf` | ✅ 200 | The official procedure document |
| Investment Law 72/2017 (English) | `https://www.gafi.gov.eg/English/StartaBusiness/Laws-and-Regulations/PublishingImages/Pages/BusinessLaws/Law%20No%20%2072%20of%202017.pdf` | ✅ 200 | Incentives, guarantees, stamp-duty/notarisation exemptions |
| **Golden Licence** | `https://goldenlicense.gov.eg/default_en.aspx` | ✅ 200 | The single strategic-licence route |
| **Investment Zones** | `https://izones.gafi.gov.eg/default_en.aspx` | ✅ 200 | Investment-zone project licensing |
| Invest in Egypt (map of opportunities) | `https://www.investinegypt.gov.eg/English/Pages/exploreMap.aspx` | ✅ 200 | Sector/opportunity map |
| **SCZONE** — Suez Canal Economic Zone | `https://sczone.eg/` and `https://www.sczone.eg/en` | ✅ 200 | Separate authority; **its own register — not GAFI's** |

⚠️ GAFI's site was **rebuilt as a JavaScript SPA**; several legacy `.../English/StartaBusiness/...`
HTML paths now redirect to a styled 404 page that returns **HTTP 200**. A "200" therefore does not
prove a page exists. Deep-link to `gafi.gov.eg/en` and navigate, or use `portal.gafi.gov.eg`.

**GAFI's own published service levels** (✅ VERIFIED, but these are *marketing claims*, not an SLA):
"**1 Business Day** to Incorporate Companies", "**2 Hours** E-incorporation for Sole
Proprietorship", "**20 Business Days** to Issue Permits". Treat as aspirational.

⚠️ **Two distinct GAFI-hosted applications** — a common source of confusion:
`https://portal.gafi.gov.eg/services/eServices` (e-services) vs `https://goldenlicense.gov.eg/`
(golden licence). And **GAFI vs SCZONE vs GOEIC** are three different bodies.

**Company forms and minimum capital** ⚠️ PARTIAL (Chambers + practitioner sources; see file 01 for
the Companies Law):

| Form | Arabic | Minimum |
|---|---|---|
| Limited Liability Company | ش.ذ.م.م | **no statutory minimum** for most activities |
| One-Person Company | ش.ش.و | **EGP 50,000** |
| Closed Joint Stock Company | ش.م.م (مقفلة) | **EGP 250,000** issued capital |
| Public Joint Stock Company | ش.م.م (مطروحة) | listed-market requirements apply |
| Foreign branch / representative office | فرع / مكتب تمثيلي | registered via GAFI; restricted activities |

### 5.2 Commercial Register

| Body | URL | Status |
|---|---|---|
| **مصلحة السجل التجاري** (under Ministry of Supply & Internal Trade) | `https://moiic.gov.eg/` | ❌ did not respond from here |
| ITDA services portal — Commercial Register services | `http://www.itda.gov.eg/registry.aspx` | ✅ 200 |
| ITDA services portal — Commercial Register & legislation | `http://www.itda.gov.eg/sgl.aspx` | ✅ 200 |
| **Digital Egypt** (commercial-registry services now run here) | `https://digital.gov.eg/` | ✅ 200 |
| **Misr Services Centre** — مركز خدمات مصر | `https://www.khadamatmisr.gov.eg/serviceslist` | ✅ 200 |

✅ **VERIFIED and operationally significant:** from **1 January 2026**, **nine** commercial-registry
services became **exclusive to the Digital Egypt platform** — updating registry data; adding an
establishment not in the "شركاتي" (My Companies) system; **enquiring about a commercial register**;
inferring registration status; transferring an individual establishment within the governorate;
obtaining a **commercial register extract**; a commercial-register data certificate; an extract for
**Ministry of Foreign Affairs authentication**; and a **negative certificate**.
Source: Ministry of Communications & IT announcement, `https://msit.gov.eg/?p=7073` — ✅ the article
exists but returned HTTP 500 on test; content verified via the indexed text.
**Agent rule: for any of those nine, send the user to Digital Egypt, not to a registry office.**

### 5.3 Tax

| Body | URL | Status | What you file there |
|---|---|---|---|
| **ETA** — مصلحة الضرائب المصرية | `https://www.eta.gov.eg/` (redirects to `/ar/home`); EN: `https://www.eta.gov.eg/en/home` | ✅ 200 | Tax card, VAT registration, returns, tax clearance |
| ETA taxpayer services portal | `https://www.eta.gov.eg/en/node/67` · new-taxpayer registration: `https://www.eta.gov.eg/en/node/15` | ✅ 200 | Registration & taxpayer services |
| ETA electronic tax services | `https://eservice.incometax.gov.eg/ETax/` | ✅ 200 | Registration, returns, unified tax registration number |
| **eInvoice / eReceipt SDK** | `https://sdk.invoicing.eta.gov.eg/start/` · `https://invoicing.eta.gov.eg/` | ✅ 200 | ERP/POS integration; eSeal X.509 certificate |
| VAT Law 67/2016 (EN PDF) | `https://www.eta.gov.eg/sites/default/files/2024-02/Law-english-no.67-2016.pdf.pdf` | ✅ 200 | Primary text |
| VAT Executive Regulations (EN PDF) | `https://www.eta.gov.eg/sites/default/files/2024-02/VAT-Executive-Regulations-English.pdf` | ✅ 200 | Forms 1/2/3/4 VAT, invoice content |
| Commercial Register Law 34/1976 (EN PDF) | `https://www.eta.gov.eg/sites/default/files/2024-10/law-34-1976.pdf` | ✅ 200 | Primary text |
| Ministry of Finance | `https://mof.gov.eg/en` | ✅ 200 | Fiscal policy, MoF decrees |

⚠️ **ETA's own notice:** from 1 July 2023, **expenses in the tax return are accepted only via the
electronic invoice.** "مهم" notice on the ETA electronic-services landing page. ✅

⚠️ **Commercial Registry Law 34/1976 also exists on the GAFI server** at
`https://www.gafi.gov.eg/English/StartaBusiness/Laws-and-Regulations/PublishingImages/Pages/TradeLaws/...pdf`
(✅ 200). Two authoritative mirrors — useful when one is down.

### 5.4 Customs

| Body | URL | Status | What you file there |
|---|---|---|---|
| **Egyptian Customs Authority** — مصلحة الجمارك المصرية | `https://www.customs.gov.eg/` | ✅ 200 | Declarations, tariffs, e-services |
| Customs declarations | `https://customs.gov.eg/Services/Declartion` | ✅ 200 | **Register and manage declarations at the port/point of entry** (note the misspelling in the live path — it is real, do not "fix" it) |
| **NAFEZA** — Advance Cargo Information system | `https://nafeza.gov.eg/en` · `/en/pages/15` | ✅ 200 | **Advance Cargo Information (ACI)** — the pre-shipment declaration system |

✅ **VERIFIED (NAFEZA, own site):** ACI requires cargo data/documents (**pro-forma invoice and
draft bill of lading if it exists**) **at least 48 hours before shipment** from the export country,
so the state can run its Risk Management System. **Phase 1 pilot 1 April 2021; mandatory from
1 October 2021.** The importer registers on the NAFEZA portal and **obtains an electronic signature
pad** to access it, lists advance cargo data and obtains the **ACID (Advance Cargo Information
Declaration)** before import operations begin. The overseas exporter sends all shipment documents to
NAFEZA via supply-chain networks using **blockchain**, upon vessel departure.
**Agent rule: the ACID is a hard gate. Tell importers to start 48h+ before the bill of lading.**

### 5.5 Social insurance

| Body | URL | Status | What you file there |
|---|---|---|---|
| **NOSI** — الهيئة القومية للتأمين الاجتماعي | `https://www.nosi.gov.eg/` | ✅ 200 | Employer file, insured's contributions, pension |
| Enquiry by national ID | `https://www.nosi.gov.eg/ar/Services/Pages/Info/GetInsuredDetails.aspx` | ✅ 200 | Insurance-number lookup (national ID + mother's first name) |
| New insured number for an individual | `https://www.nosi.gov.eg/ar/Services/Pages/Info/ANewInsuranceNo.aspx` | ✅ 200 | Individual registration |
| Open a **new employer** subscription file | `https://www.nosi.gov.eg/ar/Services/Pages/Info/ANewEmployerFile.aspx` | ✅ 200 | **Employer onboarding — Law 148/2019 + its Executive Regulations** |

### 5.6 Labour

| Body | URL | Status | What you file there |
|---|---|---|---|
| **Ministry of Manpower / Labour** — وزارة القوى العاملة | `https://www.labour.gov.eg/` (EN: `/en/`) | ✅ 200 | Services, job vacancies, foreign work permits, vocational certification |
| Egypt Labour portal (legacy EN index) | `https://www.manpower.gov.eg/index-e.html` | ✅ 200 | Employment office addresses, prohibited companies, foreign work permit, labour inspection |
| Egyptian Employment portal | `https://egyemp.labour.gov.eg/` | ✅ 200 | **Insurance-number enquiry; unified government complaints portal** |
| Ministry hotline | `19468` | — | ✅ VERIFIED (published on `manpower.gov.eg`) |

✅ Services visible on the ministry site: **skill-level certification**; **شهادة القيد (كعب العمل)**
— the "work stub" certificate, obtainable from Digital Egypt; **periodic grants for irregular
workers**; **foreign work permits**; **job vacancies**. ✅

### 5.7 Telecommunications

| Body | URL | Status | What you file there |
|---|---|---|---|
| **NTRA** — الهيئة الوطنية لتنظيم الاتصالات | `https://www.tra.gov.eg/en/` (AR: `/ar/`) | ✅ 200 | **Mobile & internet services: type approvals, licences, equipment, tariffs, consumer rights** |
| NTRA licences | `https://www.tra.gov.eg/en/regulations/licenses/` | ✅ 200 | Licence classes and procedures |
| NTRA contact | `https://www.tra.gov.eg/en/contact-us/` | ✅ 200 | `info@tra.gov.eg`, Cairo 3440 |
| ❌ `https://www.ntra.gov.eg/` | — | ❌ | DNS resolves (81.21.99.250) but **no HTTP response**; **do not send users here** |

✅ **VERIFIED from NTRA's own news feed (2025–2026):** NTRA approves tariff packages and
digital-inclusion measures; conducts **short-number auctions**; conducts **Africa's first trial of
mobile services in the 6 GHz band**; and — operationally important — **refers mobile operators to
the Public Prosecution over line-registration violations** and issues urgent measures about
**lines registered under citizens' names without their knowledge**. ⚠️ *Agent instruction: if a user
reports an unknown line on their ID, NTRA is the regulator to complain to.*

### 5.8 Banking and payments

| Body | URL | Status | What you file there |
|---|---|---|---|
| **CBE** — البنك المركزي المصري | `https://www.cbe.org.eg/en/` | ✅ 200 | Regulator; statistics; circulars |
| CBE payment systems | `https://www.cbe.org.eg/en/payment-systems-and-services/payment-systems` | ✅ 200 | SWIFT, IBAN, CCH, RTGS, ACH |
| CBE cheque clearing services | `.../payment-systems/cheque-clearing-house-cch/services` | ✅ 200 | CIC (image clearing), electronic cheque, DWS, dispute management |
| CBE **multicurrency** CCH | `.../cheque-clearing-house-cch/multicurrency-cch` | ✅ 200 | **USD and EUR cheque clearing** |
| CBE RTGS | `.../payment-systems/real-time-gross-settlement-system-rtgs` | ✅ 200 | Large-value settlement |
| CBE ACH | `.../payment-systems/ach` | ✅ 200 | Small-value bulk clearing |
| CBE SWIFT | `.../payment-systems/swift` | ✅ 200 | Correspondent banking (note: "1123 SWIFT in Egypt") |
| CBE IBAN | `.../payment-systems/iban` | ✅ 200 | IBAN scheme |
| **CBE payment services** | `.../payment-systems-and-services/payment-services` | ✅ 200 | **Payment cards · mobile wallets · payment acceptance channels** |
| **CBE mobile wallets** | `.../payment-services/mobile-wallet` | ✅ 200 | **Register of wallet brands, limits, registration rules** |
| CBE payment acceptance | `.../payment-services/payment-acceptance` | ✅ 200 | Acquiring |
| CBE payment cards | `.../payment-services/payment-cards` | ✅ 200 | Card schemes |
| CBE IBAN validator | `https://www.cbe.org.eg/en/financial-literacy/financial-tools/iban-validator` | ✅ 200 | Structure + validation |
| CBE exchange rates (historical) | `https://www.cbe.org.eg/en/economic-research/statistics/exchange-rates/historical-data` | ✅ 200 | **Do not hard-code a rate** |
| CBE consumer protection | `https://www.cbe.org.eg/en/consumer-protection` | ✅ 200 | Complaints |
| **EBC** — Egyptian Banks Company (national infrastructure operator) | `https://www.egyptianbanks.com/` · IPN: `/instant-payment-network/` · Meeza: `/meeza-card/` | ✅ 200 | **Operates IPN and develops/operates Meeza** |
| **Meeza** | `https://meeza-eg.com/` | ✅ 200 | Domestic card scheme / e-wallets |
| **InstaPay** | `https://www.instapay.eg/` | ✅ 200 | The IPN consumer app |
| **FRA** — الهيئة العامة للرقابة المالية | `https://fra.gov.eg/` | ✅ 200 | Non-bank financial sector; microfinance/CF licence register |
| **GOEIC** — General Organisation for Investment *(Egypt Post savings authority)* | `https://www.goeic.gov.eg/en` | ✅ 200 | Post Office savings | 🟡 I could not confirm the official Arabic rendering of the acronym's expansion — do not guess it into a document |

⚠️ **DO NOT use `CIPS` for Egypt.** See Corrections table item 2.

⚠️ The **mobile-wallet page was readable** (I retrieved the full list) but note its **"Last Updated:
23 Mar 2023"** stamp. The **CBE PDF of the 3rd-version mobile-wallet regulation** (April 2021) is at
`https://www.cbe.org.eg/-/media/project/cbe/listing/circulars/payments-regulations/3rd-version-mobile-wallet-april21.pdf` ✅ 200.

### 5.9 Digital government, e-signature and Post

| Body | URL | Status | What you file there |
|---|---|---|---|
| **Digital Egypt** — مصر الرقمية | `https://digital.gov.eg/` | ✅ 200 | **The citizen/business government-services platform** |
| Legacy alias | `https://misr.gov.eg/` | ✅ 200 | Same platform, older domain |
| **MCIT — Digital Egypt programme page** | `https://mcit.gov.eg/en/digital_egypt` | ✅ 200 | Programme description |
| Cabinet services | `https://www.cabinet.gov.eg/Services` | ✅ 200 | PM-level citizen services |
| Electronic Government Portal services guide | `https://psm.gov.eg/providers/21/services` | ✅ 200 | Service directory |
| **ITIDA** — هيئة تنمية صناعة تكنولوجيا المعلومات | `https://itida.gov.eg/` | ✅ 200 | **Digital signature & electronic seal regulator** |
| ITIDA e-signature page | `https://itida.gov.eg/English/Pages/E-Signature.aspx` | ✅ 200 | **How to get a signature token / an electronic seal** |
| ITIDA e-signature Executive Regulations (EN PDF) | `https://www.itida.gov.eg/English/Documents/4.pdf` | ✅ 200 | Primary text |
| Egypt Post — بريد مصر | `https://www.egyptpost.com/` · `/en` · `/eg-en` | ✅ 200 | Postal, financial, government service counters; registered mail |
| **Egypt Post "Bareedi"** (باريدي) | `https://www.egyptpost.com/Bareedi` | ✅ 200 (JS shell) | **Digital registered mail / proof of delivery** |
| Unified Government Services Centre | `https://www.khadamatmisr.gov.eg/serviceslist` | ✅ 200 | Service list |

✅ **VERIFIED on Digital Egypt's four channels** (from the official Google Play listing for the
Ministry of Communications and IT app): the platform, the website, **post offices**, and the mobile
app, with call centre **15999**; and these payment methods: **bank cards, electronic payment
companies, and mobile phone wallets**.
⚠️ Registration on Digital Egypt is done with the **Egyptian national number + the Egyptian phone
number registered to that national number**. **The same account works on the app and the website.**

✅ **VERIFIED service list on Digital Egypt:** traffic, **catering/documentation (توثيق)**,
**real estate**, courts, **commercial registry**, **real estate tax**, social housing, **civil
status**, and licensing services.

⚠️ **`https://digital.gov.eg/en/` returns 404** — the English path does not exist; there is no
reliable English UI. **Write Arabic instructions for Digital Egypt, or use a translator.**

### 5.10 Real estate, courts, police

| Body | URL | Status |
|---|---|---|
| **Real Estate Registration & Notarisation Authority** — الشهر العقاري | `https://www.realestate.gov.eg/` | ✅ 200 |
| Real Estate platform blog | `https://blogs.realestate.gov.eg/` | ✅ 200 |
| **Ministry of Interior** | `https://www.moi.gov.eg/` · `https://moi.gov.eg/` | ✅ 200 |
| **Traffic unit services** | `https://traffic.moi.gov.eg/` | ✅ 200 |
| Ministry of Trade & Industry (industrial licensing) | `https://www.mota.gov.eg/` | ✅ 200 |
| **Industrial Development Authority** — هيئة التنمية الصناعية (IDA) | `https://www.ida.gov.eg/ar` | ✅ 200 |

⚠️ **Mota.gov.eg is the *other* `gov.eg`**: it is the **Ministry of Trade and Industry**
(وزارة التجارة والصناعة) — the industrial-licensing ministry — **not** the Ministry of Supply and
Internal Trade (التموين والتجارة الداخلية), which is the one carrying the traditional Commercial
Registry. **Arabic speakers routinely confuse these two; agents confuse them more.**
⚠️ `https://www.cde.org.eg/` ❌ did not respond — I could not confirm this as the Commercial Registry
portal. Use Digital Egypt and ITDA's registry page instead.

### 5.11 Legislation databases

| Source | URL | Status | What it is |
|---|---|---|---|
| **Egyptian Legislation Portal (ELP)** — البوابة القانونية للتشريعات المصرية | `https://elpai.idsc.gov.eg/` · `/Home/About` | ✅ 200 | **The Cabinet's own portal.** Created 1998; **judicial rulings back to 1828**; >290,000 legislative instruments; >100,000 rulings; also State Council fatwas, PM decrees, ministerial decisions |
| ELP database breakdown (live) | `https://elpai.idsc.gov.eg/GeneralSearch/Result?searchText=` | ✅ 200 | Legislations 301,286 · cassation rulings 362,748 · administrative rulings 54,157 · economic-court rulings 10,402 · constitutional 3,641 · State Council fatwas 12,867 |
| IDSC (parent) | `https://www.idsc.gov.eg/` | ✅ 200 | Information & Decision Support Centre, PM's office |
| **Official Gazette / Royal Printing Presses** — المطابع الأميرية | `https://www.alamiria.com/Sec/Home` | ✅ 200 | **The Gazette printer.** `الوقائع المصرية` + `الجريدة الرسمية`, with electronic publication |
| **Official Gazette repository** (Information & Documentation Centre, PM's office) | `https://dspace.id.com.eg/` | ✅ 200 | Item-level Gazette records by year — e.g. `https://dspace.id.com.eg/collections/bb4a4122-9215-48e2-a8a5-b622ffa5eeb6` for 2026 (✅ 200) |
| Presidency — national holidays page | `https://www.presidency.eg/en/مصبر/العلاقات-الرسمية/` | ✅ 200 | Presidency site; hosts a national-holidays page |
| **Laa Laws** (Arab Union for Legal Information — **commercial**) | `https://laalaws.com/ETashM/TashSrch` | ✅ 200 | Fast full-text legislation search with **ترتيب** chronological ordering. ⚠️ Commercial — cite the Arabic, not Laa Laws. |
| Fahm Qanon (commercial) | `https://fahmqanon.com/egyptian-legislation-search` | ✅ 200 | ⚠️ Commercial. Its own site admits it is incomplete (339 of 6,361 laws) |

⚠️ **`alqalam.idsc.gov.eg` and `ela.gov.eg` do not resolve in DNS** — despite being commonly cited
as "Al-Qalam" (القلم). ❌ **Do not send anyone to those hostnames.** The working Cabinet legislation
portal is **`elpai.idsc.gov.eg`**. Treat "AlQalam" as an informal/legacy nickname; the official
name is **البوابة القانونية للتشريعات المصرية (ELP)**.
⚠️ `https://gcc.gov.eg/` **resolves and returns 200** but is the **Cultural Development Fund**
(صندوق التنمية الثقافية) under the Ministry of Culture — **not** the Official Gazette. A classic
false friend; the acronym does not survive contact with the page.

---

## 6. E-signature and electronic documents

### 6.1 The legal basis — ✅ VERIFIED (primary text)

**Law No. 15 of 2004** on E-Signature and establishing ITIDA.
Adopted 21 April 2004 · **published in the Official Gazette 22 April 2004** · **in force 23 April
2004**. ✅ (WIPO Lex record; Executive Regulations by **Ministerial Decree No. 109 of 2005**,
published in the Egyptian Government Bulletin No. 115 (Supplement), 25 May 2005 —
✅ URL OK `https://www.itida.gov.eg/English/Documents/4.pdf`.)

**Definitions (Law 15/2004 Art. 1):**
- **Electronic writing (الكتابة الإلكترونية)** — all letters, digits, symbols or signs on an
  electronic, digital, photographic or similar medium giving perceptible meaning.
- **E-signature (التوقيع الإلكتروني)** — marks/letters/digits/codes/signals on an electronically
  written message with a **unique character identifying the signer and distinguishing him/her from
  others**.
- **E-certificate (الشهادة الإلكترونية)** — issued by the authorised entity, proving the relation
  between the signer and the signature-creation data.
- **The signer**, **the certificate-issuing authority**, **signature-creation data** are separately
  defined.

**Evidentiary equivalence — ✅ VERIFIED (primary text):** within civil, commercial and
administrative transactions, an **electronic signature has the same evidentiary authority as
signatures** under the Law of Evidence in Civil and Commercial Matters, provided its creation and
completion comply with Law 15/2004 and the technical/procedural standards in the Executive
Regulations. Likewise **electronic writing and electronic documents** have the same evidentiary
authority as writing and official or private documents.
**Where the Law is silent,** the Law of Evidence in Civil and Commercial Matters governs
authenticity of electronic documents, signatures and writings.

**Validity conditions — ✅ VERIFIED (three conditions, primary text):**
1. The electronic signature is **uniquely linked to the signatory**;
2. The signatory has **sole control over the electronic device** used to create the signature;
3. **Any alteration or modification** to the document or signature data **can be detected**
(public/private-key cryptography + comparison against the certificate and original, or equivalent).

**Secrecy requirements for signature-creation data — ✅ VERIFIED (Executive Regulations):**
exclusivity, secrecy, non-deducibility, protection against forgery/imitation/manipulation,
non-damage to the document's content or meaning, and **no obstruction to the signer reading the
whole document before signing** (that last one is a genuine consumer-protection rule and is often
forgotten).

**Governance:** ✅ ITIDA is the higher e-ratification authority and issues the fundamental code
keys; it licenses **Certification Service Providers (CSPs)** and **inspects and verifies**
signature-creation data on request, for a fee set by its Board.

### 6.2 What you actually obtain — ✅ VERIFIED (ITIDA's own page)

| Product | Who it's for | What it is |
|---|---|---|
| **Digital signature certificate + token** | A **natural person** | Proves the individual's identity. Requires **in-person collection and activation of the token**. |
| **Electronic seal (الختم الإلكتروني)** | A **legal person** (company) | "An electronic signature that allows the **legal person** to identify the creator of the seal and distinguish him/her from others." **Company-level**, not person-level. |
| **GOV-CA certificates** | **Government establishments and agencies** | ✅ "The **only** entity responsible for issuing digital signature/electronic seal certificates to government establishments and agencies is the **Government Digital Certification Authority at the Ministry of Finance (GOV-CA)**." |

**Documents needed for a natural-person token** ✅ (ITIDA): copy of a valid national ID or valid
passport, **original presented for review**.

**Documents needed for a company electronic seal** ✅ (ITIDA):
- recent **commercial registry extract, no more than 3 months old** (articles of incorporation or
  declaration acceptable as an alternative — **original required**);
- a **valid tax card** (ETA-approved basic data card acceptable as alternative — original required);
- the **investment gazette / company gazette** (a contract acceptable as alternative);
- copy of the **legal representative's** valid national ID or passport — ⚠️ **"There is no
  alternative to this document"**; and the legal representative must **present the originals in
  person**.
- If a **delegate** attends instead: an original **letter of delegation** signed by the legal
  representative and **countersigned (certified) by the bank's seal**, bearing the company's seal;
  plus the electronic-seal service contract signed by the legal representative, similarly
  countersigned by the bank's seal.
- **Token collection must be by the legal representative in person — not the delegate.**

**Licensed CSPs named on ITIDA's page** ✅: El Delta Electronic Systems (15715); Fixed Misr
(15966); **Misr for Central Clearing, Depository and Registry (MCDR)** (16774); Egyptian Co. for
Digital Signature & Information Security — **Egypt Trust** (19877; WhatsApp +20 100 075 9637).

### 6.3 What must still be wet-signed — the honest answer

🟡 **UNVERIFIED as a matter of Egyptian law; this is the practical position.**

Law 15/2004 grants electronic signatures *equivalent evidentiary authority*; it does **not** by
itself convert every government filing into a digital-only process. In practice:

| Document | Position |
|---|---|
| Ordinary commercial contracts, NDAs, supply agreements, service agreements | ✅ Electronic signature accepted, especially with an ITIDA-issued token or certified electronic seal |
| Invoices / e-invoices | ✅ **Mandatory** electronic, ETA-platform, eSeal-signed |
| Customs / NAFEZA | ✅ Electronic, **with an electronic signature pad** obtained through the competent authority |
| Court filings | ⚠️ Electronic litigation exists (see file 03) but **wet-ink originals remain routinely required**; bailiffs' offices and paper case files still operate |
| **Real estate transfer / registration at الشهر العقاري** | 🟡 **Treat as wet-signature + notarisation.** Ownership is not complete until registered; the registry and the notary offices are paper-and-stamp processes. |
| **Powers of attorney (توكيل)** | ⚠️ General and special powers are executed before the **Real Estate Registration / Notarisation Authority** (مكتب الشهر العقاري) or a consular officer, **in person, with the original national ID**. The principal must attend. |
| Documents affecting **personal status, family law and succession** | 🟡 Widely treated as requiring specific formalities and generally **not** suitable for e-signature |
| Marriage, divorce, birth/death registration | 🟡 Wet / civil-status formalities |
| Anything requiring **consular legalisation** | ❌ Wet signature then legalisation chain |

**Agent rule (safe and correct):** if the transaction is one where a notary, a registry office, a
traffic unit, a court or a consulate must physically see the signature, **send the user in person
and tell them to bring the original national ID.** Do not send an e-signed PDF.

---

## 7. Payments rails in practice

### 7.1 Cash is still the centre of gravity — ✅ VERIFIED (CBE)

From the CBE's *Monetary and Financial Developments* review (FY 2023/2024):
- **Banknote issue reached EGP 1,199.8 billion at end-March 2024, constituting 9.3% of GDP** for
  the year ending March 2024.
- **Currency in circulation outside the banking system stood at EGP 1,118.6 billion** at
  end-March 2024 (+EGP 109.5bn, +10.8%).
- Denomination mix at end-March 2024: **EGP 200 note 63.2%**, **EGP 100 note 30.7%**,
  **EGP 50 note 3.6%**, aggregate EGP 5/10/20 notes **2.1%**. **Average value of a banknote:
  EGP 77.6** (up from EGP 74.7).
✅ URL OK: `https://www.cbe.org.eg/-/media/project/cbe/listing/research/volumes/2023-2024/volume-64-no,-d-,-3.pdf`

**How to read that as an agent:** an EGP 200 note doing two-thirds of the work means **everyday
transactions are large-value-cash transactions**, not petty cash. Retail price points are high in
EGP; wage packets are paid in notes; and a "cash-dominant" economy at this scale coexists with a
fast-growing digital layer.

⚠️ **PARTIAL (vendor survey, not official):** Statista Consumer Insights put the share of consumers
using **cash at POS at 77% in 2020, declining to 72% in 2023**; cash paid in advance online
**rose 10pp** over the same period. Use this only as a directional indicator and label it as
survey-sourced.

### 7.2 Cheques — still real, and structurally different from other markets

**Clearing rule (EGP)** ✅ VERIFIED — CBE Cheque Clearing House (CCH) Regulations:
- **Art. 1:** the **CBE** is in charge of the CCH, supervising and organising clearing, handling
  settlement problems and making decisions.
- **Art. 2:** membership = registered banks working in **local currency** with HQ or a branch in
  Egypt.
- **Art. 3** (as amended by Governor's Decree 13/2019): the CCH covers **all Egyptian governorates**
  and cheques are settled **on the day following presentation (T+1)**, *regardless of the
  geographical location of the drawee bank's branch*. ✅ **Egypt has abolished the old
  Cairo-T+1 / Delta-T+2 / remote-T+3 geography of cheque clearing.** An agent repeating the
  geographic-clearing table will be wrong — that table appears in pre-2019 practitioner material.
- **Art. 5 — operationally critical:** "The inter-member exchange that takes a **paper form, serves
  as a legal force**, while the **electronic data** form is used **for accounting purposes**
  regardless of the paper cheques." → **The paper cheque is the instrument; the electronic file is
  a record.** Disputes go to paper.
- **Art. 13:** acceptable instruments are cheques, transfer orders, settlement orders and
  rejections. **Instruments must be valued in the Egyptian pound** (for the EGP CCH).
- **Art. 25/26:** **banking rejections** — including where paper differs from the electronic
  record, or "any other legal reason". Disputes are registered and reverse entries are made.

**Cheques in decline — ✅ VERIFIED (CBE data reported in the press):** in **July 2025** the CBE
processed **6.040 million cheques worth EGP 2.56 trillion** — **volume −41% YoY, value −29% YoY**.
The CBE runs a **multi-currency cheque clearing house** covering EGP, **USD and euros**. Average
~**50,000 cheques/day**.
Source: Amwal Al Ghad, 2025-08-07, citing the CBE.
✅ CBE, the CCH's own page: `https://www.cbe.org.eg/en/payment-systems-and-services/payment-systems/cheque-clearing-house-cch`
→ and its **Electronic Cheque (EC)** and **Cheque Image-based Clearing (CIC)** initiatives, whose
stated purpose is to eliminate paper circulation at the deposit stage and cut the collection period
to **one day**.

**Foreign-currency cheques — ✅ VERIFIED (CBE multicurrency CCH page):**
- Covered currencies: **US dollars and euros only.**
- **Two clearing sessions**, held on **consecutive days from Monday to Thursday**, excluding
  **official holidays in Egypt and in the issuing country of the currency**.
- ⚠️ **There is no Friday or Saturday session for foreign-currency cheques.** This alone will break
  a payment plan that assumes the Egyptian working week.
- Governing instruments cited by CBE: **Banking Sector Law No. 194 of 2020**, **Trade Law No. 17
  of 1999**, **CCH Regulations — Foreign Currency**.
- The collecting bank credits the beneficiary or returns the cheque with a **rejection slip**.
✅ URL OK: `https://www.cbe.org.eg/en/payment-systems-and-services/payment-systems/cheque-clearing-house-cch/multicurrency-cch`

**Commercial Code — the commercial-debt threshold:** ✅ "In commercial matters, the **creditor may
request payment of the debt by cheque if the amount of the debt exceeds one hundred thousand
pounds.**" (Law 17/1999, transitional provisions; cheque provisions in force since 1 Oct 2005.)
✅ URL OK: `https://eg.andersen.com/wp-content/uploads/2025/12/Law-No.-17-of-1999.pdf`

### 7.3 Bank transfer and the account model

- ✅ **IBAN is mandatory in practice** (CBE direction effective 30 June 2020 per NBK). 29 characters.
- ✅ **Non-resident foreigner accounts:** the CBE issued a circular on **7 August 2024** clarifying
  procedures for opening bank accounts and providing banking services to **non-resident foreign
  clients**, stating that there are **no restrictions** on opening accounts for them and that
  refusal exposes the bank to reputational and regulatory risk. ⚠️ PARTIAL (law-firm summary of the
  circular; I did not retrieve the CBE circular itself). **Agent rule: a foreign buyer should NOT
  be told "you cannot open an account in Egypt."**
- **Typical retail KYC for a non-resident** ⚠️ PARTIAL (HSBC Egypt published requirements, used as
  an illustration of the market, not as a universal rule): **original passport with a valid entry
  visa**; **proof of residence** (electricity/telephone bill, or a tenancy contract issued or
  notarised by a governmental or public entity); **proof of employment** (HR letter, or tax card
  for self-employed); and, for foreigners or Egyptians whose address is not updated on their
  national ID/passport, the same proof-of-residence package.
- 🟡 **Some banks are salary-only.** HSBC Egypt's published current account at the research date
  was "currently open to **salary-based customers only**" with a minimum monthly gross salary
  transfer of **EGP 10,000**. **Do not write "open an Egyptian bank account" as a generic step —
  ask what the bank will actually accept.**

### 7.4 Mobile wallets — ✅ VERIFIED (CBE + operator pages)

**CBE's registration model** ✅ (CBE mobile-wallet page):
1. Visit a **bank branch, telecom company branch, or bank agent**.
2. Fill and sign the registration form **free**, using a **valid national ID** and a **mobile phone
   number, with both the number and the applicant's data matching**.
3. Receive an SMS with the app link and an **activation code**.
4. Set an **M-PIN**.
- **Only one e-wallet per mobile number.** **Maximum 3 e-wallets per national ID.**
- ⚠️ The CBE page states **individual limits of EGP 30,000/day and EGP 100,000/month.** ⚠️ **Operator
  pages state higher limits.** See the table below — **limits differ by provider and by customer
  type; always read the current operator terms.**

**Operator-published limits** ⚠️ PARTIAL — operator pages, checked 2026-10-12:

| Wallet | Operator | Individual daily | Individual monthly | Wallet max | Business daily | Business monthly | Cash-out/day |
|---|---|---|---|---|---|---|---|
| **Vodafone Cash** | Vodafone | EGP 60,000 | EGP 200,000 | — | — | — | — |
| **Orange Cash** | Orange | EGP 60,000 | EGP 200,000 | EGP 200,000 | EGP 80,000 | EGP 400,000 | ATM 30,000 / outlets 60,000 |
| **Etisalat Cash / e&** | e& | EGP 30,000 | EGP 100,000 | EGP 100,000 | — | — | ATM 20,000 / outlets 30,000; cash-in/day 50,000 |
| **WE Pay** | Telecom Egypt | ⚠️ not captured | | | | | |

⚠️ **Orange Cash newly-registered wallets** are capped for the **first 90 days**: daily **EGP 10,000**,
monthly **EGP 60,000**. ⚠️ **Orange Cash wallet rules require a valid national ID and an Orange line
registered in the subscriber's name; maximum 3 wallets on 3 different lines.**
⚠️ **Etisalat Cash requires a valid national ID and an e& line registered in the subscriber's name;
max 3 wallets and 3 lines per national ID**; cash-in/cash-out at **Fawry outlets, e& stores and ATMs**.
⚠️ **Etisalat Cash top-up limits: minimum EGP 5, maximum EGP 250** per transaction.
✅ URLs OK: `https://web.vodafone.com.eg/en/vodafone-cash` · `https://www.orange.eg/en/services/orange-financial-services` · `https://te.eg/en/web/guest/personal/we-pay` · `https://www.etisalat.eg/`

**The wallet brand is NOT the operator.** ⚠️ **Important:** the CBE's own register shows the **same
brand deployed by several institutions** — e.g. **Vodafone Cash appears with both Vodafone and
ALEXBANK**; **Orange Cash and Etisalat Cash appear with the National Bank of Egypt and Banque du
Caire** respectively; **WE Pay appears with Banque Misr and with Telecom Egypt.** The CBE register
lists 29 wallet brands across banks including BM Wallet, Ma7fazty, QNB Wallet, Cashati, Halan Cash,
Phone Cash, Easy Cash, Smart Wallet, Ameen, Banki Wallet, Audi2Pay, ABK Wallet, 3altayer, SCB
E-Wallet, UB Wallet, E-Pocket, ADCB Wallet and Agri-Wallet.
**Agent rule: "send me your wallet" is not a sufficient instruction. Ask for the *issuing
institution*.**

**CBE lists the wallet service set** ✅: cash deposit & withdrawal (ATMs, branches, operator stores,
agents); send/receive including cross-border; **Virtual Card Number (VCN)** — a one-time-use card
for internet purchases; **Account Value Load (AVL)**; payroll and pension disbursement;
bill payment and top-up; charity; **QR payment**; **Request To Pay (R2P)**; **B2B payments**; and
**governmental payments — licences, traffic fines, taxes, customs**.

### 7.5 InstaPay and the Instant Payment Network (IPN)

✅ **VERIFIED (InstaPay's own Q&A + EBC):**
- InstaPay is "the **first Payment Service provider (PSP) licensed by the Central Bank of Egypt** to
  operate over the **Instant Payment Network (IPN)**, enabling instant transfers between banks
  24/7."
- **In 2020 the CBE mandated all banks operating in Egypt to support IPN.** EBC — the operator of
  the national payment infrastructures — launched IPN **less than two years later**.
- **You can transfer to:** **IPA (Instant Payment Address)**, a **mobile number**, a **digital
  wallet mobile number**, a **bank account number or IBAN**, and **any Meeza card (debit, credit
  or prepaid)**.
- Onboarding: download the app; the **mobile number must be registered at your bank**; create a
  unique IPN account; secure it with an **IPN PIN**.
- EBC describes IPN as supporting fully digitised customer self-registration, account-alias
  management and simplified transfers **using a mobile number**, balance inquiry and mini-statement.
✅ URLs OK: `https://www.instapay.eg/` · `https://www.egyptianbanks.com/instant-payment-network/`

**Agent instruction:** for an Egyptian counterparty, **"send it to my InstaPay/IPA" is now a normal
instruction.** Also ask for the counterparty's **IPA** — it is more stable than a phone number.

### 7.6 Meeza and cards

✅ **VERIFIED (EBC):** Meeza is **Egypt's domestic card payment scheme**, established following the
National Payment Council's **2017 decree** creating a national payment scheme, and **entrusted by
CBE directive to EBC** to develop and operate. Features: **24/7 availability**, **issued by 32
banks**, debit and prepaid, wide acceptance at **ATMs, POS, government units, online and in-store**,
and **compliant with international card standards**. It is positioned as **the efficient payment
method for government bills**. ✅ `https://www.egyptianbanks.com/meeza-card/` ·
`https://meeza-eg.com/`

### 7.7 E-commerce and retail acceptance

✅ **VERIFIED (FawryPay's own product page):** FawryPay offers — **cash on delivery**;
**card payment (Mastercard, Visa, Meeza)**; **digital wallets** (bank-operated and operator), by
**QR scan** or **wallet number + mPIN**; **payment by reference code** at Fawry's retail POS network
or at any Fawry Plus branch; **Pay By Link** (generated by SMS, call centre, or shareable link);
**ATM / IVR / e-banking** channels; **installment programmes**; **automatic card collection (recurring
payments)**; and a **full refund** capability, including **cash refunds via OTP at any Fawry POS**
for reference-code payments.
✅ URL OK: `https://fawrypay.online/solutions/omni-channel`

✅ **VERIFIED (Aman):** `https://aman.eg/en/` — instalments at ATMs/POS; a **POS solution for bank
acceptance**; an **Aman instalment merchant** product; and bill/instalment payment, accepting all
bank cards, e-wallets and instalment services.

⚠️ **PARTIAL (payment-infrastructure vendor):** the mainstream licensed consumer-finance/BNPL
brands integrated on the domestic rails include **valU, Halan, Sympl** ⚠️ (not individually
verified), **Souhoola, Mogo, Premium Card, Contact Now, Forsa, Klivvr, Tru**. ⚠️ **Check FRA's
register at `https://fra.gov.eg/` before naming a licensed lender in an instruction.**

**Installments are not a niche in Egypt — they are mainstream consumer finance.** An e-commerce
instruction that offers only "card or cash on delivery" is leaving out the largest segment of
Egyptian online purchasing.

### 7.8 What evidence a person should keep

| Payment method | Keep |
|---|---|
| **Cash** | A **signed and dated written receipt (إيصال)** naming payer, payee, amount in figures **and words**, the purpose, and the property/period concerned. ⚠️ If the amount is large or the lease is contested, a **bank-routed transfer is better evidence than any receipt.** |
| **Bank transfer / IBAN** | The **bank confirmation/receipt** and a **bank statement extract** covering the period. ✅ Arabic practice commentary treats bank receipts and statements as **official documents with high evidentiary weight**. The statement must show date, payer, payee, amount. |
| **Cheque** | The **cheque itself (original)** + the payer's **bank statement showing the debit** + the payee's **statement showing the credit**; the **rejection slip** if returned. |
| **Mobile wallet / InstaPay** | The **app confirmation screen / SMS + transaction reference**, and the payee's **account statement**. ⚠️ **Screenshots alone are weak. Always attach the counterparty's bank statement.** |
| **Card** | The **merchant receipt / invoice**, plus the **ETA eInvoice** where the seller is registered (see §2.3). |
| **Anything that starts a legal process** | **Proof of service** — registered mail (Egypt Post **Bareedi** for electronic registered mail), a court filing receipt, or a bailiff's act. |

**The single most important sentence for an agent:** *a screenshot is not a payment record; a bank
statement is.* If the transaction is material, tell the user to route it through a bank so the
statement exists.

---

## 8. Bureaucracy reality

### 8.1 Official service levels vs what practitioners report

| Step | Official claim | Reality |
|---|---|---|
| Incorporate a company via GAFI | ✅ GAFI publishes "**1 Business Day** to Incorporate Companies", "**2 Hours** E-incorporation for Sole Proprietorship" | 📅 **ESTIMATE (practitioner-reported):** for a clean, complete, domestic, straightforward file, **days to a couple of weeks**. Anything involving a foreign shareholder, legalised foreign documents, apostille/legalisation of a power of attorney, or an in-kind contribution valuation runs to **weeks, and often months**. |
| Issue investment permits | ✅ GAFI publishes "**20 Business Days** to Issue Permits"; Chambers reports GAFI's electronic Investment Licensing Platform **"targets issuance of licences within 20 working days of a complete file"** | 📅 **ESTIMATE:** "complete file" is doing a lot of work. In practice, the critical path for a foreign investor "is **not the Egyptian filing itself but the preparation and consular legalisation of the foreign corporate documents and powers of attorney**". Start that first. |
| The nine Digital-Only commercial registry services | ✅ From **1 Jan 2026**, exclusive to Digital Egypt | 📅 **ESTIMATE:** online filing removes the queue but **does not remove the document problem.** Most failures are missing/expired documents, not missing technology. |
| Industrial licence (IDA) | Law 15/2017 split licences into **إخطار** (notification, low risk) and **ترخيص** (licence, medium/high risk) | 📅 **ESTIMATE:** a licence-tier application requires a **site inspection (معاينة الموقع)**, safety and environmental conditions. Plan in **weeks to months**. |

**Where the clock actually goes** 📅 **ESTIMATE (practitioner-reported):**
1. **Tax card** — reported to be required **within 30 days** of the CR entry, with penalties
   otherwise. ⚠️ This "30 days" figure came from a commercial tool page, **not from an ETA
   publication** — treat it as ⚠️ and verify.
2. **Notarisation / attestation** of foreign documents.
3. **Legalisation chains** — embassy → Egyptian Ministry of Foreign Affairs.
4. **Office attendance** and the physical return of the token / original documents.
5. **Stamp duty payment** at the bank (see §8.3).

### 8.2 Who you need — lawyer, notary, or neither

| Step | Who you need | Why |
|---|---|---|
| Simple LLC, all-Egyptian partners, no licences | 📅 **Often no lawyer** | GAFI's e-incorporation; an accountant is more useful than a lawyer |
| Foreign shareholder, foreign documents, or a complex share structure | **Lawyer** (essential) | Legalisation chain, capital, governance, tax |
| **Power of attorney (توكيل)** | ✅ **Notarisation office** | Executed before the **Real Estate Registration / Notarisation Authority (مكتب الشهر العقاري)** or a consular officer. ⚠️ **The principal must attend in person with the original national ID.** ⚠️ A lawyer's Syndicate card is *recommended*, not required. |
| **Any contract whose performance you may sue on** | 📅 **Lawyer** | The **original** is what matters in litigation |
| **Real estate** | ✅ **Notarisation office + registry** | Ownership is not complete until registered |
| Court filing / representation | **Advocate (محامٍ)** + **tawakil** | See file 03 |

### 8.3 The two tax/charge items a user will hit on day one

⚠️ **PARTIAL (specialist tax summary of Law No. 111 of 1980 as amended; verify before quoting):**

- **Stamp duty (ضريبة الدمغة / ضريبة الأختام)** under **Law No. 111 of 1980**, as amended by Laws
  140/2006, 110/2018, 147/2019, 174/2019, 199/2020 and 30/2023.
- Two types: **nominal** (fixed, per document/page) and **proportional** (percentage of value).
  Contracts are broadly **~EGP 1 per page per copy** nominally; proportional rates range
  **0.05%–0.6%** by transaction type.
- ✅ **Verified from the Arabic source (Law 199/2020 amending Law 111/1980):** a **nominal duty of
  EGP 1.50 (مائة وخمسون مليماً)** per sheet of **any contract, whether for consideration or not,
  civil or commercial, and even if concluded by correspondence**, plus certificates relating to
  waqf. ✅ URL OK:
  `https://eta.gov.eg/sites/default/files/2024-03/law_no.199-2020.pdf`
- ✅ **Investment Law 72/2017 exemption (verified primary text):** **memoranda of incorporation of
  companies and establishments, and credit-facility and pledge contracts relating to the
  business, are exempt from stamp duty as well as from notarisation and publicity fees for
  5 years** from the date they are entered in the Commercial Register. ✅ URL OK (GAFI PDF).
- ⚠️ **GAFI incorporation fees (practitioner summary):** authentication **0.25% of paid-in capital
  capped at EGP 10,000**; GAFI service fee **0.1% of capital, min EGP 1,000, max EGP 10,000**.
  ⚠️ **UNVERIFIED against an official fee schedule — confirm before telling a user a number.**

### 8.4 Online vs in person — the current balance

**Genuinely online (and often mandatory online):**
- ✅ The **nine commercial-registry services** (Digital Egypt only, from 1 Jan 2026)
- ✅ **e-invoicing / e-receipt** (ETA platform; eSeal X.509)
- ✅ **NAFEZA ACI** + **ACID** (mandatory since 1 Oct 2021)
- ✅ **Digital Egypt services**: traffic, real estate, real estate tax, civil status, commercial
  registry, courts, licensing, catering/documentation
- ✅ **Post offices** as service outlets for Digital Egypt transactions ✅ **VERIFIED**
- ✅ **Bank account opening / KYC** at many banks; wallet registration **at a branch or agent** (the
  CBE process still involves an in-person form and token/M-PIN activation)

**Still in person, essentially always:**
- ✅ **Power of attorney** — notarisation office or consulate, principal present, original ID
- ✅ **Electronic seal token issuance** — **the legal representative in person**; originals presented
- ✅ **Digital signature token issuance and activation** — in person
- ✅ **Court filing with paper originals**, bailiff service, in-person appearances
- ✅ **Traffic unit** for vehicle and licence matters requiring inspection, testing, medical
- ✅ **Real estate registration** at الشهر العقاري
- ✅ **Bank account opening** for many products
- ⚠️ **Tax office (مأمورية) visits** for card issuance, despite the electronic portal

---

## 9. Dates, working days and public holidays

### 9.1 Date formats — ✅ VERIFIED (pattern observable across official documents)

| Convention | Form | Where |
|---|---|---|
| **dd/mm/yyyy** — the dominant Egyptian written form | `25/04/2026` | Contracts, court papers, receipts, official forms |
| Gregorian month names | January…December (often written in Latin letters in English-facing documents) | ✅ Observed in official English text |
| **Arabic-Indic numerals** | `٢٠٢٦/٠٤/٢٥` | Printed documents; **note the digits run left-to-right inside RTL text** |
| Fiscal year | **July – June** | Government and many corporates. **"FY 2025/26" means the year ending 30 June 2026.** |
| ❌ US `mm/dd/yyyy` | — | **Never acceptable.** An Egyptian reader reads `04/25` as invalid. |

**Agent rule:** always emit **dd/mm/yyyy** and, if there is any doubt, spell the month out.

### 9.2 The working week — the answer depends on which institution

⚠️ **This is where "Egypt's weekend is Friday–Saturday" becomes an operational error.**

| Institution | Working week | Evidence |
|---|---|---|
| **Government / civil service (the legal default)** | ✅ **Sunday – Thursday** | HSBC Egypt publishes its callback service as "**Sunday to Thursday**, 9:30am–3:30pm"; out-of-hours callbacks are handled "the next working day". ✅ `https://www.hsbc.com.eg/accounts/products/current-account/` |
| **Private sector generally** | ✅ **Sunday – Thursday**, with **Friday or Saturday** as the weekly rest | ✅ Labour Law 12/2003 **Art. 83** (verified English translation): each worker gets "a weekly period of rest of not less than **twenty-four complete hours after at most six continuous working days**" — and it is **paid**. The statute fixes **one** rest day, not **two**. |
| **Statutory maxima** | ✅ **8 hours/day, 48 hours/week**, excluding meal and rest; breaks **≥1 hour** and the worker must not be kept **>5 continuous hours**; the span from start to finish **≤10 hours/day** | ✅ Labour Law 12/2003 **Arts. 80–82** |
| **Banks** | ✅ **Sunday–Thursday** core; **selected branches open later or on Friday** | ✅ CBE extended the hours of selected branches to **5:00 pm instead of 3:00 pm** (CBE news, 2025-07-08) ✅ URL OK. Banque Misr publishes branch hours of **Sun–Thu 10:00–18:00** with **Friday (Winter) 13:00–17:00 / (Summer) 14:00–18:00**, and Ramadan branches running **24h with full banking 09:00–15:00** and currency-exchange/POS/remittance services outside those hours. |
| **Foreign-currency cheque clearing** | ✅ **Monday – Thursday only**, two consecutive sessions, excluding Egyptian and issuing-country holidays | ✅ CBE multicurrency CCH |
| **Cash/retail** | ✅ Effectively **daily**, including Friday | 🟡 FOLKLORE, but observationally uncontroversial: shops and markets open on the weekend; that is part of why cash dominates |

**Agent rule:** **never compute an Egyptian deadline without knowing which institution's calendar
applies.** A court deadline, a bank deadline and a mobile-wallet limit are all on different clocks.

### 9.3 Public holidays — describe the rule, never the calendar

> ### ⚠️ HARD RULE FOR THIS FILE
> **Do not publish or rely on a dated holiday calendar for any future year.** Egypt's holiday list
> contains a **Hijri-based component whose Gregorian dates cannot be fixed more than ~1 year ahead**,
> plus **Coptic-calendar** dates, plus **occasionally ad-hoc days declared by decree** and days
> **substituted to align the week**. Any generated list for a future year will be wrong.
> **Tell the user to confirm against the Presidency's published national-holidays page and the
> current year's Ministry of Labour decree before relying on a date.**

✅ **VERIFIED rule (Ministerial Decree No. 294 of 2025):** the Minister of Labour sets by decree which
national and religious occasions are **full paid holidays** under the Labour Law, listing:
**Islamic:** Hijri New Year; the Prophet's Birthday; **the first two days of Shawwal**
(Eid al-Fitr); **Arafat Day and the first two days of Eid al-Adha**; **Civic/religious:** **Coptic
Christmas (7 January)**; **25 January Revolution / Police Day**; **Sham El-Nessim**;
**Sinai Liberation Day (25 April)**; **Labour Day (1 May)**; **June 30 Revolution**;
**23 July Revolution**; **Armed Forces Day (6 October)**.
✅ **And — the operational rule that matters:** "**The Minister of Labor may replace any listed
holiday with a working week's start/end day to unify holidays nationally.**"
→ **A holiday can move, and a working day can become a holiday, by ministerial declaration.**

⚠️ **Caveat on the parent statute:** this decree is described as made "under the Labour Law".
Note that **Labour Law 12/2003 was repealed on 1 September 2025 by Labour Law 14/2025** (see file
03). **Confirm whether a re-issued decree under Law 14/2025 exists before citing the holiday list as
operative.** Do not assume.

**Observations for planning (not a calendar):**
- The **Hijri** block (New Year, Mawlid, Eid al-Fitr, Arafat, Eid al-Adha) and the **Coptic** block
  (Christmas, Sham El-Nessim) are **lunar/solar-lunar and drift ~11 days earlier each Gregorian year**,
  then jump back.
- **Eid and the Coptic feasts run as multi-day blocks**, so a fortnight of disrupted business is
  normal, not exceptional.
- **Sham El-Nessim** (a Monday-ish Coptic Easter festival) is a **national holiday with no fixed
  Gregorian position**.
- Presidency holiday pages exist ✅ (`https://www.presidency.eg/`), but **they are published per year
  and are the right source to cite, not a generated list.**

### 9.4 The deadline rule that actually saves cases

✅ **VERIFIED (Code of Civil and Commercial Procedures, Law 13/1968, English translation by Andersen
Egypt, Art. 18):** "**Where the final day of a time limit falls on an official holiday, the time limit
shall be extended to the first working day thereafter.**"
✅ URL OK: `https://eg.andersen.com/wp-content/uploads/2026/08/Law-No.-13-of-1968.pdf`

Supporting rules from the same translation:
- **Art. 15:** the day of service, or the event that starts the time limit, is **not counted**; a
  limit that must expire before a step may be taken means the step cannot be taken until after the
  final day; a period **within which** a step must be taken expires at the end of its final day.
- **Time limits in months or years are computed on the Gregorian calendar** unless the law says
  otherwise.
- **Art. 15 (service):** no service or enforcement procedure may be carried out **before 7:00 a.m.,
  after 8:00 p.m., or on official holidays**, except in cases of necessity with the written
  permission of the Judge of Summary Matters. → **Agents: never serve a paper on a public holiday.**
- ✅ **Appeals:** the period for appearance is **15 days before the Court of First Instance and the
  Court of Appeal**, and **8 days before the District Courts**; reducible in necessity to 3 days and
  24 hours respectively. (See file 03 for the appeal periods themselves.)

> ⚠️ **Critical caveat:** "**working day**" here means a **day the relevant court/office is open**,
> which is driven by the court calendar, the public holidays, and (for electronic filing) the
> e-filing calendar. **Do not compute "first working day thereafter" from the weekday alone.**

---

## 10. English ↔ Arabic glossary of practical terms

**How to use this table.** This is the working vocabulary an agent needs to read an Egyptian
document, send an instruction to an Egyptian counterparty, or avoid a translation error that changes
the legal meaning. The **Trap** column says what goes wrong if you translate naively.

**Two symbols recur:**
- 🔴 **COLLISION** — one Arabic word maps to two or more English words. Picking the wrong sense
  produces a nonsense instruction.
- ✅ **NO SINGLE EQUIVALENT** — there is no clean one-to-one English rendering; a deliberate
  translation decision is required and the naive one is wrong or comic.

**Deliberately excluded:** pleasantries, kinship terms, food, and geography. None of them change a
legal or commercial instruction. What is here is what changes an *instruction*.

### 10.1 Currency, amounts and charges

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 1 | ج.م / جنيه مصري | جنيه | Egyptian pound (EGP) | Never "Egyptian dinar". ISO 4217 = **EGP / 818**. | — |
| 2 | قرش | — | piastre (1/100 EGP) | **Dead currency.** Nobody prices in piastres — but they appear in cheque words-lines. | — |
| 3 | الأرقام | — | figures | The **numeral** form of an amount. | — |
| 4 | بالحروف | — | in words | The **written-out** form. This is the الأرقام/بالحروف pair. | — |
| 5 | لا غير | — | "and nothing more" | Closes the words-line on a cheque. Omit it and the line is open to tampering. | ⚠️ |
| 6 | تفقيط | — | writing an amount out in words | Also the name of the Egyptian tools that do it. | ⚠️ jargon |
| 7 | المبلغ | — | the amount | — | — |
| 8 | المدفوع / المستحق | — | amount paid / amount due | **Distinguish.** Rendering المستحق as "paid" manufactures a debt. | 🔴 |
| 9 | باقي | — | balance / remaining | — | — |
| 10 | قسط / أقساط | — | instalment(s) | Where the consumer-finance sector meets B2B. | — |
| 11 | الحوالة | — | the transfer / the assignment | 🔴 Collision: a **bank transfer**, an **assignment of a claim**, and "remittance". Disambiguate. | 🔴 |
| 12 | التحويل | — | transfer / conversion | 🔴 Collision: bank transfer? FX conversion? assignment? Pick one explicitly. | 🔴 |
| 13 | عمولة / رسوم | — | fee / charge | Not the same as مصروفات (#16). | ⚠️ |
| 14 | دمغة / ضريبة الدمغة | — | stamp duty / revenue stamp | A **tax**, paid at the bank — not a postmark. | ✅ **YES** |
| 15 | ختم / الختم البريدي | — | stamp / postal stamp | 🔴 **Totally unrelated to الختم الإلكتروني (#83).** | 🔴 |
| 16 | مصروفات | — | costs / expenses | Legal spend — **not** الرسوم القضائية (#17). | ⚠️ |
| 17 | الرسوم القضائية | — | court fees | Distinct from مصروفات. | ⚠️ |
| 18 | مأمورية الضرائب | — | the (local) tax office | A specific ETA district office. **No English equivalent** — write "your local tax office (مأمورية)" and keep the Arabic. | ✅ **YES** |
| 19 | الشباك | — | the service window | The physical government counter. "counter" works; "desk" does not. | ✅ **YES** |

### 10.2 Identity, persons and capacity

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 20 | الرقم القومي | — | national ID number | **The master identifier.** Not "civil number", not "national number". | — |
| 21 | بطاقة الرقم القومي | — | national ID card | — | — |
| 22 | الرقم التأميني | — | social insurance number | Do **not** assume it equals the national ID — that is unverified. | — |
| 23 | كعب العمل | — | "work-stub" certificate | A proof-of-employment extract issued via Digital Egypt. Literally "the work's heel". **No English equivalent** — write "employment certificate (كعب العمل)" and keep the Arabic. | ✅ **YES** |
| 24 | شهادات | — | notaries | 🔴 **Collision:** شهادة = "certificate" generally. **شهادة استخراج = Notary Public (a person).** Never render a notary as "a certificate". | 🔴 |
| 25 | كاتب عدلي | — | notary (judicial) | The officer before whom a توكيل / real-estate instrument is executed. **Distinct from #24.** | ⚠️ |
| 26 | محضر | — | bailiff / process server | In **court** context only. In محضر الضبط or a minuted session it means "a record". | 🔴 (contextual) |
| 27 | محضر الضبط | — | record of inspection / official report | Written by a محضر on inspection. | ⚠️ |
| 28 | الموكل / الوكيل | — | principal / attorney (under a POA) | ⚠️ Not "the agent" in the agency-law sense. | ⚠️ |
| 29 | التوكيل | — | power of attorney | عام (general) / خاص (special). Executed **in person**. | — |
| 30 | التوكيل الخاص | — | special power of attorney | The everyday form. Don't use the fusha "النوعي" with a shopkeeper. | — |
| 31 | الشغلة / العامل | — | the job / the worker | 🔴 **الشغلة** colloquially = "the work/job" AND (pejoratively) "the situation". Don't translate literally. | 🔴 |

### 10.3 Documents, copies and evidence

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 32 | تذكرة | — | receipt / voucher / coupon | 🔴 **This is NOT the word for a payment receipt.** Use إيصال (#34). Use تذكرة for tickets, vouchers, coupons. | 🔴 |
| 33 | وصل | — | receipt stub / counterfoil | The duplicate of a receipt. | ⚠️ |
| 34 | إيصال | — | receipt (payment) | **The correct word for proof of payment.** | — |
| 35 | إيصال استلام إيجار | — | rent receipt | Exactly what landlords hand-write on a plain form. | — |
| 36 | صورة | — | copy | **The everyday Egyptian word for "copy" is صورة — "picture".** "ممكن صورة؟" means "can I get a copy?" Never render this as "picture". | ✅ **YES** |
| 37 | أصل | — | original | ⚠️ **But أصل is also used loosely to mean "copy" in Egyptian speech.** Use **"الأصل"** for the original, **"الصورة"** for the copy, and add **مختوم** (stamped) where the seal is what matters. | ⚠️ |
| 38 | مستخرج | — | official extract | A certified printout from a register (مستخرج سجل تجاري, مستخرج حكم). **Not a "copy"** — it carries evidentiary weight of its own. | ✅ **YES** |
| 39 | مذكرة عرض / محضرتسليم | — | delivery note / handover minute | Physical handover evidence. | ⚠️ |
| 40 | ثبت بسند | — | "he proved it by the instrument" | Everyday litigant's phrasing. **No English equivalent** — render as "he established it by the deed / the instrument". | ✅ **YES** |

### 10.4 Notices, litigation and enforcement

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 41 | إنذار | — | legal notice / formal demand | ⚠️ Also the everyday word for "a warning". **"Ultimatum" is too aggressive** — use "legal notice" or "formal demand". | ⚠️ |
| 42 | إنذار على يد محضر | — | service of notice by bailiff | **The gold standard for proof of service in Egypt.** | — |
| 43 | الإخطار | — | the notice (formal) | ⚠️ A **different legal act** from إنذار (#41) and from الإعلان (#45). Three registers. | ⚠️ |
| 44 | التسليم | — | delivery / handover | Both physical delivery of an item and legal service. | ⚠️ |
| 45 | الإعلان | — | formal service / publication (of a notice) | **الإعلان is the legally effective act** of making a document reach a party. | ⚠️ |
| 46 | حكم | — | court judgment | 🔴 **Collision:** حكم also means "rules/regulations". In litigation, always حكم. | 🔴 |
| 47 | حكم نهائي | — | final judgment (not appealable) | — | — |
| 48 | حكم ابتدائي | — | first-instance judgment | — | — |
| 49 | دعوى صحة التوقيع | — | action to confirm a signature | A **reserved/conservatory** action: it proves the signature is the defendant's. It does **not** decide ownership or the validity of the deal. | ⚠️ |
| 50 | تنفيذ | — | enforcement / execution | محاكم التنفيذ are the enforcement courts. | — |
| 51 | حضور | — | the hearing / to attend | — | — |
| 52 | ميعاد | — | the scheduled date / hearing date | — | — |
| 53 | التماس | — | the application / petition | — | — |
| 54 | فك العقد / فسخ العقد | فك | termination / rescission | 🔴 **فك = terminate prospectively. فسخ = rescind/annul retroactively. Different legal consequences — never merge.** | 🔴 |
| 55 | تمديد | — | extension (of time) | Different from تجديد (#56). | ⚠️ |
| 56 | تجديد | — | renewal | Of leases, licences, IDs, registers. | — |

### 10.5 Tenancy and property

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 57 | إيجار | — | lease / rent | 🔴 **Means both the contract AND the rent itself.** "the lease expired" and "the rent went up" are the same word. Disambiguate in English. | 🔴 |
| 58 | إيجار قديم | — | old-system lease | ⚠️ **NOT "old".** A lease carried over from the **pre-1996 regime**. | ✅ **YES** |
| 59 | إيجار جديد | — | new-system lease | ⚠️ **NOT "new".** A lease governed by the **current Civil Code regime** (Law 4/1996 and following). | ✅ **YES** |
| 60 | إيجار مفروش | — | furnished lease | Law 4/1996 carved furnished property out of its scope. | ⚠️ |
| 61 | المالك / المستأجر | — | landlord / tenant | — | — |
| 62 | الشقة / الدور / الدور الأرضي | — | flat / floor / ground floor | **Floor numbering ≠ English.** See the dedicated warning in §3.2. | ✅ **YES** |
| 63 | عمارة | — | the building / the block | Not "imāra" to an Egyptian — it is just "the building". | — |
| 64 | شارع / ميدان | — | street / square | ميدان is a named square/plaza, often the local landmark. | — |
| 65 | الشهر العقاري | — | Real Estate Registration & Notarisation Authority | "Title registry" is understood but is **not** a term Egyptians use. Ownership is **not complete** until registered here. | ⚠️ |
| 66 | التسجيل | — | registration | Always say **at the real estate registry (الشهر العقاري)** — not just "registered". | ⚠️ |
| 67 | القيد / التحفظ | — | the entry / the caution (over it) | ⚠️ "Reserved" ≠ "booked". القيد = the register entry; التحفظ = the caution noted over it. | ⚠️ |
| 68 | الرهن العقاري | — | real estate mortgage | — | — |
| 69 | التمليك / الحيازة | — | ownership / possession | ⚠️ Different estates — do not conflate. | ⚠️ |

### 10.6 Corporate, tax and commercial

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 70 | المناطق الحرة | — | free zones | — | — |
| 71 | فرع | — | branch | Of a company, a bank, or a foreign company. | — |
| 72 | مكتب تمثيلي | — | representative office | **Cannot invoice. No commercial activity.** Distinct from فرع. | — |
| 73 | رئيس مجلس الإدارة | — | chairman of the board | — | — |
| 74 | الشريك / المساهم | — | partner / shareholder | **Not interchangeable.** | 🔴 |
| 75 | رأس المال | — | capital | Not "head". | — |
| 76 | عقد عمل | — | employment contract | See #77 and #78. | — |
| 77 | عقد عمل غير محدد المدة | — | indefinite-term contract | The default category. | — |
| 78 | عقد عمل محدد المدة | — | fixed-term contract | — | — |
| 79 | السجل التجاري | — | commercial register | ⚠️ **Always cite the issuing office / governorate** — the number alone identifies nothing. | ⚠️ |
| 80 | البطاقة الضريبية | — | the tax card | **Not** "tax certificate" (شهادة ضريبية) and **not** "tax ID". A physical document with a number on it. | ✅ **YES** |
| 81 | رقم التسجيل الضريبي | — | tax registration number | The number that goes **on the invoice**. | — |
| 82 | عوض / بعوض | — | consideration / for value | **بعوض** = for value; **بغير عوض** = gratuitous. Drives stamp duty. | — |
| 83 | كفالة / ضمان | — | guarantee / surety | Also **worker sponsorship** — a third sense. | 🔴 |
| 84 | كفالة بنكية | — | bank guarantee | — | — |

### 10.7 Electronic signature and digital

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 85 | التوقيع الإلكتروني | — | the digital signature | **Person-level**, ITIDA-licensed, token-based. | ⚠️ |
| 86 | الختم الإلكتروني | — | the electronic seal | **Company-level** (legal person). 🔴 **Not** the same instrument as #85. | 🔴 |
| 87 | الفاتورة الإلكترونية | — | the electronic invoice | The ETA-platform instrument carrying the eSeal X.509. | — |
| 88 | الأعمال الإلكترونية | — | electronic transactions | The category name used across Egyptian e-signature / IT law. | — |

### 10.8 Law, sources and the state

| # | Arabic | Everyday (Egyptian) | English | Trap | Flag |
|---|---|---|---|---|---|
| 89 | قانون / لائحة | — | law / executive regulations | ⚠️ A لائحة is **always subordinate** to a قانون. Never call a لائحة a "law". | ⚠️ |
| 90 | الجريدة الرسمية | — | the Official Gazette | ⚠️ **NOT "Egyptian Gazette."** Many English sources use that phrase for a different document. | ⚠️ |
| 91 | الوقائع المصرية | — | the Egyptian Gazette | The gazette's own title — distinct from الجريدة الرسمية (#90). | ⚠️ |
| 92 | مصلحة | — | the authority / the (tax) directorate | **مصلحة** names both a ministry sub-department and a local office. E.g. مصلحة الضرائب. | ⚠️ |

### 10.9 Rendering rules for the genuinely hard cases

These are the seven places where an agent must make a deliberate translation decision rather than a
lookup:

1. **صورة vs. نسخ vs. أصل.** Everyday Egyptian **صورة** = copy. **أصل** = the original — but is also
   used loosely for a copy. Render unambiguously: "الصورة" for a copy, "الأصل" for the original, and
   add "مختوم" (stamped) where the seal is what matters.
2. **إيجار قديم / جديد.** These are **legal regimes**, not adjectives. Write "lease under the former
   (pre-1996) regime" and "lease governed by the Civil Code (Law 4/1996 and following)" — never
   "old lease" / "new lease".
3. **تذكرة vs. إيصال.** Using تذكرة for a payment receipt is a visible non-native error.
4. **شهادة vs. شهادات.** Writing "notary" for a certificate, or "certificate" for a notary, breaks
   the sentence. Always disambiguate.
5. **محضر.** "Bailiff" **only** in court context. In محضر الضبط or a minuted session it means
   "a record".
6. **فك vs. فسخ.** Prospective termination vs. retroactive rescission. **Never merge.**
7. **مأمورية vs. مصلحة.** The local office vs. the authority above it. In tax instructions, users
   mean the مأمورية. Getting this wrong sends someone to the wrong building.

## Where agents most often get Egypt wrong operationally

- **Saying "Egypt has no postal-code system."** It does — Egypt Post operates a national postcode
  standard (5-digit historically; a documented GIS-based 7-digit granular layer). The true and
  useful statement is: *coverage is inconsistent, the code is optional, and routing depends on
  governorate + district.* Never invent a code.
- **Writing "the CBE CIPS."** There is no CIPS in Egypt — CIPS is China's. Egypt's rails are **IPN /
  InstaPay, ACH, RTGS, EFT, CCH, SWIFT, IBAN, Meeza**.
- **Treating the 14th digit of the national ID as offline-validatable.** The check-digit algorithm
  is **not published**. "Luhn mod-10" is folklore. Validate structure only, and label any checksum
  as an unconfirmed heuristic.
- **Reading positions 8–9 of the national ID as the current governorate.** It is the governorate of
  **registration/birth**. Most adults no longer live there.
- **Accepting governorate codes as `01–35`.** They are a **non-contiguous set of 27 + `88`**.
- **Sending users to `ntra.gov.eg`.** It resolves but does not answer. Use **`tra.gov.eg`**.
- **Sending users to `alqalam.idsc.gov.eg` or `ela.gov.eg`.** Neither resolves. The Cabinet's
  legislation portal is **`elpai.idsc.gov.eg`** (the Egyptian Legislation Portal, ELP).
- **Sending users to `gcc.gov.eg` for the Official Gazette.** It returns 200 and is the **Cultural
  Development Fund**. The Gazette is at **alamiria.com** (المطابع الأميرية) and **dspace.id.com.eg**.
- **Conflating Giza's and Alexandria's `gov.eg` ministries.** **`mota.gov.eg` = Trade & Industry
  (industrial licensing)**; **`moiic.gov.eg` = Supply & Internal Trade (the traditional Commercial
  Registry)**. Different bodies, both real.
- **Assuming one Commercial Register.** There are **two tracks** — GAFI (investment law, free zones,
  SCZONE) and the traditional registry. A free-zone counterparty checked against the wrong one is
  not checked.
- **Quoting a commercial-registry number without its issuing office.** Numbering is sequential
  per governorate, so the number alone identifies nothing.
- **Stating a national-ID validity period.** Sources conflict (7 years vs 10 years). Read the expiry
  printed on the card.
- **Hard-coding a passport-number or driving-licence-number regex.** Neither format is published by
  Egypt. Use the MRZ.
- **Assuming the social insurance number equals the national ID.** Widely asserted, **not
  confirmed.** Query it via NOSI using national ID + mother's first name.
- **Assuming a 6–7 digit CR number.** Unverified folklore. Don't validate on length.
- **Saying "the Egyptian weekend is Friday–Saturday."** Government offices work **Sunday–Thursday**.
  Foreign-currency cheque clearing runs **Monday–Thursday only**. Private employers rest
  **Friday or Saturday** (statutorily **one** rest day after at most six working days).
- **Publishing a dated public holiday calendar for a future year.** The Hijri and Coptic dates drift,
  and the **Minister of Labour may substitute a holiday for a working day or vice versa**. Describe
  the rule and point to the source.
- **Missing the deadline rule:** where a time limit's **final day falls on an official holiday, it
  extends to the first working day thereafter** (Law 13/1968, Art. 18) — and the relevant
  "working day" depends on that court's calendar, not the weekday.
- **Serving papers on a public holiday or outside 07:00–20:00.** Barred by Law 13/1968 Art. 15.
- **Repeating the old geographic cheque-clearing table** (Cairo T+1 / Delta T+2 / remote T+3). The
  CCH Regulations Art. 3 settle **all governorates at T+1**.
- **Assuming you can settle a USD or EUR cheque on a Friday.** **No FX session Friday or Saturday**,
  and only **USD and EUR** are covered.
- **Recording the Arabic digit and amount verbatim without a Latin transliteration.** Egyptian
  documents use **Arabic-Indic numerals (٠–٩)** read **left-to-right inside RTL text**. A
  near-identical string in a contract is a transcription error waiting to happen.
- **Writing a cheque with only the numeral line.** Egyptian cheques carry the amount in
  **الأرقام** *and* **بالحروف**, framed **فقط … لا غير**.
- **Reporting a screenshot as proof of payment.** **A screenshot is not a payment record. A bank
  statement is.** Tell users to route material payments through a bank.
- **Assuming a mobile wallet identifies its issuer.** The **same brand runs on several banks**
  (Vodafone Cash with Vodafone *and* ALEXBANK; Orange Cash with NBE; WE Pay with Banque Misr).
  Ask for the **issuing institution**.
- **Quoting a wallet limit from memory.** CBE's page (last updated **23 Mar 2023**) and the operator
  pages **disagree** (CBE: EGP 30k/day, EGP 100k/month individuals; Vodafone Cash: EGP 60k/200k;
  Orange Cash: EGP 60k/200k). Read current operator terms.
- **Telling a foreigner they cannot open an Egyptian bank account.** The **CBE circular of 7 Aug
  2024** states there are **no restrictions** on accounts for non-resident foreign clients, and that
  refusal is itself a risk for the bank.
- **Writing "open a bank account" as a generic step.** Some banks are **salary-only** with a minimum
  monthly salary transfer. Ask what the bank will accept.
- **Assuming the e-signature law is 15/2020.** It is **Law 15 of 2004**; **Ministerial Decision
  361/2020** amended the Executive Regulations. (15/2020 is the Saudi E-Commerce Law — a classic
  cross-jurisdiction confusion.)
- **Sending an e-signed PDF to the الشهر العقاري, a notary, a court or a consulate.** Law 15/2004
  grants **evidentiary equivalence**, not universal process substitution. In person + original ID.
- **Using an electronic seal as if it were a digital signature.** The **electronic seal
  (الختم الإلكتروني) is a company-level** instrument; the **digital signature is person-level**,
  and GOV-CA at the Ministry of Finance is the only issuer for government bodies.
- **Skipping the NAFEZA 48-hour lead time.** ACI has been **mandatory since 1 October 2021**; the
  **ACID** is a hard gate and requires an electronic signature pad.
- **Accepting cash invoices as the default and forgetting the electronic invoice.** From
  **1 July 2023** expenses are accepted in the tax return **only via the electronic invoice**.
- **Missing the individual landlord's tax-notification duty.** Renting out a residential unit or a
  shop triggers **real-estate wealth tax**; failure to notify the مأمورية exposes the owner.
- **Confusing the ETA tax card with VAT registration.** Registration threshold **EGP 500,000**
  (but **importers, exporters and distribution agents register regardless of turnover**), plus
  the **registration certificate (Form 3 VAT)**, which is a separate document.
- **Using a legalisation route from the wrong ministry.** For **commercial-registry extracts**, one of
  the nine Digital-Only services is the **extract for Ministry of Foreign Affairs authentication**
  (طلب مستخرج للاعتماد من وزارة الخارجية) — you get the extract *from* Digital Egypt, then
  authenticate it through **MFA**, then the destination embassy.
- **Skipping stamp duty entirely.** Nominal duty is **EGP 1.50 per sheet** on contracts
  (Law 199/2020), plus proportional rates; and Investment Law 72/2017 gives a **5-year stamp-duty,
  notarisation and publicity-fee exemption** for memoranda of incorporation and credit/pledge
  contracts — **if the conditions are met**.
- **Asking for a "notary" without disambiguating شهادة استخراج (person) from كاتب عدلي (function).**
- **Asking for "the old lease"/"the new lease" in English.** Use the regime.
- **Asking for a "receipt ticket" (تذكرة) instead of an إيصال.**
- **Asking for a "copy" (نسخة) instead of a صورة.**
- **Reading `الدور الأول` as English "first floor."**
- **Assuming an HTTP 200 means the page exists.** GAFI's rebuilt SPA returns **200 on soft-404
  pages**; CBE pages intermittently return a **"Request Rejected"** WAF page to non-browser clients.
  Verify content, not status codes.