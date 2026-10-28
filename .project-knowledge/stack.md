# Stack

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-29

## What kind of project this is

**Not an application.** There is no runtime, no build step, no dependency file, no
test suite. The deliverable is **Markdown that an AI agent reads**, plus a research
corpus that the Markdown must trace to.

The "runtime" is a Claude/opencode session that selects a skill by matching its
`name` + `description` frontmatter against the user's prompt, then loads `SKILL.md`
into context. Everything else is supporting material the agent reads on demand.

| Category | Details |
|----------|---------|
| Content format | Markdown + YAML frontmatter (Anthropic Skills standard) |
| Languages | English + Modern Standard Arabic (native-written, not translated) |
| Validation | `scripts/validate.py` — Python 3 + PyYAML, **checked in**, exit 1 on failure |
| VCS | git, branch `egypt-edition`, remote `origin` = YahyaZekry fork |
| Upstream | `upstream` = `lawve-ai/awesome-legal-skills` |
| Research tooling | Exa MCP + Firecrawl MCP |
| Distribution | `.claude-plugin/marketplace.json` — **19 Egypt plugins registered** (264 upstream + 19 = 283) |
| Deployment | None. Consumers clone or install as a Claude Code plugin |

---

## Content inventory

| Metric | Value |
|--------|-------|
| Egypt skills | 38 directories (19 EN + 19 AR) |
| Egypt markdown files | 76 |
| Egypt markdown lines | 15,683 |
| Corpus files | 10 committed |
| Corpus lines | 12,902 committed |
| Upstream skill dirs | 302 in `skills/` (264 sync-tracked + 38 Egypt) |

---

## Dev commands

All commands run from the repo root. There is no `make`, no `npm script` — these are
the literal invocations used during the build.

| Command | What it does |
|---------|--------------|
| `git log --oneline -10` | Recent history |
| `find skills/egy-* -name '*.md' \| wc -l` | Count Egypt content |
| **`python3 .project-knowledge/scripts/validate.py`** | **The gate — run before every commit.** Exit 1 on failure |
| `python3 .project-knowledge/scripts/validate.py --no-parity` | Fast pass without the EN/AR diff |
| **`python3 .project-knowledge/scripts/register-egypt.py`** | Register/restore the 19 Egypt plugins (per-plugin versions). Idempotent |
| `python3 .project-knowledge/scripts/register-egypt.py --check` | Dry run of the above |
| `git push origin egypt-edition` | Publish (see `integrations.md` for the PR link) |

⚠️ **Never run a formatter, linter, or mass-rewrite over `skills/`** — 264 of the 302
directories are upstream-managed and will be overwritten by the next sync anyway.
Only ever touch `skills/egy-*`.

---

## Environment variables

None. No `.env`, no secrets in the repo.

The two API keys used during the build (Firecrawl, Exa) live in the **operator's
global opencode config**, not here:

| Variable | Used in | What it enables |
|----------|---------|-----------------|
| Firecrawl key | `~/.config/opencode/opencode.jsonc` — remote MCP, Bearer header | Scraping Egyptian government portals and gazette PDFs |
| Exa key | `~/.config/opencode/opencode.jsonc` — local stdio `exa-mcp-server`, key in env | Semantic discovery of statutes and articles |

⚠️ A Firecrawl key was pasted in plaintext in an earlier session. If this repo is ever
made public with the session history attached, **rotate it**.

---

## Why there is no linter

Every class of error this project actually produces is invisible to a Markdown
linter:

- A wrong **article number** is valid Markdown
- A **contaminated Arabic token** (Cyrillic/CJK fragment) is valid UTF-8
- A heading saying *"three"* over a four-item list is valid Markdown
- A skill citing a **repealed statute** is valid Markdown

So the checks that earn their place are bespoke and content-aware — see
`validators.md`, which lists each one and, importantly, which ones are noisy.
