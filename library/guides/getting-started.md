# Getting Started

You just cloned work-os. Here's how to make it yours and start getting value from it.

---

## You just ran `/setup`. Here's what happened.

The `/setup` wizard walked you through five steps. Here's what each one created:

**Identity** -- Your name, role, and company were written to `library/reference/me.md`. This is the file Claude reads to understand who you are. Every writing skill (`/brief`, `/spec`, `/rfc`) loads it before drafting.

**Writing voice** -- If you provided writing samples, your voice patterns were extracted and saved to `library/reference/me.md` under the Voice section. If you skipped this, defaults were used -- your voice profile will build naturally as you use `/editor`.

**Areas** -- Your work context (`areas/work/AREA.md`) was filled with your company context, team structure, and quarterly priorities. These are the "standards" Claude references when your work touches those domains.

**Desk** -- Your active projects became binders at `desk/{project}/BINDER.md`. Each binder is a working directory -- specs, briefs, research, and decisions all live alongside the manifest. This is where the work happens.

**Integrations** -- If you connected Notion, Linear, or Slack, those were configured in `.claude/notion.yaml` and `.claude/settings.json`. Skills will use these for context gathering.

---

## Your first day

Three commands to try right now:

### `/desk` -- See the whole board

This is your daily orientation. It reads your weekly plan (`areas/work/plans.md`), scans active binders, checks your backburner, and suggests what to focus on today. If no weekly plan exists, it offers to help you write one.

Try it: just type `/desk`.

### `/open {project}` -- Start a work session

This loads a project binder -- its full context, where you left off, and what files are available. Think of it as opening a project folder with memory. When you're done, it offers to update the "Last Session" so your next session picks up where you left off.

Try it: `/open` followed by any of your project names.

### `/brief {topic}` -- Write something useful

If you have a project that needs a brief, spec, or proposal, try writing one. `/brief` loads the template, pulls context from your work area and Notion (if configured), and produces a structured draft.

Try it: `/brief` followed by a topic, like `/brief api migration plan` or `/brief q4 feature prioritization`.

---

## Your first week

### Build your writing voice

If you skipped the voice calibration during setup, come back to it. The system writes better docs when it knows your patterns.

Option 1: Re-run `/setup` and choose the Voice section. Paste 2-3 of your best docs.

Option 2: Write a few docs using `/brief`, `/spec`, or `/rfc`, then run `/editor` on each one. Make your edits. Over time, the voice-examples and doc-examples files build into a calibration library.

### Try `/review` at the end of the week

`/review` is the weekly review skill. It compares what you planned to what you actually did, surfaces open corrections, reviews the backburner and commitments, and writes a review to `memory/reviews/`. Then it sets up next week.

The first time you run it, there won't be much history. That's fine. The value compounds -- after a month, you have a searchable log of what you worked on, what shipped, and what got carried forward.

### Try `/editor` on a draft

Write something with `/brief` or `/spec`, then run `/editor` on the file. The editor loads all four reference files (me.md, writing-guide.md, voice-examples.md, doc-examples.md) and makes a tightening pass -- formatting, voice, filler words, structure. It's the "polish" step in the writing workflow.

### Use `/shape` before big tasks

When someone asks you to "figure out the thing," start with `/shape`. It interrogates the problem, intent, context, and expected output before you start building. Think of it as requirements gathering for yourself. The output is a brief-back that you confirm before proceeding.

---

## How the system compounds

work-os gets better the more you use it. Here's the feedback loop:

```
  Work happens (sessions, decisions, docs)
       |
       v
  Capture (corrections, decisions, session exports)
       |
       v
  Analyze (/review scans patterns weekly)
       |
       v
  Apply (update skills, CLAUDE.md, reference docs)
       |
       v
  Better work next time
```

**Sessions** -- Every Claude Code conversation can be exported to `memory/sessions/`. These become searchable transcripts. "What did I discuss about pricing last month?" becomes answerable.

**Corrections** -- When something goes wrong (Claude misunderstands your intent, follows a bad pattern, or produces the wrong output), capture it in `memory/corrections/`. Each correction is a structured file with what happened, what should have happened, and why.

**Decisions** -- When you make a meaningful choice, record it with `/decision`. Six months from now, when someone asks "why did we choose X?", the answer is in `memory/decisions/`.

**Reviews** -- `/review` synthesizes the week, archives corrections that have been addressed, and proposes system improvements. Over time, `memory/reviews/` becomes a log of how your working system has evolved.

The key insight: corrections trend toward empty. Fewer open corrections means the system is improving. The goal is a system that makes fewer mistakes over time because it learns from the ones it made.

---

## No git? No problem.

work-os is designed for git, but it works without it. If you prefer a cloud-synced folder:

**Google Drive:**
Place the work-os folder in your Google Drive. Everything syncs automatically. You lose git history (no `git log`, no `git diff`), but the file structure and skills work the same.

**Dropbox:**
Same approach. Drop the folder in Dropbox. Session exports and corrections still work -- they're just markdown files.

**iCloud Drive:**
Place in `~/Library/Mobile Documents/com~apple~CloudDocs/work-os/`. Works, but iCloud's sync can be slow with many small files.

**What you lose without git:**
- `git log` history (no "when did I change this?")
- `/recent` skill (relies on git history for file activity)
- Diff-based review in `/review`
- Atomic commits as checkpoints

**What still works:**
- All skills (`/desk`, `/open`, `/brief`, `/spec`, `/rfc`, `/research`, `/decision`, `/editor`, `/shape`, `/review`)
- The full memory system (corrections, decisions, reviews, sessions)
- Weekly planning and orientation
- Writing workflow

If you start without git and want to add it later, just run `git init` in the root directory. All your files become the first commit.
