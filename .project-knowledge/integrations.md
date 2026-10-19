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
Registering Egypt entries in `marketplace.json` is viable, but expect a conflict on the
next upstream merge. Verify this assumption before relying on it.

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
| `plugins` | 264 entries across 26 categories |
| Plugin shape | `{name, source, description, version, author, license, category, skills[], strict}` |
| Egypt entries | **0** |

Each plugin points at one skill directory: `"skills": ["./skills/<name>"]`.

→ **Egypt skills are invisible to the plugin system.** They exist on disk only. Making
them installable is tracked in `roadmap.md`.

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
