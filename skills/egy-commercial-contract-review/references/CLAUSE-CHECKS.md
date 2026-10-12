# Clause Checks — Egyptian commercial contracts

Work top to bottom. For each: what it says, what Egyptian law does, the risk,
the fix, the fallback. Article numbers are verified against
`research/egyptian-corpus/01-commercial-corporate-contract.md` — if a clause
depends on something not listed here, say so in section 5 of the output rather
than guessing.

---

## 1. Parties and capacity

**Check**
- Legal names match commercial-registry (السجل التجاري) entries exactly. Get the
  extract, not the trading name.
- Signatory authority. A director who is not, or whose authority has lapsed,
  creates an avoidable dispute.
- Any party under interdiction (الحجر)? Civil Code **Art. 114** — acts **after
  registration** of an interdiction order are **void**; acts before are void only
  if the condition was notorious or the other party knew.
- Minority. **Arts. 110–112** — under 18; acts are void, annulable or valid
  depending on whether purely beneficial, purely prejudicial, or mixed.
- Is the counterparty actually a company that exists? A trading name is not a
  company.

**Risk:** signing against a non-existent or mis-described party is the cheapest
defect to fix and the most expensive to discover later.

---

## 2. Subject matter and scope

**Check**
- Is the obligation **determinate enough**? Civil Code Arts. 131–137 on subject
  matter and cause.
- **Art. 95 — widely under-appreciated.** If the parties have agreed on all the
  essential matters (المسائل الجوهرية) and reserved only detail matters for
  later, **without stipulating that the contract fails for want of agreement,
  the contract is deemed concluded**, and the court decides the reserved points
  by the nature of the transaction, the law, custom and equity.
  → This cuts both ways. If you are a supplier and scope feels open, you may be
  bound to work the reserved points could define. Say so.
- **Art. 148(2)** — the contract embraces not only what it says but what are among
  its requisites (مستلزماته) according to law, custom and equity. The most useful
  drafting article in the Code, and it cuts both ways.
- Service levels, acceptance criteria, deliverables. If there is no acceptance
  mechanism, there is no enforceable standard.

**Fix:** attach a specification, and state who accepts and within how long.

---

## 3. Price, currency and payment

**Check**
- **Currency.** EGP or foreign? If foreign: which rate, which date, who bears FX
  movement, and is there an Egyptian conversion/transfer issue. Do not leave this
  implicit.
- **Art. 226 — default interest:** **4% p.a. in civil matters, 5% p.a. in
  commercial matters**, running from the date of the judicial claim unless the
  agreement or commercial custom sets another date.
- **Art. 227(1) — the ceiling you cannot draft around.** Whatever rate the parties
  agree, **anything above the statutory price is reduced to 7%**, with restitution
  of the excess. A clause promising 15% is not invalid — it is **silently cut to
  7%**. Drafters over-promise here constantly without knowing.
- **Art. 232** — no interest on capitalised interest; total interest may never
  exceed principal, save where commercial custom provides otherwise.
- **Art. 343** — if costs, interest and principal are all owed, payments apply
  **first to costs, then interest, then principal**. Know this before you negotiate
  a "the first payment clears everything" clause.
- **Art. 344–345** — where several debts of the same kind exist, the debtor may
  designate; failing designation the court applies to the least burdensome, and
  between equally burdensome debts, the creditor elects.
- **Art. 272** — an undertaking payable "when able" gets a reasonable date fixed
  by the judge, judged by the debtor's means and the care of a prudent person.
  Never draft an open-ended "when able" payment obligation.

**Fix:** state a currency, a rate mechanism, a due date, and an interest rate that
will survive Art. 227.

---

## 4. Liquidated damages (غرامة تأخير / شرط جزائي)

This is where Egyptian drafting most often over-promises.

**Check**
- **Art. 224 — agreed compensation is not due if the debtor proves the creditor
  suffered no loss**, and the court may reduce it if grossly overstated or partly
  performed. Agreements to the contrary are **void**.
  → A penalty clause is **not an automatic payment**. It is an evidentiary
  starting point the other side defeats by showing no loss.
- **Art. 225 — the ceiling.** Loss exceeding the agreed figure **cannot be
  claimed unless the debtor committed fraud or gross fault**.
  → So a penalty clause is a **ceiling on ordinary claims, not a floor.** If the
  client wants to claim more than the penalty for a bad breach, they need proof of
  fraud or gross fault.
- Are the amounts distinguishable from actual performance obligations? A penalty
  that simply restates the obligation adds nothing.

**Drafting note:** where a penalty is genuinely calibrated to anticipated loss,
say so in the recitals. It does not bind the court, but it supports the
Art. 224 argument that the figure is evidenced rather than arbitrary.

**Fix:** keep the figure defensible; consider a separate, expressly non-exclusive
remedy for fraud and gross fault so Art. 225's exception is not lost by
construction.

---

## 5. Delivery, acceptance, title and risk

**Check**
- **Art. 347** — delivery in a specific thing at the place where it was when the
  obligation arose; otherwise at the debtor's domicile at performance, or the
  place of business if the obligation relates to it.
- Incoterms? If used, name the **edition and exact term** (Incoterms 2020 vs
  2010). Vague references are a recurring dispute source.
- **Art. 246 — right of retention (الحبس).** A person obliged to deliver something
  **may withhold it** until the creditor tenders the connected counter-performance
  or provides adequate security. If your client holds goods against unpaid sums,
  this is the provision — and it also means a client cannot simply demand delivery
  while withholding payment.
- When does risk pass? On delivery, on acceptance, or on signature? Name it.
- **Art. 146** — obligations and personal rights attached to a thing pass to the
  **special successor** (a purchaser) at the moment the thing passes, if they are
  among its requisites **and the purchaser knew of them at the time**. The
  knowledge condition matters for title and for IP/licence terms.

**Risk:** unaddressed risk transfer in a goods contract is where margin quietly
disappears.

---

## 6. Force majeure

**Check**
- ⚠️ **Egypt has no general statutory force majeure regime.** The clause operates
  entirely on its own wording. Say this in the review rather than assuming a
  background rule.
- Does it list the events, or leave them to a general standard? A general standard
  gets litigated.
- **Notice deadline** — to whom, how, within what time after becoming aware.
- **Mitigation** — is the obliged party required to mitigate, and what happens if
  they do not.
- **Long-stop termination right** — without one, a force-majeure event can suspend
  the contract indefinitely and lock up both sides.
- **Prepayment** — what happens to sums already paid. The default answer is
  usually that nothing happens until the contract ends, which can strand a large
  prepayment.
- Payment obligations are usually carved out of force majeure. Say whether they
  are.

**Risk:** **High** where the contract has a long tail of delivery risk and no
long-stop. This is the single most common finding in Egyptian commercial
contracts reviewed from outside.

---

## 7. Conditions and termination

**Check**
- **Arts. 265–270** on suspensive and resolutive conditions.
  - **Art. 266** — an obligation conditional on an impossible condition, or one
    contrary to morals or public order, **does not exist**.
  - **Art. 267** — a suspensive condition whose occurrence depends **solely on the
    promisor's will** is treated as non-existent. Draft a real condition.
  - **Art. 270** — conditions operate **retroactively** to when the obligation
    arose, unless the parties' will or the contract's nature shows otherwise.
- **Art. 273** — the **debtor's** term lapses on bankruptcy or insolvency
  declaration, and where his own act weakens special security; but if the
  weakening is not attributable to him, the term does not lapse unless the
  creditor called for top-up.
- **Art. 274** — with a suspensive term, the creditor may demand **security on
  reasonable grounds** where he fears insolvency.
- Termination notice: method, address, cure period, and what happens to work in
  progress and to sums paid.

---

## 8. Liability, indemnity and insurance

**Check**
- Liability cap, and **what is carved out** from it. A cap with no carve-outs is
  a very different contract from a cap with a fraud/gross-negligence/confidentiality
  carve-out.
- Indemnity: is it **Art. 225**-compatible? Drafters routinely write an indemnity
  that reads as a contractual penalty and should be understood against Art. 224
  and Art. 225.
- Excluded liabilities — death/personal injury, fraud, IP infringement — say
  explicitly rather than leaving it to construction.

---

## 9. Confidentiality

**Check**
- Is this genuinely a **commercial** agreement or a civil one? It changes the
  default interest rate (Art. 226) but not much else — the Civil Code governs
  either way.
- Duration, and whether obligations survive termination (they must — say so).
- Permitted disclosures: legal or regulatory compulsion, professional advisers,
  group companies. Define each.
- Return or destruction on termination, with a carve-out for legal retention and
  for **automated backups** (which realistically cannot be purged).
- Remedies for breach — note that a penalty clause for confidentiality breach
  runs into Arts. 224–225 like any other.

**Risk:** confidentiality clauses with no permitted-disclosure carve-out are
routinely breached on day one by ordinary legal requests.

---

## 10. Intellectual property

**Check**
- **IP Law 82/2002** — copyright is Book Three. **Arts. 160–165** on duration:
  author life **plus 50 years**; joint authorship to the death of the last
  surviving author; collective works 50 years from publication where the holder is
  a legal person, otherwise life + 50; **applied art 25 years (Art. 164)**;
  performers **50 years (Art. 166)**.
- **Art. 143** — **moral rights are permanent and not liable to prescription or
  assignment**. **Art. 145** makes any disposal of them **absolutely null and
  void**.
  → So a clause assigning "all rights, including moral rights" is void as to the
  moral-rights element. Assign the financial rights and deal with moral rights
  by waiver-of-exercise or non-assertion, not assignment.
- **Art. 144** — the injunction against circulation requires **fair compensation
  in advance** to the financial-right holder, **or the ruling is void**. Surprising
  condition; do not promise this remedy casually.
- Employment/service context: who owns work product created by a contractor.
- Registering in Egypt (patents, marks) versus relying on unregistered rights.
  Trademark and patent registration particulars are in the corpus.
- Third-party and open-source material in deliverables.

---

## 11. Governing law

**Check**
- Named law, not "its laws". "The laws of Egypt" is workable but leaves the
  question of the **non-statutory** sources open — commercial custom (عرف تجاري)
  matters in Egypt and varies by sector.
- If the deal is mixed civil/commercial, note **Art. 3 Commercial Code** — it
  applies to the **merchant's obligations only**, not the whole contract.
- Art. 1 Civil Code — where there is no text, the judge decides by custom, then by
  principles of Islamic law, then by natural law and equity. That ladder is part
  of Egyptian statutory law and is worth telling a foreign client, because "there
  is no rule" does not mean "the contract governs".

---

## 12. Boilerplate that does not work in Egypt

Flag or rewrite these:

| Boilerplate | Problem |
|---|---|
| "Consequential damages excluded" | Read against **Art. 225** — agreed compensation is not due absent loss, and excess cannot be claimed without fraud or gross fault. The clause is not doing the work an English-law drafter assumes. |
| "No hardship adjustment; contract is absolute" | **Art. 147(2)** allows the judge to reduce an obligation made excessively onerous by exceptional, unforeseeable events, and **voids any agreement to the contrary**. This clause does not exclude judicial revision. It also discloses to the counterparty that the client thinks there may be hardship. |
| "Severability" | Not fatal, but note **Art. 141** — a void contract can be raised **by the court of its own motion** and cannot be cured by ratification. Partial nullity is dealt with at **Arts. 143–144**, where a void or annulable contract carrying the requisites of another valid contract is treated as that other contract. A severability clause cannot save an illegal term. |
| "Entire agreement" | Weakened by **Art. 148(2)** — the contract embraces its requisites according to law, custom and equity, not only its text. |
| "Notice by email" | Weak. **Art. 91** — an expression takes effect when it comes to the addressee's knowledge, and **receipt is presumed, rebuttably**. Notices with consequences should have a delivery mechanism you can prove. |
| "Indemnities capped" | Check against Art. 224 before treating the indemnity as payable on breach. |

---

## Risk rating

| Rating | Meaning |
|---|---|
| **Critical** | Void, unenforceable, or exposes the client to something they cannot price. Walk away or restructure. |
| **High** | Costs real money or a real right, and the current wording loses it. Fix before signing. |
| **Medium** | Ambiguous, or leaves a common dispute unwon. Fix if the counterparty will move; otherwise note it. |
| **Low** | Housekeeping, or a risk the client has consciously accepted. |

Do not inflate. A review where everything is High is a review with no
priorities, and the client will ignore all of it.