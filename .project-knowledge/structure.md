# Project Structure

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-19

## File tree

```
awesome-legal-skills-Egy/
├── assets/
│   ├── lawve-logo.png
│   └── .lawve-sync.json                  ⛔ READ-ONLY — upstream sync map (264 tracked)
├── .claude-plugin/
│   └── marketplace.json                  ⚠️ GENERATED + 12 Egypt entries injected after
│                                           264 upstream. Regenerate with register-egypt.py
├── .github/
│   ├── FUNDING.yml
│   └── ISSUE_TEMPLATE/
├── .project-knowledge/
│   ├── INDEX.md                          ⭐ start here
│   ├── roadmap.md                        ⭐ pre-flight check — current goal + backlog
│   ├── schema.md, triggers.md, validators.md, systems.md, features.md,
│   │   integrations.md, structure.md, stack.md, history.md, sessions.md
│   └── scripts/
│       ├── validate.py                   ✅ all 5 checks + EN↔AR parity + registration
│       └── register-egypt.py             ✅ idempotent marketplace.json injector
├── CONTRIBUTING.md
├── EGYPT-EDITION.md                      ⭐ Egypt edition source of truth (190 lines)
├── LICENSE                               CC BY-NC-ND 4.0 (upstream)
├── README.md                             ⛔ sync block between LAWVE_SYNC_START/END
├── research/
│   └── egyptian-corpus/                  ⭐ THE FOUNDATION — every claim traces here
│       ├── 01-commercial-corporate-contract.md      864 lines
│       ├── 02-data-protection-privacy-consumer.md   801 lines
│       ├── 03-employment-courts-aml-banking.md    2,481 lines
│       ├── 04-practical-operations-egypt.md       1,485 lines
│       └── 05-tenancy-egypt.md                      725 lines
└── skills/                               288 dirs
    ├── <upstream-skill>/                 ⛔ DO NOT EDIT — 264 tracked, overwritten on sync
    ├── egy-<topic>/                      ✅ EN Egypt skill
    └── egy-<topic>-ar/                   ✅ AR twin of the above
```

**Legend:** ⛔ never write · ⭐ primary reference · ✅ yours to edit

---

## The 12 Egypt skill pairs

Every `egy-x` has exactly one `egy-x-ar`. Same topic, written natively in each
language — not a translation pair.

| Directory | Files | References |
|-----------|-------|-----------|
| `egy-context-operations` | SKILL, README | `GLOSSARY-EN-AR.md`, `PORTALS.md`, `PAYMENTS.md` |
| `egy-commercial-contract-review` | SKILL, README | `CLAUSE-CHECKS.md`, `DISPUTE-RESOLUTION.md` |
| `egy-ecommerce-compliance` | SKILL, README | `AUDIT-GRID.md`, `COPY-CHECKS.md` |
| `egy-legal-notice` | SKILL, README | `TEMPLATES.md` |
| `egy-company-setup` | SKILL, README | — |
| `egy-invoice-and-payment-terms` | SKILL, README | — |
| `egy-employment-contract` | SKILL, README | — (AR adds `TEMPLATES.md`) |
| `egy-employment-dispute` | SKILL, README | — |
| `egy-rental-agreement` | SKILL, README | — |
| `egy-tax-and-einvoicing` | SKILL, README | — |
| `egy-court-filing-guide` | SKILL, README | — |
| `egy-legal-research` | SKILL, README | — |

17 reference files across the edition. All resolve — verified.

---

## Key files

| File | Purpose | Why it matters |
|------|---------|----------------|
| `research/egyptian-corpus/` | Verified legislative corpus | **The citation rule says every legal proposition traces here.** Without it, skills cannot be written or checked |
| `EGYPT-EDITION.md` | Build conventions + roster | Source of truth for the roster. ✅ Its per-skill tables at lines 86–108 were stale and were **fixed 2026-10-19** — see `history.md` Fixed |
| `.project-knowledge/scripts/validate.py` | The validation gate | Run before every commit. Exit 1 on failure. **Read its docstring before acting on a warning** — it documents which findings are real and which are extractor blind spots |
| `.project-knowledge/scripts/register-egypt.py` | Marketplace registration | Idempotent — re-run after any upstream merge to restore the 12 Egypt plugin entries |
| `skills/egy-context-operations/references/GLOSSARY-EN-AR.md` | 92-term authoritative EN↔AR vocabulary | **Read before writing any Arabic.** Row 60 carries a corrected tenancy rule |
| `skills/egy-context-operations/references/PORTALS.md` | Every Egyptian portal, HTTP-tested | Carries the false-friend traps (`gcc.gov.eg`, `alqalam.idsc.gov.eg`) |
| `skills/egy-legal-research/SKILL.md` | The verification discipline | Records the Firecrawl failure mode and the source ladder |
| `assets/.lawve-sync.json` | Upstream digest map | Tells you which dirs are upstream-managed. **Read it before editing anything under `skills/`** |

---

## Entry points

There is no `main`. Entry is **the frontmatter `description`** of each `SKILL.md` —
that is the entire routing surface. See `triggers.md` for the routing map and
`schema.md` for the frontmatter contract.

The one file a human should read first: **`EGYPT-EDITION.md`**.
