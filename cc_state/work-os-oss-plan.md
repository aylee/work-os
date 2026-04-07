---
status: active
created: 2026-04-05
---

# Work-OS OSS Upgrade Plan

Local tracker for the staged OSS cleanup.

## Current Status

- Session 1 is complete: cross-agent contract, `cc_state/`, and shared
  agent guide are in place.
- Session 2 is complete: README, onboarding docs, tooling guidance, and
  `/setup` expectations now match the public PM/founder starter
  positioning.
- Session 3 is complete in `a52ff6b`: sanitize demo workspace and
  placeholder residue.
- Session 4 is complete in `b6d5322`: add maintainer hygiene audit,
  maintainer guidance, and install/onboarding refresh. README follow-up
  cleanup was pushed in `180930b`.
- Session 5 is next and should be reframed around the maintainer
  workflow plus upstream sync runbook, not just raw pattern porting.

## Session Checklist

- [x] Session 1: Add `AGENTS.md`, add `docs/agent-guide.md`, reduce
  `CLAUDE.md` to a shim, ignore `cc_state/`, verify ignored working
  state.
- [x] Session 2: Rewrite README and onboarding docs for the PM/founder
  starter audience.
- [x] Session 3: Sanitize demo content and placeholder leakage.
- [x] Session 4: Add OSS maintainer hygiene and audit checks.
- [ ] Session 5: Document the maintainer workflow and upstream sync
  process for portable patterns from `alex-os`.

## Session 5 Scope

- Define where the canonical work-os maintainer workflow lives in the
  repo.
- Document how to evaluate changes in `alex-os` for portability before
  bringing them into work-os.
- Add a lightweight maintainer runbook for sync, review, audit, and
  publish steps.
- Record guardrails for what should never port directly from `alex-os`
  into the public starter.

## Notes

- `cc_state/` is local and intentionally untracked.
- Durable decisions belong in committed docs, not here.

## Session 6 Prep

Goal: close the loop on Session 5 by reviewing `alex-os` interactively
and deciding what to port, what to rewrite, and what to leave private.

Suggested flow:

1. Walk `alex-os` top-down by area: root docs, `.claude/skills/`,
   `library/`, `areas/`, `desk/`, `memory/`, and local-only state.
2. For each candidate, classify it as `port now`, `port after rewrite`,
   or `leave in alex-os`.
3. Capture only durable outcomes in committed work-os docs. Keep raw
   exploration here in `cc_state/` while the review is active.

Question set for the interactive pass:

1. What public problem would this solve in work-os?
2. Is the value in the pattern, the example content, or the exact file?
3. Where would the public version live in work-os?
4. What private context must be stripped or rewritten first?
5. Does it preserve the PM/founder starter positioning?
6. What is the lightest public version worth bringing over?
7. How will we verify that it landed cleanly?
