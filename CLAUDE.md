# {USER_NAME}'s OS

Repo-first personal operating system. Notion is the database layer (horizons of focus, tasks, relational views). work-os is the working surface (binders, specs, reference) and memory (feedback loop).

> Run `/setup` to personalize this system.

## Preferences

- Ask before doing anything destructive (deleting files/branches, pushing, committing, force operations).
- Routine read-only stuff (searching, reading files, running tests) is fine without asking.

## Routing Table

| When the topic involves... | Load... |
|---|---|
| A specific project | Binder: `desk/{project}/BINDER.md` |
| A domain (e.g., work context, team structure) | Area: `areas/{domain}/AREA.md` |
| Project status, strategy, what's on the desk | `areas/work/AREA.md` |
| Weekly focus, what matters this week | `areas/work/plans.md` |
| Goals, OKRs, quarterly planning | Notion Goals database (if `.claude/notion.yaml` configured) |
| Mission, purpose, vision, life direction | Notion Visions database (if `.claude/notion.yaml` configured) |
| Daily/weekly/quarterly rhythms | Notion (if configured) or ask the user |
| Writing, drafting, editing | `library/reference/me.md` + `library/reference/writing-guide.md` |
| Mental models, decision patterns | `library/reference/frameworks.md` |
| Notion databases, system config | `.claude/notion.yaml` (if configured) |
| Info architecture across systems | `library/reference/info-architecture.md` |
| Past decisions, why we chose X | `memory/decisions/` |
| Corrections, what went wrong + why | `memory/corrections/` (individual files) |
| Meeting notes | Notion meeting-notes DB (if `.claude/notion.yaml` configured), fetch with `include_transcript: true` |
| Session history, cross-repo search | `memory/sessions/` + `/sessions` skill |
| What do I owe someone, commitments, action items | `areas/work/commitments.md` |
| Backburner ideas queued by person | `areas/work/backburner.md` |
| File naming, frontmatter, lifecycle | `library/reference/conventions.md` |

## Project Binders

Active workstreams live in **binders** — directories with a `BINDER.md` manifest at `desk/` root. Everything on the desk is a binder. Use a consistent org prefix (e.g., `acme-`) for work projects to distinguish them from personal ones. When a project ships, its binder moves whole to `desk/z_archive/`.

**When a user mentions a project, check for a matching binder first.** Read its BINDER.md for status, context, and where they left off.

**Session-end behavior:** Before ending a project work session, ask three things: (1) update the Last Session in BINDER.md? (2) anything the system got wrong, or an insight worth capturing? If yes, create a file in `memory/corrections/`. (3) any decisions worth logging? If yes, write to `memory/decisions/`.

**Creating files:** When skills target a project with an active binder, create files inside that binder directory. Check `desk/{project}/BINDER.md`.

## Folder Structure

Each top-level directory has an L2 entry point: areas/ use AREA.md, desk/ uses BINDER.md, memory/ uses corrections/. L3 data loads from within each module.

```
desk/              Active project binders (ls desk/ = projects)
  z_archive/       Shipped binders, intact
areas/             Life domains (AREA.md in each)
  work/
    AREA.md        Domain context (company, strategy, Big Rocks, metrics)
    plans.md       Rolling weekly/monthly intentions
    backburner.md  Ideas queued by person
library/           All reference material
  reference/       Core reference docs (me, frameworks, conventions, etc.)
  templates/       Document blueprints
  guides/          How-tos and cheatsheets
  scripts/         Executable tools (export-session.py, etc.)
  dotfiles/        Config files symlinked to ~/
memory/            Compounding feedback loop
  corrections/     Structured corrections (individual files with frontmatter)
  decisions/       Point-in-time "why we chose X"
  reviews/         Weekly synthesis from /review
  sessions/        Auto-exported transcripts from all repos
scratch/           Throwaway thinking
```

## Using Notion

Notion is the database layer — horizons of focus (Visions > Goals > Areas > Projects > Tasks), meeting notes, and relational views all live there. work-os doesn't replicate the graph; areas point TO Notion for detail.

> Notion integration is optional. If you don't use Notion, skip this section. If you do, copy `.claude/notion.yaml.example` to `.claude/notion.yaml` and fill in your database URLs.

- **Use links first**: `.claude/notion.yaml` has database URLs. Use `notion-fetch` directly.
- **Search when exploring**: `notion-search` when no link exists.
- **Don't duplicate**: Summarize and link.
- **Write-back is opt-in**: Only create Notion pages if the user explicitly asks.

## Writing Workflow

Drafting and editing are separate stages with distinct context budgets.

| Stage | Skills | Job | Loads |
|-------|--------|-----|-------|
| Shape | /shape | Define scope and intent | Domain context |
| Draft | /rfc, /brief, /spec, /research, /decision | Substance + coverage (the marble block) | Template + me.md + domain context |
| Iterate | (conversation) | Add, remove, restructure, sharpen | Whatever's needed |
| Polish | /editor | Voice, formatting, sentence craft | All 4 reference files |

Drafting skills don't load voice/formatting references. `/editor` does.

## Memory System

Durable memory lives in `memory/`. The system improves through a feedback loop: capture > store > analyze > apply.

| Layer | Location | Purpose | Written by |
|-------|----------|---------|------------|
| Sessions | `memory/sessions/` | Auto-exported transcripts from all repos | `export-session.py` or `/sessions export` |
| Corrections | `memory/corrections/` | What went wrong + why (structured frontmatter) | Session-end capture |
| Decisions | `memory/decisions/` | Point-in-time "why we chose X" | When a design choice is made |
| Reviews | `memory/reviews/` | Weekly synthesis, pattern detection | `/review` |

**The loop:**
1. **Capture** — Sessions auto-export. Corrections captured during sessions. Decisions logged when made.
2. **Store** — Sessions are append-only (never delete). Corrections are individual files with `status: open`. Decisions are permanent.
3. **Analyze** — `/review` scans corrections by domain, groups patterns, compares with sessions. Proposes system changes.
4. **Apply** — Make the change (skill, CLAUDE.md, reference doc). Delete resolved corrections (git has history). Write review to `memory/reviews/`.

**Correction format:**
```yaml
---
date: YYYY-MM-DD
domain: tooling | writing | architecture | workflow | naming | conventions
status: open | applied | retracted
source: session | reflection | user
---
## What happened
## Should have been
## Why
```

**Lifecycle:** Corrections trend toward empty — fewer open corrections = system improving.
When resolved: `applied` (system change made, delete file) or `retracted` (wrong, delete file).

## Plan Mode

- **Understand the request before planning.** If the problem, intent, or expected output is unclear, ask first.
- **Surface assumptions and open questions before finalizing.** Don't paper over ambiguity.
- **Check for existing work.** Search binders, Notion, and `memory/decisions/` before proposing new approaches.
