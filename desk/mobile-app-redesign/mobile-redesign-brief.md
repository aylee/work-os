---
status: draft
type: brief
---

# **Project Brief: Mobile App Onboarding Redesign**

**Author:** Maya Desai
**Status:** `DRAFT`
**Reviewers:**

* Eng: Marcus Chen
* Design: Priya Sharma
* Growth: Raj Patel

**Resources:** [Mobile Activation Dashboard](https://analytics.signalpath.example/mobile-activation), [Priya's onboarding prototype](https://www.figma.com/file/signalpath/mobile-onboarding-v4)

---

## **Executive Summary**

We're redesigning SignalPath's mobile onboarding flow to fix a 62%
drop-off rate that suppresses first-week activation for new field teams.
The current experience asks for four permissions, a workspace account,
and a stale tour before a user sees a real schedule or sample workflow.

**Current state:** 62% of new users abandon onboarding before they reach
a usable workspace. Of those who make it through, only 23% log a first
job or field update in their first session. The permission wall alone
accounts for 34% of total abandonment. We're spending ~$18/install on
paid acquisition and losing most of those users before they see the
product.

**Future state:** Users land in a sample workspace or invited-team
context within 60 seconds. Permissions are requested in context, not
upfront. Account creation shifts to the moment a user saves progress or
joins a team. Target: 75%+ onboarding completion, 50%+ first-session
activation.

## **Problem Definition (What?)**

### **Pain Points**

Our onboarding was designed when SignalPath was mostly a manager web
product. It hasn't kept up with the mobile app becoming a first-touch
surface, and it shows. Issues fall into **three buckets.**

**1. Permission Prompt Overload**

* Four system permissions requested on a single screen (notifications,
  location, camera, contacts)
* Users see this before they understand how the app fits into their day
* 34% of total drop-off happens at this screen alone
* Users who deny permissions end up in a degraded flow with no clear
  recovery path
* **Result:** We train users to distrust the product before they've seen
  any value

**2. Account Creation Wall**

* Full account and workspace setup required before seeing any schedule,
  job list, or sample content
* Apple and Google sign-in exist but are buried below the email form
* No guest or preview mode -- the app is a black box until you commit
* Competitive field tools let teams explore a sample day before asking
  for full setup
* **Result:** High-intent users bounce because we're asking for admin
  work without demonstrating value

**3. Stale Feature Tour**

* 7-screen carousel explaining features that have since been redesigned
  or removed
* No skip option until screen 4
* Analytics show median time-on-tour is 8 seconds (users are swiping
  through without reading)
* Tour content references the old dispatcher UI, so screenshots do not
  match what users actually see
* **Result:** The "education" step is actively confusing users instead
  of helping them

### **The Numbers**

* **Acquisition cost:** ~$18/install (paid channels), ~$4/install (partner referrals)
* **Onboarding completion:** 38% (industry benchmark for our category: 65-70%)
* **First-session activation:** 23% of users who complete onboarding
* **Effective activation rate:** 8.7% of all installs (38% x 23%)
* **Monthly wasted spend:** ~$47K on paid installs that never activate
* **Permission grant rate:** 41% (down from 58% when we had fewer prompts)

## **Product Hypothesis (Why?)**

The onboarding flow treats every user like they need to fully configure
their workspace before they can do anything. That made sense when
SignalPath was manager-led and mostly web based. It breaks now that many
new users start on mobile and only need one schedule, one photo upload,
or one teammate handoff to understand the value.

The fix isn't a better tutorial -- it's removing the wall between
install and value. If users can preview a realistic workspace and
complete one lightweight action in under 60 seconds, they'll grant
permissions in context and create accounts when saving work feels
natural.

Progressive disclosure isn't a UX trick here. It's how we make a
multi-surface product feel legible on day 0.

## **Solution / Approach (How?)**

**Phase 1: Remove the wall (2 weeks)**

Defer account creation. Let users into a sample workspace or invited
team preview immediately after install. Replace the carousel with a
single welcome screen and one CTA: "See a sample day." Move contacts and
camera permissions out of onboarding entirely.

**Phase 2: Contextual permissions (1 week)**

Request each permission the first time the user encounters a feature
that needs it. Ask for location when the user checks into a job, camera
when they attach a photo, and notifications when they opt into shift
reminders. Include brief inline explanation copy and a retry path.

**Phase 3: Smart account creation (1 week)**

Prompt for account creation after the user completes their first core
action or accepts a team invite. Pre-fill what we can from the guest
session. Offer Apple and Google sign-in prominently. Make it feel like
saving progress, not opening an account.

## **Timeline & Rollout**

| Phase | Scope | Timing | Notes |
| ----- | ----- | ----- | ----- |
| Phase 1 | Sample workspace + guest session | Weeks 1-2 | Eng-heavy, needs anonymous session handoff |
| Phase 2 | Contextual permissions | Week 3 | Mostly client-side, plus copy and support review |
| Phase 3 | Smart account creation | Week 4 | Depends on Phase 1 session upgrade work |
| Monitoring | 2-week burn-in | Weeks 5-6 | Watch activation, invite acceptance, and permission grant rates |

## **Non-Goals**

* We're not redesigning the core app experience -- just the path to get there
* We're not changing the pricing/paywall flow (that's a separate project)
* We're not building a full experimentation platform -- we'll use our
  existing holdback pattern and feature flags
* We're not localizing the new flow yet (English first, localization fast-follow)

## **Open Questions**

- [ ] Can Marcus confirm invite attribution and anonymous session upgrade
  work with guest sessions? If not, Phase 1 scope changes significantly.
- [ ] Do we run a 10% holdback for paid cohorts or full-ship once the
  metrics look stable? Raj wants the holdback; Dana wants minimal
  operational drag.
- [ ] What is the best "aha moment" for the account-creation prompt:
  first job check-in, first photo update, or first shared handoff note?
- [ ] Legal review needed on guest data retention -- how long can we
  keep anonymous session data before requiring deletion?
