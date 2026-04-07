# Maintainer Workflow

work-os is a public starter repo for PMs, founders, and other knowledge
workers. This guide is the canonical workflow for maintaining,
syncing, auditing, and publishing the repo. It should be enough to
maintain work-os without private `alex-os` docs.

Start here when you are:

- changing repo-wide contracts or starter positioning
- refreshing shipped demo content
- porting a pattern from `alex-os`
- cutting a public starter refresh or release

Use this guide with `library/guides/maintainer-hygiene.md`, which
covers the public-hygiene audit in more detail.

## Where maintainer knowledge lives

- `library/guides/maintainer-workflow.md` is the canonical maintainer
  workflow and upstream-sync runbook.
- `library/guides/maintainer-hygiene.md` documents the audit and
  allowlist rules for public demo hygiene.
- `AGENTS.md` and `docs/agent-guide.md` are the shared repo contract for
  Claude Code, Codex, and human maintainers.
- `memory/decisions/` holds durable maintainer decisions when the
  rationale will not be obvious from the diff alone.
- `memory/corrections/` holds misses or cleanup follow-ups that should
  change future maintainer behavior.
- `cc_state/` is local working state for active sync notes, plans, and
  traces. It is never the canonical source of truth.

## How agents should use this guide

- Read this guide before making repo-wide, release-facing, or
  upstream-sync changes.
- Prefer the smallest file set that makes the workflow legible in
  public.
- If a change updates the maintainer process itself, update this guide
  and any entry-point docs in the same commit.
- If a decision needs to persist beyond the current session, write it to
  `memory/decisions/` instead of leaving it in `cc_state/`.

If a maintainer cannot explain a change from work-os alone, the change
is not ready for the public repo.

## Canonical maintenance loop

1. Start from the public contract. Re-read `README.md`, `AGENTS.md`, and
   `docs/agent-guide.md` when a change affects onboarding, repo
   structure, or cross-tool behavior.
2. Define the public outcome in work-os terms. The change should make
   the starter clearer, more reusable, or easier to operate for PMs and
   founders.
3. Route the change to the right place. Use `library/guides/` for
   maintainer or user docs, `library/templates/` for reusable shells,
   `desk/` and `areas/` for coherent fictional demo content, and
   `memory/` for durable learnings.
4. Run the hygiene and review checks before publishing.
5. Commit the scoped change. Publish only after the public diff is
   understandable without private `alex-os` context.

## `alex-os` and `work-os`

`alex-os` is an upstream source of patterns, not an alternate source of
truth for this repo. work-os must stand on its own as a public starter.

### Patterns that are portable

- repo structure or binder/area/memory patterns that improve the public
  workflow
- tool-neutral agent contracts and routing rules
- reusable templates, scripts, and checklists that do not depend on
  private context
- workflow examples whose shape is useful and can be rewritten as
  coherent fictional starter content

### Patterns that must be adapted before porting

- docs that mention personal habits, company context, internal cadence,
  or private tooling
- examples that assume a private workspace, private links, or user
  history
- tool-specific instructions that need to be translated into
  cross-tool repo guidance
- demo content that needs to match the current PM/founder starter voice
  and fictional workspace

### Material that should never port directly

- real names, companies, client work, private URLs, credentials, or
  integration secrets
- raw personal memory, working notes, backlogs, or session exports
- docs that require access to `alex-os` or other private context to make
  sense
- internal-only workflows that would turn work-os into a personal
  operating system instead of a reusable public starter

## Interactive sync review

When reviewing `alex-os` in a live session, walk the tree top-down and
classify each candidate as `port now`, `port after rewrite`, or `leave
in alex-os`.

Ask the same questions for every candidate:

1. What public problem would this solve in work-os?
2. Is the value in the pattern, the example content, or the exact file?
3. Where would the public version live: repo contract, guide, template,
   script, skill, demo content, or nowhere?
4. What private context must be stripped or rewritten before this can
   ship?
5. Does the result preserve the PM/founder starter positioning?
6. What is the lightest public version worth bringing over?
7. How will we verify that it landed cleanly in work-os?

Default triage by area:

- root docs and repo contract: usually portable if they clarify public
  workflow; rewrite any private references or internal assumptions
- `.claude/skills/`: port only skills that are broadly useful in the
  public starter and do not depend on private data or internal systems
- `library/guides/` and `library/templates/`: often portable after
  sanitizing examples and tightening scope
- `library/scripts/`: port safe repo-local automation; leave behind
  scripts tied to private services, personal directories, or internal
  tooling
- `areas/` and `desk/`: port structure and patterns, not real history;
  rewrite examples as coherent fictional starter content
- `memory/`: almost never port directly; distill only reusable
  decisions, corrections, or patterns into public docs
- `cc_state/`, scratch files, local config, and integration secrets:
  never port

## Upstream-sync runbook

### 1. Source selection

- Choose a small, explicit pattern or improvement from `alex-os`, not a
  bulk copy.
- Prefer changes that strengthen the public PM/founder starter:
  onboarding, structure, reusable templates, tool-neutral agent
  behavior, or safe automation.
- Skip changes whose value depends on private history or private docs.
- Capture the sync intent in the commit series or a local
  `cc_state/{topic}-notes.md` file while the work is active.

### 2. Adaptation review

- Rewrite the change in work-os terms before editing: what public
  problem does it solve, and where should that knowledge live?
- Remove or replace private names, links, schedules, and assumptions.
- Convert personal examples into coherent fictional demo content, or
  move the idea into templates or guides if examples would imply real
  history.
- Check starter positioning. The result should still read like a public
  starter for PMs and founders, not a dump of `alex-os` internals.
- When the rationale is non-obvious or changes maintainer policy, add a
  durable note in `memory/decisions/`.

### 3. Hygiene and audit checks

- Run `python3 library/scripts/audit_public_hygiene.py`.
- Review the diff for leaked private context, placeholder residue, and
  demo-story drift across `areas/`, `desk/`, and `memory/`.
- Confirm any new generic scaffolding belongs only in setup-owned files
  or reusable templates.
- Verify repo-wide contract changes also updated the relevant shared
  docs.

### 4. Commit and publish

- Commit the work with a scoped message that explains the public change,
  not the private source.
- Keep commits reviewable. Separate broad demo rewrites from maintainer
  or runbook changes when possible.
- Before a public push or tag, make sure the repo is understandable from
  work-os alone.
- Push or tag only when ready. work-os does not depend on a private
  `alex-os` publish step.

## Lightweight publish checklist

- Canonical docs still point to the right maintainer workflow.
- Demo content remains fictional and coherent.
- The hygiene audit passes.
- The diff is reviewable without private context.
- Any durable policy change is captured in `memory/decisions/`.
