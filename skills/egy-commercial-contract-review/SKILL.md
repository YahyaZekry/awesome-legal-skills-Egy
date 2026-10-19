---
name: egy-commercial-contract-review
description: Review, draft and negotiate commercial contracts governed by Egyptian law — NDAs, services, supply, distribution, agency, construction, SaaS, employment-adjacent B2B. Produces a clause-by-clause issue log with Egyptian-law reasoning, redlines, fallbacks and a risk rating. Use when the user asks to review a contract, check a client's contract, redline a deal, compare two versions, or draft an Egyptian-law agreement. Triggers on "Egyptian contract", "contract review", "NDA", "redline", "MSA", "supplier agreement", "مراجعة عقد", "عقد موثق", "اتفاقية سرية".
metadata:
  author: Egypt Edition (Lawve catalog)
  license: CC-BY-4.0
  version: 2026.10.12
---

# Commercial Contract Review — Egyptian Law

Review and draft commercial contracts governed by Egyptian law. The output is a
working issue log with redlines, not a memo about contract law.

**Not legal advice.** This produces a structured starting point for a qualified
Egyptian lawyer to check. Say so once, early, and move on — do not repeat it in
every section.

## The rule that makes this skill worth using

Every legal proposition gets a citation, and the citation comes from the verified
corpus — never from memory. This matters more here than in most jurisdictions,
because **the four most commonly repeated facts about Egyptian contract law are
wrong**. Models reliably get them wrong because they are wrong everywhere else.

| What models say | What the Egyptian statute actually says |
|---|---|
| Egyptian Commercial Code is Law 12/1943 | **Law 17 of 1999.** No Egyptian Commercial Code numbered 12/1943 exists. |
| Egyptian Arbitration Law is Law 34/1988 | **Law 27 of 1994**, Gazette No. 16 bis, 21 April 1994. |
| Egypt's e-signature law is Law 15/2020 | **Law 15 of 2004.** The 2020 instrument is Ministerial Decision 361/2020 amending the *Executive Regulations*. |
| Contract limitation is in the 480s–500s | **Civil Code Arts. 374–388.** Art. 488 is about gifts. |

And the one models get most confidently wrong:

> **Egyptian law has no hardship clause, like English law.**
> Wrong. **Civil Code Art. 147(2)** (نظرية الظروف الطارئة) lets the judge *reduce*
> an obligation that exceptional, unforeseeable events have made excessively
> onerous, and voids any agreement to the contrary. It also disused in practice
> during high-inflation periods — so it is live on the statute book and largely
> unexercised. Say which it is. Never claim the court cannot touch a bad bargain.

Full verified corpus: `research/egyptian-corpus/01-commercial-corporate-contract.md`

## Intake

Ask what you cannot infer. Stop asking once you have enough — this is a review,
not an interrogation.

**Required**
1. Which side are we on — the client, or the counterparty?
2. What is the deal, in one sentence?
3. Where do the parties sit — Egyptian, foreign, or both?
4. Is it signed, or still a draft? Does the user want to sign it, or get it changed?

**Recommended**
5. Payment in EGP or a foreign currency? Who bears FX risk?
6. Is performance physically in Egypt, or remote?
7. Any deadline, and what is it?
8. Who has more leverage right now?

**If the user says "just review it"** — infer 1–3 from the document, state your
inferences at the top of the output, and proceed. Do not block on intake.

## Workflow

### Step 1 — Read for defects before reading for risk

Before any commercial analysis, check the contract is *valid at all*. Egyptian
Civil Code Art. 89: a contract is concluded the moment two parties exchange
matching expressions of will, subject to any formal requirement the law imposes.

Then check, in this order:

- **Formal requirements.** Some Egyptian contracts have required forms. Check the
  instrument in question in the corpus; do not assume a contract is binding
  because it was signed.
- **Capacity.** Art. 109 — capable unless deprived or restricted. A minor, or a
  party under interdiction (الحجر), changes the analysis completely. Interdiction
  after registration voids later acts (Art. 114).
- **Nullity vs annulment — do not conflate them.** This is the single most
  common legal error in Egyptian contract analysis.
  - **Nullity (البطلان), Art. 141** — any interested person may raise it, **the
    court may raise it of its own motion**, and it can never be ratified.
  - **Annulment (الإبطال), Art. 140** — the right lapses after **three years**,
    and never more than fifteen years after conclusion.
  - **Prescription (التقادم), Art. 387** — **the court may NOT apply it of its
    own motion.** The debtor must plead it.
  - So: the court will rescue a void contract on its own, but will let a
    time-barred claim die silently unless someone pleads prescription. That
    asymmetry is real and decides cases.
- **Public property.** Civil Code Art. 87 — state and public property dedicated to
  public use cannot be disposed of, attached, or acquired by prescription. If a
  counterparty is a government body, check what you are actually being given.
- **Business capacity of the parties.** Is the counterparty a company that
  actually exists? A real commercial-registry entry, or a trading name?

### Step 2 — Classify the contract

Do this before clause work. It sets the default rules.

| Type | Defaults that follow |
|---|---|
| Commercial between merchants | Commercial Code 17/1999 applies; commercial custom (عرف تجاري) fills gaps; **default interest is 5% p.a.** (Art. 226) |
| Mixed (one party a merchant) | Commercial Code applies **to the merchant's obligations only** (Art. 3) — not the whole contract |
| Civil / non-commercial | Civil Code applies; **default interest is 4% p.a.** (Art. 226) |
| Administrative contract with a state entity | Arbitration needs the **competent minister's approval** (Arbitration Law Art. 1(2), added by Law 9/1997). Without it, no arbitration. |

### Step 3 — Clause-by-clause

⚠️ **If the client is the one signing, and is not a lawyer, start with
`references/RISK-GRID.md` instead.** It names the five clauses that actually move the
money, what each does to them in plain terms, and what to ask for — which is usually
what they actually asked you. Then work the rest through the full checklist.

Work `references/CLAUSE-CHECKS.md` top to bottom. For each clause: what it says,
what Egyptian law does with it, the risk, the redline, the fallback.

**Always check these five, in every Egyptian commercial contract:**

**1. Default interest and the penalty ceiling.** Civil Code **Art. 227(1)** —
whatever rate the parties agree, **anything above the statutory price is cut to
7%** with restitution of the excess. A clause promising 15% does not fail; it is
**silently reduced to 7%**. Drafters routinely over-promise here without knowing.
Statutory defaults are 4% (civil) / 5% (commercial), Art. 226. Art. 232 bars
capitalised interest and caps total interest at principal, save for commercial
custom.

**2. Agreed liquidated damages are conditional.** Civil Code **Art. 224** — agreed
compensation is **not due if the debtor proves the creditor suffered no loss**,
and the court may reduce it if grossly overstated or partly performed. So a
penalty clause does not auto-pay: it is an evidentiary starting point the other
side can defeat by showing no loss. **Art. 225** — loss beyond the agreed figure
cannot be claimed **unless the debtor committed fraud or gross fault**. A penalty
clause is therefore a ceiling on ordinary claims, not a floor.

**3. Force majeure is thin.** Egypt has no general statutory force majeure
equivalent to the common-law framing. A clause depends on its own wording. Check
it says: what events, notice deadline, mitigation, long-stop termination, and what
happens to sums already paid. Without a long-stop termination right, a
force-majeure event can suspend the contract indefinitely.

**4. Limitation periods — check the claim you are being asked to rely on.** Civil
Code Arts. 374–388, and they are not uniform:

| Claim | Period | Art. |
|---|---|---|
| General contractual claim | **15 years** | 374 |
| **Rent** (buildings and agricultural land) | **5 years** | 375 |
| Doctors', lawyers', engineers', brokers', teachers' professional claims | **5 years** | 376 |
| Taxes and duties owed to the State | **3 years** | 377 |
| **Workers' and servants' wages — daily and non-daily** | **1 year** | 378 |
| Goods sold by a merchant to a non-merchant | **1 year** | 378 |
| Hotel and restaurant bills | **1 year** | 378 |

**Art. 378(2)** — a party pleading the one-year limit **must swear on oath that he
actually paid the debt**. That is a real evidential trap for unpaid-wages claims.

Art. 383 — prescription is **interrupted** by a judicial claim *even if filed
before an incompetent court*, by formal notice (التنبيه), by attachment, or by a
claim in bankruptcy. Art. 384 — also by the debtor's acknowledgment, express or
tacit.

**5. Adhesion and oppression.** **Art. 149** — in an adhesion contract
(عقد بالإذعان) the court **may amend or delete oppressive terms** (شروط تعسفية),
and any agreement disclaiming that power is void. **Art. 151** — doubt is
construed in the **debtor's** favour, **except** that ambiguity in an adhesion
contract may never be construed against the adhering party. If your client is the
weaker, paper-adhesion party, the statute is more protective than the contract
suggests; say so.

Also apply **Art. 148(2)** — the contract embraces not only what it says but what
are among its requisites (مستلزماته) according to law, custom and equity. It is
the most useful article in the Code for a drafting agent, and it cuts both ways.

### Step 4 — Governing law and forum

This is where Egyptian drafting goes wrong most often. Read
`references/DISPUTE-RESOLUTION.md` before touching the clause.

Short version:
- **Court:** works, but check which court. Cairo Court of Appeal has exclusive
  supervisory jurisdiction over **international commercial arbitrations** seated
  in or outside Egypt, and parties **cannot agree that away** (Arbitration Law
  Art. 9(1)).
- **Arbitration:** usually right for cross-border. But check the traps: the
  number of arbitrators must be **odd** or the arbitration is void (Art. 15(2));
  **the language is Arabic unless the parties agree otherwise** (Art. 29(1));
  the annulment window is **90 days** from notification (Art. 54).
- **Nothing:** a contract with no dispute clause gives you the default forum,
  which is rarely where you want to be.

### Step 5 — Rate and package

Produce the deliverable in the format below. Flag anything you could not verify
as needing a lawyer's check rather than silently asserting it.

## Output format

```markdown
# Contract review — [deal name]

**Side:** [client / counterparty] · **Type:** [classification] · **Status:** [draft / signed]
**Assumptions:** [anything you inferred and were not told]

## 1. Verdict
Two or three sentences. Can they sign, sign with changes, or not sign.

## 2. Deal-breakers
| # | Issue | Why it bites | Fix |
|---|---|---|---|

## 3. Issue log
| # | Clause | Position | Risk | Fix | Fallback |
|---|---|---|---|---|---|

Risk: **Critical** (walk away) / **High** / **Medium** / **Low**.

## 4. Egyptian-law redlines
Drop-in replacement wording, English and Arabic, for each change.

## 5. What is unverified
[Anything the corpus marks UNVERIFIED, or a point that turns on facts you
do not have. Be specific — "confirm the limitation period for this specific
claim" beats "this is not legal advice".]

## 6. Next steps
```

## Rules

- **Cite or stay silent.** If you cannot cite a provision, describe the
  principle and flag it in section 5. Never invent an article number.
- **Egyptian Arabic text, not translation.** Drafting redlines in transliterated
  Arabic is worse than useless in front of an Egyptian court. Give real Arabic.
- **Keep the currency real.** If the deal is EGP, price in EGP and address FX
  risk explicitly. If USD, say which rate, which date, and who bears movement.
- **Tone.** The client is not a lawyer. Explain what a clause *does to them*,
  not what it means.
- **Length.** A 40-clause contract does not get 40 paragraphs. Group, and lead
  with what costs money.

## References

- `references/CLAUSE-CHECKS.md` — the clause-by-clause working checklist
- `references/RISK-GRID.md` — ⚠️ **for a client who is signing, not reviewing.**
  The five clauses that decide their exposure, what each does in plain terms, the
  Egyptian default that applies if it is left out, and what to negotiate. Also states
  the three ceilings (Art. 227(1), Arts. 224/225, Art. 148(2)) that change what a
  signed number is actually worth
- `references/DISPUTE-RESOLUTION.md` — governing law, court vs arbitration, the
  Egyptian traps, and drafting text for each
- `research/egyptian-corpus/01-commercial-corporate-contract.md` — the verified
  corpus. **Read this before asserting anything about Egyptian law.**