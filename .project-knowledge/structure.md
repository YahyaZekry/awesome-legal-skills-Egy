# Project Structure

> Part of awesome-legal-skills-Egy/.project-knowledge/ | Last updated: 2026-10-29

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
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
│       └── validate.yml                  ✅ runs validate.py + register-egypt.py --check
├── .project-knowledge/
│   ├── INDEX.md                          ⭐ start here
│   ├── roadmap.md                        ⭐ pre-flight check — current goal + backlog
│   ├── schema.md, triggers.md, validators.md, systems.md, features.md,
│   │   integrations.md, structure.md, stack.md, history.md, sessions.md
│   └── scripts/
│       ├── validate.py                   ✅ all 5 checks + EN↔AR parity + registration
│       └── register-egypt.py             ✅ idempotent marketplace.json injector
├── CONTRIBUTING.md
├── EGYPT-EDITION.md                      ⭐ Egypt edition source of truth (228 lines)
├── LICENSE                               CC BY-NC-ND 4.0 (upstream)
├── README.md                             ⛔ sync block between LAWVE_SYNC_START/END
├── research/
│   └── egyptian-corpus/                  ⭐ THE FOUNDATION — every claim traces here
│       ├── 01-commercial-corporate-contract.md      864 lines
│       ├── 02-data-protection-privacy-consumer.md   801 lines
│       ├── 03-employment-courts-aml-banking.md    2,481 lines
│       ├── 04-practical-operations-egypt.md       1,485 lines
│       ├── 05-tenancy-egypt.md                      725 lines
│       ├── 06-criminal-procedure-egypt.md         1,715 lines
│       ├── 07-family-law-egypt.md                 1,818 lines
│       ├── 08-intellectual-property-egypt.md      1,336 lines
│       ├── 09-real-estate-purchase-egypt.md         794 lines
│       └── 10-debt-recovery-egypt.md                778 lines
└── skills/                               302 dirs
    ├── <upstream-skill>/                 ⛔ DO NOT EDIT — 264 tracked, overwritten on sync
    ├── egy-<topic>/                      ✅ EN Egypt skill   (19)
    └── egy-<topic>-ar/                   ✅ AR twin of the above (19)
```

**Legend:** ⛔ never write · ⭐ primary reference · ✅ yours to edit

---

## The 19 Egypt skill pairs

Every `egy-x` has exactly one `egy-x-ar`. Same topic, written natively in each
language — not a translation pair. ⚠️ The newer topics (Track 3) ship **SKILL.md
only** — the earlier EN skills carry a README, and `references/` exists only where
the material is reusable (19 reference files across the edition, all resolve).

| Directory | EN files | AR files | References |
|-----------|-------|-----------|------------|
| `egy-context-operations` | SKILL, README | SKILL | GLOSSARY-EN-AR, PORTALS, PAYMENTS — **both languages** |
| `egy-commercial-contract-review` | SKILL, README | SKILL, README | CLAUSE-CHECKS, DISPUTE-RESOLUTION, RISK-GRID — **both languages** |
| `egy-ecommerce-compliance` | SKILL, README | SKILL | AUDIT-GRID, COPY-CHECKS — **both languages** |
| `egy-legal-notice` | SKILL, README | SKILL | TEMPLATES — **both languages** |
| `egy-employment-contract` | SKILL, README | SKILL | TEMPLATES — **AR only** |
| `egy-company-setup` | SKILL, README | SKILL | — |
| `egy-invoice-and-payment-terms` | SKILL, README | SKILL | — |
| `egy-employment-dispute` | SKILL, README | SKILL | — |
| `egy-rental-agreement` | SKILL, README | SKILL | — |
| `egy-tax-and-einvoicing` | SKILL, README | SKILL | — |
| `egy-court-filing-guide` | SKILL, README | SKILL | — |
| `egy-legal-research` | SKILL, README | SKILL | — |
| `egy-client-explanation` | SKILL, README | SKILL | — |
| `egy-chronology-builder` | SKILL, README | SKILL | — |
| `egy-criminal-procedure` | SKILL | SKILL | — |
| `egy-ip-registration` | SKILL | SKILL | — |
| `egy-family-law` | SKILL | SKILL | — |
| `egy-real-estate-purchase` | SKILL | SKILL | — |
| `egy-debt-recovery` | SKILL | SKILL | — |

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
