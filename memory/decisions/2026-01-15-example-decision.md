# Decision: API Versioning Strategy

**Date:** 2026-01-15
**Status:** Decided
**Decided by:** [Your Name], Marcus Chen

---

## Context

We're about to launch our public API and need to decide on a versioning strategy before the first external consumer goes live. Once we ship v1, changing the strategy becomes exponentially harder -- every external integration is a contract we can't easily break.

Three constraints shaped this decision:
1. We have 4 external partners waiting to integrate (Q2 launch commitment)
2. Our internal API changes frequently (~3 breaking changes/month during active development)
3. We have 2 backend engineers -- we can't maintain many parallel versions

## Options Considered

### Option A: URL path versioning (`/v1/`, `/v2/`)

| Pros | Cons |
|------|------|
| Simple to understand and implement | Forces consumers to update all endpoints at once |
| Easy to route at the load balancer | Version proliferation if we're not disciplined |
| Industry standard (Stripe, Twilio) | Can't deprecate individual endpoints independently |

### Option B: Header versioning (`Accept: application/vnd.api+json; version=2`)

| Pros | Cons |
|------|------|
| Cleaner URLs | Hidden -- developers forget to set headers |
| Can version individual endpoints | Harder to test (can't just change the URL in a browser) |
| More RESTful in theory | Less discoverable for new developers |

### Option C: Query parameter versioning (`?version=2`)

| Pros | Cons |
|------|------|
| Easy to test | Feels hacky, not a standard pattern |
| Visible in URLs | Caching complexity (version becomes part of cache key) |
| Can default to latest | Defaulting to latest is actually dangerous |

## Decision

**URL path versioning (`/v1/`).** Major versions in the path, non-breaking changes within a version, and a 12-month deprecation window for old versions.

Per Marcus: *"Header versioning is technically cleaner but every integration partner we talked to said they prefer path versioning because it's obvious. We should optimize for developer experience, not REST purity."*

## Rationale

- **Developer experience wins.** Our partners are mid-size companies with small eng teams. They need the simplest possible integration. Path versioning is what they expect.
- **Operational simplicity.** With 2 backend engineers, we need the strategy that's cheapest to maintain. Path versioning lets us route at the infrastructure level and run versions as separate deployments if needed.
- **Stripe's precedent.** Stripe uses path versioning with the addition of a date-based header for minor changes. We're not adopting the date-header part yet, but the path versioning foundation supports adding it later.
- **Discipline over flexibility.** Header versioning gives you the power to version every endpoint independently. With a small team, that power becomes a liability -- it's too easy to end up with a matrix of endpoint-version combinations nobody can reason about.

## Consequences

- All API routes will be prefixed with `/v1/` before the Q2 launch
- We'll document a versioning policy in the public API docs: breaking changes = new major version, 12-month support window for old versions
- Internal APIs remain unversioned (they change too fast, and we control both sides)
- When v2 is eventually needed, we'll spin up a separate deployment rather than maintaining two versions in one codebase
- Marcus will add API versioning to the eng onboarding guide
