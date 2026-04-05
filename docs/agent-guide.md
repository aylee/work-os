# Agent Guide

Detailed shared guidance for agents working in `work-os`.

## Purpose

work-os is a public starter repo for PMs, founders, and other knowledge
workers who want a structured workspace for agent-assisted planning,
writing, and project coordination. The repo is intentionally
markdown-first. It is not a dump of one person's private operating
system.

The public contract has two goals:
- A fresh clone should be useful immediately via fictional demo content.
- Personalization should happen in setup-owned files, not in repo-wide
  contracts.

## First Reads

Start with these files:
- `README.md` for the public quickstart and folder overview
- `AGENTS.md` for always-on repo invariants
- `areas/work/AREA.md` and `areas/work/plans.md` when the topic is
  current work state

## Repo Routing

Load the smallest relevant surface first.

| Topic | Read |
| --- | --- |
| A specific project | `desk/{project}/BINDER.md` |
| Work priorities and context | `areas/work/AREA.md` |
| Weekly focus | `areas/work/plans.md` |
| Commitments and follow-ups | `areas/work/commitments.md` |
| Backburner ideas | `areas/work/backburner.md` |
| Writing and editing defaults | `library/reference/me.md` and `library/reference/writing-guide.md` |
| File naming and lifecycle rules | `library/reference/conventions.md` |
| Past decisions | `memory/decisions/` |
| Open corrections | `memory/corrections/` |
| Session history | `memory/sessions/` |

## Folder Model

### `desk/`

Project binders live here. A binder is a directory with a `BINDER.md`
manifest plus any briefs, specs, research, and supporting artifacts for
that project.

Rules:
- Keep project-specific files inside the binder that owns them.
- Use `desk/z_archive/` for completed binders that should stay intact.
- When a user asks about a project, read the binder before inventing new
  context.

### `areas/`

Areas hold durable domain context. In the current starter repo, `work/`
is the main area and anchors weekly planning, commitments, and strategic
context.

### `library/`

`library/` contains reusable assets:
- `reference/` for durable reference material
- `templates/` for reusable document shells
- `guides/` for user education and setup docs
- `scripts/` for utility scripts
- `dotfiles/` for optional config files

### `memory/`

Committed memory lives here:
- `corrections/` for structured learnings and misfires
- `decisions/` for point-in-time rationale
- `reviews/` for weekly review output
- `sessions/` for exported transcripts

This is durable, committed memory. It is distinct from `cc_state/`.

## Demo Content and Personalization

Shipped content under `areas/`, `desk/`, and parts of `memory/` is demo
data. Treat it as fictional starter material.

Rules:
- Do not introduce real personal or company data into committed example
  files unless the user explicitly wants to personalize the repo.
- Prefer keeping public examples coherent and obviously fictional.
- Leave templates generic.
- Use `/setup` or direct edits to personalize setup-owned files such as
  `library/reference/me.md`, area docs, and binders.

## cc_state

`cc_state/` is local working state shared by Claude Code and Codex.
Create it locally per clone. Keep it out of git.

Recommended file types:
- `{topic}-plan.md` for multi-session plans
- `{feature}-trace.md` for decision traces during implementation
- `{topic}-notes.md` for working notes
- `{topic}-spike.md` for throwaway exploration

Rules:
- Keep only active material there.
- Do not commit `cc_state/` contents.
- Distill durable outcomes into repo docs, review files, or commit
  messages.
- Delete throwaway files when they stop being useful.
- Do not create a repo-local archive under `cc_state/`.

## Working Style

- Ask before destructive actions such as deleting files, force pushes,
  or removing example content.
- Routine read-only exploration is fine.
- Prefer updating the smallest relevant file set.
- Keep repo-wide contracts tool-neutral where possible.
- If a change affects both Claude Code and Codex behavior, update
  `AGENTS.md` or this guide before adding tool-specific instructions.

## Writing Workflow

The repo's writing workflow is:
1. Shape the request and scope.
2. Draft with the appropriate template or skill.
3. Iterate on substance in conversation.
4. Polish with editing guidance and examples.

Reference docs in `library/reference/` are shared inputs to that flow.

## Memory Workflow

The committed memory loop is:
1. Capture session outputs, corrections, or decisions.
2. Store them under `memory/`.
3. Review patterns and improve the system.
4. Apply the improvement in skills, docs, or conventions.

Corrections should trend downward over time. Durable patterns belong in
the committed repo, not in `cc_state/`.

## Optional Integrations

External tools such as Notion are optional. If configured, keep machine
readable integration settings under `.claude/` and avoid duplicating
private links or secrets across the repo.
