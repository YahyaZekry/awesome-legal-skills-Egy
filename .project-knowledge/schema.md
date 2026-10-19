# Schema & Contracts

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> These are content contracts, not database tables. Breaking one silently breaks a
> skill — the agent either fails to select it, or loads it and states a falsehood.

---

## 1. Skill directory contract

```
skills/egy-<topic>/
├── SKILL.md          REQUIRED — frontmatter + body
├── README.md         REQUIRED — human-facing summary (one paragraph, no frontmatter)
└── references/       OPTIONAL — deep material loaded on demand
    └── *.md          referenced from SKILL.md as `references/FILE.md`
```

Rules:
- `<topic>` is **kebab-case and describes the task, not the statute** —
  `egy-commercial-contract-review`, never `egy-law-72-2017`
- Reference paths in `SKILL.md` are **relative to the skill dir** and must resolve
- `README.md` carries no frontmatter — it is not loaded by the agent

---

## 2. SKILL.md frontmatter

```yaml
---
name: egy-<topic>              # MUST equal the directory name exactly
description: >-                # see the Arabic warning below
  <what it does>. Use when <trigger situation>. Triggers on "<en>", "<en>",
  "<ar>", "<ar>".
metadata:
  author: Egypt Edition (Lawve catalog)
  license: CC-BY-4.0
  version: 2026.10.12
---
```

| Field | Contract |
|-------|----------|
| `name` | Must equal the directory basename. Validation asserts this. |
| `description` | Must be a **string of 80+ characters**. Carries the trigger words. |
| `metadata.license` | Always `CC-BY-4.0` — Egypt skills are **original work**, not edits of the CC BY-NC-ND upstream |
| `metadata.author` | Always exactly `Egypt Edition (Lawve catalog)` |

### ⚠️ The Arabic folded-block rule (non-negotiable)

Arabic `description` **must** use `>-` folded block style:

```yaml
description: >-
  مراجعة العقود التجارية في مصر — ...
```

A single-line Arabic description containing a **colon breaks YAML parsing** — the
whole frontmatter fails to load and the skill becomes invisible. This was hit during
the build. `>-` is the fix, and it must be used in **every** `-ar` skill.

### Trigger-word rule

- English skills: English triggers + the common Arabic words a bilingual user would
  actually type (`قانون مصري`, `الجريدة الرسمية`)
- Arabic skills: **Arabic triggers only** — what an Arabic speaker types
  (`راجع`, `عقد`, `إيجار`, `شركة`, `شكوى`)

This is why EN/AR ship as **separate directories** rather than a language toggle:
selection happens on frontmatter, so two directories means each prompt language
resolves to the right skill.

---

## 3. EN/AR pairing invariants

Verified programmatically after every batch:

| Invariant | Where it is enforced, and with what teeth |
|-----------|-------|
| Exactly one `egy-x-ar` per `egy-x` | ✅ `validate.py` check 1 — **FAIL** |
| **Heading count + order match** | ✅ `validate.py` check 5 — **FAIL**, as a **level sequence**. The only parity sub-check with **no false-positive mode**, because it extracts nothing from prose. Fenced blocks must be skipped — see `validators.md` §3a |
| URLs match exactly | ✅ `validate.py` check 5 — **FAIL**. A URL present in one language only is always a defect, not a judgement call |
| Article numbers match **in value** | ⚠️ `validate.py` check 5 — **WARN**. Extracted from inflected Arabic, so it has real blind spots — `validators.md` §3b lists them, all hand-verified as false positives |
| Law numbers match in value | ⚠️ **WARN**, same reason |
| Emoji markers match | ⚠️ **WARN** (`drift:`) — usually stylistic. Eyeball and move on |
| Figures match | ❌ **NOT automated** — EGP amounts, deadlines, percentages and thresholds still need a human eye. This is the largest remaining hole |

⚠️ **Prefer structural to heuristic wherever a choice exists.** The automatable invariants
above are the ones where the two languages must agree on something that is *not* prose.
Everything else becomes a warning, and warnings get skimmed.

**Deliberate asymmetries — do not "fix" these:**
- Arabic cites each article twice (`المادة ٥٩٨ (Art 598)`) → higher numeral count
- Arabic spells small numbers as words (`خمسين شريكاً` vs `50 partners`)
- Arabic uses Arabic-Indic numerals (٢٠٢٥) in prose
- Arabic adds law numbers where EN names a law without one
- Arabic renders acronyms outside the allow-list in Arabic

### House style in Arabic files

| Rule | Example |
|------|---------|
| Article markers carry **no trailing period** | `(Art 598)` not `(Art. 598)` |
| `bis` articles → **مكرر** | `المادة ٤ مكرر (Art 4 مكرر)` |
| `PARTIAL` → **مُتحقَّق منه جزئياً** | |
| Keep Egyptian terms in Arabic | قاضي الأمور الوقتية, محضر, الشهر العقاري |
| Latin allowed only for | backticked paths, URLs, confidence markers, `UNVERIFIED`, and article markers |

---

## 4. Corpus entry format

Every instrument in `research/egyptian-corpus/` carries:

1. **Citation** — number and year
2. **Arabic title** — ⚠️ titles change; Companies Law 159/1981 had its title amended by Law 4/2018
3. **Status** — in force / repealed / amended
4. **Provisions** — the relevant articles
5. **Amendment chain** — with gazette references
6. **Sources** — URL + retrieval method
7. **"As of" date** — when it was last checked

---

## 5. Confidence markers

Non-negotiable vocabulary. A skill may not upgrade a marker.

| Marker | Meaning | May a skill state it as fact? |
|:------:|---------|------------------------------|
| ✅ | Verified against a primary source | **Yes** |
| ⚠️ | Verified but carries a trap / conditions | Yes, with the trap stated |
| 🟡 | **UNVERIFIED** — partial, secondary, or conflicting | **No.** Must say so and tell the user to confirm |
| ❌ | Widely believed and **wrong** | Only inside a correction ("X is not Y") |

### The citation rule (non-negotiable)

> Every legal proposition carries its citation, and every citation traces to
> `research/egyptian-corpus/`. If the corpus marks something `UNVERIFIED`, the skill
> must not state it as fact.

Egyptian law is amended often and **a stale article number is a real harm, not a
cosmetic error**. This rule is why `egy-tax-and-einvoicing` carries no tax rates at
all, and why `egy-court-filing-guide` refuses to quote a fee figure.

---

## 6. The contamination contract

Arabic generation has corrupted output **five separate times** in this project:
stray Cyrillic, CJK, Portuguese fragments, repeated digit runs, duplicated words, and
half-finished sentences. Arabic **blockquote templates** are the highest-risk region.

Every Arabic file must pass the contamination scan in `validators.md` before commit.
This is not optional and not a formality — it has caught real defects every time.
