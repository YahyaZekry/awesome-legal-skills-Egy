---
name: egy-legal-research
description: Find and verify Egyptian law — the Official Gazette vs Al-Waqa' al-Misriyya distinction, the ELP legislation portal, Court of Cassation principles and annual volumes, the Ministry of Justice legislation encyclopedia, official Arabic texts and WIPO Lex, the portals that are false friends, and how to verify a citation before relying on it. Use when asked to find an Egyptian statute, check whether a law is current, locate a court judgment or Cassation principle, or verify a citation someone has given you. Triggers on "Egyptian law", "find the law", "is this law current", "Court of Cassation", "legal research Egypt", "Gazette", "قانون مصري", "الجريدة الرسمية", "الوقائع المصرية", "محكمة النقض", "المبادئ القانونية", "البحث القانوني".
metadata:
  author: Egypt Edition (Lawve catalog)
  license: CC-BY-4.0
  version: 2026.10.12
---

# Finding and verifying Egyptian law

How to locate an Egyptian statute, check whether it is still in force, find a
Cassation principle, and **verify a citation before relying on it**.

**Not legal advice.** This is a method. Say so once.

## Why this skill exists

Egyptian law is cited constantly and wrongly. In building the corpus behind these
skills, research overturned **more than twenty** widely-repeated facts, including
four that models assert confidently. A citation you have not checked is a
citation you cannot rely on.

The single most common failure: **citing an article number from memory.** Egyptian
codes have been amended for seventy years. Do not.

## Step 1 — know which "gazette" you mean

⚠️ **These are two different documents and getting it wrong is a live error.**

| Arabic | What it is |
|---|---|
| **الجريدة الرسمية** (Al-Jarida al-Rasmiya) | The **Official Gazette** — the authoritative promulgation record |
| **الوقائع المصرية** (Al-Waqa'i' al-Misriyya) | The Egyptian Gazette — **distinct**, with its own title |

⚠️ Several English-language sources use "Egyptian Gazette" for one of these and
"Official Gazette" for the other. **Always give the Arabic name and the issue
number.**

⚠️⚠️ **`gcc.gov.eg` is NOT the gazette.** It returns **HTTP 200** and is the
**Cultural Development Fund**. A status-code check passes it. The gazette printing
and archive are at **`alamiria.com`** (المطابع الأميرية) and **`dspace.id.com.eg`**.

## Step 2 — the source ladder

Work down until you reach the authority you need.

| # | Source | What it gives you |
|---|---|---|
| **1** | **ELP — Egyptian Legislation Portal** `elpai.idsc.gov.eg` | The Cabinet's portal. Consolidations, texts, gazette references |
| **2** | **Ministry of Justice legislation encyclopedia** — `serviceapi.egyptianlaws.com` | ✅ **The best source found in this project.** Carries **Supreme Constitutional Court rulings annotated inline**, which is how Laws 49/1977 and 114/1946 were obtained without a paywalled database |
| **3** | **Court of Cassation legislation portal** (بوابة تشريعات محكمة النقض) | Used by several law-firm libraries reproducing statute text |
| **4** | **`alamiria.com`** / **`dspace.id.com.eg`** | Gazette printing and archive |
| **5** | **WIPO Lex** `wipo.int/wipolex` | ✅ **English translations of Egyptian IP and arbitration law** — Arbitration Law 27/1994 is there in both languages |
| **6** | **`eta.gov.eg`** | Official Arabic texts of the Civil Code, Companies Law and IP Law as PDFs |
| **7** | **Ministry portals** — MCIT, Ministry of Labour, ETA, Ministry of Justice | Sector regulations and decisions |
| **8** | `manshurat.org`, `eastlaws.com` | Secondary reproductions; useful for finding, **not for citing an article number** |

### The false friends

⚠️ **`alqalam.idsc.gov.eg` and `ela.gov.eg` have no DNS record at all.** Both are
widely cited as Egypt's legislation database and neither resolves. Use
**`elpai.idsc.gov.eg`**.

⚠️ **`ntra.gov.eg`** resolves in DNS and never answers HTTP. Use **`tra.gov.eg`**.

⚠️ **GAFI's site is a JavaScript SPA.** Legacy `/English/StartaBusiness/...` paths
redirect to a styled 404 that returns **HTTP 200**. Navigate from
`gafi.gov.eg/en` or use `portal.gafi.gov.eg`.

⚠️ **CBE intermittently serves a "Request Rejected" WAF page** to non-browser
clients. A blocked fetch is not evidence the content is gone.

## Step 3 — retrieve Arabic PDFs by download, not by query

⚠️⚠️ **This is a methodology finding, not a warning.**

In this project, Firecrawl's **query mode silently returned the wrong articles
twice** on the official Arabic Civil Code PDF. Both times the output looked
plausible. Nothing flagged it.

→ **Download the PDF and extract the text locally.** Verify against the surrounding
articles. If a retrieved article reads oddly, assume the tool is wrong until you
have checked the raw file.

## Step 4 — check whether the law is current

Never assume. For any statute, establish:

1. **Its citation** — number and year
2. **Its Arabic title** — ⚠️ titles change. **Companies Law 159/1981** had its
   title **amended by Law 4/2018**, which dropped one-person companies from the
   statute's own Arabic name and replaced **every reference** to the old title
   across that law, its regulations and other laws
3. **Its amendment chain** — with gazette references. Companies Law has been
   amended **eight times**; Civil Code and Law 181/2018 are frequently amended
4. **Whether something repealed it** — **Labour Law 12/2003 was repealed** by
   **Law 14/2025** effective 1 September 2025
5. **Whether a pending article was changed** — e.g. a suspected further Art. 71
   amendment in the consumer law

⚠️ **A consolidated text may itself be out of date.** The Companies Law text GAFI
publishes ends at Law 4/2018. Always look for something newer.

## Step 5 — Court of Cassation principles

✅ **The Office of Legal Principles (المكتب الفني للمبادئ القانونية)**, created by
decision of the President of the Court of Cassation dated **12 October 1950**;
its mandate is in **Art. 5 of the Judicial Authority Law** (قانون السلطة القضائية):
to **extract, classify and publish the legal principles** established by the
Court's judgments.

**Where:** `cc.gov.eg` and the search platform `cc.gov.eg/judgments_search`, which
separates **civil** and **criminal** competence.

**How they are published:** collected into **numbered annual volumes**
(*مجموعة أحكام محكمة النقض عن السنة …*), indexed in civil and criminal series —
e.g. **Year 73 (2022)**. A legislative bulletin (**النشرة التشريعية**) is also
issued.

⚠️⚠️ **The point that matters for an agent.** Egyptian Cassation "principles" are:

- **official but editorially selected** — the Technical Office **exercises discretion
  not to publish** a judgment it does not consider fit to become a principle
- **not formally binding precedent**
- **cited as persuasive authority** (أقوى تفسير / حجة قانونية)

And that discretion is deliberate: publishing is withheld **so that publishing does
not convert case-specific justice into a binding rule**.

→ **Cite the annual volume**, not a blog quoting a principle. And never write "Egypt
follows the rule that…".

## Step 6 — court structure, for knowing where to look

**Court of Cassation (محكمة النقض)** → **Courts of Appeal (محاكم الاستئناف)** →
**Courts of First Instance (محاكم الابتدائية)** → **District Courts (محاكم المواد
الجزئية)**. Plus **Execution Courts (محاكم التنفيذ)** and the **judge of summary
matters (قاضي الأمور الوقتية)**.

**Pecuniary limits** — ⚠️ amended twice, by **Law 191/2020** then **Law 157/2024**:

| Court | First instance | Final |
|---|---|---|
| **District Court** | value **≤ EGP 40,000** | value **≤ EGP 5,000** |
| **Court of First Instance** | all other civil/commercial | value **≤ EGP 100,000** |

⚠️ **Specialised labour courts** now exist under **Labour Law 14/2025** (Arts.
149–150, 185–187), each with its **own enforcement department** (Decision
4621/2025). Labour cassation runs through **specialised circuits inside the Court
of Cassation (Art. 186)** — 🟡 there is **no separate "Supreme Labour Court"**, and
a screening-circuit refusal is **unappealable**.

⚠️ **Economic Courts** have jurisdiction over civil and commercial disputes under
Consumer Protection Law 181/2018.

## Step 7 — verify before you rely

Run this on every citation:

- [ ] The number and year come from a **retrieved source**, not memory
- [ ] The **Arabic title** matches the source, including any amendment
- [ ] The **article number** was read in context — check the neighbouring articles
- [ ] The **amendment chain** is checked, and the law is **not repealed**
- [ ] Any consolidation is **current**
- [ ] The citation carries a **working URL** and an **"as of" date**
- [ ] Anything you could not confirm is marked **UNVERIFIED**, not quietly asserted

## The honesty rule

If you cannot verify it, say so and say what you tried.

> "I could not confirm the amendment date. I searched the Official Gazette index
> and the ELP; the consolidations I found all end at Law 4/2018. This needs a
> primary-source check before it goes in a filing."

That is a useful answer. A confident wrong article number is worse than a gap,
because nobody checks a thing that sounds right.

## References

- `research/egyptian-corpus/` — five verified files, 128–2470 lines each, every
  instrument carrying citation, status, provisions, amendment chain, sources and
  an "as of" date
- `skills/egy-context-operations/references/PORTALS.md` — every portal,
  HTTP-tested, with the false friends
- `skills/egy-court-filing-guide/` — the procedural side