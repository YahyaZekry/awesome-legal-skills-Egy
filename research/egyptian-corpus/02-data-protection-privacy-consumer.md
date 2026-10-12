# Egypt — Data Protection / Privacy / IT / E-Commerce / Consumer Law

**Scope of this file:** personal data protection, telecom secrecy, e-signatures / online contracting, and consumer protection (incl. distance selling) of the Arab Republic of Egypt.

**Verification legend**

| Tag | Meaning |
|---|---|
| ✅ VERIFIED | Seen in a retrieved primary or near-primary source (Official Gazette reproduction, government portal, or regulator's own publication). |
| ⚠️ PARTIAL | Verified in a reputable secondary source (law-firm alert / academic source) but not confirmed against the Arabic Official Gazette text. |
| ❌ UNVERIFIED — needs primary-source check | Asserted somewhere but not confirmed in any retrieved source, or sources conflict. Do not cite without checking. |

**Two corrections to the commissioning brief** (important for citation accuracy):

1. The Egyptian data-protection regulator is the **Personal Data Protection *Center* (PDPC) — مركز حماية البيانات الشخصية**, *not* a "Data Protection **Authority** (جهاز حماية البيانات الشخصية)". Its official website is `pdpc.gov.eg` / `portal.pdpc.gov.eg` and it self-describes as "Personal Data Protection Center". There is no verified instrument converting it into a "هيئة" (Authority). **Treat "جهاز حماية البيانات الشخصية" as unverified naming.**
2. Egypt's e-signature statute is **Law No. 15 of 2004**, not Law 15 of 2020. **Law 15 of 2020 does not exist in Egypt's e-signature context** and should not be cited. (Law 15/2020 is the Saudi Arabian E-Commerce Law — an easy cross-jurisdiction confusion trap.)

---

## 1. Personal Data Protection Law No. 151 of 2020

### Personal Data Protection Law No. 151 of 2020 (قانون حماية البيانات الشخصية)

- **Citation:** Law No. 151 of 2020 promulgating the Personal Data Protection Law (قانون رقم ١٥١ لسنة ٢٠٢٠ بإصدار قانون حماية البيانات الشخصية).
- **Issuing authority / promulgating date:** Passed by the House of Representatives; promulgated at the Presidency of the Republic on **13 July 2020** (22 Dhu al-Qi'dah 1441 AH), signed by Abdel Fattah El-Sisi. ✅ VERIFIED (promulgation date appears in the enacting formula of the law text itself).
- **Gazette / entry into force:** Published in the Official Gazette (الوقائع المصرية) on **15 July 2020**; entered into force **15 October 2020**. Issuance Art. 7 provides the law comes into force "after three months have elapsed from the day following the date of its publication." ⚠️ PARTIAL — the 15 July 2020 publication date and 15 October 2020 commencement are from DataGuidance and the Global Compliance News "Egypt issues new data protection law" alert; I did **not** see the gazite masthead. Verify the gazette issue number and date before citing them in a filing.
- **Structural note (critical for citation):** Law 151/2020 has **two parts**:
  - **Issuance Articles (مواد الإصدار)** — Arts. 1–7. Art. 1 = scope, Art. 2 = penal-code reach, Art. 3 = exclusions, Art. 4 = obligation to issue Executive Regulations within 6 months, Art. 5 = Economic Courts jurisdiction, Art. 6 = 1-year compliance window after the Executive Regulations, Art. 7 = publication + commencement.
  - **Attached Law (قانون حماية البيانات الشخصية المرافق)** — Arts. 1–49. Art. 1 = definitions; Arts. 2–18 = substantive rules; Arts. 19–25 = the Center; Arts. 26–30 = licensing and sanctions; Art. 31 = budget; Arts. 32–33 = requests & complaints; Art. 34 = enforcement officers; Arts. 35–49 = offences, penalties, reconciliation.
  - Always disambiguate: "Law 151/2020, Attached Law Art. 6" ≠ "Law 151/2020 Art. 6."
- **Status:** In force. ✅ VERIFIED

#### Territorial / personal scope

- Applies to the protection of personal data relating to natural persons **processed electronically, wholly or partly, by any Holder, Controller or Processor** (Issuance Art. 1). ✅
- There is **no GDPR-style Article 3 "offering of goods/services / monitoring of behaviour" territorial clause.** ⚠️ Flag this to GDPR-trained users.
- Extraterritorial reach is limited and operates only through criminal jurisdiction: the Attached Law's offences apply to (a) Egyptian nationals inside or outside Egypt, (b) non-Egyptians resident in Egypt, and (c) non-Egyptians **outside** Egypt where the act is punishable where it occurred and the data relate to **Egyptians or residents of Egypt** (Issuance Art. 2). ✅
- Exclusions (Issuance Art. 3): purely personal/household use; official statistics or statutory-application processing; exclusively media-purpose processing (if accurate and not reused, without prejudice to press law); judicial enforcement records, investigations and court proceedings; data held by **National Security Authorities** and other data those authorities designate; and data held by the **Central Bank of Egypt** and entities under its control/supervision — **except money-transfer companies and foreign-exchange companies**, for which CBE data-handling rules apply. ✅
- **National security back door (flagged by civil society):** per Issuance Art. 3(5), at the request of the National Security Authorities the Center **must** notify the controller/processor to modify, erase, or not display/make available/circulate personal data within a specified period on national-security grounds, and the controller/processor must comply. ✅ (text) — Access Now has published critical commentary on this ("Egypt's new data protection law: data protection or data control?").

#### Definitions (Attached Law Art. 1) ✅ VERIFIED

| Term | Arabic | Substance |
|---|---|---|
| Personal Data | البيانات الشخصية | Data on an identified or identifiable natural person (directly or indirectly by linkage), incl. name, voice, image, ID number, online identifier, and data revealing psychological, health, economic, cultural or social identity. |
| Processing | المعالجة | Any electronic/technical operation: writing, collecting, recording, keeping, storing, combining, displaying, sending, receiving, circulating, publishing, erasing, changing, modifying, retrieving or analysing — wholly or partly. |
| Sensitive Personal Data | البيانات الشخصية الحساسة | Data disclosing psychological, mental, physical or genetic health; biometric measurements; financial data; religious beliefs; political opinions; security status. **"In all cases, children's data are considered Sensitive Personal Data."** |
| Data Subject | الشخص المعنى بالبيانات | The natural person to whom electronically processed personal data are attributed. |
| **Holder** | **الحائز** | **Egypt-specific third actor:** any natural/legal person who in law or fact possesses and retains personal data in any form or on any medium, whether they created it or came into possession of it. |
| Controller | المتحكم | Person who, by virtue of their work/activity, has the right to obtain personal data and determine the method, manner and criteria for retaining/processing them and exercising control, per the specified purpose or activity. |
| Processor | المعالج | Person who, by nature of their work, specialises in processing personal data for their own benefit or for a controller under agreement and per that controller's instructions. |
| Making Data Available | إتاحة البيانات | Any means by which another person becomes aware of the data (viewing, circulation, publication, transfer, use, display, sending, receipt, disclosure). |
| Data Security | تأمين البيانات | Technical/organisational procedures preserving privacy, confidentiality, integrity, unity and inter-linkage. |
| Breach / Violation | خرق أو انتهاك | Unauthorised entry/unlawful access, or unlawful copying, sending, distribution, exchange, transfer or circulation intended to reveal/destroy/modify data. |
| Cross-Border Movement | نقل البيانات الشخصية عبر الحدود | Any transfer/making available/recording/storing/circulating/publishing/using/displaying/sending/receiving/retrieving/processing of personal data from inside Egypt to outside, **or vice versa**. |
| Electronic Marketing | التسويق الإلكتروني | Sending by any technical means of any message/advertising/marketing content intended directly or indirectly to promote goods/services or commercial, political, social or charitable solicitations to particular persons. |
| National Security Authorities | جهات الأمن القومي | Presidency, Ministry of Defence, Ministry of Interior, General Intelligence Service, Administrative Control Authority. |
| Center | المركز | The Personal Data Protection Center. |
| **Licence** | **الترخيص** | Official document to a **legal person** to collect/store/transfer/process personal data and/or conduct Electronic Marketing; **3 years, renewable**. |
| **Permit** | **التصريح** | Official document to a natural **or** legal person for the same activities, or for specified tasks; **temporary, ≤ 1 year, renewable more than once**. |
| **Accreditation** | **الاعتماد** | Certificate that a natural or legal person meets the technical, legal and organisational requirements to provide data-protection consultancy. |
| Competent Minister | الوزير المختص | The Minister responsible for communications and information technology (i.e. the MCIT Minister). |

#### Lawful bases of processing (Attached Law Art. 6) ✅ VERIFIED

Electronic processing is legitimate and lawful if **any one** applies:

1. the Data Subject consents for one or more specified purposes;
2. processing is necessary and indispensable for performance of a contractual obligation or legal act, for the conclusion of a contract for the Data Subject's benefit, or for taking any step to assert or defend the Data Subject's legal rights;
3. processing is undertaken to perform an obligation regulated by law, comply with an order of the competent investigating authorities, or give effect to a court judgment;
4. it enables the Controller to perform its obligations or a person with standing to exercise legitimate rights, **unless this conflicts with the Data Subject's fundamental rights and freedoms**.

Note: the statute lists **four** grounds. The PDPC's *Lawful Basis* guideline is reported to express them as **six** (adding "claim or defence of a legal right" and "compliance with court or regulatory orders" as separate bases). ⚠️ Cite the statutory four; describe the guideline's six only as guidance.

Consent caveat: Issuance/Attached Law Art. 2 opens with a **consent-first default** — personal data must not be collected, processed, disclosed or divulged by any means without the Data Subject's express consent, **except where authorised by law**. Art. 6 then adds non-consent grounds.

#### Data subject rights (Attached Law Art. 2) ✅ VERIFIED

1. to be informed of the personal data relating to them held by any Holder, Controller or Processor, to inspect them, and to access or obtain them;
2. to withdraw prior consent to retention or processing;
3. to have data corrected, modified, erased, supplemented or updated;
4. to have processing limited to a specified scope;
5. to be informed of any breach or violation affecting their data; and
6. to object to processing or its results where they conflict with the Data Subject's fundamental rights and freedoms.

**No express right to portability** — there is no data-portability right in Law 151/2020 or Decision 816/2025. Flag this for GDPR-trained users.

**Fees:** except for right (5), the Data Subject must **pay** the cost of the service provided in connection with exercising these rights; the Center sets the amount by decision and it **must not exceed EGP 20,000** (Attached Law Art. 2, final paragraph). ⚠️ Note this is a legal barrier, not a formality — the PDPC fee decision itself is UNVERIFIED (not located).

#### Conditions for collection/processing (Attached Law Art. 3) ✅
Lawful, specified purposes made known to the Data Subject; accuracy, soundness and security; processing appropriate to the collection purpose; and **no retention longer than necessary** to fulfil the specified purpose.

#### Controller obligations (Attached Law Art. 4) ✅ — 12 items
Obtain data from the Holder or competent entities after consent or statutory authority; ensure accuracy; establish processing method/manner/standards unless delegated to a Processor **under written contract**; ensure processing is consistent with the specified purpose; **no making available except as authorised by law**; take all technical and organisational security measures; **erase immediately on expiry of the specified purpose** (and if retained for a lawful reason thereafter, must not remain in an identifiable form); correct errors immediately on notice/knowledge; maintain a **dedicated data record** (categories, recipients, legal basis, periods/restrictions/scope, erasure/modification mechanisms, cross-border transfer info, TOMs description); **obtain a Licence or Permit from the Center**; **if outside Egypt, appoint a representative in Egypt**; provide facilities to demonstrate compliance and permit Center inspections.

#### Processor obligations (Attached Law Art. 5) ✅ — 12 items
Process per written instructions from the Center/controller/entitled person on scope, subject matter, nature, data type and consistency with the specified purpose; legitimacy and no public-order/morals breach; **do not exceed the specified purpose or duration**, and notify the necessary processing period; erase on expiry or deliver to the controller; no making available except as authorised; no processing inconsistent with the controller's purpose/activity unless for **statistical or educational, non-profit** purposes that do not infringe private life; protect the processing operation, media and devices; no direct or indirect harm to the Data Subject; maintain a **processing-operations record**; provide compliance facilities and permit inspections; **obtain a Licence or Permit**; **appoint an Egyptian representative if based abroad**.

#### Data Protection Officer (Attached Law Arts. 8–9, 13) ✅
- A register of DPOs is established **at the Center**; the Executive Regulations set registration conditions. The legal representative of a legal-person Controller/Processor **must appoint a specialised employee inside its own organisational and staffing structure**, register that employee in the Center's register, and **publicly announce the appointment**.
- A Controller/Processor that is a **natural person** is itself responsible for applying the Law (no mandatory DPO).
- DPO duties (Art. 9, 8 items): implement the Law, its Executive Regulations and the Center's decisions; periodically assess and examine protection systems, document results, issue recommendations; act as direct contact with the Center and implement its decisions; enable Data Subjects to exercise rights; notify the Center of any breach/violation; respond to Data Subject requests and to Center complaints; monitor entries/updates in the controller's record or processor's processing record; remedy internal violations and take corrective measures; organise employee training.
- Art. 13: the DPO and staff under the officer must fully comply with security policies preventing breach of sensitive data.

#### Making data available / digital evidence (Attached Law Arts. 10–11) ✅
- Art. 10: act only on a **written** request from a person entitled or on a legal basis; verify and retain supporting documents; decide **within six working days** of submission; a rejection must state reasons; **silence = deemed rejection**.
- Art. 11: digital evidence derived from personal data has the **same probative force as evidence derived from written data**, subject to technical standards in the Executive Regulations (detailed in Decision 816/2025 Art. 13 — see §2).

#### Sensitive personal data (Attached Law Art. 12) ✅
A Controller or Processor (natural or legal) **must not collect, transfer, store, keep, process or make available sensitive personal data except under a Licence issued by the Center**. Outside cases authorised by law, the Data Subject's **express written consent** is required. Where the operations concern **children's data, the guardian's consent** is required. A child's participation in a game, competition or any other activity **must not be conditional** on providing data beyond what is necessary for that participation.

#### Cross-border (Attached Law Arts. 14–16) ✅
- Art. 14: data collected or prepared for processing **must not be transferred to, stored or shared in a foreign State** unless a level of protection **no lower than** that under the Law is available **and a Licence or Permit has been obtained from the Center**.
- Art. 15: exception where the express consent of the Data Subject (or representative) is obtained, in seven cases — (1) preserving the life of the Data Subject and providing medical care/treatment/health-service management; (2) performing obligations to establish, exercise before judicial authorities, or defend a right; (3) conclusion, performance or future conclusion of a contract between the processor and a third party for the Data Subject's benefit; (4) international judicial cooperation procedures; (5) necessary or legally obligatory protection of the public interest; (6) money transfers to another State per that State's applicable legislation; (7) transfer/circulation under a bilateral or multilateral international agreement to which Egypt is party.
- Art. 16: making personal data available to a controller/processor **outside Egypt** under a **Centre Licence** requires all three of — (1) compatible activity or identical purpose; (2) legitimate interest of each controller/processor **or of the Data Subject**; (3) level of legal and technical protection abroad **no lower than** in Egypt.

#### Direct electronic marketing (Attached Law Arts. 17–18) ✅
- Art. 17: an electronic communication for direct marketing must not be made unless — (1) consent obtained; (2) the communication identifies its originator and sender; (3) the sender has a valid, sufficient, reachable address; (4) the communication indicates it is for direct-marketing purposes; (5) clear and accessible mechanisms let the Data Subject reject the communication or withdraw consent.
- Art. 18: the sender must adhere to the specified marketing purpose; **must not disclose the Data Subject's contact details**; and must retain, **for three years from the date of the last transmission**, electronic records evidencing consent and amendments, **or** the Data Subject's absence of objection to continued receipt.

#### Localisation
There is **no data-localisation / data-residency requirement** in Law 151/2020 or Decision 816/2025. Instead:
- Outbound transfers require a **separate cross-border Licence or Permit** from the Center (Reg. Arts. 16, 23–27) plus, as a rule, the Data Subject's consent (Reg. Art. 16(1)(2));
- foreign controllers/processors without an Egyptian branch or representative office must appoint an **Egyptian representative approved by the Center** (Reg. Arts. 3(6), 4(5)); and
- visual-surveillance recordings captured in public places **must not be transferred/made available/recorded/processed outside Egypt** except for legally prescribed reasons (Reg. Art. 31(1)(3)).

#### Personal Data Protection Center (PDPC) — مركز حماية البيانات الشخصية

- **Legal form:** a **public economic authority** (هيئة عامة اقتصادية) with legal personality, **subordinate to the Competent Minister (MCIT)**; principal office in Cairo Governorate or a neighbouring governorate (Attached Law Art. 19). ✅
- **Board of Directors (Art. 20)** chaired by the Competent Minister, members: representatives of the Ministry of Defence, Ministry of Interior, General Intelligence Service, Administrative Control Authority, ITIDA, NTRA; the Center's CEO; and three persons with expertise appointed by the Competent Minister. Three-year terms, renewable. ✅
- **CEO (Art. 23):** appointed by **Prime Minister** decision on the Competent Minister's proposal; **4-year term, renewable once**. ✅
- **Board decision threshold:** meets at least monthly; quorum = majority; decisions by **two-thirds majority of members present** (Art. 22). ✅
- **Mandate (Art. 19)** — 17 enumerated powers including: policy/strategic plans; decisions, controls, measures, procedures and standards; approving a **codes-of-conduct** framework; issuing Licences/Permits/Accreditations; receiving complaints and issuing decisions on them; **expressing an opinion on draft laws and international agreements** relating to personal data; **monitoring and inspecting** persons subject to the Law; **verifying conditions governing cross-border movement and issuing decisions regulating it**; international cooperation/MoUs; and publishing an **annual report**. ✅
- **Budget (Art. 31):** separate budget following the Unified Accounting System but "not subject to governmental rules and systems"; **not less than one-third of the proceeds of fines** imposed by a court under the Law is allocated from the Public Treasury; plus licence/permit/accreditation fees, service charges, ITIDA budget allocations, investment returns and grants. ✅
- **Enforcement:** Center employees designated by decision of the **Minister of Justice** on the Competent Minister's proposal have **judicial-enforcement-officer status** (Attached Law Art. 34; reinforced in Reg. Arts. 3(7) and 4(4)). ✅
- **Administrative sanctions (Attached Law Art. 30)** — two-stage: first the **CEO** issues a written warning to cease and remove the causes/effects within a specified period; on non-compliance the **Board** may, by reasoned decision: (1) warn that the Licence/Permit/Accreditation may be suspended; (2) suspend it in whole or part; (3) withdraw or cancel it; (4) **publish** the established contraventions at the offender's expense in widely circulated media; or (5) place the Controller/Processor under the Center's **technical supervision** at the Controller's expense. ✅
- **Licence cancellation (Art. 29):** breach of conditions; failure to pay renewal fees; repeated failure to comply with Center decisions; assignment to a third party without approval; or a judgment declaring the Controller/Processor bankrupt. ✅
- **Official website:** `https://pdpc.gov.eg` → `https://portal.pdpc.gov.eg` ✅ (site is a JS SPA; direct PDF links of the form `pdpc.gov.eg/assets/pdf-data/...` observed in the wild now resolve to the SPA shell, not the PDF — verify links before citing them.)
- **⚠️ Naming caution:** several secondary sources (DLA Piper, TrustArc, DataGuidance, Kennedys) call the body a "Personal Data Protection Authority" / "Data Protection Authority" and refer to "PDPA". The statute and the regulator's own website say **Center / PDPC**. Cite "Personal Data Protection Center (PDPC)".

#### Licence/Permit framework (Attached Law Arts. 26–27) ✅
- Eight categories the Center issues: (1) classification of Licences/Permits/Accreditations; (2) Controller/Processor operation licences or permits; (3) **direct Electronic Marketing** licences/permits; (4) licences/permits for associations, unions and clubs processing member data; (5) licences/permits for **visual-surveillance methods in public places**; (6) licences/permits for controlling and processing **sensitive** personal data; (7) permits and accreditations for data-protection consultancy; (8) **cross-border transfer** licences and permits.
- **Fee caps:** Licence fee **must not exceed EGP 2,000,000**; Permit or Accreditation fee **must not exceed EGP 500,000**.
- **Applications (Art. 27):** decided within **ninety days** from the date all required documents/information were provided — **otherwise the application is deemed refused**. The Center may demand additional safeguards if the described protection proves insufficient. A Controller/Processor may hold more than one Licence or Permit depending on the type of personal data handled.

#### Requests and complaints (Attached Law Arts. 32–33) ✅
- **Request:** the Data Subject or any person with standing may submit a request to any Holder, Controller or Processor; the recipient **must respond within six working days**.
- **Complaint:** available where there is a violation/impairment of the right to protection, refusal to enable rights to be exercised, or a DPO decision. The Center may take any investigative measures and **must decide within thirty working days**. The respondent must implement the Center's decision **within seven working days** and report the steps taken. Court recourse is preserved.

#### Penalties — Law No. 151/2020 (Attached Law Arts. 35–49) ✅ VERIFIED, amounts as enacted

| Art. | Offence | Penalty |
|---|---|---|
| 36(1) | Holder/Controller/Processor collects, processes, divulges, makes available or circulates electronically processed personal data otherwise than as authorised by law or without consent | Fine **EGP 100,000 – 1,000,000** |
| 36(2) | Same, done for material or non-material benefit, or intending to expose the Data Subject to danger/harm | Imprisonment **≥ 6 months** + fine **EGP 200,000 – 2,000,000**, or either |
| 37(1) | Unjustified refusal to enable the Data Subject to exercise the Art. 2 rights | Fine **EGP 100,000 – 1,000,000** |
| 37(2) | Collecting personal data where the Art. 3 conditions are not met | Fine **EGP 200,000 – 2,000,000** |
| 38 | Controller/Processor failing to comply with Arts. 4, 5 or 7 duties | Fine **EGP 300,000 – 3,000,000** |
| 39 | Legal representative failing to comply with an Art. 8 duty (DPO appointment/registration/announcement) | Fine **EGP 200,000 – 2,000,000** |
| 40(1) | DPO failing to comply with Art. 9 role requirements | Fine **EGP 200,000 – 2,000,000** |
| 40(2) | Same, by negligence of the DPO | Fine **EGP 50,000 – 500,000** |
| 41 | Sensitive personal data collected/made available/circulated/processed/divulged/stored/transferred/kept without consent or in unauthorised circumstances | Imprisonment **≥ 3 months** + fine **EGP 500,000 – 5,000,000**, or either |
| 42 | Contravention of cross-border Arts. 14, 15, 16 | Imprisonment **≥ 3 months** + fine **EGP 500,000 – 5,000,000**, or either |
| 43 | Contravention of electronic-marketing Arts. 17–18 | Fine **EGP 200,000 – 2,000,000** |
| 44 | Center Board member or employee breaching the Art. 24 confidentiality duty | Fine **EGP 300,000 – 3,000,000** |
| 45 | Contravention of the Law's Licences/Permits/Accreditations provisions | Fine **EGP 500,000 – 5,000,000** |
| 46 | Preventing a Center employee with judicial-enforcement status from performing duties | Imprisonment **≥ 6 months** + fine **EGP 200,000 – 2,000,000**, or either |
| 47 | Person actually managing a legal person that contravened the Law, where they knew and managerial default contributed | **Same penalties** as the underlying offence; the legal person is **jointly and severally liable** for compensation |
| 48 | General | Court **must** order publication of the conviction in **two widely circulated newspapers and on open electronic information networks**, at the offender's expense. **Recidivism doubles both the minimum and maximum limits. Attempt = half the prescribed penalty.** |
| 49 | Reconciliation | Before proceedings: **half the minimum fine**. After proceedings and before final judgment: **half the maximum fine or the fine imposed, whichever is greater.** Settlement available with the **victim** (for Arts. 36–41, 43) and with the **Center** (for Arts. 42, 44, 45). Settlement ends the criminal proceedings without affecting the harmed party's rights. |
| 5 (Issuance) | **Jurisdiction:** the **Economic Courts** hear offences under the Attached Law | — |

**Currency note:** all amounts are the **Egyptian pounds (EGP) figures as enacted in 2020** and are **not** indexed. They have not been re-denominated. Do not compare them to GDPR fines without stating they are from 2020 and mostly in the EGP 100k–5m band.

- **Amendments:** **None located.** ❌/⚠️ I found no amending instrument to Law 151/2020 as of 2026-10-12. Treat as unamended but re-verify.
- **Sources:**
  - Unofficial English translation, Youssry Saleh & Partners (17 Aug 2026): `https://youssrysaleh.com/ysp_upload/2026/08/Law-No.-151-of-2020-Unofficial-English-Translation-YSP.pdf` (human-readable page: `https://youssrysaleh.com/en/egypts-personal-data-protection-law-pdpl-english-translation/`)
  - Unofficial English translation, ACC program materials: `https://www.acc.com/sites/default/files/program-materials/upload/Data%20Protection%20Law%20-%20Egypt%20-%20EN%20-%20MBH.PDF`
  - MCIT-hosted Arabic PDF of the Law: `https://mcit.gov.eg/Upcont/Documents/Reports%20and%20Documents_1232021000_Law_No_151_2020_Personal_Data_Protection.pdf`
  - Arabic text mirror (Privacy Laws & Business): `https://www.privacylaws.com/media/3263/egypt-data-protection-law-151-of-2020.pdf`
  - Global Compliance News (gazette date + commencement): `https://www.globalcompliancenews.com/2020/11/08/egypt-and-united-arab-emirates-egypt-issues-new-data-protection-law28092020/`
  - DataGuidance jurisdiction profile: `https://www.dataguidance.com/jurisdictions/egypt`
  - DLA Piper Egypt laws: `https://www.dlapiperdataprotection.com/?t=law&c=EG`
  - Access Now critique: `https://www.accessnow.org/egypts-new-data-protection-law-data-protection-or-data-control/`
- **As of:** 2026-10-12

---

## 2. Executive Regulations of Law 151/2020 — MCIT Ministerial Decision No. 816 of 2025 ⭐ HIGH PRIORITY

### Executive Regulations of the Personal Data Protection Law (اللائحة التنفيذية لقانون حماية البيانات الشخصية) — issued by Ministerial Decision No. 816 of 2025 (قرار وزير الاتصالات وتكنولوجيا المعلومات رقم ٨١٦ لسنة ٢٠٢٥)

**Your lead is CONFIRMED, with one correction and one caution.**

| Fact | Finding | Confidence |
|---|---|---|
| Issuing instrument | **قرار وزير الاتصالات وتكنولوجيا المعلومات رقم ٨١٦ لسنة ٢٠٢٥** — a decision of the **Minister** of Communications and Information Technology. **NOT** a Prime Ministerial decree. (Several English sources — Kennedys, LinkedIn reposts — wrongly call it a "Prime Ministerial Decree No. 816." Do not repeat that error.) | ✅ VERIFIED from the Arabic enacting text and the English translation's gazite masthead |
| Signed by | **Dr. Amr Samih Talaat / عمرو سميح طلعت**, Minister of Communications and Information Technology | ✅ VERIFIED (Arabic text signature block; English translation "Dr. Amr Talaat") |
| **Gazette publication** | **Al-Waqa'i' al-Misriyya (الوقائع المصرية), Supplement to the Official Gazette, Issue No. 244 (Supplement A)** — corresponding to **1 November 2025** (10 Jumada al-Awwal 1447 AH) | ✅ VERIFIED — reproduced in the English translation header, and corroborated by the Arabic transcription on `alhasswalawfirm.com` ("الوقائع المصرية - العدد ٢٤٤ تابع (أ) فى أول نوفمبر سنة ٢٠٢٥") and eastlaws |
| **Entry into force** | **2 November 2025.** Decision Art. 2: "This Decree shall be published in Al-Waqa'i' al-Misriyya and shall come into force on the day following its publication." (2 Nov 2025 = day after 1 Nov 2025.) Eastlaws metadata states the same: "نشر بتاريخ 01/11/2025 … يعمل به إعتباراً من 02/11/2025" | ✅ VERIFIED |
| **Compliance deadline** | **1 November 2026** — Law 151/2020 Issuance Art. 6 gives every person subject to the Law **one year from the date the Executive Regulations were issued** to bring its affairs into compliance. (DataGuidance phrases it as 31 Oct 2026; Shand Partners as 1 Nov 2026. Substantively identical.) | ✅ VERIFIED |
| Structure | Decree has **2 articles** + attached Executive Regulations of **41 articles** = 43 articles in total | ✅ VERIFIED |
| Legal basis in the preamble | Constitution; Penal Code; Civil Code; Criminal Procedure Code; Decree-Law 96/1952 (expert evidence); Law 13/1968 (Civil & Commercial Procedures); Law 25/1968 (Evidence); Law 34/1976 (Commercial Register); Law 159/1981 (Companies); **Law 12/1996 (Child Law)**; Law 17/1999 (Commercial Code); Law 82/2002 (IP); **Law 10/2003 (Telecom)**; **Law 15/2004 (E-Signature / ITIDA)**; Law 3/2005 (Competition); Law 87/2018 (Road passenger transport via IT); **Law 175/2018 (Cybercrime)**; **Law 181/2018 (Consumer Protection)**; **Law 194/2020 (CBE and Banking)**; opinion of the State Council | ✅ VERIFIED |
| Was there an earlier Executive Regulations? | **No.** Law 151/2020 Issuance Art. 4 required the Competent Minister to issue the Executive Regulations within 6 months of the Law's commencement (i.e. by ~15 April 2021). For ~4½ years none existed; the regime was inoperative for want of a licensing body, DPO register and technical standards. Decision 816/2025 is the **first and only** Executive Regulations. ❌ I found **no** separately gazetted draft or interim version. | ✅ VERIFIED in substance (absence of earlier instrument); ⚠️ if you need to assert "no draft ever existed", check the PDPC consultation record |

#### ⚠️ The "25 December 2025" trap

Several widely-cited secondary sources — DataGuidance, AmCham Egypt, ADSERO, and a Heba Tawadross LinkedIn repost — state the Executive Regulations were **issued on 25 December 2025** and that the Law "came into force" on that date. **This is wrong.** Shand & Partners (11 Jan 2026) explains the origin of the error: the copy of the Regulations handed to Egyptian law firms bears the publication date of **1 November 2025**, but that copy **was made available to law firms on 25 December 2025**; there is no official explanation for that practice. The gazette publication date remains **1 November 2025** and entry into force **2 November 2025**. **Cite 1 Nov / 2 Nov 2025.**

#### New substantive obligations introduced by Decision 816/2025

These go far beyond the Law and are the reason the regime is now operational:

1. **Licensing is now a precondition of almost any processing.** Controllers **and** processors must hold a Centre Licence or Permit *before* handling personal data (Arts. 2(1), 3(1), 4(1)). Continuous/permanent activity → Licence; defined purpose, limited duration → Permit (≤ 1 year, Reg. Art. 20).
2. **A quantified, record-volume-based fee schedule** (Arts. 19, 20). See fee tables below.
3. **The DPO is now registered, coded, exam-tested and categorised** (Arts. 7–12): qualifications + practical experience per Board standards; **must pass Centre-approved examinations**; **no prior conviction of crimes against honour or trust**; a unique "Personal Data Protection Officer Code" linked to the volume and nature of data the officer may handle; **30 working days** to decide registration; replacement appointments notified **≥ 15 days** in advance; a temporary replacement officer files a report within 15 days of assuming duties; a DPO may serve multiple entities only with entity consent **and** Centre approval (shared DPOs for structurally linked entities permitted with notification); an **annual report** on the state of privacy protection goes to the Centre.
4. **Breach notification is now operationalised** (Arts. 5–6): notify via the Centre's **electronic portal or hotline within 72 hours of awareness**; log in a secure electronic register with six prescribed content items; **if the breach relates to national-security considerations, notify immediately** and add security-linkage and volume/damage items; **notify the Data Subject within 3 working days of the Centre report**, using the channel (SMS / email / phone) specified at the time of consent collection; the Centre must run a **dedicated channel for national-security reports**, coordinate with National Security Authorities, and periodically train DPOs on breach classification.
5. **Cross-border transfers require a separate authorisation plus, as a rule, consent** (Arts. 16–17, 23–27): licence/permit after the Centre assesses destination-country adequacy; Data Subject consent; safeguards throughout the transfer lifecycle; the licence is **destination-specific** and must be updated if a new country is added; the Centre may authorise a non-adequate destination where it meets the same statutory criteria; a **separate licence/permit** is required to make data available to a foreign controller/processor (Art. 17), subject to compatible/integrated activity, legitimate interest, and protection no lower than Egypt's.
6. **Direct electronic marketing is a standalone licensed regime** (Arts. 18, 28–30): Centre Licence required; **explicit** consent; the opening of the communication must identify the recipient and state the marketing purpose and give a reject/withdraw mechanism; data must be **erased** on withdrawal of consent or on expiry of retention/the marketing purpose; marketing intermediaries must verify and retain the provenance of consent or stop using the data immediately; records of consent must be producible to the Centre; the Centre maintains a public complaints channel for e-marketing. Fees: **10%** of the controller/processor fee (own goods/services) and **25%** (third-party marketing).
7. **Visual surveillance in public places is licensed** (Art. 31): prior permits from the competent authorities; **visible notice**; **no transfer/availability/recording/processing outside Egypt** except for legal reasons; **no processing to identify individuals from images/video via facial recognition or similar technologies** except as legally provided or on the Data Subject's **explicit** consent; secrecy duties on staff; Centre inspection rights. Fees: **EGP 1,000 per 3 years** (Licence) / **EGP 500 per year** (Permit). Cameras at private residences are exempt provided they do not exceed the spatial limits of the residence.
8. **Children's data rules** (Art. 15): **under 15** — explicit written consent (paper or electronic) from the **legal guardian**, stating its time scope, before collection, for a service or any purpose, without prejudice to the guardian's right to withdraw or amend; **15–18** — the child or the guardian consents as applicable, by mechanisms the Centre determines. Art. 14(5) also bars **profiling/tracking/monitoring children's behaviour** where a child participates in a game, competition or other activity, and limits collection to what is necessary for that participation.
9. **Digital-evidence admissibility criteria** (Art. 13) — four cumulative technical/evidentiary conditions: non-destructive collection/extraction; relevance to the matter and within the investigating authority's/court's mandate; collection/extraction/preservation by authorised judicial enforcement officers or experts with full tool specification; and pre-examination documentation of the process. ✅ (Mirrors Attached Law Art. 11.)
10. **AI and emerging technology** (Art. 4(7)): a **Processor** handling personal data for the purpose of **artificial-intelligence training** and emerging/innovative technologies must follow recognised local, regional and international principles ensuring such technologies are used so as not to cause harm to the Data Subject. ⚠️ This is a principles-based obligation with no numbers or standards attached in the Regulation itself.
11. **Sector-data discipline** (Arts. 3(8), 4(8)): the controller/processor must limit itself to the volume and type of personal data its own sectoral law lets it obtain; where the sectoral law is silent on retention/security/transfer rules, the PDPL and these Regulations apply to the additional data requested.
12. **Statutory/educational secondary use by processors** (Art. 4(6)) is permitted only non-profit, with consent, subject relevance, and **encoding** of any circulated data so the Data Subject cannot be inferred.
13. **Accredited data-protection consultancy** (Arts. 32–34): accreditation certificate for natural persons (qualifications/experience + exam + no honour-crime conviction) and legal persons (documented activity + experience + staff holding Centre accreditation and a valid practice permit). Fees: **EGP 5,000/year** (natural person), **EGP 50,000/year** (legal person); certificate valid **3 years**, renewable for equal periods at the same fee.
14. **Renewal mechanics** (Art. 40): licence renewal application **at least 3 months before expiry**; permit renewal application **at least 1 month before expiry**.
15. **Electronic application gateway** (Arts. 36, 38): dedicated electronic portals for legal persons and natural persons; **90 working days** from complete documentation to decide; **silence = deemed rejection**. Natural-person permits are valid **≤ 1 year**.
16. **Electronic records mandated for controllers and processors** (Arts. 2, 3, 4): secure electronic registers recording consent (date + form), data categories and scope of use, per-category retention periods, security measures (enabling Centre periodic inspection), data-subject amendment/erasure/withdrawal requests and whether they were executed and why, and — for processors — the processing contract, the Controller's DPO and legal-representative details, processing standards, and **the countries to which data is transferred with their security systems and data-flow paths**.
17. **Restoration/containment capability** (Arts. 3(2)(4), 4(2)(2)): technical and organisational measures enabling restoration of personal data, timely access, and containment on any physical or technical incident.

#### Fee schedules (verified from the Arabic text) ✅

**Reg. Art. 19 — combined Controller/Processor Licence, legal persons (annual):**

| Individual personal-data records | Annual fee |
|---|---|
| 1 – 100,000 | **Exempt** |
| 101,000 – 200,000 | EGP 200 |
| 201,000 – 300,000 | EGP 300 |
| 301,000 – 400,000 | EGP 400 |
| 401,000 – 500,000 | EGP 500 |
| 501,000 – 600,000 | EGP 600 |
| 601,000 – 700,000 | EGP 700 |
| 701,000 – 800,000 | EGP 800 |
| 801,000 – 900,000 | EGP 900 |
| 901,000 – 1,000,000 | EGP 1,000 |
| > 1m: EGP 5,000 per 100k band | up to 2,000,000 records → cap **EGP 666,666/year** (EGP 2,000,000 total over 3 years) |
| > 2m: EGP 10,000 per 100k band | up to 3,000,000 records → cap **EGP 150,000/year** |
| > 3m: EGP 15,000 per 100k band | up to 4,000,000 records → cap **EGP 300,000/year** |
| > 4m: EGP 20,000 per 100k band | up to 5,000,000 records → cap **EGP 500,000/year** |
| > 5,000,000 records | statutory maximum **EGP 666,666/year** (EGP 2,000,000 over 3 years) |

- **Controller-only or Processor-only legal person: 50%** of the above (Reg. Art. 19 final paragraph).
- **Associations / trade unions / clubs** processing member data: associations **EGP 5,000**; trade unions **EGP 10,000**; clubs with **< 50,000** member records **EGP 20,000**; clubs with **> 50,000** member records **EGP 50,000**.

**Reg. Art. 20 — Permit (specific, temporary purpose, ≤ 1 year):** fee depends on both record volume and duration (1–3 months / >3–6 / >6–9 / >9–12):

| Individual records | 1–3 months | >3–6 months | >6–9 months | >9–12 months |
|---|---|---|---|---|
| 1 – 25,000 | Exempt | Exempt | Exempt | Exempt |
| > 25,000 – 250,000 | 10,000 | 15,000 | 20,000 | 25,000 |
| > 250,000 – 500,000 | 12,500 | 25,000 | 37,500 | 50,000 |
| > 500,000 – 1,000,000 | 25,000 | 50,000 | 75,000 | 100,000 |
| > 1m – 2m | 50,000 | 100,000 | 150,000 | 200,000 |
| > 2m – 3m | 75,000 | 150,000 | 225,000 | 300,000 |
| > 3m – 4m | 100,000 | 200,000 | 300,000 | 400,000 |
| > 4m – 5m | 125,000 | 250,000 | 375,000 | 500,000 |
| > 5m | statutory maximum | | | |

Controller-only or Processor-only natural or legal person: **50%**.

**Other fees:** cross-border transfer Licence/Permit = **50%** of the controller/processor fee (Reg. Art. 27). E-marketing = **10%** (own) / **25%** (third-party) (Reg. Art. 29). CCTV = EGP 1,000/3 yrs (Licence) or EGP 500/yr (Permit) (Reg. Art. 31). Consultancy accreditation = EGP 5,000/yr or EGP 50,000/yr, 3-year validity (Reg. Art. 34).

- **Amendments:** ❌ **UNVERIFIED — needs primary-source check.** The alhasswalawfirm transcription is captioned "(محدثا حتي عام ٢٠٢٦)" ("updated until 2026"), which may indicate consolidation rather than amendment. I located no amending decision to Decision 816/2025 as of 2026-10-12.
- **Sources:**
  - **Official text on the regulator's site (Arabic PDF):** `https://pdpc.gov.eg/assets/pdf-data/Executive%20Regulation.pdf` — ⚠️ observed to resolve to the SPA shell when fetched programmatically; try in a browser.
  - Regulator portal: `https://portal.pdpc.gov.eg/` and `https://portal.pdpc.gov.eg/guidelines`
  - **Full Arabic transcription** (2 decree articles + 41 Regulation articles, gazette reference in the preamble), Atef Hassan Ali law firm library: `https://alhasswalawfirm.com/law-library/decree-816-2025`
  - Arabic full text (Masaar): `https://masaar.net/ar/egypt_laws/اللائحة-التنفيذية-لقانون-حماية-البي/` (URL-encoded form: `https://masaar.net/ar/egypt_laws/%D8%A7%D9%84%D9%84%D8%A7%D8%A6%D8%AD%D8%A9-%D8%A7%D9%84%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%D8%A9-%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%AD%D9%85%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D8%A8%D9%8A/`)
  - eastlaws record (gazette publication date + commencement date in metadata): `https://www.eastlaws.com/legislation-full-text/ar/egypt/tech-minister-decision/01-11-2025/no-816?id=5008447&type=1`
  - **English translation with gazette masthead** (Al-Waqa'i' al-Misriyya, Supplement, Issue 244 (Supplement A), 1 November 2025): `https://www.thesedonaconference.org/sites/default/files/meeting_paper/7.4%20Egypt%20Personal%20Data%20Protection%20Law%20-%20Executive%20Regulations.pdf`
  - Shand & Partners briefing (entry into force, the 25 Dec error explained, PDPC guidelines inventory): `https://www.shandpartners.com/insights/briefings/telecoms-media-technology/the-issuance-of-the-executive-regulations-of-the-data-protection-law-and-the-establishment-of-the-data-protection-centre/`
  - Al Tamimi & Company (Legal 500 Intelligence): `https://www.legal500.com/intelligence/egypt/privacy/from-policy-to-practice-egypt-issues-executive-regulations-of-the-personal-data-protection-law`
  - Kennedys (compliance deadline, consent guidelines, cross-border summary): `https://www.kennedyslaw.com/en/thought-leadership/article/2026/egypt-s-personal-data-protection-law-the-compliance-countdown-has-begun/`
  - dsn group (licensing requirement, GDPR comparison): `https://www.dsn-group.com/privacy-notes/egypts-personal-data-protection-law-before-you-process-you-need-a-licence-2860365`
  - DataGuidance: `https://www.dataguidance.com/jurisdictions/egypt`
  - CMS (Charles Russell Speech): `https://cms.law/en/int/legal-updates/egypt-s-pdpl-executive-regulations-issued-one-year-compliance-countdown-begins`
  - Arabic academic gap analysis (EKB journal): `https://jdl.journals.ekb.eg/article_503537.html`
- **As of:** 2026-10-12

---

## 3. PDPC Guidelines (non-binding but operationally important)

⚠️ **PARTIAL** — sourced from Shand & Partners' inventory and the Kennedys article; I could not enumerate the PDFs directly because `portal.pdpc.gov.eg` is a client-side-rendered app and the legacy `pdpc.gov.eg/assets/pdf-data/...` PDF URLs now resolve to the app shell.

Published guidelines reported to cover:

| Guideline | Substance |
|---|---|
| Data Subject Consent | Design of consent requests, consent management, withdrawal, record-keeping. Consent must be **in writing (paper or electronic)**; must be presented in **Arabic as the primary language**; must be **separate** from privacy notices and general T&Cs; must require a **clear affirmative action** (no implied/presumed consent). |
| Lawful Basis | Consent; contractual obligations; legal obligations; legitimate interests; claiming or defending legal rights; compliance with court or regulatory orders. Recognised exceptions to consent where there is a clear imbalance (e.g. employment) or where processing is necessary to perform a contract to which the Data Subject is party. |
| Electronic Direct Marketing | Requirements for both creators and senders; targeted, data-based messages; clear sender/purpose disclosure; effective opt-out; valid consent or permit; prompt honouring of opt-outs; accurate records; lawful use of third-party data, cookies and tracking; avoiding dark-pattern/misleading interfaces. |
| Data Protection Officer | Role, responsibilities, registration, appointment; **DPO independence** must be supported with adequate resourcing and involvement in decision-making. |
| Data Protection Officer Categories | **Category A (Lead DPO)** — large organisations, 3–5 years' experience or recognised certification + exam; **Category B (Advanced DPO)** — medium, 2–3 years or one relevant certification + exam; **Category C (Entry-Level)** — small, 0–1 year + exam. Shared DPOs via formal agreement with Centre approval. **Reassessment every 3 years**; voluntary category changes subject to Centre approval. |
| Data Users | Controllers, processors, and combined role; role determination; Records of Processing Activities; **impact assessments**; breach notifications; sensitive data; e-marketing; cross-border transfers; cooperation; **contractual data protection clauses**. |
| Data Protection Principles | Lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, security, accountability. |
| RoPA (Record of Processing Activities) | Practical RoPA-building tools plus **Centre templates** for controllers, processors and combined; mandatory fields incl. purpose, data/data-subject categories, retention, TOMs, DPAs, cross-border details, **impact assessments**. |
| Licences and Permits | Types, application, renewal, amendment (legal change, merger, PDPL objectives); general and supplementary licences; portal procedures, documents, fees, timelines; enforcement (warning, suspension, revocation); **transitional one-year compliance provision**. |
| Privacy Notice | Must state purpose, scope, lawful basis, data types, recipients, cross-border transfers, retention, rights, security measures, and the right to complain to the PDPC. Must be **visible, in Arabic, concise, transparent, lay-language, accessible, accurate and current**; may be layered / just-in-time / multimedia; must be given **at collection, first communication, or before first disclosure to third parties**. |

⚠️ **Important:** these guidelines **do not carry the force of law**. Also note that the Shand & Partners "Data Users" guideline summary references **impact assessments** — see the open questions below, because **no DPIA/impact-assessment obligation appears in the text of Law 151/2020 or Decision 816/2025**.
- **As of:** 2026-10-12

---

## 4. Consumer Protection Law No. 181 of 2018

### Consumer Protection Law No. 181 of 2018 (قانون حماية المستهلك)

- **Citation:** Law No. 181 of 2018 on Consumer Protection (قانون رقم ١٨١ لسنة ٢٠١٨ لحماية المستهلك).
- **Issuing authority:** House of Representatives; promulgated at the Presidency of the Republic on **13 September 2018** (3 Muharram 1440 AH), signed by Abdel Fattah El-Sisi. ✅
- **Gazette:** Official Gazette (الوقائع المصرية) **Issue No. 37 bis (37 تابع)**, **13 September 2018** — the gazette header is reproduced in the official Egyptian economic courts PDF. ✅
- **Entry into force:** **14 December 2018** — Art. 5 provides the law enters into force after three months from publication; WIPO Lex records "Entry into force: December 14, 2018; Issued: September 13, 2018; Published: September 13, 2018." ✅
- **Repeals:** Consumer Protection Law No. 67 of 2006 (Art. 4). ✅
- **Not displaced by:** Law 3/2005 on Competition Protection and Prohibition of Monopolistic Practices; Law 1/2017 establishing the National Authority for Food Safety (Issuance Art. 1). ✅
- **Jurisdiction:** **Economic Courts** for civil and commercial disputes arising under the Law; **Administrative Court (القضاء الإداري)** for administrative disputes (Issuance Arts. 2). ✅
- **Status:** In force, as amended by Law No. 20 of 2024 (see §6).

#### Definitions (Art. 1) ✅
Consumer (natural **or legal** person to whom products are supplied to satisfy non-professional/non-commercial needs); **"the Agency" = جهاز حماية المستهلك (Consumer Protection Agency / CPA)**; Persons; Products (goods and services from public or private law persons, including used goods contracted through a supplier — **excluding financial and banking services regulated by CBE Law 194/2020 and the Non-Banking Financial Instruments Market Regulation Law**); Supplier; Advertiser (incl. advertising agency, advertising requester, advertising intermediary/agent, advertising medium — all per Egyptian Standards in line with ESPR requirements on advertising goods and services incl. digital media); Defect; **Distance contract (التعاقد عن بعد) = displaying, selling or purchasing products using the Internet or any visual, audible or readable means of communication, or by telephone or any other means**; Contests/competitions; Deceptive conduct; **Competent Minister = the Prime Minister** (Art. 1(11)).

#### Consumer rights (Art. 2) ✅
Health and safety in normal use; **all correct information and data** about services/products purchased, used or supplied; free choice among products meeting quality specs and fair competitive prices; **personal dignity** and respect for community customs and traditions; participation in consumer-protection bodies; **access to justice** through quick and easy procedures; and **fair compensation** for damage to person or money from buying/using products or receiving services.

#### Mandatory pre-contractual disclosure & documentation (Arts. 4, 5, 6, 7, 10, 11, 12) ✅
- **Art. 4:** the supplier **must inform the consumer of all essential data about products**, in particular the product's **source, price, specifications and basic characteristics**, plus any other data the Executive Regulations specify by product nature.
- **Art. 5 (the Arabic-language rule — commercially critical):** all advertisements, data, information, documents, **invoices, receipts and contracts, including electronic records and electronic documents**, must be **in Arabic and in clear, legible script**. They must bear data identifying the supplier, in particular **its address, contact methods, commercial-register registration data and its trade licence if any**. They may be in two or more languages **provided one of them is Arabic**. *(This is the single most-missed rule by foreign sellers in Egypt.)*
- **Art. 6:** Arabic labelling per Egyptian Standards/law/Regulations; service providers must clearly state the service's data, features, characteristics, place and times of provision.
- **Art. 7:** prices of goods/services must be displayed clearly and **inclusive of legally imposed taxes and other financial charges**.
- **Art. 10:** the supplier must give the consumer an **invoice** proving the transaction, containing in particular the **tax registration number**, transaction date, price, specifications, nature, type, quantity, plus any other data the Regulations specify. **Art. 11:** if the invoice is not issued as required, the consumer may **prove the product's specifications and all other contract elements by any means of proof.**
- **Art. 12:** reservation of a product requires a **reservation receipt**.

#### Anti-deceptive-conduct and advertising (Arts. 9, 13, 14, 15, 57) ✅
- **Art. 9 (11 listed elements):** no supplier or advertiser may engage in deceptive conduct as regards — (1) nature, essential characteristics, constituent elements or quantity of the goods; (2) source, weight, volume, method of manufacture, production or expiry date, conditions of use or precautions; (3) product characteristics and expected results of use; (4) price or method of payment (incl. surcharges and **VAT**); (5) place of production or service provision; (6) type of service, place of provision, precautions of use and essential characteristics/benefits; (7) **contracting conditions and procedures, after-sales service and warranty**; (8) awards, certificates and quality marks obtained; (9) trade marks, data or logos; (10) **existence of price reductions contrary to reality**; (11) **quantities available**. The Executive Regulations may add elements.
- **Art. 13:** prohibited to import, produce, trade in or advertise products in a manner that discriminates between citizens, disparages them, or breaches public order or public morals.
- **Art. 14:** competitions may not be advertised **until the Agency is notified, at least 3 days before advertising**, of the prescribed data; the Agency may stop a competition and related advertising if it is not serious, is deceptive, or violates Art. 13.
- **Art. 15:** advertising/contracting for the **sale of real-estate units or land for building**, or subdivision, requires a building permit under Building Law 119/2008; any contract term requiring the buyer or their successor to pay a percentage/fee/commission to the seller in connection with dealings with the unit is **void**.
- **Art. 16:** suppliers are **prohibited from soliciting at residential units** to display or sell products without the consumer's prior and express request (procedure in the Regulations).
- **Art. 57 (ad-stop procedure):** on breach of Arts. 9 or 14 the Agency may require correction/amendment **within 3 days**; if refused, or if the advertisement is harmful or violates Art. 13, the Agency may **suspend the advertisement for up to 7 days**, must prepare a report within **48 hours** and refer it to the competent Public Prosecution, which must refer it to the competent **Misdemean Appeal Court (محكمة الجنح المستأنفة)** in advisory chamber within **24 hours**; the Court decides within **72 hours** either confirming or cancelling the suspension. Failure to refer within time nullifies the suspension order.

#### Returns, exchange and withdrawal (Arts. 17, 21, 32, 40, 41) ✅
- **Art. 17 (general right, in person):** the consumer may **exchange or return the goods and recover their cash value, without giving reasons and without bearing any expenses, within 14 days of receipt**, without prejudice to any better legal or contractual guarantee. The Agency may set a **shorter** period for certain goods by nature. **Exceptions:** (1) the nature/characteristics/packaging make exchange or return impossible; (2) perishable, rapidly deteriorating consumables; (3) the goods are not in the condition they were in at sale for a consumer-attributable reason; (4) goods manufactured to the consumer's own specifications and conforming to them; (5) **books, newspapers, magazines, computer programs and the like**. The Regulations may add cases.
- **Art. 18:** the supplier must display, in a **visible place** inside sales/display premises, a statement of the Agency's approved exchange/return rights; suppliers may not condition sales on terms contrary to commercial custom, on a minimum quantity, or on bundling with other products.
- **Art. 21:** for goods **defective or not conforming to their specifications or the contracted purpose**, the consumer has **30 days from receipt** to exchange or return with refund, **at no additional cost**, without prejudice to better guarantees or shorter Agency-set periods.
- **Art. 32:** for **time-sharing (اقتسام الوقت) / partial-ownership** contracts, the consumer may withdraw **within 14 days of signing, without giving reasons and without expenses.**
- **Art. 40 (distance contracts):** the consumer who contracts at a distance may withdraw **within 14 days of receiving the goods**, without prejudice to better guarantees. The supplier must refund the amount paid **by the same payment method** (unless otherwise agreed) **within 7 days** of the return of the goods (or of the contracting date for services); **the consumer bears shipping and return costs unless the contract provides otherwise.** If the supplier **delays delivery** beyond the agreed date, or does not deliver **within 30 days** where no delivery date was agreed, the consumer may withdraw **within 14 days of the delay or 30 days of receipt, whichever is longer**, on notifying the supplier — in which case the supplier must refund **immediately** and bears **all return-shipping and delivery costs.**
- **Art. 41:** the Art. 40 withdrawal right lapses where — (1) the consumer has **fully enjoyed the service** before the deadline; (2) the agreement is for goods **made to the consumer's specifications**; (3) the agreement covers **software, information programs or printed matter whose seal the consumer removed**; (4) the agreement covers **video tapes, records, CDs** or similar where the consumer removed the seal; (5) a defect resulted from the consumer's **poor custody**; (6) the withdrawal request conflicts with the nature of the product, contravenes commercial custom, or is abusive in exercising the right (as specified by the Regulations).

#### Pre-contractual disclosures for distance contracts (Art. 37) ✅ — 11 mandatory items
Before concluding a distance contract the supplier must provide the consumer, **clearly and explicitly**, the information enabling an informed decision, in particular:
1. **supplier data** — name, address, telephone, email (if any), commercial-register number, tax card, whether the supplier is legally organised, its professional capacity and the name of the registering professional body, plus any information identifying the manufacturer or importer;
2. **product data** — source, specifications and essential characteristics, **how to use it**, and any **risks** arising from such use;
3. **price** and all sums added to it, in particular **fees, taxes and shipping costs**;
4. **duration of the offer**;
5. **the warranty** offered;
6. **after-contract services**, if any;
7. duration of an offer for services supplied on a recurring basis;
8. **delivery date and place**, and the charges payable on delivery;
9. **the withdrawal terms, in particular the period within which the consumer may withdraw**;
10. **maintenance-centre data** and how maintenance is arranged, for the goods specified by the Law; and
11. **the contracting data that will be sent to the consumer if the transaction is completed**, plus any other data securing consumer rights as specified in the Regulations.

**Art. 38 (confirmation):** where the consumer accepts a distance contract, acceptance **must be confirmed**, and the consumer has the **right to correct or amend their order within 7 working days of acceptance** (unless the parties agree a longer period), in the manner the consumer expressed their wish to purchase. Except in cases exempted by decision of the Agency's Board according to the nature of the contract or prevailing commercial custom, the supplier **must send the consumer a written notification immediately upon contracting**, containing the Art. 37 offer data and the other contract terms — **which may be sent by email or any other storable electronic medium** — and the notification **may not contain data inconsistent with the supplier's offer**.

**Art. 36 (scope of the distance-contract chapter):** does **not** apply to (1) banking and financial services and services related to capital-market trading; (2) subscriptions to newspapers and other periodicals. The Executive Regulations may add exclusions. (Reg. 822/2019 Art. 24 adds **air/rail transport booking** and **hotel booking**.)

**Art. 39:** distance contracts are subject to **all other provisions of the Law** where not specifically dealt with in that chapter.

#### Warranty, maintenance and after-sales (Arts. 19, 20, 22, 23, 24, 25, 26, 33, 34) ✅
- **Art. 19 (defect reporting — critical):** the supplier must notify the Agency of a defect in a product and its **potential harm within a maximum of 7 days** of discovering or learning of it. Where the defect may harm the consumer's **health or safety**, the supplier must notify the Agency **immediately**, **announce suspension of production or trading** and **warn consumers** via the media; must **repair, replace or refund at no additional cost**; and **may not resume** production or trading **without the Agency's approval.**
- **Art. 20:** the supplier warrants the quality and safety of the contracted product throughout the warranty period.
- **Art. 22 (durable goods):** durable goods (السلع المعمرة) carry a **warranty against manufacturing defects of at least 2 years** from the consumer's receipt, without prejudice to better guarantees. Where the product needs supplier installation or operation, the warranty runs from **actual installation/operation, capped at 2 months** from receipt, and the supplier must give a receipt stating the actual operation date. The list of durable goods is fixed by a Prime Minister's decision on the Industry Minister's proposal.
- **Art. 23:** warranty covers inspection, repair, **original spare parts**, technician travel costs, and product transport between the consumer's premises and the company/service centre and back, **including installation and operating costs**. During the warranty the supplier must inform the consumer of **periodic maintenance** intervals and issue a receipt of work performed; if the supplier fails to repair, it must **replace with a new item of the same type and specifications, or refund**.
- **Art. 24 (repeated-defect rule):** if the **same defect occurs more than twice within the first year** of receipt and materially affects functional quality, the supplier must **replace with a new item of the same type and specifications at no cost, or refund**, unless the Agency sets a shorter period.
- **Art. 25:** service providers must **refund the service fee or make good the deficiency or re-perform the service** where defective or deficient, per the contract and commercial custom or as the Agency decides.
- **Art. 26:** suppliers of **finishing, maintenance and home-installation services** warrant the soundness of their work and supplied products for **at least 1 year** (at least **3 years** if the defect is due to **fraud or gross negligence**), and must deliver a receipt at contracting and before commencing work proving the transaction, specifications and expected cost — failing which the consumer may prove the contract elements by any means.
- **Art. 33:** service and maintenance centres must inform the consumer of the necessary maintenance/repair works, their duration and cost, and must obtain the consumer's **express consent before performing them**; must issue an invoice detailing the work and replaced parts; and guarantee product safety within the service scope.
- **Art. 34:** suppliers must provide **service, maintenance and repair centres and original or approved spare parts** for imported/domestic goods and must **notify the Agency** locally of any change.

#### Used goods and vehicles (Arts. 35) ✅
Used goods: the supplier must disclose the condition and defects per the Regulations. Used vehicles: the supplier must provide the consumer with a **technical inspection report from a centre licensed to practise this activity** (unless otherwise agreed); if essential data are concealed or there was **gross negligence**, supplier and centre are **jointly liable**.

#### Product liability and contract terms (Arts. 27, 28) ✅
- **Art. 27:** the **producer** is liable for all damage caused by the product where the damage arises from a defect in its **design, manufacture or installation**. The **supplier** is liable where the damage arises from the **manner of use**, or from failure to take adequate precaution to prevent the harm or to warn of its possibility. The **distributor or seller** is liable where the damage arises from a defect in the way the product was **prepared for consumption, stored, packaged, traded or displayed**. In all cases suppliers are **jointly and severally liable**.
- **Art. 28 (nullity):** **any condition in a contract, document or instrument relating to a consumer contract is void if its effect is to reduce any of the supplier's obligations under the Law or its Executive Regulations, or to exonerate the supplier from them.** This is the consumer's principal contractual shield.

#### Consumer data protection under the Consumer Law (Art. 29) ✅ — under-cited and important
The supplier who concludes the contract must **preserve the confidentiality and data of the consumer** and must not trade in or disclose them in breach of this Law or related laws **unless the consumer has expressly consented**. The supplier must take all necessary precautions to preserve the **secrecy and privacy** of such data and information. **Disclosure constraint:** on request of an official authority or an interested party, the supplier may be ordered to disclose or provide consumer data only by the **Public Prosecutor or their delegate (at least a Deputy/Assistant Public Prosecutor)**, whether of their own motion or on application, and **only where uncovering the truth in a crime or misdemeanour is required and there are serious indications of its occurrence**. In all cases the **competent court** may access such data in connection with a dispute before it.
> *This co-exists with Law 151/2020 (which is broader and requires a Licence). Where both apply, Law 151/2020 governs data processing; Art. 29 adds a consumer-specific secrecy duty and a narrow disclosure channel.*

#### Hire purchase and instalment plans (Arts. 30, 31) ✅
**Art. 30** requires an invoice/receipt stating: total sale price; cash sale price; annual return and total return payable for the instalment period (if any); amount payable in advance; entity providing the instalment product, its duration, number of instalments and value of each; and the respective rights and obligations on breach. **Art. 31:** the consumer may at any time **pre-pay all instalments before due date**, deducting the accrued return for the remaining period, unless otherwise agreed.

#### Other special rules
- **Art. 8 (strategic products):** prohibits withholding strategic products prepared for sale from circulation by concealing them, not putting them up for sale, or refusing to sell them. A Prime Minister's decision identifies strategic products for a fixed period, circulation rules and the competent authority; non-personal-use holders must notify the competent authority of their stock and quantities; the decision is published in **two widely circulated dailies**.

#### The Consumer Protection Agency (CPA) — جهاز حماية المستهلك (Arts. 1(2), 42–61) ✅
- **Legal form (Art. 42):** the competent authority for applying the Law; **public legal personality**; **subordinate to the Competent Minister** (i.e. **the Prime Minister**, Art. 1(11)); headquarters in **Cairo**, with **branches in all governorates**; may draw on consumer-protection associations at governorate level.
- **Functions (Art. 43, 12 items):** set plans/programmes for protecting consumer rights; publish a consumer-protection culture; **receive and investigate all types of consumer complaints and reports** (the Regulations set the response period, **max 30 days by commodity group**); coordinate with state agencies, in particular the **Competition Protection and Prohibiting Monopolistic Practices Authority**, which must supply data and technical expertise on request; study proposals and recommendations; technical and legal coordination and support with administrations, sectors and ministries on consumer/user complaints; support competent civil-society associations; cooperate with market-control agencies to enforce the Law; training programmes; domestic and international cooperation, preventive action and **early warning** against potential consumer harm; **express an opinion on legislation, policies and decisions affecting consumer rights**, and competent authorities **must obtain the Agency's opinion on draft laws and regulations** relating to consumer rights; **institute and intervene in civil actions** on behalf of groups of consumers.
- **Resources (Art. 44):** budget appropriations; donations/endowments; State-directed international grants; **25% of the cash proceeds of reconciliations** in cases of breach; prescribed fees; and consideration for work, studies and services (subject to Art. 45).
- **Art. 45:** independent annual budget aligned to the State financial year, surplus to the Public Treasury. **The Agency may not charge for complaints received from consumers or for the measures it takes on them**, and its staff **may not receive incentives or bonuses from fines, donations or endowments**.
- **Board (Art. 46):** Head appointed by **Presidential decision** (or delegate) on the Competent Minister's proposal; Board chaired by the Head with: a full-time expert deputy head; a **Council of State** vice-president chosen by the Council's President; representatives of Foreign Trade, Supply & Internal Trade, Finance and Industry Ministries; the General Administration for Supply and Internal Trade Police; the National Authority for Food Safety; four consumer-association representatives (Upper Egypt, Greater Cairo, Lower Egypt, Canal/Red Sea & Sinai); the General Union for Consumer Protection; the Central Consumer Cooperative Union; the Federation of Egyptian Chambers of Commerce and the Egyptian Industries Federation. Board term **4 years, renewable once**; constituted and the deputy head's/members' remuneration fixed by Competent Minister decision.
- **Art. 47:** Board is the supreme authority; sets internal/technical/financial/administrative regulations (issued by Competent Minister decision); accepts donations; approves the annual budget and final account; **proposes which staff are granted judicial-enforcement-officer status**; considers the Head's reports.
- **Art. 48:** Board meets at least monthly (or on a third of its members' request); valid with **10 members** present; decisions by majority of those present; chair's casting vote; decisions **effective without approval or ratification**; conflict-of-interest disqualifications apply.
- **Art. 49:** full-time Executive Director appointed by Competent Minister decision on the Board's nomination; **2-year term, renewable**; attends Board meetings without a counted vote.
- **Art. 51:** Agency staff and designated civil servants have **judicial-enforcement-officer status** under this Law, **Law 48 of 1941 on Combating Fraud and Deceit**, and **Decree-Law 95 of 1945 on Supply Affairs**. They may inspect all books and documents at any government or non-government entity, **enter any premises used for selling or storing products**, and **take, examine and analyse samples** in accredited labs.
- **Art. 52 (binding decisions):** where a dispute arises between consumer and supplier/advertiser on applying the Law, or on the right to exchange or refund, the matter is **referred to the Agency for a binding decision**. The Agency may order exchange or refund **at the price announced by the Central Bank of Egypt plus the prescribed return**, or refund at **market value**, in each case from the date the consumer filed the complaint. The Board may form a **committee** to examine such disputes and issue recommendations.
- **Art. 56:** on establishing a breach the Agency must require the offender to **rectify within a period set by the Board**; where the breach caused or could cause harm to consumer health/safety, the Board may **suspend the service** or **seize the offending goods** pending investigation or judgment, and the Agency must inform consumers of the breach.
- **Art. 58:** Agency decisions under the Law are **final**, appealable before the **Administrative Court (القضاء الإداري)**; exempt from the Law 7/2000 reconciliation-committee regime.
- **Art. 59 (reconciliation):** with Board approval by majority, the Agency may **reconcile with the defendant** in offences under the Law, **unless injuries or deaths of consumers resulted**, and provided the causes of the breach are removed: before referral to court, payment of not less than the minimum and not more than **one-third of the maximum** fine; after referral and until final judgment, not less than **three times the minimum** and not more than **half the maximum** fine. Reconciliation terminates the criminal proceedings.
- **Art. 60:** the "**Consumer Friend**" (صديق المستهلك) programme — suppliers apply, get a **one-year certificate**, revocable on breach; issue fee capped at **EGP 20,000 per retail outlet**.
- **Art. 61:** parties to a complaint may obtain an **official certificate** of the complaint's outcome and copies of the related technical reports; fee capped at **EGP 200**.
- **Art. 62:** consumer-protection NGOs may institute/intervene in actions on behalf of consumer groups, survey and compare prices/quality and monitor compliance with advertised prices, feed information to government bodies, receive and verify consumer complaints, assist complainants, build databases, provide consultations and centres — **but may not accept donations or endowments from suppliers or advertisers.**
- **Official site:** `https://cpa.gov.eg/` (Arabic: `https://cpa.gov.eg/ar-eg/`) — legislation page `https://cpa.gov.eg/ar-eg/تشريعات`

#### Penalties — Consumer Protection Law No. 181/2018 ✅ VERIFIED, amounts as enacted

| Art. | Trigger | Penalty |
|---|---|---|
| 64 | Supplier breaching Arts. 3, 4, 5, 6, 7, 12, 14, 16, 18, 21, 35, 38, 40, 55 (1st ¶), 56, or 62 (last ¶) | Fine **EGP 10,000 – 500,000** **or twice the value of the product**, whichever is greater. Same penalty for breaching Art. 33 (1st ¶) or Art. 40 (3rd ¶); the court may order **closure of the non-compliant service/maintenance centre for up to 6 months** |
| 65 | Breaching Arts. 10, 20 (2nd/3rd ¶), 22, 24, 25, 26, 29, 30, 31, 33 (2nd/3rd ¶) | Fine **EGP 30,000 – 1,000,000** or twice the product value, whichever is greater |
| 66 | Breaching Arts. 9, 13 (1st ¶), 15, 32 (2nd ¶), 34, 56 | Fine **EGP 50,000 – 2,000,000** or twice the product value, whichever is greater |
| 67 | (1) obstructing judicial enforcement officers; (2) failing to provide the Agency with Art. 54 data/documents; (3) knowingly supplying false data/documents | Fine **EGP 20,000 – 500,000** |
| 68 | Failing to comply with the Art. 57 advertisement-stopping decision | Fine **EGP 50,000 – 1,000,000** or twice the amount agreed with the advertising medium for the offending advertisement, whichever is greater |
| 69 | **Recidivism** in any of the above offences | **Both minimum and maximum fines doubled** |
| 70 | Breaching Art. 19 (defect reporting) | Fine **EGP 50,000 – 2,000,000** or the value of the goods, whichever is greater. **If the breach endangers the consumer's life or exposes them to an addictive or incurable disease:** **imprisonment + fine EGP 100,000 – 2,000,000**, or either |
| **71** | **Breaching Art. 8 (hoarding/withholding strategic products)** | **⚠️ SEE AMENDMENT BELOW.** Original text: imprisonment **≥ 1 year** + fine **EGP 100,000 – 2,000,000** or the value of the goods, whichever is greater; **on recidivism, imprisonment 2–5 years and the fine doubled**; in all cases **confiscation** and **publication of the judgment in two widely circulated dailies** at the defendant's expense |
| 72 | If a violation causes **permanent disability or addiction/incurable disease** | **Imprisonment** + fine **EGP 100,000 – 1,000,000** or the product value, whichever is greater. If the court applies Art. 17 of the Penal Code, custodial sentence may be reduced by up to **1 year**. If the violation **causes the death of one or more persons** | **Life imprisonment** + fine **EGP 200,000 – 2,000,000** or the product value, whichever is greater |
| 73 | Additional to penalties above | The court **must** order the supplier to **refund the value of the product to the consumer** in every case where the consumer is entitled to a refund and has not already obtained it. Not barred by Penal Code Art. 32(1) |
| 74 | Actual manager of a non-compliant legal person | **Same penalties** where they knew of the breach and their managerial default contributed; the **legal person is jointly liable** for financial penalties and compensation |
| 75 | Conviction | Court **must** order publication of the judgment at the defendant's expense in **one daily newspaper and on widely circulated electronic sites**; the Agency **must publish** detailed final judgments on its website, **for three years** from the judgment date, and the competent court's registrar must supply official copies to the Agency free of fees |
| 76 | Art. 13 (discrimination) offence | Criminal proceedings may **only be initiated on the written request of the Competent Minister or his delegate** (i.e. the Prime Minister) |
| 59 | Reconciliation | See §Agency above: before referral, **minimum fine to one-third of maximum**; after referral until final judgment, **3× minimum to half of maximum** |

- **Amendments:** **Law No. 20 of 2024** (see §6). ❌ **UNVERIFIED — needs primary-source check:** I did not locate the full Arabic gazette text of Law 20/2024; the amendment is known to me from the Al Tamimi & Co / MELES library record and Al-Masry Al-Youm coverage. Also unresolved: a secondary source refers to a **"Law No. 19 of 2024"** amending the same Law — see open questions.
- **Sources:**
  - **Official Arabic text (Egyptian economic courts portal, government domain):** `https://elec.eecourts.gov.eg/assets/laws/16%20-%20%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%AD%D9%85%D8%A7%D9%8A%D8%A9%20%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D9%87%D9%84%D9%83.pdf` ✅ *This is the source used for every article number and every fine amount above.*
  - Consumer Protection Agency (official) PDF of the Law: `http://cpa.gov.eg/Portals/0/Law/CPA-Newlaw.pdf`
  - WIPO Lex record (dates): `https://www.wipo.int/wipolex/en/legislation/details/19866`
  - WIPO Lex Arabic record: `https://www.wipo.int/wipolex/ar/legislation/details/19866`
  - Manshurat legal corpus record (issuing authority, date): `https://manshurat.org/node/31479`
  - Consortio Law Firm — "Complete English Translation": `https://consortiolawfirm.com/egyptian-consumer-protection-law-181-2018-english-translation/` ⚠️ paywalled/gated; content not machine-verified by me
  - Andersen in Egypt translation page: `https://eg.andersen.com/translation-law-181-2018/`
  - Chambers Advertising & Marketing 2025 — Egypt chapter: `https://practiceguides.chambers.com/practice-guides/advertising-marketing-2025/egypt`
  - Baker & McKenzie Egypt consumer overview (pre-2018 Law 67/2006): `https://www.ftc.gov/system/files/documents/public_events/316871/egyptamalehsan.pdf`
  - Independent critique of CPA independence: `https://www.theregreview.org/2018/12/13/saleh-independence-egypts-consumer-protection-agency/`
  - SSRN: "An Overview Of The Consumer Protection Agency In Egypt": `https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3764047_code3781327.pdf?abstractid=3764047&mirid=1`
- **As of:** 2026-10-12

---

## 5. Consumer Protection Executive Regulations — Prime Minister's Decree No. 822 of 2019

### Executive Regulations of the Consumer Protection Law (اللائحة التنفيذية لقانون حماية المستهلك) — Prime Minister's Decree No. 822 of 2019 (قرار رئيس مجلس الوزراء رقم ٨٢٢ لسنة ٢٠١٩)

- **Citation:** Prime Minister's Decree No. 822 of 2019 issuing the Executive Regulations of Consumer Protection Law No. 181 of 2018. **47 articles.**
- **Issued / signed:** **1 April 2019** (25 Rajab 1440 AH) by Prime Minister **Dr. Mostafa Madbouly**. ✅
- **Gazette:** **Al-Waqa'i' al-Misriyya, Issue No. 13 bis (A) — 13 مكرر (أ) — 1 April 2019.** ✅
- **Entry into force:** **2 April 2019** — Decree Art. 2: published in the Official Gazette, effective from the day following publication. WIPO Lex: "Issued: April 1, 2019; Published: April 1, 2019; Entry into force: April 2, 2019… in accordance with its Article 2." ✅
- **Legal basis:** Constitution; Penal Code 58/1937; Law 48/1941 on Combating Fraud and Deceit; Decree-Law 95/1945 on Supply Affairs; Civil Code 131/1948; Criminal Procedure Code 150/1950; Law 120/2008 establishing the Economic Courts; Law 1/2017 on the National Authority for Food Safety; Law 70/2017 on Civil Work Associations; Law 181/2018; **after taking the opinion of the Consumer Protection Agency's Board**; opinion of the State Council. ✅
- **Status:** In force. ⚠️ The transcription I used is captioned "updated until 2025" (محدثاً حتى عام ٢٠٢٥). ❌ I located **no** amending decision to Decree 822/2019 — confirm before asserting it is unamended.

#### Key provisions (selected; article numbers verified from the Arabic text) ✅

| Art. | Substance |
|---|---|
| 1 | Definitions mirror the Law, including **distance contract** = displaying/selling/buying via the Internet or any visual, audible or readable means of communication, by telephone or any other means; and **supplier** expressly covers dealing "by any means whatsoever, **including electronic means and other modern technical means**" |
| 3 | Supplier must clearly inform the consumer of **all essential product data**, in particular **source, components, specifications, essential characteristics, how to use it** (if there is a special method of use), **expected results of use**, **the all-inclusive price**, and **how to pay** |
| 4 | Restates the Arabic-language rule (advertisements, data, information, documents, invoices, receipts, contracts including **electronic records and electronic documents** in clear legible Arabic) + supplier identity data |
| 8 | List of the deceptive-conduct elements (11, mirroring Law Art. 9) |
| 9 | Pre-contract disclosure list for distance contracts — includes **exchange/return periods and the method of contacting the Agency** and **warranty duration for warranted products** |
| 11 | Competition/contest advertising — Agency may stop a contest and related advertising if not serious, deceptive, or violating Law Art. 13 |
| 12 | **Prohibition on soliciting at residential units**; the consumer's consent given **by telephone or electronic or any other means of communication** counts as prior express request |
| 13 | Exchange/return exceptions (mirror of Law Art. 17) |
| 14 | Supplier must display an **Agency-issued statement with an approved number** in a **visible place** inside display/sales premises, stating the exchange/return rights; no bundling, no minimum-quantity or contrary-to-custom conditions |
| 15 | **Defect reporting to the Agency** — implementation of Law Art. 19; health/safety-risk defects require **immediate** notification, public announcement of suspension via dailies/websites/satellite/radio channels or direct consumer contact, and the report must state the product(s), the supplier's **sales outlets and maintenance centres with coordinates on the electronic map of Egypt** where possible |
| 17 | For products requiring supplier installation/operation, the warranty runs from actual installation/operation, **capped at 2 months** from receipt; supplier must issue a receipt showing the actual operation date |
| 18 | Warranty contents: inspection, repair, original spare parts, technician travel, product transport, installation and operating costs; **no warranty for defects or faults from misuse or breach of operating instructions/technical conditions** |
| 21 | Maintenance/service centre data to be given to consumers |
| 22 | Maintenance centre data — activity, product types, location **with coordinates on Egypt's electronic map**, etc. |
| **23** | **Used goods:** the supplier must give sufficient information on the condition, defects and repair needs **before use**, without creating a false or misleading impression or confusion |
| **24** | **Distance-contract exclusions** — adds to Law Art. 36: **(3) air and rail transport booking services; (4) hotel booking services** |
| **25** | **Order confirmation and correction window:** the consumer's acceptance must be confirmed and they may correct or amend the order **within 7 working days**, **in the manner by which they expressed their wish to purchase**, unless a longer period is agreed — **but not** if the consumer has already received the product, or the contract is for importing a specifically identified product, or for manufacture to special specifications; correction/amendment must be **in the same contracting manner and the same way**. In all cases the supplier must **keep a complete and accurate record of the details of purchase operations** |
| **26** | **Distance-contract withdrawal exceptions** — adds to Law Art. 41: **(5) requests for withdrawal incompatible with the product's nature, contrary to commercial custom, or abusive by the consumer — including perishable consumer goods, consumables and cosmetics, jewellery and the like** |
| 27 | Board composition for consumer-association representatives (nominated by the Board Chair after consulting the General Union of Civil Associations; association general-membership ≥ 200; three-year activity report certified by the Ministry of Social Solidarity) |
| 33–34 | Complaint channels (hotline, post, the Agency's website, in person at a branch, or any other channel the Agency determines) + required supporting data; complaint registration on the Agency's electronic system, assignment to the competent department, and regular recording |
| 35 | The Agency Head publishes **monthly** on the Agency's website and at its premises a count of complaints, minutes drawn up against offenders, Board decisions, and resolution rates |
| 37 | Taking samples requires **express prior permission** from the Executive Director / Deputy Head / Head, specifying issue date, validity and the names of the samplers |
| 38 | Sampling procedure: the owner/manager must be summoned on entry and asked to produce provenance documents; if not produced the product is seized and a minute drawn, with sampling continuing |
| 41 | Where same-type replacement is impossible because the current market price of the disputed goods is higher than the contract price, the complainant may request **return of the goods at the market price or with the prescribed return added, per the CBE-announced price at the date the complaint was filed** |
| 45 | "Consumer Friend" certificate fee tiers by registered paid-up capital or value of goods displayed: **EGP 1,000 / 2,000 / 3,000 / 5,000 / 10,000** (capital < 100k; 100k–<500k; 500k–<2m; 2m–<10m; ≥ 10m); names published on the Agency's website, including withdrawn ones |

- **Sources:**
  - **Full Arabic transcription of the gazette text (47 articles), Atef Hassan Ali law firm library:** `https://alhasswalawfirm.com/law-library/decree-822-2019`
  - eastlaws record: `https://www.eastlaws.com/legislation-full-text/ar/egypt/prime-minister-decision/01-04-2019/no-822?type=1&id=1937298&sub=9598249`
  - WIPO Lex (dates, in-force note): `https://www.wipo.int/wipolex/en/legislation/details/19958`
  - Manshurat record: `https://manshurat.org/node/70791`
  - Al-Masry Al-Youm (gazette issue confirmation): `https://www.masrawy.com/news/news_egypt/details/2019/4/3/1543783/`
  - Shalakany summary (warranties, penalties): `https://shalakany.com/new-consumer-protection-law-executive-regulations/`
- **As of:** 2026-10-12

---

## 6. Amendment: Law No. 20 of 2024

### Law No. 20 of 2024 amending certain provisions of Consumer Protection Law No. 181 of 2018 (قانون رقم ٢٠ لسنة ٢٠٢٤ بتعديل بعض أحكام قانون حماية المستهلك الصادر بالقانون رقم ١٨١ لسنة ٢٠١٨)

- **Citation:** Law No. 20 of 2024.
- **Gazette publication date:** **5 April 2024.** ⚠️ PARTIAL — date from the Al Tamimi & Co (MELES) library record and Al-Masry Al-Youm; ❌ **issue number not verified**.
- **Substance:** **a single article** — it replaces **Art. 71** of Law 181/2018 (the penalty for breaching Art. 8, i.e. withholding/hoarding strategic products). ✅ VERIFIED as to content via the Al Tamimi & Co record, which reproduces the Arabic and English text:

> **Art. 71 (as substituted):** Whoever violates the provisions of Art. 8 of this Law shall be liable to **imprisonment of not less than one year** and a **fine of not less than EGP 150,000 and not more than EGP 3,000,000**, or the equivalent of the value of the goods subject matter of the crime, **whichever is greater**. **On recidivism**: imprisonment of **not less than two and not more than five years**, and **both the minimum and maximum limits of the penalty shall be doubled**.
> In all cases the goods shall be seized and confiscated, and the court shall order **closure of the store or the place where the crime was committed for a period not exceeding six months**. The judgment shall be published in **two widely circulated dailies** at the defendant's expense. The court may order **cancellation of the store's/place's licence**.

- **Practical effect:** the fine ceiling for Art. 8 breaches rose from EGP 2,000,000 to **EGP 3,000,000**, the floor from EGP 100,000 to **EGP 150,000**, and a **licence-cancellation** sanction was added. The original Art. 71 already provided 2–5 years' imprisonment and doubled fines on recidivism.
- **Status:** ⚠️ **PARTIAL.** Verified only via the Al Tamimi & Co / MELES library record plus press coverage. ❌ **UNVERIFIED — needs primary-source check:** the **Official Gazette issue number and date**; and whether the number is **20** (Al Tamimi/MELES, Al-Masry Al-Youm) or **19** (one secondary source referenced "Law No. 19 of 2024" with the same long title). Verify the gazette before citing the number in a filing.
- **Sources:**
  - Al Tamimi & Co / MELES library record (Arabic + English text): `https://dspace.id.com.eg/items/4e0672e3-85c1-42ac-bed1-b8745e613057`
  - Al-Masry Al-Youm: `https://www.almasryalyoum.com/news/details/3144773`
- **As of:** 2026-10-12

---

## 7. E-signatures and online contracting

### Law No. 15 of 2004 on E-signature and establishing the Information Technology Industry Development Authority (ITIDA) (قانون رقم ١٥ لسنة ٢٠٠٤ بتنظيم التوقيع الإلكتروني وبإنشاء هيئة تنمية صناعة تكنولوجيا المعلومات)

> ⚠️ **The commissioning brief said "Law 15/2020 on e-signatures". That is wrong.** Egypt's e-signature statute is **Law No. 15 of 2004**. `Decision 816/2025`'s own preamble cites "Law No. 15 of 2004 on E-signature and Establishment of the Information Technology Industry Development Authority (ITIDA)". **Law 15 of 2020 is the Saudi Arabian E-Commerce Law — a common cross-jurisdiction confusion.**

- **Citation:** Law No. 15 of 2004. ✅
- **Promulgated / adopted:** **21 April 2004** (WIPO Lex: "Adopted: April 21, 2004"). ✅
- **Published:** Official Gazette **22 April 2004**; **entered into force 23 April 2004** (Art. 30: published in the Official Gazette, effective from the day following publication). ✅
- **Institution:** establishes **ITIDA (Information Technology Industry Development Authority / هيئة تنمية صناعة تكنولوجيا المعلومات)**, a public authority **affiliated to MCIT**. ✅
- **Key provisions:**
  - **Electronic signature (توقيع إلكتروني)** and **electronic writing (كتابة إلكترونية)** are defined in Art. 1. ✅
  - **Art. 14:** contracts may not be denied enforceability merely because they are concluded electronically, provided the technical requirements of the Law and its Executive Regulations are satisfied; an electronic signature within civil, commercial and administrative dealings has the same conclusive effect as a handwritten signature. ⚠️ PARTIAL (widely reported; the ITIDA PDF confirming Art. 14 text could not be fetched).
  - Electronic signatures, electronic writings and electronic messages have the **determinative effect for evidence** where they comply with prescribed technical conditions. ✅
  - ITIDA powers (Art. 4) include licensing and supervising **certification service providers**, issuing **certification practice statements**, and setting technical standards. ✅
  - **ITIDA certificate = the practical gateway**: a "qualified electronic signature" (التوقيع الإلكتروني المؤهل) tied to a certificate issued by a licensed certification service provider carries the full legal effect of a handwritten signature. Practical consequence: **simple e-signatures are recognised but full equivalence requires ITIDA certification**, so online consumer checkout flow-through under the Consumer Law should not assume signature equivalence without certification.
- **Executive Regulations:** ITIDA hosts "Executive Regulations — Electronic Signature Law" at `https://www.itida.gov.eg/English/Documents/4.pdf`. ❌ **UNVERIFIED — needs primary-source check:** the **decision number and year** issuing these Regulations. Secondary sources variously cite a **"Resolution 109 of 2005"** and a **"Prime Ministerial Decision No. 634 of 2008"**; **I could not confirm either.** One source states the Regulations were later **amended**. Do not cite a decision number for the e-signature Executive Regulations without checking the ITIDA portal directly.
- **Court practice:** the Egyptian **Court of Cassation**, in Judgment No. 17689 of Judicial Year 89, held that it is no longer permissible to deny the authenticity of emails as evidence where they meet the technical requirements of Law 15/2004. ⚠️ PARTIAL (single source; verify the case number before citing).
- **E-commerce-specific regulation:** ❌ **UNVERIFIED / appears not to exist.** No standalone Egyptian e-commerce law and no MCIT e-commerce regulation were located. Commercial commentary consistently states that e-commerce in Egypt is regulated by the **general commercial law plus Law 181/2018's distance-contract chapter and Law 15/2004**, and that incorporation of an e-commerce business requires satisfying **general company-incorporation and activity-licensing rules** rather than a dedicated e-commerce regime. An e-commerce bill has been discussed but I found **no enacted instrument**. Verify before asserting.
- **Sources:**
  - WIPO Lex (dates, ITIDA status, definitions): `https://www.wipo.int/wipolex/en/legislation/details/13546`
  - ITIDA — Executive Regulations of the E-Signature Law: `https://www.itida.gov.eg/English/Documents/4.pdf`
  - ITIDA — Law text extract: `https://itida.gov.eg/English/Documents/2.pdf`
  - Andersen in Egypt translation page: `https://eg.andersen.com/translation-law-15-2004/`
  - Lexis Middle East — Egypt E-Signature Law: `https://www.lexismiddleeast.com/legislativeInsight/Egypt/Egypt_E-Signature_Law/en`
  - Legal 500 — E-commerce and Information Technology in Egypt: `https://www.legal500.com/intelligence/egypt/media-telecoms-it-entertainment/e-commerce-and-information-technology-in-egypt`
  - Lexology — E-commerce Regulations in Middle East (Egypt has no specific e-commerce law): `https://www.lexology.com/library/detail.aspx?g=072193da-0d8a-421d-9c79-bffe91b0eb6d`
  - US ITA — Egypt eCommerce country commercial guide: `https://www.trade.gov/country-commercial-guides/egypt-ecommerce`
  - Shalakany — emails and e-signatures as evidence: `https://shalakany.com/are-emails-and-e-signatures-accepted-under-egyptian-law-as-means-of-evidence/`
- **As of:** 2026-10-12

### Cybersecurity / Anti-Cyber and Information Technology Crimes Law No. 175 of 2018 (قانون رقم ١٧٥ لسنة ٢٠١٨ بشأن مكافحة جرائم تقنية المعلومات)

- **Citation:** Law No. 175 of 2018 on Anti-Cyber and Information Technology Crimes. ✅
- **Promulgated:** ratified by the President; published in the Official Gazette **14 August 2018**, **Issue 32 bis (C)** (per the Library of Congress Global Legal Monitor). ⚠️ PARTIAL.
- **Data-protection relevance:** imposes **duties on service providers to retain data, protect user information and cooperate with authorities**. It sits alongside — not instead of — Law 151/2020. Where Law 151/2020 applies, it governs personal-data processing; Law 175/2018 governs criminality of IT conduct and provider obligations.
- **Sources:** WIPO Lex `https://www.wipo.int/wipolex/en/legislation/details/19959` · Library of Congress `https://www.loc.gov/item/global-legal-monitor/2018-10-05/egypt-president-ratifies-anti-cybercrime-law/` · Andersen `https://eg.andersen.com/translation-law-175-2018/`
- **As of:** 2026-10-12

---

## 8. Telecommunications and NTRA

### Telecommunications Regulation Law No. 10 of 2003 (قانون تنظيم الاتصالات) — NTRA (الهيئة الوطنية communicated Regulation Authority / الهيئة الوطنية ل регуляции الاتصالات)

- **Citation:** Law No. 10 of 2003 on Telecommunications Regulation. ✅
- **Establishment of the NTRA (Art. 3):** a national authority named the **National Telecommunication Regulatory Authority (NTRA)**, with **public juristic personality**, **subordinate to the Minister Concerned** (the MCIT Minister), headquartered in **Cairo and Giza**, with branches nationwide. ✅
- **Status:** In force; described by commentators as still the operative telecom statute. ❌ **UNVERIFIED:** whether any amendment has been enacted since 2003. ❌ **UNVERIFIED:** the Official Gazette publication/entry-into-force dates (the NTRA's own English PDF does not state them on the face of the document).

#### NTRA's data-privacy-relevant functions ✅

| Art. | Provision |
|---|---|
| 2 | General compliance rules for telecom services include **protection of Users' rights** |
| 5(6) | NTRA sets up the **rules guaranteeing Users' protection that will ensure telecommunication confidentiality**, and a **system for users' complaints** reception, investigation and follow-up with providers |
| 13(7) | NTRA Board issues licences and monitors their execution **in a manner guaranteeing Users' rights, especially their privacy rights in accordance with the Law**, and without disturbing national security or state interests |
| **19** | Entities and companies in the telecom field must give the NTRA whatever reports, statistics or information on their activities it requests, **except matters relating to national security** |
| **25** | A licensee's duties include a complaints system, and **ensuring the confidentiality of communications and calls of its customers** and establishing the rules necessary to verify the same |
| **58** | NTRA prepares and updates the frequency-spectrum users database; **the database shall be classified so as to protect the privacy of the Users** |
| **64(1)** | Operators, providers, their affiliates and users **may not use any encryption device for telecommunication services** without the approval of **each** of the NTRA, the **Armed Forces** and the **national security agencies** (radio/television broadcasting encryption exempt). ⚠️ This is a broadly-applied restriction and is routinely cited as a chilling provision. |
| **64(2)** | Subject to citizens' legally-protected right to privacy, each operator/provider must, **at its own expense**, make available within the licensed network all technical capabilities (equipment, systems, software, in-network communications) enabling the Armed Forces and national security agencies to exercise their competences within the limits of the law. Operators, providers **and their marketing agents** must obtain accurate information and data about their users **from citizens and from the various State entities**. |
| **65** | NTRA, jointly with the Armed Forces and competent State bodies, prepares a **prior plan** for operating networks during natural/environmental disasters, general mobilisation (Law 87 of 1960), or any other national-security situation; to be updated periodically; operators and providers are bound to implement it |
| **66** | NTRA coordinates with the Armed Forces and national security agencies when preparing or amending the frequency-spectrum plan and the national numbering plan |
| **67** | Competent State authorities may place all services and networks of any operator/provider under their administration in disasters, general mobilisation or national-security situations |
| **68** | Operators'/providers' obligations are reduced to the extent affected by Arts. 65 and 67; they are entitled to appropriate compensation for Art. 67 measures |
| **69** | By decision of the **Minister of Justice**, in agreement with the Competent Minister, designated NTRA/Armed Forces/national-security staff may be vested with law-enforcement (judicial seizure) powers for offences under the Law |

> **Interaction with Law 151/2020:** the NTRA is **not** the data-protection regulator. It is (a) a **board member of the PDPC** (one NTRA representative, Law 151/2020 Attached Law Art. 20(6)), and (b) the sectoral authority for **telecom confidentiality and lawful-interception capability**, which persists alongside Law 151/2020. A telecom operator needs **both** a PDPC Licence and NTRA compliance.

#### Penalties — Telecommunications Regulation Law No. 10/2003 ✅ VERIFIED (from the NTRA's own English translation and the Andersen in Egypt translation)

| Art. | Offence | Penalty |
|---|---|---|
| 71 | Intentionally destroying/damaging telecom buildings, installations, lines or rendering them unusable causing interruption | Imprisonment + fine **EGP 50,000 – 100,000**. **Negligent** variant: detention **≤ 6 months** + fine **EGP 500 – 1,000**, or either. Court must order payment of the value destroyed/damaged or restoration costs |
| 72 | Operating networks, building network infrastructure, providing services or routing international calls **without an NTRA licence** | Imprisonment **6 months – 5 years** + fine **EGP 50,000 – 500,000**, or either; confiscation of all equipment/connections; compensation for unlawful international routing |
| **73** | Telecom-sector staff who, in the course of duties: broadcast/publish/record a message's content without legal authority; conceal/alter/obstruct/tamper with a message; wilfully refrain from transmitting a message; or **unlawfully disclose information about network Users or their incoming/outgoing communications** | Imprisonment **≥ 3 months** + fine **EGP 5,000 – 50,000**, or either |
| 74 | Assigning a frequency or band licence to a third party without NTRA approval | Imprisonment **≥ 3 months** + fine **EGP 20,000 – 100,000**, or either, **plus revocation of the licence** |
| 75 | Disclosing/publishing/broadcasting information obtained by virtue of employment about a telecom undertaking, where it causes unfair competition | Imprisonment + fine **EGP 20,000 – 100,000**, or either |
| 76 | Using or assisting unlawful means to conduct communications; or deliberately harassing/annoying others by misusing telecom equipment | Imprisonment + fine **EGP 500 – 20,000**, or either |
| 77 | Importing, manufacturing, assembling or **marketing** telecom equipment without an NTRA permit (violating Art. 44(1)) | Imprisonment **1 – 5 years** + fine **EGP 2,000,000 – 5,000,000**, or either. Possession/use/installation/operation without a permit: imprisonment + fine **EGP 100,000 – 300,000**, or either (**not applicable to wireless devices under an NTRA general licence**). **Rigorous imprisonment** if done to harm national security. **Penalties doubled on recidivism.** Confiscation of equipment in all cases |
| 78 | Unlawfully intercepting or interfering with radio waves allocated to others | Imprisonment **≤ 6 months** + fine **EGP 20,000 – 50,000**, or either; confiscation of devices/equipment |
| 79 | Breaching Art. 42 | Imprisonment + fine **EGP 20,000 – 50,000**, or either; court may order removal of unlicensed works damaging network routes, at the offender's cost |
| 80 | Breaching Arts. 30 or 39 | Imprisonment **≤ 3 months** + fine **EGP 5,000 – 20,000**, or either |
| **81** | **Breaching Art. 64** (the encryption restriction / lawful-interception capability / user-data duty) | Imprisonment + fine **EGP 10,000 – 100,000**; court must also order **temporary suspension of the licence** until the offender provides the equipment, systems and telecom software required by Art. 64 |
| 82 | Disobeying the Art. 67 call-up orders | Imprisonment (**rigorous** if in war or general mobilisation); temporary suspension of licence until compliance |
| 83 | Provider failing to comply with health/environmental safety standards or structural measures in Arts. 6, 35, 36, 37 | Imprisonment + fine **EGP 20,000 – 200,000**, or either; court orders removal of the causes, at the violator's cost |
| 84 | Breaching Arts. 19, 21(3), 28(1) and (3), 59(2) | Fine **EGP 10,000 – 50,000**; **doubled on recurrence** |
| 85 | Provider/operator breaching licence conditions or technical-quality/performance controls | Fine **EGP 20,000 – 200,000**. **Overcharging above approved rates:** a fine **equal to 10× the excess amount charged**, **repeating per user affected** |
| 86 | Actual manager of a non-compliant legal person | **Same penalties** where aware and managerial default contributed; legal person **jointly liable** for financial penalties and compensation |

- **Amendments / implementing instruments listed by NTRA:** Ministerial Decree No. 258 of 2003; Ministerial Decree No. 259 of 2003; **Ministerial Decree No. 128 of 2006**; **Ministerial Decree No. 667 of 2017 (Regulation of Disciplinary Penalties)**; and the **Executive Regulations of Law No. 175 of 2018** (Cybercrime). ✅ (from the NTRA's own "Laws and Legislations" page)
- **Sources:**
  - **NTRA official English translation of Law 10/2003 (PDF):** `https://www.tra.gov.eg/wp-content/uploads/2020/11/Law-No-10-of-2003.pdf`
  - **Andersen in Egypt translation (PDF, used for the penalty amounts above):** `https://eg.andersen.com/wp-content/uploads/2025/11/Law-No.-10-of-2003.pdf`
  - UNODC Egypt — Telecommunications Act (English): `https://www.unodc.org/cld/uploads/res/document/egy/2003/egypt_telecommunication_regulation_act_english_html/Egypt_Telecommunications_Act_English.pdf`
  - **NTRA — Laws and Legislations (official):** `https://www.tra.gov.eg/en/regulations/laws-and-legislations/`
  - Legal 500 — Telecommunications Law Review in Egypt: `https://www.legal500.com/intelligence/egypt/media-telecoms-it-entertainment/telecommunications-law-review-in-egypt`
  - AFTE Egypt — Centralization of Telecommunications (Arts. 64, 67, 81, 82, 84 analysis): `https://afteegypt.org/en/legislations-en/legislative-analysis-en/2021/06/29/23250-afteegypt.html`
  - OHCHR UPR — The Right to Privacy in Egypt (Art. 64 analysis): `https://uprdoc.ohchr.org/uprweb/downloadfile.aspx?filename=1085&file=EnglishTranslation`
- **As of:** 2026-10-12

---

## 9. Cross-border data transfer — state of play

### Statutory framework ✅
- **General rule (Law 151/2020 Attached Law Art. 14):** no transfer to / storage or sharing in a foreign State without (a) an equivalent-or-higher protection level and (b) a **Centre Licence or Permit**.
- **Exceptions (Art. 15):** seven cases, each requiring the Data Subject's (or representative's) express consent — see §1.
- **Remote controller/processor access (Art. 16):** a separate Centre Licence, subject to three cumulative conditions.
- **Executive Regulations Art. 16** — the operative rules:
  - **(1)** a Licence or Permit from the Centre, following the Centre's assessment of the **adequacy of the level of protection in the destination country**;
  - **(2)** the **Data Subject's consent**;
  - **(3)** all measures ensuring an adequate protection level throughout transfer/circulation/sharing/storage, in line with the Licence conditions and proportionate to volume/nature;
  - **(4)** transfer strictly per the Licence, **updated whenever another country is added**.
  - **Art. 16(2):** the Centre determines, in its adopted policies, **which countries ensure an adequate level of protection**, subject to **periodic review**, against three criteria: (a) the existence of personal-data-protection legislation/controls and its consistency with the Law; (b) the presence of **technical and security rules** achieving effective protection; (c) the presence of **legal rules on compensation** for damage suffered by a Data Subject from misuse of their data. Where a country meets the criteria, the Centre may authorise licences/permits for transfer/storage/sharing to it.
  - **Art. 16(3):** the Centre **may also** authorise licences/permits for other countries that satisfy the same criteria.
  - **Art. 17:** making data available to a foreign controller/processor requires a Centre Licence plus compatible/integrated activity and a legitimate interest, and protection abroad **not lower than** in Egypt.
  - **Arts. 23–26:** separate cross-border Licence (legal persons) and Permit (natural persons) categories, with distinct application contents (destination, nature of activity, data categories, security systems, **temporary and final storage locations** and in-transit protection, purpose, storage details per Centre templates, data categories/volume/retention). Applications via the dedicated electronic gateway.
  - **Art. 26:** **90 working days** to decide; **non-response = deemed rejection**.
  - **Art. 27:** fee = **50%** of the controller/processor licence/permit fee.
- **Sovereignty carve-out for surveillance data:** Reg. Art. 31(1)(3) — public-place visual-surveillance recordings must not be transferred/available/recorded/processed outside Egypt except for legally prescribed reasons.
- **Sector overlay:** Reg. Arts. 3(8) and 4(8) — data obtained under a sectoral law is limited to the volume/type that law permits; where that law is silent on retention/security/transfer, the PDPL and Regulations apply to the additional data requested. **The CBE regime is largely carved out of Law 151/2020** (Issuance Art. 3(6), except money-transfer and foreign-exchange companies).

### Status of adequacy decisions / SCCs — honest assessment
- ❌ **No published list of countries deemed to provide an adequate level of protection was located.** Article 16(2) of the Regulations empowers the Centre to issue one, but I found no published decision or list. DataGuidance, DLA Piper and Legal 500 all describe the mechanism without identifying any designated country. Legal 500's own cross-border article refers only to a **"potential adequacy whitelist [that] may, over time, reduce friction"** — i.e. it does not yet exist.
- ⚠️❌ **Standard contractual clauses (SCCs) and binding corporate rules (BCRs):** a Legal 500 cross-border article asserts these are "contemplated" and "subject to regulatory approval", and describes them in some detail. **I did not find SCC or BCR language anywhere in the text of Decision 816/2025 (Arts. 16–27) or Law 151/2020.** The Commission's article also self-describes a "**potential** adequacy whitelist" and frames SCCs/BCRs as what the framework "contemplates". **Treat SCCs/BCRs as UNVERIFIED.** Do not tell a client that an SCC is an available transfer mechanism in Egypt without checking for a Centre decision or policy document first.
- ⚠️ **What is verified:** the only two routes in the text of Decision 816/2025 are (i) a Centre cross-border Licence/Permit (which requires the Centre's adequacy assessment of the destination + the Data Subject's consent), and (ii) the Law's Art. 15 exception grounds (which also require express consent). Plus PDPC authorisation of a **transitional one-year compliance period** under the Regulations for existing processing.
- **Practical note:** as of the last checks, the **Centre's electronic portal for licence/permit applications was not yet operational** and application forms had not been published (Shand & Partners, 11 Jan 2026). dsn group (20 May 2026) reported the portal "expected to go live by mid-June 2026". ❌ **UNVERIFIED** whether it is now live.

### Sources
- Legal 500 cross-border deep dive: `https://www.legal500.com/guides/hot-topic/strategic-challenges-and-opportunities-in-cross-border-data-transfers-under-egypts-personal-data-protection-regime/`
- DLA Piper Egypt: `https://www.dlapiperdataprotection.com/?t=law&c=EG`
- Shand & Partners: `https://www.shandpartners.com/insights/briefings/telecoms-media-technology/the-issuance-of-the-executive-regulations-of-the-data-protection-law-and-the-establishment-of-the-data-protection-centre/`
- Decision 816/2025 Arabic text: `https://alhasswalawfirm.com/law-library/decree-816-2025`
- **As of:** 2026-10-12

---

## 10. Consolidated penalties table

| Instrument | Provision | Penalty | Verified |
|---|---|---|---|
| **PDPL 151/2020** | Attached Law 36 | Unauthorised collection/processing/divulging: fine **EGP 100k–1m**; aggravated: **imprisonment ≥ 6 months** + fine **EGP 200k–2m** | ✅ |
| | Attached Law 37 | Refusing data-subject rights: fine **EGP 100k–1m**; collecting outside Art. 3 conditions: fine **EGP 200k–2m** | ✅ |
| | Attached Law 38 | Breach of controller/processor/breach duties (Arts. 4, 5, 7): fine **EGP 300k–3m** | ✅ |
| | Attached Law 39 | Legal representative breach of DPO duty: fine **EGP 200k–2m** | ✅ |
| | Attached Law 40 | DPO breach: fine **EGP 200k–2m**; negligent: **EGP 50k–500k** | ✅ |
| | Attached Law 41 | Unauthorised sensitive-data processing: **imprisonment ≥ 3 months** + fine **EGP 500k–5m**, or either | ✅ |
| | Attached Law 42 | Cross-border breach: **imprisonment ≥ 3 months** + fine **EGP 500k–5m**, or either | ✅ |
| | Attached Law 43 | E-marketing breach: fine **EGP 200k–2m** | ✅ |
| | Attached Law 44 | Center staff confidentiality breach: fine **EGP 300k–3m** | ✅ |
| | Attached Law 45 | Licensing breach: fine **EGP 500k–5m** | ✅ |
| | Attached Law 46 | Obstructing enforcement officer: **imprisonment ≥ 6 months** + fine **EGP 200k–2m**, or either | ✅ |
| | Attached Law 47 | Actual manager: same penalties; legal person jointly liable | ✅ |
| | Attached Law 48 | Publication in 2 dailies + open electronic networks at offender's cost; **recidivism doubles both limits**; **attempt = half** | ✅ |
| | Attached Law 49 | Settlement: **half the minimum fine** pre-proceedings; **half the maximum or the fine imposed (greater)** post-proceedings/pre-final-judgment | ✅ |
| | Attached Law 26 | Administrative fee caps: **Licence ≤ EGP 2,000,000**; **Permit / Accreditation ≤ EGP 500,000** | ✅ |
| | Attached Law 2 | Data-subject rights fee cap: **EGP 20,000** | ✅ |
| | Decision 816/2025 Art. 19 | Combined controller/processor licence fee: exempt ≤ 100k records; EGP 200 → EGP 1,000 across 101k–1m; above 1m, banded up to statutory cap **EGP 666,666/year (EGP 2m over 3 yrs)**; controller-only or processor-only = **50%** | ✅ |
| | Decision 816/2025 Art. 20 | Permit fee: exempt ≤ 25k records; EGP 10,000–125,000 depending on volume × duration; controller-only/processor-only = **50%** | ✅ |
| | Decision 816/2025 Arts. 27, 29, 31, 34 | Cross-border = **50%** of licence fee; e-marketing = **10%** (own) / **25%** (third-party); CCTV = **EGP 1,000/3 yrs** or **EGP 500/yr**; consultancy accreditation = **EGP 5,000/yr** (natural person) / **EGP 50,000/yr** (legal person), 3-year validity | ✅ |
| **Consumer Law 181/2018** | Art. 64 | Fine **EGP 10k–500k** or 2× product value, whichever greater; service-centre closure up to 6 months | ✅ |
| | Art. 65 | Fine **EGP 30k–1m** or 2× product value | ✅ |
| | Art. 66 | Fine **EGP 50k–2m** or 2× product value | ✅ |
| | Art. 67 | Fine **EGP 20k–500k** (obstructing enforcement; non-production of documents; false information) | ✅ |
| | Art. 68 | Fine **EGP 50k–1m** or 2× the amount agreed with the advertising medium | ✅ |
| | Art. 69 | **Recidivism: both fine limits doubled** | ✅ |
| | Art. 70 | Defect-reporting breach: fine **EGP 50k–2m** or goods value; if life endangered / addiction or incurable disease: **imprisonment + fine EGP 100k–2m**, or either | ✅ |
| | Art. 71 (**as amended by Law 20/2024**) | Strategic-product withholding: **imprisonment ≥ 1 year** + fine **EGP 150k–3m** or goods value, whichever greater; **recidivism 2–5 years + both limits doubled**; **confiscation**, **store closure ≤ 6 months**, judgment in **2 dailies**, and **possible licence cancellation** | ⚠️ (content ✅; gazite reference ❌) |
| | Art. 72 | Disability / incurable or addiction disease: **imprisonment + fine EGP 100k–1m** or product value (Penal Code Art. 17 may reduce custody by up to 1 year). **Death: life imprisonment + fine EGP 200k–2m** or product value | ✅ |
| | Art. 73 | **Mandatory restitution** of the product's value to the consumer where the consumer is entitled to a refund | ✅ |
| | Art. 74 | Actual manager: same penalties; legal person jointly liable | ✅ |
| | Art. 75 | Publication of judgment (1 daily + electronic sites) at offender's cost; **Agency must publish final convictions on its website for 3 years** | ✅ |
| | Art. 76 | Art. 13 discrimination offence: prosecution **only on written request of the Prime Minister (or delegate)** | ✅ |
| | Art. 59 | Reconciliation: pre-referral **minimum fine → ⅓ of maximum**; post-referral **3× minimum → ½ maximum**; not available where injuries or death resulted | ✅ |
| | Arts. 60, 61 | "Consumer Friend" certificate ≤ **EGP 20,000** per retail outlet; complaint-outcome certificate ≤ **EGP 200** | ✅ |
| **Decree 822/2019** | Art. 45 | Consumer Friend certificate: **EGP 1,000 / 2,000 / 3,000 / 5,000 / 10,000** by capital or goods-display value tier | ✅ |
| **Telecom Law 10/2003** | Arts. 71–86 | See the table in §8 — highest bands: Art. 77 **imprisonment 1–5 years + fine EGP 2m–5m** for unlicensed equipment manufacture/marketing (rigorous imprisonment for national-security purpose; doubled on recidivism); Art. 72 **imprisonment 6 months–5 years + fine EGP 50k–500k** for unlicensed operation; Art. 85 **10× overcharge per user affected** | ✅ |
| **E-signature Law 15/2004** | — | ❌ **UNVERIFIED — needs primary-source check.** Penalties in the E-Signature Law and its Executive Regulations were not verified. Do not state amounts. | ❌ |

---

## 11. GDPR → Egypt comparison (for agents trained on GDPR)

| Point | GDPR | Egypt (Law 151/2020 + Decision 816/2025) | Trap |
|---|---|---|---|
| **Regulator** | Independent DPAs (Art. 51), one-stop-shop | **Personal Data Protection *Center* (PDPC)** — a **public economic authority subordinate to the MCIT Minister**, Board **chaired by that Minister**, with **Ministry of Defence, Ministry of Interior, GIS and Administrative Control Authority representatives on the Board** (Attached Law Art. 20); CEO appointed by **Prime Minister** (Art. 23). Board decisions by **two-thirds majority of those present** (Art. 22). | ❌ Not independent. Not a "Data Protection Authority". Do not cite GDPR-style "supervisory authority independence" for Egypt. |
| **Territorial scope** | Art. 3 — offering goods/services to, or monitoring, data subjects in the Union | **No offering/monitoring clause.** Scope is "electronic processing by any Holder, Controller or Processor" (Issuance Art. 1). Extraterritorial reach runs only through **criminal jurisdiction** and is **limited to Egyptian nationals and residents** (Issuance Art. 2). | ❌ Do not port GDPR Art. 3(2) reasoning. |
| **Number of actors** | Controller + Processor | **Three: Holder (الحائز) + Controller + Processor.** A Holder has no decision-making authority — it merely possesses/retains the data. Liability analysis must accommodate a third role. | ❌ Easy to miss. |
| **Lawful bases** | Art. 6(1) — six bases incl. **vital interests (d)** and **legitimate interests (f)** as a standalone balancing test | **Four grounds** in Attached Law Art. 6: consent; contract necessity / legal-act / asserting or defending legal rights; legal obligation, investigating-authority order or court judgment; performing the Controller's obligations or exercising legitimate rights **unless conflicting with the data subject's fundamental rights and freedoms**. **No express vital-interests basis**; no standalone balancing legitimate-interests test. But the **opening rule is consent-first**: no collection/processing/disclosure without **express consent except where authorised by law** (Art. 2). | ⚠️ The PDPC's *Lawful Basis* guideline is reported to list **six** bases. Cite the statutory four; attribute the six to guidance. |
| **Consent** | Art. 4(11), 7 — freely given, specific, informed, unambiguous; Art. 7(4) explicit for special categories; Art. 7(3) as easy to withdraw as to give | **Express** consent (Art. 2). **Executive Regulations Art. 2(2): providing personal data to receive lawful services or transactions constitutes consent — but only for that purpose**, and any other use needs **prior** consent. **Center approval is required for the collection mechanisms and for the consent-capture mechanism** (Art. 2(3)). PDPC Consent guideline: **written (paper or electronic)**, **Arabic as the primary language**, **separate** from privacy notices and T&Cs, requiring a **clear affirmative action**. | ⚠️ "Consent by providing data to get a service" is a quasi-deemed-consent rule unique to Egypt. |
| **Sensitive / special-category data** | Art. 9 — general prohibition with ten exceptions | **Positive licensing model:** Art. 12 — may not collect/transfer/store/keep/process/make available **except under a Licence issued by the Center**, plus **express written consent** outside statutorily authorised cases, plus **guardian consent for children's data**. Reg. Art. 14 adds necessity, no-harm, Centre security standards, records, and a ban on **profiling/tracking/monitoring children's behaviour**. | ❌ Not an Art. 9-style prohibition list. It is "licence + written consent". |
| **Children's data** | Art. 8 — information society services offered directly to a child; consent age 13–16 depending on member state | **All children's data are Sensitive Personal Data by definition** (Art. 1). Reg. Art. 15: **< 15** → guardian's **explicit written consent** stating its time scope; **15–18** → child or guardian consents per Centre mechanisms. Child participation in a game/activity must not be conditioned on data beyond necessity (Art. 12). | ⚠️ Egyptian age thresholds are **not** GDPR's 13–16 range. |
| **Data portability** | Art. 20 — explicit right | **No portability right.** | ❌ Do not promise portability in Egypt. |
| **Right to object** | Art. 21 — unconditional right to object to direct marketing | Art. 2(6) — right to object **only where processing or its results conflict with the data subject's fundamental rights and freedoms**. Marketing objection is governed separately by Arts. 17–18 (must be able to reject/withdraw). | ⚠️ The general objection right is **qualified** in Egypt. |
| **Fees for rights** | Art. 12(5) — free by default | Data Subject **must pay** for exercising rights, except the breach-notification right; Centre sets the fee, **capped at EGP 20,000** (Art. 2). | ❌ Materially different. Commentary notes EGP 20,000 ≈ 2.5× the average Egyptian monthly salary. |
| **Response deadlines** | 1 month, extendable by 2 months | **6 working days** for requests to Holder/Controller/Processor (Arts. 10, 32); **6 working days** to decide a "make data available" request (Art. 10, with **deemed rejection on silence**); **30 working days** for the Centre to decide a complaint (Art. 33); respondent must comply in **7 working days** (Art. 33). | ⚠️ Much tighter. Silence = rejection for data-available requests. |
| **Breach notification** | Art. 33 — notify the supervisory authority **within 72 hours**, *where feasible*, unless unlikely to result in risk; notify data subjects **without undue delay** | **72 hours** to the Centre via portal or hotline (Art. 7; Reg. Art. 5); **immediately** if national-security related, with extra content; **data subjects within 3 working days of the Centre report**, via the channel specified at consent; six prescribed register entries. There is **no "unlikely to result in risk" threshold** — the 72-hour duty is unconditional on becoming aware. | ❌ No risk threshold. |
| **DPIA / impact assessment** | Art. 35 — mandatory for high-risk processing | ❌ **No DPIA obligation appears in Law 151/2020 or Decision 816/2025.** ⚠️ The PDPC's *Data Users* guideline is reported to cover "impact assessments", and RoPA templates reportedly include an "impact assessments" field. Treat any Egyptian DPIA obligation as **UNVERIFIED**; check for a Centre decision before relying on it. | ❌ Do not assert an Art. 35 equivalent. |
| **Licensing / prior authorisation** | No general authorisation; Art. 36–39 only for special categories, large-scale processing and public-sector processing | **The defining feature.** Controllers **and** processors need a Centre **Licence** or **Permit** before handling personal data at all (Arts. 4(1), 5(1); Reg. Arts. 2(1), 3(1), 4(1)). **Separate licences** for direct electronic marketing (Art. 17; Reg. Arts. 28–30), **public-place visual surveillance** (Reg. Art. 31, incl. an effective **ban on facial recognition** unless legally provided or explicitly consented), and **cross-border transfer** (Reg. Arts. 23–27). Fees are **volume-based and charged annually**. | ❌ This is the single biggest behavioural difference. A GDPR-compliant entity may still be unlicensed and non-compliant in Egypt. |
| **Representatives of foreign controllers** | Art. 27 — EU representative for Art. 3(2) entities | Reg. Arts. 3(6) and 4(5) — a controller/processor **outside Egypt with no branch or representative office** must appoint a representative **in Egypt** (company branch, authorised office, or, for a natural person, an agent) **approved by the Centre** for the licence/permit term. This is a **representative/localisation requirement**, broader than GDPR Art. 27. | ⚠️ Applies to **processors** too, and needs Centre approval. |
| **Records of processing** | Art. 30 ROPA, accountability-based | Similar in substance (Attached Law Arts. 4(9), 5(9); Reg. Arts. 2, 3, 4 prescribe the register content), but the Centre's **inspectors hold judicial-enforcement-officer status** (Attached Law Art. 34) and can inspect on site. There is **no self-certification-only posture**. | — |
| **DPO** | Art. 37 — mandatory only for large-scale regular systematic monitoring or large-scale special-category processing | **Broadly mandatory**: the legal representative of **every** legal-person controller/processor must appoint a **specialised employee inside its own structure**, register them with the Centre and **publicly announce** the appointment (Art. 8). Under the Regulations the DPO must be **coded, exam-tested, categorised (A/B/C)** and file an **annual report**. A natural-person controller/processor is itself responsible. | ⚠️ Far broader than GDPR Art. 37. |
| **Enforcement** | Art. 58 — administrative fines up to **€20m or 4% of global annual turnover** | **Egyptian fines are EGP-denominated and capped** at **EGP 5,000,000** for the gravest offences (sensitive data, cross-border, licensing). There is **no turnover-based element**. Proceedings are criminal misdemeanours before the **Economic Courts**, with **mandatory publication**, **doubled penalties on recidivism**, and a **reconciliation/settlement** mechanism (Art. 49) allowing payment of **half the minimum fine pre-proceedings** or **half the maximum post-proceedings**. Administrative sanctions (Art. 30) include **publication** and **Center technical supervision at the offender's cost**. | ❌ Comparing EGP 5m to a GDPR 4%-of-turnover fine is misleading. Also note the **settlement discount** is unique. |
| **Cross-border transfers** | Arts. 44–49 — adequacy decisions, appropriate safeguards (SCCs/BCRs), derogations | **Licence-led**: Centre Licence/Permit after assessing destination adequacy **plus** the Data Subject's consent, destination-specific and updateable (Reg. Art. 16). Law Art. 15 provides seven **consent-gated** exceptions. The Centre may designate adequate countries on three statutory criteria (Reg. Art. 16(2)–(3)). ❌ **No adequacy list located; SCCs/BCRs not found in the enacted text.** | ❌ Do not tell a client an SCC works in Egypt. |
| **Language** | No requirement | **Arabic is mandatory** in a number of places: consumer-facing advertisements, documents, invoices, receipts and **electronic documents** (Consumer Law Art. 5); privacy notices and consent requests (PDPC guidelines). | ⚠️ Easily missed by foreign sellers. |
| **Complaints / redress** | Art. 77 — right to lodge a complaint with a DPA; Art. 78–79 — judicial remedy; Art. 82 — compensation | Attached Law Art. 33 — complaint to the Centre with a **30-working-day** decision and **7-working-day** compliance duty; court recourse preserved. Economic Courts have jurisdiction over both **civil/commercial disputes and criminal offences** under the Consumer Law (Consumer Law Issuance Art. 2). | — |
| **Regulatory guidance** | EDPB Guidelines are not binding but influential | PDPC guidelines (consent, lawful basis, e-marketing, DPO, DPO categories, data users, principles, RoPA, licences/permits, privacy notice) **do not carry the force of law** — but they are the best evidence of enforcement expectations. | ⚠️ Attribute guidance as guidance. |

---

## Cross-cutting notes — what a GDPR-trained agent gets wrong about Egypt

1. **The regulator's name is wrong in most databases.** It is the **Personal Data Protection Center (مركز حماية البيانات الشخصية)**, not a "Data Protection Authority" (جهاز حماية البيانات الشخصية). DLA Piper, TrustArc, DataGuidance and Kennedys all use "Authority". It is a **public economic authority subordinate to the MCIT Minister**, with the Prime Minister appointing its CEO and **security-service representatives sitting on its Board**. Any answer implying GDPR-style regulator independence is wrong.
2. **The regime was dormant for almost five years and only became operational on 2 November 2025.** The Licensing requirement, the DPO registry, technical standards, fee schedule and breach portal were all dormant until Decision 816/2025. **The compliance deadline is 1 November 2026** — i.e. within weeks of this corpus's "as of" date.
3. **"MCIT Decision 816 of 2025" is correct; "Prime Ministerial Decree 816" is not.** Several English outlets (Kennedys, LinkedIn reposts) misdescribe it. It is a decision of the **Minister** of Communications and Information Technology, signed by **Dr. Amr Talaat**, gazetted in **Al-Waqa'i' al-Misriyya Supplement, Issue 244 (Supplement A), 1 November 2025**, **in force 2 November 2025**.
4. **Ignore every source saying the Executive Regulations were issued on 25 December 2025.** That date is when law firms received the text, not a legal date. Verified gazette date: **1 November 2025**.
5. **Licensing is the regime, not a side-issue.** Any GDPR compliance narrative that omits "obtain a Licence or Permit from the PDPC before processing" is wrong for Egypt. Fees are **annual and volume-based**, are **exempt below 100,000 records** for controllers/processors (below 25,000 for permits), and are charged **again** for cross-border, marketing, and CCTV authorisations.
6. **Egyptian law has two layers of article numbering inside Law 151/2020.** "Art. 6" means the *Issuance Article* 6 (the 1-year compliance window) or the *Attached Law* Art. 6 (lawful bases), depending on context. Always disambiguate — this is a common source of citation error.
7. **Kennedys' claim that "Article 2 of the PDPL confirms the law applies to any person who processes personal data relating to individuals located in Egypt" is wrong.** Art. 2 is the **criminal-jurisdiction** provision (Egyptian nationals anywhere, residents, and non-residents only where the data relate to Egyptians or residents). Art. 1 is the scope provision, and it says nothing about targeting or monitoring.
8. **There is no data portability right, and no DPIA in the enacted text.** Both are common assumptions imported from GDPR. The PDPC's *Data Users* guideline is *reported* to cover impact assessments — verify before relying on it.
9. **Egypt's consent model is odd in both directions.** Consent is the **default** (no processing without express consent except where authorised by law), *yet* the Executive Regulations deem the act of providing data to obtain a lawful service or transaction to be consent for that purpose only. And the PDPC requires **Center approval of the collection and consent-capture mechanisms** — a public-authority veto over how you ask for consent.
10. **The right to object is qualified.** Art. 2(6) applies only where processing or its results conflict with the data subject's fundamental rights and freedoms — not unconditionally as in Art. 21 GDPR.
11. **Data subject rights can cost up to EGP 20,000.** Art. 2's final paragraph. Commentators note this is ~2.5× the average Egyptian monthly salary.
12. **No risk threshold on breach reporting.** Unlike Art. 33(1) GDPR, Egypt's 72-hour duty attaches on **becoming aware**, with a separate **immediate** trigger for national-security-related breaches.
13. **Cross-border transfers need a licence plus consent, per destination.** There is no published adequacy whitelist and no SCC/BCR route found in the enacted text. Marketing the existence of a "whitelist" or "standard contractual clauses" mechanism in Egypt is **UNVERIFIED and probably wrong today**.
14. **Arabic is mandatory in consumer-facing documentation.** Consumer Law Art. 5 requires advertisements, invoices, receipts, contracts and **electronic documents** to be in Arabic, bilingual only if one language is Arabic. This catches foreign sellers and marketplaces.
15. **Distance contracts in Egypt are unusually well regulated.** 14-day no-reason withdrawal (Arts. 17 and 40), a 7-working-day order-correction window (Art. 38 + Reg. Art. 25), a mandatory post-contract written confirmation (Art. 38), and specific delayed-delivery withdrawal rules with **supplier-borne** return costs (Art. 40). Compare with GDPR, which says nothing about distance selling.
16. **The Consumer Protection Agency is a Prime Ministerial body**, not an independent regulator, and its decisions are **final and appealable only before the Administrative Court** (Art. 58).
17. **Encryption in telecom is effectively restricted** (Telecom Law Art. 64(1): NTRA **and** Armed Forces **and** national security approval required), while Art. 64(2) imposes a **standing lawful-interception capability** duty on operators at their own expense and an obligation to collect accurate user data from citizens and State entities. A "privacy by encryption" argument does not land the same way in Egypt as in the EU.
18. **National security carve-outs are broad and operational.** Issuance Art. 3(5) lets the National Security Authorities direct the Centre to require data modification/erasure/non-disclosure; Data held by the National Security Authorities and (outside money-transfer and FX companies) the CBE is excluded entirely from the PDPL.
19. **AI training is mentioned but not governed.** Reg. Art. 4(7) is a one-line principles-based obligation on **processors**. Do not extrapolate an AI-specific regime from it.
20. **Money transfers and FX companies sit outside the CBE carve-out** and therefore **inside** the PDPL — an easy miss.
21. **Be careful with Egypt's e-signature statute number.** It is **Law 15 of 2004**, not 15/2020 (which is Saudi Arabia's e-commerce law). And the **Executive Regulations' issuing decision number is UNVERIFIED** — do not cite one.
22. **Law 181/2018 was amended by Law No. 20 of 2024** (Art. 71 substituted — strategic-product hoarding penalties raised to EGP 150k–3m plus licence cancellation). The gazette reference is unverified, and one source says the number is **19/2024**. Check before filing.
23. **There is no Egyptian e-commerce law.** E-commerce is governed by Law 181/2018's distance-contract chapter, Law 15/2004 on e-signatures, and general commercial/company law. Don't invent an "Egyptian E-Commerce Law".

---

## Open questions for primary-source verification

| # | Question | Why it matters | Suggested primary source |
|---|---|---|---|
| 1 | **Official Gazette issue number and publication date for Law 151/2020.** Sources give "15 July 2020"; the gazette issue number was not seen. | Fixes the commencement date (15 October 2020) and the Art. 4 six-month deadline for Executive Regulations. | Al-Waqa'i' al-Misriyya; MCIT; or the Court of Cassation legislation portal referenced by alhasswalawfirm |
| 2 | **Exact Official Gazette issue number for Decision 816/2025.** "Issue No. 244 (Supplement A), 1 November 2025" is from the English translation's masthead and the alhasswalawfirm transcription; verify against the gazette itself. | Core citation. | Al-Waqa'i' al-Misriyya issue 244 (تابع أ) |
| 3 | **Is Decision 816/2025 amended?** The transcription is captioned "(محدثا حتي عام ٢٠٢٦)". | Fee schedules and article numbers may have shifted. | PDPC website + Al-Waqa'i' al-Misriyya |
| 4 | **Official Gazette reference for Law No. 20 of 2024** (and whether the number is 19 or 20). | Only amendment to the Consumer Law located. | Al-Waqa'i' al-Misriyya; cpa.gov.eg legislation page |
| 5 | **Is Law 181/2018 subject of a further bill?** A secondary reference suggests the House of Representatives approved an Art. 71 amendment in "February last year" (i.e. Feb 2026), possibly a further layer. | Would change the Art. 71 text again. | cpa.gov.eg legislation page; Al-Waqa'i' al-Misriyya |
| 6 | **Is Decree 822/2019 amended?** Transcriptions are captioned "updated until 2025". | Distance-contract exclusion list and complaint mechanics. | cpa.gov.eg; Al-Waqa'i' al-Misriyya |
| 7 | **Has the PDPC published an adequacy list of countries?** | Determines whether any destination can be treated as pre-approved. | `portal.pdpc.gov.eg` policies/decisions (needs a browser — the site is a JS SPA) |
| 8 | **Do PDPC-approved SCCs or BCRs exist?** Asserted by Legal 500; absent from the enacted text. | Would be the main non-licence transfer route for multinationals. | PDPC decisions/portal; Centre circulars |
| 9 | **Is the PDPC licence/permit electronic portal operational, and are the application forms published?** Shand (Jan 2026) said no; dsn group (May 2026) expected mid-June 2026. | Determines whether any deadline is practically achievable. | `portal.pdpc.gov.eg/services` |
| 10 | **The PDPC decision fixing the data-subject rights fee** (capped at EGP 20,000 by Attached Law Art. 2). Not located. | The actual fee charged to consumers. | Al-Waqa'i' al-Misriyya; PDPC decisions page |
| 11 | **Is there an impact-assessment (DPIA) obligation?** Reported only in PDPC guidelines; absent from the enacted texts. | Large difference from GDPR for risk assessments. | PDPC *Data Users* and *RoPA* guidelines (obtainable via a browser) |
| 12 | **Verify the DPO Category A/B/C scheme** (experience bands, 3-year reassessment) — sourced only from a law-firm summary. | Affects who can be appointed as DPO. | PDPC DPO Guidelines + DPO register |
| 13 | **Issuing decision number and year of the E-Signature Law Executive Regulations.** Secondary sources say "Resolution 109 of 2005" and "Prime Ministerial Decision No. 634 of 2008"; neither confirmed. Also whether the Regulations were later amended. | Full legal effect of e-signatures depends on ITIDA certification under those Regulations. | `itida.gov.eg`; Al-Waqa'i' al-Misriyya |
| 14 | **Court of Cassation Judgment No. 17689 of Judicial Year 89** (email as evidence under Law 15/2004) — verify the case number. | Evidentiary weight of email in e-commerce disputes. | Egyptian Court of Cassation judgments database |
| 15 | **Has the Cybersecurity Law 175/2018 been amended?** | Interaction with Law 151/2020 for providers. | Al-Waqa'i' al-Misriyya |
| 16 | **Has the Telecommunications Law 10/2003 been amended since 2003?** The NTRA's own translation is undated on its face. | Arts. 64, 73, 81 penalties are the telecom-secrecy teeth. | Al-Waqa'i' al-Misriyya; NTRA legislative updates page |
| 17 | **Gaslighting check on "Personal Data Protection Authority":** confirm there has never been a presidential or prime-ministerial instrument renaming the Center into a "هيئة/جهاز". | Prevents an agent citing a non-existent regulator. | Al-Waqa'i' al-Misriyya; PDPC founding decisions |
| 18 | **Confirm there is no enacted Egyptian e-commerce law or MCIT e-commerce regulation.** | Prevents citing a non-existent instrument. | MCIT legislation page; WIPO Lex Egypt profile |
| 19 | **Verify Law 15/2024 (Commercial Law / Commercial Register) and Law 194/2020 (CBE) interaction** with the PDPL carve-outs — in particular whether the CBE's own data rules have been aligned with the PDPL for money-transfer and FX companies. | Determines whether fintech data is PDPL-regulated in practice. | CBE regulations; PDPC sector guidance |
| 20 | **Check whether any PDPC enforcement action or administrative sanction has been published.** The Regulations took effect 2 Nov 2025 and the compliance deadline is 1 Nov 2026, so enforcement is imminent but I found no published case. | Precedent value; realistic penalty expectations. | PDPC news/annual report (Law Art. 19 requires an annual report) |

---

*Compiled 2026-10-12. Every article number, fine amount, date and gazette reference in this file was read from a retrieved source, not from memory. Items marked ⚠️ or ❌ must be checked against the Arabic Official Gazette before being cited in advice, a filing or a contract.*