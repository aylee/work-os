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
- Sessions 3-5 remain queued.

## Session Checklist

- [x] Session 1: Add `AGENTS.md`, add `docs/agent-guide.md`, reduce
  `CLAUDE.md` to a shim, ignore `cc_state/`, verify ignored working
  state.
- [x] Session 2: Rewrite README and onboarding docs for the PM/founder
  starter audience.
- [ ] Session 3: Sanitize demo content and placeholder leakage.
- [ ] Session 4: Add OSS maintainer hygiene and audit checks.
- [ ] Session 5: Add upstream sync process for portable patterns from
  `alex-os`.

## Notes

- `cc_state/` is local and intentionally untracked.
- Durable decisions belong in committed docs, not here.
