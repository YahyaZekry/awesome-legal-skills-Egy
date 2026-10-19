# awesome-legal-skills-Egy — Knowledge Index

> Last updated: **2026-10-19**
> Status: **Installable ✅ — 24 Egypt skills (12 EN/AR pairs) registered as 12 plugins**
> Stack: Markdown + YAML frontmatter · validated with `scripts/validate.py` (Python 3) · no runtime
> Current goal: **port more upstream skills and add Egypt-native topics (criminal
> procedure, family law, IP registration)** — the "make it installable" goal is **done**.

## What This Project Does

An **Egyptian-law edition** of the Lawve legal-skills catalog. It adds 12 practical
Egyptian topics — company setup, commercial contracts, employment, tenancy,
e-commerce, tax, court filing, legal notices and research — as **24 skills**
(12 English + 12 Arabic), each backed by a hand-verified legislative corpus.

It exists because the upstream catalog is US/EU-centric and the user is **not a
lawyer** working in Egypt. The skills are original work (`CC-BY-4.0`) written in new
`egy-*` directories; **no upstream skill is edited**, because the upstream sync
replaces tracked directories wholesale.

> **The core discipline:** every legal proposition traces to
> `research/egyptian-corpus/`. If the corpus marks something `🟡 UNVERIFIED`, the
> skill must say so rather than assert it. Research overturned **30+ widely-repeated
> facts** about Egyptian law to get here — four of them in the operator's own briefs.

---

## Files in This Folder

| File | Contents | Load when… |
|------|----------|------------|
| `stack.md` | What kind of project this is, content inventory, dev commands, env | Setting up, counting content, wondering why there's no build step |
| `structure.md` | File tree, the 12 skill pairs, key files, ⛔ read-only markers | Navigating the repo, adding a skill or reference file |
| `schema.md` | Skill directory contract, frontmatter schema, EN/AR pairing invariants, corpus format, confidence markers | Writing or editing any skill — **read first** |
| `triggers.md` | Routing map: which skill loads on what, deliberate adjacencies, planned-skill overlap risks | Before writing a new skill (avoid overlap) or debugging wrong-skill selection |
| `validators.md` | The five validation checks with working code, and **each one's false-positive modes** | Before committing anything; after any Arabic output |
| `systems.md` | The four systems: upstream sync (destructive), corpus-first research, EN/AR paired build, validation gate | Understanding *why* the workflow is shaped this way |
| `features.md` | What the edition covers by need, plus the legal findings that reshaped whole skills, and what was deliberately NOT ported | Onboarding, explaining the edition, checking whether a topic exists |
| `integrations.md` | Exa MCP, Firecrawl MCP, the upstream sync contract, `marketplace.json`, GitHub branches, exact data contracts | Touching research tooling, or registering/distributing skills |
| `roadmap.md` | **Current goal**, the 4 build tracks, known bugs, and the 25-item research backlog | **Before starting any task** — this is the pre-flight check |
| `history.md` | Removed items, 11 fixed defects, 16 architectural decisions | Debugging, reviewing why something is the way it is |
| `sessions.md` | Session-by-session log | Reviewing work history |
| `scripts/validate.py` | All five validation checks + EN↔AR parity + registration. **Exit 1 on failure — CI-safe.** Its docstring is the reference for FAIL-vs-WARN and known extractor blind spots | Before **every** commit; after any Arabic output |
| `scripts/register-egypt.py` | Injects/restores the 12 Egypt plugin entries in `.claude-plugin/marketplace.json`. **Idempotent** | After any `upstream/main` merge; when adding a new Egypt skill |

> Only files that exist are listed. `routes.md`, `hooks.md` and `components.md` were
> not created — this project has no routes, hooks or components. Their roles are
> filled by `triggers.md` and `validators.md`.

---

## Context Loading Guide

| Task | Load these files |
|------|-----------------|
| **Starting any task** | `roadmap.md` (know what's in flight) |
| Writing or editing a skill | `schema.md` + `triggers.md` + `history.md` |
| Writing an **Arabic** file | `schema.md` + `validators.md` + the glossary at `skills/egy-context-operations/references/GLOSSARY-EN-AR.md` |
| Adding a new Egypt topic | `triggers.md` (overlap check) + `schema.md` |
| **Making skills installable / registering plugins** | `integrations.md` §4 + `scripts/register-egypt.py` |
| Running the validation gate | `scripts/validate.py` (its docstring), then `validators.md` |
| Verifying or researching a citation | `systems.md` → corpus-first pipeline + `skills/egy-legal-research/` |
| Working with MCP research tools | `integrations.md` (⚠️ read the Firecrawl failure mode) |
| Touching anything under `skills/` | `integrations.md` → sync safety check **first** |
| Fixing a defect | `validators.md` + `history.md` |
| General orientation (new session) | This file → then pick by task |
| Full audit | All files |

---

## The four things a new session must not get wrong

1. **Never edit an existing upstream skill directory, and never add Egypt skills
   inside the `LAWVE_SYNC_START` / `END` README block.** 264 directories are
   sync-tracked by digest and replaced wholesale. Run the safety check in
   `integrations.md` before touching anything under `skills/`.

2. **Every legal claim traces to the corpus, and `🟡 UNVERIFIED` is never upgraded.**
   Egyptian law is amended often; a stale article number is a real harm. This is why
   `egy-tax-and-einvoicing` carries no rates and `egy-court-filing-guide` refuses to
   quote a fee figure.

3. **Arabic output must pass the contamination scan before commit.** It has corrupted
   five separate times — stray Cyrillic, CJK, Portuguese fragments, digit runs,
   duplicated words, half-finished sentences. Blockquote templates are the highest
   risk. See `validators.md` — and read its false-positive section, because the scan
   reported 188 issues in one run and only **two** were real.

4. **Never edit Arabic content to silence a `validate.py` warning.** Warnings are
   `review:` or `drift:`. The extractor reads Arabic that inflects, prefixes, abbreviates
   and uses list constructions, so it has documented blind spots — in the session that
   built it, the checker reported **29 failures of which zero were real**. Fix the
   extractor, or confirm against the source that something is genuinely missing. A
   confident wrong fix is worse than the warning, because nobody re-checks a thing that
   now looks right.

---

*Maintained with [project-knowledge](https://github.com/YahyaZekry/project-knowledge-skill) · by [Yahya Zekry](https://github.com/YahyaZekry)*
