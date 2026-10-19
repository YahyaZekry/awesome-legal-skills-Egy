# Egyptian Intellectual Property Law — Verified Reference Corpus
# قانون حماية حقوق الملكية الفكرية — المرجع التشريعي

**Purpose:** a citation-safe reference for an AI agent handling Egyptian intellectual property — for a **non-lawyer in Egypt** (small
business owner, freelancer, independent creator) who wants to **register** and **enforce** IP. Every article number below was read out
of a retrieved primary or official-secondary text. Nothing is asserted from memory.

**As-of date for the whole file: 2026-10-19.**
⚠️ **Each section carries its own `As of:` line — that is the date *that section* was last read against a source.** The sections
re-verified on **2026-10-19** are **§1** (amendment chain, read out of the Court of Cassation consolidated Arabic text), **§2**
(office transfer, read out of EGIPA's own decisions), **§4** (patent/UM terms, out of the WIPO English text extracted locally),
**§6** (copyright terms), **§7** (ITIDA's statutory deposit power, read out of Law 15/2004), **§9** (Economic Courts, out of
Laws 146/2019 and 156/2024 and the Official Gazette scan) and **§10** (fee schedules, read off page scans of the EGIPA decisions
themselves). Everything else stands on its earlier date.

**Relationship to the other files in this corpus.** `01-commercial-corporate-contract.md` **§7** already carries an IP section. That
section was built from a *truncated mirror* of the WIPO English text and it says so; it left the following explicitly open — the
**patent term start date** ("truncated at *as of the*"), the **utility-model term** ("length not verified"), the **trade-secret
article numbers** ("not verified"), whether there is a **distinct software chapter**, the **Art. 167 phonogram term start**, the
**complete amendment list**, and the **full text of Arts. 147 and 414**. **All seven of those gaps are closed in this file.** This
file does **not** restate file 01 §7's treaty table or its Art. 139 national-treatment paragraph; it extends them.
File `05-tenancy-egypt.md` established the "corrections table + per-section As-of + open questions + trap list" shape that this
file follows.

## How to read the confidence markers

| Marker | Meaning |
|---|---|
| ✅ **verified** | I read the article text or the official gazette reference in a retrieved document, and I quote the source URL. |
| ⚠️ **PARTIAL** | The instrument is verified; a specific article number or detail inside it is **not**. Describe the concept, never the number. |
| 🟡 **UNVERIFIED — needs primary-source check** | I could not confirm it. I say what I searched. Do not cite. |
| ❌ **DOES NOT EXIST (as described)** | I searched specifically for it and found it does not exist under that citation or in that form. The premise is wrong. |

---

## ⚠️ CORRECTIONS TABLE — read this before citing anything in this file

Sixteen things a model will get wrong. Four of them were wrong in the brief I was given; one of them was in a **published law-firm
client alert** that I am contradicting.

| # | The common assumption (or the brief's guess) | What the retrieved primary texts actually say |
|---|---|---|
| 1 | "Law 82/2002 has been amended by **Law 131/2003** and **Law 5/2010**." | ❌ **NO SUCH AMENDING LAWS EXIST.** I read the **complete amendment-footnote list at the foot of the Court of Cassation's consolidated Arabic text** of Law 82/2002. The law has been amended **exactly three times**: **Law 26/2015**, **Law 144/2019** and **Law 178/2020**. WIPO Lex's own "Notes" field on the consolidated version lists the *same three and no others*. The "131/2003 and 5/2010" pair is a phantom that file 01 already flagged as unverified; it is now affirmatively contradicted. See §1.3. |
| 2 | "IP law gets amended all the time, so article numbers drift." | ❌ **NOT FOR THE CORE.** **Books One and Two have never been amended since 2002.** Patents, utility models, layout designs, trade secrets, trademarks, trade names, geographical indications and industrial designs all sit on their **2002 numbering and 2002 wording**. Every single amendment has hit **Book Three** (copyright: Law 26/2015, Law 144/2019, Law 178/2020) or **Book Four** (plant varieties: Law 26/2015, Law 144/2019). **A Book One or Book Two article number read in 2002 is still right today.** |
| 3 | "IP is run by the Ministry of Supply, or the Ministry of Culture, or ITIDA." | ⚠️ **OUT OF DATE SINCE 7 AUGUST 2023.** **Law 163/2023** created the **Egyptian Intellectual Property Authority (EGIPA — الجهاز المصري للملكية الفكرية)**, a **public body attached to the Prime Minister**, which *replaces* the six competent ministries and the Patent Office and the Plant Variety Office. The ministers' powers transfer to the **Chairman of the Authority**. Head: **Dr. Hisham Azmy**. See §2. |
| 4 | "Trademarks are registered with the **Trade Registry Department** as Art. 64 says, so you go to the Supply Ministry / ITDA in Nasr City." | ⚠️ **THE STATUTE IS UNCHANGED AND STILL SAYS `إدارة العلامات التجارية` — the *practice* moved.** The Trademark Office has been **relocating to EGIPA's premises at 101 Kasr El Aini St., Cairo** (i.e. the Patent Office building). Reported as in progress from **18 November 2025**, with a warning of processing delays during the move. ⚠️ **Separately: as of 19 October 2026 `itda.gov.eg`'s trademark pages (`/form-tm.aspx`, `/hint-tm.aspx`, `/TM-Details.aspx`) all return HTTP 404** — the forms/guidance the file relied on are gone from that host. **Do not tell a client "go to ITDA in Nasr City" without checking.** See §2.4. |
| 5 | "An IP case worth EGP 5 million goes to the Economic Court's appellate circuit." | ❌ **STALE BY TWO AMENDMENTS.** That was the **2008** figure. **Law 146/2019** raised the first-instance civil ceiling to **EGP 10 million**, then **Law 156/2024** raised it to **EGP 15 million**. The **finality** figure also moved twice: **EGP 500,000** (2019) → **EGP 750,000** (2024). See §9.2. |
| 6 | "IP appears as item **(9)** of the Economic Courts Law Art. 4 list." | ⚠️ **RENUMBERED.** In the **original 2008** text IP was item **9**. **Law 146/2019 replaced Art. 4 wholesale**; in the current text IP is item **(8)** of the **criminal** list (Art. 4) and item **(7)** of the **civil** list (Art. 6). An agent citing "item 9" is citing a repealed version. |
| 7 | "ITIDA gives software businesses a **free-zone / export exemption** from IP or tax." | ❌ **DOES NOT EXIST IN THAT FORM.** I read **Law 82/2002** and **Law 15/2004** (ITIDA's own statute) for anything of the sort. Law 15/2004's Art. 3 objective is merely to *increase opportunities for exporting* ICT services — an aim, not a relief. What actually exists is: **(a) ITIDA's Export-IT programme**, a **cash rebate** of 10–35% of value-added exports capped at **EGP 2.5 million per company**, eligible to ICT companies >50% Egyptian-owned, HQ in Egypt, **annual revenue ≤ EGP 150 million**; and **(b) free-zone / investment-zone relief, which lives in Investment Law 72/2017**, not in any IP law. See §7.3. |
| 8 | "Copyright is automatic, so there is nothing to file." | ⚠️ **TRUE FOR PROTECTION, FALSE FOR DEALING WITH IT.** Protection arises on creation with no formality (ITIDA's own booklet says so). **But Art. 185 as amended by Law 178/2020 provides that a disposal of a work is *not effective against third parties until the recordal is completed*** — «**وفي جميع الأحوال، لا يكون التصرف نافذًا في حق الغير إلا بعد إتمام القيد**». **A publisher or producer who buys your rights and does not record the transfer cannot enforce it against a subsequent purchaser.** This is the single most consequential sentence in Book Three for a freelancer. See §6.6. |
| 9 | "The limitation period for an IP crime is in the **Penal Code**." | ❌ **WRONG INSTRUMENT.** It is **Art. 15 of the Code of Criminal Procedure (Law 150/1950)**: **3 years for misdemeanours**, **10 years for felonies**, **1 year for contraventions**, «**ما لم ينص القانون على خلاف ذلك**». Since **every** penalty in Law 82/2002 is a fine or a short term of imprisonment, every IP offence in the law is a **جنحة (misdemeanour)** ⇒ **3 years**, interrupted by investigation/charge/trial steps under **Art. 17** of the same law. See §9.6. |
| 10 | "A patent lasts 20 years from grant." | ✅ **Verified correction: from the FILING DATE, in Egypt.** **Art. 9**: «**The protection period for a patent shall be 20 years as of the date of filing the application in Egypt.**» This closes file 01's truncated-gap flag. |
| 11 | "A utility model gets 10 years like in the EU / China." | ❌ **EGYPT: SEVEN YEARS, NON-RENEWABLE.** **Art. 30**: «**The protection period of a utility model shall be for a non-renewable period of seven years starting from the filing date of the application for the utility model with the Patent Office in Egypt.**» Closes file 01's "length not verified". |
| 12 | "There is a separate software chapter in the law." | ❌ **NO.** Software is handled **inside Book Three**: computer programs are **Art. 140(2)** protected works and databases are **Art. 140(3)**. The **department** that handles them is separate (the Computer Software and Database Protection Office) but the **chapter** is copyright. Closes file 01's flag. |
| 13 | "Trade secrets are at Commercial Code Arts. 66 and 83." | ⚠️ **THOSE ARE A DIFFERENT REGIME.** Law 82/2002 has its **own** undisclosed-information chapter: **Book One, Chapter Three — Arts. 55–62**, including the **unfair-competition list at Art. 58** and the **criminal penalty at Art. 61 (fine EGP 10,000–50,000)**. The Commercial Code provisions are cumulative, not the primary home. Closes file 01's flag. |
| 14 | "There is no limitation period specific to IP, so nothing to worry about." | ❌ **THREE CLOCKS RUN AT ONCE, and one of them is short.** **(a)** Civil compensation: **Civil Code Art. 374 — 15 years** general rule; **Art. 375 — 5 years** for periodic/self-renewing rights (i.e. **unpaid royalties**). **(b)** Criminal: **3 years** (CPC Art. 15). **(c)** Trademark non-use: **5 consecutive years** and the mark is cancellable by the court on any interested party's request (**Art. 91**). And **prescription is NOT applied by the court of its own motion** — Civil Code **Art. 387** — so the debtor must plead it. See §9.6. |
| 15 | "Renewing a trademark late just costs the late fee." | ⚠️ **THE MARK IS STRUCK OFF.** **Art. 90**: renewal in the last year of the term; a **6-month grace period after expiry** on payment of the fee plus a **supplement not exceeding EGP 500**; **«failing which the Department shall proceed to cancel the said mark from the register»**. Re-registration after cancellation is possible within **3 years** and **only in favour of the former owner** (**Art. 92**, fee ≤ EGP 1,000) — but a **cancelled mark is cancellable, and the 3-year window is a privilege, not a right**. |
| 16 | "There is a **2026 amendment to Law 82/2002** that is now in force." | 🟡 **NOT ENACTED as of 19 October 2026, as far as I can establish.** The bill (see §1.4) was referred by the Speaker to a **joint committee of the Media, Legislative and Education & Scientific Research committees**, and **consultation hearings with publishers began the week of 27 April 2026**. I found **no promulgation, no law number and no gazette reference** for it. **Do not tell a client the penalties changed.** |

---

## Index of instruments

| # | Instrument | Citation | Status | Marker |
|---|---|---|---|---|
| 1 | **IP Code** | Law 82/2002, Books One–Four | in force; **amended 3× (26/2015, 144/2019, 178/2020)** | ✅ |
| 2 | **IP Authority** | Law 163/2023 (EGIPA) | in force from 7 Aug 2023 | ✅ |
| 3 | Executive Regulations, Books I, II, IV | PM Decree 1366/2003 | in force from 17 Aug 2003 | ✅ |
| 4 | Executive Regulations, Book III (copyright) | PM Decree 497/2005 | in force from 30 Mar 2005 | ✅ |
| 5 | **Economic Courts** | Law 120/2008, **as amended by Law 146/2019 and Law 156/2024** | in force | ✅ |
| 6 | Code of Criminal Procedure | Law 150/1950, **Art. 15 (limitation)**, Art. 17 (interruption) | in force | ⚠️ |
| 7 | Civil Code — limitation | Law 131/1948, **Arts. 374, 375, 387** | in force | ✅ |
| 8 | Customs Law + ER | Law 207/2020 + PM Decree 430/2021 | in force | ✅ |
| 9 | E-signature / ITIDA | Law 15/2004, **Art. 4(ط)** | in force from 23 Apr 2004 | ✅ |
| 10 | Patent agents | Law 23/1951 (still live — EGIPA fees under it) | in force | ✅ |
| 11 | ITIPA (information-technology crimes) | Law 175/2018 | in force | ⚠️ |
| 12 | Investment Law (free zones / SEZ) | Law 72/2017 | in force | ✅ |
| — | Madrid Protocol, Nice Agreement, PCT, Paris, Berne, UPOV, TRIPS | see file 01 §7 treaty table | in force | ✅ |

---

# 1. The governing statute — Law 82/2002

**Citation:** **قانون رقم 82 لسنة 2002 بإصدار قانون حماية حقوق الملكية الفكرية** (Law No. 82 of 2002 issuing the Law on the Protection of
Intellectual Property Rights).
**Promulgated / published:** 2 June 2002. **Entry into force:** **3 June 2002**.
**Sources (primary):**
- ✅ **Court of Cassation Information Centre consolidated Arabic text** (بوابة تشريعات محكمة النقض) — downloaded as PDF, text extracted locally with `pdftotext -layout` and NFKC-normalised. **This is the working source for the whole of §1.** It carries the amendment-footnote list at the foot of the file.
- ✅ **WIPO Lex English**, 2002 version: https://www.wipo.int/wipolex/en/text/191565. ⚠️ **WIPO's own caveat on this file: "Current text in English unavailable. 2002 version provided for reference purposes."** Every English quotation in this file that touches an amended article is therefore taken from the **Arabic**, not from WIPO.
- ✅ WIPO Lex Arabic consolidated, "amended up to 5 September 2020": https://www.wipo.int/wipolex/ar/legislation/details/22066
**As of:** 2026-10-19.

## 1.1 Structure — four Books

✅ **Book One** — Patents and Utility Models, Layout Designs for Integrated Circuits, and Undisclosed Information.
✅ **Book Two** — Marks, Trade Names, Geographical Indications and Industrial Designs.
✅ **Book Three** — Copyright and Related Rights.
✅ **Book Four** — Plant Varieties.

Both WIPO Lex's Notes field and the Arabic consolidated text agree on this division.

## 1.2 Commencement — the delayed bit that catches people out

✅ **Art. 4 of the promulgating law:** the Law is published in the Official Gazette and comes into force **the day after publication**
(i.e. 3 June 2002), **EXCEPT** the provisions on patents for **food-related chemical products, pharmaceutical chemical products,
micro-organisms, and products not previously subject to protection**, which came into force on **1 January 2005** — without prejudice
to Art. 44 (Part I) and Art. 45 (Part II) of Book One. *(Restated from file 01 §7, re-read here and confirmed.)*

## 1.3 The amendment chain — ✅ complete, and it is only three laws

**This is the authoritative list.** It is read from the amendment footnotes on the Court of Cassation consolidated text, and it is
**independently corroborated** by the "Notes" field of WIPO Lex's consolidated entry, which names the same three amending laws and
the same articles.

| Amending law | Official Gazette | What it did |
|---|---|---|
| **Law 26 of 2015** | OG No. 25 bis (B), **22 June 2015** | Substituted **Arts. 189, 191, 192, 193, 194, 195, 196, 198, 199, 201, 202**; **inserted** Arts. 189 bis, 192 bis, 192 bis(1), 194 bis, 202 bis, 202 bis(1); **repealed Art. 200**. **All of this is Book Four (plant varieties).** |
| **Law 144 of 2019** | OG No. 31 bis (D), **6 August 2019** | Substituted parts of **Arts. 192, 192 bis, 193, 194, 195, 198, 201, 202, 202 bis(1)**. **Book Four again** — the UPOV-1991 alignment that made Egypt a full UPOV member. |
| **Law 178 of 2020** | OG No. 36 bis, **5 September 2020** | Substituted **Art. 185** only. **Book Three (copyright)** — the register-of-disposals article. |

**Conclusions that follow, and that an agent should be able to state flatly:**

- ✅ **Books One and Two have NEVER been amended.** Not once, not by any law, since 2002. Every patent, utility model, layout-design, trade-secret, trademark, trade-name, GI and industrial-design article number and wording in this file is the **original 2002 text**.
- ✅ **Book Three has been amended ONCE** (Art. 185, by Law 178/2020). Everything else in copyright is 2002 text.
- ✅ **Book Four is the live area** — three of the three amending laws touched it.
- ❌ **There is no Law 131/2003 and no Law 5/2010** amending Law 82/2002. They are phantoms.

⚠️ **A small internal conflict to record.** Law 178/2020's Art. 2 provides: «**ينشر هذا القانون في الجريدة الرسمية، ويعمل به بعد مرور شهر من اليوم التالي لتاريخ نشره**» — published **5 September 2020**, so it took effect **after one month**, i.e. **6 October 2020**. **WIPO Lex's metadata, however, records Law 178/2020 as "in force from 05/09/2020".** The gazette text is the statute; WIPO's metadata is the summary. **Cite the statute: 6 October 2020.**

## 1.4 The 2026 draft amendment — 🟡 NOT ENACTED

A private member's bill to amend Law 82/2002 was introduced by **MP Aya Abdel Rahman (آية عبد الرحمن)** with **60 members** (more than
one tenth of the House, which is the threshold for a private member's bill to be admissible without government sponsorship). The
Speaker, **Counselor Hisham Badawi**, referred it to a **joint committee of the Media and Culture Committee, the Constitutional and
Legislative Affairs Committee, and the Education and Scientific Research Committee**.
**What it would do** (as reported): raise the penalty for piracy/counterfeiting of books and literary works to **imprisonment of not
less than 6 months and not more than 1 year plus a fine of up to EGP 1,000,000**, and on **repetition** to **1–3 years** with the
same fine. Press coverage of the MP's own statements describes the fine proposal inconsistently — **both "up to EGP 1 million"**
(elbalad.news, 22 Apr 2026) **and "ten-fold the fine"** (الشرق الأوسط / shorouknews, 27 Apr 2026) appear. ⚠️ **Record both; prefer
neither.**
**Status as of 19 October 2026:** committee stage, with **consultation hearings with publishers, authors, universities and the head of
EGIPA** underway from late April 2026. **No law number, no gazette reference, no promulgation was located.** Treat the current
penalties in §6.7 and §9.5 as the operative ones.

**Sources:** https://www.elbalad.news/6944398 (22 Apr 2026) · https://www.shorouknews.com/news/view.aspx?cdate=27042026&id=c6a211cc-63c3-4e2a-932e-d704d7fd804f (27 Apr 2026) · https://www.tahiamasr.com/1084674.
⚠️ **A separate, unrelated trap in the same search space:** the Egyptian Parliament's own page
`https://www.parliament.gov.eg/News_Show.aspx?frm=3645` is headed *"مجلس النواب يوافق على مشروع قانون بتعديل بعض أحكام قانون حماية
الملكية الفكرية"* — **but it is dated 10 July 2019** and it is about the **UPOV/plant-varieties** amendment (Law 144/2019), not the
2026 bill. An agent searching for "IP law amendment parliament" will land on it and conclude wrongly.

---

# 2. Who actually administers this — the authorities

**Source:** ✅ **Law 163/2023** (Arabic, full text, downloaded and extracted locally) — **قانون رقم 163 لسنة 2023 بإصدار قانون إنشاء
الجهاز المصري للملكية الفكرية**. **Official Gazette No. 31 bis (B), 6 August 2023. In force 7 August 2023.**
✅ WIPO Lex entry confirming the same dates: https://www.wipo.int/wipolex/ar/legislation/details/22398
**As of:** 2026-10-19.

## 2.1 The Egyptian Intellectual Property Authority (EGIPA)

✅ **Promulgating Art. 2 of Law 163/2023:** the **Authority replaces** the competent ministries — higher education & scientific
research, **supply & internal trade**, **culture**, **communications & IT**, agriculture, and trade & industry — together with the
**Academy of Scientific Research and Technology**, the **Internal Trade Development Authority (ITDA)**, the **Supreme Council for
Media Regulation**, the **Patent Office** and the **Plant Variety Protection Office**; and **the Chairman of the Authority replaces
those ministers** in the laws and decrees referred to.
✅ **Annexed law Art. 2:** EGIPA is a **public entity attached to the Prime Minister**, with **headquarters in Cairo**.
✅ **Art. 3:** **transition period of a maximum of one year**, extendable **once** by six months.
✅ **Art. 4 — competencies**, as reported verbatim by the State Information Service's parliamentary desk
(https://www.tahiamasr.com/1084674, 13 Oct 2026): including **(2) registration, recordal and deposit of IP rights and the grant of
protection documents**; **(7) establishing registers of patent agents and trademark agents and other IP agents**; **(8) a register of
technical experts in IP asset valuation**; and **(10) examining complaints submitted to the Authority**.
✅ **Art. 4 also makes EGIPA a `جهة خبرة` — an expert body for the courts and police.**
✅ **Art. 5:** the board includes the **ITIDA CEO**, a **Customs Authority** representative, and an **Egyptian Drug Authority**
representative. *(Restated from earlier work in this session; the board-composition point is confirmed by the ITIDA and Customs
membership appearing in EGIPA's own decisions.)*
✅ **Art. 9(9):** the Chairman issues the rules for **judicial seizure officers (رجال الضبطية القضائية)**.
✅ **Head of the Authority: Dr. Hisham Azmy (أ.د. هشام عزمي)**, appointed August 2024, **appears as the signatory on every EGIPA
decision in §10**.
✅ **Board formed by PM Decree No. 4370 of 2024** — cited as the enabling instrument in EGIPA Decisions **139, 140 and 141 of 2025**.
✅ **PM Decision No. 492 of 2025** transferred the individual IP offices (see §2.2).

## 2.2 Where each office sits after the transfer

✅ **PM Decision No. 492 of 2025** distributed the offices as follows — this is the current map and it is not what the 2003 Executive
Regulations say:

| Function | Office | Where it now sits |
|---|---|---|
| Patents & utility models | **Egyptian Patent Office** — 101 Kasr El-Aini St., Cairo, P.O. Box 11516 | EGIPA |
| **Trademarks & industrial designs** | Trademark & Industrial Design Office — **4 El Nasr Rd, Makram Ebeid intersection, Nasr City** | **Relocating to EGIPA, 101 Kasr El Aini St.** |
| Plant varieties | Plant Variety Protection Office | EGIPA (ex-Ministry of Agriculture) |
| **Computer programs & databases** | Computer Software and Database Protection Office | **EGIPA (ex-ITIDA)** |
| Broadcasting & audio-visual works | | EGIPA (ex-Supreme Council for Media Regulation) |
| Copyright (general) | four offices incl. the **register-of-disposals** office | EGIPA (ex-Ministry of Culture) |
| Contact point | | Ministry of Investment and Foreign Trade |

📌 **A caution the agent must carry:** this table is built from **PM Decision 492/2025** and from **PM Decree 492's** reporting. The
**PCT Applicant's Guide** (WIPO), which is generally the most current third-party source, still names the receiving office as the
**"Egyptian Intellectual Property Authority"** at **101 Kasr El Aini St.**, with `patinfo@egypo.gov.eg` for PCT matters and
`egypa-info@egypo.gov.eg` generally. **Use those two addresses and that street address.**

## 2.3 Addresses, telephones and e-mail — as published

| | Detail | Marker |
|---|---|---|
| **EGIPA / Patent Office** | 101 Kasr Al Ainy St., Cairo; P.O. Box 11516 | ✅ |
| Telephone | (202) **279-21291 / 279-21274 / 279-21273** | ✅ |
| E-mail | **patinfo@egypo.gov.eg** (PCT and general) · **egypa-info@egypo.gov.eg** | ✅ |
| Website | **http://www.egypo.gov.eg** — publishes the current fee decisions (§10) | ✅ |
| **Trademark Office (pre-move)** | **4 El Nasr Road, Makram Ebeid intersection, Nasr City, Cairo** · tel (202) **22 715 040** → +20 2 22715040 | ⚠️ |
| **Trademark Office (post-move)** | **101 Kasr El Aini St., Cairo** | ⚠️ |
| **Government complaints line** | **16528** (shakwa.eg unified complaints), linked from EGPO's own site | ✅ |

## 2.4 ⚠️ The trademark-office status is genuinely unsettled — do not guess

Three different facts point the same way, but none of them is a final official notice:

1. ✅ **EGIPA publishes patent, plant-variety and copyright fee schedules on `egypo.gov.eg`. It publishes NO trademark fee schedule.** The absence is conspicuous, not accidental — trademark fees are the only core IP fees still not centrally published.
2. ⚠️ **`itda.gov.eg`'s trademark pages now 404.** I fetched `/form-tm.aspx`, `/hint-tm.aspx` and `/TM-Details.aspx?TM=1|2` on **19 October 2026**: all four returned `HTTP 404 / "The resource cannot be found."`. The site's current content is **commercial registry, land, investment and post offices** — no trademark section at all. The same pages are still **cached in search indexes**, which is exactly how a model gets this wrong.
3. ⚠️ **The relocation was announced as in progress on 18 November 2025** (Mondaq / Adams): *"The Egyptian Trademark Office has begun preparations for its planned relocation to the premises of the Egyptian General Intellectual Property Authority… The new address for the Egyptian Trademark Office is 101 Kasr El Aini Street, Cairo, Egypt."* The same alert warns of **document-migration delays**.
   Source: https://www.mondaq.com/trademark/1706028/trademark-office-relocating-its-premises

✅ **What survives regardless of the address:** Egypt's trademark database has been in **TMview** since **13 December 2021**, with more
than **131,500** Egyptian marks added at launch. **A free pre-filing search can be run without visiting any office.**
📌 **Practical instruction to give a client: telephone before travelling.** 🟡 The pre-move address in ITDA's own guidance page
(I still see the archived text: *"تم إنشاء إدارة العلامات التجارية عام 1940… إدارة مركزية… لاثبات أسبقية العلامة بالرقم المسلسل"*)
should be treated as superseded.

---

# 3. Trademarks (Book Two, Chapter One)

**Sources:** ✅ WIPO Lex English text of Law 82/2002, extracted locally (article text quoted below); ✅ PM Decree 1366/2003 Executive
Regulations Books One/Two/Four (English, extracted locally) for procedure; ✅ EGIPA Decisions 64 & 65 of 2026 (from firm alerts, §10).
**As of:** 2026-10-19 for the fee decision; **2026-10-12** for the statutory articles.

## 3.1 What can be a trademark

✅ **Art. 63** (quoted in full because the last sentence is the one everyone misses):
> «A trademark is any sign distinguishing goods, whether products or services, and include in particular names represented in a
> distinctive manner, signatures, words, letters, numerals, designs, symbols, signposts, stamps, seals, drawings, engravings, a
> combination of distinctly formed colours and any other combination of these elements if used, or meant to be used, to distinguish
> the products of a particular industry, agricultural, forest or mining venture or any goods, or to indicate the origin of products or
> goods, or their quality, category, guarantee, preparation process, or to indicate the provision of any service.
> **In all cases, a trademark shall be a sign that is recognizable by sight.**»

❌ **Consequence:** **sound marks, smell marks, taste marks and texture marks cannot be registered in Egypt.** The Court of Cassation
consolidated Arabic text reads «**يجب أن تكون العلامة التجارية مما يدرك بالبصر**» — *must be perceptible by sight*. Corroborated
independently by a specialist firm's country guide checked on 2026-10-06:
*"Only visually perceptible signs are protected, so sound and smell marks cannot be registered."*

## 3.2 Who may own one, and the "who is the owner" rule

✅ **Art. 66** — without prejudice to international conventions in force in Egypt, **any natural or legal person, Egyptian or foreign,
belonging to or having its centre of effective activity in a WTO member, or applying reciprocity to Egypt**, may apply to register at
the **Department of Trade Registry**. **So a foreigner can register directly. A non-WTO national needs reciprocity.** ⚠️ Note the
separate, tighter point in Art. 66's second paragraph about MFN-style advantages.
✅ **Art. 65 — the five-year ownership presumption, which is the whole ballgame in a dispute:**
> «The person who has registered a trademark and who has made use of it for a period of **five years** as of the date of its
> registration shall be deemed the owner of such a trademark, **unless precedence of use by a third party is proven.**
> A **prior user** of the mark may, **within the said period of five years**, challenge the validity of its registration.
> The registration of a mark may, however, be challenged **at any time, where the registration is made in bad faith.**»

📌 **Plain-English version for a business owner:** *register it, use it for five years, and it is effectively yours. Until the fifth
anniversary, someone who can prove they used the mark first can take it off you. If you registered it knowing someone else was using
it, they can take it off you whenever they like — there is no five-year shelter.*

## 3.3 What cannot be registered

✅ **Art. 67 — the list, read in full (8 heads):**
(1) marks **devoid of any distinctive character**, or composed of signs/statements which only **usage** grants to the products, or which
are the **normal picture or image** thereof; (2) marks **contrary to public order or morality**; (3) **public armorial bearings, flags
and other emblems of the State or any other state, regional or international organisations**, and imitations; (4) marks **identical
with or similar to symbols of a religious character**; (5) the **Red Cross / Red Crescent** and equivalent emblems and imitations;
(6) **the portrait of an individual or his armorial bearings, except with his consent**; (7) **designations of honorary degrees** the
applicant cannot prove a right to; (8) **marks and geographical indications likely to mislead or confuse the public, or containing
false descriptions as to origin** of goods or services, or **signs containing an indication of a fictitious, imitated or forged trade
name**.
📌 **For a small business: heads (1) and (4) are the ones that actually bite.** A purely descriptive word ("Fresh", "Cairo Shoes")
is refused under (1). **A cross, a crescent, a star of David, or a stylised Quranic motif will be refused under (4)** — and this is
routinely attempted and routinely refused.

## 3.4 Well-known marks — protection WITHOUT registration

✅ **Art. 68** — the owner of a **well-known trademark, worldwide and in Egypt**, enjoys the Law's protection **even if the mark is not
registered in Egypt**. The Department must **ex officio reject** an application identical to a well-known mark for identical products
unless the well-known owner filed it; and this extends to **non-identical** products where **the well-known mark is registered in a
WTO member country AND in Egypt** and use would suggest a connection and prejudice the owner.
📌 **Two limits to be honest about: (a) "well-known" is a fact question, judged by reputation, not by a certificate; (b) the
anti-dilution limb for non-similar goods has a double registration precondition.** An agent must not tell a client that fame alone
protects them across all 45 classes.

## 3.5 Collective and certification marks

✅ **Art. 69 (collective marks)** and ✅ **Art. 70 (certification marks)** are provided for — a **collective mark** is owned by a group
and used by its members; a **certification mark** certifies quality/origin. The Executive Regulations' fee schedule charges **EGP 100**
for the application and **EGP 100** for the registration of a certification mark (2003 figures). ⚠️ **Detailed rules of use for
collective/certification marks are in the Executive Regulations and were not read article-by-article here.**

## 3.6 Registration procedure — the steps, correctly ordered

| Step | Rule | Sources |
|---|---|---|
| **1. Application filed with the Department** | **Art. 73** — filed with the **Trade Registry Department** in the manner and form laid down in the Regulations. | ✅ Law |
| **1a. What you must supply** | ER **Art. 71** — the application form plus a **power of attorney**. ER **Art. 72** — **four copies of the mark image**. | ✅ ER 1366/2003 |
| **1b. The six-month document trap** | ER **Art. 73** — **the supporting documents must be filed within 6 months** of filing, **or the application is deemed never to have existed (`يعتبر الطلب كأن لم يكن`)**. | ✅ ER |
| **2. Fees** | **Art. 73**: «The Regulations shall prescribe the fees due for the application and all procedures related to the mark. **Such fees shall not exceed a total of 5,000 pounds.**» ⚠️ Today the *practical* fee is the 2003 ER figure **plus** **EGP 500** per service under EGIPA Decisions 64 & 65 of 2026 (§10.4). | ✅ Law / ✅ ER / ⚠️ decision |
| **3. Classification** | **Art. 74** — registered for **one or more categories** of goods produced or intended to be produced, **per the Regulations**. Use is **limited to the registered categories**. **Egypt applies the Nice Classification** — ⚠️ the *statute* does not name Nice; the **Nice Agreement** binds Egypt (instrument **18 March 2005**, **in force 18 June 2005**, per WIPO Lex), and TMview carries an **Arabic-language Nice search** launched with ITDA/EUIPO. **Nice terminology in Egyptian practice is safe to use, but cite Nice as a treaty obligation, not as an Art. 74 command.** | ✅ / ⚠️ |
| **3a. Multi-class in one application** | ✅ ER **Art. 71** allows **one application to designate one or more classes**, with **one registration certificate per application** (reported by JCIPO's guide, checked 2026-10-06, reading ER Art. 71). | ✅ ER (via specialist summary) |
| **4. Priority** | **Art. 75** — a **6-month** priority right from the first filing in a **WTO member / reciprocal** country, for the same mark and the same products. | ✅ Law |
| **5. Simultaneous applications** | **Art. 76** governs competing applications. | ✅ Law |
| **6. Examination; refusal; appeal** | **Arts. 77–79** — examination by the Department; refusal decisions are **appealable to the appeal committee** (three members, at least one from the **Council of State**). ✅ JCIPO's read: **amendments required by the examiner must be made within 6 months**; **refusal or amendment decisions may be appealed to the Grievance Committee within 30 days**. | ✅ / ⚠️ |
| **7. Publication** | **Art. 80** — the **acceptance** decision is published in the **Gazette of Trademarks and Industrial Designs**, as prescribed by the Regulations. ✅ ER **Art. 82**: the Authority issues the Gazette **monthly, in the first week of each month**. | ✅ Law + ✅ ER |
| **8. Opposition — 60 days** | **Art. 80**: «**Any interested party may submit, in writing to the Department, within 60 days from the date of publication** … a motivated opposition.» The Department then sends a copy to the applicant **within 30 days**. ✅ ER **Art. 89**: 60 days. ✅ ER **Art. 90**: the **applicant must reply within 30 days** of receiving the opposition **or the application is deemed abandoned**. ✅ ER **Art. 92**: **90 days** to complete registration after a **rejected** opposition. | ✅ |
| **9. Registration** | **Art. 83** — **the registration takes effect from the FILING date**, not the registration date. | ✅ Law |
| **10. Certificate** | Issued after the opposition window closes unobstructed. | ✅ |

⚠️ **Sequence honesty note.** Steps 6–8 above come from the **2003 Executive Regulations**. They have not been re-made, so they are the
operative procedure; but EGIPA has been **transferring offices and processes since 2023** and individual steps may be executed in a
different order or online. **State the statutory windows (6 months / 60 days / 30 days / 90 days) with confidence; state the office
choreography with the 2003 date attached.**

## 3.7 Duration and renewal

✅ **Art. 90:**
> «The period of protection conferred by the registration of the mark is **10 years**, renewable for an **identical period or periods
> upon request of its owner and every time within the last year of the protection period**, against payment of the fees due for the
> initial registration application.
> The owner of the mark may request the renewal of the protection period **within six months after the date of its expiry** against
> payment of the prescribed fees and **a supplement prescribed by the Regulations not exceeding 500 pounds**, failing which **the
> Department shall proceed to cancel the said mark from the register**.»

📌 **Two things a business owner must diarise: (a) renewal is due *during the last year*, not after; (b) there is a six-month
rescue window, after which the mark is gone.** ✅ **ER (2003 schedule) items on renewal:** *request for renewal of a mark* — **EGP 50**
per class, **plus EGP 200** if within the three-month period following expiry, **plus EGP 300** if in the next three months.
⚠️ Those are the **2003** figures; **add the EGP 500 EGIPA surcharge per service** (§10.4) and **verify the base figure with the
office**, because **EGIPA has published no trademark fee schedule**.

## 3.8 Losing a mark for non-use — Art. 91, and the trap inside Art. 74

✅ **Art. 91:**
> «The competent court may, **upon request by any interested party**, issue an **enforceable decision to cancel the registration** if it
> appears to the court that the mark **has not been seriously used for a period of five consecutive years**.»

✅ **Art. 74, last paragraph:** «**Provisions of Article 91 shall apply to the categories for which the mark has not been seriously
used.**» ⇒ **Cancellation is CLASS-BY-CLASS.** A mark registered in classes 25, 35 and 43 but only used in 25 can lose 35 and 43 while
keeping 25.

📌 **The point most often missed:** **Art. 91 says "seriously used" (استعمال جدي), not "used at all".** Token use — a single
promotional posting, an internal document — does not answer a five-year non-use claim. **Keep dated, evidencing use: invoices,
packaging, advertising, shelf photographs.**

## 3.9 Re-registration after cancellation

✅ **Art. 92** — a cancelled mark may be **re-registered in favour of its owner exclusively, within three years** of cancellation, on
the same conditions and procedure, **against a fee prescribed by the Regulations not exceeding EGP 1,000**.
📌 **Note the direction of the rule: it is a privilege for the previous owner, NOT a bar on others.** It is *not* an Egyptian version
of a US-style "intent-to-resume". 🟡 **Whether it bars third parties during the three years is not stated in the article; treat as
unclear.**

## 3.10 The Madrid Protocol — Egypt's practical position

✅ **Treaty status (WIPO Lex):** Madrid **Agreement** (Marks) — **1 July 1952**. Madrid **Protocol** — signed **28 June 1989**,
ratified **3 June 2009**, **in force 3 September 2009**.
✅ **Two operational consequences, both from a specialist guide checked 2026-10-06:** **(a) Egypt has made no 18-month declaration,
so the provisional-refusal period for an international registration designating Egypt is 12 months; (b) no individual fee is
charged** — Egypt has not notified an Art. 8(7) individual fee.
📌 **What this means for a small business owner in Egypt:** *Madrid is a **route out**, not a route in. If you want protection in
other countries you must first have a home application or registration in Egypt, and then you can designate other members through
WIPO. If a foreign company wants Egypt, it can designate Egypt through Madrid and pay no individual fee.*

## 3.11 Trade names — the under-used neighbour of trademarks

✅ **Book Two Chapter Two covers trade names (الأسماء التجارية)** and ✅ **Arts. 101–102 cover trade indications (البيانات التجارية)**.
Law 82/2002 **repealed Law 57/1939** on trademarks by its promulgating Art. 2.
⚠️ **Article-level detail of the trade-name chapter was not read here. What is safe to say:** a trade name is protected under Law
82/2002 as a distinct right from a trademark, and **EGIPA's Decisions 64 & 65 of 2026 impose the same EGP 500 surcharge on
"trade names" services as on trademarks** — which is itself evidence that trade-name filings are still live and chargeable.
**As of:** 2026-10-12 (statute) / 2026-10-19 (fee decision).

---

# 4. Patents, utility models and layout designs (Book One)

**Sources:** ✅ WIPO Lex English text of Law 82/2002, extracted locally and quoted below; ✅ PM Decree 1366/2003 Executive Regulations;
✅ WIPO **PCT Applicant's Guide — Egypt**, "valid from 1 September 2026", for the PCT national-phase rules and current PCT fee figures.
**As of:** 2026-10-19.

## 4.1 Patentability

✅ **Art. 1:**
> «A patent shall be granted … to any **industrially applicable invention, which is new, involves an inventive step**, whether connected
> with **new industrial products, new industrial processes, or a new application of known industrial processes**.»
> «The patent is **also granted, independently**, for any **modification, improvement or addition to a previously patented invention**,
> which meets the criteria of being new, inventive and industrially applicable…; in which case the patent shall be granted … to the owner
> of the modification, improvement or addition.»

📌 **Three cumulative requirements: novelty, inventive step, industrial applicability.** The second paragraph is the **Egyptian
"improvement patent"** — a real second patent on top of someone else's existing patent, not a licence.

✅ **Art. 3** defines **novelty** (restated from file 01: novelty is destroyed by disclosure, subject to the stated exceptions).
✅ **Arts. 7–8** govern **employee inventions** — the employee's right to the invention and the employer's rights where the invention
arises from the employment.
📌 **For a freelancer/employee, this is the article to check before signing anything.** ⚠️ **The precise allocation of ownership and
the compensation entitlement in Arts. 7–8 were not read here; §12 lists this as an open item.**

## 4.2 What CANNOT be patented — Art. 2, the complete five heads

✅ **Art. 2:**
> «Patents shall not be granted for:
> **(1)** Inventions whose exploitation is likely to be **contrary to public order or morality, or prejudicial to the environment,
> human, animal or plant life and health**.
> **(2) Discoveries, scientific theories, mathematical methods, programs and schemes.**
> **(3) Diagnostic, therapeutic and surgical methods for humans and animals.**
> **(4) Plants and animals, regardless of their rarity or peculiarity, and essentially biological processes for the production of
> plants or animals, other than micro-organisms, non-biological and microbiological processes for the production of plants or animals.**
> **(5) Organs, tissues, live cells, natural biological substances, nuclear acid and genome.**»

📌 **Three consequences a business owner will actually hit:**
- **A business method, an app's idea, an algorithm, a mathematical model or a "program" as such cannot be patented** — head **(2)**. *The idea inside a program can be patented if it is a technical process; the program as such cannot.*
- **A surgical or diagnostic method cannot be patented** — head **(3)**. **A medical device can**; a method of treating a patient cannot.
- **A plant variety cannot be patented** — head **(4)**. **That is why Book Four exists**: plants go to the **plant-variety** system, not the patent system. (Egypt's UPOV instrument: **1 November 2019, in force 1 December 2019**, per WIPO Lex.)

## 4.3 Filing and examination

| Step | Rule | Marker |
|---|---|---|
| Filing | **Arts. 12–15** — application, contents and documents, filed with the Patent Office. | ✅ |
| Examination | **Art. 16** — substantive examination, then **publication in the Patent Gazette**, then a **60-day opposition** window. | ✅ |
| Security / defence opposition | **Art. 17** — a **90-day** route for security- or defence-related subject matter. | ✅ |
| Grant | **Art. 19** — the **grant is published after one year**; the application **remains confidential until then**. | ✅ |
| Priority | **Art. 38** — **Paris Convention priority, 1 year**. | ✅ |
| Employee inventions | **Arts. 7–8**. | ⚠️ see §12 |
| Progressive annual fees | **Art. 11** — **annual fees run from the second year** and are progressive. **Art. 31** does the same for utility models. | ✅ |
| Lapse | **Art. 26** — lapse for non-payment, including a **7% overdue surcharge**. | ✅ |

📌 **"Confidential for a year" is a genuinely important protection for a small inventor:** the file is not published immediately, so
you keep a twelve-month window before the world sees the specification.

## 4.4 Terms — the numbers file 01 was missing

| Right | Term | Starts | Renewal | Marker |
|---|---|---|---|---|
| **Patent** | **20 years** | **date of filing the application IN EGYPT** | none | ✅ **Art. 9** |
| **Utility model** | **7 years** | **filing date with the Patent Office in Egypt** | **NON-RENEWABLE** | ✅ **Art. 30** |
| **Layout design of an integrated circuit** | **10 years** | filing in Egypt, **or 10 years from first commercial exploitation** in Egypt or abroad, **whichever is earlier**; rights **cease 15 years from creation** | — | ✅ **Arts. 45–48** |

✅ **Art. 30 verbatim:**
> «The protection period of a utility model shall be for a **non-renewable period of seven years** starting from the filing date of the
> application for the utility model with the Patent Office in Egypt.»

✅ **Art. 31:** a filing fee is payable, and **a progressive annual fee starting from the second year until expiry**; the Regulations fix
the amounts, **not exceeding EGP 1,000 for each application**, with conditions for reduction and waiver.
📌 **The reduction matter.** ✅ **PCT Applicant's Guide (Egypt):** the national filing fee is **EGP 150** for a patent and **EGP 100** for a
utility model, **0 for students**; and the **individual/establishment reductions** from the 2003 Regulations (students 0/10%; individuals
or establishments with **≤10 staff at 50%**) are carried into EGIPA's practice. **Always ask about the reduction — it is not automatic.**

## 4.5 What a patent actually gives you — and the exhaustion rule

✅ **Art. 10:**
> «A patent shall confer on its owner the right to **prevent a third party from exploiting the invention by any means**.»
> «The right of a patent owner to prevent a third party from **importing, using, selling or distributing** a product **shall lapse when he
> commercialises the product in any country or authorises a third party to do so**.»
> «The following shall **not** be considered as infringements of that right when carried out by third parties: [enumerated]»

📌 **This is a NATIONAL-EXHAUSTION clause, and it is unusually wide — the trigger is commercialisation "in ANY country", not merely in
Egypt.** *If you sell your patented product anywhere in the world, you cannot then stop its import into Egypt.* An agent advising an
exporter must raise this.

## 4.6 Non-voluntary licences, expropriation, lapse

✅ **Arts. 23–24 — non-voluntary ("compulsory") licences**, with **eight grounds**, including:
- **failure to exploit** the invention — the clock is **4 years from the date of the application OR 3 years from the grant, whichever is later**; and
- **abuse of the patent owner's rights / practices that restrict fair competition**;
- **dependent patents** (where a later patent cannot be worked without the earlier one);
- **semiconductors** — non-voluntary licences **only for public non-commercial use** (the TRIPS Art. 31(c) carve-out).
✅ **Art. 25 — expropriation** of a patent by the State.
✅ **Art. 26 — lapse**, including the **7% overdue surcharge**.

📌 **The honest framing for a client:** *you own your patent, but it is not absolute. If you do not work it in Egypt, someone else can be
licensed to.*

## 4.7 PCT national phase — Egypt's actual rules

✅ **Source: WIPO PCT Applicant's Guide — Egypt, "valid from 1 September 2026"** (the most recent official statement I could read).

| Item | Egypt's rule | Marker |
|---|---|---|
| **National-phase deadline** | **30 months** from the priority date — **PCT Arts. 22(1) and 39(1)(a)** | ✅ |
| **Language** | **Arabic** (translation required) | ✅ |
| **National filing fee** | **EGP 150** (patent); **EGP 100** (utility model); **0 for students** | ✅ |
| **Annual fees** | from the **2nd year EGP 20**, **3rd year EGP 40**, rising; with student and individual reductions | ✅ |
| **Reinstatement of rights** | **"due care"** standard (not "unintentional") | ✅ |
| Reinstatement fee | **EGP 800** individuals/research institutes · **EGP 1,000** companies **<10** employees · **EGP 1,500** companies **>10** employees | ✅ |
| Restoration of priority right | also the **"due care"** standard | ✅ |
| **RO transmittal fee** | **USD 142** | ✅ |
| **ISA is EG (the Egyptian office itself)** | fee **EGP 4,000 / CHF 64 / EUR 70 / USD 80**, with a **25% reduction** for certain income-group applicants | ✅ |
| **IPEA** (preliminary examination) | **EGP 3,000** | ✅ |

📌 **The "due care" point is worth flagging to a client:** Egypt is **not** one of the easy "unintentional delay" states. Reinstating a
missed PCT deadline requires showing you exercised **due care**, which is a substantive evidentiary burden.

## 4.8 Treaty position for patents (verified, WIPO Lex)

✅ **Paris Convention** — acceded **5 March 1951**, **in force 1 July 1951**.
✅ **PCT** — ratified **6 June 2003**, **in force 6 September 2003**.
✅ **Strasbourg Agreement (IPC)** — **17 October 1975**.
✅ **Washington Treaty on Intellectual Property in Respect of Integrated Circuits** — signed **5 December 1989**, instrument **26 July
1990**, but **never in force**. ⚠️ *This is the correct answer if a client asks whether Egypt is bound by the Washington Treaty: no,
because the treaty never entered into force for anyone.*

---

# 5. Industrial designs (Book Two, Chapter Four)

**Sources:** ✅ WIPO Lex English Law 82/2002; ✅ PM Decree 1366/2003 ER (English, local extraction).
**As of:** 2026-10-12.

| Item | Rule | Marker |
|---|---|---|
| **Definition** | **Art. 119** — an industrial design is an **ornamental / aesthetic aspect** of a product. | ✅ |
| **Novelty requirement** | **Art. 120** — the design must be **new**. | ✅ |
| **Registration office** | **Art. 122** — the **Trade Registry Department** keeps a **special register of industrial designs**. | ✅ |
| **Multiple designs in one application** | **Art. 122** — **up to 50 designs** in one application, **provided all such designs form one coherent unit**. | ✅ |
| **Fee cap** | **Art. 122** — the Regulations prescribe the fees for filing, renewal "and all relevant procedures", **the total not exceeding EGP 3,000**. | ✅ |
| **Conflict of interest** | **Art. 123** — **staff of the Trade Registry Department may not file industrial-design applications**. | ✅ |
| **What cannot be registered** | **Art. 124** — the non-registrable list. | ✅ (article located; ⚠️ heads not read verbatim here) |
| **Opposition** | Via the ER; the 2003 schedule charges **EGP 75** for *objecting registration of an industrial design*. | ✅ ER |
| **TERM** | **Art. 126** — **10 years from the date of filing the registration application in Egypt**, **extendable for a further 5 years** on application **within the last year** of the term. **A further 3-month post-expiry grace applies**, failing which the Department **automatically revokes** the registration. | ✅ |
| **Renewal fee** | ⚠️ **Art. 126 states no cap and the ER figure is not quoted here. Confirm with the office.** | 🟡 |
| **Criminal penalty** | **Art. 134** — fine **EGP 4,000–10,000**; on **repetition**, imprisonment **≥1 month** plus fine **EGP 8,000–20,000**. | ✅ |
| **Conservatory measures** | **Art. 135** — the seizure/attachment route for designs. | ✅ |

📌 **Practical note:** the design term is **10 + 5 = 15 years maximum**, and **the renewal decision has to be taken in the tenth year**.
A design that is not renewed is not merely unenforceable — it is **automatically revoked**.

---

# 6. Copyright and related rights (Book Three)

**Sources:** ✅ WIPO Lex English Law 82/2002 extracted locally; ✅ **PM Decree 497/2005** Executive Regulations for Book Three
(English, Official Gazette No. 12 bis, **29 March 2005**; issued at Cabinet **18 Safar 1426 / 28 March 2005**; **in force from the day
after publication, i.e. 30 March 2005**); ✅ **Law 178/2020** Arabic gazette text.
**As of:** 2026-10-19.

## 6.1 Automatic protection — and the crucial caveat

✅ **Protection arises on creation. There is no registration requirement and no formality.** ITIDA's own booklet for startups says it
in terms: *"وتتمتع المصنفات بالحماية دون الحاجة لاتخاذ إجراءات الإيداع والتسجيل… فالمصنف يكون مشمول بالحماية بمجرد الانتهاء منه، إلا
أنه تكمن أهمية الإيداع للمصنفات في كونها وسيلة قانونية هامة في الاثبات"* — **deposit is an evidential tool, not a condition of the
right.**
Source: ✅ **ITIDA, "الملكية الفكرية للشركات الناشئة" (IPR Booklet for Startups)**,
`https://itida.gov.eg/English/Publications/Documents/IPR-Booklet.pdf`.

⚠️ **BUT the corollary is the opposite of what most people assume** — see §6.6 (Art. 185). **You do not need to file to OWN copyright.
You DO need to file to make a SALE of copyright bite against third parties.**

## 6.2 What is protected — Art. 140, and the two heads that matter most here

✅ **Art. 140** lists protected works. The two entries that carry this file:
- ✅ **Art. 140(2) — computer programs (برامج الحاسب الآلي)**
- ✅ **Art. 140(3) — databases (قواعد البيانات)**

📌 **This is the answer to file 01's open question: there is no separate software chapter. Software and databases are Book Three
copyright works.**

✅ **Art. 141** — **no protection for ideas or mere data, and none for official documents.**
✅ **Art. 142** — **national folklore is in the public domain**; the **ministry exercises the rights** in it, and the **Ministry of
Culture** is charged with folklore under ✅ **ER Art. 3**.
✅ **Art. 138** — definitions. **Art. 138(2) defines "Creation"**. **Art. 138(18)/(19)** define the **competent minister / ministry** as:
**Minister of Culture** generally; **Minister of Information** for broadcasting; **Minister of Communication and Information** for
**computer programs and databases**. ✅ **ER Art. 1(c),(d)** repeats exactly this split.

## 6.3 Moral rights — perpetual, and impossible to sign away

✅ **Art. 143** — the author and successors enjoy **permanent moral rights** which are **not liable to prescription or assignment
(لا تسقط بالتقادم ولا تنتقل)**: **(1) the right to first make the work available to the public; (2) the right to claim authorship;
(3) the right to object to any amendment the author deems a distortion or mutilation** (with the stated translation carve-out).
✅ **Art. 144** — the author **alone** may apply to the **Court of First Instance**, **on serious reasons**, for a ruling preventing
circulation, withdrawing the work from circulation, or ordering substantial amendment, **notwithstanding disposal of the financial
exploitation rights** — **but must offer fair compensation in advance** to the holder of the financial rights, **and if it is not paid
within the court's period the ruling is void.**
✅ **Art. 145** — **any disposal of a moral right under Arts. 143 and 144 is ABSOLUTELY NULL AND VOID.**
✅ **Art. 146** — where the financial-rights term has expired and there is no heir or testamentary beneficiary, **the competent
ministry exercises the moral rights under Arts. 143 and 144**. ✅ **ER Art. 2** repeats this and adds that the ministry takes all
procedures needed to protect the work and the author's reputation.

📌 **Talking point for a freelancer:** *no contract, however long, however much money is on it, can make you give up your moral rights,
and no clause saying you do is worth anything.* **But moral rights do not stop you from being paid badly** — that is the economic
rights, which you can and will assign (§6.5).

## 6.4 Economic rights

✅ **Art. 147** — the author and successors have the **exclusive right to grant licences or to prevent any exploitation of the work, in
any manner**, including exploitation over **the internet and communication networks**. *(Restated from file 01 §7, where the source
excerpt was truncated; the article number and the internet limb are confirmed.)*
✅ **Art. 148** — **the translation right into Arabic lapses after 3 years** (the Arabic-translation lapse rule).
✅ **Arts. 149–153** — assignment. ✅ **Assignment must be in writing.** ✅ **Art. 153** — a purported assignment of **future
production** is **void (`باطل`)**.
📌 **Art. 153 is the freelancer's best friend and is routinely breached.** *A contract that says "all works you create during the term,
including works not yet conceived, are assigned to us" is attacking Art. 153. Future-production blanket assignments are void.*

## 6.5 Terms — the complete table, with file 01's gaps closed

| Work / right | Term | Marker |
|---|---|---|
| **Author, natural person** | **Life of the author + 50 years** from death — **Art. 160** | ✅ closed (was truncated in file 01) |
| **Joint works** | Life of the authors + **50 years from the death of the LAST surviving author** — **Art. 161** | ✅ |
| **Collective works** (except applied art) | **50 years from publication or first making available, whichever is later**, where the right holder is a legal person; if a natural person, Arts. 160–161 apply. Works **first published after the author's death**: **50 years from first publication or first making available, whichever is later** — **Art. 162** | ✅ |
| **Anonymous / pseudonymous** | **50 years from first publication or first making available, whichever is later**; if the author is identified and well known **or has disclosed their identity**, Art. 160 applies — **Art. 163** | ✅ |
| **Applied art** | **25 years** from first publication or making available, whichever is later — **Art. 164** | ✅ |
| **Computation / parts** | The **later** of first publication or first making available; repetition does not restart the clock **unless the author made substantial modifications rendering the work novel**; **for works published in separately published parts or volumes, EACH PART is treated as independent** — **Art. 165** | ✅ |
| **Performers** | **50 years from the date of the performance or registration**, as the case requires — **Art. 166**. Moral rights are covered by ✅ **Art. 155**; economic rights by ✅ **Art. 156** | ✅ |
| **Producers of phonograms** | **50 years — Art. 167** | ⚠️ **the term length is confirmed; the *start point* is the item file 01 flagged as truncated and I have not resolved it verbatim. See §12.** |
| **Broadcasting organisations** | **20 years** — **Art. 168**, with rights defined at ✅ **Art. 158** | ✅ |

## 6.6 Art. 185 — the register of disposals, the 2020 amendment, and the one sentence that matters

✅ **Art. 185 as substituted by Law 178/2020** (Arabic gazette text, Official Gazette No. 36 bis, **5 September 2020**; ⚠️ WIPO Lex
metadata says "in force 05/09/2020" but the statute's own Art. 2 says it takes effect **one month after the day following publication**
⇒ **6 October 2020**):
> «**مادة 185** — تُنشئ الوزارة المختصة **سجلاً لقيـد التـصرفات** الواردة على المصنفات والأداءات والتسجيلات الصوتية والبرامج الإذاعية
> الخاضعة لأحكام هذا القانون.
> وتحدد اللائحة التنفيذية لهذا القانون نظام القيد فى السجل **مقابل رسم لا يجاوز ألف جنيه للقيد الواحد**.
> **ويُعفى من الرسم** المشار إليه فى هذه المادة طالب القيد **الذى تقل سنه عن واحد وعشرين عامًا**، وكذلك الذين يسرى فى شأنهم **قانون
> حقوق الأشخاص ذوى الإعاقة** الصادر بالقانون رقم **10 لسنة 2018**.
> **وفى جميع الأحوال، لا يكون التصرف نافذًا فى حق الغير إلا بعد إتمام القيد**.»

📌 **Translated operationally: (1) there is a register for disposals of works, performances, sound recordings and broadcasts;
(2) the recordal fee is capped at EGP 1,000 per entry; (3) applicants UNDER 21 and persons covered by the disability-rights law are
EXEMPT from the fee; (4) IN ALL CASES a disposal is NOT EFFECTIVE AS AGAINST THIRD PARTIES until the recordal is complete.**

⚠️ **SOURCE CONFLICT — record both.** The bill text as reproduced in a news report of **18 August 2020**
(`rosaelyoussef.com/758100`) shows a **EGP 100 fee** for applicants under 21, whereas the **enacted and consolidated text** (both the
gazette scan and the Court of Cassation consolidated text) says **`يُعفى` — exempt** — and contains **no EGP 100 limb at all**.
**The enacted text governs: exemption, not a reduced fee.** The EGP 100 version was a drafting stage that did not survive.
✅ **ER Art. 14** (2005 text) sets the **recordal** procedure and confirms the per-entry cap at **L.E. 1,000**; ✅ **ER Art. 11** requires
the ministry to establish the registry; ✅ **Arts. 12–13** fix the application contents (applicant details; work name, data and filing
number; kind of action and the parties — plus **the instrument of the act or a certified copy**); ✅ **ER Art. 15** specifies the
register page contents.
⚠️ **The ER figures are the 2005 ones (L.E. 100 per entry for Cultural-Office entries; L.E. 200/300/500 for software entries) and are
superseded for what EGIPA now charges — see §10.3.**

## 6.7 Legal deposit, deposit certificates, and establishments

✅ **Art. 184** — **legal deposit**: up to **10 copies**; **failure to deposit does NOT affect the rights**; fine **EGP 1,000–3,000 per
work**.
📌 **The two halves of this article are the point: depositing is mandatory, but not depositing does not weaken your copyright.**
✅ **Art. 186** — a **deposit certificate** may be obtained from the competent ministry on payment of a fee capped by the Regulations
at **L.E. 1,000 per certificate** (✅ ER **Art. 16**).
✅ **Art. 187** — **establishments that put works into circulation** (by sale, lease, lending or licensing) **need a licence and must keep
registers**; fine **EGP 1,000–5,000**; on **repetition EGP 10,000–20,000**. ✅ **ER Art. 17** implements the licence and the 2005 schedule
charges **L.E. 250** for a one-activity one-year licence and **L.E. 1,000** for multi-activity.
✅ **Art. 188** — **law-enforcement officers** are designated.
✅ **Art. 182** — disputes may go to **arbitration under Law 27/1994**. ✅ **Art. 183** — licences for the **commercial or professional use
of works in the public domain**. ✅ **Art. 170** — **compulsory translation/reproduction licence for teaching**.
✅ **Arts. 171–172 — the exceptions.** ✅ **Art. 171(3)** allows **a single archival/replacement copy of a computer program by its lawful
holder**, and adaptation within the licensed purpose, with destruction of the copy when the holder's title ends. There are **six numbered
exceptions** in Art. 171 (private/family performance; single personal copy; archival software copy; analytical studies and quotations for
criticism/discussion/media; copies for judicial or administrative proceedings; short extracts for teaching) — **read out in full from the
gazette text published 9 October 2026.** ✅ **ER Art. 10** additionally permits **adaptation of computer software for non-commercial,
educational or training purposes after publication**, provided it does not harm the author's legal interests and **references the
source software**.

## 6.8 Deposit and registration — where you actually go

📌 **This is the practical answer to "how do I register my copyright in Egypt":**

| Work | Deposit with | Marker |
|---|---|---|
| **Books and printed works** | **دار الكتب والوثائق القومية — the National Library & Archives of Egypt** | ✅ ITIDA booklet |
| **Computer programs and databases** | **the IPR office at ITIDA** — ☑ «**مكتب الملكية الفكرية بهيئة تنمية صناعة تكنولوجيا المعلومات**» | ✅ ITIDA booklet |
| **Disposals (Art. 185 register)** | the competent ministry's **register-of-disposals office** — four copyright offices at the Ministry of Culture, now under EGIPA per PM Decision 492/2025 | ✅ |
| **Deposit certificates (Art. 186)** | the competent ministry / office | ✅ |

⚠️ **Format caution.** ITIDA's booklet is written for startups and says, in the same breath, that deposit is *not* necessary for
protection. **Both statements are true.** The deposit is an **evidential and administrative** act. **The register of disposals under
Art. 185 is a different thing entirely and IS legally operative against third parties.**

## 6.9 Copyright criminal penalties — Art. 181

✅ **Art. 181** — **imprisonment of not less than one month AND a fine of EGP 5,000–10,000, or either of those two penalties**, for the
**seven enumerated heads**, which include **dissemination over the internet** and **manufacturing/selling circumvention devices**.
✅ On **repetition**: **imprisonment ≥3 months plus a fine of EGP 10,000–50,000.**
✅ **Confiscation** is provided for; and **closure of the establishment for up to 6 months**.
📌 **Note the structure: "imprisonment ≥1 month AND fine EGP 5,000–10,000, OR EITHER of the two."** That "or either" is not a
formality — **a court can impose only a fine.** ⚠️ **This is the exact article the 2026 draft amendment proposes to raise** (§1.4).
**As of:** 2026-10-19.

---

# 7. Software, databases and ITIDA

**Sources:** ✅ Law 15/2004 (WIPO Lex English + Arabic text extracted locally); ✅ PM Decree 497/2005 ER Book Three; ✅ ITIDA's own IPR
booklet; ✅ ITIDA's Export-IT programme page; ✅ GAFI's investment-incentives pages; ✅ Law 82/2002 Art. 140(2),(3).
**As of:** 2026-10-19.

## 7.1 The statutory basis — Law 15/2004 Art. 4(ط)

✅ **Law 15/2004** — **قانون رقم 15 لسنة 2004 بتنظيم التوقيع الإلكتروني وبإنشاء هيئة تنمية صناعة تكنولوجيا المعلومات.**
**Official Gazette No. 17 bis (d), 22 April 2004. In force 23 April 2004.**
✅ **Art. 2** — establishes **ITIDA (هيئة تنمية صناعة تكنولوجيا المعلومات)** as a **public authority with public corporate personality**,
**affiliated to the Minister with policy jurisdiction**, **headquarters in Giza Governorate**, may establish branches nationwide.
✅ **Art. 3** — objectives, including **(c) increasing opportunities for exporting communications and information technology services and
the products thereof**.
✅ **Art. 4(ط)** — verbatim:
> «**إيداع وقيد وتسجيل النسخ الأصلية لبرامج الحاسب الآلي وقواعد البيانات، التي تتقدم بها الجهات أو الأفراد الناشرون والطابعون
> والمنتجون لها للمحافظة على حقوق الملكية الفكرية وغيرها من الحقوق**»

**In English (WIPO Lex):** *"Depositing, recording, and registration of **original software and databases** submitted by entities or
individuals publishing, printing, and producing thereof in order to protect copyrights and other rights."*

📌 **This is the statutory charter for everything Egypt does with software copyright.** It is a **deposit/recordal** power — **not** a
registration-that-creates-the-right power. **The right exists under Law 82/2002; ITIDA's office is where you put the copy on record.**

## 7.2 Where a software author goes — and the office transfer

✅ **PM Decree 497/2005, ER Art. 1(e)** names **three "Offices"**: the **Copyright Protection Office at the Ministry of Culture**; the
**Computer Software and Database Protection Office at ITIDA**; and the **Broadcasting, Audio, Visual and Audio-Visual Works Protection
Office at the Ministry of Information**.
⚠️ **PM Decision 492 of 2025 moved the computer-programs-and-databases office from ITIDA to EGIPA.** So as of 2026: **the statute (Law
15/2004) still vests the power in ITIDA; the office that exercises it has been transferred to EGIPA.** ✅ **ITIDA's CEO sits on EGIPA's
board (Law 163/2023 Art. 5)**, which is how the two are stitched together.
📌 **Practical instruction:** *for a software deposit, the safe route is to approach EGIPA (which now holds the office) and, if
redirected, ITIDA. Do not assume ITIDA alone.*

✅ **ER Art. 1(h) — definition of computer software:** *"Any form of instructions and orders expressed by a particular language, symbol or
sign that could be used directly or indirectly in a computer to perform a function or achieve a result — whether in their original form
or any other computer-related form."*
✅ **ER Art. 1(i) — definition of a database:** *"Any storage of data **featured by innovation in terms of arrangement and display** or
**reflecting a personal effort worth protection**, whether the storage is made through a language, symbol or any other form, provided
that **it is stored by the computer and is retrievable by the computer** or any other e-means."*
📌 **Read ER Art. 1(i) carefully.** *A bare list of facts is not a protected database. The protection attaches to the **arrangement and
display**, or to the **personal effort**. A database compiled mechanically, with no creative arrangement and no personal effort, is
arguably not protected — which is deliberately consistent with the international "sweat of the brow" debate.*

## 7.3 ❌ The "ITIDA free-zone / export exemption" does not exist in that form

I was asked to verify this item. **I could not find it, because it is not there.**

❌ **Law 15/2004** contains **no** tax exemption, no free-zone provision and no export relief. Its Art. 3 objective is to *increase
opportunities for exporting* ICT services — **an aim, not a benefit**. **Book Three of Law 82/2002** likewise contains no export or
free-zone relief; its fee article (Art. 185) creates a **fee**, and its only reliefs are the **under-21 and disability-law exemptions**.

✅ **What actually exists — two separate things, neither of them an IP exemption:**

**(a) ITIDA's Export-IT programme — a cash rebate, not a tax exemption.**
Source: `https://itida.gov.eg/English/Programs/Export-IT/pages/default.aspx`
- **What it is:** direct cash support on **proceeds from value-added exports** collected in a given calendar year. Launched 2010; **15 rounds**; **370+ companies** supported.
- **Eligibility:** ICT companies with **>50% Egyptian ownership**, **headquartered in Egypt**, exporting **ICT services, embedded software, or IT-enabled services** (the last subject to committee approval).
- **Hard ceiling:** companies with **total annual revenue above EGP 150 million are not eligible**.
- **Support value:** **10–35%** of value-added exports depending on size (**Micro ≤ EGP 2m**, **Small >2–20m**, **Medium >20–150m**); plus, **for micro and small companies only**, **+10%** for operating outside Cairo/Giza/Alexandria and **+5%** for export growth. **Support ceiling on payment: EGP 2.5 million per company.**
- **What it is NOT:** *not* a tax exemption, *not* an exemption from IP fees, and *not* automatic. It is a **disbursed cash grant on exports already made**, awarded in annual rounds, on an application, subject to committee approval.

**(b) Free-zone and Special Economic Zone relief — real, but it lives in Investment Law 72/2017, not in any IP law.**
Source: **GAFI's own incentives pages** — `https://gafi.gov.eg/en/contenttemplate/b06c70a1-ffcb-4dc6-a651-4146a06f30e0` ("Investment Facilitations and Incentives") and
`https://gafi.gov.eg/en/contenttemplate/8287b6a6-9599-4516-aa71-2bf3ec876497` ("General, Special and Additional Incentives"), read **2026-10-19**.
⚠️ **This is the investment authority's summary, not the statute text — I did not read Law 72/2017's own articles for this file.** Do not quote an article number.

- **Free zones (public and private), under Law 72/2017:** *projects located in the zones and their profits are exempt from the applicable taxes and fees in Egypt*; **exported or imported goods are exempt from customs duties and VAT**; tools, machinery and necessary means of transport are exempt from customs duties and VAT; goods move in and out without ordinary import/export rules and customs procedures.
- **Special Economic Zones (e.g. the Suez Canal Economic Zone):** a **50% deduction of investment costs for 7 years** from the date the activity actually commences; **0% VAT** on goods and services exported abroad *and* on goods/services supplied by the local market to the zone; customs-duty exemption on equipment, machinery, raw materials and spare parts imported to manufacture export products; the project is not subject to import/export regulation and is not entered on the importers'/exporters' registers.

📌 **Read this correctly.** These are **advantages of an investment regime attached to a zone and to an approved project.** **None of them is an IP benefit, and none of them exempts a software author from anything in Law 82/2002.** A company in a free zone still registers its trademark, still pays the IP fees in §10, and still needs the Art. 185 recordal for a disposal to bind third parties.

**The business point, stated plainly:** if you want tax relief as an Egyptian software exporter, **your route is Investment Law 72/2017 or an export-incentive programme — not the IP law.** Anyone telling you "ITIDA gives software companies an IP/export exemption" is conflating **the Export-IT cash rebate** with **the free-zone regime**. Neither is in Law 82/2002, and neither is in Law 15/2004.

**As of: 2026-10-19** (Law 15/2004 Art. 3–4 read in the Arabic Official Gazette text; Export-IT and GAFI pages read the same day).

---

# 8. Trade secrets, unfair competition and geographical indications

**Where these live.** **Undisclosed information (trade secrets)** is **Book One, Chapter Three — Arts. 55–62**, i.e. inside the *patents* Book, at the end. **Trade indications and geographical indications** are **Book Two, Chapter Two — Arts. 100–112**. Both are read verbatim out of the WIPO English text, and both Books have **never been amended** (see §1.3), so the article numbers are stable.

## 8.1 Trade secrets — Arts. 55–62

✅ **Art. 55 — the three-part test.** Information is protected only when **all three** are met:
1. it is **confidential** — *"not, as a body or in the precise configuration or assembly of its components, generally known or common among those involved in the industrial art within the scope of which the information falls"*;
2. it **"has commercial value because it is confidential"**;
3. it **"depends on the effective measures taken by the person lawfully in control of it, to keep it confidential."**

📌 **Head (3) is the one that kills claims.** A secret you did not lock up, did not restrict, did not mark and did not put under NDA **is not a secret in law** — and Art. 57 then makes that your own fault, not the defendant's.

✅ **Art. 56 — test data for pharmaceuticals and agrochemicals.** Where undisclosed information *"involved a considerable effort"* was submitted on request to the competent authorities for marketing approval of a pharmaceutical or agrochemical product using **new chemical components** necessary for the tests, the authorities must protect it against **disclosure and unfair commercial use** *"from the date of its submission … until it is no longer confidential, or for a period not exceeding five years, whichever comes first."* Disclosure where necessary to protect the public is **not** an infringement.

✅ **Art. 57 — the owner must police his own secret.** The person lawfully in control **"shall take all appropriate measures to preserve the confidentiality"**, limit circulation inside the establishment to authorised persons, and *"shall not be exempt from liability when others infringe the information, unless he proves that he has exerted reasonable and adequate efforts to preserve such information."* The confidentiality — and the rights to stop others — **subsist only while the information remains undisclosed under Art. 55**. And the right is a narrow one: it is limited to preventing acts *"contrary to fair commercial practices, as stipulated in Article 58"*, with the courts open where a third party is proven to have done such an act.

✅ **Art. 58 — the unfair-competition list (six heads):**
| # | The act |
|---|---|
| 1 | **Bribery** to acquire the information from employees of the establishment that owns it |
| 2 | **Incitement of employees** to disclose information acquired by virtue of their employment |
| 3 | **Disclosure by a party to a "confidential information contract"** of information so acquired |
| 4 | Acquisition **from the place where it is preserved, through illicit means** — *"such as theft, espionage or the like"* |
| 5 | Acquisition **through fraudulent means** |
| 6 | **Use** of information acquired by any of the above, **by a third party aware** that it is confidential and that it was so acquired |

The **consequences** of those acts — a third party disclosing, acquiring or using the information without the owner's authorisation — are the infringement.

✅ **Art. 59 — what is NOT an infringement (four heads):**
| # | The lawful route |
|---|---|
| 1 | Acquisition from **available public sources** — *"libraries, including patent office libraries, public government records and published research, studies and reports"* |
| 2 | **Independent effort** — *"examination, testing and analysis of products in circulation which incorporate the undisclosed information"* (**this is lawful reverse engineering**) |
| 3 | Acquisition resulting from **independent scientific research, innovation, invention, development, modification and improvement** |
| 4 | Acquisition and use of **known and available information circulating among those involved in the art** |

📌 **This is the whole reason a trade secret is sometimes better than a patent — and the whole risk.** Reverse engineering a product you lawfully bought **is expressly lawful**. So a trade secret only protects you against *dirty* acquisition (theft, spying, bribery, breach of confidence), **never against cleverness**. If your product reveals the secret when it is put on the market, **you have no remedy** — whereas a granted patent stops copying however the copier learned the invention.

✅ **Art. 60 — trade secrets are assignable**, with or without compensation, by the person lawfully in control **or his successor**. There is **no recordal/publicity requirement** for the assignment (unlike copyright disposals — see §6.6). Put it in writing anyway.

✅ **Art. 61 — the criminal penalty.** *"Without prejudice to any more severe punishment stipulated under any other law"*: a fine of **not less than EGP 10,000 and not more than EGP 50,000** for anyone who **uses an illegal means to disclose** protected information, or **acquires or uses** it *"while aware of its confidentiality and that it was acquired by such illegal means"*. **Repetition**: **imprisonment for a period of not more than two years** + a fine of **EGP 50,000–100,000**. See §9.5.

✅ **Art. 62 — the enforcement articles carried into this chapter.** *"The provisions of Articles 4, 33, 35 and 42 shall apply to this Chapter."* That means a trade-secret owner gets **Art. 4** standing/national treatment, **Art. 33 conservatory measures** (and the **8-day** rule — see §9.4), **Art. 35 destruction** and security for fines/damages, and **Art. 42** judicial officers.

⚠️ **What the chapter does not have.** There is **no article that obliges the court to award damages** for a trade-secret breach; the compensation claim runs on the **general Civil Code** rules (§9.6). And **the chapter does not make an NDA binding in itself** — an NDA is a contract, enforced as a contract, with the criminal route of Art. 61 available only if the acquisition/disclosure falls in the Art. 58 list.

## 8.2 Trade indications and geographical indications — Arts. 100–112

✅ **Art. 100 — "trade indication"** means any clarification connected directly or indirectly with: **(1)** number, quantity, dimension, measure, capacity or weight; **(2)** place or country of manufacture/production; **(3)** method of manufacture/production; **(4)** elements and components; **(5)** name or capacity of the producer or manufacturer; **(6)** patents or any other industrial property rights, or commercial/industrial concessions, awards or distinctions; **(7)** the name or form under which certain goods are usually known.

✅ **Art. 101 — trade indications "shall be factual in all aspects"**, whether placed on the products, packaging, invoices, correspondence, advertisements or other means of offering the products to the public, *"or whether on signboards, inside the shops or in warehouses."*

✅ **Art. 102 — medals, diplomas, awards and honorary distinctions** may be mentioned **only** in relation to the products for which they apply or the persons/commercial names that acquired them (or their successors), and the mention must include **correct indications of the date, the nature of the award, the authority and the occasion**. A joint exhibitor **may not** use for his own products the distinctions granted jointly to the exhibited products unless he clearly indicates the source and nature of the distinction.

✅ **Art. 103 — the competent minister may prohibit the sale, marketing or importation** of products where **quantity, dimension, measure, capacity, weight, origin or ingredients** is a factor in assessing value, unless the product bears those indications; and the minister determines **how they are placed on the product in Arabic**.

✅ **Art. 104 — geographical indications, the core rule.** Where a geographical origin *"has become descriptive of the quality, reputation or other characteristics of a certain product so as to be largely instrumental in its marketing"*, the indication is used to indicate the **place of origin in a district or part of a country that is a member of the World Trade Organisation or a country according Egypt reciprocity**. **"The protection in the country of origin is required to protect such indications."** (This tracks TRIPS Arts. 22–24.)

✅ **Art. 105** — a person **residing in** a place especially reputed for producing a product **may not** affix that place's geographical indications on **the products of his trade** in a way that leads the public to believe the products were produced there. *(Yes — this bites on locals, not only on outsiders.)*
✅ **Art. 106** — **no means may be used** to designate or present products so as to lead the public to believe they come from a geographical area **other than the real place of origin**.
✅ **Art. 107** — a producer in a place especially reputed for a product may not affix that place's indication on **similar products he produces elsewhere** so as to suggest they were produced in the reputed place.
✅ **Art. 108 — the generic carve-out.** Where a geographical name *"has become descriptive, to indicate in a commercial sense the nature of any products and not their geographical place of origin"*, the name **may be used** with such products.
✅ **Art. 109** — a **trade mark including a geographical indication may only be registered if the applicant continuously produces the products in the reputed geographical area.**
✅ **Art. 110** — a **trade mark including a geographical indication may not be registered** where the indication is likely to **mislead the public as to the real origin** of the goods.
✅ **Art. 111** — a mark including a GI **may be registered if the right was acquired in good faith before this Law entered into force, or before the geographical indication was protected in the country of origin.**
✅ **Art. 112 — the civil action for a GI.** *"Any interested party may institute normal proceedings before the competent court of first instance to order prohibiting the use of any geographical indication not included in a registered trademark, where such use is likely to mislead the public as to the real origin of the products."* **Jurisdiction lies where the indication is used.**

⚠️ **What Egypt does not have here: a sui generis GI register.** Law 82/2002 creates **no register of geographical indications** and no GI-holder right separate from the ordinary courts' power to stop misleading use (Art. 112) and the trade-mark rules (Arts. 109–111). If a client's question assumes "we will register our GI", the correct answer is that **the law does not provide that**. Recorded in §11.

**As of: 2026-10-19** (Arts. 55–62 and 100–112 read verbatim in the WIPO English text of Law 82/2002 extracted locally; Book One and Book Two have never been amended — §1.3).

---

# 9. Enforcement — courts, customs, remedies and the clocks

## 9.1 The two doors

There are **two doors**, and most small businesses only ever use the first badly.

1. **The courts** — and specifically the **Economic Courts** (Law 120/2008, §9.2), which hold both the **criminal** and the **civil** IP jurisdiction. Conservatory measures (seizure, description, discontinuance) are available **pre-trial, on petition**, in every Book of Law 82/2002 (§9.4).
2. **The administration** — **customs** (Law 207/2020 + ER 430/2021, §9.3), and the **police/prosecution** route (§9.7), and the **EGIPA** registration side from §2.

## 9.2 The Economic Courts — the numbers that keep changing

**Chain of instruments.** **Law 120/2008** (in force **1 October 2008**) → amended by **Law 146/2019** (Official Gazette **31 bis (D)**, **6 August 2019**; **in force 1 October 2019**) → amended by **Law 156/2024** (Official Gazette **27 bis (d)**, **10 July 2024**; **in force the day following publication**).

| | **2008 original** | **as amended by Law 146/2019** | **as amended by Law 156/2024 (current)** |
|---|---|---|---|
| IP in the **criminal** list, **Art. 4** | item **(9)** | replaced wholesale — IP is item **(8)** | item **(8)** |
| IP in the **civil** list, **Art. 6** | item **(9)** | item **(7)** | item **(7)** |
| First-instance civil ceiling | **EGP 5 million** | **EGP 10 million** | **EGP 15 million** |
| Judgment **final** at or below | **EGP 500,000** | **EGP 750,000** | **EGP 750,000** |
| Felony circuits | — | — | **new economic felony circuits**, first-degree and appellate |

⚠️ **Any figure below EGP 15 million quoted to you is stale, and "item 9" is a repealed text.** See corrections table rows 5 and 6.

✅ **Art. 10 — appeal.** Appeal from the economic court's judgment is by **appeal (استئناف) within 40 days**. *(Verified in the 2008 text as amended; the article was not touched by 156/2024 in the parts I read.)*

✅ **Art. 8 bis(و) — added by Law 146/2019: compulsory pre-litigation settlement before the هيئة التحضير والوساطة (Preparation and Mediation Body)**, for a fee between **EGP 2,000 and EGP 200,000**, with the **crucial sentence**: **«ويوقف تقادم الدعاوى الخاصة بتلك المنازعات أثناء مباشرة تلك الإجراءات»** — **prescription of those disputes is suspended while those procedures are being conducted.** ⚠️ **If a client is close to a limitation deadline and the parties go to mediation, the clock stops** — for an IP claim that is usually a benefit, but it can also extend the period in which the *other* side can sue **your** client. Diarise it.

✅ **Art. 8 bis(أ)** — the judge may fine a party **EGP 200–500** for failing to produce documents on request.

## 9.3 Customs — the only enforcement route a small business can trigger in a week

Source: the **Egyptian Customs Authority's own IPR booklet** (April 2026) read on `customs.gov.eg`, which states its legal basis as **Customs Law No. 207 of 2020** plus its **Executive Regulations, PM Decree No. 430 of 2021**.

| Step | What it says |
|---|---|
| **The unit** | The Authority's **IP Rights Protection Department** receives, examines and decides complaints **"in coordination with the competent authority"** (ER Art. 2) |
| **Who may complain** | The **right owner, usufructuary, exploiter**, or their agents — covering **copyright, neighbouring rights, trademarks, geographical indications, industrial designs, patents and integrated-circuit designs** (ER Arts. 3–5) |
| **Scope** | Goods **not yet released** and goods **en route to Egyptian ports** |
| **What you file** | A complaint containing the listed data and documents — proof of the right, description of the goods, the consignment details |
| **💰 The cost of a suspension** | A **cash security or bank letter of guarantee equal to one quarter (1/4) of the consignment value** must be deposited |
| **How long the suspension lasts** | **Not more than 10 working days**, within which the complainant **must take judicial measures** or the suspension falls away (ER Art. 8) |
| **The importer's counter-move** | The importer may **object to the Head of the Customs Authority within 3 working days**, and the objection **does not release the consignment until it is decided** (ER Art. 9) |
| **Ex officio** | Customs **may suspend on its own initiative** on prima facie evidence (the TRIPS Art. 58 pattern) |
| **A separate import ban** | **Import Regulations No. 770 of 2005, Art. 40** prohibits importing/exporting products bearing trademarks **without the owner's or agent's approval** |

🟡 **The Department's e-mail address** appeared in the booklet's extract as `ipr@customs.gov.eg`, but the extraction rendered the Arabic-embedded address **reversed**. **Verify by telephone before relying on it.** The booklet is dated April 2026 — if you are using this file later, re-pull it.

📌 **The practical read.** Customs is fast, cheap to start and **effective on counterfeits that move by sea** — but the **1/4 security is the real hurdle for a small business**, and **10 working days is the whole window** to get a court order. Have the court petition drafted *before* you file the customs complaint.

## 9.4 Civil remedies — the conservatory measures, Book by Book

Every Book of Law 82/2002 has a **pre-trial seizure** article. The differences matter: **the number of days you have to file the case afterwards is different in each**, and missing it kills the order.

| Book | Article | What can be ordered | **Deadline to sue, or the order lapses** | Appeal against the order |
|---|---|---|---|---|
| **Patents & utility models** | ✅ **Art. 33** | Conservatory measures against products/goods claimed to imitate the patented product, **per the detailed description in the patent document**; ordered to preserve the goods in their state. **May be issued before proceedings are instituted.** | **8 days** | — |
| **Patents (damages/destruction)** | ✅ **Art. 35** | Conservatory measures to **ensure payment of the decided fines or damages**; and **destruction of the objects in question, where necessary** | — | — |
| **Trade secrets** | ✅ **Art. 62** applying **Arts. 33 and 35** | as above | **8 days** (via Art. 33) | — |
| **Trademarks** | ✅ **Art. 115** | Description/inventory of machines, implements, products, signboards, packaging, invoices, advertisements; establishing the infringement | **15 days** | ✅ **Art. 116 — within 30 days**; the president may confirm or revoke, totally or in part |
| **Industrial designs** | ✅ **Art. 135** (same structure as the trademark articles) | as above | **15 days** | Art. 136 |
| **Copyright** | ✅ **Art. 179** | **(1)** detailed description of the work/performance/recording/broadcast; **(2)** discontinuance of publication, exhibition, reproduction or manufacture; **(3)** **seizure** of the original and copies and of the material used for re-publication (where that material could only be so used); **(4)** establishing the infringement; **(5)** **assessment and seizure of the income** made from exploitation. The president may appoint **experts** to assist the bailiff, and **shall require an appropriate security from the requesting party.** | **15 days** | ✅ **Art. 180 — within 30 days**; the president may confirm, revoke, **or appoint a custodian**, with income deposited in the court's treasury until the dispute is settled |
| **Destruction / disposal of seized goods (trademarks)** | ✅ **Art. 117** | The court may order the **sale** of the articles distrained and deduction of their value from compensation or fines; **destruction of the illegal marks**, and where necessary of the products, packaging, signboards, invoices, correspondence, advertisements **or other items** bearing them, and of the **machines and implements used specifically in the infringement**; and **publication of the judgment in one or more newspapers at the convicted party's expense**. 📌 **«The court may order some or all of the above measures, even in the event of acquittal.»** | — | — |

📌 **The single most valuable thing in this section:** **Art. 117 lets the court order destruction even if the defendant is acquitted.** So the strategic value of the criminal complaint is not the sentence — it is the **seizure and destruction** that follow. Say this to a client before they decide that "the case is not worth it".

⚠️ **The security requirement (Art. 179, third paragraph) is the practical barrier in copyright cases**, exactly as the 1/4-consignment deposit is at customs. Budget for it.

## 9.5 Criminal penalties — the complete table, by article

📌 **Every one of these is a `جنحة` (misdemeanour)** for limitation purposes, whatever the fine or the term of imprisonment. **That is why the limitation period is 3 years and not 10** (see §9.6).

| Law / Book | Article | Act | Penalty |
|---|---|---|---|
| **82/2002 Book One** — patents & UMs | ✅ **Art. 32** | **(1)** imitation for commercialisation of a granted invention or utility model; **(2)** sale, offering for sale, circulation, import or possession with intent to trade in imitations, known to be imitations, where the patent is granted and valid in Egypt; **(3)** unlawful use on products, advertisements, trademarks or packaging of indications that may lead to believe a patent has been obtained | **Fine EGP 20,000–100,000.** **Repetition:** imprisonment **up to 2 years** + **EGP 40,000–200,000**. In all cases: **seizure** of the imitated products and the implements, and **publication of the conviction in daily newspapers at the convicted party's expense** |
| **82/2002 Book One** — trade secrets | ✅ **Art. 61** | Illegal-means disclosure; acquisition or use while aware of confidentiality and illegal acquisition | **Fine EGP 10,000–50,000.** **Repetition:** imprisonment **≤ 2 years** + **EGP 50,000–100,000** |
| **82/2002 Book Two** — marks | ✅ **Art. 113** | **(1)** counterfeiting or imitating a registered mark in a misleading manner; **(2)** fraudulently using counterfeit/imitated marks; **(3)** fraudulently affixing another's mark to one's products; **(4)** knowingly selling, offering, distributing or acquiring for sale products bearing a counterfeit/imitated or unlawfully affixed mark | **Imprisonment ≥ 2 months + fine EGP 5,000–20,000, or either punishment.** **Repetition:** imprisonment ≥ 2 months + **EGP 10,000–50,000**. In all cases: **confiscation of the infringing products, the revenue and returns, and the implements.** The court **may** order **closure of the enterprise up to 6 months**, and **on repetition closure is mandatory** |
| **82/2002 Book Two** — false trade indications / geographical | ✅ **Art. 114** | Seven heads: false trade indication on products, shops, warehouses, signboards, packaging, invoices, correspondence, advertisements; fraudulent indication that a mark **has been registered**; **use of an unregistered mark in the cases of Art. 67 ¶¶ 2, 3, 5, 7, 8**; false mention of medals/diplomas/awards; misuse of joint-exhibition distinctions; misleading geographical indications (Art. 105); misleading designation of origin (Art. 106); affixing a reputed place's GI to products made elsewhere (Art. 107) | **Imprisonment ≥ 1 month + fine EGP 2,000–10,000, or either.** **Repetition:** imprisonment ≥ 1 month + **EGP 4,000–20,000** |
| **82/2002 Book Two** — industrial designs | ✅ **Art. 134** | Infringement of a registered design | **Fine EGP 4,000–10,000.** **Repetition:** imprisonment ≥ 1 month + **EGP 8,000–20,000** |
| **82/2002 Book Three** — copyright & related rights | ✅ **Art. 181** | **Seven heads** — see §6.9: **(1)** selling/renting/circulating a protected work without prior written authorisation; **(2)** knowingly imitating, selling, offering, circulating or renting; **(3)** knowingly imitating within Egypt, or selling/offering/circulating/renting/**exporting** a work published abroad; **(4) dissemination through computer networks, the Internet, information networks, communication networks and other means of technology** of a work, recording, broadcast or performance without prior written authorisation; **(5)** manufacturing, assembling or importing for sale/rent devices **especially designed to circumvent** a technical protection measure; **(6)** removing, neutralising or disabling in bad faith any technical protection device; **(7)** **infringing any of the moral or economic copyright or related rights provided for in this Law** | **Imprisonment ≥ 1 month + fine EGP 5,000–10,000, or either sanction.** **Sanctions are multiplied according to the number of infringed works, recordings, broadcasts or performances.** **Repetition:** imprisonment ≥ 3 months + **EGP 10,000–50,000**. **Confiscation in all cases.** **Closure ≤ 6 months on conviction; mandatory on repetition under heads (2) and (3).** **Publication of a summary of the judgment at the convicted person's expense.** (See §6.9) |
| **82/2002 Book Three** — legal deposit | ✅ **Art. 184** | Failure by publisher, printer or producer to deposit copies (≤ 10), where the minister has set the number | **Fine EGP 1,000–3,000 per work**; the deposit obligation **remains** |
| **82/2002 Book Three** — establishments | ✅ **Art. 187** | Circulating works/recordings/broadcasts by sale, rent, loan or licensing **without the licence** or **without keeping the registers** | **Fine EGP 1,000–5,000.** **Repetition: EGP 10,000–20,000** |

✅ **Who enforces:** **Art. 118** (Book Two) and **Art. 188** (Book Three) — *"The Minister of Justice shall, in agreement with the competent minister, issue a decision designating law enforcement officers for the purposes of this Law"* / *"…designating law enforcement officers…"*. **Art. 42** does the same for Book One. **This is the article that makes a seizure visit lawful — ask to see the designation before you let anyone in, and ask for it again if the officers are from a different administration than the right book.** (See §9.7 for which administration.)

## 9.6 The three clocks

| Clock | Instrument | Period | When it starts / is interrupted |
|---|---|---|---|
| **Civil compensation** — general | ✅ **Civil Code (Law 131/1948) Art. 374** | **15 years** | general rule |
| **Civil compensation** — periodic / self-renewing rights | ✅ **Civil Code Art. 375** | **5 years** | *"the rights of … periodic, recurrent dues such as … rent, **the wages (الأجور)**, … and in general everything that is due periodically or for a limited period"* — **this is the royalty clock, and it is short** |
| **Criminal** | ✅ **Code of Criminal Procedure (Law 150/1950) Art. 15** | **10 years** for felonies / **3 years** for misdemeanours / **1 year** for contraventions — *"unless the law provides otherwise"* | every Law 82/2002 offence is a **misdemeanour** ⇒ **3 years**. **Art. 17** of the same law: the period is **interrupted** by investigation, charge and trial steps |
| **Prescription must be pleaded** | ✅ **Civil Code Art. 387** | — | **the court may NOT apply prescription of its own motion** — «لا يجوز للقاضي أن يقضي من تلقاء نفسه بالتقادم». **If you are the defendant and you do not raise it, you lose it.** |
| **Reconciliation** | ✅ **CPC Art. 18 bis** | — | a **صلح (reconciliation)** ends the **criminal** case, **and has no effect on the injured party's civil claim** |
| **Suspension in Economic Court settlement** | ✅ **Law 120/2008 Art. 8 bis(و)** | — | **prescription is suspended while the preparation-and-mediation procedure runs** (§9.2) |

📌 **Three traps, in one paragraph.** **(a)** An unpaid royalty claim is a **5-year** claim, not 15 — Art. 375, and it self-renews year by year, so a freelancer who invoices and is never paid **loses each month's invoice five years later**, silently. **(b)** A criminal IP case is **3 years**, and the criminal case **does not carry the civil compensation** — Art. 18 bis means a settlement in the criminal file can leave you with nothing. **(c)** Because of **Art. 387** the limitation is a **shield you must pick up**, not a wall — this is why "nothing happened, they never sued" is not an answer in Egypt the way it is in some civil-law systems.

## 9.7 Who investigates and who prosecutes

Source: **ITIDA's own IPR Booklet** (`https://itida.gov.eg/English/Publications/Documents/IPR-Booklet.pdf`, retrieved via Firecrawl — `curl` to the host fails).

| Type of right | The police administration that takes the complaint |
|---|---|
| **Copyright and neighbouring rights** | **الإدارة العامة لمباحث المصنفات والملكية الفكرية** — the General Administration of Works-of-Mind (Artistic Works) and Intellectual Property Investigations, **Ministry of the Interior** |
| **Patents, trademarks, industrial designs** | **الإدارة العامة لمباحث التموين** — the General Administration of Supply Investigations |

✅ **The prosecution is the `نيابة الشئون المالية والإدارية`** (the Public Prosecution for Financial and Administrative Affairs) for these offences.
✅ **Government complaints line: 16528.**

📌 **Practical effect:** the **first phone call for a counterfeit trademark is to the Supply Investigations administration, not to the trademark office**, and the first call for pirated software or a stolen course recording is to **Works-of-Mind Investigations**. EGIPA registers rights; it does not make arrests.

## 9.8 The sequence, in the order that works

For a small business owner who has just found an infringer. **This is my synthesis of the articles above — the articles are verified, the sequencing is my recommendation.**

1. **Freeze the evidence.** Photograph the listing, the shop, the packaging; buy a sample through a witness if you can; note dates. Nothing you file later beats a dated screenshot taken now.
2. **Check your own position.** Is the mark registered **and in use** (§3.8 — a mark unused 5 consecutive years is cancellable)? Is the patent granted and in force (annuities paid)? Is the deposit/recordal in place for the copyright chain (§6.6)?
3. **Compute the value** to decide the forum: **≤ EGP 15 million** ⇒ first instance; **> EGP 15 million or undetermined** ⇒ the appellate court as first instance; **≤ EGP 750,000** ⇒ expected to be final (§9.2).
4. **Send a cease-and-desist** — it is cheap, it often works, and it **starts a paper trail that matters for "knowingly" in the criminal articles** (Arts. 32(2), 113(4), 181(2)).
5. **Get the seizure order first, then move.** Conservatory measures are available **before** suit (Arts. 33, 115, 135, 179). **And note the deadlines you then owe the court: 8 days for patents and trade secrets, 15 days for trademarks and copyright.**
6. **If the goods are moving, file with customs** (§9.3) — and be ready to deposit **one quarter of the consignment value** and to produce the judicial measure **within 10 working days**.
7. **File the criminal complaint** with the right investigations administration (§9.7). The value is the **seizure, confiscation and destruction** — including **after an acquittal** (Art. 117) — plus, in trademark cases, the **threat of closure of the enterprise** (Art. 113).
8. **Diarise the clocks** (§9.6) and **do not let a criminal settlement bury the civil claim** (CPC Art. 18 bis).

**As of: 2026-10-19** (Economic Courts: Laws 120/2008, 146/2019 and the Official Gazette scan of 156/2024; limitation: Civil Code textual file and CPC Art. 15; enforcement articles and penalties: WIPO English text of Law 82/2002; customs: the Customs Authority booklet of April 2026).

---

# 10. Fees — what things actually cost, and how confident this file is

## 10.1 Read this before you quote any number

There are **four layers**, and the number published on a website is almost never the whole figure.

| Layer | Instrument | What it is |
|---|---|---|
| **1. The statutory ceiling** | **Law 82/2002 itself** — Arts. 31, 73, 90, 92, 122, 185–187 | An upper bound written into the *law*, which the executive regulations may not exceed |
| **2. The statutory fee schedule** | **PM Decree 1366/2003** (Books I, II, IV) and **PM Decree 497/2005** (Book III) | The actual fees — **but at 2003/2005 prices** |
| **3. The Authority's service charge** | **EGIPA Decisions 84, 138, 139, 140, 141 of 2025** | A *separate* charge per service, **"in addition to the fees imposed by law and the stamp dues payable under the Stamp Law"** — see the header sentence on every annex |
| **4. The annual top-up** | **EGIPA Decisions 64 and 65 of 2026** ⚠️ | Fixed additions per service — **sourced only from law-firm client alerts**, not the decision text (§10.5) |
| **+ Stamp duty, always** | The Stamp Law | Every schedule ends with *"Stamp value to be added, according to the legislation on stamps"* |

📌 **The consequence, stated plainly:** **a quoted figure that is not dated is worthless.** Fees move by administrative decision, the decisions are **image-only PDFs in Arabic on `egypo.gov.eg`**, and no consolidated English fee list exists. **Every figure below carries the date I read it.**

## 10.2 The statutory ceilings (Law 82/2002)

| Article | The fee | **Cap in the law** |
|---|---|---|
| ✅ **Art. 31** | Utility-model application fees | **not more than EGP 1,000** |
| ✅ **Art. 73** | The fees for the acts in the trademark register, **in total** | **not more than EGP 5,000** |
| ✅ **Art. 90** | Renewal supplement during the **6-month grace** | **not exceeding EGP 500** |
| ✅ **Art. 92** | Re-registration of a cancelled mark within 3 years | **not more than EGP 1,000** |
| ✅ **Art. 122** | Design application (up to **50 designs** in one application) | **not more than EGP 3,000** |
| ✅ **Art. 185** | Recordal of a disposal of a work in the register | **not more than EGP 1,000 per work** |
| ✅ **Art. 186** | Deposit certificate | **not more than EGP 1,000 per certificate** |
| ✅ **Art. 187** | Licence for an establishment circulating works | **not more than EGP 1,000** |

## 10.3 The statutory schedules — the 2003/2005 layer

### (a) Patents, utility models and layout designs — ER 1366/2003, annex "Fee Schedule for Patents for Inventions and Utility Models, and Layout Designs for Integrated Circuits" ✅ read locally

| Service | Fee (2003) |
|---|---|
| Application for a **patent for an invention** | **EGP 150** per application |
| Application for a **utility model** | **EGP 100** per application |
| Application to register a **layout design for an integrated circuit** | **EGP 1,000** per application |
| Access to / true copy of a patent application | EGP 100 |
| **Appeal** before the Art. 36 committee | EGP 250 |
| **Objecting to the grant** of a patent | EGP 500 |
| | *Stamp value to be added* |

✅ **The four footnotes, verbatim:**
1. *"Applications filed by students of any kind of educational institutes shall be exempt of such fees."*
2. *"The annual fee shall be reduced to 10% for students."*
3. *"The annual fee shall be reduced to half for individuals or establishments with a maximum staff of ten persons."*
4. *"A surcharge of 7% shall be due for each year of delay."*

✅ **The annual progressive fee** (annex, from the 2nd year of filing to expiry):
| Beginning of year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **EGP** | 20 | 40 | 80 | 100 | 150 | 200 | 250 | 300 | 350 | 400 |
| **Beginning of year** | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| **EGP** | 500 | 600 | 700 | 800 | 900 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |

⚠️ **An internal contradiction in the regulation:** the table is headed *"Starting from the Second Year from the Filing Date"* but its first row reads **"Beginning of first year — 20"**. The **PCT Applicant's Guide** for Egypt resolves it the other way (annual fees *"from the second year"* at EGP 20 for the **2nd** year and EGP 40 for the 3rd), so the two official sources are **one year out of step**. **When a patent is in force, verify the annuity year against EGIPA's demand, not against a table.**

### (b) Trademarks — ER 1366/2003, annex "Fee Schedule for Trademarks" ✅ read locally

| # | Service | Fee (2003) |
|---|---|---|
| 1 | Application, **one class** | **EGP 50** |
| 2 | Application, multiple classes: first class **50**, **each other class 25** | |
| 3 | Application for a **certification mark** | EGP 100 |
| 4 | Application to register a **local mark abroad** (per country) | EGP 100 |
| 5 | **Appeal** to the appeal committee (Arts. 77, 78) | EGP 100 |
| 6 | **Publication** of the mark on acceptance | EGP 50 |
| 7 | **Objecting** to acceptance (opposition) | **EGP 250** |
| 8 | **Registration**, one class | **EGP 60** |
| 9 | Registration, multi-class: first **60**, each other **50** | |
| 10 | Registration of a **certification mark** | EGP 100 |
| 13 | Request for **cancellation** of a registered mark | EGP 50 |
| 14 | Recording a **transfer of ownership** or right of use — within **3 months** 100 (per related mark 50); after 3 months 125 (60); after 6 months 150 (70) | |
| 16 | Recording a **mortgage** of a mark — within 3 months 50; after 3 months 60; after 6 months 100 | |
| 20 | **Renewal** in the last year — one class **50**; multi-class first **50**, each other **25**; certification mark **100**. **Surcharge if filed in the 6 months following expiry: EGP 200** | |
| 21 | **Re-registration after cancellation**, within 3 years (Art. 92) | **EGP 1,000** |
| 23 | Access to / extracts from the register | EGP 55 |
| 33 | **Examination of a mark before filing** the application | EGP 150 |
| — | *Stamp value to be added, according to the legislation on stamps* | |

### (c) Industrial designs — ER 1366/2003, annex "Fee Schedule for Industrial Designs" ✅ read locally

| # | Service | Fee (2003) |
|---|---|---|
| 1 | Application, **single design** | **EGP 30** |
| 1 | **Each additional design** in a multiple deposit | **EGP 15** |
| 2 | Application to register a local design abroad | EGP 100 |
| 3 | **Appeal** (Art. 124 committee) | EGP 100 |
| 4 | Publication of each design | EGP 30 |
| 5 | Objecting to registration | EGP 75 |
| 6 | **Registration** | EGP 75 |
| 7 | Request for **cancellation** | EGP 15 |
| 8 | Recording transfer of ownership / right of use — within 3 months 75; after 3 months 100; after 6 months 150 | |

### (d) Copyright — ER 497/2005, "Table of Fees in Respect of Copyright and Neighboring Rights" ✅ read locally

| Service | Office | Fee |
|---|---|---|
| **Personal licence for copying and/or translating a work** (Art. 170 compulsory-licence regime) | Copyright Protection Office, **Ministry of Culture** | **L.E. 400/work** |
| same, for works under the Ministry of Information | Broadcasting / Audio-Visual Office | L.E. 400/work |
| same, for **computer software and databases** | **ITIDA** — Computer Software & Database Office | **L.E. 250/work** |
| same, for software/databases where the Culture Office is the proper office | Culture | L.E. 400/work |
| **Commercial or professional use of works in the public domain** (Art. 183) | Culture | **L.E. 1,000/work** |
| same — broadcasting / sound recordings / performances | Broadcasting Office | L.E. 500/work |
| same — **audio works** (interviews, poetry, lyrics, music…) | Broadcasting Office | L.E. 600/work |
| same — **audio-visual works** (films, shows, cartoons) | Broadcasting Office | L.E. 800/work |
| same — **TV series, plays, feature films** | Broadcasting Office | L.E. 1,000/work |
| same — software/database in the public domain, **educational** use | **ITIDA** | L.E. 500/work |
| same — software/database in the public domain, **non-educational** use | **ITIDA** | L.E. 1,000/work |
| **Establishment licence** to circulate works by sale/rent/loan/licensing (Art. 187(1)) | Culture | **L.E. 250** one activity for one year; **L.E. 1,000** more than one activity for one year |
| same, for **software/databases** | **ITIDA** | **L.E. 500/work non-profit; L.E. 1,000/work for-profit** |
| same (broadcasting) | Broadcasting Office | L.E. 1,000/work |
| **Entry in the Art. 185 register of disposals** — author's disposal of a work | Culture | **L.E. 100 per entry** |
| entries for **audio** works | Broadcasting Office | L.E. 500 per entry |
| entries for **audio-visual** works | Broadcasting Office | L.E. 800 per entry |
| entries for **software/database** | **ITIDA** | L.E. 250 per entry (educational) / L.E. 500 (non-educational) |
| **Deposit certificate** (Art. 186) — written work, plastic-arts text, performance of a recorded work ≤ 1 hour (Culture: 200; ≤ 4 hours: **500**); audio (200/300); audio-visual (400; TV series/plays/films 500); software (250 educational / 500 non-educational) | per office | **L.E. 200 – 1,000 per certificate** |
| *Value of the fiscal stamps are to be added in accordance with the Stamp Law* | | |

⚠️ **A structural trap in this table:** the **"appropriate office" is not cosmetic**. The **same act costs a different amount depending on which office is competent**, and **competence is decided by the class of work** (Art. 138(18)/(19) — see §6.8). Getting the office wrong means paying the wrong fee and the recordal does not bind third parties (§6.6).

## 10.4 The current EGIPA service charges — read off the page scans, 2026-10-19

**What I read.** Five decisions of the **Chairman of the EGIPA Board**, all signed **أ.د. هشام عزمي (Dr. Hisham Azmy)** — the fee schedules **dated 14 October 2025**, the patent-agents decision **dated 8 September 2025**:

| Decision | Subject | Annex |
|---|---|---|
| **138 of 2025** | Patents & utility models; general services | 3 pages, ✅ read page-by-page |
| **139 of 2025** | **Secured papers (الأوراق المؤمنة)** bearing the State emblem | ✅ read |
| **140 of 2025** | **Plant varieties** | ✅ read |
| **141 of 2025** | **Copyright** (المؤلف) | ✅ read |
| **84 of 2025** | **Patent agents** (dated 8/9/2025) | ✅ read |

✅ **The common preamble (read verbatim, Decision 138/2025 page 1)** cites: **Law 82/2002** and its ER; **Law 163/2023**; **PM Decree 4370 of 2024** (forming the EGIPA board); **PM Decision 223 of 2025** (the organisational structure); **EGIPA Decision 34 of 2025** on the collection of fees; **board minutes No. 3 of 19 May 2025** and **No. 4 of 7 September 2025**. And ✅ **Art. 4 of each decision: "يُعمل بهذا القرار من تاريخ صدوره"** — *the decision applies from the date of its issue* ⇒ **14 October 2025**.

📌 **So the "14 vs 15 October 2025" disagreement in the law-firm alerts is settled by the decisions themselves: 14 October 2025.** Recorded as a source conflict at the end of §11.

### (a) Decision 138/2025 — patents, utility models and general services (read off `doc138-1..3`)

✅ **Table One — General services:**

| # | Service | Fee |
|---|---|---|
| 1 | **Translation** — per page | **EGP 200** |
| 2 | **Certified copy of a translation** — per page | EGP 200 |
| 3 | **Review and vetting of applications** — per page | EGP 200 |
| 4 | **To-whom-it-may-concern certificate** — electronic certificate extract | EGP 1,000 |
| 5 | Paper copy of a to-whom-it-may-concern certificate | EGP 1,000 |
| 6 | **Request for a judicial seizure (ضبطية قضائية)** | **EGP 10,000** |

✅ **Table Two — services of the General Administration for Patents:**

| # | Service | Fee |
|---|---|---|
| 7 | Extension of the deadline to pay **examination costs** — one month | **EGP 25,000** |
| 8 | Extension of the deadline to pay **experts' fees** — one month | EGP 1,000 |
| 9 | **Preparing and registering a patent application** through the electronic filing system — **individuals** | EGP 1,000 |
| 10 | **Registering a patent application** through the electronic filing system — **individuals** | EGP 500 |
| 11 | **Submitting documents** through the electronic filing system | EGP 500 |
| 12 | **Formatting the application to the new forms** (agents, companies) — **max 100 pages** | **EGP 10,000** |
| 13 | Formatting — **per page beyond 100** | EGP 20 |
| 14 | **Preparing drawings** | EGP 250 |
| 15 | **Patent searches** | EGP 7,000 |
| 16 | **Recording assignments / licences of use** | **EGP 10,000** |
| 17 | **Publication of an expression of intent** | EGP 3,000 |
| 18 | **Amending the applicant's data** | EGP 1,000 |
| 19 | **Changing the patent agent** | EGP 5,000 |
| 20 | **Amending company names** | EGP 6,000 |
| 21 | **Adding an inventor — per name** | EGP 200 |

⚠️ **Every annex is headed: «يُسدد بالإضافة إلى الرسوم المفروضة قانونًا والدمغات المستحقة وفقًا لقانون الدمغة» — *paid in addition to the fees imposed by law and the stamp dues payable under the Stamp Law*.** **That is why the total on the counter is not the number in the table.**

⚠️ **Item 12 is the sleeper cost:** a company or a professional (as opposed to an individual) that files a patent application of up to 100 pages on the new forms pays **EGP 10,000 for formatting**. **For a small company's first patent, that single line can exceed every other fee combined.**

### (b) Decision 141/2025 — copyright (read off `doc141-2`)

| # | Service | Fee |
|---|---|---|
| 1 | Filing a **deposit application** | **EGP 1,000** |
| 2 | **Pre-examination**: review of the work in the electronic register before filing; document-review request; deposit application presented to the Copyright Administration | **EGP 300** |
| 3 | Request for **publication of acceptance** (deposit, waiver, transfer of ownership, suspension or revival of restricted disposals, mortgage, attachment) and publication of amendments — at the applicant's option | EGP 500 |
| 4 | Request by the **author** to amend a **work already deposited** | EGP 2,000 |
| 5 | Request by the **author** to amend the **title** of a work that has been disposed of | EGP 2,000 |
| 6 | **Amending data or images, or adding documents** to a previously filed application | EGP 1,000 |
| 7 | **Certificate authentication** | EGP 1,000 |
| 8 | **Amending the design** (adding/removing parts) where it does not comply with the specifications | EGP 1,000 |
| 9 | **Delegate visit** to inspect a **technical work** requiring travel to its location — in addition to fees and the service charge: **Cairo 2,000 / Lower Egypt governorates 5,000 / Upper Egypt governorates 7,000** | |
| 10 | **Delegate visit** to complete deposit/waiver/transfer of a financial right outside the office | EGP 5,000 |

📌 **For a freelancer or small publisher the realistic first bill is items 1 + 2 + 7 (or 3): EGP 2,300 / 2,500.** **Not counted here: the statutory ER 497/2005 fees and the stamp duty, which are added on top** (§10.3(d)).

### (c) Decision 140/2025 — plant varieties (read off `doc140-1..2`)

| # | Service | Fee |
|---|---|---|
| Examination | | EGP 2,000 |
| Amending data | | EGP 400 |
| **Priority claim** | | EGP 3,000 |
| **English-language certificate** | | EGP 2,000 |
| Recording / transferring / deleting a representative | | EGP 4,000 |
| Representation statement | | EGP 2,000 |
| **DUS results (Distinctness, Uniformity, Stability)** | | **EGP 10,000** |
| Maintenance report | | EGP 2,000 |
| DUS copy — inside Egypt / outside | | EGP 4,000 / EGP 10,000 |
| Enquiry on a protected variety | | EGP 500 |
| **Provisional protection certificate** | | EGP 500 |
| Statement on a protected variety / to an interested party | | EGP 2,000 / EGP 2,000 |
| **Request for an infringement-verification committee** | | EGP 10,000 |
| Recording assignments / licences | | EGP 10,000 |

*(This annex is dated **14/10/2025** in the same series.)*

### (d) Decision 139/2025 — secured papers
✅ The annex covers **الأوراق المؤمنة** — the **security paper** used for official certificates — at, among other amounts, **EGP 200 per page**. ⚠️ **This is a paper/document charge, not an IP fee; do not fold it into a filing estimate as if it were.**

### (e) Decision 84/2025 — patent agents (dated 8 September 2025)
| Service | Fee |
|---|---|
| **Registering a patent agent** | **EGP 5,000** |
| **Striking a patent agent off** | **EGP 1,000** |
*(plus statutory fees and stamp dues as stated on the page scan)*

## 10.5 The 2026 top-up — Decisions 64 and 65 of 2026 ⚠️

⚠️ **Sourced only from law-firm client alerts** (One World, JCIPO, Alyafi), **not from the decision text** — I could not retrieve the decisions themselves. **Verify before relying.**

| What the alerts say | Amount |
|---|---|
| In force | **5 April 2026** |
| **Additional fixed fee on all services of the Central Administration for Trademarks** — trademarks, trade names, geographical indications, industrial designs | **EGP 500** |
| **Specialised company search service** | **EGP 2,000** |
| **Official copies** of expert reports, minutes, case files and complaints **recorded up to 2024** | **EGP 5,000** |
| same, **up to 2025** | **EGP 3,000** |

📌 **If the alerts are right, the practical effect on a trademark filing is: the 2003 statutory fee + the EGP 300 EGIPA service charge (if any) + EGP 500 + stamp.** **But the base trademark fee itself is still unverified — see §10.6.**

## 10.6 ❌ What I could NOT find: an official current trademark fee schedule

**I searched and it is not there.** Recorded because it is the single most-asked cost question in this field.

- ❌ **No trademark fee schedule among EGIPA's 2025 decisions** that I could find or read (the published set covered patents/UMs, secured papers, plant varieties, copyright, patent agents).
- ❌ **`itda.gov.eg`'s trademark pages are dead** — `/form-tm.aspx`, `/hint-tm.aspx`, `/TM-Details.aspx` all returned **HTTP 404 on 2026-10-19** (§2.4).
- ❌ **No EGIPA trademark fee page** surfaced in the search.
- ⚠️ **JCIPO's own trademark guide, checked independently on 2026-10-06, states that its fee figures *could not be verified from an official source*.** I agree with that conclusion from my own search.

**So the only verifiable trademark figures are the three layers above:** the **statutory caps** (Art. 73 — total ≤ EGP 5,000), the **2003 ER schedule** (§10.3(b) — 23 years old and certainly not what is charged now), and the **⚠️ EGP 500 addition** of Decisions 64/65 of 2026. **An all-in current trademark filing cost cannot be stated from an official source as of 2026-10-19.** 🟡

📌 **What to tell a client instead of a number:** *"the statutory ceiling for all trademark-register fees together is EGP 5,000 (Art. 73); the published EGIPA charges add a fixed amount per service; ask EGIPA at the counter or on 16528 for the current figure, in writing, before you budget."* **That is honest, and it is the only honest answer available.**

## 10.7 PCT national-phase fees (WIPO PCT Applicant's Guide — Egypt, valid from 1 September 2026) ✅

| Item | Amount |
|---|---|
| **National-phase deadline** | **30 months** from the priority date (PCT Arts. 22(1), 39(1)(a)) |
| **Translation required into** | **Arabic** |
| **National filing fee — patent** | **EGP 150** |
| **National filing fee — utility model** | **EGP 100** |
| Students | **0** |
| **Annual fees** | from the 2nd year: **EGP 20**; 3rd year: **EGP 40**; … (with the student and small-establishment reductions of §10.3(a)) |
| **Reinstatement** of rights — "due care" criterion | **EGP 800** individuals / research institutes; **EGP 1,000** companies < 10 employees; **EGP 1,500** companies > 10 employees |
| Restoration of priority | also on the **"due care"** criterion |
| **RO transmittal fee** | **USD 142** |
| **ISA is EG (Egyptian Patent Office)** — search fee | **EGP 4,000** (also quoted CHF 64 / EUR 70 / USD 80), **25% reduction** for applicants in certain income groups |
| **IPEA** (preliminary examination) | **EGP 3,000** |

📌 **Read the reinstatement table against the small-business reality: the *fee to be late* (EGP 1,500) is ten times the fee to file (EGP 150).** Egypt prices delay, not filing.

## 10.8 What a small business actually pays — the honest summary

| Goal | What is verifiable today | Confidence |
|---|---|---|
| **Register a trademark** | Statutory cap **EGP 5,000 total** (Art. 73); 2003 schedule as a *floor*; **+ EGP 500 per service** if Decisions 64/65 of 2026 apply; **+ stamp**; **+ whatever EGIPA currently charges** | 🟡 **Cannot be stated** — §10.6 |
| **File a national patent** | Statutory **EGP 150** + EGIPA service charge (individuals: **500 + 1,000** for electronic filing/preparation, or **10,000** formatting if via an agent/company on the new forms, max 100 pages) + searches **7,000** + stamp | ⚠️ **Components verified; total not** — the layers are priced independently |
| **Deposit a copyright work** | EGIPA **1,000** (application) + **300** (pre-examination) + **500** (publication) + **1,000** (authentication) + ER 497 statutory fee + stamp | ⚠️ **≈ EGP 1,800** (application + pre-examination + publication) **to ≈ EGP 2,800** (with certificate authentication) |
| **Register a design** | Statutory **EGP 30** + **15** per extra design (2003); Art. 122 cap **EGP 3,000**; **+ EGP 500** per 2026 alert; + stamp | ⚠️ |
| **Licence a work to the public (public domain / establishment)** | ER 497/2005 figures are **the operative schedule** here — 250/400/500/800/1,000 per work (§10.3(d)) | ✅ |
| **Enforce** | **EGP 10,000** for a judicial-seizure request (Dec. 138/2025) + the **court security** (Art. 179) or **1/4 of the consignment value** at customs + the **settlement fee 2,000–200,000** if the Economic Court sends you to mediation | ✅ |

**As of: 2026-10-19** (statutory caps and penalties: WIPO English text of Law 82/2002; ER 1366/2003 and ER 497/2005 fee schedules read in the locally extracted English texts; EGIPA decisions 138/139/140/141/84 of 2025 read off their page scans the same day; Decisions 64/65 of 2026 ⚠️ from client alerts; PCT figures from the WIPO PCT Applicant's Guide — Egypt, valid from 1 September 2026).

---

# 11. Widely repeated but unverified — check before repeating

**This section is the mirror image of the corrections table.** The corrections table holds things the primary texts **contradict**. This section holds things that **everyone repeats and I could not verify either way** — often because the only sources are law-firm blogs, SEO content or an old version of a government page. **Nothing here may be stated as fact.** Where I *did* resolve one, the row says so.

| # | The claim, as it circulates | Where it circulates | Status |
|---|---|---|---|
| 1 | **Specific trademark registration fee figures** — e.g. "EGP 6,000 to file a mark", "EGP X per class" | Law-firm blog posts, forums, "how to register a trademark in Egypt" articles, sometimes by well-known firms | 🟡 **UNVERIFIED — and I searched hard.** No official current trademark fee schedule exists in any source I could reach (§10.6). The only verifiable layers are the **statutory cap (Art. 73, EGP 5,000 total)**, the **23-year-old ER 1366/2003 schedule**, and the **⚠️ EGP 500 addition** of Decisions 64/65 of 2026. **Any specific figure a model produces is a guess.** |
| 2 | "The IP law was amended by **Law 131/2003** and **Law 5/2010**" | Historic Egyptian legal commentary; older academic pages; **and file 01 of this corpus flagged it as unverified** | ❌ **CONTRADICTED.** Only **26/2015, 144/2019, 178/2020**. See corrections table row 1 and §1.3. |
| 3 | "**ITIDA gives software companies a free-zone / export exemption**" | Repeated by software businesses, incubators and non-specialist advisers | ❌ **DOES NOT EXIST in that form.** See §7.3 and corrections table row 7. The real things are ITIDA's **Export-IT cash rebate** and the **Investment Law 72/2017** zone relief. |
| 4 | "**Trademarks are registered at ITDA in Nasr City**" (still stated on many current firm pages) | Very widely — the address was correct for years | ⚠️ **OUT OF DATE IN PRACTICE.** The office has been **relocating to 101 Kasr El Aini St.** (EGIPA premises) since **18 November 2025**, and the ITDA trademark pages **404 as of 19 October 2026** (§2.4). Verify by telephone before sending anyone. |
| 5 | "**The 2026 amendment to the IP law is in force and raises the copyright penalties**" | News coverage of the bill's committee stage; re-posts | 🟡 **NOT ENACTED as of 19 October 2026 as far as I could establish** — no promulgation, no law number, no gazette reference found (§1.4). **And the press disagrees on the fine even for the draft** ("up to EGP 1 million" vs "ten-fold the fine"). Do not tell a client the penalties changed. |
| 6 | "Copyright applicants **under 21 pay EGP 100**" | Appears in coverage of the **bill that became Law 178/2020** (e.g. the 18 August 2020 report on `rosaelyoussef.com/758100`) | 🟡 **The variant did not survive into the enacted text.** Art. 185 as enacted provides an **exemption for under-21s and holders of the disability/karama card** and **omits the EGP 100 limb**. **The enacted text governs** — do not quote the EGP 100. |
| 7 | "**Sound marks and smell marks can be registered in Egypt**", or "Egypt allows non-traditional marks" | Comparative-trademark articles; conference papers | ❌ **CONTRADICTED BY THE TEXT.** Art. 63: «**يجب أن تكون العلامة التجارية مما يدرك بالبصر**» — the mark **must be visually perceptible**. §3.1. |
| 8 | "**Software must be registered with ITIDA to be protected**" / "registration creates the copyright" | Vendor and consultancy content | ⚠️ **Half wrong.** Copyright **arises on creation** with no formality (**Art. 138(2)**; **Art. 140(2)** protects computer programs); **ITIDA's/EGIPA's act is a deposit and a recordal**, not the source of the right (§6.1, §7.2). ⚠️ **What I could not verify:** whether any *practical* enforcement forum demands a deposit certificate. **Do not promise that a certificate is a legal precondition, and do not promise that it is useless.** |
| 9 | "A **deposit certificate is proof of ownership**" | Widely said about copyright certificates generally | 🟡 **UNVERIFIED, and structurally doubtful.** Law 82/2002 gives the certificate as evidence of **deposit** (Art. 186); it does **not** create a presumption of authorship the way **Art. 65** does for a **registered trademark** (five-year use presumption). **Treat it as evidence of date and content, not of title.** |
| 10 | "Egypt has a **register of geographical indications** you can apply to join" | Said about GI protection regionally | ❌ **NO SUCH REGISTER in Law 82/2002** (§8.2). Protection runs through **prohibiting misleading use (Art. 112)** and the **trademark rules (Arts. 109–111)**. |
| 11 | "**Customs can destroy counterfeit goods**" / "customs handles it end to end" | Trade press | ⚠️ **PARTIAL, and dangerous to promise.** Customs' role is a **suspension of not more than 10 working days** (ER 430/2021 Art. 8) **conditional on the right owner taking judicial measures**, against a **deposit of one quarter of the consignment value** (§9.3). **Destruction is a court order**, not a customs decision (Art. 117). |
| 12 | "**The customs 1/4 security is refundable**" / "you get it back automatically" | Reasonable assumption, so people repeat it | 🟡 **UNVERIFIED.** The Authority's booklet (April 2026) states the deposit requirement **without stating the return mechanism**. **Do not advise a client that the money comes back; ask the IPR Protection Department in writing.** |
| 13 | "**The limitation period for an IP claim is 15 years**" | Said by analogy with Civil Code Art. 374 | ⚠️ **TRUE ONLY FOR LUMPSUM CLAIMS.** **Art. 375** puts **periodic, self-renewing dues — royalties included — at 5 years** (§9.6), and the criminal clock is **3 years** (CPC Art. 15). |
| 14 | "**Registering a mark gives you a defence for 5 years against any attack**" | A garbled version of Art. 65 | ⚠️ **GARBLED.** Art. 65 gives a **presumption of use / ownership** from registration after **5 years**, but **(a)** a **bad-faith** challenge is available **at any time**, and **(b)** **non-use for 5 consecutive years** makes the mark **cancellable on any interested party's request (Art. 91)**. §3.2, §3.8. |
| 15 | "**Egypt made an 18-month refusal declaration under the Madrid Protocol**" | Comparative filing guides | ❌ **CONTRADICTED by WIPO Lex's Madrid records:** Egypt made **no** such declaration (the refusal period is the **default 12 months**) and charges **no individual fee** (§3.10). |
| 16 | "A **utility certificate** (as in some Arab jurisdictions) exists in Egypt alongside the patent" | Regional IP comparisons | 🟡 **NO SUCH INSTRUMENT FOUND** in Law 82/2002. Egypt has a **patent**, a **utility model** (Art. 30 — 7 years, non-renewable), and **layout designs for integrated circuits** (Arts. 45–48). If a client asks for a "utility certificate", the Egyptian analogue is the **utility model**. |
| 17 | "**EGIPA was created by the 2023 IP law and replaced the Patent Office immediately**" | Summaries of Law 163/2023 | ⚠️ **PARTIAL.** Law 163/2023 **created** EGIPA from **7 August 2023**, but it built in a **transition period of up to one year, extendable once by six months**, and the **offices were only transferred by PM Decision 492 of 2025** (§2.2). Papers filed with the old offices during the transition were valid. |

📌 **Rule for a model using this file.** **If a claim is in this section, do not assert it.** Say: *"this is widely stated but I could not verify it from an official source; the verifiable position is …"* — and then give the **statutory ceiling, the article, or the official page** from the sections above.

## Source conflicts recorded in this file

**Where two retrieved sources disagree, I record both and say which governs.**

| # | The conflict | Side A | Side B | Which governs |
|---|---|---|---|---|
| 1 | **Effective date of Law 178/2020** | **The statute itself:** takes effect **one month after the day following publication** ⇒ gazette **5 Sept 2020** ⇒ **6 October 2020** | **WIPO Lex metadata:** shows **5 September 2020** | ✅ **The statute.** Cite **6 October 2020** and say the WIPO metadata differs. §1.3 |
| 2 | **The Art. 185 fee for under-21 applicants** | The **bill text as reported** (rosaelyoussef.com/758100, 18 Aug 2020) shows a **specific EGP 100** figure | The **enacted** Art. 185 provides an **exemption** and **omits the EGP 100 limb** | ✅ **The enacted text.** Do not quote the EGP 100. §6.6, §11 row 6 |
| 3 | **Effective date of EGIPA Decisions 138, 140 and 141 of 2025** | **Alyafi:** **14 October 2025** | **One World:** **15 October 2025** | ✅ **The decisions' own text:** dated **14/10/2025** and «يُعمل بهذا القرار من تاريخ صدوره» ⇒ **14 October 2025**. §10.4 |
| 4 | **The penalty in the 2026 draft amendment** | **El Balad (22 Apr 2026):** a fine of **up to EGP 1 million** | **Al-Shorouk (27 Apr 2026):** a fine of **ten times** the original | 🟡 **NEITHER — the bill is not law.** Record both, assert neither. §1.4, §11 row 5 |
| 5 | **The patent annuity year sequence** | **ER 1366/2003 annex:** headed *"from the Second Year from the Filing Date"* but its first row is **"Beginning of first year — EGP 20"** | **WIPO PCT Applicant's Guide — Egypt (Sept 2026):** annual fees *"from the 2nd year"* at **EGP 20**, 3rd year **EGP 40** | ⚠️ **Unresolved — the two official sources are one year apart.** Verify the year against EGIPA's own demand. §10.3(a) |
| 6 | **Who and where the trademark register is** | **The law (Art. 64, unchanged since 2002):** the **Trade Registry Department** | **Practice:** the **Trademark & Industrial Design Office**, moved to **EGIPA, 101 Kasr El Aini St.**; the ITDA TM pages **404** | ⚠️ **Both are true in their own register.** Quote the article for the *law*, the address for the *counter*. §2.4, §3 |
| 7 | **Whether Egypt's Madrid position includes an 18-month refusal period** | Comparative filing guides say or imply it does | **WIPO Lex Madrid records:** **no declaration** made — the default **12 months** applies, **no individual fee** | ✅ **WIPO Lex.** §3.10, §11 row 15 |

---

# 12. Open questions and things I could NOT resolve

| # | Question | What I searched | Status |
|---|---|---|---|
| 1 | The **current official trademark fee figures** (application, publication, registration, renewal, opposition) | EGIPA's decisions 138/139/140/141 of 2025 (none covers trademarks as a schedule); `egypo.gov.eg`; `itda.gov.eg` (TM pages 404); `itida.gov.eg` (via Firecrawl); JCIPO's guide (which independently says its own fees could not be verified officially) | 🟡 **UNRESOLVED — the single biggest gap in this file.** Everything verifiable is in §10.6. |
| 2 | The **text of EGIPA Decisions 64 and 65 of 2026** (the EGP 500 / 2,000 / 5,000 / 3,000 additions) | One World, JCIPO, Alyafi client alerts only; could not retrieve the decisions | ⚠️ **UNRESOLVED — firm alerts only.** §10.5. |
| 3 | **Art. 167 phonogram/recording term start point** — from fixation, publication, or first communication? | WIPO English text; the Arabic consolidated text | ⚠️ **NOT RESOLVED — carried open from file 01.** The term is **50 years**; the *start* is what is unclear. **Describe, do not cite a start point.** |
| 4 | **Arts. 7–8 (employee inventions)** — the detail of ownership, notification and compensation | Not read beyond the article headings in this pass | 🟡 **NOT READ.** These are the two articles a freelancer/employee question most often needs. **Read Arts. 7–8 in full before advising on who owns a work invention.** |
| 5 | Whether **EGIPA has actually taken over the software/database deposit office** from ITIDA in practice, and which counter a software author should approach | PM Decision 492 of 2025; ITIDA's booklet; no EGIPA practice notice found | 🟡 **UNRESOLVED.** §7.2 — the safe instruction is *"EGIPA first, ITIDA if redirected"*. |
| 6 | **EGIPA's internet presence and any e-filing portal** for patents/trademarks (does one exist, is it usable, what are its fees) | `egypo.gov.eg` (image-only PDFs; fee annexes retrieved), no working portal located | 🟡 **UNRESOLVED.** Everything found had to be read from page scans — which is itself evidence there is no usable public data layer yet. |
| 7 | Whether the **Economic Court felony circuits** created by Law 156/2024 have been **constituted by the Supreme Judicial Council** and are sitting | Law 156/2024 text and gazette scan; no implementation decision found | 🟡 **UNRESOLVED.** The **statute** is verified; the **courts** are not. |
| 8 | The **current location of the Trademark & Industrial Design Office**, as a settled fact | Mondaq/Adams alert of 18 Nov 2025 (relocation in progress); `itda.gov.eg` 404s | ⚠️ **IN TRANSITION.** §2.4. |
| 9 | The **Customs IPR department's e-mail address** (extraction reversed the string) and the **return mechanism for the 1/4 security** | Customs Authority booklet, April 2026 | 🟡 **UNRESOLVED.** Verify by telephone: **16528**. |
| 10 | Whether the **Art. 185 recordal obligation** applies to **exclusive licences** as it does to assignments, and whether non-recordal affects **exclusive licensees** as it does buyers | Text of Art. 185 as amended (Book Three), Law 178/2020 | ⚠️ **PARTIAL.** The enacted sentence is general («التصرف») and I read it verbatim (§6.6); **its application to licences is my reading, not a court's.** Advise recordal in every case. |
| 11 | The **full text and detail of Arts. 7–8**, **Arts. 11–15 filing mechanics**, and the **examination-cost schedule** for patents | English text read at article level; the operational detail sits in ER 1366/2003 (read) and in current EGIPA practice (not published) | ⚠️ **PARTIAL.** §4.3 covers the steps; the **out-of-pocket costs** are in §10.4 and are the authority's practice, not a statutory entitlement. |
| 12 | Whether **Egypt has any online trademark search** available to the public | Searched; the ITDA TM pages are dead | 🟡 **UNRESOLVED.** A clearance search therefore has to be commissioned from the office or an agent. |
| 13 | The **2026 IP bill's current parliamentary position** (committee stage, next hearing, whether it has been carried over to a new session) | El Balad (22 Apr 2026), Al-Shorouk (27 Apr 2026); no later development found by 19 Oct 2026 | 🟡 **UNRESOLVED.** §1.4. **Re-check before any advice that depends on copyright penalties.** |
| 14 | Whether the **2025 EGIPA fee decisions replaced, or merely supplemented, the ER 1366/2003 and ER 497/2005 schedules** | The decisions' own text («بالإضافة إلى الرسوم المفروضة قانونًا») | ⚠️ **SUPPLEMENTARY, on the text** — they are expressed as **in addition to** the statutory fees. **But nothing I found confirms EGIPA still collects the 2003 figures as the statutory base**, and no consolidated schedule was found. **§10.6.** |

---

# 13. Trap list for the agent — the twelve things that go wrong most

1. **Citing the phantom amending laws.** "Law 82/2002 as amended by Law 131/2003" — **the amendments are 26/2015, 144/2019 and 178/2020, and nothing else** (§1.3). **Books One and Two have never been amended**, so a Book One/Two article number is safe; a Book Three article number is not (Art. 185 was rewritten in 2020).
2. **Using the old Economic Court figures.** IP is **item (8)** of the **criminal** list (Art. 4) and **item (7)** of the **civil** list (Art. 6); the first-instance civil ceiling is **EGP 15 million** and finality is at **EGP 750,000** (§9.2). Anything quoting "item 9" or EGP 5m/10m is citing repealed text.
3. **Sending a client to the wrong office.** The Trademark Office has been **relocating to EGIPA's premises at 101 Kasr El Aini St.** since late 2025, and **ITDA's trademark pages are 404** as of 19 October 2026 (§2.4). **Telephone first — 16528** — every time.
4. **Believing copyright needs no paperwork and then discovering the deal does not bind anyone.** Protection is automatic; **but a disposal is not effective against third parties until the Art. 185 recordal is completed** (§6.6). **Tell the client to record the transfer before they deliver the work**, not after. And remember the competent office depends on the **class of work** — Culture / ITIDA / Information (§6.8, §10.3(d)).
5. **Missing the short post-seizure deadline.** The conservatory order **lapses** if the case is not filed within **8 days** (patents, utility models, trade secrets — Arts. 33, 62) or **15 days** (trademarks and copyright — Arts. 115, 179) (§9.4). **Draft the petition in advance and diarise the day.**
6. **Using 15 years as the clock for unpaid royalties.** **Art. 375 puts periodic, self-renewing dues — royalties among them — at 5 years**, and the right **renews silently year after year** (§9.6). A freelancer's uncollected invoices from 2020 may already be gone.
7. **Assuming prescription applies automatically.** **Civil Code Art. 387: the court may not apply prescription of its own motion.** On the defence side, plead it; on the claim side, do not assume the other side knows (§9.6).
8. **Quoting a fee without a date, or quoting the table figure as the total.** Every EGIPA annex is expressly **"in addition to the fees imposed by law and the stamp dues"**, the statutory fees are the **2003/2005** schedules, and the **2026 top-up is alert-sourced** (§10). **Give the client a range, the layers, and the date.**
9. **Treating the renewal grace period as a fee problem.** **Art. 90: if the mark is not renewed, «the Department shall proceed to cancel the said mark from the register»**, and re-registration within 3 years is a **privilege in favour of the former owner only** (Art. 92) (§3.7, §3.9). **Six months of grace, not indefinitely.**
10. **Selling a trade secret as if it were a patent.** **Reverse engineering from products in circulation is expressly lawful (Art. 59(2))**, and protection ends the moment the information stops being undisclosed (Arts. 55, 57). If the client's secret is visible in the product, **the trade secret is the wrong instrument** (§8.1).
11. **Getting the patent and utility-model terms wrong.** **Patent: 20 years from the date of filing in Egypt (Art. 9). Utility model: 7 years from filing, non-renewable (Art. 30).** Both, plus the **annuity trap** — the progressive annual fee with a **7% surcharge per year of delay** and lapse for non-payment (§4.4, §10.3(a)).
12. **Repeating the two big whoppers.** **(a)** that the **2026 IP bill is law** (it is not, as far as I could establish — §1.4); and **(b)** that **ITIDA provides a free-zone/export IP exemption** (the real relief is the **Export-IT cash rebate** and **Investment Law 72/2017** — §7.3). Both are stated confidently all over the internet, and both are wrong.

---

*File compiled and written **2026-10-19**. Primary Arabic text: the **Court of Cassation Information Centre consolidated** Law 82/2002 (amendment footnotes read in full). Primary English text: the **WIPO Lex** 2002-version translation — ⚠️ **WIPO's own caveat applies: "Current text in English unavailable. 2002 version provided for reference purposes"**, so English quotations are used for **Books One and Two** (never amended) and **checked against the Arabic** for Book Three. Executive regulations read in locally extracted English (1366/2003, 497/2005) and Arabic. Economic Courts: Laws 120/2008, 146/2019 and the **156/2024 gazette page scan**. Fees: **EGIPA Decisions 84, 138, 139, 140 and 141 of 2025 read off page scans** (the PDFs are image-only; OCR was unusable for Arabic-Indic digits, so the pages were rendered and read visually). Customs: the **Egyptian Customs Authority's April 2026 IPR booklet**. PCT: the **WIPO PCT Applicant's Guide — Egypt, updated to 1 September 2026**. **Companion files:** `01-commercial-corporate-contract.md` (§7 IPR — its seven open items are closed here; its treaty table is **not** restated), `05-tenancy-egypt.md` (the format this file follows), `06`/`07` where they cover IP-adjacent subjects. **Article numbers without a source are not asserted anywhere in this file.***