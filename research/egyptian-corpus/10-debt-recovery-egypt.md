# Egyptian Debt Recovery — Verified Reference Corpus
# تحصيل الديون في مصر — المرجع التشريعي

**Purpose:** a citation-safe reference for an AI agent helping a **non-lawyer in Egypt** collect money that is
legally owed to them (or respond to a claim that is owed by them): what counts as provable debt, the fast payment
orders (أوامر الأداء) and petition orders (أوامر على العرائض), the interim protections (الحجز التحفظي on movables,
garnishment ما لدى الغير), the cheque as a collection weapon (civil + criminal + the صلح that kills it), the exact
limitation clocks, the execution machinery (التنفيذ) including execution on real property and on wages, the assets
that cannot be attached, and how the proceeds are distributed.
Every article number below was read out of a retrieved primary or official-secondary text. **Nothing is asserted from memory.**
**As-of date for the whole file: 2026-10-28.**

⚠️ **Each section carries its own `As of:` line — that is the date *that section* was last read against a source.**
Everything in this file was first built on **2026-10-28**.

⚠️⚠️ **THE SINGLE MOST IMPORTANT THING IN THIS FILE:** in Egypt, **a court judgment (or another سند تنفيذي) is
the only gateway to taking money or property from a debtor.** CPC **Art. 280**: «لا يجوز التنفيذ الجبري إلا بسند
تنفيذي اقتضاء لحق محقق الوجود ومعين المقدار وحال الأداء». No payment order, no attachment, no sale, no garnishment
can exist on the strength of an unpaid invoice alone — the fastest legitimate route is **أمر الأداء** (CPC Arts.
201–210), which itself produces an executory instrument. An agent that suggests "just go take his furniture" or
"block his salary yourself" is describing illegal self-help.

**Relationship to the other corpus files:** `04-practical-operations-egypt.md` §7.2 verifies cheque clearing and
evidence discipline for payments — this file cross-refers for the banking mechanics and adds the collection side.
`05-tenancy-egypt.md` verifies lease fixed-dates (Law 25/1968 Art. 15) — the lease rules that survive an attached
property are here (Arts. 408–409) cross-refed to 05. `07-family-law-egypt.md` verifies the maintenance (نفقة)
special rules (Law 1/2000 Art. 76) — cross-refed, not duplicated. `03-employment-courts-aml-banking.md` carries the
court structure and the pecuniary-threshold question — see its stale-figures note.

## How to read the confidence markers

| Marker | Meaning |
|---|---|
| ✅ **verified** | I read the article text or the official gazette reference in a retrieved document, and I quote the source URL. |
| ⚠️ **PARTIAL** | The instrument is verified; a specific article number or detail inside it is **not**. Describe the concept, never the number. |
| 🟡 **UNVERIFIED — needs primary-source check** | I could not confirm it. I say what I searched. Do not cite. |
| ❌ **does not exist / claim overturned** | A claim that circulates is false, or the instrument it names could not be located. This is a finding, not a gap. |
| ⭐ | A rule worth surfacing to the user unprompted, because it changes their decision. |

## ⚠️ CORRECTIONS TABLE — read this before citing anything in this file

These are claims or beliefs that this research checked and **overturned or narrowed**. If an AI output contradicts this table, trust the table.

1. ❌ **"أمر بالإحضار" / "الأمر بالإحضار أو بحجز أموال المدين" as an Egyptian CPC tool, attributed to a
   "Law 10/1953"** — **no such provision exists in the current CPC.** The full text of CPC Law 13/1968
   (lawhub.info `?p=11332`, 6,269 lines, read end-to-end) contains **zero** occurrences of إحضار, تجريد from
   الحيازة, or "بحجز أموال المدين". No primary or secondary source located a Law 10/1953 carrying this title —
   two targeted searches returned only unrelated statutes and Algerian/Palestinian material. The phrase belongs to
   the *regional* CPC family (the Kuwaiti/others' codes, where an أمر بالإحضار block exists and is commonly
   numbered in the 216–218 range) — the classic cross-border contamination vector for this topic. **The Egyptian
   interim toolkit is: أوامر الأداء (Arts. 201–210) + الحجوز التحفظية (Arts. 316–352).** Do not cite أمر
   بالإحضار, and never cite "Law 10/1953" for it. (§5)
2. ❌ **"حجز الراتب من 20% إلى 50%" / Kuwaiti garnishment figures** — the Egyptian rule is one sentence: CPC
   **Art. 309** — «لا يجوز الحجز على الأجور والمرتبات إلا بمقدار الربع وعند التزاحم يخصص نصفه لوفاء دين النفقة
   المقررة والنصف الآخر لما عداه من الديون» — **one quarter (25%) of wages/salaries**, and when debts compete,
   half of that quarter goes to the court-ordered maintenance claim and half to the rest (§6.2). The 20%/50%
   numbers come from other Gulf codes sharing the same article-number lineage.
3. ❌ **"الشيك صالح للوفاء ثلاثة أشهر"** — **stale pre-2004 text.** Commercial Code **Art. 504** as shown in the
   consolidated text: cheques drawn and payable in Egypt must be presented within **six months**; drawn abroad and
   payable in Egypt — **eight months**; the period runs from the date on the cheque; presentation to a recognised
   clearing house counts as presentation. The alberonsy consolidated text's footnote (3)/(4) records that both
   phrases were **replaced by Law 156/2004** (operative per Law 158/2003). The "3 months" figure survives on stale
   pages (benisuef.gov.eg) and in memory-based AI answers (§4.1).
4. ⚠️ **"أوامر على العرائض = المواد 194–210"** (some secondary pages label the whole block this way) — the block
   is two instruments: **أوامر على العرائض = Arts. 194–200** (the general petition-order mechanism) and
   **أوامر الأداء = Arts. 201–210** (the payment-order instrument). Art. 211 opens the appeal chapter (§3).
5. ❌ **"جريمة الادعاء الكاذب بالتزوير = المادة 537"** (some secondary sources number it so) — it is
   **Commercial Code Art. 536**; **Art. 537** is the *publication* of the conviction and the chequebook
   withdrawal penalty. Verified against the consolidated text and the Supreme Constitutional Court judgment
   document that quotes the block (§4.4).
6. ❌ **"الشيك سند تنفيذي"** — it is not. Nothing in Commercial Code Book Seven or CPC Art. 280 makes a cheque an
   executory instrument. The holder's routes are: **أمر أداء** (a cheque is a written, due, determinable debt —
   Art. 201), the ordinary action, **garnishment without a bond after dishonour** (Art. 525), and the **criminal
   route of Art. 534** with its صلح escape (§4).
7. ❌ **"التقادم التجاري عشر سنوات"** — the actual rule (Commercial Code **Art. 68**): claims between merchants
   arising from their commercial dealings prescribe in **seven years** from due date — and **final judgments in
   those claims lapse after ten years**. Civil claims: **15 years** (CC Art. 374). (§6)
8. ❌ **"المادة 382 من القانون المدني = سقوط الأحكام المدنية بعد عشر سنوات"** — CC **Art. 382** is the
   **suspension** of prescription whenever an obstacle makes demanding the right impossible (the mohamedhamadlaw
   and allied-for-legal summaries agree), e.g. between principal and agent. A "civil judgments lapse in 10 years"
   rule was **not found** in any retrieved text; the 10-year judgment-lapse rule exists **only in commercial
   claims** (Art. 68). Treat "civil judgment lapse" claims as unverified (§6.1, backlog #2).
9. ⚠️ **CPC pecuniary thresholds (Arts. 41, 42/1, 43, 47/1, 248, 480)** — the displayed lawhub text carries the
   base figures, and its amendment notes show **two successive replacements** by **Law 191/2020** and
   **Law 157/2024**. The operative figures cannot be stated with confidence from the retrieved texts alone —
   never quote a threshold number to the user; say "the thresholds were raised twice, most recently by
   Law 157/2024, and the clerk of the court confirms the current figure" (§3, §7.7).
10. ⚠️ **Art. 326's garnishment cost/interest cap («…عشر المبلغ…أربعون جنيهاً»)** — the concept is verified
    (one year's interest + expenses capped at a fraction of the debt); the monetary figures in the displayed text
    are obviously stale. Never quote the 40-EGP figure (§5.2).
11. ⚠️ **Art. 378's newspaper-notice threshold («خمسة آلاف جنيه»)** — same caveat as #9/#10: concept verified
    (newspaper publication for higher-value sale notices), figure possibly amended (§7.4).
12. ⚠️ **"قانون الإجراءات الجنائية الجديد" (2025)** — real and named: **Law 174/2025** (Gazette No. 45 bis (د),
    12 November 2025), but its application was **postponed to 1 October 2027** by **Law 160/2026**. Until then
    **CPCrim Law 150/1950 governs**, and the cheque-crime lapse rule lives in its **Art. 15** (as amended by
    Law 340/1952) — **three years for misdemeanours** (Art. 17 is the *interruption* rule, not the lapse rule —
    the "Art. 17" attribution circulating comes from the new code's renumbering) (§6.4).

## Index of instruments verified in this file

| Instrument | Role here | Verified blocks |
|---|---|---|
| **CPC — Law 13/1968** (and its amendment chain) | The whole procedure: orders, attachments, execution, distribution | Arts. 194–219 (orders + appeals), 274–312, 316–352, 353–466, 469–488 |
| **Civil Code — Law 131/1948** | Debt substance, interest, prescription | Arts. 226, 374, 375, 382, 385 (as sourced in 07/02 + mohamedhamadlaw) |
| **Commercial Code — Law 17/1999** (consolidated to 19 Feb 2018) | Commercial debts, notices, proof, the cheque | Arts. 56–70, 503–546 |
| **CPCrim — Law 150/1950** (as amended by 340/1952) | Criminal-lapse rule for cheque prosecution | Arts. 15, 17 |
| **Law 174/2025** (new CPCrim) + **Law 160/2026** | Future code — deferred to 1 Oct 2027 | promulgation + deferral only |
| **Law 1/2000 Art. 76** | Maintenance priority in garnished wages | cross-ref `07-family-law-egypt.md` |

---

# 1. Scope and the shape of a debt file

`As of: 2026-10-28`

## 1.1 What this file covers

✅ Civil and commercial money-debt recovery in the ordinary courts and via the CPC execution book: a business
owed money by a customer (or owing one), a freelancer with an unpaid invoice, a landlord-adjacent money claim,
a cheque or promissory note holder, a personal loan evidenced in writing. **Excluded on purpose:** the
maintenance (نفقة) collection track — its special rules live in Law 1/2000 and are verified in
`07-family-law-egypt.md` (cross-ref §6.2, §8); tax and social-insurance arrears — state-collection tracks with
their own statutes, not researched here (backlog); and rent-eviction — `05-tenancy-egypt.md`.

## 1.2 First question: is the debt "commercial"?

✅ **The classification changes the whole file** — interest, prescription, proof, and the debtor-protection rules:

- ⭐ Commercial debts owe **delay interest from the mere due date** (CC-of-commerce Art. 64, §6.2) — civil debts
  need a demand or a judgment before interest runs in most cases (CC Art. 226, §6.1).
- ⭐ Commercial claims between merchants prescribe in **7 years**, not 15 (Art. 68).
- ⭐ Commercial obligations can be proved **by any means at any value** (Art. 69/1) — civil legal acts above a low
  value require writing (CC Art. 15 rule; the current threshold figure is 🟡 — §1.3).
- ⭐ Merchants get **no statutory payment grace**: courts may not grant a merchant debtor extension or
  instalments except in necessity and without serious harm to the creditor (Art. 59).
- ✅ Payment in commercial matters is demanded only in **working hours** (Art. 57) and the creditor cannot be
  forced to accept agreed compensation in place of performance (Art. 60).

## 1.3 Proving the debt

`As of: 2026-10-28`

- ✅ **Commercial debts: any evidence, any value** — Commercial Code **Art. 69**: «يجوز إثبات الالتزامات التجارية
  أيا كانت قيمتها بكافة طرق الإثبات ما لم ينص القانون على غير ذلك» — and evidence against a written document is
  allowed in commercial matters (Art. 69/2).
- ✅ **Commercial books**: Art. 70 — the trader's own compliant books are evidence against him; books kept in
  compliance are evidence *for* their keeper against a merchant opponent; conflicting compliant books require the
  court to seek other evidence.
- ✅ **Payment discharges by handing back the document**: Art. 61 — payment to the holder of the debt document,
  indicated by التخالص or holding a مخالصة, discharges the debtor; possession of the document by the debtor is a
  **presumption of discharge** unless the creditor proves otherwise. ⭐ **Practical rule for both sides: never pay
  a debt without getting the original document back or a signed مخالصة — and never hand over the original without
  getting paid.**
- ⚠️ **Civil debts**: the general civil proof rules apply (writing above a value threshold); the threshold's
  current figure was not re-verified this pass — describe the concept, confirm the number with the court
  (backlog).

## 1.4 What a non-lawyer should have before asking for anything

- The original written instrument (contract, invoice, delivery note, cheque, promissory note, إقرار).
- The counterparty's **full identity and address** (the order/suit needs the full name and residence; CPC
  Art. 203 requires the debtor's full name and residence in the payment-order application).
- A payment history (bank transfers are the cleanest).
- The date the debt **fell due** — every clock starts there.

---

# 2. Before court: the invoice trail and the formal notice

`As of: 2026-10-28`

## 2.1 The commercial notice (الإنذار/الإعذار)

✅ Commercial Code **Art. 58**: notice in commercial matters is by **official notice or registered letter with
acknowledgement**; in urgent cases telegraph/telex/fax or other fast means suffice. (This is the same instrument
the skill `egy-legal-notice` operationalises — cross-ref it for drafting.)

- ⭐ For cheques, Art. 518 supplies a better proof anyway: the **bank's dishonour statement written on the
  cheque** (§4.3) — a formal notice is still worth sending because it fixes the debtor's knowledge and the
  interest/إنذار record, but the cheque route does not depend on it.
- ✅ An incidental rule with teeth: **Art. 59** — no extension/instalments for a merchant debtor except necessity
  + no serious creditor harm. ⭐ A creditor who agrees to informal instalments outside court may find the clock
  and the leverage gone — keep any instalment agreement written and dated.

## 2.2 What to demand in the notice

Not statutorily fixed — but the file that supports orammat-al-adaw must already contain: the debt's amount, its
ground, its due date, and the demand with a deadline. The **≥5-day written demand** is a *statutory precondition*
for أمر الأداء (Art. 202, §3.1) — one well-drafted notice can serve both purposes.

---

# 3. Fast payment routes (the court shortcuts)

`As of: 2026-10-28`

## 3.1 أوامر الأداء — CPC Arts. 201–210 ⭐ the main tool

✅ All six operative articles read in the full CPC text (lawhub `?p=11332`):

- ✅ **Art. 201** (the gate): exception from the ordinary suit rules where the creditor's right is
  **established in writing** and **due**, and everything claimed is a **money debt of determinable amount** or a
  **movable identified in kind/quantity**. For **commercial-paper creditors** (bills, notes, cheques): the order
  route runs **only against the الساحب (drawer), المحرر (maker), القابل (acceptor) or الضامن الاحتياطي
  (avaller)** — going after anyone else means the ordinary rules.
- ✅ **Art. 202** (the precondition): the creditor must **first demand payment with at least a five-day term**
  (تكليف بالوفاء) — satisfied by **registered mail with proof of delivery**, or by a **protest (بروتوستو عدم
  الدفع)** which replaces the demand. The order issues from the **قاضي المواد الجزئية at the debtor's domicile
  court** (or the head of the primary-court division) — unless the debtor accepted another court's jurisdiction.
- ✅ **Art. 203** (the application): a two-identical-copies petition with the debt instrument and proof of the
  demand attached, stating the facts, grounds, the debtor's **full name and residence**, and a **chosen domicile
  for the creditor** in the court's district. The order issues within **three days**.
- ✅ **Art. 204**: if the judge is not satisfied, he **refuses the order and sets a hearing** — turning it into an
  ordinary suit with service on the opponent. Refusing part of the claim ≠ refusing everything.
- ✅ **Art. 205** (service): the debtor is served **in person or at his domicile** with the petition and the
  order; **if service is not completed within three months of the order, it is as if it never existed.**
- ✅ **Art. 206** (the debtor's objection): تظلم within **ten days of service**, before the same-instance court,
  reasoned — and the appeal window starts when the تظلم window lapses; the right to تظلم is lost if the debtor
  appeals directly.
- ✅ **Art. 207**: the objector stands as a plaintiff; absence at the first hearing = objection as if it never
  was.
- ✅ **Art. 208**: the creditor pre-pays the full court fees (a quarter for the Art. 210 garnishment case).
- ✅ **Art. 209**: **accelerated enforcement (النفاذ المعجل)** applies to the payment order.
- ✅ **Art. 210** ⭐ (the garnishment combo): the same judge who issues the payment order may order the **حجز
  لدى الغير** — an express exception from Arts. 275/319/327 (which reserve that for قاضي التنفيذ) — and the
  creditor must, **within eight days of the attachment**, submit the payment-order application and the validity
  of the attachment procedure, **or the attachment is as if it never was**.

⭐ **Practical shape:** notice with ≥5-day term → 3 days for the order → serve within 3 months → debtor has 10
days to object → order is enforceable with accelerated enforcement → execute. It is the cheapest real route from
unpaid invoice to execution, and with Art. 210 it can freeze the debtor's receivables on day one.

## 3.2 أوامر على العرائض — CPC Arts. 194–200

✅ **Art. 194**: wherever **another statute** says a party may obtain an **order**, the petition goes to
**قاضي الأمور الوقتية** at the competent court (or the presiding judge of the pending case), in two identical
copies, with facts, grounds, a chosen domicile, and supporting documents.
✅ **Art. 195**: the judge issues the written order **by the following day at the latest**; reasons are required
only if departing from a previous order.
✅ **Art. 196**: the clerk hands the petitioner the second copy bearing the order by the next day.
✅ **Art. 197**: تظلم to the court within **ten days** of the refusal or the start of execution/service, by the
ordinary suit procedures.
⚠️ The **specific orders** (e.g. maintenance orders under Law 1/2000, eviction-related orders) are named in the
statutes that invoke this mechanism — see 07 and 05. The CPC block itself is the *mechanism*, not a menu.

## 3.3 The المستعجل route

⚠️ **PARTIAL**: the judge of urgent matters (قاضي الأمور المستعجلة) can order interim payment and protective
measures before a final judgment — the concept is verified through the code's uses (e.g. Art. 288's accelerated
enforcement for مستعجلة judgments; Art. 44's حيازة disputes), but this pass did **not** re-verify the
jurisdiction-list article and its number. Describe the route, don't cite the list article (backlog).

## 3.4 Ending it without a fight: settlement and substitute deposits

- ✅ **CPC Art. 280**: **محاضر الصلح certified by the courts or مجالس الصلح are سندات تنفيذية** — a certified
  settlement is directly executable. ⭐ This is what makes settlement attractive to a creditor: it converts the
  compromise into an enforcement ticket.
- ✅ **CPC Art. 302**: at any stage before the sale is imposed, a **deposit equal to the attached debts +
  interest + expenses** transfers the attachment from the assets to the money (new attachments on the deposited
  amount don't affect those already allocated).
- ✅ **CPC Art. 303**: the debtor may ask قاضي التنفيذ مستعجلاً to **fix an amount to deposit** with the court
  treasury — same effect.
- ✅ **CPC Art. 336**: the garnished third party keeps paying interest and can pay despite the attachment,
  **into the court treasury**.

---

# 4. The cheque as a collection weapon

`As of: 2026-10-28`

**Cross-ref first:** `04-practical-operations-egypt.md` §7.2 verifies the clearing/discipline mechanics of
paying by cheque. This section adds the collection side. All Commercial Code texts below come from the
consolidated alberonsy text (last amendment 19 February 2018).

## 4.1 The basics that change collection strategy

- ✅ **Art. 503/1**: a cheque is payable **at sight** — «مستحق الوفاء بمجرد الاطلاع» — any contrary statement is
  void. **Art. 503/2** ⭐: a cheque presented **before** its issue date (a post-dated cheque) **must be paid on
  the day of presentation** — except crossed cheques (Art. 515) and government cheques. ⭐ **In Egypt a
  post-dated cheque is not deferrable: the bank pays it on presentation.** An agent repeating "post-dated cheques
  can't be cashed early" is wrong.
- ✅ **Art. 504** (presentation periods, as replaced by **Law 156/2004** — consolidated footnote 3/4): **six
  months** (drawn and payable in Egypt) / **eight months** (drawn abroad); from the cheque's date; clearing-house
  presentation counts.
- ✅ **Art. 506** ⭐: the bank **may not refuse payment even after the presentation period expired** if it holds
  مقابل الوفاء — an "expired cheque" with funds on deposit is still payable money.
- ✅ **Art. 509** ⭐: simultaneous cheques with insufficient funds are paid by **issue-date order**; same booklet,
  same date — **lower number first**; different booklets — **smallest amount first**.
- ✅ **Art. 530**: the bank writes cheque number, bank name and account data on chequebook pages; **accepting the
  periodic account statement (expressly or by 30 days' silence) discharges the bank** — ⭐ dispute a wrong bank
  statement within 30 days or lose the protest.
- ✅ **Art. 62** ⭐: in commercial matters the creditor may demand payment **by cheque if the debt exceeds
  100,000 EGP** (current consolidated wording).

## 4.2 Holder's rights on dishonour

- ✅ **Art. 518**: the holder may recourse against the **drawer, endorsers and other obligors** if presented in
  time and unpaid, **proven by protest (احتجاج) — or by the bank's dated, signed statement on the cheque itself**
  (عوض الاحتجاج) which the bank may not refuse to issue (it may ask for up to the **next working day** to issue
  it); the statement is available as a special form or from the clearing house. ⭐ **In Egyptian practice the
  bank statement on the back of the cheque is the operative dishonour proof** — get it before leaving the bank.
- ✅ **Art. 519**: the holder notifies those who endorsed to him and the drawer of non-payment (Art. 440 rules).
- ✅ **Art. 521**: all obligors are **jointly and severally** liable; the holder may sue them individually or
  together in any order; whoever pays gets the same right (521/3).
- ✅ **Art. 522** ⭐ (what the holder claims): (أ) the unpaid principal; (ب) **interest from the presentation date
  at the Central Bank's dealing rate**; (ج) protest/notification/stamp expenses. (Art. 523 mirrors it for one who
  paid: the amount + interest from payment + his expenses.)
- ✅ **Art. 524**: whoever pays gets the cheque + protest + receipt; an endorser who pays may strike his
  endorsement and later ones.
- ✅ **Art. 525** ⭐⭐: the holder with a protest (or its substitute) may place a **conservatory attachment
  WITHOUT a bond** on the assets of the drawer, any endorser or the avaller, per the CPC's conservatory rules —
  the cheque-holder's day-one freeze right. Combine with §3.1's Art. 210.
- ✅ **Art. 527**: recourse against the **drawer survives even without timely presentation/protest** if the drawer
  had مقابل الوفاء deposited and it stayed there through the presentation period before being dissipated by a
  cause not attributable to him.

## 4.3 Prescription on cheques — Commercial Code Art. 531 (all five paragraphs verified)

✅ **Art. 531**:
1. recourse of the holder against **drawer, endorsers and other obligors**: **one year** from presentation or
   from expiry of the presentation period;
2. the holder's claim against the **drawee (the bank)**: **three years**;
3. recourse **among obligors who paid**: **one year** from the day of payment or of being judicially demanded;
4. filing the suit **interrupts** the period — it runs again from the **last act** in the suit;
5. **no prescription** where a judgment established the debt or the debtor **acknowledged it by a standalone
   document with renewal effect**;
6. interruption/suspension follow the **Civil Code** rules.
✅ **Art. 532** ⭐: even after prescription, the holder may claim from the drawer who **never provided مقابل
الوفاء or withdrew it**, and from any endorser unjustly enriched, restitution of what they unjustly received.

## 4.4 The criminal route — Commercial Code Art. 534 (and its neighbourhood)

✅ **Art. 534 full text** verified twice: in the consolidated code text, and quoted verbatim in the Supreme
Constitutional Court judgment PDF (manshurat file 75777, downloaded and text-extracted 2026-10-28):

1. **Imprisonment and/or a fine up to 50,000 EGP** for whoever **intentionally**: (أ) issues a cheque with **no
   payable consideration**; (ب) withdraws all/part of the balance or disposes of it after issuing the cheque so
   the remainder fails the cheque's value; (ج) orders the drawee **not to pay** outside the legally permitted
   cases; (د) drafts or signs the cheque in bad faith so it cannot be paid, or endorses it defectively.
2. Same penalty for whoever **hands over a cheque to another** — by endorsement or as payable-to-bearer —
   **knowing** it has no payable consideration or is unpayable.
3. **Recidivism within five years** of a final conviction for any of these → imprisonment **and** a fine up to
   **100,000 EGP**.
4. ⭐ **Settlement (صلح) with the victim extinguishes the criminal case — even one filed by الادعاء المباشر** —
   and the prosecution orders stopping execution of the sentence if the صلح happens during execution, even after
   the judgment became final.

✅ **Neighbourhood articles** (all read in the consolidated text):
- **Art. 533**: bank-employee offences (false statement about مقابل الوفاء, bad-faith refusal to pay a covered
  cheque without valid objection, refusing to issue the Art. 518 statement, issuing a defective chequebook) —
  fine **3,000–10,000 EGP**, **the bank is jointly liable** for the fine.
- **Art. 535**: the bad-faith beneficiary who collects a non-funded cheque — fine up to 1,000 EGP.
- **Art. 536**: whoever **falsely claims forgery** of a cheque and a final judgment rejects the claim —
  imprisonment and/or a fine up to **half the cheque's value**. (Myth note: corrections table #5.)
- **Art. 537**: on conviction the court may order publication of the judgment at the convict's expense in the
  Chambers-of-Commerce federation's journal; **on recidivism the court may withdraw his chequebook and bar new
  ones**, notified by the prosecution to all banks.
- **Art. 538**: extraterritorial application for cheques drawn on Egyptian banks.
- **Art. 539** ⭐: the holder who joined the criminal case civilly may claim judgment for **the unpaid part of the
  cheque's value** — the civil claim rides on the criminal case (civil-claim-attached rules apply).

⭐ **Practical sequence for a bounced cheque:** bank presentation → **Art. 518 bank statement on the cheque** →
(and optionally) Art. 525 conservatory attachment without bond → complaint to the prosecution → the criminal case
 pressures settlement → **صلح extinguishes the case (534/4)** → if no settlement: civil claim in the criminal
case (539) or the payment order / civil action. ⚠️ Also: a judgment or the debtor's standalone acknowledgment
stops the 531 clock entirely (531/5).

---

# 5. Interim protection: the conservatory attachments (CPC Book Two, Part Two)

`As of: 2026-10-28`

## 5.1 Conservatory attachment on movables — Arts. 316–324

✅ **Art. 316**: the creditor may attach his debtor's movables where: (1) he holds a **bill of exchange or
promissory note bearing a trader-debtor's signature**; or (2) in **every case where he fears losing his security**
(«خشية فوات الضمان»).
✅ **Art. 317**: the **lessor** may attach the tenant's movables for his statutory lien (امتياز المؤجر) —
cross-ref `05-tenancy-egypt.md`.
✅ **Art. 319**: conditions — the right must be **established and due**; absent an executory instrument or a
necessarily-enforced judgment, or where the debt is unquantified, the creditor applies to **قاضي التنفيذ** for
authorisation and (for unquantified debts) a temporary quantification — decided within **three days at most**.
✅ **Art. 320**: the attachment must be **served within eight days** or it is **as if it never was**; where the
attachment issued by قاضي التنفيذ's order, the creditor must file the **validity suit (دعوى صحة الحجز) within
eight days**. Once validity is judged, the sale follows the executive-track rules.
⚠️ Arts. 318, 321–324 (multi-creditor priority before the sale, the audit/تفريغ procedure) verified in concept in
the full text read; quote them only after a dedicated re-read (backlog).

## 5.2 Garnishment — حجز ما للمدين لدى الغير — Arts. 325–352 ⭐

✅ **Art. 325** (the gate): any creditor with an **established, due** debt may attach what his debtor holds **with
third parties** — movables **or debts**, even **deferred or conditional** ones; the attachment reaches any debt
that arises for the debtor in the garnishee's hands **until the تقرير**, unless it was created by a standalone
document.
✅ **Art. 326**: the attaching creditor may add to his claim **one year's interest** (not yet accrued) plus
expenses capped at a fraction of the debt — ⚠️ figures stale (corrections #10).
✅ **Art. 328**: **no prior notice to the debtor** is needed; the attachment proceeds by the bailiff's paper
served **on the garnishee (المحجوز لديه)** with the statutory data.
✅ **Art. 331**: multiple branches — the attachment produces effect only for the branch named.
✅ **Art. 332** ⭐: the attachment must be **notified to the creditor's own debtor (المحجوز عليه) within eight
days** of serving the garnishee — **else the attachment is as if it never was**.
✅ **Art. 333**: where the attachment issued by **قاضي التنفيذ's order**, the creditor must file the **validity
suit within eight days** (joined with a pending debt suit).
✅ **Art. 335**: the **creditor's own debtor (المحجوز عليه)** may sue to lift the attachment before his own
قاضي التنفيذ; notifying the garnishee stops the garnishee paying the creditor until the suit is decided.
✅ **Arts. 336–337**: attachment doesn't stop interest; payment happens **into the court treasury**; deposits stay
attached, and the clerk notifies the parties within three days.
✅ **Art. 338** ⭐: the garnishee must **pay the creditor's own debtor the non-attachable portion** (e.g. the
protected maintenance/necessities share) **without needing a judgment**.
✅ **Art. 339**: the garnishee must make a **تقرير (declaration)** of what he owes within **fifteen days** of
service — detailing the debt, its cause, whether discharged, all attachments on hand, with supporting documents;
holding movables requires a detailed list; **not owing the creditor's debtor doesn't excuse the declaration**.
✅ **Art. 340**: state bodies/public institutions/companies issue the creditor a **certificate that substitutes
for the تقرير**.
✅ **Art. 341**: garnishee's death/incapacity/loss of quality → serve the heirs; 15-day declaration.
✅ **Art. 342**: disputes over the declaration → قاضي التنفيذ.
✅ **Art. 343** ⭐: no declaration, false declaration, or hidden documents → judgment against the garnishee
**for the full attached amount** in favour of the creditor holding a سند تنفيذي, plus costs and compensation.
✅ **Art. 344**: within **fifteen days of the declaration** the garnishee pays the creditor what he admitted —
once the creditor's right is executory and the **Art. 285 procedure** (8-day إعلان العزم) was observed.
✅ **Art. 345**: the garnishee deducts expenses the judge quantifies.
✅ **Art. 346**: if nothing was paid or deposited, the creditor **executes on the garnishee's own assets** with
his سند تنفيذي + certified copy of the declaration.
✅ **Art. 347–348**: attached goods are sold without a new attachment; a **not-yet-due debt** is sold per Art. 400,
or the creditor may have the debt **assigned to himself** (a presumption of assignment) against both debtors.
✅ **Art. 349**: a **creditor who is himself his debtor's creditor** may attach **under his own hand** (الحجز تحت
يد نفسه) with notice to his debtor; 8-day validity suit if by the judge's order.
✅ **Art. 350** ⭐⭐: attachments on **state bodies, local units, public institutions and their companies** last
**three years only** — the creditor must serve a **renewal notice (باستبقاء الحجز)** within the period and repeat
every three years, **or the attachment is as if it never was, whatever procedures/agreements/judgments happened**.
⭐ This is the trap that silently kills garnishments on state-affiliated employers and payers.
✅ **Art. 351**: قاضي التنفيذ may authorise the creditor's own debtor to collect from the garnishee despite the
attachment where: the attachment had no executory instrument/judgment/order; or the Art. 332/333 notices/suits
were missed; or a deposit-and-allocation happened (Arts. 302).
✅ **Art. 352**: the garnishee who dissipates attached securities/movables suffers the penalty of **Art. 341 Penal
Code (التبديد)**.

## 5.3 What cannot be attached at all — CPC Arts. 305–309 ⭐

✅ **Art. 305**: the debtor's, his wife's, and relatives/in-laws living in one household's **beds, clothing, and a
month's food** — no attachment.
✅ **Art. 306**: the debtor's **books, tools and trade equipment**, and **female livestock necessary for the
family's subsistence** + their month's feed — attachable **only** for their own price, maintenance costs, or a
court-ordered maintenance debt.
✅ **Art. 307**: court-awarded **temporary maintenance** sums and monies gifted/willed for maintenance — no
attachment **except up to one quarter** for a court-ordered maintenance debt.
✅ **Art. 308**: gifted/willed assets **with a no-attachment condition** — protected from creditors whose debt
**pre-dates** the gift/will (except maintenance debts, same quarter rule).
✅ **Art. 309**: **wages and salaries — one quarter only** (§6.2).
✅ **Art. 310**: attached harvests deliverable to the State/public bodies — the attachment transfers to the **price**.

---

# 6. The limitation clocks (التقادم)

`As of: 2026-10-28`

## 6.1 Civil

- ✅ **CC Art. 374**: personal rights prescribe in **fifteen years** from due date, unless a special text says
  otherwise (mohamedhamadlaw; carried in 02/07 chains).
- ✅ **CC Art. 375**: **periodic rights** (rents, wages, pensions, interest due at set intervals and the like)
  prescribe in **five years** — even if the debtor acknowledged them repeatedly.
- ✅ **CC Art. 382**: prescription **does not run** whenever an **obstacle** makes it impossible for the creditor
  to demand his right (the mohamedhamadlaw article page + practitioner summaries agree) — e.g. between principal
  and agent. ❌ It is **not** a judgment-lapse rule (corrections #8).
- ✅ **CC Art. 385/2**: prescription is **interrupted by the debtor's acknowledgment** (mohamedhamadlaw) — ⭐ a
  signed "I owe you X" letter or payment plan restarts the 15-year clock. (Interruption also by suit and other
  CC/CPC routes; renewal requires a new cause — ⚠️ Art. 387's exact mechanics not re-verified this pass.)

## 6.2 Commercial — Commercial Code Art. 68 ⭐

✅ **Art. 68 full text** (consolidated alberonsy text): claims arising from **merchants' obligations towards each
other in their commercial dealings** prescribe in **seven years** from due date unless a special text says
otherwise — **and final judgments in those claims lapse after ten years**.
⭐ Two clocks in one article: **7 years to sue**, then **10 years to enforce**. An SME creditor who waits
comfortably past year seven loses the claim; a creditor with judgment who sleeps past year ten loses the
execution.

## 6.3 Negotiable instruments

✅ Cheque: **Art. 531** (1 year / 3 years / 1 year — §4.3) — its own shorter family of clocks, with the
acknowledgment/judgment suspension (531/5) and the post-prescription enrichment claim (532).
⚠️ Bill of exchange / promissory note prescription (Commercial Code Book Five — the corresponding articles) was
**not re-read this pass**; verify before citing numbers (backlog).

## 6.4 The criminal clock (for cheque crimes)

✅ **CPCrim Law 150/1950 Art. 15** (as amended by Law 340/1952): the criminal case lapses — **felonies: ten years**
from the crime; **misdemeanours: three years**; infractions: one year (menarights PDF full text; alberonsy;
fahmqanon). ✅ **Art. 17** = interruption by investigative/prosecution acts (manshurat node 14676).
⚠️ **Law 174/2025** (new CPCrim, Gazette 45 bis (د) 12 Nov 2025) restates the lapse rule in its **Art. 17** — but
its application is **deferred to 1 October 2027 by Law 160/2026**; until then 150/1950's Art. 15 governs (§7 of
the `egy-criminal-procedure` skill carries the same finding).

## 6.5 The clocks table ⭐

| Debt situation | Clock | Source |
|---|---|---|
| Civil personal debt | **15 years** from due date | CC Art. 374 ✅ |
| Periodic rights (rent/wage/pension instalments, interest) | **5 years** | CC Art. 375 ✅ |
| Merchant-vs-merchant commercial claim | **7 years** from due date | Comm. Code Art. 68 ✅ |
| Final judgment (commercial claims) | lapses after **10 years** | Comm. Code Art. 68 ✅ |
| Cheque recourse vs drawer/endorser/obligors | **1 year** from presentation/expiry | Comm. Code Art. 531/1 ✅ |
| Cheque claim vs the drawee bank | **3 years** | Comm. Code Art. 531/2 ✅ |
| Cheque obligors among themselves | **1 year** from payment/judicial demand | Comm. Code Art. 531/3 ✅ |
| Cheque crime prosecution | **3 years** (misdemeanour) | CPCrim 150/1950 Art. 15 ✅ |
| Renewal | debtor's **acknowledgment** restarts the clock | CC Art. 385/2 ✅ |
| Civil judgment lapse | **not verified** | 🟡 backlog |

---

# 7. The execution book — how money is actually taken (CPC Book Two)

`As of: 2026-10-28`

## 7.1 The machinery — Arts. 274–279

✅ **Art. 274**: execution proceeds **under the supervision of قاضي التنفيذ**, appointed at each primary court;
assisted by sufficient bailiffs; before him the primary-court procedures apply unless the law says otherwise.
✅ **Art. 275** ⭐: **قاضي التنفيذ alone** decides all **material and temporal execution disputes at any value**,
and issues the execution decisions and orders — deciding temporal disputes as a judge of urgent matters.
✅ **Art. 279**: execution is carried by **معاوني التنفيذ** (execution assistants = the bailiffs' administration);
refusal to act → petition to the **إدارة التنفيذ's director**; resistance/assault → the assistant may request
police/local-authority assistance.

## 7.2 The سند تنفيذي — Arts. 280–286 ⭐ the cornerstones

✅ **Art. 280**: no forced execution except by an **سند تنفيذي** claiming an established, quantified, due right.
**The executory instruments are: judgments, orders (الأوامر), notarised documents (المحررات الموثقة), and
certified settlement minutes — plus any other instruments the law grants the quality.** Execution uses a copy
stamped with the execution formula: «على الجهة التي يناط بها التنفيذ أن تبادر إليه متى طلب منها وعلى السلطات
المختصة أن تعين على إجرائه ولو باستعمال القوة متى طلب إليها ذلك».
✅ **Art. 281**: execution must be preceded by **service of the سند تنفيذي on the debtor personally or at his
original domicile** — else void; the service must contain the payment order, what's demanded, and the creditor's
chosen domicile at the execution court's town; executing a notarial credit-deal includes a statement of the
debtor's account from the creditor's commercial books; **execution starts at least one day after the service**.
✅ **Art. 282**: the bailiff receiving service or executing **must take the money if offered, and give the
discharge receipt, without a special mandate**.
✅ **Art. 283**: whoever lawfully or contractually replaced the creditor succeeds to the execution steps taken.
✅ **Art. 284**: the debtor's death/loss of capacity/disappearance — execution may not proceed against the heirs
before **eight days** from serving them, and jointly within **three months** at the last domicile.
✅ **Art. 285**: a **third party** may not be made to pay nor be compelled to pay the سند تنفيذي's demand until
the debtor is notified of the **intent to execute at least eight days beforehand** (إعلان العزم).

## 7.3 Accelerated enforcement — Arts. 287–289

✅ **Art. 287**: judgments are not enforced while appealable unless accelerated enforcement is **prescribed by law
or ordered by the judgment** — but **interim protective measures are always allowed**.
✅ **Art. 288**: accelerated enforcement **without a bond, by law**, for judgments in urgent-matters cases and for
**orammat on petitions**; with a bond for commercial-case judgments unless the law says otherwise.
✅ **Art. 289**: (verified in the full text read; mechanics of bond security) — ⚠️ quote after re-read if
specific.

## 7.4 Execution on movables — Arts. 353–397

✅ The highlights (all read in the consolidated text):
- **Art. 353**: the attachment is made by a **محضر drafted at the place of signing** — else void — naming the
  سند تنفيذي, the creditor's chosen domicile, obstacles met, the attached items in detail with approximate value,
  **and the sale's date/hour/place fixed on the spot**; the debtor signs if present (signature ≠ consent).
- **Art. 354**: standing crops attachable only within **45 days** before maturity.
- **Art. 355**: the attachment may not be signed **in the petitioner's presence**.
- **Art. 356**: breaking doors/locks requires a **judicial police officer present who signs** the محضر; a body
  search needs **prior قاضي التنفيذ permission**.
- **Art. 361**: items become attached **by their listing in the محضر even without a guard**.
- **Art. 363**: notices are posted on the place's door and on the local administration board — with the sale date.
- **Art. 364–368**: a **guard** is appointed (the debtor preferred unless dissipation is feared; the guard may not
  use the assets; his fee is a privileged expense set by قاضي التنفيذ).
- **Art. 374** ⭐: a creditor **without a سند تنفيذي** may attach **the sale proceeds under the bailiff's hand**
  without needing a validity judgment.
- **Art. 375** ⭐: the attachment is **as if it never was if the sale is not completed within three months** of
  signing (extensions ≤3 months by agreement or judge's order).
- **Art. 376**: sale only **≥8 days after serving the محضر copy**, and ≥1 day after the posting/publication;
  perishables → immediate sale.
- **Art. 378**: value above the statutory figure → **newspaper publication** before the sale (⚠️ figure stale —
  corrections #11).
- **Art. 384**: public auction, called by the bailiff, **with immediate payment**.
- **Art. 385–386**: gold/silver may not sell below intrinsic value (held in the treasury otherwise); jewels'
  auction extends and may finally sell below valuation.
- **Art. 389** ⭐: the winning bidder who doesn't pay immediately → **resale on his account at any price**, and
  the **محضر البيع is an سند تنفيذي for the price difference**; the bailiff himself is liable if he fails to
  collect or re-sell.
- **Art. 391**: the sale محضر records everything, the final price, and the buyer's name and signature.

## 7.5 Securities, listed revenues, shares — Arts. 398–400

✅ **Art. 398**: bearer/endorsable shares and bonds attach **as movables**.
✅ **Art. 399**: annuity revenues, **nominal shares**, accrued profit shares in legal persons, and will-rights
attach **as garnishment (لدى الغير)** — with their fruits and interest up to the sale day.
✅ **Art. 400**: they are sold **through a bank, broker or dealer appointed by قاضي التنفيذ**, which sets the
notice procedures.

## 7.6 Execution on real property — Arts. 401–428 (+ 459–466) ⭐

✅ The chain (all read; the strongest single collection asset in Egypt is a registered receivable against land):
- **Art. 401**: execution opens with a **notice of divestment (تنبيه بنزع ملكية العقار)** served on the debtor
  personally/at domicile — stating the سند, the debt, a warning that non-payment registers the notice and sells
  the property, and the property's full description; the creditor may obtain an order licensing the bailiff to
  enter the property for description.
- **Art. 402**: the notice is **registered at every الشهر العقاري office** in whose district the properties lie.
- **Art. 403**: a prior registered notice is annotated on the margin.
- **Art. 404** ⭐: **registration makes the property attached**.
- **Art. 405** ⭐: the debtor's/his possessor's/the real guarantor's **disposals of the property after registration
  do not run against the attaching creditors** (even ordinary ones), nor against the Art. 417 creditors — nor
  against a judgment imposing the sale.
- **Art. 406**: **fruits/revenues attach from the registration date**.
- **Art. 407**: the debtor remains **guardian (حارس)** of the property until sale unless removed.
- **Art. 408** ⭐ (cross-ref 05 §lease rules): leases **with fixed dates** (per Law 25/1968 Art. 15) bind the
  attaching creditors under the code's conditions.
- **Art. 409**: **مخالصات (rent prepayments)** bind if fixed-dated before registration — **otherwise one year
  only**.
- **Art. 410**: dissipating attached fruits/damaging the property triggers the **Penal Code penalties (341/342/361
  chain as referenced by the text)**.
- **Art. 414**: the **sale-conditions list** is drafted within **90 days** of the divestment notice.
- **Art. 415**: the registry supplies the property's documents and a ten-year extraction record.
- **Art. 417** ⭐: mortgagees, holders of registered real rights, and the prosecution are **notified and become
  parties** to the execution procedure.
- **Art. 428**: the **sale notice** is published **15–30 days** before the auction.
- **Arts. 459–466**: the special sales regime (bankrupt's property, interdicted property, absent persons' property)
  runs on a filed sale-conditions list with objections from mortgagees/rights-holders/prosecution.

## 7.7 Distribution of the proceeds — Arts. 469–488

✅ **Art. 470**: where the proceeds cover everyone, the holder pays each creditor **upon presenting his سند
تنفيذي** or with the debtor's consent.
✅ **Art. 471**: proceeds insufficient for all creditors → the holder **deposits them in the court treasury**
with a signed attachment schedule.
✅ **Art. 472**: refusal to deposit → قاضي التنفيذ forces it with a deadline, then **forced execution on the
refuser's own assets**.
✅ **Art. 473**: absent agreement with the debtor and possessor within **fifteen days** of the deposit, the clerk
refers the matter to **إدارة التنفيذ** within three days to distribute.
✅ **Art. 474**: the administration drafts a **provisional distribution list** within fifteen days and the clerk
serves the debtor, possessor, attaching creditors and parties.
(✅ Arts. 475–478 read in the full text — objections and the هيئة الإعلام procedures; re-read before quoting.)
✅ **Art. 479**: unresolved objections → the director records them and refers to **قاضي التنفيذ who decides
immediately**; no new objections after that session.
✅ **Art. 480**: the distribution ruling is appealable **only where the disputed amount exceeds the statutory
figure**, whatever the creditor's right or the proceeds' value — appeal window **ten days** (⚠️ the displayed
figure is subject to the Law 157/2024 chain — corrections #9).
✅ **Art. 488**: on refusal of an offered payment in kind, cash is deposited in the treasury by the next day and
the creditor served within three days; non-cash → the debtor may ask the مستعجل judge to license deposit
elsewhere or custody.

## 7.8 Debtor-side protections inside execution

✅ **Arts. 302/303**: substitute deposit lifts the attachment from the assets (§3.4).
✅ **Art. 311**: the debtor, the judges who handled the execution, and the lawyers may not bid — the sale is void.
✅ **Art. 312**: on an execution obstacle, the bailiff may pause or proceed on reserve basis and must bring the
parties before قاضي التنفيذ (even within an hour, at home if needed); execution cannot complete before the
judge's ruling; a further objection doesn't stop execution unless the judge orders it.
✅ **Arts. 305–309** protect the household's necessities and the wage quarter (§5.3, §6.2).

---

# 8. Wages, pensions and the family interplay

`As of: 2026-10-28`

## 8.1 The wage rule

✅ **CPC Art. 309** (full text quoted in corrections #2): wages/salaries attachable **up to one quarter**; in
competition, **half of that quarter** goes to the court-ordered maintenance creditor, the other half to the rest.

## 8.2 The maintenance priority

⚠️/✅ **Law 1/2000 Art. 76** — the maintenance creditor's own garnishment priority — is verified in
`07-family-law-egypt.md` (Law 1/2000). Cross-ref it; do not restate its wording here. The interplay with Art. 309
follows the special statute for maintenance debts — say that, and read 07 before quoting figures.

## 8.3 Practical garnishment notes for the creditor

- ✅ Garnish via **Art. 325** (the employer = المحجوز لديه) **or** via **Art. 210's combo** with أمر الأداء.
- ✅ The employer must **تقرير within 15 days** (339) or get a state-body certificate (340); no/false declaration
  → judgment for the full amount (343) ⭐.
- ✅ Payment to the creditor requires the creditor's right to be **executory** + the 8-day **إعلان العزم**
  (Arts. 285, 344).
- ✅ **State-affiliated employers: renew every three years** (Art. 350) ⭐.
- 🟡 **Pensions** (المعاشات): the social-insurance statute's own garnishment rules were not researched here —
  verify before claiming any pension-garnishment percentage (backlog).

---

# 9. What the new CPCrim 174/2025 will change (and what it won't)

`As of: 2026-10-28`

✅ Law 174/2025 was promulgated 12 November 2025 and is **not applied until 1 October 2027** (Law 160/2026
postponed Art. 6 of the issuing provisions — merghanylaw; youm7 gazette report). For debt recovery the new code
matters only for the **criminal-lapse renumbering** (Art. 17 restating Art. 15's rule — §6.4). The CPC's civil
execution machinery (Arts. 274+ etc.) is untouched by it. **No debt-collection rule should be cited from the new
code before 2027.**

---

# 10. Sources

**Primary / full-text mirrors used for article text:**

- **CPC Law 13/1968 full text** — lawhub.info, `https://lawhub.info/eg/?p=11332` (6,269 lines; retrieved in full;
  amendment notes visible incl. Laws 23/1992, 81/1996, 191/2020, 157/2024).
- **CPC Law 13/1968** — Arabic Wikisource raw wikitext (`ar.wikisource.org`, page «قانون 13 لسنة 1968 بإصدار قانون
  المرافعات المدنية والتجارية/_مصر»; 184KB; mixes the code body with the old-code fragments retained by Art. 1 —
  used only for the 13/1968 blocks identified by the code's own headings).
- **Commercial Code Law 17/1999, consolidated to 19 Feb 2018** — alberonsy.com
  (`https://alberonsy.com/قانون-التجارة-17-لسنة-1999-وتعديلاته/`), with amendment footnotes (1)–(8) incl.
  **Law 156/2004** replacing Arts. 504's and 531's phrases.
- **Supreme Constitutional Court judgment quoting Art. 534 verbatim** — manshurat.org file 75777
  (`https://manshurat.org/file/75777/download?token=3dL0QRN9`), downloaded and pdftotext-extracted locally
  2026-10-28; also carries the الشيكات البريدية paragraphs (1/3/4) holding and the Law 179/2008 origin of the
  para-2/3 structure.
- **CPCrim Law 150/1950 full text** — menarights.org PDF (`menarights.org/wp-content/uploads/2026/05/
  EGY_code-of-criminal-procedure_1950_AR.pdf`) and manshurat.org node 14676 (Art. 17 interruption).
- **Civil Code articles** — mohamedhamadlaw.com per-article pages (Arts. 374/375/382/385).

**Secondary (corroboration, never article text):**

- eastlaws.com — CPCrim articles; Cassation 4135/94 (Art. 532's عدم الاحتجاج rule context).
- merghanylaw.com — the Law 160/2026 deferral of Law 174/2025 to 1 October 2027; youm7 (gazette publication) and
  presidency.eg (promulgation).
- Practitioner pages (alrayacls.net أوامر الأداء study; egy-/facebook lawyer pages; mohamymasr; soutalomma;
  benisuef.gov.eg) — used to locate texts and to record the myths they carry (corrections #1, #3, #5).
- alhasswalawfirm.com (2026 bounced-cheque explainer) — corroboration of Art. 534 mechanics.

**Judgments:**

- SCC judgment (file 75777) — Art. 534 verbatim + postal-cheque holding.
- Cassation 4135/94 — no recourse claim without protest (Art. 532) — verified via eastlaws snippet only; full
  text in backlog.

# 11. Cross-references

- **Cheque clearing, paying by cheque safely, evidence discipline:** `04-practical-operations-egypt.md` §7.2.
- **Leases surviving an attached property (Arts. 408–409) + fixed dates:** `05-tenancy-egypt.md` (Law 25/1968
  Art. 15) — and §9.2 of 05 for the stale-pecuniary-figures warning that applies here too.
- **Maintenance (نفقة) collection and its priority garnishment:** `07-family-law-egypt.md` (Law 1/2000 Art. 76).
- **Court structure, tiers, and filing mechanics:** `03-employment-courts-aml-banking.md` (threshold figures
  stale — corrections #9) and the skills `egy-court-filing-guide` / `egy-legal-notice`.
- **Criminal procedure (the complaint route, الادعاء المباشر, the new code's deferral):**
  `egy-criminal-procedure` skill and corpus 06.
- **Skill layer:** the non-lawyer-facing skill for this topic is `egy-debt-recovery` (+ `-ar` twin).

# 12. Research backlog (UNVERIFIED items → carry to roadmap.md)

1. 🟡 **Operative CPC pecuniary thresholds after the 191/2020 + 157/2024 chain** (Arts. 41, 42/1, 43, 47/1, 248,
   480) — retrieve both amending laws' gazette texts and compute the current figures.
2. 🟡 **A civil-judgment lapse rule** — searched ("سقوط الأحكام النهائية المدنية") — found only the commercial
   rule (Art. 68) and the **suspension** rule (CC Art. 382). Either locate the rule (some literature claims a
   lapse) or convert to a ❌ finding with the search trail.
3. 🟡 **Bill-of-exchange / promissory-note prescription articles** (Commercial Code Book Five) — not re-read this
   pass; the cheque file (531) is verified.
4. 🟡 **Art. 326's current cap figures** (garnishment interest/expenses) and **Art. 378's newspaper-notice
   threshold** — the displayed figures are stale; find the amending laws or confirm the base text still governs.
5. 🟡 **Bankruptcy (الإفلاس) instrument number** — the regime exists; not verified here; do not cite a number
   until read.
6. 🟡 **Pension (معاشات) garnishment rules** under the social-insurance statutes.
7. 🟡 **Tax and social-insurance arrears collection** (state-execution tracks) — out of scope here; research
   before advising on any state-claim garnishment.
8. 🟡 **CPC Arts. 318, 321–324, 475–478, 289** — read in the full text but not separately re-quoted; re-read
   before citing specifics.
9. 🟡 **Cassation 4135/94 ق full text** (no-protest recourse rule) — secondary carry only.
10. 🟡 **أوامر الأداء Art. 210 footnote (*)** — the amendment note origin (probably Law 23/1992) not confirmed.
11. 🟡 **The orammat-on-petitions amendment note (*)** on Art. 197 (Law 23/1992 context) — confirm before citing
    the تظلم route's current shape.
12. 🟡 **Law 174/2025's cheque-relevant provisions** (renumbering of the criminal-lapse rule; any new
    dishonour-cheque rules) — verify when the code enters force 1 Oct 2027.

## Verification snapshot (end of file)

- Instruments verified with full or operative text: **CPC 13/1968** (✅ the order blocks 194–219, the execution
  book 274–466, distribution 469–488 — two independent full-text mirrors), **Commercial Code 17/1999 consolidated**
  (✅ Arts. 56–70, 503–546 incl. Art. 534 verbatim ×2), **CPCrim 150/1950 Arts. 15/17** (✅), **Law 174/2025 +
  Law 160/2026 deferral** (✅), **CC Arts. 374/375/382/385/226** (✅ per-page or carried chains).
- Overturned claims on record: **12** (Corrections table).
- UNVERIFIED carried to backlog: **12**.
- Marker counts at commit: ✅ on **60** lines; ⚠️ on **22**; ❌ on **8** (findings + myth table); 🟡 on **15**
  (mostly backlog items and their in-text pointers).
