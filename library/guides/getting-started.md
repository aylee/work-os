# Getting Started

You can use work-os in two phases:

1. Explore the fictional demo workspace.
2. Replace demo content with your real work.

## Start with the demo

The repo already includes:

- a sample weekly plan in `areas/work/plans.md`
- demo commitments and a backburner
- two example project binders under `desk/`

If you are using Claude Code, start with:

- `/desk` to see the current board
- `/open mobile-app-redesign` to open a demo binder
- `/brief activation experiment plan` to draft something against the
  existing structure

If you are using Codex, start by asking it to read `AGENTS.md`,
`docs/agent-guide.md`, `areas/work/plans.md`, and the demo binders, then
summarize the current desk state.

The point of the demo is not realism. It is to make the workflow
legible before you personalize it.

---

## You just ran `/setup`

`/setup` personalizes setup-owned files. It should not rewrite the
shared repo contract in `AGENTS.md`, `CLAUDE.md`, or
`docs/agent-guide.md`.

Here is what setup is meant to change:

**Identity** -- Your name, role, and company go into
`library/reference/me.md`. Drafting and editing skills use this to
understand who you are.

**Writing voice** -- If you provide writing samples, setup records voice
patterns in `library/reference/me.md`. If you skip this, defaults remain
until you refine them.

**Work area** -- `areas/work/AREA.md` becomes your context: company,
team, priorities, and operating conventions. Demo plans, commitments,
and backburner items can be replaced during setup or later.

**Desk** -- Your active projects become binders at `desk/{project}/`.
Each binder gets a `BINDER.md` manifest and can hold briefs, specs,
research, and working docs.

**Integrations** -- If you opt in, setup can create local integration
files such as `.claude/notion.yaml`. Those files should remain
untracked.

**Working state** -- For multi-session planning or implementation, keep
active notes in local `cc_state/`. Treat it as hot working state, not
committed memory.

---

## Your first day

Three good starting moves in Claude Code:

### `/desk`

Reads `areas/work/plans.md`, active binders, commitments, and
backburner items to synthesize the current state of work.

### `/open {project}`

Loads a binder and resumes project context from `BINDER.md`. Use this at
the start of any focused project session.

### `/brief {topic}`

Creates a structured draft from the repo's templates and references. Use
it when you need a 1-pager, proposal, or project brief quickly.

If you are working in Codex instead, the equivalent move is to point it
at the same files directly: binders in `desk/`, work context in
`areas/`, and shared rules in `AGENTS.md`.

---

## Your first week

### Build your writing voice

If you skipped voice calibration during setup, come back to it. Good
voice examples improve drafting quality fast.

Two ways to do it:

- Re-run `/setup` and choose the Voice section with 2-3 of your own docs
- Draft a few docs, edit them hard, and promote your best examples into
  the reference files over time

### Try `/review`

`/review` is the weekly closing loop. It compares planned work to actual
work, looks for open corrections, and updates the system.

The first run is light. The value comes from repetition.

### Try `/editor`

Write first, then polish. `/editor` is for tightening a file after the
substance is already right.

### Use `/shape` before big tasks

When the ask is fuzzy, start with `/shape`. It helps clarify the
problem, the expected output, and the real scope before you build.

---

## How the system compounds

work-os improves when you separate active working state from durable
memory:

```text
Work -> Capture -> Analyze -> Apply
```

**`cc_state/`** -- Local, untracked plans, traces, notes, and spikes for
active work across sessions.

**`memory/`** -- Committed corrections, decisions, reviews, and session
exports that should survive beyond the current task.

**`/review`** -- The point where patterns become system improvements in
skills, guides, and reference docs.

The goal is fewer open corrections over time.

---

## No git? No problem.

work-os works best with git, but it still works in a synced folder.

**What you lose without git:**
- `git log` history
- diff-based review habits
- some convenience in `/recent` and other file-activity workflows

**What still works:**
- the binder and area structure
- Claude slash commands
- Codex contract-based use through repo docs
- the memory system
- local `cc_state/` working state

If you add git later, just run `git init` in the repo root.
