# Risk Grid — the five clauses that decide your exposure

**For a founder or business owner who is not a lawyer.** This is the companion to
`CLAUSE-CHECKS.md`, not a replacement:

| File | Who it is for | What it does |
|---|---|---|
| `CLAUSE-CHECKS.md` | Someone doing the review | Goes clause by clause, top to bottom |
| **`RISK-GRID.md`** (this file) | Someone deciding **whether to sign** | Names the five clauses that actually move the money, what each does to you, and what to ask for |

Read this first. It tells you where to spend your attention. Then use
`CLAUSE-CHECKS.md` on the clauses this flags — and `DISPUTE-RESOLUTION.md` for
governing law and forum.

---

## ⚠️ First: silence is not safety

⚠️ **The single most expensive misconception in Egyptian contracting is that a
clause you left out is a risk you avoided.**

It is not. The Egyptian Civil Code is full of **supplétive** (gap-filling) rules that
apply **when the contract is silent** — so silence is not a neutral state, it is
**choosing the default**, and the default is frequently worse than what you could
have negotiated.

✅ The clear example, and it is the one to remember: **Art. 226** sets the default
interest rate, and it **differs between a civil and a commercial agreement**. You do
not get to have no rate; you get the Code's rate.

**So the question is never "is this clause safe?" It is "is this clause better or
worse than the default that applies without it?"**

---

## The five clauses, on one page

| # | Clause | What it decides | The red flag | What to ask for |
|---|---|---|---|---|
| 1 | **Liability cap** | The most the other side can ever recover from you | A cap with **no carve-outs** | Carve-outs for fraud, gross negligence, confidentiality, IP |
| 2 | **Indemnity** | Who pays when a **third party** sues | An indemnity that reads as a penalty | Cap it, and test it against **Art. 224/225** |
| 3 | **IP ownership** | Who owns what you create | "All IP vests in the Client" with no licence back | A **licence back** for pre-existing and generic material |
| 4 | **Data protection** | Your exposure under **Law 151/2020** | Silence, while you process personal data | Name the roles, the purpose, the retention, the transfers |
| 5 | **Termination** | How you get out, and what happens to work in flight | Termination "for convenience" with no payment for work done | Cure period, notice mechanics, and payment on termination |

**If you only read five things in a contract, read these five.** Everything else is
usually standard, negotiable later, or cheap to get wrong.

---

## 1. Liability cap

**What it decides.** Almost every dispute between businesses is really a fight about
this number. It is the ceiling on your total exposure.

**The Egyptian default.** ⚠️ There is no general statutory cap. Without a clause, your
exposure is whatever the general rules of compensation produce — which is why the cap
is one of the few clauses worth real negotiation time.

**The red flag.** A cap with **nothing carved out of it**. Read it looking for what is
*excluded* from the cap, not what is included. A cap that covers everything, including
fraud and confidentiality breaches, is a cap that wildly favours the drafter.

**What to ask for.** Carve-outs for **fraud, gross negligence, breach of
confidentiality, and IP infringement**. These are standard and a counterparty that
refuses all four is telling you something.

**Watch for:** sub-caps that are separate and smaller (e.g. a separate low cap for
data breach), and "super-cap" wording that reintroduces unlimited liability through the
back door.

---

## 2. Indemnity

**What it decides.** The difference between a cap and an indemnity is that an
indemnity is about a **third party** — someone outside the contract sues, and the
question is who pays.

**The red flag.** ✅ **An indemnity drafted as a penalty.** This matters more in Egypt
than the English-language template it was copied from, because of two articles:

- **Art. 225** — where the parties agree on compensation, it is understood as
  compensation for the damage actually suffered, and **the court may reduce it** if
  the obligor proves the agreed amount is exaggerated or that performance has partly
  occurred.
- **Art. 224** — a penalty clause is a **ceiling, not a floor**.

⚠️ **What this means in plain terms:** an uncapped indemnity in a contract does **not**
reliably give you the number written in it. It gives you a right to argue for that
number, subject to the court's power to cut it down. So an indemnity figure is a
**negotiating position, not a guarantee** — and a counterparty who promises "we will
indemnify you fully, unlimited" may be promising a number nobody will ever collect.

**What to ask for.** Cap it, define what triggers it, and require the indemnified
party to control the defence of the third-party claim (or at least be consulted) —
otherwise you pay for a defence you had no say in.

---

## 3. IP ownership

**What it decides.** Who owns the work product. ⚠️ **This is the clause most often
signed without being read, and the one most expensive to fix afterwards.**

**The red flag.** *"All intellectual property created under this Agreement vests in
the Client."* — read literally and with no carve-out, this can sweep in material that
has nothing to do with the engagement: your **pre-existing** components, your
**generic** tooling, and possibly work for other clients.

**What to ask for.**
- Carve out **pre-existing IP** explicitly, by schedule if necessary.
- Carve out **generic know-how and tooling** — the stuff you would use for any client.
- For anything you do hand over, insist on a **licence back** for your own reuse, or
  at minimum for portfolio and internal purposes.
- Say what happens to the IP if the client **does not pay**.

**Egyptian law.** The governing statute is **Law 82/2002** on the protection of
intellectual property rights. ⚠️ **Its operative provisions are deliberately not
summarised in this file** — a dedicated verified corpus file covering registration,
scope, term and enforcement is being built. Until it lands, treat any specific claim
about Egyptian IP scope as 🟡 **unverified** and check it. What you *can* rely on for
negotiation purposes is that ownership follows the contract far more than it follows
registerable title — so **the contract wording is where the fight is**.

---

## 4. Data protection

**What it decides.** ✅ Egypt has a **general** data protection statute, so this is not
an area where silence is available.

| Item | Value |
|---|---|
| Statute | **Law 151/2020** |
| Executive regulations | **MCIT Decision 816/2025** — Gazette 244, Supplement A, 1 Nov 2025 |
| Regulator | **Personal Data Protection Center** |
| Compliance deadline | ✅ **1 November 2026** |
| Transfer abroad | ⚠️ **No adequacy list and no standard contractual clauses route** — transfers need their own lawful basis |

**The red flag.** Silence. If you process personal data for a client and the contract
says nothing, you have neither the allocation of roles nor the lawful basis
documented.

**What to ask for — name all four in the contract:**
1. **Who is controller and who is processor** — and for which processing.
2. **Purpose limitation** — the client may only instruct you for the agreed purpose.
3. **Retention and deletion** — including what happens on termination.
4. **Transfers abroad** — ⚠️ called out separately, because there is **no adequacy
   list and no SCC route**. A transfer clause that assumes the European mechanism
   exists is a clause that does not work in Egypt.

**Also:** the deadline has passed or is imminent depending on when you read this. The
deadline is **1 Nov 2026**.

---

## 5. Termination

**What it decides.** Whether you can get out, and whether you get paid for work you
have already done when you do.

**The red flags.**
- Termination **for convenience** by the other side, with **no payment for work in
  progress**. This is the clause that closes small businesses.
- No **cure period** — meaning a trivial, fixable breach can end the contract.
- Notice by a **mechanism you cannot prove**.

⚠️ On that last point: **Art. 91** provides that an expression of will takes effect
when it comes to the addressee's **knowledge**, and **receipt is presumed, rebuttably**.
So "notice by email" is weak — a party can dispute receipt. Notices with real
consequences need a delivery mechanism you can **prove**.

**What to ask for.**
- Payment on termination for **work properly done plus committed costs**.
- A **cure period** (15–30 days) for non-payment and other curable breaches.
- Notice by a **provable** method, with a defined address.
- Say what happens to **confidentiality and IP** after termination — they must
  survive, and survival must be stated rather than assumed.

---

## The Egyptian ceilings that change the arithmetic

⚠️ Three rules silently change the value of what you have signed. Get these wrong and
you will build a budget on a number the court will not award:

| Rule | Effect |
|---|---|
| ✅ **Art. 227(1)** | Agreed interest is capped at **7%**. A contract promising more is not enforceable at the higher rate |
| ✅ **Art. 224/225** | A penalty clause is a **ceiling, not a floor**, and the court may **reduce** it |
| ✅ **Art. 148(2)** | The contract embraces its requisites according to **law, custom and equity** — not only its text. So a literal reading is not the whole reading, and an "entire agreement" clause is weakened by this |

**The practical consequence:** when a counterparty offers you a large penalty figure or
a generous interest rate, you are being offered something the court can reduce. Value
it accordingly, and do not trade real concessions for it.

---

## Negotiation order

When you cannot get everything, trade in this order:

1. **The liability cap and its carve-outs.** Highest value, and hardest to fix later.
2. **Payment terms and what is owed on termination.** Cash flow risk.
3. **IP carve-outs.** Cheap for them to concede, expensive for you to lose.
4. **Data protection allocation.** Cheap to draft correctly, and the deadline is real.
5. **Notice mechanics.** Small, and it decides disputes you cannot otherwise win.

⚠️ **Do not spend your negotiation capital on the penalty clause.** It is the clause
most often fought over and least often decisive, because **Art. 224/225** lets the
court adjust it anyway and **Art. 227(1)** caps the interest.

---

## Exposure estimate — the one page to fill in

```markdown
Contract: ______________________  Counterparty: ______________
Value: EGP ______   Term: ______   My exposure this year: EGP ______

| Clause | Present? | Does it beat the default? | Worst realistic outcome | Action |
|---|---|---|---|---|
| Liability cap | Y / N | | EGP ______ | |
| Indemnity | Y / N | | | |
| IP ownership | Y / N | | | |
| Data protection | Y / N | | | |
| Termination | Y / N | | | |

Ceilings noted:  interest capped at 7% (Art. 227(1))   [ ] checked
                 penalty is a ceiling, reducible   (Arts. 224/225)  [ ] checked
Unverified items I must check before signing: ______________________
```

⚠️ **Fill in the last line honestly.** Anything you could not verify goes there,
rather than into a decision.

---

## What this file does not do

- It does **not** tell you whether to sign. It tells you where the money is.
- It does **not** replace `CLAUSE-CHECKS.md` for a full review.
- It does **not** cover **forum or governing law** — see `DISPUTE-RESOLUTION.md`. A
  perfect liability cap in a contract with the wrong forum is still a bad contract.
- ⚠️ It does **not** state Egyptian IP scope, deliberately — see §3.
