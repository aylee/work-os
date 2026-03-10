# Doc-Level Examples

Curated sections from real docs showing structural patterns by doc type. Use alongside `voice-examples.md` (sentence-level) for full calibration.

> These examples use fictional content to illustrate the *structure* of each doc type. When you create your own docs, replace these with excerpts from your best work. `/editor` loads this file during editing passes.

---

## RFC Pattern

**Source:** RFC: Notification System Overhaul (fictional)

Shows: metadata block --> problem statement with competing patterns --> proposal with core principle

```markdown
# **RFC: Notification System Overhaul**

**Author:** [Your Name]
**Status:** `READY FOR REVIEW`
**Reviewers:**

* Eng: Jordan Blake
* Design: Sam Torres
* Ops: Riley Chen

## **Problem Statement**

Our notification system grew organically over 18 months. Every new feature
added its own notification channel without coordinating with what already
existed. Users now receive an average of 23 notifications/day across email,
push, and in-app -- and they've started turning everything off.

Today we have two patterns that don't work at scale:

**1. Feature-Owned Notifications**

* Each feature team defines its own notification logic
* No global frequency cap -- a user can get 8 emails in an hour
* Works fine for individual features, breaks down in aggregate

**2. User Preferences Page**

* 47 individual toggles across 6 categories
* Default state is "everything on"
* Only 3% of users have ever visited this page

**Tradeoffs:** We need notifications for engagement and retention, but the
current volume is driving opt-outs. The solution can't require every feature
team to rewrite their notification code.

## **Proposal: Centralized Delivery with Smart Batching**

**Core principle:** Features declare *intent* to notify. A central system
decides *when and how* to deliver.
```

**Why this works as a pattern:**
- Problem opens with a specific origin story ("grew organically over 18 months")
- Competing patterns numbered and contrasted with clear failure modes
- Each pattern gets bullets showing where it works and breaks
- Tradeoffs named explicitly before the proposal
- Proposal starts with a bold core principle, one sentence

---

## Project Brief Pattern

**Source:** Project Brief: Customer Data Pipeline Rebuild (fictional)

Shows: exec summary with Current/Future state --> numbered pain points --> "The Numbers" proof section

```markdown
## **Executive Summary**

We're rebuilding the customer data pipeline to eliminate the 6-hour lag
between user actions and dashboard updates. Real-time data unlocks three
features the sales team has been waiting for, and fixes the "dashboard
doesn't match reality" complaints that account managers deal with daily.

**Current state:** Customer activity data takes 6 hours to flow from our
app to the analytics dashboard. Account managers check the dashboard in
the morning and make decisions based on yesterday's data. Three times in
the past month, a sales rep quoted a customer's usage stats that were
wrong by the time the call happened.

**Future state:** Activity data lands in the dashboard within 60 seconds.
Account managers see real-time usage during customer calls. Automated
alerts fire when usage patterns change, instead of waiting for the next
morning's batch.

## **Problem Definition (What?)**

### **Pain Points**

The pipeline was built for weekly reports. We're now trying to use it for
daily decisions. Issues fall into **three buckets.**

**1. Stale Data --> Wrong Decisions**

* Account managers quote usage stats on calls that are 6+ hours old
* Three misquotes in the past month led to awkward customer conversations
* Sales team has stopped trusting the dashboard and asks data team for
  "fresh" numbers -- adding 2-3 ad-hoc requests/day
* **Result:** Data team spends 30% of their week answering "is this
  number right?" questions instead of building

**2. Batch Pipeline Fragility**

* Single-threaded nightly job processes 2.4M events
* If it fails (3x in the past quarter), the next morning's data is missing
* No retry logic -- failure requires manual intervention from on-call eng
* **Result:** On-call engineers dread the pipeline rotation

### **The Numbers**

* **Data lag:** 6 hours average, 14 hours worst case (after pipeline failure)
* **Ad-hoc data requests:** 12-15/week from sales (each takes ~30 min)
* **Pipeline failures:** 3 in the past quarter (Q4), each requiring 2-4
  hours of manual recovery
* **Eng time on pipeline support:** ~15 hours/week across the data team
```

**Why this works as a pattern:**
- Exec summary is one paragraph + Current/Future state labels -- genuinely brief
- Pain points numbered with bold descriptive names
- Each pain point has sub-bullets with specific evidence
- Bold **Result:** callouts summarize the impact
- "The Numbers" section grounds the problem in hours and headcount, not adjectives

---

## Decision Doc Pattern

**Source:** Decision: Choosing a Project Management Tool (fictional)

Shows: exec summary with Doc purpose / Recommendation --> options with Why/Tradeoffs --> priors table

```markdown
## **Exec Summary**

**Doc purpose:** We've outgrown spreadsheet-based project tracking.
Which tool should we adopt, and how do we migrate without losing velocity?

**Recommendation:** Adopt Linear for product and engineering. Keep
Notion for docs and knowledge management. Don't try to consolidate
into one tool.

## **Possible Solutions**

### **Option A: Linear (Recommended)**

**Why? It matches how we actually work.** Cycles map to our 2-week
sprints. Projects map to our quarterly rocks. The CLI and API mean
engineers can update tickets without leaving their terminal.

* Eng team trialed it for 2 weeks -- adoption was immediate
* Pricing: $8/user/month for our team size
* Migration: Linear has a Notion importer. ~2 hours of cleanup after.

**Tradeoffs.** Linear is opinionated. Customization is limited compared
to Jira or Asana. If your process doesn't fit Linear's model, you
change your process, not the tool. For us, that's a feature -- our
process needs simplifying anyway.

### **Option B: Jira**

**Why.** Industry standard. Every contractor and external partner
knows it. Deep customization.

**Tradeoffs.** Jira is where processes go to get complicated. Our
team of 12 doesn't need enterprise workflow automation. The median
Jira workspace has 200+ custom fields within a year. We don't have
an admin to maintain that.

### **Priors**

These are the assumptions behind Option A. If any are wrong, the
calculus changes.

| Assumption | What Changes If Wrong |
| --- | --- |
| Team stays under 30 people for 18+ months | If we 3x headcount, Jira's structure advantages may outweigh Linear's simplicity |
| Engineers will self-manage tickets | If adoption is low, the tool doesn't matter -- the problem is cultural |
| We won't need deep external partner collaboration | If partners need access, Linear's limited guest model becomes a constraint |
```

**Why this works as a pattern:**
- Recommended option uses "Why?" headers with bold thesis sentences
- Business impact as concrete evidence (trial results, pricing, migration estimate)
- Non-recommended options get compact Why/Tradeoffs blocks
- Priors table names assumptions and says what changes if they're wrong

---

## Research Doc Pattern

**Source:** Vendor Evaluation: Email Service Providers (fictional)

Shows: question --> current state --> findings with comparison table --> recommendation

```markdown
## Question

Which email service provider should we switch to? Our current provider
(MailGun) is hitting rate limits at our volume, and their deliverability
has dropped 8% over the past quarter.

## Current State

We send 340K transactional emails/month and 85K marketing emails/month.
MailGun has been reliable for two years but we're now hitting their
100K/hour rate limit during peak sends (Monday morning digests), causing
queuing delays of 15-45 minutes.

## Findings

| Provider | Deliverability | Rate Limits | Price (at our volume) | Migration Effort |
|----------|---------------|-------------|----------------------|-----------------|
| **SendGrid** | 97.2% (industry benchmark) | 10M/month included | $450/mo | Medium (2-3 days) |
| **Postmark** | 98.7% (best in class) | No hard limits | $625/mo | Low (1 day, similar API) |
| **Amazon SES** | 95.8% (varies) | Adjustable | $120/mo | High (1 week, different paradigm) |
| **MailGun (current)** | 91.3% (declining) | 100K/hour | $380/mo | None |

## Recommendation

**Postmark.** The 7% deliverability gap between Postmark and our
current provider translates to ~29,750 emails/month that reach inboxes
instead of spam folders. At our conversion rates, that's worth ~$14K/month
in recovered engagement. The $245/month premium over MailGun pays for
itself 57x over.
```

**Why this works as a pattern:**
- Question is specific and explains why we're asking now
- Current state includes the numbers that make the problem real
- Comparison table is scannable with the most important columns
- Recommendation leads with the choice, then shows the math

---

## Adding Your Own Examples

As you create docs using `/brief`, `/spec`, `/rfc`, and `/research`, pull your strongest sections here. For each example:

1. **Show the markdown** -- enough to see the structure and voice
2. **Annotate why it works** -- what structural or rhetorical pattern makes it effective?
3. **Name the pattern** -- "Pain points with bold Results," "Options table with Priors" -- so `/editor` can reference it

The best examples come from your own docs after they've been reviewed, revised, and validated by stakeholders. A pattern that worked once is interesting. A pattern that worked three times is a standard.
