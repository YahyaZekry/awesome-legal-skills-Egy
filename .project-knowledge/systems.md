# Systems

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19

Four systems run this project. Three work well. One is actively dangerous.

---

## 1. Upstream Lawve sync — ⚠️ DESTRUCTIVE

**What it is:** a job in `lawve-ai/awesome-legal-skills` that regenerates derived
files in this fork. Commit messages look like `chore: sync public Lawve skills`.

**What it owns:**

| Artifact | Behaviour |
|----------|-----------|
| `assets/.lawve-sync.json` | Map of **264** skill UUIDs → `{digest, path, updated_at}`. Read-only. |
| `.claude-plugin/marketplace.json` | **Generated.** 264 plugins. Will be rewritten. |
| `README.md` lines 19–~330 | Between `<!-- LAWVE_SYNC_START -->` and `<!-- LAWVE_SYNC_END -->`. Will be rewritten. |
| `skills/<upstream>/` — 264 dirs | Overwritten **wholesale** if the digest changes |

**Two hard rules (from `EGYPT-EDITION.md`):**

1. **Never edit an existing upstream skill directory.** An edit to
   `skills/nda-reviewer-jamie-tso` survives exactly until the next sync. Tracked by
   UUID + digest — the sync does not merge, it replaces.
2. **Never add Egypt skills inside the synced README block.** The next sync deletes
   them.

**Verify safety before touching anything under `skills/`:**

```bash
python3 -c "
import json
d=json.load(open('assets/.lawve-sync.json'))['resources']
paths={v['path'] for v in d.values()}
print('tracked:', len(paths))
print('egy tracked:', [p for p in paths if '-egy' in p or p.split('/')[-1].startswith('egy')] or 'NONE — safe')
"
```

> ⚠️ **Substring trap:** filtering on `'egy'` produces false positives — it matches
> `disclosure-strate**gy**-mapper-…`. Match on the path **basename prefix** instead.

**Current state:** ✅ no Egypt skill is sync-tracked. All 24 are safe.

**Freeze condition:** the Egypt edition is safe only because it lives entirely in new
`egy-*` directories. **Adding Egypt content to any existing directory re-introduces
the problem.**

---

## 2. Corpus-first research pipeline — ⭐ the core practice

**What it is:** the rule that no skill may be written before the underlying law is
retrieved and recorded.

```
Exa search  →  candidate statutes / gazette refs
Firecrawl   →  scrape portal or PDF
local extract  →  download PDF, extract text, read surrounding articles
corpus entry   →  citation + Arabic title + status + provisions + amendment chain + source + as-of date
skill          →  may only assert what the corpus marks ✅ or ⚠️
```

**Why it exists — the measured result:** research overturned **30+ widely-repeated
facts** about Egyptian law. **Four of them were in the operator's own initial briefs**,
written from memory. Had the skills been written from recall, roughly **one claim in
six** would have been wrong, and all of them would have sounded authoritative.

**⚠️ The pipeline's known failure mode:** Firecrawl's **query mode silently returned
the wrong articles twice** on the official Arabic Civil Code PDF. Both times the
output was plausible and nothing flagged it.

→ **Always download Arabic legal PDFs and extract the text locally.** Verify against
the surrounding articles. If a retrieved article reads oddly, assume the tool is wrong
until you have checked the raw file.

**Best source found:** the Ministry of Justice legislation encyclopedia at
`serviceapi.egyptianlaws.com` — it carries **Supreme Constitutional Court rulings
annotated inline**, which is how two tenancy statutes were obtained without a
paywalled database.

---

## 3. EN/AR paired build — ⭐ the quality mechanism

**What it is:** every topic is built twice, natively, in separate directories.

The stated reason is *routing* — the agent selects on frontmatter, so an Arabic prompt
needs an Arabic `description`. But the **unstated benefit is the one that mattered**:

> Building the second language surfaces defects in the first. All three shipped
> defects were in the **English** files and survived schema validation, contamination
> scanning, and a direct read-through. Each was caught by an Arabic agent reading the
> translation back against its source.

A single-language review catches content errors. It does **not** catch a file
disagreeing with itself. Two languages diffing each other do.

**Build order:** EN first (so the corpus is settled), then AR against it, then
parity-diff. For a batch of Arabic twins, build **sequentially** — launching three
simultaneous subagents hit rate limits three separate times.

---

## 4. Validation gate — see `validators.md`

Five checks. Two are clean signal (frontmatter, parity). One is required but noisy
(contamination). One is manual and highest-yield (internal consistency). One should
be skipped (heuristic token scans).

**Current standing:** 24 skills · 0 pairing orphans · 0 frontmatter/reference
failures · 0 contamination.

---

## What is NOT here

| Absent | Consequence |
|--------|-------------|
| CI | Validation ran by hand. Nothing enforces it on a future commit |
| Tests | The "test" is the parity diff, run manually |
| Schemas checked in | The five validators exist only in this folder and the session history |
| Plugin registration | Egypt skills are **not** in `marketplace.json` — see `roadmap.md` |
| Licensing review | Egypt skills are `CC-BY-4.0` original work while the repo is `CC BY-NC-ND`. Publishing publicly needs a licence check against each upstream source |
