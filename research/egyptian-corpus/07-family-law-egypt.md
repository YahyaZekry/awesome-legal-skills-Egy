# Egyptian Family Law (Personal Status) — Verified Reference Corpus
# قانون الأحوال الشخصية في مصر — المرجع التشريعي

**Purpose:** a citation-safe reference for an AI agent helping a **non-lawyer in Egypt** with personal-status (أحوال شخصية) problems —
marriage and its documentation, divorce by each of its routes, maintenance (نفقة), custody and visitation (حضانة، رؤية، استضافة),
parentage (نسب), inheritance and wills, the family courts and what happens after judgment.
Every article number below was read out of a retrieved primary or official-secondary text. **Nothing is asserted from memory.**
**As-of date for the whole file: 2026-10-19.**

⚠️ **Each section carries its own `As of:` line — that is the date *that section* was last read against a source.**
Everything in this file was first built on **2026-10-19**; nothing here stands on a date earlier than that.

⚠️⚠️ **THE SINGLE MOST IMPORTANT THING IN THIS FILE:** the rules below are the rules **as they still stand under the
1920/1929/1985/2000/2004 laws**. As of **19 October 2026 there is still no new consolidated personal-status law**.
Three government bills (Muslim family law; Christian family law; a Family Support Fund) are sitting in a **joint parliamentary
committee** and have not been debated article-by-article — see **§1**. Anything an agent says about "the new personal status law"
must be framed as **what is proposed**, never as what the law is. **§1 is the section to read first.**

**Relationship to the other corpus files:** `05-tenancy-egypt.md` covers civil procedure figures and the civil courts;
`03-employment-courts-aml-banking.md` covers the general court structure (⚠️ its pecuniary figures are stale, see 05 §9.2);
`06-criminal-procedure-egypt.md` covers the criminal process — this file gives the **penal articles** that family cases actually
trigger and cross-refers there for how a criminal case runs. Files `01`, `02`, `04`, `08` are not relevant here.

## How to read the confidence markers

| Marker | Meaning |
|---|---|
| ✅ **verified** | I read the article text or the official gazette reference in a retrieved document, and I quote the source URL. |
| ⚠️ **PARTIAL** | The instrument is verified; a specific article number or detail inside it is **not**. Describe the concept, never the number. |
| 🟡 **UNVERIFIED — needs primary-source check** | I could not confirm it. I say what I searched. Do not cite. |
| ❌ **DOES NOT EXIST (as described)** | I searched specifically for it and found it does not exist under that citation or in that form. The premise is wrong. |

---

## ⚠️ CORRECTIONS TABLE — read this before citing anything in this file

Twenty-one things a model — or a person who has been told "the law says" — will get wrong. Several of them are the *most commonly
repeated* statements about Egyptian family law on the Arabic internet, and several were wrong in the brief this file was built from.

| # | The common assumption (or the brief's guess) | What the retrieved texts actually say |
|---|---|---|
| 1 | "The **marriage age of 18** is in the Child Law." | ❌ **WRONG LAW.** It is **Art. 31 bis of the Civil Status Law (قانون الأحوال المدنية) No. 143 of 1994**, added by **Law 126/2008**: «لا يجوز توثيق عقد زواج لمن لم يبلغ من الجنسين ثماني عشرة سنة ميلادية كاملة.» The misattribution is understandable and self-inflicted by the legislator: the *official heading* of Law 126/2008 in the Gazette is «**قانون رقم ١٢٦ لسنة ٢٠٠٨ بتعديل بعض أحكام قانون الطفل**» — read off the primary Gazette PDF page 1 — and its long title amends the Child Law 12/1996, the **Penal Code 58/1937** and the **Civil Status Law 143/1994**. The Child Law itself only *defines* the child (Art. 2, as replaced by the same law: «كل من لم يجاوز ثمانية عشرة سنة ميلادية كاملة»). **Never cite "Child Law Art. 31 bis" for the marriage age.** |
| 2 | "Marrying off a child under 18 is a **crime** in Egypt — the penalty is up to **200,000 EGP**." | ❌ **NOT ENACTED — this is a bill, not law.** The prohibition on *documenting* the marriage is real (Art. 31 bis of Law 143/1994) but its only sanction is **disciplinary** against the registrar: «**ويعاقب تأديبياً** كل من وثق زواجاً بالمخالفة لأحكام هذه المادة». The criminal law in force is **Penal Code Art. 227** only: up to **2 years and/or a fine up to 300 EGP** for a party who lies about age to prove a spouse has reached the legal age, and up to imprisonment **or a fine up to 500 EGP** for the person legally empowered to conclude a marriage contract who **knows** one party is under age. The **1 year + 50,000–200,000 EGP** figure comes from the **2022 draft law banning child marriage** (approved in principle by the Constitutional & Legislative Committee on **3 July 2022**, never enacted). The "200,000 EGP" number also circulates as a *human-trafficking* penalty — a different offence. |
| 3 | "**DNA (البصمة الوراثية) proves paternity** in an Egyptian court." | ❌ **THERE IS NO SUCH STATUTE.** No Egyptian statute gives a DNA test binding force in a نسب claim. Paternity follows the **الولد للفراش** rule (a child of a valid subsisting marriage is attributed to the husband), and the DNA report is an **expert opinion (تقرير خبير)** which the court weighs and is **not bound by**; nor does the law compel anyone to submit to testing. Some of this is court practice rather than statute, so this row is a *negative finding* about the statute book, not a claim about how every judge rules. See §6.3. |
| 4 | "A **will in favour of an heir is void** in Egypt (الوصية لوارث باطلة)." | ❌ **WRONG under the codified law.** **Law 71/1946 Art. 37**: a will up to **one-third** of the estate is valid **whether the legatee is an heir or not**, and takes effect **without the heirs' consent**; only what exceeds one-third is suspended on the heirs' consent given **after the testator's death**. What the classical *shari'a* debate is about (a bequest to an heir) is not what the Egyptian statute says. See §7.1. |
| 5 | "Not paying maintenance is **Penal Code Art. 292**." — and "the fine is **500 EGP**." | ⚠️ **Art. 293, not 292 — and the fine figure everyone quotes is STALE.** **Art. 293** = failure to pay maintenance/custody/housing/nursing money under a final enforceable judgment, while able, for **3 months after notification** → up to **1 year** and/or a fine, **on complaint only**. **Art. 292** = a parent's or grandparent's failure to hand over a minor under a judicial custody/abduction decision, or abducting him — a different offence. The 2004 Fund law expressly names «**المادة (٢٩٣)** من قانون العقوبات» (**Law 11/2004 Art. 3**, as replaced by **Law 113/2015**) — an independent confirmation of the number. ⚠️ **On the fine: Law 6/2020 rewrote Art. 293** and the current text is quoted in 2026 reporting as «**غرامة لا تتجاوز خمسة آلاف جنيه**» — **EGP 5,000, not 500** — together with **suspension of the convict's government services** until payment. ⚠️ **Many current news pages still print "500 EGP" from pre-2020 copies.** See §4.5 and §9.1, and the source conflict in §12.
| 6 | "Custody ends at 10 for a boy and at marriage for a girl." | ❌ **STALE.** **Law 25/1929 Art. 20(1) as replaced by Law 4/2005** (Gazette No. 4 bis, 4 March 2005) ends **women's custody at 15 for a girl *and* a boy alike**: «ينتهى حق حضانة النساء ببلوغ الصغير أو الصغيرة سن الخامسة عشرة.» After 15 the child **chooses** to stay with the custodian, **without custody pay**, until the boy reaches majority (الرشد) and until the girl marries. The 10/until-marriage split is the pre-2005 rule. See §5.2. |
| 7 | "Grandparents may only claim **رؤية** of a grandchild if the parents are absent." | ❌ **STRUCK DOWN.** The words «عند عدم وجود الأبوين» in Art. 20 of Law 25/1929 were held unconstitutional by the **Supreme Constitutional Court, Case 37 of judicial year 33, session 12 May 2013 (2 Rajab 1434)** — published **Gazette No. 21 bis, 26 May 2013**. Grandparents claim رؤية in their own right. See §5.4. |
| 8 | "The divorcer must always **provide housing** for his children and their custodian." | ⚠️ **PARTLY UNCONSTITUTIONAL.** **Law 25/1929 Art. 18 bis/3** (added by Law 100/1985) was held unconstitutional by the **SCC, Case 5 of judicial year 8, session 6 January 1996** (Gazette No. 3, 18 Jan 1996) **insofar as** it obliged the divorcer even where **the children have present money sufficient** or **the custodian has a residence (rented or not)**, **and insofar as it set a time limit**. Read the article with those two subtractions. See §5.5. |
| 9 | "A husband's **طلاق** takes effect the moment he pronounces it, whatever the paperwork." | ⚠️ **PARTLY TRUE AND VERY DANGEROUS.** Under classical *shari'a* the divorce occurs on pronouncement; under **Law 25/1929 Art. 5 bis** (added 1985) he must **document** it within **30 days**, and under **Law 1/2000 Art. 21** the divorce is **not provable against a denying party except by إشهاد and توثيق**. The consequences for the wife's money are severe: effects run from the pronouncement, **but if he concealed the divorce from her, her inheritance and other financial rights run only from the date she learns of it** (Art. 5 bis(3)). See §3.1. |
| 10 | "**خلع** means the wife forfeits everything, including her children's rights." | ⚠️ **FALSE FOR THE CHILDREN.** Under **Law 1/2000 Art. 20** she returns the **mahr** and waives **her own** shari'a financial rights (المالية الشرعية) — but Art. 20(3) is express: «**ولا يصح أن يكون مقابل الخلع إسقاط حضانة الصغار، أو نفقتهم أو أى حق من حقوقهم**» — the consideration may not be the surrender of custody, child maintenance or any right of the children. The خلع judgment is also **not appealable by any means** (Art. 20, final paragraph). See §3.2. |
| 11 | "Filing a **نفقة** claim needs a lawyer and costs court fees." | ❌ **NEITHER.** **Law 1/2000 Art. 3**: no lawyer's signature is required on a personal-status claim before the District Court (and the court may appoint a lawyer at the Treasury's expense if needed), and «**وتعفى دعاوى النفقات وما فى حكمها من الأجور والمصروفات بجميع أنواعها من كافة الرسوم القضائية فى كل مراحل التقاضى**». **Law 10/2004 (annexed) Art. 3** extends that to family courts and expressly to **imprisonment claims for non-execution**. A lawyer is still *wise*, but not a precondition, and not a fee barrier. See §8.3. |
| 12 | "**A new consolidated personal status law has passed** (or will apply to my case)." | ❌ **NO.** As of **19 October 2026** the three bills — **قانون الأسرة (المسلمين)** and **قانون الأسرة للمصريين المسيحيين** (both referred to a joint committee in **May 2026**; Cabinet approval **29 April 2026**; **355 substantive articles**, three parts: الولاية على النفس / الولاية على المال / إجراءات التقاضى) and the **الصندوق التكافلى لدعم الأسرة المصرية** bill (referred **12 October 2026**, announced 13 Oct 2026) — are **all still in committee, none enacted**. See §1.2. |
| 13 | "We lost in the family appeal — we'll take it to **النقض**." | ⚠️ **PROBABLY NOT.** **Law 10/2004 (annexed) Art. 14**: judgments and decisions of the **specialised family appellate circuits (الدوائر الاستئنافية)** are «**غير قابلة للطعن فيها بطريق النقض**» — without prejudice to **CPC Art. 250**. But **Law 1/2000 Art. 62** (still on the books) says the parties and the Public Prosecution *may* appeal by cassation against appeal-court judgments. **The two annexed laws conflict.** Law 10/2004 is later and specific, so the working rule is **finality**, subject to whatever Art. 250 preserves. Record *both*; do not promise a cassation route. See §8.6. |
| 14 | "If the husband doesn't pay, **بنك ناصر pays the whole maintenance**." | ⚠️ **NO — there is a cap.** The statute (Law 11/2004 Art. 3 as replaced by Law 113/2015) has **no cap**; the **operating cap applied by the Family Insurance Fund under Nasser Social Bank is EGP 500 per month per beneficiary** — the Fund pays that monthly without waiting to collect, and the balance of a higher award «**يتم رد فارق القيمة عند التحصيل**» (paid when recovered from the defaulter). This figure is on the bank's **official page (nsb.gov.eg)** and repeated by the Ministry of Social Solidarity and the press in 2020, 2022, 2025 and April 2026. See §4.6. |
| 15 | "Non-Muslim Egyptians' personal status is governed by **Law 462/1955**." | ❌ **REPEALED — but the rule survives in another instrument.** **Art. 4 of the promulgating provisions of Law 1/2000** (✅ read verbatim) repeals «**لائحة ترتيب المحاكم الشرعية … رقم ٧٨ لسنة ١٩٣١ … والقوانين أرقام ٤٦٢ لسنة ١٩٥٥، ٦٢٨ لسنة ١٩٥٥، ٦٢ لسنة ١٩٧٦ …**». The confessional allocation rule now lives in **Art. 3(2) of the same promulgating provisions**: disputes between **non-Muslim Egyptians of the same sect and milla who had organised milliya courts until 31 Dec 1955** are decided «**طبقا لشريعتهم — فيما لا يخالف النظام العام**». The **Supreme Constitutional Court** (Case 151 of judicial year 20) holds that this paragraph **«حلت محل الفقرة الثانية من المادة 6 من القانون رقم 462 لسنة 1955»** and that the **Coptic Orthodox personal-status lagna of 9 May 1938** (in force 8 July 1938) is thereby **legal rules subject to constitutional review**. **Cite Law 1/2000's promulgating Art. 3(2), not 462/1955.** See §1.3. |
| 16 | "Christians have their own inheritance/نصيب rules, so Islamic shares don't apply to them." | ❌ **INHERITANCE IS ONE OF THE UNIFIED AREAS.** The SCC's own summary of the system: apart from «**الدائرة المحدودة التي وحد المشرع في نطاقها القواعد الموضوعية في مسائل الأحوال الشخصية للمصريين جميعهم — كتلك التي تتعلق بمواريثهم ووصاياهم وأهليتهم**» (estates, wills, capacity), non-Muslim Egyptians are governed by their own religious laws. **So Law 77/1943 (inheritance) and Law 71/1946 (wills) apply to every Egyptian.** ⚠️ There is a **live constitutional argument** (advanced in published litigation commentary under **Constitution Art. 3**) that this unification is now unconstitutional for Christians — a **scholarly/pending** position, **not** a change in the law. See §1.3 and §7. |
| 17 | "The **wife always inherits 1/8**" / "the **wife inherits nothing** if there are children". | ⚠️ **BOTH WRONG — it is 1/4 or 1/8 depending on descendants.** The Quranic share of the wife (or wives collectively) is **1/8 where there is a descendant** and **1/4 where there is none**; the husband takes **1/4 with a descendant and 1/2 without**. ⚠️ **Read this row as Quranic/statutory shares in outline; the arithmetic of any single estate is a توزيع problem** — see §7.3, and do not quote a fraction without the descent condition. |
| 18 | "**The رؤية (visitation) order can be enforced by force** — the police bring the child." | ❌ **THE STATUTE SAYS THE OPPOSITE, IN TERMS.** **Law 25/1929 Art. 20(2)** (✅ verbatim): «**ولا ينفذ حكم الرؤية قهراً**، ولكن إذا امتنع من بيده الصغير عن تنفيذ الحكم بغير عذر أنذره القاضي فإن تكرر منه ذلك جاز للقاضي بحكم واجب النفاذ **نقل الحضانة مؤقتا** إلى من يليه من أصحاب الحق فيها لمدة يقدرها». The sanction for refusal is **temporary transfer of custody**, not forced production of the child. See §5.4. |
| 19 | "**All family-court claims are free** — there are no fees." | ⚠️ **ONLY THE MAINTENANCE FAMILY IS FREE.** **Law 1/2000 Art. 3(2)** exempts «**دعاوى النفقات وما فى حكمها من الأجور والمصروفات بجميع أنواعها**» from «**كافة الرسوم القضائية فى كل مراحل التقاضى**» — i.e. **maintenance and things in its nature (wages, expenses)**, extended by **Law 10/2004 Art. 3** to family courts and expressly to **imprisonment claims for non-execution**. **Mahr, جهاز, خلع consideration, inheritance and property claims are NOT exempted by those words.** ⚠️ **I could not establish the current fee for a خلع or mahr claim** — see §8.3 and §12. |
| 20 | "**Custody automatically goes to the mother** until 15." | ⚠️ **THE ORDER IS STATUTORY, THE OUTCOME IS NOT AUTOMATIC.** **Art. 20** does list the mother first («**فيثبت الحق في الحضانة للأم ثم للمحارم من النساء**»), but (a) the article itself requires the custodian to be **أهل للحضانة** and continues with a long ordered list, and (b) **Law 10/2004 Art. 10** directs the court to be guided by «**ما تقتضيه مصالح الطفل الفضلى**», and the **social/psychological experts' attendance is compulsory** in custody and رؤية cases (**Art. 11**). **Never promise a parent the outcome** — describe the order and the discretion. See §5.1–§5.3. |
| 21 | "There is a **criminal penalty for denying visitation**" / "the new law criminalises withholding رؤية". | 🟡 **NOT IN FORCE as of 19 October 2026.** The **2026 family-law package** (and the Fund bill's coverage) is reported to include «**تجريم منع حق الرؤية أو الاستزارة دون مبرر وفرض عقوبات مالية على الحاضن المخالف**» — the Cabinet-referred bill's own description, reported by **El-Watan on 9 May 2026**. **It is a bill in joint committee** (§1.2). The **law in force** is Art. 20's **transfer-of-custody** sanction and, for **إعلان/تنفيذ**, the execution machinery of Law 1/2000 (see §9). **Do not tell a parent the other side can be prosecuted for it today.** |

---

## Index of instruments

| # | Instrument | Citation | Status | Marker |
|---|---|---|---|---|
| 1 | **Law on maintenance and some personal-status matters** | Law 25/1920 (المرسوم بقانون 25/1920) | in force; Art. 1 replaced 1985; **Art. 3 bis** added 1926; Arts. 3, 7, 12 repealed by Law 25/1929 | ✅ |
| 2 | **Law on some personal-status matters** (طلاق، ضرر، حضانة، مفقود، نسب) | Law 25/1929 (المرسوم بقانون 25/1929) | in force, heavily amended | ✅ |
| 3 | **The 1985 reform** | Law 100/1985 | in force; added Art. 5 bis, 11 bis, 11 bis/2, 18 bis, 18 bis/2, 18 bis/3, 20 bis to Law 25/1929 and replaced Art. 1 & 16 of Law 25/1920 | ✅ |
| 4 | Custody age reform | Law 4/2005 | in force; replaced Art. 20(1) of Law 25/1929 | ✅ |
| 5 | **Law on the organisation of some litigation positions and procedures in personal-status matters** (procedure) | Law 1/2000 | in force; amended by Law 91/2000 (Art. 76 bis, Art. 9(أولاً)(٩)) and Law 176/2020 (Art. 47) | ✅ |
| 6 | Imprisonment for maintenance default | Law 91/2000 | in force (Gazette No. 20 bis (أ), 18 May 2000) | ✅ |
| 7 | Interim disbursement ceilings | Law 176/2020 | in force from **5 Sept 2020**; ⚠️ **two gazette numbers recorded** — «العدد ٣٧ مكرر» (footnotes of the consolidated copy) vs «العدد ٣٦ (مكرر)» (egyptianlaws.com reproduction); **record the conflict, do not choose** (§12) | ⚠️ |
| 8 | **Family courts law** | Law 10/2004 | in force from **1 Oct 2004**; Art. 2 amended by Law 142/2006; Art. 11 amended by Law 215/2017 | ✅ |
| 9 | **Family Insurance Fund** | Law 11/2004, as amended by **Law 113/2015** | in force | ✅ |
| 10 | Civil Status Law | Law 143/1994 (أحوال مدنية) — Arts. 5, 30, 31, **31 bis**, 66 | in force; Art. 31 bis added by Law 126/2008; other articles amended by Laws 4/2016, 15/2018 | ✅ |
| 11 | **The marriage-age amendment** | Law 126/2008 | in force (Gazette No. 24 bis, 18 June 2008) | ✅ |
| 12 | Wills | Law 71/1946 (الوصية) — Arts. 37, 38, 40, 71–79 | in force | ✅ |
| 13 | Inheritance / estates | Law 77/1943 (تصرفات التركات) — **Art. 49** added by Law 219/2017 | in force; upheld by the SCC | ✅ |
| 14 | Penal Code | Law 58/1937 — **Arts. 227, 292, 293, 341**; **Art. 293 replaced by Law 6/2020** | in force | ✅ |
| 15 | Child Law | Law 12/1996 — Art. 2 (definition) | in force; Art. 2 as replaced by Law 126/2008 | ✅ |
| 16 | Public-order litigation (الحسبة) | Law 3/1996 | in force; only the Public Prosecution may bring | ✅ |
| 17 | Ma'zoun / documentation decisions | MoJ Decision **6927/2008**; MoJ Decision **1727/2000** (لائحة المأذونين Art. 33(4)); Circular 7/2018 | in force per the **official NCW page** — text not read from the Gazette | ⚠️ |
| 18 | الولاية على المال (guardianship over property) | Law 119/1952 | in force — procedural context for Law 1/2000 Part on الولاية على المال | ⚠️ |
| 19 | **The three pending bills** | قانون الأسرة; قانون الأسرة للمصريين المسيحيين; الصندوق التكافلى لدعم الأسرة | **NOT enacted — in joint committee as of 19 Oct 2026** | ⚠️ |
| 20 | Repealed or superseded and *often still cited* | Law 44/1979 (held unconstitutional); لائحة ترتيب المحاكم الشرعية 78/1931 (**repealed by Law 1/2000 promulgation Art. 4**) | ❌ do not cite as current | ✅ |
| 21 | **Penal reform of the maintenance offence** | Law 6/2020 — Gazette No. 5 bis, **2 February 2020**; replaced **Penal Code Art. 293** | in force; fine now **up to EGP 5,000**, plus service-suspension and صلح provisions | ✅ |
| 21 | **Constitution** | 2014 Constitution, as amended by the **23 April 2019** referendum — **Arts. 2, 3** (shari'a sources; Christian/Jewish *sharai'*) | in force | ✅ |
| 22 | **Confessional allocation rule (the live instrument)** | **Law 1/2000 — promulgating (مواد الإصدار) Art. 3(2)**: non-Muslims of one sect/milla with a milliya court organised until **31 Dec 1955** → their own shari'a within public order — held by the **SCC (Case 151/20)** to have **replaced Art. 6(2) of Law 462/1955** | in force | ✅ |
| 23 | Christian **marriage documentation** | Law **68/1947**, amended by Law **629/1955** (documentation by the Christian communities) | in force per the **Cassation subject index**; ⚠️ text not read | ⚠️ |
| 24 | Maintenance-default penalty | **Penal Code Art. 293**, as amended by **Law 6/2020** (EGP 5,000 ceiling + suspension of government services) | in force, per the amended text quoted in 2026 reporting | ⚠️ |
| 25 | **Visitation procedure** | **MoJ Decision 1150/2010** (لائحة تنظيم رؤية المحضونين), Art. 12 — weekly/monthly/annual visitation quotas + electronic contact | in force per secondary quotation; text not read | ⚠️ |
| 26 | **Law 462/1955** (the instrument everyone cites) | «بإلغاء المحاكم الشرعية والمحاكم الملية» — published **الوقائع المصرية 24 Sept 1955** | **REPEALED by Law 1/2000 promulgating Art. 4** — cite it for *history and Cassation case-law*, **never as the current allocation rule** | ✅ |

**Not re-researched here** (already established in file 05 and inherited): the Official Gazette is **not** on `gcc.gov.eg`;
`serviceapi.egyptianlaws.com` was down (HTTP 500) on 19 Oct 2026; **`moj.gov.eg:73/Doc/001/<id>.pdf` is the primary source that
works** (`curl -k`) but is **scan-only** (no text layer); **`lawhub.info/eg/?p=NNNN` is the best verbatim text source found**
(full consolidated Arabic text **plus footnotes giving the amending law and the Gazette issue**); `mksegypt.org/ar/laws/<id>`,
`manshurat.org/node/<id>` and `alhasswalawfirm.com/law-library/<slug>` reproduce official texts with amendment provenance;
`sccourt.gov.eg` publishes SCC judgments and the judgments list their own Gazette publication.

---

# 1. ⭐ The governing statutes, the amendment chain, and the question everyone asks: has the new consolidated law passed?

**Citation:** the personal-status field in Egypt is **not codified in one law**. It is a patchwork: **Law 25/1920** (maintenance and
some personal-status matters), **Law 25/1929** (divorce, custody, missing persons, parentage — the "المرسوم بقانون" as the 1985 and
2005 Gazettes style it), **Law 100/1985** (the reform that added the modern articles 5 bis, 11 bis, 11 bis/2, 18 bis, 18 bis/2,
18 bis/3, 20 bis), **Law 4/2005**, **Law 1/2000** (procedure, and the substantive articles 17–22), **Law 10/2004** (family courts),
**Law 11/2004 + Law 113/2015** (the Fund), plus the Civil Status Law 143/1994 and the Penal Code.
**Status:** all in force; **nothing has been consolidated**.
**Sources:** https://lawhub.info/eg/?p=11576 (Law 25/1929, full text **with amendment footnotes and SCC citations**; retrieved by
direct page fetch) · https://lawhub.info/eg/?p=11578 (Law 25/1920, same treatment; retrieved by direct page fetch) ·
https://lawhub.info/eg/?p=11675 (Law 10/2004) · https://mksegypt.org/ar/laws/24131 (Law 1/2000, all 79 annex articles) ·
primary Gazette PDFs at `https://moj.gov.eg:73/Doc/001/<id>.pdf` (17 instruments downloaded with `curl -k`, pages rendered at
500 DPI and **article numbers confirmed by viewing cropped images**, because tesseract mis-reads Arabic-Indic numerals).
**As of:** 2026-10-19.

## 1.1 The amendment chain you have to keep straight

| Instrument | What it did | Gazette / date |
|---|---|---|
| **Law 25/1920** | maintenance for the wife (Art. 1), the divorcée (Art. 2), judicial divorce for non-maintenance (Arts. 4–6), separation for defects (Arts. 9–11) | issued at Ras El-Tin 25 Shawwal 1338 = **12 July 1920**; in force on publication in الوقائع المصرية |
| **Law 33/1926** | **Art. 1 replaced Art. 3** of Law 25/1920 (temporal bar on a divorcée's maintenance claim) and **Art. 2 added «مادة ٣ مكرر»** — the execution cap: «لا يجوز تنفيذ أحكام بنفقة عدة عن مدة تزيد على سنة من تاريخ الطلاق بالنسبة لغير المرضع وعلى سنتين وثلاثة أشهر من تاريخ الوضع بالنسبة للمرضع» | الوقائع المصرية, **العدد ٤٥ تابع, ٧ يونية ١٩٢٦** — read from the primary PDF `590331926.pdf`; the article number **٣ مكرر** and the words of the added article were **read off a 500-DPI crop**, and the law's own explanatory memorandum (same PDF, page 4) states the figures **سنة واحدة / سنتين وثلاثة أشهر** ✅ |
| **Law 25/1929** | divorce, ضرر, arbitration, شقاق, missing husband, imprisoned husband, **parentage admissibility (Art. 15)**, **maintenance assessment + نفقة مؤقتة (Art. 16)**, mahr (Art. 19), **custody and رؤية (Art. 20)**, missing persons (Arts. 21–22), the penal article 23 bis | issued Abdeen Palace 28 Ramadan 1347 = **10 March 1929**; published 25 March 1929. **Art. 24 of Law 25/1929 repealed Arts. 3, 7 and 12 of Law 25/1920** — which is why the 1926 provision lives on as **Art. 3 bis** |
| **Law 100/1985** | the big reform of *both* laws (see row 3 of the index) | Gazette **العدد ٢٧ (تابع), ٤ يولية ١٩٨٥**, corrected by an **استدراك in العدد ٣٣, ١٥/٨/١٩٨٥** (the footnotes say so expressly) |
| **Law 4/2005** | replaced **Art. 20(1)** of Law 25/1929 — custody age **15 for both** | Gazette **العدد ٤ (مكرر), ٤ مارس ٢٠٠٥** |
| **Laws 103/1958, 33/1992, 2/2006, 140/2017** | the المفقود articles (Arts. 21–22 of Law 25/1929): presumption of death **4 years / 30 days / 1 year**, and Art. 22 replaced by **140/2017** | each in its own Gazette; all four PDFs were downloaded and identified |
| **Law 1/2000** | the procedure code for personal status, and substantive Arts. 17–22 (proof of marriage, طلاق, مراجعة, خلع) | 29 January 2000; **in force one month after publication** |
| **Law 91/2000** | added **بند (٩)** to Art. 9(أولاً) (District Court, **final** judgment, in imprisonment-for-non-execution claims) and inserted **Art. 76 bis** (imprisonment up to **30 days**) | Gazette **العدد ٢٠ تابع (أ), ١٨ مايو ٢٠٠٠** |
| **Law 176/2020** | replaced **Art. 47** of Law 1/2000 (disbursement authority raised to **EGP 20,000**, once every three months, with an urgent-medical top-up) | Gazette **العدد ٣٧ مكرر, ٢٠٢٠** |
| **Law 10/2004** | family courts: composition, settlement offices, experts, family file, execution department | promulgated 17 March 2004; Gazette **العدد ١٢ تابع (أ), ١٨ مارس ٢٠٠٤**; **in force 1 October 2004** |
| **Laws 142/2006, 215/2017** | Art. 2 of Law 10/2004 (at least one woman expert) and the last paragraph of Art. 11 (the social expert's report in نسب cases must state whether the child is in the alternative-family system) | 29 June 2006; Gazette **العدد ٤٩ مكرر (أ), ٢٠ ديسمبر ٢٠١٧** |
| **Law 11/2004 + Law 113/2015** | the Family Insurance Fund and its contribution bands | 2015 amendment: signed **12 November 2015**, in force **13 November 2015** |
| **Law 126/2008** | added **Art. 31 bis** to the Civil Status Law (age 18 + medical examination) and amended the Child Law and the Penal Code | Gazette **العدد ٢٤ (مكرر), ١٨ يونية ٢٠٠٨** — the header line was read off page 1 of the primary PDF |

⚠️ **Two conflicting citations for one date** (recorded, not resolved): the Gazette header of the Law 126/2008 issue reads
«العدد ٢٤ (مكرر) في **١٨ يونية** سنة ٢٠٠٨», while the footnotes on the consolidated reproduction at
`alhasswalawfirm.com` date that law's publication **١٥/٦/٢٠٠٨**. The signature on the gazette text is **١١ جمادى الآخرة ١٤٢٩
= ١٦ يونية ٢٠٠٨**, so a **15 June** publication date precedes the signature — prefer the **Gazette header (18 June 2008)** and do not
put a day-precise publication date in advice.
⚠️ **Naming conflict for Law 25/1929**: it is cited as «قانون رقم ٢٥ لسنة ١٩٢٩» and, in the 1985 and 2005 Gazettes,
as «**المرسوم بقانون** رقم ٢٥ لسنة ١٩٢٩». Both refer to the same instrument.

## 1.2 ⚠️ The three bills now before Parliament — what is *proposed* (nothing here is law)

**What I searched for and found (19 Oct 2026):** fresh Arabic press, the parliamentary committee's own statements via members,
and the government's referral dates. Nothing was found that shows enactment, and several sources state the opposite in terms.

**Re-checked 28 October 2026:** still not enacted — nothing has changed. The most recent reporting found (El-Balad,
24 Oct 2026, following the Egypt Forum 2026 recommendation of 24 Oct to expedite the package) again describes the three
as drafts «**مطروحة للنقاش، وليست قواعد نافذة**». A law firm's explainer (28 Aug 2026) states it outright: «**لا يوجد حتى
تاريخه قانون أحوال شخصية جديد صادر في مصر**», and lists the in-force instruments exactly as this file does
(1920/1929+1985, 1/2000, 10/2004, 11/2004, 126/2008).

| Step | Date | What happened | Source |
|---|---|---|---|
| Cabinet approval | **29 April 2026** | Cabinet approved the draft «قانون بإصدار قانون الأسرة» — **355 substantive articles** in three parts (الولاية على النفس، الولاية على المال، إجراءات التقاضى أمام محاكم الأسرة) | El-Watan, 17 Aug 2026 |
| Referral to Parliament | **4 May 2026** | Referred to a **joint committee** of the Constitutional & Legislative Affairs Committee, and the *bureaus* of Social Solidarity & Family, Religious Affairs & Awqaf, and Human Rights | El-Watan, 17 Aug 2026; Tafsela, 11 Sept 2026 |
| The Christian family bill | **May 2026** | «قانون الأسرة للمصريين المسيحيين» referred to the same joint committee | Shorouk, 13 Oct 2026 |
| Listening sessions, then a pause | mid-2026 | The committees held **two listening sessions** and did **not** complete the two bills, **waiting for the third bill** to be referred | Shorouk, 13 Oct 2026 |
| Bill 3 | **12 October 2026** | Speaker **هشام بدوى** referred «مشروع قانون إنشاء وتنظيم **الصندوق التكافلى لدعم الأسرة المصرية**» to the joint committee — completing the "triangle" | Shorouk, 13 Oct 2026 |
| Status of the file | **18 September 2026** | MP **عبلة الهوارى** (Legislative Committee): the law «موجود بالفعل لدى لجنة الشؤون الدستورية والتشريعية إلا أنه **لم يعرض حتى الآن على المجلس ولم تبدأ اللجنة في مناقشته أو دراسته**» — and she denied the rumours that it had been withdrawn | Veto, 18 Sept 2026 |
| Al-Azhar | **18 May 2026** | Al-Azhar's media centre stated the draft **had not been put to Al-Azhar** and that Al-Azhar did not take part in drafting it; Al-Azhar had submitted its own comprehensive draft in **April 2019** | El-Watan, 17 Aug 2026 |
| Government denial of withdrawal | Sept 2026 | Minister of Parliamentary Affairs **هانى عازر**: the government did not withdraw the draft; it is in Parliament's hands | Tafsela, 11 Sept 2026 |

**What the drafts are reported to contain** (⚠️ from press reporting of the bill, **not** from the text — I could not retrieve the
bill's text; treat everything in this paragraph as *proposed*): mother first then father in the custody order, with the court free to
depart for the child's best interest; **custody ending at 15** with the child choosing a parent after that; new controls on
**رؤية and استضافة**; **electronic visitation (رؤية إلكترونية)**; forfeiture conditions; and maintenance/متعة rules. The **Support Fund
bill** is described as a non-profit body with public legal personality, under the Minister of Social Solidarity, headquartered in
Cairo, supporting families **pending enforcement of final maintenance and similar judgments** (including school fees where the debtor
refuses) and families with no breadwinner; one MP stated the government bill **repeals Law 11/2004**. Source: Tafsela 11 Sept 2026,
Veto 18 Sept 2026, newsroom 22 Sept 2026, Shorouk 13 Oct 2026, El-Watan 14 Oct 2026.
**Context for why this matters:** MP **بسام الصواف** put the family caseload at **1,327,000 cases in one judicial year** and
**over 4,000,000 in the last three to four years**, and criticised the current رؤية regime as 2–3 hours a week in a club (Shorouk,
13 Oct 2026). Treat that figure as a **politician's figure**, not a statistic: 🟡 no judicial-statistics publication was located.

**Consequences for an agent:**
1. Never write "the new personal status law says…" — write "**the law in force** says…" and, if useful, "a bill pending in committee
   would change this".
2. If a person's case is a **نمط** the bills target (custody age, رؤية, استضافة, the Fund's payments), say that the bill **may**
   change the position **later**, but that a **pending bill does not suspend the statute**.
3. The Fund bill (Oct 2026) **repeals Law 11/2004** if enacted — which is the law a current beneficiary is being paid under.
   Advise against acting on the assumption it has already happened.

*(Source retrieval method: Exa web search + `web_fetch_exa` on the article URLs above; URLs in the final report of this file's build.)*

## 1.3 ⭐⭐ THE CONFESSIONAL STRUCTURE — the fact almost every guide omits

**Egyptian personal status is confessional.** There is no single code. Which *substantive* rules apply to a marriage, a divorce or a
custody dispute depends on the **religion and the sect/denomination (الملة والطائفة)** of the spouses. **Law 1/2000 does not change
this — it codifies it, in its promulgating provisions, not in the annexed law.**

**The two paragraphs that decide every case (✅ Law 1/2000, مواد الإصدار, Art. 3 — read verbatim):**
> «**تصدر الأحكام طبقا لقوانين الأحوال الشخصية والوقف المعمول بها، ويعمل فيما لم يرد بشأنه نص فى تلك القوانين بأرجح الأقوال من مذهب
> الإمام أبى حنيفة.**
> **ومع ذلك تصدر الأحكام فى المنازعات المتعلقة بالأحوال الشخصية بين المصريين غير المسلمين المتحدى الطائفة والملة الذين كانت لهم
> جهات قضائية ملية منظمة حتى ٣١ ديسمبر سنة ١٩٥٥ - طبقا لشريعتهم - فيما لا يخالف النظام العام.**»

Read out of it, the three operative rules:

1. ✅ **Muslims** (and anyone whose spouses differ in religion or sect) → the **codified statutes** (the 1920/1929/1985/2000/2004
   patchwork) and, **where the statutes are silent, the most preponderant (أرجح) opinion of the Hanafi school**. The Abu-Hanifa
   clause is the reason Egyptian judgments look like *fiqh*: it is **statutory gap-filling**, and it is why the *wali*, the *مهر المثل*
   and the classical custody conditions appear in reasoning without an article behind them.
2. ✅ **Non-Muslim Egyptians of the SAME sect and milla**, whose community had an **organised milliya court as at 31 December 1955**
   → **their own shari'a**, within «النظام العام» (public order).
3. ✅ **Different sects or different millas** (e.g. a Coptic Orthodox husband and a Coptic Catholic wife, or a Christian and a
   Muslim) → **not** confessional law: the fallback is the **Islamic shari'a**, i.e. the codified statutes plus the Hanafi rule.
   This is settled Cassation doctrine: the connecting factor is **religion/sect at the time of the claim**, and the topic index of
   the Court of Cassation's personal-status digest lists rulings on exactly this — «**اختلاف طائفة كل من الزوجين غير المسلمين عن
   الآخر. جواز إيقاع الطلاق بالإرادة المنفردة**» (i.e. where sects differ, a unilateral مشروع divorce becomes available to the
   husband because Islamic law applies).

**❌ The instrument everyone cites is repealed. Do not cite it.** **Art. 4 of Law 1/2000's promulgating provisions** (✅ verbatim)
provides: «**تلغى لائحة ترتيب المحاكم الشرعية الصادرة بالمرسوم بقانون رقم ٧٨ لسنة ١٩٣١، ويلغى الكتاب الرابع من قانون المرافعات المدنية
والتجارية … والقوانين أرقام ٤٦٢ لسنة ١٩٥٥، ٦٢٨ لسنة ١٩٥٥، ٦٢ لسنة ١٩٧٦ المشار إليها …**». So **Law 462/1955** — the statute every
English-language guide cites for "non-Muslims have their own personal status law" — is **gone as an instrument**. Its *rule* moved to
Law 1/2000 promulgating Art. 3(2). The **Supreme Constitutional Court** states this expressly (**Case 151 of judicial year 20**):
«…الأقباط الأرثوذكس التي أقرها المجلس الملى العام في ٩ مايو سنة ١٩٣٨، وعمل بها اعتباراً من ٨ يوليه سنة ١٩٣٨» are «قواعد قانونية»
and the SCC cites «**الفقرة الثانية من المادة الثالثة من القانون رقم ١ لسنة ٢٠٠٠** … **التي حلت محل الفقرة الثانية من المادة ٦ من
القانون رقم ٤٦٢ لسنة ١٩٥٥**».

**The constitutional layer (✅ read from the 2014 Constitution as amended 2019):**
- **Art. 2**: «الإسلام دين الدولة، واللغة العربية لغتها الرسمية، **ومبادئ الشريعة الإسلامية المصدر الرئيسي للتشريع**.»
- **Art. 3**: «**مبادئ شرائع المصريين من المسيحيين واليهود المصدر الرئيسي للتشريعات المنظمة لأحوالهم الشخصية، وشئونهم الدينية،
  واختيار قياداتهم الروحية.**»

⚠️ **Note the three limits in Art. 3(2) itself**, because each of them is argued about in practice: (a) «**شريعتهم**» means the
**community's own body of rules** — for Coptic Orthodox Christians, the **lagna** (bylaws) of the General Milliya Council, **not** the
Bible by itself; (b) the spouses must be **متحدى الطائفة والملة** — **one** sect; (c) the result must not contradict «**النظام العام**».
The SCC's position is that these confessional rules are **subject to constitutional review** precisely because the legislature has
promoted them into legal rules.

**Which areas are unified and which are confessional — the line that matters most:**
| Area | Regime |
|---|---|
| **Marriage formation, its documentation and its effects** (mahr, nafaqa, طاعة) | ⚠️ **Confessional for non-Muslims**; statute for Muslims — though the **documentation machinery** (Civil Status Law 143/1994, Ma'zoun/notary offices) is state machinery |
| **Divorce / separation** | ⚠️ **Confessional** — and see the trap immediately below |
| **Custody, رؤية, guardianship of the person** | ⚠️ **Confessional in principle**, but the **family-court procedural law** (Law 10/2004, Law 1/2000) and the custody articles of **Law 25/1929** are applied by the national courts to everyone in practice; the Cassation digest carries a ruling that **custody as an effect of marriage is governed by Egyptian law alone where one spouse was Egyptian at the time of the contract** |
| **Inheritance, wills, legal capacity** | ✅ **UNIFIED** — one law for all Egyptians. SCC: apart from «**الدائرة المحدودة التي وحد المشرع في نطاقها القواعد الموضوعية … كتلك التي تتعلق بمواريثهم ووصاياهم وأهليتهم**», non-Muslims are subject to their own shari'a. **Law 77/1943 and Law 71/1946 apply to Christians and Muslims alike** (§7) |

**⚠️ THE DIVORCE TRAP FOR NON-MUSLIMS (read this before advising anyone).** **Law 1/2000 Art. 17(3)** (✅ verbatim):
> «**ولا تقبل دعوى الطلاق بين الزوجين متحدى الطائفة والملة إلا إذا كانت شريعتهما تجيزه.**»

So for a **Coptic Orthodox** couple (the largest non-Muslim community), the court will **not** grant a divorce their church's lagna
does not allow — which is why the Coptic divorce question is a *church-law* question, not a family-court question, and why the
"**الطلاق للضرر للزوجة القبطية**" campaigns exist. **Two consequences an agent must state:**
1. ❌ **خلع is NOT an available generic exit for a Catholic or Orthodox couple** in the way it is for Muslims: khul' is a form of
   **تطليق** (Law 1/2000 Art. 20 ends «ويقع بالخلع فى جميع الأحوال طلاق بائن»), and Art. 17(3) gates divorce on their shari'a
   permitting it. ⚠️ **This is the reading of the two articles together — I found no court ruling on it in this pass** — but it is
   the reason the Coptic personal-status file is a separate political file, and the 2026 bill package exists (§1.2).
2. ✅ **The escape valves that do exist**: (a) a **unicameral change of rite/denomination** puts the spouses in *different* sects, and
   the Cassation rule then applies Islamic law — the digest lists rulings going both ways, including one holding that a husband who
   **joined another church** while his wife remained Coptic Orthodox is governed by **Islamic** shari'a, so the divorce is proved
   under Islamic rules; (b) **annulment (فسخ/bطلان)** grounds that the community's own law allows; (c) **where the community's law
   itself permits** the divorce — e.g. adultery grounds.
   ⚠️ **The pre-2000 Art. 7 of Law 462/1955 (which regulated change of religion/sect) fell with the repeal.** Legal commentary calls
   its survival as custom «قاعدة عرفية» — **do not rely on it.** See §11 row 12 and §12.
3. ✅ **The documentation route for a non-Muslim couple** is not the Ma'zoun: the **Christian communities document their own
   marriages** through the church under **Law 68/1947 as amended by Law 629/1955** (⚠️ from the Cassation subject index; text not
   read), and the state's notary/registry machinery under Civil Status Law 143/1994 handles the rest (§2.1). Marriage and divorce
   between spouses of **different** religions or sects are documented at the **real-estate notary offices** — note that this is the
   *documentation* rule; it says nothing about which law applies, which is Art. 3(2) above.

**Sources for §1.3:** ✅ the **consolidated Arabic text of Law 1/2000 (promulgating Arts. 1–6 + annexed Arts. 1–79)**, retrieved by
direct page fetch from `mksegypt.org/ar/laws/24131` and read locally article by article · ✅ **Constitution 2014 (as amended 2019)**,
Arts. 2–3, retrieved via Constitute Project and WIPO Lex Arabic · ✅ the **SCC** passage (Case 151/20) as reproduced with the
confessional-law litigation commentary on `laweg.net/Default.aspx?ID=6017` · ⚠️ the **Court of Cassation subject index** of
personal-status rulings (`ahmedazimelgamel.blogspot.com` digest of النقض headings, and `mksegypt.org/ar/court-of-cassation-rulings/21892`
quoting Cassation reasoning on Law 462/1955 Arts. 6–7) · ⚠️ **Dar al-Ifta** statements are *fatwas*, not law — used only in §5.6.
**As of:** 2026-10-19.

---

# 2. Marriage — the contract, its documentation, عرفي marriages, the age rule, mahr and قائمة المنقولات

**Citation:** Civil Status Law 143/1994 **Arts. 5, 30, 31, 31 bis, 66**; Law 1/2000 **Arts. 17, 7**; Law 25/1929 **Art. 19**;
Penal Code **Art. 227**.
**Status:** in force. **The marriage contract itself is not created by the paperwork** — the paperwork is what makes it provable,
and, for most claims, what makes it *enforceable at all*.
**Sources:** https://lawhub.info/eg/?p=11399 (Civil Status Law 143/1994, full text with amendment footnotes; direct page fetch) ·
https://mksegypt.org/ar/laws/23813 (same law; corroboration) · https://www.laweg.net/Default.aspx?FIID=1306&action=LegsCates (the
official Gazette portal's list of amending laws, which shows the text of the inserted Art. 31 bis) ·
https://ncw.gov.eg/Page/474/... (the **National Council for Women's** official page «تطور سن الزواج فى القانون», which lists
MoJ Decision 6927/2008, Ma'zoun Regulation Art. 33(4) and Circular 7/2018) · primary PDF `https://moj.gov.eg:73/Doc/001/...`
(mirrored scan of the 1926 issue) · https://lawhub.info/eg/?p=11576 and the penalty text in the Penal Code.
**As of:** 2026-10-19.

## 2.1 Where the marriage is documented — and what happens at each office

- **Art. 5 of Law 143/1994 (✅ verified):** marriage and divorce are recorded by «**أقلام الكتاب بمحاكم الأحوال الشخصية**» where
  **both parties are Egyptian and of the same religion and sect**; and by the **real-estate notary offices (مكاتب التوثيق بالشهر
  العقارى)** where **one party is foreign** or the **two Egyptians differ in religion or sect**.
- **Art. 30** requires the documenting authority to lodge the record with the personal-status court's registry **within 15 days**
  of the marriage, with ID/national-number and date of birth supported by **official documents**; **Art. 31** does the same for the
  notary offices. **Art. 66** punishes breaches of a list of articles (19, 21, 22, 24, 31 first para, 35, 41, 52 first para, 53, 54
  first para, 58, 60) with a fine of **100–200 EGP** — note that **31 bis is not in that list**: the sanction for the age rule is the
  disciplinary penalty inside 31 bis itself.
- **What "توثيق" gives you, in one line:** an **official document (وثيقة رسمية)** of the marriage. Almost everything else in this file
  turns on having one.

## 2.2 ⭐ The minimum age (18) and its enforcement — get this right first

- **Art. 31 bis of Law 143/1994** (added by **Law 126/2008**), ✅ verified verbatim:
  > «لا يجوز توثيق عقد زواج لمن لم يبلغ من الجنسين **ثماني عشرة سنة ميلادية كاملة**. ويشترط للتوثيق أن يتم **الفحص الطبى** للراغبين في
  > الزواج للتحقق من خلوهما من الأمراض التي تؤثر على حياة أو صحة كل منهما أو على صحة نسلهما، وإعلامهما بنتيجة هذا الفحص، ويصدر بتحديد
  > تلك الأمراض وإجراءات الفحص وأنواعه والجهات المرخص لها به قرار من **وزير الصحة بالاتفاق مع وزير العدل**. **ويعاقب تأديبياً** كل من
  > وثق زواجاً بالمخالفة لأحكام هذه المادة.»
- **There is no exception, no guardian-consent exception, and no judicial-dispensation route in the article.** ❌ The widely repeated
  "she can marry at 16 with the guardian's consent" has **no basis in Art. 31 bis**.
- **The implementing layer (⚠️ official secondary source, text not read from the Gazette):**
  - **MoJ Decision 6927/2008**: «ولا يجوز مباشرة عقد الزواج أو المصادقة على زواج ما لم يكن سن الزوجين ثمانى عشر سنة وقت العقد»;
  - **Ma'zoun Regulations Art. 33(4)** as replaced by **MoJ Decision 1727/2000**: before documenting, the Ma'zoun must obtain the
    couple's declaration that they are free of the diseases that justify separation (العنة، الجنون، الجذام، البرص، الإيدز) after
    warning them about those diseases;
  - **Circular 7/2018**: the child-protection machinery (hotline 16000, governorate protection committees, Public Prosecution).
  - Source: official NCW page, https://ncw.gov.eg/Page/474/... (retrieved by search + fetch, 19 Oct 2026).
- **The criminal layer (✅ Penal Code Art. 227, read verbatim):**
  > «يعاقب بالحبس مدة لا تتجاوز **سنتين** أو بغرامة لا تزيد على **ثلاثمائة جنيه** كل من أبدى أما السلطة المختصة بقصد إثبات بلوغ أحد
  > الزوجين السن المحددة قانونا لضبط عقد الزواج أقوالا يعلم أنها غير صحيحة أو حرر أو قدم لها أوراقا كذلك **متى ضبط عقد الزواج على
  > أساس هذه الأقوال أو الأوراق**. ويعاقب بالحبس أو بغرامة لا تزيد على **خمسمائة جنيه** كل شخص خوله القانون سلطة ضبط عقد الزواج وهو
  > **يعلم** أن أحد طرفيه لم يبلغ السن المحددة فى القانون.»
  Note the shape of it: **lying about age is the offence**, and the officiant's offence requires **knowledge**. Marrying off a minor
  in an **عرفي** (undocumented) ceremony is not, by itself, an offence under this article.
- Why the fine ceilings are so low: the Penal Code is from 1937 and these articles have not been adjusted. **Low ceilings are why the
  enforcement of the age rule is weak**, and why the 2022 draft (below) proposed 1 year + 50,000–200,000 EGP.
- ⚠️ **Underage marriage is prosecuted/spoken of in practice mostly through other routes** — the child-protection committees,
  the Child Law's protection measures, and documentary pressure on the Ma'zoun. **I could not verify a single reported conviction
  under Art. 227 for an underage marriage**, and I am not asserting one.

## 2.3 The pre-marriage medical examination

Verified from **Art. 31 bis(2)** itself (text above): the examination is a **condition of documentation**, the diseases and the
authorised bodies are fixed by a **Health-Minister decision in agreement with the Justice Minister**, and the couples must be
**informed of the result**. Anyone who documents a marriage in breach is **disciplinarily punished**. ⚠️ The **list of diseases and the
validity period** of a test certificate are in that ministerial decision, which I did not retrieve — do not state a period.

## 2.4 ⭐ عرفي (undocumented) marriage — what it is, and what it can and cannot prove

This is the single most practically important doctrine in Egyptian family law and it is stated wrongly in both directions on the
internet. The verified position:

- **The marriage is not void for want of documentation.** Egyptian law does not make registration a condition of *validity*; a
  marriage contracted with the *shari'a* elements and without the paperwork is described as **زواج عرفي** and, on the classical
  analysis, is a **valid marriage** as between God and the parties. That is why the wife has a **نسب** claim and a **طلاق/فسخ** route.
- **But it is very weak as evidence, by statute.** **Law 1/2000 Art. 17** (✅ verbatim):
  > «ولا تقبل عند الإنكار **الدعاوى الناشئة عن عقد الزواج** – فى الوقائع اللاحقة على **أول أغسطس سنة ١٩٣١** – ما لم يكن الزواج ثابت
  > بوثيقة رسمية، **ومع ذلك تقبل دعوى التطليق أو الفسخ** بحسب الأحوال دون غيرهما **إذا كان الزواج ثابتا بأية كتابة**.»
  Read that carefully — it is the operating rule for every عرفي case:
  1. Claims **arising out of the marriage contract** (mahr, جهاز, نفقة, قائمة, etc.) are **not admissible on denial** unless the
     marriage is proved by an **official document**;
  2. **Only طلاق or فسخ (including تطليق)** are admissible where the marriage is proved by **any writing at all** (أية كتابة) —
     which is what an عرفي contract is;
  3. and **Law 1/2000 Art. 17(1)** bars *any* claim arising out of a marriage contract where the **wife was under 16** or the
     **husband under 18** **at the time the claim is filed**.
- **The acknowledgment-of-parentage route after death** is specially narrowed by **Law 1/2000 Art. 7** (✅ verbatim):
  > «لا تقبل عند الإنكار دعوى الإقرار بالنسب … **بعد وفاة المورث** إلا إذا وجدت **أوراق رسمية** أو **مكتوبة جميعها بخط المتوفى
  > وعليها إمضاؤه** أو أدلة قطعية جازمة تدل على صحة هذا الادعاء.»
- **Practical consequence** (this is the answer an agent should give): in an عرفي marriage the wife can **get a divorce** (تطليق/فسخ)
  proved by any writing, and can litigate **نسب** for the child under the rules in §6 — but claims for **نفقة, مؤخر, جهاز, قائمة**
  will fail **on denial** for want of an official document. The *wrong* advice in both directions is common: "عرفي gives you nothing"
  (❌ — the divorce and the child's نسب are reachable) and "عرفي gives you everything" (❌ — the money claims are usually lost).
- ⚠️ **Do not promise a نسب outcome.** Practice varies by court and by the strength of the writing or documents. See §6.

## 2.5 Mahr (الصداق) — proving it, and the قائمة المنقولات

- **Law 25/1929 Art. 19** (✅ verbatim) is the whole rule for disputes about the mahr:
  > «إذا اختلف الزوجان في مقدار المهر **فالبينة على الزوجة** فإن عجزت كان **القول للزوج بيمينه** إلا إذا ادعى مالا **يصح أن يكون
  > مهراً لمثلها عرفاً** فيحكم **مهر المثل**. وكذلك الحكم عند الاختلاف بين أحد الزوجين وورثة الآخر أو بين ورثتهما.»
  Three sentences, three consequences: (a) the **wife bears the burden of proving the mahr** — an undocumented mahr is usually lost;
  (b) if she fails, the **husband's oath** decides; (c) unless his asserted figure is one that **could not be a mahr for a woman like
  her**, in which case the court awards **مهر المثل** — closing the "I married her for one pound" escape.
- **مؤخر الصداق** is part of the mahr and follows the same proof rule. ✅ (Art. 19 covers "مقدار المهر"; the statute does not
  distinguish مقدم from مؤخر.)
- **قائمة المنقولات** (the inventory of household goods annexed to the marriage contract): ⚠️ **there is no statute of general
  application that governs the قائمة.** What is verified is that it is a **private written instrument**, and that a marriage
  document (the contract proper, and its annexes) is what the courts look at. Its two uses in practice:
  - **Civil:** as a **written acknowledgment/debt** the husband signed — a claim for the value of the items, or for the items.
  - **Criminal:** ⚠️ prosecutions for **خيانة الأمانة (breach of trust)** under **Penal Code Art. 341** are widely brought over a
    قائمة (or over the furniture itself) — the article text I read is: «كل من اختلس أو استعمل أو بدد مبالغ أو أمتعة أو بضائع …
    وكانت الأشياء المذكورة لم تسلم له إلا على وجه **الوديعة** أو الإجارة أو على سبيل عارية الاستعمال أو الرهن … يُحكم عليه بالحبس
    ويجوز أن يزاد عليه غرامة لا تتجاوز **مائة جنيه**». **I did not verify any Cassation ruling applying it to a قائمة**, and the
    elements (delivery as a deposit + criminal intent) matter. 🟡 **Do not tell a client that signing or contesting a قائمة
    automatically produces a criminal conviction** — check the current Cassation position in the file.
- ⚠️ **A related giant trap:** because of **Art. 17 of Law 1/2000** (above), a قائمة in an **عرفي** marriage is worth very little if
  the marriage itself is denied, because the claim "arises out of the marriage contract".

## 2.6 Polygamy is lawful, but the second marriage has procedural consequences

Not a marriage-formation rule, but it starts at the documentation office: **Law 25/1929 Art. 11 bis** (added 1985) requires the
husband to **declare his marital status in the marriage document** and, if married, to give **the names and residences of his existing
wives**, whom the registrar must notify of the new marriage **by registered letter with acknowledgment of receipt**. A wife taken over
may then seek a divorce for **material or moral harm** even without a contractual stipulation — full details, including the **1-year
lapse** rule, in **§3.3**. ✅

## 2.7 ⚠️ The 2022 child-marriage bill — read this before quoting any fine

The commonly quoted "1 year and 50,000–200,000 EGP" for marrying off a child comes from a **bill**, and the description of it below
is from press reporting of the bill and of the committee meeting (the bill's text was not retrieved):

- **3 July 2022:** the Constitutional & Legislative Affairs Committee **approved in principle** the government's draft banning child
  marriage, together with three MPs' drafts. The government draft had **5 articles plus a publication article**: no documentation of a
  marriage for anyone **under 18**; no **تصادق** (registrar's ratification) of such a contract; concerned parties may apply **by
  petition (على عريضة) to the president of the Family Court** for permission to document the marriage in cases where a female was
  sexually assaulted after a final conviction; and the Ma'zoun/notary must **notify the Public Prosecution** of **عرفي** marriages
  where one party is under 18 and which are brought to him for ratification, attaching the contract's parties and witnesses.
  Proposed penalty: **imprisonment of at least 1 year**, and a **fine of 50,000–200,000 EGP**, for those who participate in marrying
  a child off. (Source: Cairo24, 3 July 2022.)
- **October 2022:** the committee decided to start article-by-article discussion **without waiting for Al-Azhar's opinion**, which had
  not arrived; several MPs sought postponement; the bill was **not decided** before the session ended. (Source: Manassa, 16 Oct 2022;
  Cairo24, 13 Sept 2022.) ⚠️ **Al-Azhar's opinion was supportive of the substance** per the editor of *Sawt al-Azhar*.
- ⚠️ **No later enactment was found.** As of 19 Oct 2026 the marriage-documentation ban in force remains **Art. 31 bis of Law
  143/1994** (disciplinary penalty only) plus **Penal Code Art. 227**. 🟡 *Searched: Arabic press 2022–2026 on «تجريم زواج
  الأطفال/القاصرات»; the 2026 family-law bill coverage. A final passage of a stand-alone child-marriage law was not located — and the
  consolidated bill's fate (§1.2) is the thing to watch.*

---
# 3. Divorce — the four routes, and which one a person should use

**Citation:** Law 25/1929 **Arts. 1–5, 5 bis, 6–14, 23 bis**; Law 25/1920 **Arts. 2, 3 bis, 4–6, 9–11**; Law 1/2000
**Arts. 17, 18, 19, 20, 21, 22, 61, 63**.
**Status:** all in force. **There is no single "divorce" in Egyptian law** — there are four distinct routes with different proof
requirements, different money outcomes and different rights of appeal, and choosing wrongly costs the client real money.
**Sources:** https://lawhub.info/eg/?p=11576 (Law 25/1929 verbatim + footnotes) · https://lawhub.info/eg/?p=11578 (Law 25/1920
verbatim + footnotes) · https://mksegypt.org/ar/laws/24131 (Law 1/2000, all articles) · https://lawhub.info/eg/?p=11675 and
`https://moj.gov.eg:73/Doc/001/13791102004.pdf` (Law 10/2004) · Gazette PDF of **Law 91/2000** (personal copy of the MOJ scan).
**As of:** 2026-10-19.

## 3.1 Route 1 — the husband's unilateral طلاق, and the paperwork that decides everything

- **The pronouncement rules (✅ Law 25/1929 Arts. 1–5, verbatim, and worth knowing because clients are usually wrong about them):**
  - **Art. 1:** «لا يقع طلاق **السكران والمكره**.» — no divorce by an intoxicated or coerced man.
  - **Art. 2:** a **suspended/conditional** divorce «إذا قصد به الحمل على فعل شيء أو لا غير» **does occur** — i.e. "you're divorced if
    you don't come home" divorces her if he meant to force her.
  - **Art. 3 ⭐:** «الطلاق **المقترن بعدد** لفظا أو إشارة **لا يقع إلا واحدة**.» — **"أنت طالق ثلاثاً" is one divorce**, not three.
    This is the article that decides the most common client panic in Egypt. (It does not undo a *repeat* pronouncement on separate
    occasions.)
  - **Art. 4:** implied forms (كنايات) do not divorce without **intention**.
  - **Art. 5:** every divorce is **revocable (رجعي)** except the third of three, the divorce before consummation, a divorce **for
    consideration (طلاق على مال)**, and whatever this law and Law 25/1920 make **irrevocable (بائن)**. **خلع is بائن under Law 1/2000
    Art. 20 — and so is the judicial divorce under Law 25/1929 Arts. 6, 12, 13, 14.**
- **The documentation duty (✅ Law 25/1929 Art. 5 bis, added by Law 100/1985, corrected by the استدراك in Gazette 33 of 15/8/1985):**
  > «على المطلق أن **يوثق إشهاد طلاقه** لدى الموثق المختص **خلال ثلاثين يوما** من إيقاع الطلاق. وتعتبر الزوجة **عالمة بالطلاق بحضورها
  > توثيقه**، فإذا لم تحضره كان على الموثق **إعلان إيقاع الطلاق لشخصها على يد محضر**، وعليه تسليم نسخة إشهاد الطلاق إليها … **وتترتب
  > آثار الطلاق من تاريخ إيقاعه إلا إذا أخفاه الزوج عن الزوجة، فلا تترتب آثاره من حيث الميراث والحقوق المالية الأخرى إلا من تاريخ
  > علمها به**.»
- **Proof against a denial (✅ Law 1/2000 Art. 21):** «لا يعتد فى إثبات الطلاق عند الإنكار، **إلا بالإشهاد والتوثيق**» — and at the
  documentation the registrar **must warn the couple of the risks of divorce and call each of them to name an arbitrator** from their
  families to reconcile them; if both insist, or both state it has occurred, or the husband states he divorced, **the divorce must be
  documented after إشهاد**. **The same applies where the wife had reserved the right to divorce herself in the marriage document.**
  And the last paragraph: the divorce is not effective against **either** spouse unless that spouse **was present at the documentation
  in person or by proxy, or from the date of formal notice by official paper**.
- **The penal sanction (✅ Law 25/1929 Art. 23 bis, added 1985):** the divorcer is punished with **imprisonment up to 6 months and/or
  a fine up to 200 EGP** for breaching any of Art. 5 bis's rules; the **husband** likewise for giving the registrar **false marital-status
  or residence data** contrary to Art. 11 bis; the **registrar** with **imprisonment up to 1 month and/or a fine up to 50 EGP** for
  breaching any legal obligation, and may be **removed from office or suspended for up to 1 year**.
- **Revocation (مراجعة) (✅ Law 1/2000 Art. 22):** not accepted against a denying husband unless he **notified her by official paper
  within 60 days** (a woman who menstruates) or **90 days** (a woman whose عدة runs by months) of the documentation — unless she is
  pregnant or has acknowledged the عدة has not ended. The wife may prove revocation **by any means of proof**.
- **Money consequences of a unilateral طلاق:** عدم عدة maintenance (§4), **متعة** (§3.5), the mahr/mؤخر (§2.5), and a possible
  **ضرر** claim. A wife divorced unilaterally is **not** stripped of her shari'a financial rights — that is the whole difference from خلع.

## 3.2 Route 2 — خلع (Law 1/2000 Art. 20): the wife buys her freedom, but not with her children's rights

✅ **Art. 20 verbatim (all four paragraphs, read from the consolidated Law 1/2000 text):**

> «ل**لزوجين أن يتراضيا** فيما بينهما على الخلع، فإن لم يتراضيا عليه وأقامت الزوجة دعواها بطلبه **وافتدت نفسها وخالعت زوجها
> بالتنازل عن جميع حقوقها المالية الشرعية وردت عليه الصداق الذى أعطاه لها، حكمت المحكمة بتطليقها عليه**.
> **ولا تحكم المحكمة بالتطليق للخلع إلا بعد محاولة الصلح** بين الزوجين، وندبها **لحكمين** لموالاة مساعى الصلح بينهما، **خلال مدة
> لا تجاوز ثلاثة أشهر**، وعلى الوجه المبين بالفقرة الثانية من المادة (18) والفقرتين الأولى والثانية من المادة (19) من هذا القانون،
> **ويعد أن تقرر الزوجة صراحة أنها تبغض الحياة مع زوجها** وأنه لا سبيل لاستمرار الحياة الزوجية بينهما **وتخشى ألا تقيم حدود الله**
> بسبب هذا البغض.
> **ولا يصح أن يكون مقابل الخلع إسقاط حضانة الصغار، أو نفقتهم أو أى حق من حقوقهم.**
> **ويقع بالخلع فى جميع الأحوال طلاق بائن.** ويكون الحكم – فى جميع الأحوال – **غير قابل للطعن عليه بأى طريق من طرق الطعن**.»

**The five operating rules an agent must give correctly:**
1. **Consideration = her own shari'a financial rights + return of the mahr.** That is the *statutory* price, and the court will not
   grant خلع without it. It is not "whatever the parties agreed".
2. **It is not a fast route any more.** The court must attempt reconciliation, **appoint two arbitrators**, and allow up to **three
   months** for that; and Art. 18(2) (children) still governs the reconciliation sessions.
3. **The magic words are judicial, not moral:** she must **state expressly** that she abhors the life with him and fears she cannot keep
   God's limits. A judge who does not hear that statement cannot grant خلع under Art. 20.
4. **⭐ The consideration cannot touch the children.** Custody, child maintenance and "any right of the children" are outside the deal.
   A خلع agreement that purports to give up the child's maintenance is **not a valid consideration** under Art. 20(3) — which is *not*
   the same as saying the child's claim can never be compromised by other means; the article governs **the consideration for the خلع**.
5. **No appeal at all.** «غير قابل للطعن عليه بأى طريق من طرق الطعن» — this is the only family judgment in the file with that absolute
   finality. It cuts both ways: it cannot be appealed *against* the wife either, and it cannot be reopened.
- ⚠️ **Two consequences people get wrong:** (a) **متعة is not payable** on خلع, because the wife consented (the condition in Art. 18 bis
  of Law 25/1929 is a divorce «دون رضاها ولا بسبب من قبلها»); (b) the waiver is of **her own** rights — her **child's** maintenance and
  custody survive (see 3 above).

## 3.3 Route 3 — judicial divorce/tatliq under Law 25/1929 (and Law 25/1920 for non-maintenance)

This is the route for a wife (or, for defects, either spouse) who does **not** want to pay the خلع price. **Each ground has its own
article and its own proof burden.**

### 3.3.1 الضرر — harm making cohabitation impossible (Art. 6)

✅ «إذا ادعت الزوجة **إضرار الزوج بها بما لا يستطاع معه دوام العشرة بين أمثالهما** يجوز لها أن تطلب من القاضي التفريق وحينئذ
**يطلقها القاضي طلقة بائنة إذا أثبت الضرر وعجز عن الإصلاح** بينهما، فإذا رفض الطلب ثم تكررت الشكوى ولم يثبت الضرر **بعث القاضي
حكمين** وقضى على الوجه المبين بالمواد (7 و8 و9 و10 و11).»
Note what the article does: it **distinguishes a proven injury (immediate irrevocable divorce)** from an **unproven** repeated complaint
(which is sent to arbitration — the same mechanism as Art. 11).

### 3.3.2 The arbitration machinery (Arts. 7–11) — six months, an oath, and a report

- **Art. 7 (replaced 1985):** the two arbitrators must be «**عدلين من أهل الزوجين** إن أمكن، وإلا فمن غيرهم ممن لهم خبرة بحالهما
  وقدرة على الإصلاح بينهما» — the pre-1985 version limited them to the families; the current one does not.
- **Art. 8 (replaced 1985; corrected by the 1985 استدراك):** the decision appointing them fixes the start and end of their mandate,
  **not exceeding six months**; the court warns the arbitrators and the litigant, and **swears each arbitrator an oath** to do the job
  honestly. The court may give them **one further extension of not more than three months**; if they do not deliver their report in
  time they are **deemed to disagree**.
- **Art. 9 (replaced 1985):** a spouse's refusal to attend the arbitration does **not** stop it as long as he/she was notified; the
  arbitrators must **identify the causes of the شقاق (discord)** and make every possible effort at reconciliation.
- **Art. 10 (replaced 1985) — who is at fault decides the money:**
  1. fault **entirely the husband's** → they propose **irrevocable divorce with no prejudice to any marital right**;
  2. fault **entirely the wife's** → they propose divorce **against suitable consideration (بدل مناسب)** borne by the wife;
  3. fault **shared** → divorce with or without consideration **in proportion to the share of fault**;
  4. fault **unknown** → divorce **without consideration**.
- **Art. 11 (replaced 1985):** the arbitrators report with reasons; **if they disagree they add a third** with experience and capacity,
  sworn the same oath; if they disagree or fail to report in time, the court proceeds to the evidence. Then: «وإن عجزت المحكمة عن
  التوفيق بين الزوجين **وتبين لها استحالة العشرة بينهما وأصرت الزوجة على الطلاق** قضت المحكمة بالتطليق بينهما **بطلقة بائنة مع
  إسقاط حقوق الزوجة المالية كلها أو بعضها وإلزامها بالتعويض المناسب** إن كان لذلك كله مقتضى.»
  ⭐ **This is the article that decides the wife's money in a ضرر case**, and it is a **judicial discretion**, not a formula. It reads
  «وأصرت الزوجة **على** الطلاق» in the retrieved consolidated text — the word is عن/على in the reproduction (the 1985 Gazette wording
  is the one to check for a live case). ⚠️ **Flag it: the sense is "the wife insisted on the divorce"; verify the preposition against
  the Gazette before quoting this clause in a pleading.**
- **Law 1/2000 Art. 19** adds the modern procedural layer: the court must ask **each spouse to name an arbitrator** from their own
  family «قدر الإمكان» at the next session at the latest, and **appoints one for a spouse who fails to name or attend**; the
  arbitrators must **attend the next session** to state what they concluded together, and if they disagree or one fails to attend the
  court hears them (or the attending one) **under oath**, and the court «**لها أن تأخذ بما انتهى إليه الحكمان أو بأقوال أيهما، أو
  بغير ذلك** مما تستقيه من أوراق الدعوى» — i.e. **the arbitrators' opinion does not bind the court**.
- **Law 1/2000 Art. 18 (reconciliation is mandatory):** in *all* الولاية على النفس claims the court must **offer reconciliation**
  (and treats a spouse who fails to attend the reconciliation session without acceptable excuse, having known of it, as **refusing**
  it); in **طلاق/تطليق** claims it may not rule before making a genuine attempt and failing; and **if there is a child, it must offer
  reconciliation at least twice, with 30–60 days between the two sessions**. ⭐ Plan for **two months-plus** in any divorce with
  children.

### 3.3.3 نشوز / non-obedience (Art. 11 bis/2) — read this before advising a wife to "just leave"

✅ **Art. 11 bis/2 (added 1985)** in full substance: if the wife **refuses to obey without right**, her maintenance **stops from the date
of the refusal**; she is **deemed to refuse without right if she does not return to the marital home after the husband's summons by
court officer**, and **the summons must state the residence**; the wife has the right to **object to the First Instance court within
30 days** of that summons, **stating the shari'a grounds** for her refusal, failing which «حكم بعدم قبول اعتراضها» and her maintenance
counts as stopped **from the end of the objection period**; and on the objection, or at either spouse's request, the court must
intervene to settle the dispute, and if the disagreement is entrenched **and the wife asks for a divorce, the court follows the
arbitration procedure of Arts. 7–11**.
- ⚠️ **A very common piece of wrong advice:** "he can't stop her maintenance unless he sues for نشوز". The statute says the
  **maintenance stops on the refusal** and is only **reviewed in the objection**, and the wife must raise her grounds within 30 days.
- ⚠️ **The 1985 reform also protects her from the opposite abuse:** **Law 25/1920 Art. 1** (as replaced by Law 100/1985) provides that
  **her going out to lawful work is not a cause of forfeiture** unless it appears that she is **abusing the right or it conflicts with
  the family's interest** and the husband **asked her to stop** — and her leaving the marital home does **not** forfeit her maintenance
  «في الأحوال التي تباح فيها ذلك بحكم الشرع مما ورد به نص أو جرى به عرف أو قضت به ضرورة».

### 3.3.4 Absence and imprisonment (Arts. 12–14)

- **Art. 12:** if the husband is **absent for a year or more without acceptable excuse**, the wife may ask the judge to divorce her
  **بائنا** if she **has suffered harm from his absence** — **even if he has money she could spend from**.
- **Art. 13:** if **letters can reach the absent husband**, the judge **fixes a term and warns him** that she will be divorced from him
  unless he comes to live with her, moves her to him, or divorces her; if the term expires and he does neither and shows no acceptable
  excuse, the judge **separates them with an irrevocable divorce**. Where he cannot be reached, the divorce is granted **without notice**.
- **Art. 14:** the wife of a man **finally sentenced to a custodial penalty of three years or more** may ask for an irreconcilable
  divorce **one year after his imprisonment**, for harm — **even if he has money she could spend from**.

### 3.3.5 Non-maintenance: the fastest judicial route (Law 25/1920 Arts. 4–6) ⭐

✅ **Verbatim substance — this is the "طلاق القاضي لعدم الإنفاق" and people forget it exists:**
- **Art. 4:** if the husband **refuses to maintain** her: if he has **visible property (مال ظاهر)** the maintenance judgment is
  **executed against it**; if he has **no visible property and does not claim to be insolvent but insists on not paying, the judge
  divorces him immediately (طلق عليه القاضي في الحال)**; if he **claims insolvency (العجز)**, and **does not prove it → immediate
  divorce**; if he **proves it**, the judge **gives him a grace period of not more than one month**, and if that passes without payment,
  **divorce follows**.
- **Art. 5:** the same ladder applies to a **near-absent** husband; for a **far-absent, unknown-address or missing** husband with no
  property from which the wife can spend, **the judge divorces him immediately**. «وتسري أحكام هذه المادة على **المسجون الذي يعسر
  بالنفقة**».
- **Art. 6 ⭐:** «**تطليق القاضي لعدم الإنفاق يقع رجعياً**، وللزوج أن يراجع زوجته **إذا ثبت إيساره واستعد للإنفاق في أثناء العدة**،
  فإن لم يثبت إيساره ولم يستعد للإنفاق لم تصح الرجعة.»
  ⭐ A non-maintenance divorce is **revocable**, and the husband can take her back during the عدة **if** he proves solvency and
  readiness to spend. **Tell the client this before they celebrate.** Contrast the irrevocable ضرر/خلع/absence divorces.

### 3.3.6 Defects (Law 25/1920 Arts. 9–11)

- **Art. 9:** either spouse may claim separation for a **settled defect (عيب مستحكم)** that cannot be cured, or can be cured only after
  a long time, and which makes life together possible only with harm — «**كالجنون والجذام والبرص**» — whether the defect preceded the
  contract (and was unknown) or arose after it (and was not accepted). **No separation if the marriage was contracted knowing of the
  defect**, or if the defect arose afterwards **and was accepted expressly or impliedly** after knowledge.
- **Art. 10:** «**الفرقة بالعيب طلاق بائن**» — separation for a defect is an **irrevocable** divorce. **Art. 11:** experts are used for
  the defects for which annulment is sought.
- **Cross-ref:** the pre-marriage declaration about (العنة، الجنون، الجذام، البرص، الإيدز) sits in the **Ma'zoun Regulations Art. 33(4)**
  as replaced by MoJ Decision 1727/2000 (⚠️ from the NCW official page) — see §2.2.

### 3.3.7 Bigamy as a ground (Art. 11 bis) ✅

- The husband **must declare his marital status in the marriage document**; if married, he must **state the names and residences of
  the wives in his household**, and the registrar must **notify them of the new marriage by registered letter with acknowledgment**.
- A wife **taken over (التى تزوج عليها)** may ask for divorce if she suffers **material or moral harm** making cohabitation impossible
  — **even without a contractual stipulation**. If the judge cannot reconcile them, he **divorces against the husband (طلقها عليه)
  بائنا**.
- **The right lapses one year after she learns of the other marriage**, unless she **expressly or impliedly consented**, and **it is
  renewed each time he marries another** — and **a new wife who did not know he was married may also seek divorce**.
- ✅ The penal backstop: a husband who gives the registrar **false marital-status or residence data** is punished under **Art. 23 bis**
  (§3.1).

## 3.4 Route 4 — فسخ / بطلان الزواج (annulment), briefly

- The plea for annulment of a marriage brought before the Family Court belongs to the **فسخ/بطلان** category, and **Law 10/2004 Art. 11**
  makes the **attendance of both experts (social and psychological) mandatory** in such claims — see §8.1.
- **Law 1/2000 Art. 17** allows the **فسخ** plea to be proved by **any writing** (unlike money claims) — that is the statutory doorway for
  an عرفي marriage to be terminated or annulled. See §2.4.
- **Art. 63 of Law 1/2000** governs enforcement of annulment and divorce judgments — see §3.6.
- ⚠️ **Do not state the substantive grounds of بطلان** (impediments, foster-relation, etc.) from this file: they are classical-fiqh
  grounds applied through **Law 1/2000 promulgation Art. 3** («ت**صدر الأحكام طبقا لقوانين الأحوال الشخصية والوقف المعمول بها**، ويعمل
  فيما لم يرد بشأنه نص فى تلك القوانين **بأرجح الأقوال من مذهب الإمام أبى حنيفة**»), not a codified list. Reference the *Hanafi* default
  and get the specific impediment checked.

## 3.5 What a divorced wife is actually owed — the money checklist

| Item | Article | Rule |
|---|---|---|
| **نفقة العدة** | Law 25/1920 **Art. 2** (maintenance of a divorcée is a debt **from the date of divorce**) + **Art. 3 bis** (cap) + Law 25/1929 **Art. 17** (no claim for عدة maintenance **beyond one year** from the divorce) | the statute caps both the **claim** and the **execution**: execution of an عدة-maintenance judgment may not exceed **1 year from the divorce** for a non-nursing woman and **2 years 3 months from delivery** for a nursing woman (Art. 3 bis) ✅ |
| **متعة** | Law 25/1929 **Art. 18 bis** (added 1985, corrected by the 1985 استدراك) | a wife **of a valid, consummated marriage**, divorced **without her consent and without fault on her part**, gets — **in addition to the عدة maintenance** — «**متعة قدرها نفقة سنتين على الأقل**»، assessed by «حال المطلق يسرا وعسرا وظروف الطلاق ومدة الزوجية»، and the divorcer **may be allowed to pay it in instalments** ✅ |
| **مؤخر الصداق + جهاز/قائمة** | Law 25/1929 **Art. 19** (proof) | burden on the wife; failing that the husband's oath; unless it is not a plausible mahr for her like-kind → **مهر المثل** ✅ — see §2.5 |
| **Children's maintenance** | Law 25/1929 **Art. 18 bis/2** | continues on the father (see §4.1) regardless of the divorce route ✅ |
| **Housing for the children** | Law 25/1929 **Art. 18 bis/3** | as qualified by **SCC Case 5/8J of 6 Jan 1996** — see §5.5 ✅ |
| **Non-maintenance divorce is revocable** | Law 25/1920 **Art. 6** | he may take her back in the عدة if he proves solvency and readiness to spend ✅ |
| **خلع and متعة** | Law 1/2000 **Art. 20** vs Law 25/1929 **Art. 18 bis** | **no متعة on خلع** (she consented) — the conditions of Art. 18 bis are not met ✅ |

## 3.6 The timing trap: a divorce judgment is not enforceable at once (Law 1/2000 Art. 63)

✅ **Art. 63:** «**لا تنفذ الأحكام الصادرة بفسخ عقود الزواج أو بطلانها أو بالطلاق أو التطليق إلا بانقضاء مواعيد الطعن عليها بطريق
النقض**، فإذا طعن عليها فى الميعاد القانونى، استمر عدم تنفيذها إلى حين الفصل فى الطعن.»
- So a **divorce/annulment judgment** waits out the **cassation** period; **نفقة, رؤية, تسليم الصغير and أجور** judgments do not — they are
  enforceable **by force of law and without security** (Art. 65). **This asymmetry is the number-one practical fact for a client who
  needs money now.** Get the نفقة order first; it is immediately enforceable.
- **Art. 59:** pending an appeal against a judgment under **Art. 10**, the appellate court «**يجوز لها إصدار حكم مؤقت واجب النفاذ** بشأن
  **الرؤية** أو بتقرير نفقة أو تعديل النفقة … **بالزيادة أو بالنقصان**».
- **Art. 61:** the appeal period is **60 days for a person with no domicile in Egypt**, without adding a distance period.
- ⚠️ For the **no-cassation** question in family appeals (Law 10/2004 Art. 14), see the corrections table row 13 and §8.6 — the two
  annexed laws conflict.

---

# 4. Maintenance (نفقة) — who owes what, how it is assessed, and how it is actually collected

**Citation:** Law 25/1920 **Arts. 1, 2, 3 bis, 4–6**; Law 25/1929 **Arts. 16, 17, 18, 18 bis, 18 bis/2**; Law 1/2000 **Arts. 3, 10,
16, 23, 65, 71–79** and **Art. 76 bis** (added by Law 91/2000); Law 11/2004 as amended by Law 113/2015; Penal Code **Art. 293**.
**Status:** in force.
**Sources:** as §3, plus the **personal copy of the Gazette scan of Law 91/2000** (`https://moj.gov.eg:73/Doc/001/13228912000.pdf`,
downloaded with `curl -k`, pages rendered at **500 DPI** and read as images because the scan has no text layer and tesseract
**mis-reads Arabic-Indic numerals**) · https://nsb.gov.eg/en/expenses/family-insurance-fund/ (Nasser Social Bank's official Fund page).
**As of:** 2026-10-19.

## 4.1 Who owes maintenance to whom

- **Wife from husband (✅ Law 25/1920 Art. 1, replaced by Law 100/1985):** «تجب النفقة للزوجة على زوجها **من تاريخ العقد الصحيح إذا
  سلمت نفسها إليه ولو حكماً** حتى لو كانت **موسرة** أو **مختلفة معه في الدين**، ولا يمنع مرض الزوجة من استحقاقها للنفقة. وتشمل
  النفقة **الغذاء والكسوة والسكن ومصاريف العلاج** وغير ذلك بما يقتضى به الشرع.» It is **not** due if she **apostatises**, refuses
  herself **without right**, is compelled by a cause **not attributable to the husband**, or leaves **without his permission** — with
  the two carve-outs in §3.3.3 (lawful work; and leaving in cases the shari'a permits).
- **Children on the father (✅ Law 25/1929 Art. 18 bis/2, added 1985):** «إذا لم يكن للصغير مال **فنفقته على أبيه**»; the daughter's
  maintenance continues **until she marries or earns enough**; the son's **until he completes 15 able to earn** — and **beyond that**
  if he completes 15 **unable to earn** through physical or mental disability, or **because he is pursuing study suited to his peers
  and aptitudes**, or **because such earning is not available**. The father must also «**توفير المسكن** لهم بقدر يساره وبما يكفل
  للأولاد العيش فى المستوى اللائق بأمثالهم». ⭐ **And: «وتستحق نفقة الأولاد على أبيهم من تاريخ امتناعه عن الإنفاق عليهم»** — child
  maintenance runs **from the date of the father's abstention**, not from the judgment.
- **Divorcée (✅ Law 25/1920 Art. 2):** the divorcée who is entitled to maintenance has it **as a debt from the date of divorce**, as in
  the preceding article.
- **Parents and other relatives, and nursing/custody/housing pay:** «الأجور وما فى حكمها» (نفقة الوالدين، نفقة الأقارب، **أجر حضانة،
  أجر رضاعة، أجر مسكن**) are all inside the same system — they are named expressly in **Law 1/2000 Art. 76** (garnishment) and in
  **Penal Code Art. 293** (which punishes non-payment of «نفقة لزوجة أو أقاربه أو أصهاره **أو أجرة حضانة أو رضاعة أو مسكن**»). ✅
- **Both the wife and her young children benefit from the provisional order** — Art. 16 says «**لنفسها ولصغارها**» — see §4.3.

## 4.2 Assessment, and the date from which it runs

- **✅ Law 25/1929 Art. 16(1):** «**تقدر نفقة الزوجة بحسب حال الزوج وقت استحقاقها يسرا أو عسرا** على ألا تقل النفقة **فى حالة العسر
  عن القدر الذى يفي بحاجتها الضرورية**.» → assessment is on **the husband's circumstances when it falls due**, with a **floor** at
  her essential needs. (Art. 16 was replaced by Law 100/1985 and corrected by the 1985 استدراك.)
- **✅ Law 25/1920 Art. 1 (final part, 1985 text) — five rules in one paragraph:**
  1. her maintenance is «**ديناً على الزوج من تاريخ امتناعه عن الإنفاق مع وجوبه**» and «**لا تقسط إلا بالأداء أو الإبراء**» — a debt,
     not extinguished save by payment or release;
  2. «**ولا تسمع دعوى النفقة عن مدة ماضية لأكثر من سنة نهايتها تاريخ رفع الدعوى**» — **a claim for past maintenance is time-barred
     beyond one year ending at the date the claim is filed** ⭐ (this is why the claim must be filed at once);
  3. «**ولا يقبل من الزوج التمسك بالمقاصة** … إلا فيما يزيد على ما يفي بحاجتها الضرورية» — set-off only above her essential needs;
  4. «ويكون له **من نفقة الزوجة امتياز على جميع أموال الزوج**، ويتقدم في مرتبته **على ديون النفقة الأخرى**» — a **privilege over all the
     husband's property**, ranking **above other maintenance debts**;
  5. plus the نشوز rules and the work carvе-out in §3.3.3.
- **✅ Law 1/2000 Art. 23 — the income-hunting article, and it is powerful:** if the defendant's **income is seriously disputed** and the
  file does not allow it to be fixed, the court **must ask the Public Prosecution to investigate**; the **Public Prosecution conducts
  the investigation itself**, and **notwithstanding the bank-secrecy law (Presidential Decree-Law 205/1990) any governmental or
  non-governmental body must give the Public Prosecution the information it holds that bears on fixing the income**. ⭐ For a wife facing
  "he's a driver with no income on paper", this is the statutory route.
- **Runs from abstention:** wife — from the date he **abstained with the obligation in force** (Art. 1, above); children — from the date
  the father **abstained** (Art. 18 bis/2, above); divorcée — from the **date of divorce** (Art. 2 of Law 25/1920).

## 4.3 ⭐ Provisional maintenance (نفقة مؤقتة) — the clock is the strongest right she has

✅ **Law 25/1929 Art. 16(2), verbatim:** «وعلى القاضى فى حالة قيام سبب استحقاق النفقة وتوفر شروطه **أن يفرض للزوجة ولصغارها** منه
**فى مدى أسبوعين على الأكثر من تاريخ رفع الدعوى نفقة مؤقتة** (بحاجتها الضرورية) **بحكم غير مسبب واجب النفاذ فوراً** إلى حين الحكم
بالنفقة بحكم واجب النفاذ.»
- **"أن"** — the judge **must** do it once the cause and its conditions exist. **"غير مسبب"** — he need not give reasons, which removes
  the usual drafting delay. **"واجب النفاذ فوراً"** — enforceable immediately.
- ✅ **Law 1/2000 Art. 10(4):** during the divorce case itself the court may «تصدر **أحكاماً مؤقتة واجبة النفاذ** بشأن **الرؤية** أو
  بتقرير **نفقة وقتية** أو **تعديل** ما عساها تكون قد قررته من نفقة بالزيادة أو النقصان»; and those interim rulings **may not be
  appealed except once the final judgment issues** (Art. 10(5)). ✅
- ⚠️ **Two honest caveats:** (a) **two weeks is the statutory ceiling, not a promise** — court lists, service of process and the
  settlement-office step (§8.2) sit in front of it, and practitioners treat it as "as early as the court can", so do not tell a client
  "you will have money within 14 days"; (b) the interim order fixes **her essential needs**, not the final standard, which comes with
  the final judgment.
- ✅ **Art. 16(3):** the husband may **set off** what he already paid against maintenance **finally awarded**, «بحيث لا يقل ما تقبضه
  الزوجة وصغارها عن القدر الذى يفي بحاجتهم الضرورية».

## 4.4 Cost, lawyer, and where to file

- **Law 1/2000 Art. 3** — no lawyer's signature required before the District Court; the court may appoint a lawyer at the Treasury's
  expense; and **نفقة claims are exempt from all judicial fees and expenses at every stage of litigation**. ✅
- **Law 10/2004 annex Art. 3** — that exemption (and the Art. 3 pleading rules) applies **before the family courts**, expressly
  including «**دعاوي الحبس لامتناع المحكوم عليه عن تنفيذ الأحكام الصادرة بها**». ✅
- **Law 10/2004 annex Art. 7** — resort to the **settlement offices is free of charge** («ويكون اللجوء إلى تلك المكاتب **بدون رسوم**»). ✅
- **Forum:** نفقة and what is in its like are **District Court / family court** matters under **Law 1/2000 Art. 9(أولاً)(2)**; but once a
  طلاق/تطليق/تفريق جسمانى claim is before the **Court of First Instance**, that court rules **alone** on maintenance, custody, رؤية,
  housing etc. (Law 1/2000 Art. 10(2)) — see §8.7.

## 4.5 Enforcement against the defaulter — the ladder, in order

### 4.5.1 The Family Insurance Fund is meant to be step one (Law 1/2000 Arts. 71–72; Law 11/2004)

- ✅ **Art. 71:** a **family-insurance system** is created, one of whose aims is «**ضمان تنفيذ الأحكام الصادرة بتقرير نفقة** للزوجة أو
  المطلقة أو الأولاد أو الأقارب»، supervised by **بنك ناصر الاجتماعى**.
- ✅ **Art. 72:** the bank **must pay** the maintenance, wages and the like awarded to the **wife, divorcée, children and parents**,
  under rules issued by a **Justice-Minister decision** with the Social-Insurance Minister's agreement.
- **See §4.6 for what this actually pays, and its cap.**

### 4.5.2 Automatic deduction (Law 1/2000 Arts. 73–77)

- ✅ **Art. 73:** on a request from **بنك ناصر الاجتماعى** (with a true copy of the executable judgment and proof of completed service),
  **ministries, government departments, local units, public bodies, public-sector and business-sector units, the private sector, the
  National Insurance Authority, the armed-forces pension administration, professional syndicates and other bodies must deduct** the
  amounts **within the garnishment ceilings of Art. 76** from salary and the like and pensions and **deposit them in the bank's treasury
  immediately on receipt of the request and without need of any other procedure**.
- ✅ **Art. 74:** a debtor **who is not a salary/pension earner must deposit** the awarded amount in the bank's treasury (or branch or the
  social-affairs unit in whose district he resides) **in the first week of each month**, once the bank has notified him to pay.
- ✅ **Art. 75:** the bank **recovers** what it paid out **and its actual expenses**.
- ✅ **Art. 76 — the ceilings (read verbatim, because people misquote these constantly):**
  | Band | Ceiling |
  |---|---|
  | (أ) a wife **or** divorcée | **25%**, rising to **40%** where there is **more than one** |
  | (ب) the parents or one of them | **25%** |
  | (ج) two children or fewer | **35%** |
  | (د) wife/divorcée **+** one or two children **+** parents (or one) | **40%** |
  | (هـ) wife/divorcée **+ more than two children +** parents (or one) | **50%** |
  | in all cases | the deductible percentage may not exceed **50%**, divided among the entitled persons **in proportion to their awards** |
- ✅ **Art. 77 priority:** the wife's or divorcée's maintenance → **children** → **parents** → **relatives** → other debts.
- ✅ **Art. 78:** an objection to execution (إشكال فى التنفيذ) **does not suspend** execution of a maintenance judgment.
- ✅ **Art. 79:** **imprisonment of not less than 6 months** for anyone who obtains money from Nasser Bank under a judgment or order made
  under this law **by sham or manufactured procedures or evidence**, knowing it.

### 4.5.3 ⭐ The 30-day imprisonment route (Law 1/2000 Art. 76 bis, added by Law 91/2000)

✅ Read from the **primary Gazette scan of Law 91/2000** (page images; the numerals **٧٦ مكرر** and the reference to **Art. 293** of the
Penal Code were confirmed by eye at 500 DPI, because tesseract mis-read them):
- A **new item 9** was added to **Art. 9(أولاً)** of Law 1/2000 (District Court jurisdiction): «**دعاوى الحبس لامتناع المحكوم عليه عن
  تنفيذ أحكام النفقات وما فى حكمها ويكون الحكم فى ذلك نهائياً**» — **and that judgment is FINAL (نهائياً)**.
- **Art. 76 bis:** in «دعاوى النفقات والأجور وما فى حكمها» the **entitled person may bring the matter before the court that issued the
  judgment or where execution is proceeding**; once it is established to that court that **the debtor is able to pay** what was awarded,
  and the court **orders him to pay and he does not comply**, it **imprisons him for a period not exceeding 30 days**. If he **pays what
  was awarded or produces a guarantor acceptable to the entitled person, he is released**. **All of this is without prejudice to the
  creditor's right to execute by the ordinary means.**
- **The criminal route under Penal Code Art. 293 may not be used** in the cases governed by Art. 76 bis **unless the creditor has first
  exhausted** the procedure just described — i.e. **Art. 76 bis is the precondition of the Art. 293 complaint**.
- **Crediting:** if he was subjected to **إكراه بدنى** under Art. 76 bis and is then sentenced to imprisonment for the same act under
  **Penal Code Art. 293**, the days of the first period **are deducted** from the sentence; and a **fine is reduced at execution by
  5 EGP for each day** of the previously enforced إكراه بدنى.
- **Note the shape of the remedy:** it is **coercive imprisonment for debt**, available only on **proof of ability**, and it is
  **final** — no appeal from the District Court's decision on it.

### 4.5.4 The criminal complaint (Penal Code Art. 293)

✅ **Verbatim, as it now stands — Art. 293 was REPLACED by Law 6/2020** (Gazette No. 5 bis, **2 February 2020**), and this is the
current text: «كل من صدر عليه **حكم قضائى واجب النفاذ** بدفع نفقة لزوجه أو أقاربه أو أصهاره **أو أجرة حضانة أو رضاعة أو مسكن**
وامتنع عن الدفع **مع قدرته عليه لمدة ٣ أشهر بعد التنبيه عليه بالدفع**، يعاقب **بالحبس مدة لا تزيد على سنة وبغرامة لا تتجاوز
خمسة آلاف جنيه أو بإحدى هاتين العقوبتين**.»
- **The 2020 additions (Law 6/2020), in substance:** the complaint may be a **«شكوى أو طلب»** from the interested person; a **conviction
  suspends the convict's use of the services he needs to practise his profession that are provided by government bodies, public
  authorities, public/business-sector units, and public-utility providers, until he pays what he owes to the judgment creditor **and
  to Nasser Social Bank** as the case may be; **صلح (settlement) may be recorded at any stage**, on the request of the victim or his
  private agent, his heirs, or **the Bank**, and it **extinguishes the criminal action** and stays execution of the penalty — but it
  does **not** take effect if the judgment creditor has already taken all or part of the award from the Bank, unless the convict
  produces the Bank's certificate of settlement; and **the Government decides the services and the suspension rules**.
  ⚠️ **The old text is still everywhere on the internet:** pre-2020 copies (and this file's own first draft) print «غرامة لا تتجاوز
  خمسمائة جنيه» — **EGP 500**. That text is superseded. See §9.1 and the §12 entry.
- **Pay-or-guarantee defence survives:** «وفى جميع الأحوال، إذا أدى المحكوم عليه ما تجمد فى ذمته أو قدم كفيلاً يقبله صاحب الشأن فلا
  تنفذ العقوبة.»
- Three requirements: **an enforceable judgment**, **ability**, and **3 months' default after notification**; plus **complaint only**.
- **Paying — or producing an acceptable guarantor — before execution defeats the penalty.**
- ✅ **Law 11/2004 Art. 3 (as replaced by Law 113/2015)** gives **بنك ناصر الاجتماعى** the right to **move the criminal action as an
  interested party** under **Art. 293** to recover what it paid out under Art. 72.

## 4.6 ⭐ What the Fund actually pays — and the part that is not in the statute

- **Statutory position (✅):** Law 11/2004 Art. 2 (as replaced by Law 113/2015) sets the **contribution bands** that fund the system —
  **100 EGP** per marriage paid by the husband plus **4 EGP** per marriage-document extract; **100 EGP** per divorce or revocation paid
  by the divorcer/revoker plus **9 EGP** per divorce-document extract; **20 EGP** on the **first** birth-certificate extract and **3 EGP**
  on each later one; **4 EGP** per death-certificate or family-record extract and **5 EGP** per national-ID card. **Art. 3:** the bank's
  payment under Art. 72 is made **from the Fund's resources**, deposits/recoveries under Arts. 73–75 accrue to the Fund, the bank may
  move the Art. 293 criminal action, and the **President may add other insurance services** funded by the Fund. Signed **12 Nov 2015**,
  in force **13 Nov 2015**. **There is no cap in the statute.**
- **⚠️ The operating cap, which is what a client asks about:** the Fund «يضمن سرعة تنفيذ الأحكام **للنفقة الشهرية** لصالح المحكوم لصالحهم
  من النساء والأبناء **وبحد أقصى ٥٠٠ جنيه شهرياً** دون انتظار تحصيله من المحكوم ضده أو صرف قيمة الحكم بالكامل حال تحصيله من المنفذ
  ضده» — **EGP 500 per month per beneficiary**, paid **without waiting to collect from the debtor**, with the balance of a higher award
  «**يتم رد فارق القيمة عند التحصيل** من الممتنع عن التنفيذ». Source: **nsb.gov.eg** (bank's official page) and repeat statements by
  the Ministry of Social Solidarity / bank officials in 2020, 2022, 2025 and **April 2026**. **It has been EGP 500 throughout that
  period.**
- **What it covers (⚠️ official-secondary):** monthly maintenance for the **wife, children and parents**; the Fund's own page and the
  2025 ministry statement say it pays under **interim (مؤقتة) as well as final** judgments. Documents required (per the Fund):
  the **executable copy of the judgment (الصيغة التنفيذية)**; a **recent statutory notice** (إعلان under CPC Art. 281) with the
  **شهادة بخاتم الشعار**; an **official court certificate on whether the judgment was appealed** (and, if appealed, an official copy of
  it, **provided it did not amend the first-instance judgment**); the **insurance numbers** of the beneficiary and the debtor;
  the beneficiary's **ID**; a copy of the **marriage document**; the **children's birth certificates**; and a **general power of attorney
  in the name of the bank's chairman**.
- **Where:** any Nasser Social Bank branch; payment by branch, ATM card, mobile or Fawry; the bank's own page says the service operates
  through ~55 branches.
- **⚠️ The Fund's own warning to defaulters is worth quoting to a client:** failing to deal with it can lead to **restriction of liberty**
  and to being **listed on the criminal-execution units' lists** (**منعك من التمتع ببعض الخدمات** such as social housing, or banks
  refusing credit). Source: nsb.gov.eg.
- **Scale (⚠️ official statements, 2022):** ~**510,000 beneficiaries**, ~**305,000 judgments executed**, **EGP 5.068 billion** disbursed
  since 2004, at ~**EGP 81–82 million a month**. Ministry of Social Solidarity figures.
- **The pipeline:** the **الصندوق التكافلى لدعم الأسرة المصرية** bill (referred **12 Oct 2026**) is described as support **pending
  enforcement of final judgments** plus support for breadwinner-less families, and one MP states it **repeals Law 11/2004** — see §1.2.
  A **draft law to develop the Fund's resources in order to raise the EGP 500 ceiling** was already under discussion in **March 2025**.

---
# 5. Children — custody, visitation, the home, and the two guardianships

**Citation:** **Law 25/1929** Arts. **20**, 18 bis/2, 18 bis/3; **Law 100/1985** (adding 18 bis/2 and 18 bis/3); **Law 4/2005**
(replacing Art. 20(1)); **Law 1/2000** Arts. 2, 9(أولاً), 10, **70**, **65–69**; **Law 10/2004** Arts. 10, 11, 12, 15; **Civil Status
Law 143/1994** Art. 31 bis; **نظام** الولاية على المال (Law 119/1952, ⚠️ procedural context).
**Status:** all in force. ⚠️ **The 2026 bills propose to change the custody order, the age, and visitation** — §1.2. **Nothing here
is law until enacted.**
**Sources:** ✅ the consolidated **Law 25/1929** (Art. 20 in full, with the **Law 4/2005** substitution note and both SCC notes),
`lawhub.info/eg/?p=11576` · ✅ **Law 1/2000** Art. 9(أولاً)(7), Arts. 10, 24–25, 70–79 and Art. 2, `mksegypt.org/ar/laws/24131` ·
✅ **Law 10/2004** Arts. 10–15, `lawhub.info/eg/?p=11675` · ✅ **Law 1/2000 Arts. 65–69 read VERBATIM** from the consolidated text
(`mksegypt.org/ar/laws/24131`) — **this replaced an earlier secondary quotation of the same articles from the Bar Association's
explainer (`egyls.com`, 22 Oct 2020)**, and the numbers were confirmed against the text in **§9** · ⚠️ **MoJ Decision 1150/2010** (لائحة تنظيم رؤية المحضونين) quoted through
`parlmany.com` (16 Apr 2026) — **secondary** · ⚠️ **Dar al-Ifta** fatwas on the *wali* — **fatwas, not law**.
**As of:** 2026-10-19.

## 5.1 Who has custody — the statutory order is a fixed list, not a preference

✅ **Law 25/1929 Art. 20 (final paragraph, added 1985), verbatim in substance:** custody belongs
«**للأم ثم للمحارم من النساء، مقدما فيه من يلي بالأم على من يلي الأب**» — and the order is:
**الأم → أم الأم وإن علت → أم الأب وإن علت → الأخوات الشقيقات → الأخوات لأم → الأخوات لأب → بنت الأخت الشقيقة → بنت الأخت لأم →
الخالات بالترتيب المتقدم في الأخوات → بنت الأخت لأب → بنات الأخ بالترتيب المذكور → العمات بالترتيب المذكور → خالات الأم بالترتيب
المذكور → خالات الأب بالترتيب المذكور → عمات الأم بالترتيب المذكور → عمات الأب بالترتيب المذكور.**
**Then**, if no woman from that list is available, not fit, or the women's custody period has ended: «**انتقل الحق في الحضانة إلي
العصبات من الرجال بحسب ترتيب الاستحقاق في الإرث، مع مراعاة تقديم الجد الصحيح علي الإخوة**». **Then**, if none: the male
**محارم** in the order **الجد لأم → الأخ لأم → ابن الأخ لأم → العم → الخال الشقيق → الخال لأب → الخال لأم**.
- ⚠️ **The words «مقدما فيه من يلي بالأم علي من يلي الأب» are the whole game** in disputed cases: where two equally-ranked female
  relatives tie, the maternal side outranks the paternal.
- ⚠️ **Read the list with corrections row 20**: the order is statutory, but **Law 10/2004 Art. 10** directs the court to be guided
  by «**ما تقتضيه مصالح الطفل الفضلى**», and the expert reports under **Art. 11** are compulsory. **Do not promise a parent the
  outcome; tell them the order and the discretion.**
- ✅ **The father's duty to house the children** is in **Art. 18 bis/2**: «**ويلتزم الاب بنفقة أولاده وتوفير المسكن لهم بقدر يساره
  وبما يكفل للأولاد العيش في المستوي اللائق بأمثالهم**» — the level is defined **by reference to the father's means**, i.e. it moves
  up with him.

## 5.2 ⭐ The custody ages — 15 for a girl and a boy alike, and then the child chooses

✅ **Law 25/1929 Art. 20(1), as replaced by Law 4/2005 (Gazette No. 4 bis, 4 March 2005), verbatim:**
> «**ينتهى حق حضانة النساء ببلوغ الصغير أو الصغيرة سن الخامسة عشرة، ويخير القاضى الصغير أو الصغيرة بعد بلوغ هذه السن فى البقاء فى يد
> الحاضنة دون أجر حضانة وذلك حتى يبلغ الصغير سن الرشد وحتى تتزوج الصغيرة.**»

**Read it out, because four things follow and each of them is commonly got wrong:**
1. ✅ **Women's custody ends at 15 for a girl AND a boy** — the pre-2005 split (10 for a boy; until marriage for a girl) is **repealed
   text**. The lawhub note on the article confirms the substitution: «الفقرة الأولى مستبدلة بالقانون رقم ٤ لسنة ٢٠٠٥».
2. ✅ **After 15 the child chooses** (يخير) to remain **in the custodian's hands**.
3. ✅ **From 15, the custodian receives NO custody wage (دون أجر حضانة)** — a custodian who keeps the child after 15 cannot collect
   أجر حضانة for that period. **This is the money trap hidden in the age rule.**
4. ✅ **The two different end dates after 15**: the arrangement lasts **until the boy reaches الرشد** (majority) and **until the girl
   marries** — not a common 18 for both.

## 5.3 Conditions of custody — what the statute says and what it does not

- ✅ **The article's own fitness test**: custody passes over a woman who is not «**أهل للحضانة**» and over a woman who «**لم يكن
  منهم أهل للحضانة**». **The statute does not enumerate the disqualifications.**
- ⚠️ **The classical disqualifications** (marriage of the custodian to a man who is not a محرم of the child; apostasy; gross
  misconduct; incapacity) are **Hanafi fiqh applied through Law 1/2000 promulgating Art. 3(1)** («**يعمل فيما لم يرد بشأنه نص …
  بأرجح الأقوال من مذهب الإمام أبى حنفى**») — **not** a codified list. **Never quote an article number for them.** ⚠️ **The 2026
  draft is reported to add express forfeiture conditions** — again, proposed, not law (§1.2).
- ✅ **Custody is decided with the child's best interest as the court's guide** — Law 10/2004 Art. 10 (with the sessions held **in
  separate premises** from other courts, and **provision for the children's attendance** «وما قد تقتضيه من حضور الصغار تلك الجلسات
  للاستماع إلى أقوالهم» — **listening to the child is written into the statute**).
- ✅ **The Public Prosecution's emergency power** (Law 1/2000 **Art. 70**): where a dispute over the custody of a child **of the age
  of women's custody** is brought to it, or custody is provisionally claimed by the person likely to be awarded it, the **PP may
  issue a reasoned decision handing the child to that person**, signed by **at least a chief prosecutor (رئيس نيابة)**, and it is
  **immediately enforceable until the custody judgment**. **This is the fastest route in a child-removal emergency.**
- ⚠️ **Custody over a child of a different religion / a non-Muslim mother** raises the confessional question (§1.3). The Cassation
  digest records a ruling that **custody as an effect of marriage is governed by Egyptian law alone where one spouse was Egyptian at
  the time of the contract** — but **do not advise on a cross-confessional custody case from this file**; the community's shari'a is
  argued in those cases.

## 5.4 ⭐ رؤية and استضافة — visitation, exactly as the statute and the ministry decision provide

- ✅ **Law 25/1929 Art. 20(2), verbatim:** «**ولكل من الأبوين الحق في رؤية الصغير أو الصغيرة وللأجداد مثل ذلك عند عدم وجود
  الأبوين** [SCC: **that condition is unconstitutional**] **وإذا تعذر تنظيم الرؤية اتفاقا، نظمها القاضي علي أن تتم في مكان لا يضر
  بالصغير أو الصغيرة نفسيا. ولا ينفذ حكم الرؤية قهراً، ولكن إذا امتنع من بيده الصغير عن تنفيذ الحكم بغير عذر أنذره القاضي فإن تكرر
  منه ذلك جاز للقاضي بحكم واجب النفاذ نقل الحضانة مؤقتا إلي من يليه من أصحاب الحق فيها لمدة يقدرها.**
- ✅ **Both parents have the right; grandparents have it too.** The words «**عند عدم وجود الأبوين**» (grandparents only where the
  parents are absent) were **struck down as unconstitutional** — **SCC, Case 37 of judicial year 33, session 12 May 2013
  (2 Rajab 1434), published Gazette No. 21 bis, 26 May 2013** — and the consolidated text carries the SCC note («**حكم بعدم
  دستورية الفقرة**»). **Grandparents claim رؤية in their own right.**
- ✅ **The place must not harm the child psychologically** — the court fixes it if the parties cannot agree. ✅ **The order CANNOT be
  enforced by force** — this is express, and it is corrections row 18. ✅ **The sanction for unjustified refusal is temporary transfer
  of custody** to the next person in the order, for a period the judge fixes, **by an immediately enforceable judgment**.
- ⚠️ **The operational layer — MoJ Decision 1150/2010 (لائحة تنظيم رؤية المحضونين), Art. 12**, quoted in a 2026 press report:
  «…**يحدد القاضي مدة الرؤية أو المبيت بحيث تكون مرة أو مرتين من كل أسبوع لأحد الأبوين ومرة أو مرتين في الشهر للأجداد و٣ أو ٤
  مرات في السنة لباقي من لهم حق الرؤية من الأقارب المحارم** ما لم يتفق الطرفان على خلاف ذلك … كما يجوز له الإذن بالتواصل عبر وسائل
  الاتصال الحديثة مع المحضون في أوقات يحددها …» ⚠️ **This is a secondary quotation of the decision; the decision itself was not
  retrieved. Cite it as "the ministry regulation reported to provide…", not as verbatim law.** Its practical value: it shows the
  **baseline quotas** (a parent once or twice weekly; grandparents once or twice monthly; other relatives 3–4 times a year) and that
  **electronic contact** is already contemplated.
- ⚠️ **استضافة (overnight hosting)** is **not** a term of the statute: it is the practice/short-hand for extended contact and
  overnight stays, and it is one of the things the **2026 bills would codify** (reported proposals: *one 24-hour stay per week*, the
  first and third weeks of July/August/September, the second and third days of Eid al-Fitr and the third and fourth of Eid al-Adha,
  with a **suspension sanction if the paying parent falls 3 months behind** — `parlmany.com`, 16 Apr 2026). **Reported as a proposal,
  never as law.** See §11.
- ⚠️ **Execution of visitation orders**: **Art. 67** (رؤية to be executed at places designated by a Justice-Minister decision with
  the Social Affairs Minister's approval, **unless the custodian and the judgment creditor agree on another place**; the place must give
  the child security), **Art. 69** (execution by bailiffs or the administration, under a Justice-Minister decision), **Art. 66**
  («**يجوز تنفيذ الأحكام والقرارات الصادرة بضم الصغير وحفظه وتسليمه جبرًا**» — **ضم/حفظ/تسليم may be executed by force**, with entry to
  homes «وفق ما يأمر به قاضى التنفيذ» and re-execution with the same instrument whenever needed), **Art. 65** (judgments for
  **تسليم الصغير، رؤيته، النفقات، الأجور والمصروفات** are «**واجبة النفاذ بقوة القانون وبلا كفالة**»), **Art. 68** (the court registry
  adds the executory formula), and **Art. 70** (the **Public Prosecution's** reasoned, immediately enforceable decision to hand over a
  child of custodial age pending the custody judgment). ✅ **All six articles are now read verbatim — see §9.2–§9.3, which supersedes
  the earlier secondary quotation used in this bullet.** **Note the asymmetry that is verified**: **رؤية is never by force** (Art. 20
  of 1929), while **تسليم/ضم** may be (Art. 66) — do not merge the two.

## 5.5 The children's housing — and the constitutional subtraction

✅ **Law 25/1929 Art. 18 bis/3 (added by Law 100/1985), verbatim:**
> «**على الزوج المطلق أن يهيئ لصغاره من مطلقته ولحاضنتهم المسكن المستقبل المناسب، فإذا لم يفعل خلال مدة العدة، استمروا في شغل
> مسكن الزوجية المؤجر دون المطلق مدة الحضانة. وإذا كان مسكن الزوجية غير مؤجر كان من حق الزوج المطلق أن يستقل به إذا هيأ لهم
> المسكن المستقبل المناسب بعد انقضاء مدة العدة. ويخير القاضي الحاضنة بين الاستقلال بمسكن الزوجية وبين أن يقدر لها أجر مسكن مناسب
> للمحضونين ولها. فإذا انتهت مدة الحضانة فللمطلق أن يعود للمسكن مع أولاده إذا كان من حقه ابتداء الاحتفاظ به قانونا.
> وللنيابة العامة أن تصدر قرارا فيما يثور من منازعات بشأن حيازة مسكن الزوجية المشار إليه حتي تفصل المحكمة فيها.**»

**⚠️ TWO SUBTRACTIONS, both from the SCC — read the article with them struck out (the SCC note is printed at the foot of the
consolidated text):**
1. ✅ **The obligation does not apply where the children have present money sufficient for housing, or where the custodian has a
   dwelling — rented or not** — **SCC, Case 5 of judicial year 8, session 6 January 1996**, published **Gazette No. 3, 18 January
   1996** («**إلزامها المطلق بتهيئة مسكن مناسب … ولو كان لهم مال حاضر يكفى لسكناهم، أو كان لحاضنتهم مسكن تقييم فيه، مؤجرا كان أم
   غير مؤجر**»).
2. ✅ **The time limit** the article imposed on the husband's obligation was also struck down («**تقييدها حق المطلق … بان يكون إعداده
   مسكنا مناسبا … واقعا خلال فترة زمنية**»).
**Consequence for a non-lawyer**: if the mother has her own flat or the children have money, **the "stay in the marital home"
mechanism is unavailable** — and the court's remedy becomes **أجر مسكن (a rent allowance)** instead. ⚠️ **Do not tell a client
"she keeps the flat"; the correct advice is "she may keep it, or get a rent allowance instead, depending on what she already has".**
✅ **The Public Prosecution may decide possessory disputes over the marital home pending the court's ruling** — the last paragraph.

## 5.6 الولاية على النفس — the *wali*, and what the statute actually does with it

- ✅ **The statute's only direct trace of the wali is Law 1/2000 Art. 9(أولاً)(7)**: among the **District Court's** powers is
  «**الإذن بزواج من لا ولى له**» — **permission for the marriage of a woman who has no wali.** So the legislature's assumption is
  that a wali's involvement exists, **and that the court substitutes for an absent one**.
- ⚠️ **The substantive position (Dar al-Ifta — a FATWA, not law; and the fatwas are unambiguous that Egyptian law follows the Hanafi
  school here):** «**رأى الإمام أبو حنيفة أن البالغة الرشيدة لا ولاية لأحدٍ عليها … فلها أن تزوِّج نفسها … بكرًا كانت أم ثيبًا …
  وقد أخذ القانون المصري بمذهب السادة الحنفية فجعل للمرأة البالغة حق تزويج نفسها، ويعدُّ زواجها صحيحًا إذا تزوجت من كفءٍ
  بمهرِ مثلِها**» (fatwa of Dr Ali Gomaa, 30 June 2005), and: «**الولايةَ عليها حينئذٍ تكون ولاية استحبابٍ لا ولاية إجبارٍ**»
  (fatwa of Dr Shawqi Allam, 27 Feb 2024). **A second fatwa (30 Mar 2026) repeats it and states the doctrine expressly: «إن جمهور
  الفقهاء يرى أن وجود الولي شرط لكمال عقد الزواج وليس شرطًا لصحته».** ⚠️ **Dar al-Ifta also preserves the wali's classical
  challenge**: where she married a **non-compatible (غير كفء)** man or **below مهر المثل**, «**يجوز للولي في هذه الحالة الاعتراض على
  الزواج … وله المطالبة بالفسخ عند ثبوت ما يدعيه؛ وذلك عن طريق القضاء**» — **again, a fatwa, not a statute.** See §11 (fatwas and
  advocacy positions are not law).
- ⚠️ **The gap between the fatwa and the counter** — and this is the practical truth a non-lawyer needs: **Ma'zouns in Egypt are
  reported to demand a wali for a bride, of any age, and one 2023 investigative report quotes a Ma'zoun as saying there are
  «تعليمات شفوية من محكمة الأسرة … بألا يزوج فتاة بكرًا دون ولي، إذا كانت دون الأربعين من عمرها»** (`fakartany.net`, 13 Nov 2023).
  🟡 **That report is journalism, not a regulation — I could not verify any such instruction in the Ma'zoun Regulations.** **Practical
  rule for an agent: tell the client the law allows her to marry without a wali if she is an adult of sound mind, that a wali (or a
  written power of attorney to a person who acts as one) is the practical path, and that if the office refuses, the remedy is an
  application to the District Court under Art. 9(أولاً)(7).**
- ✅ **The age rule and the wali do NOT combine to allow child marriage**: Art. 31 bis of Law 143/1994 forbids documenting a marriage
  for anyone under **18 complete calendar years**, with **no guardian-consent exception** (§2.2). ⚠️ **So the classical "she may marry
  young with the wali's consent" is dead in the statute** — a point the fatwa literature sometimes blurs.
- 🟡 **الولاية التعليمية (educational guardianship)** — the jurisdiction to decide a child's schooling — is **not** a codified
  article I could retrieve; it is handled in family-court practice as part of الولاية على النفس. ⚠️ **The 2026 drafts reorganise
  الولاية على النفس in full** and are reported to address the wali's role. **Do not state a rule; the file cannot support one.**

## 5.7 الولاية على المال — guardianship over property: a different regime with the same court

- ✅ **Law 1/2000 Art. 9(ثانياً)** gives the **District Court** the property-guardianship docket where the value does not exceed its
  jurisdiction: **appointing the وصي, the مشرف, the مدير**, supervising, **discharging and replacing** them; **establishing and ending
  الغيبة** and appointing a **وكيل عن الغائب**; **المساعدة القضائية**; «**استمرار الولاية أو الوصاية إلى ما بعد سن الحادية والعشرين**»
  and **authorising the minor to receive and manage his property, trade and act**; appointing a **مأذون بالخصومة**; **assessing
  maintenance for the minor out of his own property** and deciding disputes **between the ولى النفس/ولى التربية and the وصي** over the
  minor's maintenance, upbringing or care; **excusing the wali**; **تنحى الولى واستردادها**; **authorising what is spent for a minor's
  marriage**; **all other property-management matters**, of whatever value, and property-preservation measures; and, where the estate
  does not exceed the court's jurisdiction, **appointing an estate administrator, discharging and replacing him and deciding
  liquidation disputes**.
- ✅ **Minority and capacity**: **majority (الرشد) is reached at 21** — that is the statutory assumption behind Art. 9(ثانياً)(4)'s
  «استمرار الولاية … إلى ما بعد سن الحادية والعشرين». ✅ **Litigation capacity in الولاية على النفس is complete at 15** (Art. 2).
- ✅ **The Public Prosecution's role (Arts. 26–29)**: it **protects the interests of persons lacking/failing capacity and absentees,
  preserves and supervises the administration of their money**, may **delegate a judicial police officer**, may use **assistants
  attached to it by a Justice-Minister decision who are judicial police officers** for those tasks, and **may assess provisional
  maintenance out of the entitled person's property until the court assesses it**. ✅ **Reporting duties**: close relatives living in
  one household with the deceased, or the eldest of-age heir, must **inform the PP of a death of an absentee/incapacitated person or
  a pregnant woman (حمل مستكن) or the death of a wali, trustee, curator or agent of an absentee within three days**; treating doctors
  and hospital directors must report **loss of capacity from mental defect**; the **trustee of a pregnant woman (الوصى على الحمل
  المستكن)** must report the end of pregnancy or the birth, alive or dead.
- ✅ **Art. 47** — the **PP may authorise** the representative of an incapacitated or absent person to **disburse from liquid funds
  without going to court** within a statutory ceiling. ⚠️ **The consolidated copy read for this file still prints the OLD text**
  («**بما لا يجاوز مبلغ ألف جنيه يجوز زيادته إلى ثلاثة آلاف جنيه … وذلك لمرة واحدة كل ستة أشهر**»), because it was not updated.
  ✅ **Law 176/2020 replaced Art. 47** — «**يستبدل بنص المادة (47)**» — and the **Gazette page scan of Law 176/2020** (read as a page
  image, OCR-checked) prints the new text, whose **figures are spelled out in words**: «**بما لا يجاوز مبلغ عشرة آلاف جنيه، ويجوز
  زيادته إلى عشرين ألف جنيه بقرار من المحامى العام المختص، وذلك لمرة واحدة كل ثلاثة أشهر**»; plus a new emergency paragraph letting
  the Attorney-General raise the amount **in cases of extreme necessity, accidents or illness requiring urgent medical intervention**,
  «**بقدر حالة الضرورة ونفقتها**», with supporting documents required before the next disbursement request. ⭐ **So the ceilings are
  now 10,000 / 20,000 EGP and the frequency is once every three months, not six.** ⚠️ The **Gazette issue number** of Law 176/2020 is
  recorded in two forms — «العدد ٣٧ مكرر» vs «العدد ٣٦ (مكرر)», both **5 September 2020** — and I did not resolve it (§12).
- ✅ **Art. 51** — the court may order **all or some of the fees and expenses charged to the public treasury**. ✅ **Art. 50** —
  estate-preservation expenses rank **with judicial expenses** in privilege.
- ⚠️ **The substantive law of property guardianship is Law 119/1952 (الولاية على المال)** — cited as the framework but **not read in
  this pass**. 🟡 **An agent asked about a minor's money should check Law 119/1952's articles directly.**

---

# 6. Parentage (النسب) — how a child is attached to a father, and the DNA question

**Citation:** **Law 25/1929 Art. 15**; **Law 1/2000 Arts. 7, 24–25**; **Law 10/2004 Arts. 3, 11**; the Hanafi default via **Law 1/2000
promulgating Art. 3(1)**.
**Status:** in force. ⚠️ **This is the area with the most confident wrong advice on the internet.**
**Sources:** ✅ Art. 15 of Law 25/1929 and ✅ Arts. 7, 24–25 of Law 1/2000, read verbatim from the consolidated texts (as in §3) ·
⚠️ **Dar al-Ifta** and the Cassation heading index on «الولد للفراش».
**As of:** 2026-10-19.

## 6.1 الولد للفراش — the base rule, and the statutory time limits on disproving it

- ⚠️ **The classical rule — «الولد للفراش» (a child born within a valid subsisting marriage is attributed to the husband)** — is
  **Hanafi fiqh applied through Law 1/2000 promulgating Art. 3(1)**, not a numbered article. ✅ The Cassation's personal-status
  digest lists النسب under Law 25/1929 Art. 15 and treats the rule as settled.
- ✅ **Law 25/1929 Art. 15 — the statute's only door-closer, verbatim:**
  > «**لا تسمع عند الإنكار دعوي النسب لولد زوجة ثبت عدم التلاقي بينها وبين زوجها من حين العقد ولا لولد زوجة أتت له بعد سنة من غيبة
  > الزوج عنها ولا لولد المطلقة والمتوفي عنها زوجها إذا أتت به لأكثر من سنة من وقت الطلاق أو الوفاة.**»
  **Three situations in which a *claim* of parentage is not heard on denial**: (1) where it is established that the spouses **never
  met** since the contract; (2) a child **born more than a year after the husband's absence**; (3) a child born **more than a year
  after divorce or the husband's death**. ⚠️ **Note that the article speaks to the *claim*, and that the year is the statutory
  working limit — the classical فقه periods (six months minimum; up to two years for pregnancy) are doctrine, not this article.**
- ✅ **Art. 2 of Law 25/1929** — inheritance requires the heir to be **alive at the death** or at the presumed-death judgment; a
  **حمل مستكن is entitled to inherit** subject to **Art. 43** (the estate is held for the unborn child). *(Used here for the
  unborn-child rules.)*
- ✅ **The death certificate route** (below, §6.2) is how a legal heir is established in practice.

## 6.2 Acknowledgement after death — the strictest test in the whole file

- ✅ **Law 1/2000 Art. 7, verbatim:**
  > «**لا تقبل عند الإنكار دعوى الإقرار بالنسب أو الشهادة على الإقرار به بعد وفاة المورث إلا إذا وجدت أوراق رسمية أو مكتوبة
  > جميعها بخط المتوفى وعليها إمضاؤه أو أدلة قطعية جازمة تدل على صحة هذا الادعاء.**»
  **Three admissible routes, and only three**: **official documents**; **a writing wholly in the deceased's own hand and signed by
  him**; or **conclusive and decisive evidence**. ⚠️ **Nothing else.** Note «**بعد وفاة المورث**» — the article governs
  **after-death** claims; a claim against a living alleged father is not governed by it.
- ✅ **Law 1/2000 Arts. 24–25 — the certification route:** an applicant for **إشهاد الوفاة أو الوراثة أو الوصية الواجبة** applies to
  the competent court **attaching an official paper proving the death**, states the **last domicile of the deceased, the heirs, the
  obligatory-will legatees and their domiciles**, **serves them with notice** for the hearing, and the **judge verifies the
  application by reliable testimony and may add administrative enquiries**; **if an heir or obligatory legatee denies and the judge
  considers the denial genuine, he must refer the application to the Court of First Instance**; and **Art. 25** — the certificate is
  **conclusive evidence of the death, the inheritance and the obligatory will unless a judgment rules otherwise**.
- ✅ **Law 10/2004 Art. 3(3)** — **the president of the Family Court issues the death and inheritance certificates**, and may refer
  them to the court **where a serious dispute arises**.
- ✅ **Law 10/2004 Art. 11 (last para, added by Law 215/2017)** — in a **نسب** case, the **social expert's report must state whether
  the child is in the alternative-family system (نظام الأسر البديلة) of the Ministry of Social Solidarity or not.**

## 6.3 ⭐ DNA (البصمة الوراثية) — ❌ there is no statute; read this before promising anything

**This is corrections row 3, expanded. The negative finding is the deliverable.**
- ❌ **No Egyptian statute gives a DNA test binding force in a nasab claim.** I searched for one — a statute making the genetic
  fingerprint decisive evidence, or compelling a party to submit to testing — and found **none**. **Do not cite one.**
- ⚠️ **What actually happens**: the report is an **expert opinion (تقرير خبير)** under the ordinary rules of evidence — the court
  weighs it and **is not bound** to adopt it, and **no statute compels a party to submit to the test**. Where the husband refuses,
  the outcome is a **judicial evaluation of that refusal**, not an automatic determination.
- ⚠️ **The attestations that do exist**: the Cassation's Nassab jurisprudence (indexed under Law 25/1929 Art. 15) and the
  evidentiary weight of an **expert medical report** in the personal-status file. **These are case-law and practice, not a DNA
  statute.**
- ⚠️ **A related trap**: **the 2026 family-law drafts are reported to regulate «البصمة الوراثية»** as part of الولاية على النفس.
  **Not law.** If an agent searches "Egypt DNA paternity law", the hits will be the *draft* coverage and comparative pages. 🟡
  *Searched: Arabic queries on «البصمة الوراثية إثبات النسب مصر قانون», «الدليل الجيني المحاكم المصرية» — no statute located.*

## 6.4 The child of an عرفي (undocumented) marriage

- ✅ **Child maintenance and custody belong to the child**, and the statute's rules for them are independent of the parents' marriage
  (§5, §4.1). **A child's right to maintenance from his father is not conditioned on the marriage being documented** — «**إذا لم يكن
  للصغير مال فنفقته على أبيه**» — the condition is **paternity and minority**.
- ⚠️ **But establishing paternity is where the عرفي marriage hurts the child**: the mother's claim is, in form, a **nasab** claim, and
  the **evidence problem of §2.4** applies. The **documented** facts that help: the عرفi contract in writing, hospital records
  naming the father, acknowledgements, correspondence, and (⚠️ with the limits in §6.3) testing. **The statutory limits of Art. 15
  (one-year bars) bite hard here — which is why a late claim is often framed as a claim by the CHILD, whose own right is argued to be
  unaffected by the mother's delay.** ⚠️ **I did not find a retrieved text settling that framing; flag it and get it checked.**
- ✅ **The child's maintenance runs from the father's abstention** (Art. 18 bis/2), and **Art. 70 of Law 1/2000 gives the Public
  Prosecution power to hand the child to the person whose interest lies with it, pending judgment** — a route that does not depend on
  the marriage papers.

---

# 7. Inheritance (الميراث) and wills (الوصية) — the unified law, the shares, and the criminal offence of withholding them

**Citation:** **Law 77/1943** (المواريث) — **Arts. 1–25**, and **Art. 49** (added by **Law 219/2017**); **Law 71/1946** (الوصية) —
**Arts. 37, 76, 78**; **Law 1/2000** Arts. 24, 25; **Law 10/2004** Art. 3.
**Status:** in force; **Art. 49 has been upheld by the SCC.** ✅ **Inheritance and wills are UNIFIED for all Egyptians** — see §1.3 and
corrections row 16. **The confessional rules do not apply here.**
**Sources:** ✅ **Law 77/1943** consolidated with the **Law 219/2017** footnote, `lawhub.info/eg/?p=11346`, read locally (Arts. 1–25
in sequence) · ✅ **Law 71/1946 Art. 37** and **Art. 76** (from `lawhub.info/eg/?p=11414` and the SCC judgment reproducing Art. 76
verbatim), **Art. 78** quoted by **Dar al-Ifta** in its explanatory fatwa · ✅ **Art. 49 of Law 77/1943** read in the SCC judgment
reproduced by `alberonsy.com` and in the Ministry-of-Justice-style summary on `manshurat.org/node/22420` · ✅ the SCC's refusal of the
constitutional challenge (below).
**As of:** 2026-10-19.

## 7.1 Wills — one-third, and it may go to an heir

- ✅ **Law 71/1946 Art. 37, verbatim:** «**تصح الوصية بالثلث للوارث وغيره وتنفذ من غير إجازة الورثة، وتصح بما زاد على الثلث ولا تنفذ
  فى الزيادة إلا إذا أجازها الورثة بعد وفاة الموصى وكانوا من أهل التبرع عالمين بما يجيزونه.**»
  **Three consequences, and corrections row 4 is built on them: (1) a bequest of up to one-third is valid — to an heir or to a
  non-heir — and takes effect WITHOUT the heirs' consent; (2) a bequest above one-third is valid but NOT effective as to the excess,
  unless the heirs consent; (3) the consent must be given AFTER the testator's death, by persons legally competent to donate,
  knowing what they are approving.** ⚠️ **Rule (1) is the one that contradicts the popular "الوصية لوارث باطلة" — the Egyptian
  statute deliberately departed from that position.**
- ⚠️ **A will is a gratuitous disposition (تبرع) with a one-third ceiling** — and **Art. 37 also governs** the case of a person with
  no heir and no debt: the whole estate may be bequeathed without Treasury approval.
- ✅ **The الوصية الواجبة (obligatory will) — Law 71/1946 Art. 76**, read verbatim in the SCC's own judgment: «**إذا لم يوص الميت
  لفرع ولده الذى مات فى حياته أو مات معه ولو حكمًا بمثل ما كان يستحقه هذا الولد ميراثًا فى تركته أو كان حيًّا عند موته وجبت للفرع
  فى التركة وصية بقدر هذا النصيب فى حدود الثلث بشرط أن يكون غير وارث وألا يكون الميت قد أعطاه بغير عوض ما يساوى الوصية الواجبة**…»
  **In plain terms: if a grandparent dies without having bequeathed to the children of a child who predeceased him, those
  grandchildren take an obligatory bequest equal to the share their parent would have taken, capped at one-third, provided they are
  not themselves heirs and were not already given that much.** ✅ **Art. 78** — **the obligatory will ranks ABOVE other wills**. ✅
  **Cassation (Appeal 212/74, session 11 Feb 2014, per Dar al-Ifta): the obligatory will is extracted from the estate FIRST, then the
  remainder is distributed among the heirs, whether fixed-share or residuary.** ✅ **The SCC upheld Art. 76** — it had rejected a
  challenge in **Case 46 of judicial year 7, session 4 April 1987**, and refused the later challenge (the 2021 judgment reproduced on
  `sccourt.gov.eg` holds that the constitutional docket did not extend to Arts. 77–79 because the defence had not covered them).
- ⚠️ **Practical point**: the **الوصية الواجبة is claimed and certified in the same court application as the inheritance
  certification** (Law 1/2000 Art. 24 names «الوصية الواجبة» expressly) — so the grandchild's route is: **application for إشهاد
  الوفاة والوراثة والوصية الواجبة**, served on the heirs, with referral to the Court of First Instance if the denial is genuine.

## 7.2 التركة — what the estate is, and the order of payment

✅ **Law 77/1943 Art. 4, verbatim:**
> «**يؤدى من التركة بحسب الترتيب الآتي: أولا – ما يكفى لتجهيز الميت ومن تلزمه نفقته من الموت الى الدفن. ثانيا – ديون الميت. ثالثا –
> ما أوصى به فى الحد الذى تنفذ فيه الوصية. ويوزع ما بقى بعد ذلك على الورثة، فإذا لم يوجد ورثة قضى من التركة بالترتيب الآتي: أولا –
> استحقاق من أقر له الميت بنسب على غيره. ثانيا – ما أوصى به فيما زاد على الحد الذى تنفذ فيه الوصية، فإذا لم يوجد أحد من هؤلاء آلت
> التركة أو ما بقى منها إلى الخزانة العامة.**»
**Three payments before any heir receives anything: (1) burial/funeral costs for the deceased and those whose maintenance he owed
from death to burial; (2) the deceased's debts; (3) the will up to the enforceable limit. Then distribution.** And **where there is
no heir at all**, the order becomes: **first, the acknowledgement of a person the deceased acknowledged as a نسب relative; then any
bequest above the one-third limit; and failing these, the estate (or what remains) goes to the Public Treasury.**
- ⚠️ **Where the widow's مؤخر الصداق sits**: in «**ديون الميت**» — the second rank, ahead of the will and ahead of distribution
  (§4.2). ⚠️ **Characterised, not quoted: the statute says "the deceased's debts" and the deferred mahr is a debt; no article says
  "المؤخر" by name.**
- ✅ **Art. 1** — inheritance accrues **on the death** or on a **judgment presuming death**. ✅ **Art. 2** — the heir must be **alive
  at the death**; an unborn child (حمل مستكن) inherits subject to Art. 43. ✅ **Art. 3** — where two people die and the order is
  unknown, **neither inherits from the other**, whether or not the deaths were in one accident. ✅ **Art. 5** — **murder of the
  deceased is a bar to inheritance** — including being a **false witness** whose testimony led to an execution — if the killing was
  without right or excuse and the killer was **sane and aged 15 or over**; **excess in self-defence is treated as an excuse**.
- ✅ **Art. 6 — the religion rule, verbatim:** «**لا توارث بين مسلم وغير مسلم. ويتوارث غير المسلمين بعضهم من بعض، واختلاف الدارين لا
  يمنع من الإرث بين المسلمين ولا يمنع بين غير المسلمين إلا إذا كانت شريعة الدار الأجنبية تمنع من توريث الأجنبى عنها.**»
  **There is NO inheritance between a Muslim and a non-Muslim; non-Muslims inherit from each other; and difference of country does
  not bar inheritance** (for Muslims, and for non-Muslims unless the foreign law bars it). ⚠️ **For a mixed-religion marriage this
  is a hard rule with severe consequences for the survivor — and it is one of the provisions said to raise a Constitution Art. 3
  question (§1.3). Note it, and note it is still the text.**
- ✅ **Art. 7** — causes of inheritance: **الزوجية (marriage), القرابة (kinship), العصوبة السببية**; marriage gives a **فرض**;
  kinship gives a **فرض, تعصيب, or both, or رحم**, subject to الحجب and الرد. ✅ **Art. 8** — «**الفرض سهم مقدر للوارث فى التركة،
  ويبدأ فى التوريث بأصحاب الفروض**» and lists them: **الأب، الجد الصحيح وإن علا، الأخ لأم، الأخت لأم، الزوج، الزوجة، البنات، بنات
  الابن وإن نزل، الأخوات لأب وأم، الأخوات لأب، الأم، الجدة الصحيحة وإن علت.**

## 7.3 The Quranic shares (الفروض) — read the numbers off the articles, not from memory

| Heir | Share | Article |
|---|---|---|
| **الزوج** | **1/2** if no descendant; **1/4** with a descendant | Art. 11 ✅ |
| **الزوجة** | **1/4** if no descendant; **1/8** with a descendant — **and the plural زوجات share that one fraction** | Art. 11 ✅ |
| **المطلقة الرجعية** who dies leaving her in the idda | **counts as a wife** — so she inherits | Art. 11 ✅ |
| **المطلقة بائنا in مرض الموت** who did **not** consent to the divorce, where the divorcer **died of that illness while she was in the idda** | **treated as a wife** | Art. 11 ✅ |
| **الأب** | **1/6** where there is a child or a child's son however low | Art. 9 ✅ |
| **الجد الصحيح** (meaning: one whose line to the deceased has no female link) | **1/6** on the same terms | Art. 9 ✅ |
| **الأم** | **1/6** with a descendant or with two or more siblings; **1/3** otherwise — **but where she is with one spouse and the father only, she takes 1/3 of what remains after the spouse's share** | Art. 14 ✅ |
| **الجدة الصحيحة** (mother of a parent or of a correct grandfather, however high) | **1/6**, shared equally among the grandmothers | Art. 14 ✅ |
| **أولاد الأم** (maternal siblings) | **1/6** for one; **1/3** for two or more, **males and females equally** | Art. 10 ✅ |
| **البنات** | **1/2** for one; **2/3** for two or more | Art. 12 ✅ |
| **بنات الابن** | the same where there is no daughter or higher son's-daughter; **1/6** with a daughter or a higher son's-daughter | Art. 12 ✅ |
| **الأخوات الشقيقات** | **1/2** for one; **2/3** for two or more | Art. 13 ✅ |
| **الأخوات لأب** | the same where there is no full sister; **1/6** with a full sister | Art. 13 ✅ |
| **الأب or الجد with a daughter / son's daughter** | **1/6 as فرض PLUS the remainder as تعصيب** — subject to Art. 21 | Art. 21 ✅ |

- ⚠️ **This table is the bare فرض layer, not a توزيع.** The rules of **الحجب (exclusion), الرد (return of the residue), العصوبة
  (residuary entitlement), and the special combinations (العمريتان, الأكدرية …)** are in **Arts. 15–23** and are arithmetic. **Never
  tell a person what their share is from this table alone**; the distribution needs the full family tree.
- ⚠️ **The one arithmetic error everyone makes**: the wife's share is **1/8 only where there is a descendant**; **1/4** where there
  is none. Corrections row 17.
- ✅ **The marriage must be a valid marriage at the death** for the spouse's فرض to arise (Art. 11's terms), and the **رجعي**
  divorcée during the idda is expressly included.

## 7.4 ⭐ Law 219/2017 — the criminal offence of withholding an inheritance

✅ **Art. 49 of Law 77/1943, ADDED by Law 219/2017 as a new «باب تاسع — العقوبات»**, read verbatim from the text reproduced in the
SCC judgment and the Ministry summary:
> «**مع عدم الإخلال بأية عقوبة أشد ينص عليها أي قانون آخر، يعاقب بالحبس مدة لا تقل عن ستة أشهر وبغرامة لا تقل عن عشرين ألف جنيه
> ولا تجاوز مائة ألف جنيه، أو بإحدى هاتين العقوبتين، كل من امتنع عمدًا عن تسليم أحد الورثة نصيبه الشرعي من الميراث، أو حجب سندًا
> يؤكد نصيبًا لوارث، أو امتنع عن تسليم ذلك السند حال طلبه من أي من الورثة الشرعيين.**
> **وتكون العقوبة في حالة العود الحبس الذي لا تقل مدته عن سنة.**
> **ويجوز الصلح في الجرائم المنصوص عليها في هذه المادة في أي حالة تكون عليها الدعوى ولو بعد صيرورة الحكم باتًّا.**
> **ولكل من المجني عليه أو وكيله الخاص، ولورثته أو وكيلهم الخاص، وكذلك للمتهم أو المحكوم عليه أو وكيلهما الخاص، إثبات الصلح في
> هذه الجرائم أمام النيابة أو المحكمة بحسب الأحوال.**»

**The verified reading, element by element:**
| Element | The text |
|---|---|
| **Penalty** | **imprisonment of not less than 6 months**, and/or a fine of **20,000 to 100,000 EGP** ✅ |
| **Repeat offence (العود)** | **imprisonment of not less than 1 year** ✅ |
| **Conduct (three forms)** | (1) **knowingly refusing to hand an heir his shari'a share**; (2) **concealing a document evidencing a share**; (3) **refusing to hand over that document on demand** by any shari'a heir ✅ |
| **Reconciliation (الصلح)** | allowed **at any stage, even after the judgment is final**; it **extinguishes the criminal case** (even if brought by direct accusation) and the PP **stops execution** if it occurs during execution; **it does not affect the victim's civil rights** ✅ |
| **Who may settle** | the victim or his private agent, his heirs or their agent; and the accused/convicted person or their agent — proved **before the PP or the court**, as the case may be ✅ |
| **The offence's elements as summarised in the legal press** | (1) an estate owned by the deceased; (2) the estate **in the possession (حيازة) of one of the heirs**; (3) the holder's refusal to hand it to the entitled person ✅ *(a lawyer's summary, not the statute)* |
| **Constitutional status** | ⚠️ **Upheld.** A challenge was referred in **Dec 2021** (`manshurat.org/node/74846`) as to the absence of a requirement of a **final amicable or judicial partition**; the SCC **refused the challenge** in a judgment reported **8 July 2023**, on the basis that the article **protects the right of inheritance as a source of the right of private property under Constitution Art. 35** ✅ |
| **Legislative purpose** | the Explanatory Memorandum states that no previous law addressed the failure to hand over estate assets, that the practice **mostly affected women**, and that the **Council of Senior Scholars of Al-Azhar approved** the text ✅ |

⚠️ **Three cautions an agent must carry:**
1. **It is not an automatic "brother goes to prison" rule** — the offence requires **intent (عمدًا)** and **possession of the estate by
   the refusing heir**; the accused can settle out of it at any time; and the civil claim survives settlement.
2. **It is in Law 77/1943, Art. 49 — NOT in the Penal Code**, and the article is new (2017) — which is why searches for "عقوبة حرمان
   البنت من الميراث في قانون العقوبات" return nothing.
3. **The complaint route is normal criminal procedure** — see file `06-criminal-procedure-egypt.md` for how a complaint, direct
   accusation (الادعاء المباشر, which the article's text expressly contemplates) and the criminal case run.

## 7.5 An unregistered (عرفي) marriage and inheritance — the two ways it fails

- ✅ **The widow's claim is a claim "arising out of the marriage contract"** (a claim of inheritance **by reason of the marriage**),
  and **Law 1/2000 Art. 17(2)** refuses such claims **on denial** unless the marriage is proved by an **official document** — so an
  **عرفي widow cannot claim her inheritance where the heirs deny the marriage**. ⚠️ **This is the Code's own text applied to the
  inheritance claim; state it as the direct consequence of Art. 17(2), and note that the *defence* of "no marriage" is a denial
  within that article.**
- ✅ **A SECOND, independent bar for a divorced wife**: **Law 25/1929 Art. 17** — «**لا تسمع عند الإنكار دعوى الإرث بسبب الزوجية
  المطلقة توفى زوجها بعد سنة من تاريخ الطلاق**» — a **divorced** wife's inheritance claim is not heard on denial where the husband
  died **more than a year after the divorce** — **but note the mirror-image protection in Art. 5 bis(3)**: where the husband
  **concealed** the divorce, **her inheritance and other financial rights run only from the date she learned of it** (§3.1).
  **Read the two together: the year runs from what she knew, if he hid it.**
- ✅ **The child's route**: the child inherits from his father (and through him) **only once the نسب is established** — so the
  evidence problems of §6.3 govern. ⚠️ The **documentary routes** that work in practice: a **written acknowledgement of paternity**,
  official documents, a judgment of نسب, and — where the father is alive — an **acknowledgement before the court**.
- ✅ **Where the deceased leaves a written document**: nothing prevents an heir from using it — but note that **Law 1/2000 Art. 7's
  three-route test applies only to post-death acknowledgement claims**, not to documents used in distribution.

## 7.6 Getting the estate certified — the procedural track

- ✅ **Law 1/2000 Arts. 24–25** — the application, the official death paper, the notice to the heirs and obligatory-will legatees, the
  verification by testimony, **the referral to the Court of First Instance if the denial is genuine**, and the certificate's
  conclusiveness «**ما لم يصدر حكم على خلافه**».
- ✅ **Law 10/2004 Art. 3(3)** — the **president of the Family Court** issues the death and inheritance certificates and may refer
  them to the court when a serious dispute arises.
- ✅ **Law 1/2000 Art. 8(2)** — an **estate claim** is not heard on denial if brought **more than 33 years after the right was
  established**, unless an excuse prevented it. ⚠️ *(Quoted alongside the waqf rule in the same article — read it as the long-stop it
  is, and check its application to your facts.)*
- ✅ **Practical**: the certified **إشهاد الوراثة** is what banks, registries and the real-estate office ask for; and the **إشهاد
  الوصية الواجبة** comes in the same application.

---
# 8. The Family Courts — how a case is actually brought, step by step

**Citation:** **Law 10/2004** — promulgating (إصدار) Arts. **1–5** and annexed Arts. **1–15**; **Law 1/2000** — promulgating Arts.
**1–6** and annexed Arts. **2–19, 23–25, 52–64**; **Law 1/2000 promulgating Art. 5** (the Ma'zoun/notary and document-form
regulations said to underlie the ministry decisions cited at §2.2).
**Status:** all in force. Law 10/2004 takes effect **1 October 2004** and was signed **17 March 2004**. Annexed Art. 11 was amended by
**Law 215/2017**; promulgating Art. 2 was amended by **Law 142/2006** (⚠️ the amending text was not read in this pass — so do not
quote the *pre-2006* transfer rule as current).
**Sources:** ✅ the **consolidated Law 10/2004** (promulgating Arts. 1–5 and annexed Arts. 1–15 read article by article, with the Law
215/2017 footnote printed under Art. 11), `lawhub.info/eg/?p=11675` · ✅ the **consolidated Law 1/2000** (promulgating Arts. 1–6 and
annexed Arts. 2–19, 23–25, 52–64 read article by article), `mksegypt.org/ar/laws/24131` · ✅ the **Gazette scan** of Law 215/2017
(OCRed page image) · ⚠️ the **amendment of promulgating Art. 2 by Law 142/2006** — from the index only.
**As of:** 2026-10-19.

## 8.1 The court, the appeal circuit, the experts, and the family prosecution

- ✅ **Annexed Art. 1:** «**تنشأ بدائرة اختصاص كل محكمة جزئية للأسرة**، يكون تعيين مقرها بقرار من **وزير العدل**. وتنشأ فى دائرة
  اختصاص كل محكمة من محاكم الاستئناف **دوائر استئنافية متخصصة**، لنظر طعون الاستئناف التى ترفع إليها … وفى الأحوال التى يجيزها
  القانون عن الأحكام والقرارات الصادرة من محاكم الأسرة. وتنعقد هذه الدوائر الاستئنافية فى دوائر اختصاص المحاكم الابتدائية.»
  Both the family courts and the appeal circuits may sit **anywhere in or outside their district** if necessary, on the Justice
  Minister's decision at the request of the president of the first-instance or appeal court. ⭐ **This is why the family court is not
  necessarily in the courthouse the client knows** — check the seating decision.
- ✅ **Annexed Art. 3(1):** «**تختص محاكم الأسرة دون غيرها** بنظر **جميع مسائل الأحوال الشخصية** التى ينعقد الاختصاص بها للمحاكم
  الجزئية والابتدائية طبقاً لأحكام قانون تنظيم بعض أوضاع وإجراءات التقاضي فى مسائل الأحوال الشخصية الصادر بالقانون رقم 1 لسنة
  2000.» ⭐ **Read the consequence:** the Family Court **absorbed both the District and the First-Instance personal-status dockets** —
  the distinction between §§9(أولاً) and 10 of Law 1/2000 now decides **which formation** of the family court sits, not which
  courthouse.
- ✅ **Annexed Art. 2:** the family court is composed of **three judges, one at least a president at the First-Instance Court level**;
  the court is assisted in the Art. 11 cases by **two experts — one social, one psychological, at least one of them a woman**; the
  appeal circuit is **three counsellors, one at least a president**, and may use experts; the experts come from **lists issued by a
  Justice-Minister decision in agreement with the Social-Affairs or Health Minister**.
- ✅ **Annexed Art. 11 — the compulsory-expert claims (read verbatim):** «يكون **حضور الخبيرين** المنصوص عليهما فى المادة (2) من هذا
  القانون جلسات محكمة الأسرة **وجوبيا** فى دعاوى **الطلاق والتطليق والتفريق الجسمانى والفسخ وبطلان الزواج وحضانة الصغير ومسكن
  حضانته وحفظه ورؤيته وضمه والانتقال به وكذلك فى دعاوى النسب والطاعة**. وللمحكمة أن تستعين بهما فى غير ذلك من مسائل الأحوال
  الشخصية إذا رأت ضرورة لذلك. وعلى كل منهما أن يقدم للمحكمة تقريرا فى مجال تخصصه.» **And the Law 215/2017 addition (third
  paragraph):** «فإذا تعلقت الدعوى بإثبات النسب، وجب على الإخصائى الاجتماعى أن يُضمن تقريره ما إذا كان الصغير خاضعاً لنظام
  **الأسر البديلة** التابع لوزارة التضامن الاجتماعى أم غير خاضع.» ⭐ So the expert reports are **not optional decoration** in a
  divorce, custody, visitation or paternity case — the statute requires the attendance.
- ✅ **Annexed Art. 10:** family-court and appeal-circuit sessions are held **in places separate from the other courts' sessions**, and
  the court is equipped for the nature of the disputes and their parties, **including the attendance of minors to hear their
  statements**; and «**وتسترشد المحكمة فى أحكامها وقراراتها بما تقتضيه مصالح الطفل الفضلى**» — the **best interests of the child**
  guide the court.
- ✅ **Annexed Art. 4 — the specialised prosecution:** a **نيابة متخصصة لشئون الأسرة** performs the Public Prosecution's functions
  before the family courts and appeal circuits; its intervention in those cases and appeals is **mandatory** — «**ويكون تدخلها فى تلك
  الدعاوى والطعون وجوبياً وإلا كان الحكم باطلاً**»; it must **file a written opinion (مذكرة بالرأي) in every case or appeal** and
  whenever the court asks; and it **supervises the family courts' registries** on entry of claims and appeals and completion of
  documents, per **CPC Art. 65**. ⭐ **A judgment in which the family prosecution did not intervene is void** — that is the text.
- ✅ **Annexed Art. 13 — the procedure stack:** the rules of Law 10/2004 and of Law 1/2000 apply, and anything not specially provided
  for in either is governed by **the CPC, the Law of Evidence in civil and commercial matters, and the Civil Code on the administration
  and liquidation of estates** (that last part for estate matters — §7.2).
- ✅ **Promulgating Art. 5 (Law 1/2000) — the Ma'zoun/notary layer's parent article:** «يصدر وزير العدل القرارات اللازمة لتنفيذ أحكام
  القانون المرافق. **كما يصدر لوائح تنظيم شئون المأذونين والموثقين وأعمالهم ونماذج الوثائق اللازمة لأداء هذه الأعمال**.» ⭐ Cite
  **this** when you describe the Ma'zoun Regulations (§2.2) — the regulations are the Minister's, made under this article.

## 8.2 ⭐ The settlement office (مكتب تسوية المنازعات الأسرية) must come first — and it is free

- ✅ **Annexed Art. 5:** in the district of **every District (جزئية) court** one or more **family-dispute settlement offices** are
  created, **attached to the Ministry of Justice**, with enough **legal, social and psychological specialists** chosen by a
  Justice-Minister decision after consulting the relevant ministers; each office is headed by an **experienced person** (lawyer or
  other family specialist) entered on **a special register** kept at the Ministry of Justice.
- ✅ **Annexed Art. 6 — who must go and who is excused:** «**فى غير** دعاوى الأحوال الشخصية **التى لا يجوز فيها الصلح**، و**الدعاوى
  المستعجلة**، و**منازعات التنفيذ**، و**الأوامر الوقتية**، يجب على من يرغب فى إقامة دعوى بشأن إحدى مسائل الأحوال الشخصية التى تختص
  بها محاكم الأسرة، أن يق**د**م [كذا فى النسخة: «يقد»] **طلباً لتسوية النزاع إلى مكتب تسوية المنازعات الأسرية المختص**.» The office's
  panel **meets the parties, hears them, explains the case's aspects, consequences and the cost of persisting**, and gives advice and
  guidance **to try to settle it amicably to preserve the family**.
- ✅ **Annexed Art. 7:** «**ويكون اللجوء إلى تلك المكاتب بدون رسوم**» — **free of charge**. (The Justice Minister fixes the offices'
  composition, seats, how requests are lodged and recorded, notices, sessions and the settlement procedure.)
- ✅ **Annexed Art. 8 — the clock and the output:**
  - «**يجب أن تنتهي التسوية خلال خمسة عشر يوما** من تاريخ تقديم الطلب، ولا يجوز تجاوز هذه المدة **إلا باتفاق الخصوم**.»
  - If **settled**: the office head records it in **minutes signed by the parties**, attached to the session minutes, «**وتكون له قوة
    السندات واجبة التنفيذ**» — **it has the force of an executory instrument**, and the dispute ends within the settled scope. ⭐ That
    is a **free, fast enforcement title** — a point almost every guide misses.
  - If **not settled**: minutes of what was achieved, signed by the parties or their representatives, with the **experts' reports** and
    the **office head's report** attached, sent to the competent family court's registry with the claim, **within seven days**, for the
    judicial stage to proceed on what was not agreed.
- ✅ **Annexed Art. 9 — the sanction for skipping it:** a claim brought directly to the family courts in a settlable matter **without
  the settlement request** is «**لا تقبل**» (not accepted) — **but** the court **may instead of ruling it inadmissible refer the claim
  to the competent office** to carry out the settlement task. ⭐ In practice, then, the omission costs time, and the court has the
  power to cure it.
- ✅ **Transferred cases:** **promulgating Art. 2(1)** transfers pending personal-status claims to the family courts **free of fees**
  («**بدون رسوم**») and in their existing state, with the registry notifying an absent party of the transfer order; ✅ and
  **promulgating Art. 2(2)** expressly says family courts hear those transferred claims «**دون عرضها على مكاتب تسوية المنازعات
  الأسرية**»; ✅ **promulgating Art. 2(3)** keeps cases already judged or reserved for judgment under the appeal rules in force before
  the law.
- ✅ **Urgent matters are not stuck behind the office.** The **الأوامر الوقتية** carve-out in Art. 6 is the **judge of urgent matters'
  order-on-petition** route defined in **Law 1/2000 promulgating Art. 1**, which lists five matters, including — the one that matters
  most in practice — «**التظلم من امتناع الموثق عن توثيق عقد الزواج أو عدم إعطاء شهادة مثبتة للامتناع** سواء للمصريين أو الأجانب»
  and «**المنازعات حول السفر إلى الخارج** بعد سماع أقوال ذوى الشأن». ✅ And **Law 10/2004 annexed Art. 3(4)** gives that power to the
  **president of the family court**, as judge of urgent matters, for the matters in that article. ⭐ **So if a Ma'zoun or notary
  refuses to document a marriage, the statutory remedy is an order on petition — not a lawsuit, and not a wait for the settlement
  office.** (This is the practical answer to the wali-refusal problem described in §5.6.)
- ⚠️ **What I could not verify:** whether a **settlement request is required** in a divorce between **non-Muslim spouses of one
  sect** where the community's own law governs — the exception is drafted as «الدعاوى التى لا يجوز فيها الصلح», and I found no decision
  applying it to the milliya/community rules. **Ask the office.** See §12.

## 8.3 ⭐ Fees and legal aid — what is exempt, what is only discretionary, and what I could not price

| Item | Instrument | Verified position |
|---|---|---|
| **No lawyer needed on the claim sheet** (District-court personal-status claims) | ✅ **Law 1/2000 Art. 3(1)** | «**لا يلزم توقيع محام على صحف دعاوى الأحوال الشخصية أمام المحكمة الجزئية**، فإذا رفعت الدعوى بغير توقيع محام على صحيفتها **كان للمحكمة عند الضرورة أن تندب محاميا للدفاع عن المدعى**. ويحدد الحكم الصادر فى الدعوى **أتعابا للمحامى المنتدب، تتحملها الخزانة العامة**، وذلك دون إخلال بالتزام مجالس النقابات الفرعية بتقديم **المساعدات القضائية** على النحو المنصوص عليه فى **القانون رقم 17 لسنة 1983** بشأن إصدار قانون المحاماة.» |
| **Maintenance claims are entirely fee-exempt** | ✅ **Law 1/2000 Art. 3(2)** | «**وتعفى دعاوى النفقات وما فى حكمها من الأجور والمصروفات بجميع أنواعها من كافة الرسوم القضائية فى كل مراحل التقاضى.**» |
| **That exemption runs before the family courts too — expressly including imprisonment claims** | ✅ **Law 10/2004 annexed Art. 3(2)** | «ويسرى أمام محاكم الأسرة فى شأن **صحف الدعاوى** التى كانت تختص بها المحاكم الجزئية، وفى شأن **إعفاء دعاوى النفقات وما فى حكمها، شاملة دعاوى الحبس لامتناع المحكوم عليه عن تنفيذ الأحكام الصادرة بها** أحكام المادة (3) من القانون ذاته.» |
| **The settlement office is free** | ✅ **Law 10/2004 annexed Art. 7** | «ويكون اللجوء إلى تلك المكاتب **بدون رسوم**.» |
| **Transferred claims enter free** | ✅ **Law 1/2000 promulgating Art. 2(1)** / **Law 10/2004 promulgating Art. 2(1)** | transfer «**بدون رسوم**» |
| **The court may throw the fees on the State** | ✅ **Law 1/2000 Art. 51** (الولاية على المال) | «للمحكمة أن تأمر بإضافة **كل الرسوم أو بعضها أو المصاريف على عاتق الخزانة العامة**.» |

- ⚠️ **What is NOT covered by those words, read strictly:** the exemption is drafted for «**دعاوى النفقات وما فى حكمها من الأجور
  والمصروفات**». **مهر، جهاز، دوطة، شبكة، مقابل الخلع، الميراث والتركات، ودعاوى الملكية** are **outside the express words**, and
  **Law 1/2000 Art. 9(أولاً)(4)** itself treats the مهر/جهاز claims as ordinary money claims with a **finality threshold** tied to the
  District judge's pecuniary limit. ✅ **See the corrections table row 19 and §10.4** — do not tell a client "family cases are free".
- 🟡 **The price of the non-exempt claims I could NOT establish.** What I searched: the consolidated texts of Laws 1/2000 and 10/2004
  (neither sets a fee scale — Art. 3 only exempts), the Justice Ministry's published decision lists, and the Egyptian-law portals. I
  did **not** retrieve the **general judicial-fees legislation** or the current ministry/ Supreme Judicial Council fee decisions in this
  pass, so **I state no figure**. **Ask the family court's registry (قلم الكتاب) for a written estimate (تقدير الرسوم)** — and note
  that the registry is supervised by the family prosecution (Annexed Art. 4, above).
- 🟡 **The experts' fees** (أتعاب الخبيرين) under **Law 10/2004 annexed Art. 11** — the article orders attendance and reports but
  **says nothing about who pays**; the duty to pay in practice (a deposit into court, charged to the losing party, or borne by the
  Treasury) is not in the text I read. **Unverified — §12.**

## 8.4 Where to file — the two jurisdiction questions, and the one-file rule

- **Type jurisdiction (which formation):** ✅ **Law 1/2000 Art. 9(أولاً)** lists the **District** matters — custody, حفظ، رؤية، ضم،
  الانتقال; نفقة and what is in its like (الأجور والمصروفات بجميع أنواعها); إذن الزوجة بمباشرة حقوقها; **مهر، جهاز، دوطة، شبكة**;
  correction of personal-status entries in marriage and divorce documents; documenting what the parties agree on before the court;
  **الإذن بزواج من لا ولى له**; and **تحقيق الوفاة والوراثة والوصية الواجبة** where no dispute arises. ✅ **Art. 10** gives the
  **First-Instance Court** the rest of the personal-status claims plus waqf claims, and — the important part — **the divorce court
  rules alone on maintenance, custody, رؤية and housing** (§8.7).
- **Local jurisdiction (which court geographically):** ✅ **Art. 15(1)** — the defendant's domicile; **no domicile in Egypt → the
  claimant's**; several defendants → any of them. ⭐ **Then the claimant-friendly rule:** in claims by **الأولاد أو الزوجة أو الوالدين
  أو الحاضنة** for **نفقة/أجور, حضانة/رؤية, مهر/جهاز/دوطة/شبكة, and التطليق/الخلع/الإبراء/الفرقة بجميع أسبابها الشرعية**, competence lies with
  «**المحكمة التى يقع فى دائرتها موطن المدعى أو المدعى عليه**» — **her choice**, not his. ✅ **Art. 15(2)**: estate verification and
  liquidation → the deceased's **last domicile in Egypt**, else where an estate asset is. ✅ **Art. 15(3)**: property guardianship →
  the wali's/minor's domicile (وصاية: the last domicile of the deceased or the minor); interdiction → the domicile of the person to be
  interdicted; غيبة → the absentee's last domicile.
- ✅ **Law 10/2004 annexed Art. 12 — the one-court, one-file rule:** «**تكون محكمة الأسرة المختصة محليا بنظر أول دعوى ترفع إليها من
  أحد الزوجين مختصة محليا، دون غيرها، بنظر جميع الدعاوى التى ترفع بعد ذلك من أيهما، أو تكون متعلقة أو مترتبة على الزواج أو الطلاق
  أو التطليق أو التفريق الجسمانى أو الفسخ**، وكذلك **دعاوى النفقات أو الأجور وما فى حكمها سواء للزوجة أو الأولاد أو الأقارب، ودعاوى
  الحبس لامتناع المحكوم عليه عن تنفيذ الأحكام الصادرة بها، وحضانة الصغير وحفظه ورؤيته وضمه والانتقال به ومسكن حضانته، وجميع دعاوى
  الأحوال الشخصية** — وذلك كله مع سريان أحكام **الفقرتين الرابعة والخامسة من المادة (10)**» of Law 1/2000. And a **family file
  (ملف للأسرة)** is opened at the registry when the first claim is filed, into which **all** the family's later papers are deposited.
  ⭐ **Practical:** after the first claim the whole family's litigation is centralised; a later claim filed in another court is
  exposed to a transfer order.

## 8.5 How the case runs — filing, the gates, the two reconciliations, the arbitrators

1. **Filing.** ✅ **Art. 16:** «**ترفع الدعوى فى مسائل الولاية على النفس بالطريق المعتاد لرفع الدعوى** المنصوص عليه فى قانون
   المرافعات المدنية والتجارية» — i.e. the ordinary writ; and the Art. 3 pleading rules of §8.3 apply.
2. **Admissibility gates — read them before promising anything.**
   - ✅ **Art. 17(1):** «**لا تقبل الدعاوى الناشئة عن عقد الزواج إذا كانت سن الزوجة تقل عن ست عشرة سنة ميلادية، أو كانت سن الزوج
     أقل عن ثمانى عشرة سنة ميلادية وقت رفع الدعوى**» — a claim arising out of the marriage is **not accepted** where the **wife is
     under 16 or the husband under 18 when the claim is filed**. ⚠️ **Do not confuse this with the documentation age (18/18) of
     Art. 31 bis of Law 143/1994 (§2.2)** — they are two different rules in two different laws, and only one of them is a criminal-
     adjacent sanction. **Never merge them into "the marriage age is 16/18".**
   - ✅ **Art. 17(2):** claims arising out of the marriage contract, **in facts after 1 August 1931**, are «**لا تقبل عند الإنكار**
     … ما لم يكن الزواج **ثابتاً بوثيقة رسمية**» — and **however**, «**تقبل دعوى التطليق أو الفسخ** بحسب الأحوال **دون غيرهما** إذا
     كان الزواج ثابتاً **بأية كتابة**». ⭐ This is the article that makes an **عرفي** marriage provable **for divorce purposes only**
     (§2.4, §3.4).
   - ✅ **Art. 17(3):** «**ولا تقبل دعوى الطلاق بين الزوجين متحدى الطائفة والملة إلا إذا كانت شريعتهما تجيزه**» — the confessional
     gate (§1.3).
3. **The court must offer صلح — twice where there is a child.** ✅ **Art. 18:** in الولاية على النفس claims «**تلتزم المحكمة … بعرض
   الصلح على الخصوم**، ويعد من تخلف عن حضور جلسة الصلح — مع علمه بها — بغير عذر مقبول **رافضاً له**»; and **in طلاق/تطليق** the court
   «**لا يحكم بهما إلا بعد أن تبذل المحكمة جهدا فى محاولة الصلح بين الزوجين وتعجز عن ذلك**، فإن كان للزوجين **ولد** تلتزم المحكمة
   بعرض الصلح **مرتين على الأقل** تفصل بينهما مدة **لا تقل عن ثلاثين يوما ولا تزيد على ستين يوما**.» ⭐ **This is the statutory
   reason a divorce with children cannot finish quickly**; the pre-suit settlement office (§8.2) is a *separate*, earlier step.
4. **The arbitrators (الحكمان).** ✅ **Art. 19:** in **تطليق** claims requiring arbitrators, the court must ask **each spouse to name
   an arbitrator from their own family** (as far as possible) **by the next session at the latest**; if either fails to name one or
   fails to attend that session, **the court names one for him**; the arbitrators must appear at the session after their appointment
   **to state what they concluded together**, and if they disagree or one is absent, the court hears them **or the attending one under
   oath**; and «**وللمحكمة أن تأخذ بما انتهى إليه الحكمان أو بأقوال أيهما، أو بغير ذلك مما تستقيه من أوراق الدعوى**» — the court is
   **not bound** by their conclusion. ✅ Art. 20 adds that in **خلع** the same arbitration is used **to pursue reconciliation**, within
   **a period not exceeding three months** (§3.2).
5. **Evidence.** ✅ **Art. 4** lets the court, when preparing the case for judgment, give directions and deadlines for defence, and
   **appoint one or more social experts** from the Justice-Minister lists to report on the case or an issue in it, with a report
   deadline **not exceeding two weeks**; ✅ plus the **compulsory experts** of Law 10/2004 annexed Art. 11 (§8.1); ✅ **Art. 23** — the
   **Public Prosecution's income investigation** where income is seriously disputed, with its 30-day deadline (§4.2).
6. **Publicity and the PP.** ✅ **Art. 5:** the court may hear personal-status matters **in the consultation chamber (غرفة المشورة)**
   for reasons of public order or morals, with a Public Prosecution member present where it is a party, and **pronounces its judgments
   and decisions in open session**. ✅ **Art. 6:** the PP may **bring** a personal-status claim in matters of public order or morals,
   **may intervene** in District-court claims, and **must intervene** in personal-status and waqf claims before the First-Instance or
   Appeal courts — «**وإلا كان الحكم باطلا**». ✅ Plus the mandatory family-prosecution intervention (Law 10/2004 annexed Art. 4).
7. **Where death/inheritance certificates come from.** ✅ **Law 10/2004 annexed Art. 3(3):** «**واستثناء من أحكام الفقرة الأولى يختص
   رئيس محكمة الأسرة بإصدار شهادات الوفاة والوراثة، ويجوز له أن يحيلها إلى المحكمة عند قيام نزاع جدى فى شأنها**» — the family court's
   **president**, not the claim docket; and the referral-on-serious-dispute route matches **Law 1/2000 Arts. 24–25** (§7.6).

## 8.6 Appeal, cassation — and the conflict between the two laws

- ✅ **Law 1/2000 Art. 56:** «**طرق الطعن** فى الأحكام والقرارات المبينة فى هذا القانون هى **الاستئناف والنقض والتماس إعادة
  النظر**. وتتبع — فيما لم يرد به حكم خاص فى المواد الآتية — القواعد والإجراءات المنصوص عليها فى قانون المرافعات المدنية
  والتجارية.»
- ✅ **Art. 57:** the **Public Prosecution** may always appeal in the cases where its intervention is obligatory or permitted.
- ✅ **Art. 59 — the appellate court's interim power:** an appeal against an Art. 10 judgment **stages the whole matter it decided**,
  and until the appellate judgment issues the court «**يجوز لها إصدار حكم مؤقت واجب النفاذ بشأن الرؤية أو بتقرير نفقة أو تعديل
  النفقة** التى قضى بها الحكم المطعون فيه **بالزيادة أو بالنقصان**».
- ✅ **Art. 61:** the appeal period is **60 days for a person with no domicile in Egypt**, «**دون إضافة ميعاد مسافة**». ⚠️ **This is
  the only appeal-period figure in the article** — the ordinary domestic appeal period is in the CPC, which I did not read in this
  pass; **do not state a number for it, or you will state the wrong one.**
- ✅ **Art. 62 — the cassation article relied on by family lawyers:** «**للخصوم وللنيابة العامة الطعن بالنقض فى الأحكام الصادرة من
  محاكم الاستئناف**، كما يكون لهم الطعن بالنقض فى **القرارات** الصادرة من هذه المحاكم فى مواد **الحجر والغيبة والمساعدة القضائية
  وعزل الوصى وسلب الولاية أو وقفها أو الحد منها أو ردها واستمرار الولاية أو الوصاية والحساب**.»
- ✅ **Law 10/2004 annexed Art. 14 — the article that cuts it off:** «**مع عدم الإخلال بأحكام المادة (250) من قانون المرافعات
  المدنية والتجارية، تكون الأحكام والقرارات الصادرة من الدوائر الاستئنافية غير قابلة للطعن فيها بطريق النقض.**»
- ⚠️ **The conflict, stated plainly:** **Art. 62 of Law 1/2000** (February 2000) opens cassation in appeal-court judgments; **Art. 14
  of Law 10/2004** (in force 1 Oct 2004) closes it for the **specialised family appeal circuits**. The later, specific rule governs,
  **subject to whatever CPC Art. 250 preserves** — and CPC Art. 250 itself was **not read in this pass**, so I do not describe what it
  preserves. **Working instruction for an agent: tell the client the appeal judgment is probably final, and have a lawyer check
  Art. 250 and the current Cassation practice before filing.** Recorded again in §12.
- ✅ **Art. 63** — enforcement of a divorce/annulment/tatliq judgment waits for the cassation periods to lapse (§3.6); ✅ **Art. 64**
  limits **التماس إعادة النظر** in property-guardianship matters to final decisions in six listed matters; ✅ **Art. 53** requires
  reasons to be filed within **8 days** (District) or **15 days** (other courts) for conclusive decisions in listed property matters.
- ⭐ **The practical asymmetry, once more:** interim orders are **not** appealable until the final judgment (**Art. 10(5)**), while
  maintenance/رؤية/child-delivery orders are enforceable **by force of law and without security** (**Art. 65**, §9.2). **The money
  moves while the appeal is pending; the appeal rarely moves the money.**

## 8.7 ⭐ One court, one file, one judgment — the linked-claims rule (Art. 10)

- ✅ **Art. 10(2):** «**ويكون للمحكمة الابتدائية المختصة محليا بنظر دعوى الطلاق أو التطليق أو التفريق الجسمانى دون غيرها، الحكم
  ابتدائيا فى دعاوى النفقات أو الأجور وما فى حكمها سواء للزوجة أو الأولاد أو الأقارب، وحضانة الصغير وحفظه ورؤيته وضمه والانتقال به
  ومسكن حضانته.**»
- ✅ **Art. 10(3):** the First-Instance and District courts before which any of those claims is or will be brought «**تلتزم … بإحالتها
  إلى تلك المحكمة حتى يصدر فيها حكم قطعى واحد**» — **referred, so that one final judgment issues.**
- ✅ **Art. 10(4):** during the case the court may issue **interim enforceable orders** on رؤية or **نفقة وقتية** (increase or
  decrease); ✅ **Art. 10(5):** those interim orders **may not be appealed except once the final judgment issues**.
- ✅ **Law 10/2004 annexed Art. 12** adds the **family file** and mirrors the centralisation (§8.4).
- ⭐ **What to tell a client, in one line:** if there is a divorce case, **bring the maintenance, custody, visitation and housing
  claims inside it** — filed separately they will be referred, costing months; and if the divorce case is in **her** chosen court under
  Art. 15(1), the linked claims follow it there.

---

# 9. Enforcement (التنفيذ) — getting the money and getting the child

**Citation:** **Law 1/2000** Arts. **65–79** and **Art. 76 bis** (added by **Law 91/2000**); **Law 10/2004** annexed **Art. 15**;
**Law 25/1929** Art. **20(2)**; **Law 25/1920** Art. 1 (the debt and its non-extinction); **Penal Code Art. 293** (as replaced by
**Law 6/2020**); **Law 11/2004** Arts. 2–3 (as replaced by **Law 113/2015**).
**Status:** all in force. ⚠️ **The Fund's operating cap, and the current fine under Penal Code Art. 293, are the two figures to carry
carefully — §4.5–§4.6.**
**Sources:** ✅ **Arts. 65–79 of Law 1/2000 read verbatim** from the consolidated text (`mksegypt.org/ar/laws/24131`) — **this
supersedes the secondary quotation of Arts. 65–69 used earlier in §5.4 of this file** · ✅ **Art. 76 bis** from the **Gazette scan** of
Law 91/2000 (`moj.gov.eg:73/Doc/001/13228912000.pdf`, read as page images) · ✅ **Law 10/2004 annexed Art. 15**, `lawhub.info/eg/?p=11675` ·
✅ **Law 25/1929 Art. 20(2)**, `lawhub.info/eg/?p=11576` · ✅ **Penal Code Art. 293** as amended · ✅ **Law 113/2015** Gazette scan
(Arts. 2–3 of Law 11/2004 as replaced).
**As of:** 2026-10-19.

## 9.1 The four routes to the money — and where each one's authority comes from

| # | Route | Instrument | What it needs | What stops it |
|---|---|---|---|---|
| 1 | **The Family Insurance Fund pays** | ✅ Law 1/2000 **Arts. 71–72** + **Law 11/2004** Art. 3 (Law 113/2015) | an **enforceable maintenance judgment** for the wife, divorcée, children, parents; the bank pays «وفقاً للقواعد والإجراءات التى يصدر بها قرار من وزير العدل» | the bank's own operating cap and rules — **EGP 500/month per beneficiary, no arrears** (§4.6) |
| 2 | **Automatic deduction from salary/pension** | ✅ **Art. 73** | a request from **بنك ناصر الاجتماعى** + a true copy of the executory judgment + proof of completed service; the employer/body then deducts **within the Art. 76 ceilings** and deposits into the bank's treasury «**فور وصول الطلب إليها ودون حاجة إلى إجراء آخر**» | the Art. 76 ceilings (25%/35%/40%/50%); the debtor's lack of a salary — then **Art. 74**: he must deposit in the first week of each month after the bank's notice |
| 3 | **Coercive imprisonment for debt** | ✅ **Art. 76 bis** (Law 91/2000) | an enforceable maintenance judgment + **proof the debtor is able to pay** + a court order to pay + non-compliance → **up to 30 days**; release on paying **or producing a guarantor acceptable to the entitled person** | ability must be proved; the judgment is **final**; ⭐ **and this route is the precondition of route 4** |
| 4 | **The criminal complaint** | ✅ **Penal Code Art. 293** (Law 6/2020) | an enforceable judgment + **ability** + **3 months** of default after notification + a **complaint** | payment or an acceptable guarantor at any time; **صلح** at any stage; and the Art. 76 bis precondition |

- ⭐ **The order matters.** Do the free/mechanical things first (§9.1 rows 1–2), then go to the court for the 30-day order with
  evidence of ability, and only then — because Art. 76 bis is its precondition — to the criminal complaint. **A criminal complaint
  filed first can be defeated by the very article that creates the remedy.**
- ✅ **Art. 75:** the bank recovers from the debtor **what it paid out and its actual expenses** — so the Fund route does not forgive
  the debt; it advances it. ✅ **Art. 77 priority:** wife/divorcée → children → parents → relatives → other debts (§4.5.2).
- ⚠️ **The counter-offence, and it is a real risk in family disputes:** ✅ **Art. 79** — «**يعاقب بالحبس الذى لا تقل مدته عن ستة أشهر**
  كل من توصل إلى الحصول على أية مبالغ من بنك ناصر الاجتماعى نفاذاً لحكم أو لأمر صدر استناداً إلى أحكام هذا القانون **بناء على إجراءات
  أو أدلة صورية أو مصطنعة مع علمه بذلك**»، and **up to two years** for obtaining amounts not due to him from the bank knowing it.
  ⭐ **The Fund is a soft target for fraud, and the statute treats it that way.**
- ⚠️ **Two figures collapse in one sentence if you are careless:** the **EGP 5,000** ceiling is the **fine under Penal Code Art. 293
  as amended in 2020**; the **EGP 500** figure that circulates as "the fine" is the **pre-2020 Penal Code text** (§4.5.4, §12), while
  **EGP 500 per month** is the **Fund's operating payment cap** (§4.6). **Do not mix them.** See also the fines in §10.5.

## 9.2 What is enforceable immediately — and who executes it

- ✅ **Art. 65, verbatim:** «**الأحكام والقرارات الصادرة بتسليم الصغير أو رؤيته أو بالنفقات أو الأجور أو المصروفات وما فى حكمها
  تكون واجبة النفاذ بقوة القانون وبلا كفالة.**» ⭐ **Read the four words that matter: "بقوة القانون" (by force of law) and "بلا
  كفالة" (without security).** No appeal suspends these, and the debtor cannot demand a deposit to stop them.
- ✅ **Art. 68:** «**على قلم كتاب المحكمة التى أصدرت الحكم أو القرار وضع الصيغة التنفيذية عليه إذا كان واجب النفاذ**» — the executory
  formula is the registry's duty **if** the order is enforceable; it is the document the bank, the employer and the bailiff act on.
- ✅ **Law 10/2004 annexed Art. 15:** «**تنشأ بكل محكمة أسرة إدارة خاصة لتنفيذ الأحكام والقرارات الصادرة منها أو من دوائرها
  الاستئنافية**، تزود بعدد كاف من **محضرى التنفيذ المؤهلين المدربين** الذين يصدر بتحديدهم قرار من رئيس المحكمة. **ويتولى الإشراف
  على هذه الإدارة قاض للتنفيذ** تختاره الجمعية العمومية للمحكمة الابتدائية من بين قضاة محكمة الأسرة فى دائرة تلك المحكمة.» ⭐ **There
  is a dedicated execution judge and a dedicated execution department for family judgments** — ask for them by name at the counter;
  a client who files an execution request at the general bailiff's office is in the wrong line.
- ✅ **Art. 69:** execution is carried out «**بمعرفة المحضرين أو جهة الإدارة**», and the Justice Minister issues a decision on the
  procedures for executing **تسليم، ضم، رؤية وسكنى** judgments and on who is responsible. ⚠️ **That ministerial decision is the
  operating document and I did not retrieve it** — if a client's problem is *how* the enforcement officer acts, this is the text to get
  from the court. See §12.
- ✅ **Art. 63 — the counterpoint:** divorce, annulment and tatliq judgments are **not executed until the cassation periods lapse**
  (§3.6). ⭐ So there is a lawful window in which a man is **divorced on paper but the court will not yet enforce the dissolution** —
  while the **maintenance and رؤية orders run anyway** under Art. 65.

## 9.3 Executing custody, ضم and رؤية — and the one line that blocks force

- ✅ **Art. 66, verbatim:** «**يجوز تنفيذ الأحكام والقرارات الصادرة بضم الصغير وحفظه وتسليمه جبرًا.** ويتبع فى تنفيذ الأحكام
  الصادرة فى هذا الشأن ما ينص عليه القانون من إجراءات. **ويراعى فى جميع الأحوال أن تتم إجراءات التنفيذ ودخول المنازل وفق ما يأمر
  به قاضى التنفيذ.** **ويجوز إعادة التنفيذ بذات السند التنفيذى كلما اقتضى الحال ذلك.**»
  - **ضم/حفظ/تسليم may be executed by force** — ✅ in terms;
  - **entry into homes is subject to the execution judge's order** — the statute's only guardrail on how a child is taken;
  - ⭐ **and the same instrument may be used again as often as needed** — the answer to "he handed her over once then took the child
    back".
- ⭐ **But رؤية is the exception, and it is explicit.** ✅ **Law 25/1929 Art. 20(2):** «**ولا ينفذ حكم الرؤية قهراً**، ولكن إذا امتنع
  من بيده الصغير عن تنفيذ الحكم **بغير عذر** أنذره القاضي، فإن تكرر منه ذلك **جاز للقاضي بحكم واجب النفاذ نقل الحضانة مؤقتا إلى من
  يليه من أصحاب الحق فيها** لمدة يقدرها.» ⭐ **So the operational truth is: the child can be *delivered* by force, but a *visit*
  can never be; the sanction for refusing visits is losing custody temporarily.** Do not promise a parent police-assisted visitation,
  and do not let a custodian believe refusal is risk-free.
- ✅ **Art. 67 — where a visit happens:** «**ينفذ الحكم الصادر برؤية الصغير فى أحد الأماكن التى يصدر بتحديدها قرار من وزير العدل بعد
  موافقة وزير الشئون الاجتماعية، وذلك ما لم يتفق الحاضن والصادر لصالحه الحكم على مكان آخر.** ويشترط فى جميع الأحوال أن يتوفر فى
  المكان **ما يشيع الطمأنينة فى نفس الصغير**.» ⭐ **The parties' agreement on a place is a statutory alternative to the designated
  venues**, and it is far cheaper than enforcement.
- ⭐ **The fastest child-return route in the statute — and the least known:** ✅ **Art. 70.** Where a dispute is presented to the
  **Public Prosecution** about the custody of a child **of custodial age (سن حضانة النساء)**, or where **provisional custody** is
  requested for the party likely to be awarded it, the PP may — **after the appropriate investigation** — issue a **reasoned
  decision** handing the child to the person whose interest is realised with him. The decision issues from a **prosecution chief
  (رئيس نيابة) at least**, and is «**واجب التنفيذ فوراً إلى حين صدور حكم من المحكمة المختصة فى موضوع حضانة الصغير**». ⭐ **In a sudden
  removal of a child, this is the route to ask about**, not a custody suit's first hearing.
- ⚠️ **Practice layer (mark it as such):** the picture of police and judicial officers recovering children circulates from the Bar
  Association's own explainer of Arts. 65–69 (`egyls.com`, 22 Oct 2020) and from news reporting. **The statute says what Art. 66 says,
  and leaves the procedure to a Justice-Minister decision I did not retrieve.** Do not describe an enforcement scene to a client as
  if it were in the law.

## 9.4 What a debtor can do to slow it down — and what the text will not give him

- ✅ **Art. 78:** «**لا يترتب على الإشكال فى تنفيذ أحكام النفقة** المشار إليها فى المادة السابقة **وقف إجراءات التنفيذ**» — an
  **objection to execution does not suspend** the enforcement of a maintenance judgment. Combined with **Art. 65** (no security) and
  **Art. 10(5)** (interim orders unappealable until final judgment), the debtor's procedural brakes are **deliberately weak** in this
  field — that is the legislative design, and it is the single most useful thing to tell a client who has been told "he will appeal and
  you will wait".
- ✅ **The defences the text does give him:** **payment or release** (Law 25/1920 Art. 1: «**ولا تقسط إلا بالأداء أو الإبراء**»);
  an **acceptable guarantor** (Art. 76 bis and Penal Code Art. 293: performance defeats the penalty); **inability**, which defeats both
  the coercive and the criminal routes because both require ability; and **صلح** under Art. 293 as amended in 2020.
- ⚠️ **What is NOT in the articles I read, and must not be asserted:** I found **no** provision suspending a father's maintenance
  obligation **because the custodian refuses visitation** — the statute's answer to refused visitation is **Art. 20(2)'s transfer of
  custody**, not a maintenance strike. Nor is there a **statutory percentage** of income for maintenance (assessment is judicial —
  §4.2). **When a client says "the lawyer told me I can stop paying if she stops the visits", the verified answer is that the statute
  does not say that; the remedy is the custody-transfer route.**
- ✅ **And the one that protects the *other* side:** **Art. 76 bis' release on payment or guarantor**, **Art. 293's pay-or-settle
  defence**, and **the صلح that extinguishes the criminal action** — including the 2020 requirement of the **Bank's certificate**
  where the creditor has already collected from the Fund (§4.5.4).

---
# 10. Fees and money at the counter — what is verified, what is not, and why

## 10.1 Read this before you quote a number

**In personal-status work the verified fee facts are exemptions, not prices.** Three things are ✅ established in this pass: the
**maintenance family is exempt from all judicial fees at every stage**; the **settlement office is free**; and the **court may charge
fees and expenses to the public treasury** in property-guardianship matters. **Everything else — the price of a خلع claim, the experts'
fees, the Ma'zoun's charge, the notary's charge — I could not price from a primary text**, and §10.4 says so item by item. **A model
that produces a fee figure for family litigation in Egypt is guessing** unless it cites one of the two tables below.

## 10.2 The charges that ARE verified — the Family Insurance Fund's levies

✅ **Law 11/2004** created «**صندوق نظام تأمين الأسرة**» — a **non-profit fund with public legal personality**, seat in **Cairo**,
**managed by Nasser Social Bank** (Art. 1), and it is funded by the **charges on the events of marriage, divorce, birth and the
national ID**, collected under a Justice-Minister decision with the competent minister's agreement. ⭐ **These are the charges a
person actually pays at the counter** — and they are **receipts for the Fund, not court fees**.

| Event / document | **Original Law 11/2004** (Gazette No. 12 تابع (أ), **18 March 2004**) ✅ | **Law 113/2015** — Arts. 2–3 replaced (Gazette No. 48 (تابع), **11 November 2015**) ✅ — **the text in force** |
|---|---|---|
| **Marriage** | 50 EGP per marriage event, **paid by the husband** | **100 EGP** per marriage event, **paid by the husband**, **plus 4 EGP** per extract of the marriage document |
| **Divorce or revocation (مراجعة)** | 50 EGP per event, paid by the divorcer | **100 EGP** per event, paid by the divorcer/revoker, **plus 9 EGP** per extract of the divorce document |
| **Birth certificate** | 20 EGP per birth event, paid by the notifier once, on obtaining the certificate | **20 EGP on the first extract** of the birth certificate and **3 EGP on every later extract** |
| **National ID** | — | **5 EGP per issuance** of the national ID card |
| **Gazette references** | ⚠️ Issue number **garbled in the scan's OCR**; the date is **18 March 2004** | ⚠️ OCR reads the issue as **«العدد ٤٨ (تابع)»**, dated **11 November 2015** — **the numerals are the unreliable part of both scans** |
| **Who pays what for what** | ⚠️ The **old bands are still printed in old guides and at some counters**; the **2015 text governs**. | |

✅ **Comparison of the two gazette scans is the point of the table:** the figures **doubled in 2015** for marriage and divorce and the
**extract charges were introduced**, so **any pre-2015 table is wrong**. ⚠️ **Both rows were read from page images of the Official
Gazette (OCR of text in which the numbers are spelled out as Arabic words, not digits)** — the words «خمسين»، «مائة»، «عشرين»،
«أربعة»، «تسعة»، «ثلاثة»، «خمسة» were legible; the **digits were not**. **Verify with the Fund/bank before quoting to a client.**
✅ **Art. 3** (as replaced) confirms that the Fund pays maintenance under **Art. 72 of Law 1/2000** out of its resources; **amounts
deposited or recovered under Arts. 72, 74 and 75 of that law accrue to the Fund**; and **Nasser Bank may move the criminal action as
an interested party under Penal Code Art. 293** to recover what it paid.

## 10.3 The court-side charges that are verified — the exemptions (restated, because they are the answer to "how much?")

| Item | Instrument | Verified position |
|---|---|---|
| Maintenance and what is in its like (نفقة، أجر، مصروف) — **all judicial fees, every stage** | ✅ **Law 1/2000 Art. 3(2)** | «**وتعفى دعاوى النفقات وما فى حكمها من الأجور والمصروفات بجميع أنواعها من كافة الرسوم القضائية فى كل مراحل التقاضى.**» |
| The same exemption **before the family courts**, **including** the imprisonment-for-non-execution claims | ✅ **Law 10/2004 annexed Art. 3(2)** | quoted verbatim at **§8.3** |
| The **settlement office** (the mandatory pre-suit step) | ✅ **Law 10/2004 annexed Art. 7** | «**ويكون اللجوء إلى تلك المكاتب بدون رسوم.**» |
| Claims **transferred** into the family courts | ✅ **Law 10/2004 promulgating Art. 2(1)** / **Law 1/2000 promulgating Art. 2(1)** | «**بدون رسوم**» |
| A **lawyer** — not needed to sign the claim, and the Treasury pays one the court appoints | ✅ **Law 1/2000 Art. 3(1)** | quoted verbatim at **§8.3**; and the bar's **legal-aid duty under Law 17/1983** |
| Fees in **property-guardianship** matters | ✅ **Law 1/2000 Art. 51** | «للمحكمة أن تأمر بإضافة **كل الرسوم أو بعضها أو المصاريف على عاتق الخزانة العامة**» |
| Failure to file an accounting | ✅ **Law 1/2000 Art. 46** — a **fine**, not a fee | up to **500 EGP**, and up to **1,000 EGP** on repetition, remittable in whole or part |

## 10.4 🟡 The gaps — costs I could NOT verify, item by item

**What I searched, once, so the reader does not repeat it in the dark:** the consolidated texts of **Law 1/2000** (which only
*exempts*) and **Law 10/2004** (which only sets the free offices); the Justice Ministry's decision pages; the Egyptian legislation
portals (`lawhub.info/eg`, `mksegypt.org/ar/laws`, `manshurat.org`); and the fee-related ministerial decisions named elsewhere in this
file. **The general judicial-fees legislation, the current ministry fee schedules, and the Supreme Judicial Council / court-practice
notices were not retrieved in this pass.** Therefore:

| # | The cost | Status and what to do |
|---|---|---|
| 1 | The court fee (رسم) on a **خلع** claim | 🟡 **Not established.** The Art. 3 exemption covers maintenance and its like; خلع is a تطليق and is **not** in those words. **Ask the قلم الكتاب for a تقدير الرسوم in writing.** |
| 2 | The court fee on **مهر / جهاز / دوطة / شبكة** claims | 🟡 **Not established** — and note Art. 9(أولاً)(4) ties these to the District judge's pecuniary limit, which is itself unstated in Law 1/2000 (§12). |
| 3 | The fee for **تحقيق الوفاة والوراثة والوصية الواجبة** (the إشهاد application) | 🟡 **Not established.** Practically the most-requested certificate in this file (§7.6). |
| 4 | The **experts' fees** (الخبيران: social + psychological) under Law 10/2004 annexed Art. 11 — amount, who advances them, who bears them finally | 🟡 **Not in the article and not retrieved elsewhere.** ⭐ This is the largest real cost driver in a contested custody or divorce case, and the file cannot price it. |
| 5 | The **Ma'zoun / documentation** charges for a marriage contract, and the **notary (الشهر العقاري)** charges where the marriage is documented there (Civil Status Law Art. 5, §2.1) | 🟡 **Not established.** The ministry decisions named at §2.2 were not read from the Gazette. |
| 6 | The charge for registering / notarising a **قائمة المنقولات** | 🟡 **Not established** (§2.5 covers its evidentiary force, not its price). |
| 7 | The **bailiff (محضر)** fees for notification and execution | 🟡 **Not established.** |
| 8 | The **lawyer's fee** — market rate, and the fee the court fixes for an **appointed** lawyer under Art. 3(1) (paid by the Treasury) | 🟡 **The article fixes the principle, not the amount.** |
| 9 | The **Fund's** payment and any charge for opening a Fund file | ✅ the payment cap is **EGP 500/month per beneficiary** (§4.6); 🟡 **the ministerial instrument setting that cap was not retrieved**. |

📌 **Rule for an agent: never state a figure that is not in §10.2 or §10.3.** Say: *"this claim is outside the statutory fee
exemption; the fee is assessed by the court's registry, and I cannot quote it — ask the registry for a written تقدير."*

## 10.5 Penalties that get mistaken for fees — carry them apart

| Instrument | Amount | Where |
|---|---|---|
| **Penal Code Art. 293** (failure to pay maintenance/custody/housing money) — **as replaced by Law 6/2020** | up to **1 year** and/or a fine **not exceeding EGP 5,000** ⚠️ **not 500** | §4.5.4 |
| **Law 25/1929 Art. 20(2)** — refusal of رؤية | **no fine**: warning, then **temporary transfer of custody** | §5.4, §9.3 |
| **Law 77/1943 Art. 49** (withholding an inheritance, added 2017) | **not less than 6 months' imprisonment** and/or **EGP 20,000–100,000**; **not less than 1 year** on repetition; **صلح at any stage** | §7.4 |
| **Penal Code Art. 227** (lying about age to obtain a marriage contract) | up to **2 years** and/or a fine up to **300 EGP**; the officiant knowing: up to a fine of **500 EGP** | §2.2 |
| **Law 1/2000 Art. 46** (failure to file an accounting) | fine up to **500 EGP**, up to **1,000 EGP** on repetition | §10.3 |
| **Law 1/2000 Art. 79** (obtaining Fund money by sham procedures or evidence) | **6 months to 2 years**; up to **2 years** for undue amounts | §9.1 |
| **Law 11/2004 Art. 5** → **Arts. 17 and 18 of the Nasser Bank law** apply to the Fund | *not a money figure* — ✅ read in the 2004 gazette scan («**وتسرى على الصندوق أحكام المادتين (١٧، ١٨) من القانون رقم ٧٧ لسنة ١٩٧١ بإنشاء هيئة عامة باسم بنك ناصر الاجتماعى**» — ⚠️ **the two articles' content was not read**, so do not describe what they provide) | ✅ Art. 5 read; ⚠️ content of the referred articles not read |

---

# 11. Widely repeated but unverified — check before repeating

**This is the mirror image of the corrections table.** The corrections table holds things the primary texts **contradict**. **This
section holds things that everyone repeats and I could not verify either way** — because the only sources are fatwas, campaign pages,
law-firm content, or a copy of a law that was never updated. **Nothing in this section may be stated as law.** Where I did resolve
one, the row says so.

| # | The claim, as it circulates | Where it circulates | Status |
|---|---|---|---|
| 1 | «**الصندوق التكافلى لدعم الأسرة** already pays / replaces the Family Insurance Fund» | 2026 news reporting and commentary on the third bill | 🟡 **NOT ENACTED.** The bill was referred to the **joint committee on 12 October 2026**; one MP says it would **repeal Law 11/2004**. **Today the payer is the Fund under Law 11/2004 — do not migrate a beneficiary on the strength of the bill.** §1.2, §10.2 |
| 2 | "A bride **must have a wali**, and the Ma'zoun will not document the marriage without one" | Said as *law* by Ma'zoun-counter tradition, family, and some advisers | ⚠️ **THE LAW IS THE OPPOSITE IN THE HANAFI DEFAULT THAT EGYPT APPLIES** (Art. 3(1) of Law 1/2000 promulgating: «بأرجح الأقوال من مذهب الإمام أبى حنيفة») — and **the practice is the opposite of both**: reported oral instructions to Ma'zouns to refuse a first-marriage bride under 40 without a wali, which **I could not find in any regulation**. ⭐ **And the statutory remedy if a Ma'zoun or notary refuses is an order on petition to the judge of urgent matters** (Law 1/2000 promulgating Art. 1(1)) — §5.6, §8.2 |
| 3 | "An **عرفي** marriage gives the wife **no rights at all**" | Said to women in difficulty, widely | ❌ **TOO BROAD, and the error runs against the wife.** An عرفي marriage is a **valid contract** whose *proof* is restricted: it cannot support money claims **on denial** (Art. 17(2)), but **it can support تطليق/فسخ** (the same article's exception), it produces **نسب** within Art. 15 of Law 25/1929, and it carries **mutual maintenance duties while the spouses live together**. §2.4, §6.4, §7.5 |
| 4 | "The wife can claim **years of unpaid maintenance** when she finally sues" | Common in advice columns | ❌ **CONTRADICTED — one year.** Law 25/1920 Art. 1: «**ولا تسمع دعوى النفقة عن مدة ماضية لأكثر من سنة نهايتها تاريخ رفع الدعوى**». The remedy for delay is the **provisional order within the case** (Art. 16(2) of Law 25/1929), not a longer arrears claim. §4.2–§4.3, §9.1 |
| 5 | "Maintenance is a **fixed proportion of the husband's salary**" / "there is a **minimum of EGP X**" | Widely believed, and expressed in some news pieces | 🟡 **NO STATUTORY PERCENTAGE AND NO STATUTORY MINIMUM FIGURE.** Art. 16(1) assesses on **the husband's circumstances** with a **floor** at her essential needs, and the **garnishment** percentages in Art. 76 (25–50%) are **deduction ceilings**, **not** the maintenance award. ⭐ **Do not read Art. 76's percentages back into the award.** §4.2, §4.5.2 |
| 6 | "The divorced wife may stay in the **marital home for two years**" | Repeated by clients and in some firm blogs | ⚠️ **CONFUSED.** The housing right in **Art. 18 bis/3** is drafted for **the children and their custodian**, and it was **partly struck down** by the SCC where the children have money or the custodian has a residence — a **duration for the wife herself** is not in the text I read. §5.5 |
| 7 | "Custody after **15** means the child **goes to the father**" | Universal shorthand | ❌ **CONTRADICTED — the child CHOOSES**, and the same article gives no automatic transfer: Art. 20(1) (Law 4/2005) ends women's custody at 15 and lets the child stay **with the custodian without custody pay** until the boy reaches majority and the girl marries. ⚠️ **Who supports the child in that window is not spelled out in the articles read** — get it into the judgment. §5.2 |
| 8 | "A **remarried mother** loses custody automatically" | Classical-fiqh shorthand | 🟡 **NOT IN THE STATUTE READ.** Art. 20 lists the custodian's qualifications and the order; the **classical conditions** (a woman's marriage to a stranger, etc.) come through the Hanafi default of Law 1/2000 promulgating Art. 3(1) — **and I did not read a statute or a Cassation heading embodying them.** Check before warning a client. §5.1–§5.3 |
| 9 | "The **رؤية schedule** is the law: parents weekly, grandparents monthly, other relatives 3–4 times a year" | Quoted from press coverage as if it were the statute | ⚠️ **THE STATUTE HAS NO SCHEDULE** — it says the court fixes the arrangement, place and manner (Art. 20(2) of Law 25/1929). The quotas come from **MoJ Decision 1150/2010, quoted only through a 2026 press report**; the decision's text was not retrieved. **Say "the ministry regulation is reported to provide…"**. §5.4 |
| 10 | "The Fund's **EGP 500** cap is in the law / **was raised** in 2024–2026" | Repeats the bank's own figures as if statutory | ⚠️ **THE STATUTE SETS NO CAP** (Art. 72 + Law 11/2004 Art. 3). The **EGP 500/month per beneficiary** figure is what **Nasser Bank's official page** and the Ministry of Social Solidarity state as the operating payment; **I could not retrieve the instrument fixing it, and found no verified raise.** §4.6, §12 |
| 11 | "A spouse who **changes religion or sect** changes the law that governs the marriage — it is an established «قاعدة عرفية»" | Stated as settled in litigation commentary and in the Cassation digests | 🟡 **THE OLD ANCHOR FELL WITH THE LAW.** The pre-2000 rule (Art. 7 of **Law 462/1955**) regulating change of rite was **repealed with the whole law by Law 1/2000 promulgating Art. 4**; commentary itself calls the survival «**قاعدة عرفية**»; and the reported Cassation rulings **go both ways** on a spouse who joins another church. **Treat it as case-law practice, never as a statutory rule, and never as a mechanism a client can rely on.** §1.3, §12 |
| 12 | ⭐ **"«تغيير الملة أو الطائفة» is the reason a Christian couple can get a divorce in Egypt"** | The most-repeated practical advice in Coptic personal-status discussion | 🟡 **SAME ROW AS 11, and it is the one to be most careful with.** Art. 3(2) governs spouses «**المتحدى الطائفة والملة**»; **where the spouses cease to be of one community the confessional gate of Art. 17(3) stops applying and the Hanafi default becomes the candidate governing law** — but **the mechanism's statutory basis was repealed in 2000 and its survival depends on case-law described as customary**. **Do not tell a client to change denomination in order to divorce**; say the reported practice exists, that it is contested, and that it needs a lawyer's current Cassation search. §1.3 |
| 13 | "**Adoption (التبني) is forbidden** and only **الأسر البديلة** exists" | Comparative-family pages and NGO material | 🟡 **ONE STATUTORY TRACE CONFIRMED, THE REST NOT.** ✅ Law 10/2004 annexed Art. 11 (as amended by **Law 215/2017**) requires the social expert, in a **نسب** case, to state whether the child is **within the alternative-families system of the Ministry of Social Solidarity** — so the system exists and the court must know a child's status in it. ⚠️ **The statute that organises الأسر البديلة, its conditions, and whether any form of adoption exists in Egyptian law were not read in this pass.** |
| 14 | "**Married women need the husband's written permission** to travel or to hold a passport" | Everyday belief, and half-true in consular practice | ⚠️ **THE STATUTE'S PROVISIONS ARE NARROWER.** Art. 9(أولاً)(3) gives the District court jurisdiction over «الإذن للزوجة بمباشرة حقوقها، **متى كان القانون الواجب التطبيق يقضى بضرورة الحصول على إذن الزوج**»; and **promulgating Art. 1(5)** gives the **judge of urgent matters** orders on petition in «**المنازعات حول السفر إلى الخارج** بعد سماع أقوال ذوى الشأن». 🟡 **The passport/travel-administration rules themselves were not read** — do not quote a permission rule as law. §8.2 |
| 15 | "A woman's **testimony is worth half a man's** in family cases" | Frequently asserted about Egyptian courts | 🟡 **NO CODIFIED HALVING RULE WAS FOUND.** The statutory evidence rules are those of the **Evidence Law (civil and commercial)** plus the Hanafi default (**Law 1/2000 promulgating Art. 3(1)**), and specific proof rules are set **per claim type** (e.g. Art. 17(2) on proving the marriage; Art. 19 on the arbitrators' evidence; Art. 24 on the judge's verification «بشهادة من يثق به»). **Do not assert a general evidence-weight rule either way**; identify the specific article for the specific claim. §8.5 |
| 16 | "The **child's opinion is taken at 15**, and that decides custody" | Reasonable reading of the custody-age rule, widely repeated | ⚠️ **PARTIALLY TRUE, ON DIFFERENT ARTICLES.** Art. 20(1) gives the **child** the post-15 choice to remain with the custodian; **Law 10/2004 annexed Art. 10** requires the court to be equipped for **the attendance of minors to hear their statements**; **Art. 11** makes the experts' reports compulsory in custody claims. **There is no article making the child's wish decisive — the standard is «مصالح الطفل الفضلى».** §5.2, §8.1 |
| 17 | "**Children's housing** after divorce is automatic, and it is the wife's for life" | Standard advice | ⚠️ **TWO SUBTRACTIONS.** Art. 18 bis/3 was held **partly unconstitutional** (SCC, Case 5/8J, 6 Jan 1996) **where the children have present money or the custodian has a residence**, and **as to its time limit** — and the right runs to **the children and their custodian**, not to the wife as such. §5.5, corrections row 8 |

📌 **Rule for a model using this file.** **If a claim is in this section, do not assert it.** Say: *"this is widely stated but I could
not verify it from an official source; the verifiable position is …"* — then give the **article, the SCC ruling, or the official page**
from the sections above. **And where the source is a fatwa, a campaign, or a bill, name it as such in the same sentence.**

## Source conflicts recorded in this file

**Where two retrieved sources disagree, both are recorded, with a note on which governs.**

| # | The conflict | Side A | Side B | Which governs |
|---|---|---|---|---|
| 1 | **The fine in Penal Code Art. 293** | **The amended text (Law 6/2020, Gaz. No. 5 bis, 2 Feb 2020):** «**غرامة لا تتجاوز خمسة آلاف جنيه**» — **EGP 5,000** | **Pre-2020 copies and a large share of current Arabic pages:** «غرامة لا تتجاوز **خمسمائة** جنيه» — **EGP 500**; ⚠️ and this file's own first draft carried 500 | ✅ **The amended text.** Cite **EGP 5,000**, note that the 500 circulates. §4.5.4, §10.5, row 1 of the corrections table |
| 2 | **The Official Gazette issue number of Law 176/2020** (which replaced Art. 47 of Law 1/2000) | The **footnotes of the consolidated copy**: «**العدد ٣٧ مكرر**» | A **portal reproduction** (`egyptianlaws.com`): «**العدد ٣٦ (مكرر)**» — and the **OCR of the gazette page scan's own header** read «**العدد ٥٥ مكرر**» — all dated **سبتمبر / 5 September 2020** | ⚠️ **UNRESOLVED — three variants, and the OCR of the scanned header is the least reliable of them**, because that scan's Arabic-Indic digits OCR badly (the month **سبتمبر** is legible; the numerals are not). The **substitution and the new figures** (10,000 / 20,000 EGP, once every **three** months, plus the emergency-majoration paragraph) are ✅ read from the page image. **Reproduce the conflict; do not choose an issue number.** §5.7 |
| 3 | **Art. 47's figures** | The **consolidated copy used for this file** (not updated): 1,000 EGP, raisable to 3,000 EGP, **once every six months** | **Law 176/2020's gazette page scan:** **10,000 EGP**, raisable to **20,000 EGP**, **once every three months** | ✅ **The amending law.** The consolidated copy is a **stale reproduction** — a reminder that **every consolidated Arabic text on the web has an update horizon**. §5.7 |
| 4 | **The appeal route to the Court of Cassation in family cases** | ✅ **Law 1/2000 Art. 62:** the parties and the PP **may** challenge appeal-court judgments by cassation | ✅ **Law 10/2004 annexed Art. 14:** the **specialised family appeal circuits'** judgments and decisions are «**غير قابلة للطعن فيها بطريق النقض**»، «مع عدم الإخلال بأحكام المادة (250)» of the CPC | ⚠️ **The later, specific law governs in principle — but CPC Art. 250 was not read**, so the exception's scope is open. **Advise finality; verify Art. 250 with a lawyer.** §8.6, §12 |
| 5 | **What the Fund pays** | ✅ The **statute** (Art. 72 + Law 11/2004 Art. 3 as replaced) — **no cap**, and the bank **recovers** what it pays (Art. 75) | **Nasser Bank's official page / Ministry statements:** **EGP 500 per month per beneficiary**, **no arrears**, balance «**يتم رد فارق القيمة عند التحصيل**» | ✅ **Both are true in their own register** — cite the **statute for the right** and the **bank page for the practice**; the client's expectation must be set on the practice. §4.6 |
| 6 | **The custody age** | **Law 25/1929 Art. 20(1) as replaced by Law 4/2005** (Gaz. No. 4 bis, 4 March 2005): **15** for girl and boy alike | **Pre-2005 rulings, old guides and family-court folklore:** **10 for a boy, until marriage for a girl** | ✅ **The 2005 text.** §5.2, corrections row 6 |
| 7 | **Whether the confessionally governed areas include custody** | **The SCC's own summary** counts as unified only «**كتلك التى تتعلق بمواريثهم ووصاياهم وأهليتهم**» — **estates, wills, capacity** | **The general guides** treat custody and divorce ages as one law for all Egyptians | ⚠️ **UNRESOLVED — and it matters for non-Muslim families.** The SCC passage implies **custody sits inside the confessional area**, so **Art. 20's ages may not be the governing rule** for a couple of one sect whose community law provides otherwise. **Verify before advising a Christian couple on custody ages.** §1.3, §12 |
| 8 | **The marriage age's home** | ✅ **Art. 31 bis of the Civil Status Law 143/1994** (added by Law 126/2008), whose sanction is **disciplinary** | ⚠️ The **Gazette heading of Law 126/2008 itself** reads «**بتعديل بعض أحكام قانون الطفل**», and the same law also amends the Child Law and the Penal Code — which is why the internet files the age rule under the Child Law | ✅ **The article that contains the rule: Art. 31 bis of Law 143/1994.** Cite it, and mention the misleading heading. §2.2, corrections row 1 |
| 9 | **The "200,000 EGP" child-marriage fine** | **The 2022 draft banning child marriage** (approved in principle 3 July 2022, **never enacted**): 1 year + 50,000–200,000 EGP | **The law in force:** Penal Code Art. 227 — up to 2 years and/or **300 EGP**, officiant with knowledge up to **500 EGP** | ✅ **The law in force**; the 200,000 figure is **a bill and a different offence (trafficking)**. §2.2, §2.7 |
| 10 | **Law 462/1955 as the governing instrument for non-Muslims** | **Commentary, books and (still) court submissions** cite Law 462/1955 | ✅ **Law 1/2000 promulgating Art. 4 repealed it**; the rule now sits in **promulgating Art. 3(2)**, and the **SCC (Case 151/20)** says that paragraph «**حلت محل الفقرة الثانية من المادة 6 من القانون رقم 462 لسنة 1955**» | ✅ **Law 1/2000 Art. 3(2).** Cite 462/1955 **only** for history and case-law. §1.3, corrections row 15 |

---

# 12. Open questions and things I could NOT resolve

**None of the items below may be filled in from memory. Each says what was searched.**

| # | Question | What I searched | Status |
|---|---|---|---|
| 1 | The **court fee (رسم)** for a **خلع** claim, a **مهر/جهاز** claim, an **inheritance** claim, or an **إشهاد الوراثة** application — the claims outside Art. 3's exemption | Consolidated Laws 1/2000 and 10/2004 (they exempt or make things free, they do not price); MoJ decision listings; `lawhub.info/eg`, `mksegypt.org/ar/laws`, `manshurat.org`; **the general judicial-fees legislation and current fee schedules were not retrieved** | 🟡 **UNRESOLVED — the biggest gap in this file, and the one a client will hit first.** Ask the registry for a written تقدير. §10.4 |
| 2 | The **experts' fees** under Law 10/2004 annexed Art. 11: amount, advance, and final incidence | The article's text (silent); Law 10/2004 promulgating Art. 4 (MoJ implementation decisions — not retrieved); no fee schedule found | 🟡 **UNRESOLVED.** §8.3, §10.4 |
| 3 | The **Justice-Minister decision under Law 1/2000 Art. 69** (procedures for executing تسليم/ضم/رؤية/سكنى judgments, and who carries them out) | Article text read; the decision itself **not retrieved**; `moj.gov.eg` document paths not searched exhaustively for it | 🟡 **UNRESOLVED.** Without it, no one can say from this file **how** an enforcement officer will act. §9.2 |
| 4 | **MoJ Decision 1150/2010** (لائحة تنظيم رؤية المحضونين) — its text, and whether it is the Art. 69 decision | Only a **secondary quotation** (parlmany.com, 16 Apr 2026) was reachable; the decision itself not retrieved | ⚠️ **PARTIAL — secondary only.** Quotas may not be quoted as law. §5.4, §11 row 9 |
| 5 | The **instrument fixing the Fund's EGP 500/month cap**, and whether it has changed since 2020 | Nasser Bank's official Fund page (`nsb.gov.eg`); Ministry of Social Solidarity statements; 2020/2022/2025/2026 press | 🟡 **NOT RETRIEVED.** The statute has no cap; the practice cap is sourced to the bank's page. §4.6, §11 row 10 |
| 6 | The **Official Gazette issue number of Law 176/2020** (٣٧ مكرر vs ٣٦ (مكرر)) and of **Law 215/2017** (its scan's digits are OCR-garbled) | Both gazette page scans; the footnotes of the consolidated copies | ⚠️ **UNRESOLVED — reproduce both forms rather than choosing.** §5.7, source conflicts rows 2–3 |
| 7 | **Law 119/1952 (الولاية على المال)** — the substantive guardianship law the whole الولاية على المال chapter operates on | Cited by name in Art. 9(ثانياً) of Law 1/2000 and in §5.7; **not read in this pass** | 🟡 **NOT READ.** An agent handling a minor's money must read it. §5.7 |
| 8 | The **pecuniary finality threshold (النصاب الانتهائى)** of the District judge, on which Art. 9(أولاً)(4)'s finality for مهر/جهاز claims depends | Law 1/2000 (refers to it, does not state it); the amending laws I read are silent | 🟡 **UNRESOLVED.** Do not state a finality amount. §8.4, §10.4 |
| 9 | The **ordinary appeal period** in personal-status cases (as distinct from Art. 61's 60 days for a person domiciled abroad) | Law 1/2000 Art. 61 read (only the 60-day rule); the **CPC** was not read in this pass | 🟡 **UNRESOLVED.** State Art. 61's rule only. §8.6 |
| 10 | What **CPC Art. 250** preserves against Law 10/2004 Art. 14's no-cassation rule | The text of Art. 14 (which carves it out); CPC Art. 250 not retrieved | 🟡 **UNRESOLVED — and it is the whole scope of the cassation question.** §8.6, source conflicts row 4 |
| 11 | Whether the **settlement office** step is required in a **confessional divorce** where the community's own law governs, and how the «الدعاوى التى لا يجوز فيها الصلح» exception is applied there | Law 10/2004 Arts. 6 and 9 read; no decision, circular or practice note found | 🟡 **UNRESOLVED.** Ask the office in writing. §8.2 |
| 12 | Whether **custody, its ages and its incidents for a non-Muslim couple** are governed by Law 25/1929 Art. 20 or by the community's own rules | The SCC passage on the «دائرة محدودة» of unification; the confessional structure in Art. 3(2) | ⚠️ **UNRESOLVED and important** — the unification is described as covering **estates, wills and capacity**, not custody. Verify for a Christian couple. §1.3, source conflicts row 7 |
| 13 | The **text of the three 2026 bills** (355 articles, the Christian family bill, the Fund bill) — what exactly they would change | Press reporting of the referral and of some provisions only; the bill's text was **not retrievable** | 🟡 **UNRESOLVED.** Everything in §1.2 about their contents is **reported**, not read. §1.2 |
| 14 | **Law 142/2006's** amendment of Law 10/2004 promulgating Art. 2 (the transfer rule) | Not read; the index records only that it amended Art. 2 | ⚠️ **NOT READ.** Do not quote the pre-2006 transfer rule as current. §8.2 |
| 15 | The **list of diseases and the validity period** of the pre-marriage medical examination under Art. 31 bis(2) | The article (which refers to a Health/Justice ministers' decision); the decision **not retrieved** | 🟡 **UNRESOLVED.** §2.3 |
| 16 | Whether a **DNA report** is admitted in a نسب case in practice, and what weight it is given | The statute book (**no provision** — ✅ a negative finding, §6.3); court practice not verifiable from the sources reached | 🟡 **UNRESOLVED — the statute's silence is the verified part.** §6.3 |
| 17 | The **classical (Hanafi) conditions of custody** that operate through the default rule — remarriage of the mother, religion, and the like | Art. 20 of Law 25/1929 (a qualifications list, no such conditions); the Hanafi default in Law 1/2000 promulgating Art. 3(1); no Cassation heading located | 🟡 **UNRESOLVED.** Do not tell a mother her remarriage costs her custody without checking current Cassation. §5.1–§5.3, §11 row 8 |
| 18 | Whether **unstamped/unpaid Fund levies** (Law 11/2004 Art. 2) block documentation of a marriage or a divorce at the counter | Law 11/2004 Arts. 2 and 4 read (collection rules promised to a MoJ decision); the decision not retrieved | 🟡 **UNRESOLVED.** §10.2 |

---

# 13. Trap list for the agent — the fifteen things that go wrong most

1. **Promising that "the new personal status law" applies.** As of **19 October 2026** there is **no consolidated family law** — three
   bills sit in a **joint committee** (§1, §1.2). Say *the law in force*, then, if useful, *a bill would change this*.
2. **Citing Law 462/1955 as the current rule for non-Muslims.** It was **repealed by Law 1/2000 promulgating Art. 4**; the allocation
   rule is now **promulgating Art. 3(2)** (§1.3, corrections row 15). And **inheritance, wills and capacity are unified for all
   Egyptians** — the confessional carve-out does not reach them (corrections row 16).
3. **Filing in the wrong order.** For a settlable family claim the **settlement office comes first** (free, 15 days, and its صلح minutes
   are **executory**), and skipping it makes the claim «**لا تقبل**» — though the court may cure it by referral (§8.2).
4. **Then filing in the wrong court.** The **divorce court rules alone** on maintenance, custody, رؤية and housing, and any other court
   must **refer** those claims to it «**حتى يصدر فيها حكم قطعى واحد**» (§8.7); local competence can be **her choice** under Art. 15(1);
   and after the first claim the family has **one court and one file** (Law 10/2004 Art. 12).
5. **Forgetting the two reconciliations.** With a child, a **طلاق/تطليق** judgment requires the court to offer صلح **twice, 30–60 days
   apart**, plus **arbitrators named by the parties** with their own session (§8.5). **Do not promise a fast decree** — and do not let a
   client conclude the judge is delaying on purpose.
6. **Merging the two age rules.** The **documentation** age is **18/18** (Art. 31 bis of Law 143/1994, sanction **disciplinary**);
   the **claim-admissibility** ages are **16 for a wife and 18 for a husband at filing** (Law 1/2000 Art. 17(1)). §2.2, §8.5.
7. **Treating an عرفي marriage as either void or fully provable.** It proves **نسب, تطليق and فسخ**; it **fails against a denial** for
   **money and inheritance** claims (Arts. 17(2), 7, 5 bis(3)) — §2.4, §6.4, §7.5.
8. **Skipping the Fund and the deduction route and going straight to a criminal complaint.** **Art. 76 bis is the precondition** of the
   Art. 293 complaint in the cases it governs; and the criminal route needs **ability proved** and **3 months' default after
   notification** (§9.1).
9. **Quoting the EGP 500 fine for Art. 293.** The amended text says **up to EGP 5,000**; **500** is the **pre-2020** text, and "**EGP
   500**" is also the **Fund's monthly payment cap** — three different things that sound the same (§4.5.4, §9.1, §10.5, conflicts
   row 1).
10. **Promising forced visitation — or telling a custodian that refusal is free.** **«ولا ينفذ حكم الرؤية قهراً»**; the sanction is
    **temporary transfer of custody**. But **ضم/تسليم may be executed by force**, subject to the **execution judge's** order (§5.4, §9.3).
11. **Getting custody wrong in three ways at once:** the age is **15 for both**, the child **chooses** afterwards, and the **mother's
    custody is not automatic** (§5.1–§5.3). And grandparents' رؤية **does not** depend on the parents being absent — that condition was
    **struck down by the SCC in 2013** (corrections row 7).
12. **Assuming the housing duty is absolute, and the wife's.** Art. 18 bis/3 is **partly unconstitutional** and runs to the **children
    and their custodian** (§5.5, corrections row 8).
13. **Wills and inheritance folklore:** a bequest **to an heir is valid up to one-third** (Art. 37 of Law 71/1946); **الوصية الواجبة
    needs the certification application**; there is **no inheritance between a Muslim and a non-Muslim** (Art. 6 of Law 77/1943); and
    the **withholding offence is Art. 49 of Law 77/1943, not the Penal Code** (§7.1–§7.4).
14. **The two-timing trap after judgment.** A **divorce/annulment** judgment **is not enforceable until the cassation periods lapse**
    (Art. 63), while **maintenance, رؤية and child-delivery orders are enforceable at once, without security** (Art. 65) and an
    **إشكال does not suspend** them (Art. 78). Get the money order first; explain the delay in the divorce itself (§3.6, §9.2, §9.4).
15. **Selling a fee figure, a fatwa, a campaign, or a bill as law.** Family litigation is **partly free** (maintenance family,
    settlement office) and **partly unpriced in this file** (§10.4); **Dar al-Ifta opinions are fatwas** (§5.6); **NGO and campaign
    positions are advocacy**; and the **2026 package is a bill**. Name the source of every sentence — **this file's whole method is
    that the reader can tell what was read, what was only reported, and what was searched for and not found.**

---

*File compiled and written **2026-10-19**. **Method, stated once:** every article number in this file was read out of a retrieved text —
the consolidated Arabic texts of **Law 25/1920** and **Law 25/1929** (`lawhub.info/eg/?p=11578`, `?p=11576`), **Law 1/2000**
(promulgating Arts. 1–6 and annexed Arts. 1–79, `mksegypt.org/ar/laws/24131`), **Law 10/2004** (`lawhub.info/eg/?p=11675`),
**Law 77/1943** and **Law 71/1946**; the **Penal Code Art. 293** as amended; and the **Official Gazette page scans** of the amending
laws (**Law 91/2000** — Art. 76 bis; **Law 113/2015**; **Law 176/2020**; **Law 215/2017**; **Law 126/2008**; **Law 4/2005**), fetched
from `moj.gov.eg:73/Doc/001/…` with `curl -k` and read as **rendered page images**, because the scans have no usable Arabic text layer
and OCR mis-reads Arabic-Indic numerals — which is itself recorded as a source conflict at §12 and source conflicts row 2. Case-law is
cited from the **Supreme Constitutional Court**'s own publications, and **Dar al-Ifta opinions are labelled fatwas wherever they
appear**. The **2026 bills** are described only as reported, in §1.2, and there is no sentence in this file that treats them as law.
**Companion files:** `08-intellectual-property-egypt.md` (the structural exemplar), `05-tenancy-egypt.md` (the format's originator),
`06-criminal-procedure-egypt.md` (how a Penal Code Art. 293 complaint or a Law 219/2017 prosecution actually runs), and
`03-employment-courts-aml-banking.md` (the general court structure). **As-of date for the whole file: 2026-10-19.***

