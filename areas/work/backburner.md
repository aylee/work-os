---
type: reference
---

# Backburner

Ideas and asks queued by person. Pull when they have capacity.

## Marcus
- Investigate WebSocket connection pooling -- current implementation creates a new connection per session, probably fine at our scale but will bite us at 10x
- Prototype offline mode for mobile -- multiple customer requests, unclear if worth the complexity

## Priya
- Design system audit -- component library has diverged between web and mobile, creating inconsistencies
- Explore animated micro-interactions for onboarding (could layer onto the redesign)

## Taylor
- Build a self-serve revenue dashboard for the exec team -- they keep asking for the same cuts of data
- Document the attribution model -- only Taylor understands how it works

## Unassigned
- API rate limiting overhaul -- current limits are per-key, should be per-org
- Audit notification preferences -- users can't control what emails they get
