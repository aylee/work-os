---
status: draft
type: brief
---

# **Project Brief: Mobile App Onboarding Redesign**

**Author:** [Your Name]
**Status:** `DRAFT`
**Reviewers:**

* Eng: Marcus Chen
* Design: Priya Sharma
* Growth: Raj Patel

**Resources:** [Current Onboarding Analytics (Amplitude)](https://analytics.example.com/onboarding), [Priya's Figma exploration](https://figma.com/file/example)

---

## **Executive Summary**

We're redesigning the mobile app's onboarding flow to fix a 62% drop-off rate that's killing activation. The current flow asks too much too soon -- four permission prompts, an account creation wall, and a feature tour that nobody finishes.

**Current state:** 62% of new users abandon onboarding before reaching the main screen. Of those who make it through, only 23% complete a core action in their first session. The permission prompt screen alone accounts for 34% of total abandonment. We're spending $18/install on paid acquisition and losing most of those users before they see the product.

**Future state:** Users reach the core experience within 60 seconds. Permissions are requested in context (when the user actually needs the feature), not upfront. Account creation is deferred until the user has experienced value. Target: 75%+ onboarding completion, 50%+ first-session activation.

## **Problem Definition (What?)**

### **Pain Points**

Our onboarding was designed two years ago for a different product. It hasn't kept up with three major feature launches, and it shows. Issues fall into **three buckets.**

**1. Permission Prompt Overload**

* Four system permissions requested on a single screen (notifications, location, camera, contacts)
* Users see this before they understand what the app does or why it needs access
* 34% of total drop-off happens at this screen alone
* Users who deny permissions can't easily re-enable them later, creating a degraded experience
* **Result:** We train users to distrust us before they've seen any value

**2. Account Creation Wall**

* Full registration (email, password, profile photo) required before seeing any content
* Social login options exist but are buried below the email form
* No guest/preview mode -- the app is a black box until you commit
* Competitors (Duolingo, Spotify) let you experience the product before asking for signup
* **Result:** High-intent users bounce because we're asking for commitment without demonstrating value

**3. Stale Feature Tour**

* 7-screen carousel explaining features that have since been redesigned or removed
* No skip option until screen 4
* Analytics show median time-on-tour is 8 seconds (users are swiping through without reading)
* Tour content references the old UI -- screenshots don't match what users actually see
* **Result:** The "education" step is actively confusing users instead of helping them

### **The Numbers**

* **Acquisition cost:** $18/install (paid channels), ~$3/install (organic)
* **Onboarding completion:** 38% (industry benchmark for our category: 65-70%)
* **First-session activation:** 23% of those who complete onboarding
* **Effective activation rate:** 8.7% of all installs (38% x 23%)
* **Monthly wasted spend:** ~$47K on paid installs that never activate
* **Permission grant rate:** 41% (down from 58% when we had fewer prompts)

## **Product Hypothesis (Why?)**

The onboarding flow treats every user like they need to be fully set up before they can do anything. That made sense when the app had one workflow. It doesn't work now that we have six features, each requiring different permissions.

The fix isn't a better tutorial -- it's removing the wall between install and value. If users can reach the core experience in under 60 seconds, they'll self-select into the features that matter to them, and we can request permissions in context when they actually make sense.

Progressive disclosure isn't a UX trick here. It's the product strategy: let the app sell itself.

## **Solution / Approach (How?)**

**Phase 1: Remove the wall (2 weeks)**

Defer account creation. Let users into a limited "guest" experience immediately after install. Show a single welcome screen (not a carousel) with one CTA: "Try it now." Move all permission prompts out of onboarding entirely.

**Phase 2: Contextual permissions (1 week)**

Request each permission the first time the user encounters a feature that needs it. Example: ask for camera access when the user taps the scan button, not during onboarding. Include a brief inline explanation of why we need it.

**Phase 3: Smart account creation (1 week)**

Prompt for account creation after the user completes their first core action (the "aha moment"). Pre-fill what we can from the guest session. Offer social login prominently. Make it feel like saving progress, not creating an account.

## **Timeline & Rollout**

| Phase | Scope | Timing | Notes |
| ----- | ----- | ----- | ----- |
| Phase 1 | Remove wall, guest mode | Weeks 1-2 | Eng-heavy, needs API changes for anonymous sessions |
| Phase 2 | Contextual permissions | Week 3 | Mostly client-side, design-heavy |
| Phase 3 | Smart account creation | Week 4 | Depends on Phase 1 anonymous session work |
| Monitoring | 2-week burn-in | Weeks 5-6 | Watch activation metrics, permission grant rates |

## **Non-Goals**

* We're not redesigning the core app experience -- just the path to get there
* We're not changing the pricing/paywall flow (that's a separate project)
* We're not building a full A/B testing framework -- we'll use a simple feature flag for rollout
* We're not localizing the new flow yet (English first, localization fast-follow)

## **Open Questions**

- [ ] Can Marcus confirm the deep-link attribution SDK works with anonymous sessions? If not, Phase 1 scope changes significantly.
- [ ] Do we A/B test or full-ship? Raj wants a holdback group. Marcus says the eng cost of maintaining two flows isn't worth it given how bad the current one is. Need Dana to break the tie.
- [ ] What's the "aha moment" we're optimizing for in Phase 3? We have three candidates (first search, first save, first share) and no clear data on which predicts retention.
- [ ] Legal review needed on guest data retention -- how long can we keep anonymous session data before GDPR requires deletion?
