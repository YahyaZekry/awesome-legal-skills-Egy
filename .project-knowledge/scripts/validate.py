#!/usr/bin/env python3
"""
Validate the Egypt Edition.

    python3 .project-knowledge/scripts/validate.py            # full run
    python3 .project-knowledge/scripts/validate.py --no-parity # skip EN/AR diff
    python3 .project-knowledge/scripts/validate.py --quiet     # failures only

Exit code is 0 when clean, 1 when any check fails. Safe to wire into CI.

WHAT THIS CHECKS, AND WHY EACH ONE EXISTS
-----------------------------------------
1. Pairing          every egy-x has exactly one egy-x-ar
2. Frontmatter      parses as YAML; name == directory; description >= 80 chars
3. References       every `references/...` path in a SKILL.md resolves
4. Contamination    stray scripts, replacement chars, digit runs, duplicated words
5. Parity           EN vs AR on article numbers, law numbers, URLs, markers
6. Registration     marketplace.json is valid and its Egypt entries resolve

Checks 2 and 5 are the ones that caught real shipped defects. Check 4 is noisy by
nature — see NOISE below and read past it.

KNOWN NOISE (deliberately excluded rather than "fixed")
-------------------------------------------------------
- GLOSSARY-EN-AR.md is bilingual by design; its English column trips any
  Latin-in-Arabic rule. Skipped.
- `(Art. N)` / `(Art N)` citation markers are legitimate Latin in Arabic prose.
- Brand names: InstaPay, WhatsApp, FawryPay, JavaScript, Meeza, Bareedi.
- Repeated Arabic-Indic numerals (١٠٠٠, ١٩٩٩) are correct numerals, not glitches.
- Indentation and `........` template blanks are not "triple repeats".
- README.md is excluded from parity entirely — it is a human-facing summary with
  no parity contract, and the English ones cite law numbers inline.

FAIL vs WARN — read this before "fixing" a warning
--------------------------------------------------
FAIL is reserved for things that are unambiguously wrong and always fixable:
unparseable frontmatter, a reference path that does not resolve, real
contamination, a missing EN/AR twin, a URL present in one language only, and a
registration entry pointing at a directory that does not exist.

WARN items prefixed `review:` mean "a human should glance at this". They are
extracted by regex from Arabic that inflects, prefixes and abbreviates, so the
extractor has known blind spots and a warning is NOT proof of a defect:

  - Article ranges with no preceding article word (`٣٩–٤٨ من القانون`).
  - Ranges split differently between the languages.
  - Limbs rendered as Arabic prose rather than a Latin limb letter.
  - Arabic list constructions: `القوانين رقم ٤٩ لسنة ١٩٧٧ ورقم ١٣٦ لسنة ١٩٨١`
    names the law word once, then only `ورقم N` — the later numbers have no
    `قانون` before them to anchor on.

WARN items prefixed `drift:` are mention-count differences. They are almost
always stylistic and can be ignored once eyeballed.

Do NOT edit the Arabic content to silence a warning without first confirming
against the source that something is genuinely missing. A confident wrong fix is
worse than the warning, because nobody re-checks a thing that now looks right.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILLS = REPO / "skills"
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

AR = "\u0600-\u06FF"
AR_INDIC = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

# Files that are intentionally bilingual or contain Latin by design.
SKIP_CONTAMINATION = {"GLOSSARY-EN-AR.md"}
# README.md is EXCLUDED from parity. It is a human-facing summary, not skill
# content, and carries no parity contract — the English summaries cite law
# numbers and articles inline while the Arabic ones are plain prose. Including it
# manufactures hundreds of false "missing in AR" failures.
SKIP_PARITY = {"GLOSSARY-EN-AR.md", "README.md"}

# Latin allowed to appear inside Arabic prose beyond backticks and URLs.
ALLOWED_LATIN = {
    "UNVERIFIED", "PARTIAL", "Art", "Arts", "Code", "Law", "Civil", "Commercial",
    "Companies", "Consumer", "EEA", "SME", "EGP", "IBAN", "VAT", "GAFI", "CRS",
    "CRM", "CV", "ETA", "SDK", "ERP", "POS", "NOSI", "ECESR", "X.509", "HTTP",
    "DNS", "PDF", "HR", "InstaPay", "WhatsApp", "FawryPay", "JavaScript", "Meeza",
    "Bareedi", "reference", "references", "research",
}

# --- regexes ---------------------------------------------------------------

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
REF = re.compile(r"`(references/[^`]+)`")
SCRIPT_CHARS = re.compile(r"[\u0400-\u04FF\u3000-\u9FFF\uFF00-\uFFEF]")
DIGIT_RUN = re.compile(r"(?:[0-9]{4,}\s*){3,}")
DUP_WORD = re.compile(r"([\u0600-\u06FF]{3,})\s+\1\b")
GLUE = re.compile(r"[\u0600-\u06FF]{2,}_[\u0600-\u06FF]{2,}")
URL = re.compile(r"`([a-z0-9][a-z0-9.\-]*\.(?:gov\.eg|com|org|net|eg|int|io)[^`]*)`")

# Article citations, applied to canonicalised text (see canon()).
#   `Art. 5` · `Arts. 149-150` · `Art. 4 bis` · `Art. 148(c)` · `Art. 43(6)`
# The limb is a single letter or 1-2 digits, so prose like
# "Art. 29 (under-cited, and it bites)" is NOT captured as an article identity.
ARTICLE = re.compile(
    r"\bArts?\.?\s*(\d+(?:\s*bis)?(?:\s*\((?:[a-z]|\d{1,2})\))?(?:\s*[–-]\s*\d+)?)"
)

# Law citations: 17/1999 · Law 90 of 1944 · قانون رقم ٦٧ لسنة ٢٠١٦ ·
# قانون الإثبات رقم ٢٥ لسنة ١٩٦٨  (note: an Arabic NAME may sit between the word
# "law" and the number, which is why the gap is `[^\d]{0,40}?` rather than `\s*`).
LAW_SLASH = re.compile(r"\b(\d{1,4})\s*/\s*(\d{4})\b")
LAW_OF = re.compile(
    r"(?:Law|Decision|Decree|قانون|قرار)[^\d]{0,40}?(\d{1,4})\s*(?:of|لسنة)\s*(\d{4})"
)

MARKERS = {"✅": "\u2705", "⚠️": "\u26a0", "🟡": "\U0001F7E1", "❌": "\u274c", "→": "\u2192"}

# Arabic limb letters → Latin, so 18(ب) and 18(b) compare equal.
LIMB = str.maketrans({"أ": "a", "ب": "b", "ج": "c", "د": "d", "ه": "e", "و": "f"})

# Every Arabic form of "article", not just the dictionary form. Arabic inflects
# and prefixes this word, so a literal `.replace("المادة", ...)` silently misses:
#   المادتان  dual, "the two articles"   (Arts. 14-15)
#   بالمادة / للمادة  preposition + article  (Art. 604)
#   المواد / والمواد  plural
# Note `لل`: when the preposition ل attaches to the definite article, the two lams
# assimilate and the alif disappears — للمادة, not لالمادة. Writing this prefix as
# `ال?` does NOT cover it, because `ال?` means "alif, then optional lam", and
# للمادة has no alif at all. That single missed form produced recurring false
# "article missing in AR" reports for Arts. 604.
ARTICLE_WORD = re.compile(
    r"[ولبفك]{0,2}(?:ال|لل)?مواد"
    r"|[ولبفك]{0,2}(?:ال|لل)?ماد(?:ة|تان|تين|ت)"
)


def canon(text: str) -> str:
    """
    Put Arabic and English citations into one comparable form.

    Four Arabic conventions have to be reconciled or every comparison produces
    false failures:

      1. digits       ٦٧ لسنة ٢٠١٦      -> 67 لسنة 2016
      2. bis          Art 4 مكرر         -> Art 4 bis
      3. limbs        18(ب)              -> 18(b)
      4. article word المادة ٢ / المواد ٣٩–٤٨ -> Art 2 / Arts 39-48

    (4) matters most: the Arabic skills frequently write the article in Arabic
    with NO Latin `(Art N)` marker at all, so a marker-only extractor silently
    misses those articles and reports them as "missing in AR".
    """
    t = text.translate(AR_INDIC)
    t = t.replace("مكرر", "bis")
    t = re.sub(r"\(([\u0623-\u0648])\)", lambda m: f"({m.group(1).translate(LIMB)})", t)
    t = ARTICLE_WORD.sub(" Art", t)
    return t


def norm(s: str) -> str:
    """Collapse whitespace and unify dashes; assumes canon() has already run."""
    return re.sub(r"\s+", " ", s.replace("\u2013", "-").replace("\u2014", "-")).strip()


def articles(text: str) -> Counter:
    return Counter(norm(m) for m in ARTICLE.findall(canon(text)))


def laws(text: str) -> Counter:
    t = canon(text)
    out: Counter = Counter()
    for a, b in LAW_SLASH.findall(t):
        out[f"{a}/{b}"] += 1
    for a, b in LAW_OF.findall(t):
        out[f"{a}/{b}"] += 1
    return out


def urls(text: str) -> Counter:
    return Counter(URL.findall(text))


def markers(text: str) -> Counter:
    """Actual occurrence counts, not presence."""
    return Counter({k: text.count(v) for k, v in MARKERS.items() if v in text})


def egy_skill_dirs() -> list[Path]:
    return sorted(d for d in SKILLS.glob("egy-*") if d.is_dir())


def md_files() -> list[Path]:
    return sorted(SKILLS.glob("egy-*/**/*.md"))


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


# --- checks ----------------------------------------------------------------

def check_pairing(dirs: list[Path], fail: list[str]) -> None:
    names = {d.name for d in dirs}
    en = {n for n in names if not n.endswith("-ar")}
    ar = {n for n in names if n.endswith("-ar")}
    for n in sorted(en):
        if f"{n}-ar" not in names:
            fail.append(f"pairing: {n} has no -ar twin")
    for n in sorted(ar):
        if n[:-3] not in names:
            fail.append(f"pairing: {n} has no EN twin")


def check_frontmatter(dirs: list[Path], fail: list[str]) -> None:
    try:
        import yaml
    except ImportError:
        fail.append("frontmatter: PyYAML not installed — install pyyaml")
        return
    for d in dirs:
        sk = d / "SKILL.md"
        if not sk.is_file():
            fail.append(f"frontmatter: {d.name}/SKILL.md missing")
            continue
        t = read(sk)
        m = FM.match(t)
        if not m:
            fail.append(f"frontmatter: {d.name}/SKILL.md has no frontmatter block")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except Exception as e:  # noqa: BLE001
            # The classic cause: a single-line Arabic description containing a
            # colon. It must use `>-` folded block style.
            fail.append(f"frontmatter: {d.name} YAML parse failed: {e}")
            continue
        if fm.get("name") != d.name:
            fail.append(f"frontmatter: {d.name} name={fm.get('name')!r} != directory")
        desc = fm.get("description")
        if not isinstance(desc, str) or len(desc) < 80:
            fail.append(f"frontmatter: {d.name} description too short/missing")
        if (fm.get("metadata") or {}).get("license") != "CC-BY-4.0":
            fail.append(f"frontmatter: {d.name} license is not CC-BY-4.0")


def check_references(dirs: list[Path], fail: list[str]) -> None:
    for d in dirs:
        sk = d / "SKILL.md"
        if not sk.is_file():
            continue
        for r in sorted(set(REF.findall(read(sk)))):
            if not (d / r).exists():
                fail.append(f"reference: {d.name} -> {r} does not exist")


def check_contamination(files: list[Path], fail: list[str]) -> None:
    for p in files:
        if p.name in SKIP_CONTAMINATION:
            continue
        t = read(p)
        rel = p.relative_to(REPO)
        for i, line in enumerate(t.split("\n"), 1):
            for ch in SCRIPT_CHARS.findall(line):
                fail.append(f"contamination: {rel}:{i} stray script char {ch!r}")
            if "\ufffd" in line:
                fail.append(f"contamination: {rel}:{i} U+FFFD replacement char")
        for m in DIGIT_RUN.finditer(t):
            fail.append(f"contamination: {rel} digit run {m.group(0)[:24]!r}")
        for m in DUP_WORD.finditer(t):
            fail.append(f"contamination: {rel} duplicated word {m.group(1)!r}")
        for m in GLUE.finditer(t):
            fail.append(f"contamination: {rel} glued token {m.group(0)!r}")


def check_parity(dirs: list[Path], fail: list[str], warn: list[str]) -> None:
    en = sorted(d for d in dirs if not d.name.endswith("-ar"))
    for d in en:
        ar = SKILLS / f"{d.name}-ar"
        if not (ar / "SKILL.md").is_file():
            continue
        # Compare a skill's whole tree against its twin's.
        def blob(root: Path) -> dict[str, str]:
            out = {}
            for f in sorted(root.rglob("*.md")):
                if f.name in SKIP_PARITY:
                    continue
                out[f.name] = read(f)
            return out

        a, b = blob(d), blob(ar)

        # Articles: EN declares them, AR repeats them. A difference is worth a
        # look but is NOT a hard invariant — the Arabic legitimately uses list
        # constructions ("القوانين رقم ٤٩ ... ورقم ١٣٦ ...") where the law word
        # appears once, renders limbs as Arabic prose where the allow-list
        # rejects a bare Latin letter, and splits ranges differently.
        ea, ba = articles(" ".join(a.values())), articles(" ".join(b.values()))
        missing = {k: v for k, v in ea.items() if k not in ba}
        if missing:
            warn.append(f"review: {d.name} articles in EN not found in AR: {sorted(missing)}")

        # Law numbers: distinguish a genuine ABSENCE from mere mention drift.
        # `Counter` subtraction conflates the two — subtracting counts reports a
        # law mentioned 5 times in EN and 3 in AR as though EN had something AR
        # lacked, which is not true and not worth anyone's attention.
        el, bl = laws(" ".join(a.values())), laws(" ".join(b.values()))
        absent_ar = sorted(k for k in el if k not in bl)
        absent_en = sorted(k for k in bl if k not in el)
        if absent_ar:
            warn.append(f"review: {d.name} law numbers not present in AR: {absent_ar}")
        if absent_en:
            warn.append(f"review: {d.name} law numbers not present in EN: {absent_en}")
        count_drift = {
            k: (el[k], bl[k])
            for k in set(el) & set(bl)
            if el[k] != bl[k]
        }
        if count_drift:
            warn.append(f"drift: {d.name} law number mention counts EN/AR {count_drift}")

        # URLs: a URL present in one language and absent from the other IS a hard
        # failure. This check caught two real defects — a typo'd ITIDA domain and
        # a URL ejected from an Arabic sentence into a stray code fence. A URL in
        # both but mentioned a different number of times is only drift.
        eu, bu = urls(" ".join(a.values())), urls(" ".join(b.values()))
        if set(eu) != set(bu):
            fail.append(
                f"parity: {d.name} URL sets differ. EN-only={sorted(set(eu) - set(bu))} "
                f"AR-only={sorted(set(bu) - set(eu))}"
            )
        elif eu != bu:
            diff = {k: (eu[k], bu[k]) for k in set(eu) | set(bu) if eu[k] != bu[k]}
            warn.append(f"drift: {d.name} URL mention counts differ EN/AR {diff}")

        # Markers: a review item, not a failure. Emoji counts are not a content
        # contract — the English prose uses the `→` arrow to introduce takeaways
        # where the Arabic often uses a different construction.
        em, bm = markers(" ".join(a.values())), markers(" ".join(b.values()))
        if em != bm:
            warn.append(f"drift: {d.name} marker counts differ EN={dict(em)} AR={dict(bm)}")


def check_registration(fail: list[str], warn: list[str]) -> None:
    if not MARKETPLACE.is_file():
        warn.append("registration: marketplace.json not found — skipped")
        return
    try:
        d = json.loads(read(MARKETPLACE))
    except Exception as e:  # noqa: BLE001
        fail.append(f"registration: marketplace.json is not valid JSON: {e}")
        return
    plugins = d.get("plugins", [])
    egy = [p for p in plugins if p.get("name", "").startswith("egy-")]
    dirs = {x.name for x in egy_skill_dirs()}
    en_dirs = {n for n in dirs if not n.endswith("-ar")}
    if not egy:
        warn.append("registration: no Egypt plugins registered — run register-egypt.py")
        return
    registered = {p["name"] for p in egy}
    for n in sorted(en_dirs - registered):
        warn.append(f"registration: {n} exists on disk but is not registered")
    for n in sorted(registered - en_dirs):
        fail.append(f"registration: {n} is registered but has no skill directory")
    for p in egy:
        for s in p.get("skills", []):
            if not (REPO / s).is_dir():
                fail.append(f"registration: {p['name']} points at missing {s}")
    names = [p.get("name") for p in plugins]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        fail.append(f"registration: duplicate plugin names {dupes}")


# --- main ------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-parity", action="store_true", help="skip the EN/AR diff")
    ap.add_argument("--quiet", action="store_true", help="print failures only")
    args = ap.parse_args()

    fail: list[str] = []
    warn: list[str] = []
    dirs = egy_skill_dirs()
    files = md_files()

    if not dirs:
        print("ERROR: no skills/egy-* directories found", file=sys.stderr)
        return 1

    check_pairing(dirs, fail)
    check_frontmatter(dirs, fail)
    check_references(dirs, fail)
    check_contamination(files, fail)
    if not args.no_parity:
        check_parity(dirs, fail, warn)
    check_registration(fail, warn)

    en = sum(1 for d in dirs if not d.name.endswith("-ar"))
    if not args.quiet:
        print("Egypt Edition validation")
        print(f"  skills          {len(dirs)}  ({en} EN + {len(dirs) - en} AR)")
        print(f"  markdown files  {len(files)}")
        print(f"  corpus files    {len(list((REPO / 'research' / 'egyptian-corpus').glob('*.md')))}")
        print()

    if warn:
        print(f"WARNINGS ({len(warn)})")
        for w in warn:
            print(f"  ! {w}")
        print()

    if fail:
        print(f"FAILURES ({len(fail)})")
        for f in fail:
            print(f"  x {f}")
        print()
        print("FAILED")
        return 1

    if not args.quiet:
        print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
