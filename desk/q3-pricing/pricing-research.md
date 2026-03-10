---
status: draft
type: research
---

# Pricing Model Options: Research & Analysis

**Date:** 2026-03-08
**Status:** In Progress

---

## Question

Should we move from pure usage-based pricing to a hybrid model for Q3? Our top accounts are undercharged relative to value delivered, and our smaller accounts are churning because usage-based feels unpredictable.

## Current State

We charge $0.12 per API call with a $500/month minimum. This was set 18 months ago when our average customer made ~8,000 calls/month. Today:

- **Average calls/month:** 34,000 (4x growth)
- **Top 10 accounts:** 180,000+ calls/month, paying ~$21,600/month
- **Bottom quartile:** 2,000-5,000 calls/month, paying $500-600/month
- **Churn concentration:** 78% of churn comes from accounts in months 2-4, before they've scaled usage enough for the product to feel "worth it"
- **Expansion revenue:** Strong (140% NDR) but entirely driven by organic usage growth, not deliberate upsell

The pricing model is accidentally punishing small accounts (high per-unit cost relative to value) and undercharging large ones (marginal cost drops with scale, but price doesn't).

## Findings

### Competitor Pricing Models

| Company | Model | Base Price | Usage Component | Notes |
|---------|-------|-----------|----------------|-------|
| **Rival A** | Tiered seats + usage | $49/seat/mo | $0.05/call over 10K | Introduced tiers in 2025, reported 15% churn reduction |
| **Rival B** | Flat platform fee | $2,500/mo flat | None | Enterprise-only, no self-serve |
| **Rival C** | Usage-based (like us) | $0.15/call | $0.10/call over 50K | Recently added "committed use" discounts |
| **Adjacent D** | Hybrid | $199/mo base | $0.03/call over 5K | Base includes support + 5K calls. Fastest-growing in category |
| **Adjacent E** | Seat-based | $79/seat/mo | None | Simple but creates "seat management" friction in enterprise |

### Key Insight: The "Adjacent D" Pattern

Adjacent D's hybrid model is the most interesting signal. Their base fee covers enough usage for small accounts to see value (5K calls), while the usage component captures growth from power users. Their Q4 earnings cited this model change as the primary driver of 23% YoY revenue growth.

The base fee also solves our churn problem -- small accounts pay a predictable amount and get enough capacity to reach the "aha moment" before usage pricing kicks in.

### Internal Data

**Revenue concentration:**
- Top 10 accounts: 64% of consumption, 38% of revenue
- Top 10 accounts: average margin of 72% (high value, low marginal cost)
- Bottom quartile: average margin of 31% (support costs eat into thin revenue)

**Churn analysis (Taylor's data):**
- Accounts that reach 15K+ calls/month in the first 60 days have 94% 12-month retention
- Accounts below 5K calls/month at day 60 have 43% 12-month retention
- The "5K threshold" aligns with completing at least one full workflow integration

## Options

| Option | Pros | Cons | Effort | Revenue Impact (est.) |
|--------|------|------|--------|-----------------------|
| **A: Hybrid (base + usage)** — $299/mo base (includes 10K calls) + $0.08/call over | Predictable for SMB, captures enterprise value, matches market trend | Requires migrating existing contracts, sales needs retraining | Medium | +18-22% ARR |
| **B: Tiered plans** — Good/Better/Best at $199/$499/$1,499/mo with usage caps | Simple to understand, clear upgrade path | Caps create friction, enterprise hates artificial limits | Medium | +12-15% ARR |
| **C: Committed use discounts** — Keep usage-based, add 12-month commit for 20% discount | Low migration risk, rewards loyalty | Doesn't fix SMB churn, doesn't capture enterprise upside | Low | +5-8% ARR |
| **D: Status quo** — No changes | Zero effort, no migration risk | Churn continues, enterprise undercharged | None | Baseline (declining) |

## Recommendation

**Option A: Hybrid model.** The base fee solves SMB churn by making the first months predictable and valuable. The usage component above 10K preserves expansion revenue from enterprise accounts. This matches the market direction (Adjacent D's results are strong evidence) and aligns with what Taylor's data shows about the 5K-call activation threshold.

One risk to model: Nadia's team has been selling "unlimited usage" positioning. A per-call component above 10K needs careful framing -- "you've been paying per-call all along, now your first 10K are included" is better than "we're adding a new fee."

The committed-use discount (Option C) could layer on top of Option A as a retention tool for mid-market accounts, but it's not sufficient on its own.

## Sources

- Internal usage data (Taylor Kim, Revenue Ops export, March 2026)
- Rival A pricing page + Q4 2025 earnings transcript
- Adjacent D Q4 2025 earnings call (hybrid model results)
- Rival C blog post: "Why We're Adding Committed Use Discounts" (Feb 2026)
- Jordan Wells margin analysis (internal, March 2026)
