# Work-OS

work-os is an opinionated starter workspace for knowledge workers using
Claude Code and Codex. It ships with fictional demo content so a fresh
clone can exercise the workflow immediately, then `/setup` can
personalize the repo for real use.

## First Reads
- `README.md` for user-facing orientation and quickstart
- `docs/agent-guide.md` for the detailed shared repo guide

## Working State
`cc_state/` is hot local working state shared by Claude Code and Codex.
It is intentionally untracked and should never contain committed files.

Allowed file shapes:
- `{topic}-plan.md`
- `{feature}-trace.md`
- `{topic}-notes.md`
- `{topic}-spike.md`

Rules:
- Keep only active work in `cc_state/`.
- Distill completed reasoning into committed docs or commit messages.
- Delete or cool stale working notes manually; do not create
  `cc_state/archive/`.

## Public Repo Guardrails
- Keep committed content reusable and free of personal data.
- Treat shipped binders and area files as fictional examples, not user
  history.
- Leave placeholders only in reusable templates or setup-owned starter
  files.

## Repo Model
- `desk/` holds project binders. Every active project directory should
  include a `BINDER.md` manifest.
- `areas/` holds durable domain context such as work priorities and
  commitments.
- `library/` holds reusable reference docs, templates, guides, scripts,
  and dotfiles.
- `memory/` holds committed corrections, decisions, reviews, and session
  exports.
- When a user mentions a project, check for a matching binder first and
  keep new project artifacts inside that binder.

## Safety
- Ask before destructive actions such as deleting files, force-pushing,
  rewriting history, or removing example content.
- Routine read-only exploration and verification are fine without asking.

## Reference
Detailed shared guidance lives in `docs/agent-guide.md`.
