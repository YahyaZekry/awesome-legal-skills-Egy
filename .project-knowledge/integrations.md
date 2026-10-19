# External Integrations & Data Contracts

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19

---

## 1. Exa MCP — research discovery

- **Used for:** semantic discovery of Egyptian statutes, gazette references, and
  articles where the exact citation is not yet known
- **Configured in:** `~/.config/opencode/opencode.jsonc` — local stdio
  `exa-mcp-server`, API key in env
- **Contract:** input = a semantically rich description of the ideal page, not
  keywords. Output = candidate URLs + content
- **Load-bearing results it produced:** **Law 164/2025**, the ITIDA
  **Decree 109/2005**, and the **Labour Law Arts. 117–126** hours provisions. None
  of these were findable by keyword from the initial assumptions
- **Owner:** operator's global config, not this repo

---

## 2. Firecrawl MCP — page and PDF retrieval

- **Used for:** scraping Egyptian government portals, downloading gazette PDFs
- **Configured in:** `~/.config/opencode/opencode.jsonc` — remote MCP with a Bearer
  header
- **⚠️ Known failure mode — the most important contract in this file:**

> Firecrawl's **query mode silently returned the wrong articles twice** on the
> official Arabic Civil Code PDF. Both times the output looked plausible and nothing
> flagged it.

- **Required practice:** download Arabic legal PDFs and extract text **locally**.
  Verify against surrounding articles. If a retrieved article reads oddly, assume the
  tool is wrong until the raw file confirms it
- **Owner:** operator's global config, not this repo

---

## 3. Upstream lawve-ai — the sync contract

| | |
|---|---|
| Remote | `upstream` → `https://github.com/lawve-ai/awesome-legal-skills.git` |
| Local remote | `origin` → `https://github.com/YahyaZekry/awesome-legal-skills-Egy.git` |
| Relationship | `origin` is a **fork** of `upstream` |

**Files upstream owns — never hand-edit:**

| File | Contract |
|------|----------|
| `assets/.lawve-sync.json` | `{resources: {<uuid>: {digest, path, updated_at}}}` — 264 entries. A changed digest means the skill gets **replaced wholesale**, not merged |
| `.claude-plugin/marketplace.json` | Generated. 264 plugins |
| `README.md` (lines 19–~330) | Generated, between `LAWVE_SYNC_START` / `LAWVE_SYNC_END` |
| `skills/<264 upstream dirs>` | Replaced on digest change |

**⚠️ How the sync reaches this fork:** `.github/` contains **no workflow files** — only
`FUNDING.yml` and `ISSUE_TEMPLATE/submit-skill.yml`. So there is **no CI and no sync
job running in this repo**. Confirmed by authorship: every `sync` commit is by an
upstream author (Antoine Louis, Samuel Compagnon / notnotsamuel), never by an action
in this fork. The sync arrives by **merging `upstream/main`**.

→ **Consequence:** the risk to Egypt work is **merge conflicts**, not silent deletion.
✅ **Mitigated (2026-10-19):** `register-egypt.py` is idempotent, so a conflicted or
clobbered `marketplace.json` is restored by re-running one command. The conflict is now
an inconvenience rather than a loss. *(Assumption still unverified — see roadmap Track 1.)*

**Safety check before touching anything under `skills/`:**

```bash
python3 -c "
import json
d=json.load(open('assets/.lawve-sync.json'))['resources']
paths={v['path'] for v in d.values()}
egy=[p for p in paths if p.split('/')[-1].startswith('egy-')]
print('egy skills sync-tracked:', egy or 'NONE — safe')
"
```

> ⚠️ Substring trap: filtering on `'egy'` matches `disclosure-strate**gy**-mapper-…`.
> Match the **basename prefix**.

**Current state:** ✅ no Egypt skill is sync-tracked.

---

## 4. `.claude-plugin/marketplace.json` — distribution

| Field | Value |
|-------|-------|
| `name` | `lawve-ai` |
| `version` | `2.0.0` |
| `owner` | Lawve AI — `contact@lawve.ai` |
| `plugins` | **276** entries — 264 upstream + 12 Egypt |
| Plugin shape | `{name, source, description, version, author, license, category, skills[], strict}` |
| Egypt entries | **12** (`egy-*`) |
| Egypt categories | 1 new: **`Property Law`** (tenancy); the rest reuse the upstream set |

Each upstream plugin points at one skill directory: `"skills": ["./skills/<name>"]`.
**Each Egypt plugin points at two** — both languages:

```json
"skills": ["./skills/egy-rental-agreement", "./skills/egy-rental-agreement-ar"]
```

→ **The Egypt skills are now installable.** One install serves both languages, and
because skill selection is by frontmatter, an English prompt never loads the Arabic
skill even though it is installed.

### ⚠️ Editing this file: use the generator, never hand-edit

```bash
python3 .project-knowledge/scripts/register-egypt.py --check   # dry run
python3 .project-knowledge/scripts/register-egypt.py           # apply / restore
```

It is **idempotent** — re-running replaces the Egypt block rather than duplicating it,
verified byte-identical. Run it after any `upstream/main` merge. It refuses to run if a
skill directory is missing or if the file's trailing structure has changed.

**It injects text; it does not round-trip JSON.** `json.dumps(indent=2)` does **not**
reproduce the upstream file — 243 KB vs 235 KB, because the real file keeps `skills`
arrays inline. A JSON round-trip would reformat all 264 upstream entries. Textual
injection gives a **+156 / −0** diff.

Also note the upstream file carries **no trailing comma** convention and raw UTF-8 (not
`\u` escapes) — the generator matches both.

---

## 5. GitHub sync forks — pull and push targets

| Purpose | URL |
|---------|-----|
| Feature branch | `https://github.com/YahyaZekry/awesome-legal-skills-Egy/tree/egypt-edition` |
| Open a PR | `https://github.com/YahyaZekry/awesome-legal-skills-Egy/pull/new/egypt-edition` |
| Base | `main` |

---

## Data contracts worth stating exactly

**Skill selection contract:** the agent matches on frontmatter `name` + `description`.
There is no registry, no index, no manifest read at selection time.
→ **A skill with a broken `description` is invisible**, and no tool will tell you.

**Corpus citation contract:** every legal claim in a skill must resolve to an entry in
`research/egyptian-corpus/` carrying citation, Arabic title, status, provisions,
amendment chain, source URL, and an "as of" date. `🟡` items may not be stated as fact.

**Parity contract:** EN and AR twins must match on article numbers, law numbers, URLs,
heading order, markers, and figures — with the documented deliberate asymmetries
(see `schema.md`).

⚠️ **But only URL sets and structure are enforced as hard failures.** `validate.py` runs
the article/law-number comparison as a **warning**, because the extractor reads Arabic
that inflects, prefixes, abbreviates and uses list constructions, and it therefore has
documented blind spots. A warning means *a human should glance*, not *something is
broken*. **Do not edit Arabic content to silence a warning** without confirming against
the source that something is genuinely missing — a confident wrong fix is worse than the
warning, because nobody re-checks a thing that now looks right.

---

## 6. Validation + registration scripts

Both live in `.project-knowledge/scripts/`. Neither is sync-managed.

| Script | Purpose | Idempotent | Exit code |
|--------|---------|-----------|-----------|
| `validate.py` | All five checks: pairing, frontmatter/YAML, references, contamination, EN↔AR parity, plus registration | yes | **1 on failure** — CI-safe |
| `register-egypt.py` | Injects/restores the 12 Egypt plugin entries | yes (byte-identical) | non-zero on refusal |

```bash
python3 .project-knowledge/scripts/validate.py              # full run
python3 .project-knowledge/scripts/validate.py --no-parity   # skip the EN/AR diff
python3 .project-knowledge/scripts/validate.py --quiet       # failures only
```

`validate.py`'s docstring is the authoritative reference for **which findings are
FAIL vs WARN**, the excluded noise (glossary, brand names, `(Art N)` markers), and the
list of known extractor blind spots. It also holds the one Arabic detail that broke the
checker three separate times: `ال?` in a regex means "alif, then optional lam", **not**
"optional `ال`" — and in `للمادة` the preposition's lam assimilates into the definite
article, leaving no alif at all.
