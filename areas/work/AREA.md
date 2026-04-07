---
status: active
type: area
---

# Work

Company context for the shipped demo workspace. This example centers on
one fictional company so the desk reads like an intentional operating
system, not unfinished setup.

## Company

**SignalPath** is a fictional workflow platform for distributed field
teams. Managers run scheduling, reporting, and pricing from the web
app; technicians use the mobile app in the field; larger customers
connect the product to their stack through a partner API.

### Role

| Field | Value |
|-------|-------|
| **Title** | Group Product Manager, Activation & Monetization |
| **Team** | Core Product |
| **Reports to** | Dana Alvarez, VP Product |
| **Scope** | New-user activation across web and mobile, self-serve monetization, and packaging for growth accounts |

### Team Structure

| Person | Role | Works on |
|--------|------|----------|
| Marcus Chen | Eng Lead | Mobile onboarding, identity, and partner API foundations |
| Priya Sharma | Staff Product Designer | Activation flows, design system, and lifecycle UX |
| Taylor Kim | Revenue Ops Lead | Pricing analysis, packaging experiments, and forecast models |
| Jordan Wells | Finance Partner | Margin modeling, launch approvals, and board-ready narratives |

### Strategy

SignalPath wins when a new team can go from invite to first completed
job in a day, then grow into deeper integrations as their operation gets
more complex. This quarter the product org is tightening activation,
simplifying packaging, and laying down partner API foundations that make
larger accounts easier to land without bloating the core workflow.

## Big Rocks

### 1. Raise first-week activation
Make the first session feel useful fast enough that new teams complete
setup and log real work in the same week.
**DRI**: Maya Desai | **KPI**: first-week activated workspaces | **Success**: 24% -> 40%

- [ ] Ship the mobile onboarding redesign
- [ ] Retire the stale tour across web and mobile
- [ ] Align activation instrumentation with growth reporting

### 2. Rework pricing for healthier expansion
Land a pricing model that is easier for smaller teams to understand and
captures more value from large, integration-heavy accounts.
**DRI**: Maya Desai | **KPI**: projected ARR lift with flat SMB churn | **Success**: pricing package approved for Q3 rollout

- [ ] Finish churn and margin modeling
- [ ] Pressure-test the hybrid package with sales and finance
- [ ] Draft the rollout memo for the pricing council

### 3. Launch the partner API foundation
Turn the API from a bespoke enterprise promise into a productized
surface with clear versioning and support expectations.
**DRI**: Marcus Chen | **KPI**: beta integrations live | **Success**: 2 pilot customers on v1 policy by end of quarter

- [ ] Publish the versioning policy
- [ ] Finalize auth and rate-limit guidance
- [ ] Select the first beta partners

### 4. Tighten operating visibility
Give product, finance, and growth the same read on what is working so
decisions move faster.
**DRI**: Taylor Kim | **KPI**: time to answer routine product questions | **Success**: weekly KPI readout lands every Monday

- [ ] Standardize the activation dashboard
- [ ] Replace ad hoc pricing pulls with one shared model
- [ ] Document the attribution assumptions

## What's On the Desk

*Last refreshed: Apr 6, 2026*

This is the current snapshot of active work grouped by Big Rock.

### Big Rock 1: Raise first-week activation

**Now:** `desk/mobile-app-redesign/` is driving the mobile half of the
activation push, with guest access and in-context permissions as the
primary bets.
**Next:** Bring the archived `onboarding-v2` learnings back into the
manager-web follow-up once mobile scope is locked.

| Project | Status | Docs |
|---------|--------|------|
| Mobile App Redesign | In Progress | `desk/mobile-app-redesign/` |

### Big Rock 2: Rework pricing for healthier expansion

**Now:** `desk/q3-pricing/` is converging on a hybrid package
recommendation for the April pricing council.
**Next:** Translate the recommendation into customer-facing talk tracks
and migration rules.

| Project | Status | Docs |
|---------|--------|------|
| Q3 Pricing Strategy Review | In Progress | `desk/q3-pricing/` |

### Big Rock 3: Launch the partner API foundation

**Now:** The versioning decision is documented in
`memory/decisions/2026-01-15-example-decision.md`.
**Next:** Draft auth docs and pick the first pilot accounts.

## This Week

See [plans.md](plans.md) for weekly focus.

## Systems

- **Notion area:** `https://notion.so/signalpath/product`
- **Databases:** Goals, Projects, Pricing Council, Customer Research
- **Code:** `~/code/signalpath-app`, `~/code/signalpath-api`
- **Project management:** Linear
