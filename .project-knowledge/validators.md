# Validators

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> These are the checks that earn their place. Each entry records what it catches,
> and — equally important — how it produces **false positives**, because a noisy
> checker gets ignored and the real defect hides in the noise.

✅ **These are now checked in as a single runnable script:**
`python3 .project-knowledge/scripts/validate.py` — **all six checks** (pairing,
frontmatter, references, contamination, parity, registration), exit 1 on any failure,
safe to wire into CI. The code below is the original heredoc form, kept as the
reference for *what each check means and how it misfires*. **Prefer the script.**

⚠️ **The script found a real shipped defect on its first run** (an Arabic URL ejected
from its sentence into a stray code fence), and then **five bugs in itself** that had
produced 29 false failures and zero real ones. Read its docstring for the FAIL-vs-WARN
split and the documented extractor blind spots before acting on any warning.

⚠️⚠️ **A later addition is the one parity sub-check that is a hard failure: heading
structure.** It is structural — it compares a level sequence and extracts nothing from
inflected Arabic — so unlike the article/law-number checks it has **no false-positive
mode**. Its fence handling is load-bearing (see §3a). Within an hour of being written it
found a real asymmetry in `egy-legal-notice`. **When a structural check is available,
prefer it to a heuristic one** — the failure is the signal.

---

## 1. Frontmatter + reference resolution

**Catches:** YAML that fails to parse, `name` ≠ directory, thin descriptions,
dangling `references/` paths.

```bash
cd <repo> && python3 - <<'PY'
import re,glob,os,yaml
bad=0
for sk in sorted(glob.glob('skills/egy-*/SKILL.md')):
    d0=os.path.dirname(sk); t=open(sk,encoding='utf-8').read()
    m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
    try:
        fm=yaml.safe_load(m.group(1))
        assert fm['name']==os.path.basename(d0)
        assert isinstance(fm['description'],str) and len(fm['description'])>80
        assert fm['metadata']['license']=='CC-BY-4.0'
    except Exception as e:
        print(" FAIL",d0,e); bad+=1; continue
    refs=set(re.findall(r'`(references/[^`]+)`',t))
    miss=[r for r in refs if not os.path.exists(os.path.join(d0,r))]
    if miss: print(" MISSINGREF",d0,miss); bad+=1
print("problems:",bad)
PY
```

**Noisy?** No. Clean signal. Run after every batch.

---

## 2. Contamination scan (Arabic) — **REQUIRED**

**Catches:** stray Cyrillic / CJK / fullwidth characters, U+FFFD replacement chars,
Arabic words glued to Latin, duplicated Arabic words, digit runs (a template-loop
artifact), and `word_word` glitches.

```bash
cd <repo> && python3 - <<'PY'
import re,glob
AR=re.compile(r'^(UNVERIFIED|Art|Code|Law|Civil|references|research|egypt|md|eg|gov|www|EGP|IBAN|VAT|ETA|NOSI)$')
bad=0
for p in sorted(glob.glob('skills/egy-*/**/*.md',recursive=True)):
    t=open(p,encoding='utf-8').read()
    for i,l in enumerate(t.split('\n'),1):
        for m in re.findall(r'[\u0400-\u04FF\u3000-\u9FFF\uFF00-\uFFEF]',l):
            print("SCRIPT",p,i,m); bad+=1
        if '\ufffd' in l: print("REPL",p,i); bad+=1
    for m in re.finditer(r'([\u0600-\u06FF]{3,})\s+\1\b',t): print("DUPWORD",p,m.group(1)); bad+=1
    for m in re.finditer(r'[\u0600-\u06FF]{2,}_[\u0600-\u06FF]{2,}',t): print("GLITCH",p); bad+=1
    for m in re.finditer(r'(?:[0-9]{4,}\s*){3,}',t): print("DIGITRUN",p); bad+=1
print("total issues:",bad)
PY
```

### ⚠️ Known false-positive modes — read before trusting output

This checker reported **188 "issues"** in one run and **two** were real. Its noise:

| False positive | Why |
|---|---|
| `LATIN Art`, `Arts` | `(Art. N)` citation markers are legitimate |
| Bilingual glossary's English column | `GLOSSARY-EN-AR.md` is intentionally bilingual — **exclude it** |
| `InstaPay`, `WhatsApp`, `FawryPay`, `JavaScript`, `StartaBusiness` | Real brand names |
| Triple-repeat rule | Matches markdown indentation spaces and `........` template blanks |
| URLs in backticked table cells | Appear "missing" because the script strips code spans before display |

**Mitigation:** filter the allow-list, exclude `GLOSSARY-EN-AR.md`, and prefer the
parity checks (#3, #4) for content questions. The contamination scan answers
*"is this text corrupted"*; parity diffs answer *"did content go missing"*. Different
jobs — only one is load-bearing at a time.

---

## 3. EN↔AR parity diff — **highest-value check**

**Catches:** dropped articles, law numbers that drifted, wrong URLs, missing table
rows, marker asymmetry. This is what found the shipped defects.

```bash
python3 - <<'PY'
import re
from collections import Counter
def grab(p, pat):
    return Counter(re.findall(pat, open(p,encoding='utf-8').read()))
# normalise Arabic-Indic digits to ASCII first for article/law numbers
# then set-diff EN vs AR and report BOTH directions
PY
```

### 3a. Heading structure — **FAIL**, and the only *structural* check here

**Catches:** a section present in one language and absent from the other. This is
silent content loss, which is exactly what parity is for.

**Levels only.** The heading **text** is translated by design, so comparing text would
fail on every pair. Compare the level sequence instead — `[1, 2, 3, 2, 2]` must match
exactly. Verified to compare **22 files across 14 pairs**.

⚠️ **The fence handling is load-bearing, and it is the whole reason this is not a
one-liner.** Every skill carries an **Output format** section whose body is a
`markdown` template, and **the template's first line is itself a `#` heading** —
`# [the client's question]`. Counting those reports a phantom mismatch on nearly every
pair, and a check that is wrong most of the time is a check nobody reads. Fenced blocks
must be tracked and skipped.

⚠️ **This is the one parity sub-check that is a FAIL rather than a WARN**, because it
extracts nothing from inflected prose. The other four read Arabic that inflects,
abbreviates and omits — so they warn. This one compares a sequence, which is exact.

**And it earned that status on its first run**, by finding a real asymmetry nobody had
noticed: the Arabic `egy-legal-notice-ar/references/TEMPLATES.md` carried a
`## المراجع` section that the English lacked. Fixed by giving the **English** the same
cross-links, not by deleting the Arabic one.

### 3b. The four extracted sub-checks

- Article numbers (ranges expanded, `bis`/`مكرر` normalised)
- Law numbers
- Backticked **URLs** — this caught a real typo
- Emoji marker counts (✅ ❌ ⚠️ 🟡 →)

**Noisy?** Only if the extractor is wrong. One parity script reported a spurious
mismatch caused by **four bugs in the extractor itself**, not the file. If a mismatch
appears, verify the extractor before editing content.

⚠️ **Documented extractor blind spots — do NOT "fix" the Arabic to silence these:**
genuine content is regularly reported absent because Arabic expresses it differently.
Observed and hand-verified as false positives in this repo:

| Form | English | Arabic | Why the extractor misses it |
|---|---|---|---|
| Limbs as prose | `Art. 31(1)(3)` | `البند ٣ من الفقرة الأولى من المادة ٣١` | no numeric limb to match |
| Paragraph, prose | `Art. 378(2)` | `مع الفقرة (٢) منها` | ditto |
| Range, no article word | `Arts. 39–48` | `٣٩–٤٨ من القانون رقم ٤٩ لسنة ١٩٧٧` | no `مادة` before the range |
| List construction | `Law 49/1977 and Law 136/1981` | `القوانين رقم ٤٩ لسنة ١٩٧٧ ورقم ١٣٦ لسنة ١٩٨١` | the law word appears **once**, so later numbers have nothing to anchor on |
| Dual | `Arts. 25–26` | `المادتان ٢٥ و٢٦` | the dual form is not the plural `مواد` |
| Assimilated prefix | `Art. 15` | `للمادة ١٥` | the lam merges into the article and **the alif disappears** — so `ال?` does not cover it (`ال?` means "alif, then optional lam"; `للمادة` has no alif at all) |

---

## 4. URL-set reconciliation

**Catches:** typo'd domains, dropped URLs between EN and AR.

⚠️ **This caught a real defect that validation #1 and #2 both passed:** the Arabic
`PORTALS.md` had `itda.gov.eg` where the bare ITIDA domain is `itida.gov.eg`.

⚠️⚠️ **And the first fix made it worse.** A blanket replace also "corrected"
`itda.gov.eg/registry.aspx` and `itda.gov.eg/sgl.aspx` — which are **genuine working
paths**. Two valid URLs were destroyed to fix one typo.

**Lesson: set-diff before replacing, and never blanket-replace a domain.** Diff the
full URL set, not the host.

---

## 5. Internal-consistency checks (manual, highest yield per minute)

No script. These caught defects **every automated check missed**:

- **Heading agrees with its own list/body.** A heading said *"three hard rules"* over
  a **four**-item list. A heading said *"the one-year cure"* while the body said the
  cure reaches arrears **worth more than five years**.
- **Read the Arabic against the English.** Both defects above were found this way —
  by an agent diffing a translation back against its source. Single-language review
  catches content errors; it does not catch a file disagreeing with itself.
- **Scan for mixed-script artifacts.** A corrupted string
  `محاكم ECONEconomic` shipped in `egy-court-filing-guide` and survived schema
  validation, contamination scanning, and a direct read-through.

---

## The honest summary

| Check | Signal | Worth running |
|---|---|---|
| Frontmatter + refs | Clean | Always |
| Contamination | ⚠️ Noisy — allow-list it | Always, but read past the noise |
| **Heading structure** | **Exact — FAIL, no false positives** | After every Arabic file |
| EN↔AR parity (extracted) | **Highest** for content | After every Arabic file |
| URL reconciliation | High — caught a real one | After any reference edit |
| Internal consistency | **Highest, manual** | Before every commit |
| Heuristic "suspicious token" scans | ❌ Too noisy to use | Skip — it flagged indentation and brand names |

⚠️ **Heading structure is now automated, but §5's other manual checks are not, and
cannot easily be.** *"Heading agrees with its own body"* is a semantic check — it
compares a heading's claim against the list beneath it, which no extractor here can
do. It found a heading saying *"three hard rules"* over a **four**-item list, and a
heading saying *"the one-year cure"* while the body said the cure reaches arrears
**worth more than five years**. **That class of defect is still only found by reading.**
Both were in **English** files — the bilingual build finds them by making someone read
the translation against its source, not by parsing.
