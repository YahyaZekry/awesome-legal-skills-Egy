# Validators

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19
> These are the checks that earn their place. Each entry records what it catches,
> and — equally important — how it produces **false positives**, because a noisy
> checker gets ignored and the real defect hides in the noise.

None of these are checked into the repo. They were run as heredocs. Copy the pattern
from here rather than rebuilding it.

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

**Check all four:**
- Article numbers (ranges expanded, `bis`/`مكرر` normalised)
- Law numbers
- Backticked **URLs** — this caught a real typo
- Emoji marker counts (✅ ❌ ⚠️ 🟡 →)

**Noisy?** Only if the extractor is wrong. One parity script reported a spurious
mismatch caused by **four bugs in the extractor itself**, not the file. If a mismatch
appears, verify the extractor before editing content.

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
| EN↔AR parity | **Highest** | After every Arabic file |
| URL reconciliation | High — caught a real one | After any reference edit |
| Internal consistency | **Highest, manual** | Before every commit |
| Heuristic "suspicious token" scans | ❌ Too noisy to use | Skip — it flagged indentation and brand names |
