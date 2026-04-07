# Writing & Formatting Guide

Reference for drafting and editing docs. Skills load this before writing.

---

## Headers

**All headers use bold text inside the markdown header.** This is non-negotiable.

```
# **Doc Title**
## **Section Name**
### **Subsection Name**
```

Not `## Section Name`. Always `## **Section Name**`.

**H1 titles include the doc type prefix:**
- `# **RFC: Human-AI Collaboration Patterns**`
- `# **Project Brief: Better Onboarding**`
- `# **Eval Framework: Pricing Agent**`
- `# **Launch Plan: Q3 Release**`

**Header naming is purpose-driven**, not generic. Use descriptive names that tell the reader what they'll get:
- `## **Problem Definition (What?)**` not `## Problem`
- `## **The Answer: Context, Not Weights**` not `## Solution`
- `## **Phase 1: Backtest Against Baseline ✅ COMPLETE**` not `## Phase 1`

**Numbered strategic sections use the number in the header:**
- `### **1. Fix the Foundation**`
- `### **2. Build the Bridges**`

---

## Metadata Block

Every doc opens with a bold-field metadata block. Not YAML frontmatter — that's for internal tracking only. The metadata block is for readers.

**Standard fields (most doc types):**
```
**Owner:** Maya Desai (mailto:maya@signalpath.example)
**Status:** `DRAFT`
**Reviewers:**

* Eng: Marcus Chen (mailto:marcus@signalpath.example)
* Design: Priya Sharma (mailto:priya@signalpath.example)
* Ops: Jordan Wells (mailto:jordan@signalpath.example)

**Last Updated:** April 6, 2026
**Resources:** [Mobile Activation Dashboard](https://analytics.signalpath.example/mobile-activation)
```

**Strategy variant** (heavier, more formal):
```
**Product Line Strategy**
**Core Product**
**Contributors:** Maya Desai (mailto:maya@signalpath.example), Dana Alvarez (mailto:dana@signalpath.example)
**Reference Documents:** [FY26 Product Plan](https://notion.so/signalpath/fy26-product-plan)
**Status:** Draft / **In Review** / Final
**Last Updated:** April 6, 2026
```

**Key conventions:**
- Status values in backticks: `DRAFT`, `IN REVIEW`, `LIVE`, `LIVING DOC`, `READY FOR REVIEW`, `EARLY DRAFT`, `ARCHIVED`
- Reviewers grouped by function: `* Eng:`, `* Design:`, `* Ops:`
- Resources section links related docs with full titles
- Use `---` horizontal rule after the metadata block

---

## Formatting Patterns

### Bold + period list leads

When a bullet starts with a bolded key term, end the bold with a period, then continue:

```
- **Better Inputs.** What the system knows when it starts reasoning
- **Better Tools.** What the system can do when it needs to act
- **Better Guardrails.** How we know the system is working
```

Not `- **Better Inputs**: What the system knows...` (no colon after bold). Not `- **Better Inputs** — What the system knows...` (no emdash).

### Bold + colon for inline labels

When labeling a concept inline, bold the label and use a colon:

```
**Current state:** Operators spend hours manually crafting recommendations...
**Future state:** AI generates complete packages...
**Core principle:** Keep one task system, but make it smarter about what it shows to whom.
**Why this matters:** If tasks are too cluttered, operators ignore the system...
```

### Numbered bold items in running text

For a few key items that aren't a deep list:

```
**1. Quality Crisis → Resource Strain**

* Operators without domain backgrounds...

**2. Audit Trail Gap**

* Critical decisions vanish into email...
```

### Comparison tables

For structured comparisons, especially Today vs Future:

```
| Traditional ML | LLM Agents |
| ----- | ----- |
| Feedback updates model weights | Feedback updates context/prompts |
| Model "remembers" patterns | The model has no memory |
```

Also used for Before/After, Option A/B, and Current/Proposed.

### Decision framing

State options, then declare the decision with rationale:

```
| Decision | Owner | Status | Notes |
| ----- | ----- | ----- | ----- |
| **1. Ownership:** Who is responsible? | Maya Desai | Completed | Decision: Product owns the rollout, Eng owns the guardrails. |
```

Or inline: **Decision:** Option B. It keeps rollout risk low and the
customer story simple.

Attribution: "Per Marcus Chen:" or "From April 2, 2026: Dana Alvarez
decided..."

### Strawman/WIP disclaimers

When content is provisional:

```
🚨 **DISCLAIMER:** The numbers/metrics below are a strawman intended to spark conversation. Don't get too hung up on individual numbers/targets.
```

```
🚧 **Early Thinking** 🚧
```

### Checkbox open questions

Always format open questions as checkboxes:

```
- [ ] Who owns QC for the first rollout?
- [ ] What's our rollback trigger?
```

Completed items use strikethrough: `- [x] ~~Decision documented~~`

### Status annotations in section headers

When a phase or section has a clear status:

```
## **Phase 1: Backtest Against Baseline ✅ COMPLETE**
## **Phase 2: Live with Customers (CURRENT STATE)**
```

### Functional requirement numbering

In PRDs, requirements get IDs:

```
**FR-1.1:** System shall auto-generate form link when visit is scheduled
**FR-1.2:** Form must be accessible on mobile without app installation
```

### JTBD format

Jobs to Be Done statements:

```
**When** a dispatcher is covering 3 last-minute callouts → **I want** to reassign work from my phone → **So that** the schedule stays accurate without opening my laptop
```

### ASCII/table UI mockups

For internal docs, use ASCII art or tables to sketch UIs — not Mermaid diagrams. Mermaid is reserved for state machines and workflow diagrams.

```
My Tasks (8)
━━━━━━━━━━━━━━━━━━━━━━━━━━
High Priority (3)
  📋 Review proposal - 123 Main St (Due today)
  📋 Follow up with client - 456 Oak Ave
```

### Arrows for flow

Use `→` (not `->` or `-->`) for inline flows:

```
new data → retrain model → better predictions
DRAFT → SUBMITTED_FOR_REVIEW → APPROVED → EXECUTED
```

### State/status values in inline code

Technical state names, system statuses, and constants use backtick formatting:

```
Once state = `APPROVED`, the customer can see the report.
The current label is `AI Draft Pending`.
```

---

## Section Patterns by Doc Type

### RFC
1. Metadata block
2. `## **Problem Statement**` or `## **The Problem: Reporting Lag Hurts Sales**`
3. `## **Proposal: Centralized Delivery**` or `## **The Answer: Preview Before Account Setup**`
4. `### **What Changes**` (specifics)
5. `### **Why This Approach**` (pros/cons, tradeoffs)
6. `## **Alternatives Considered**`
7. `## **Open Questions**` (checkboxes)

### PRD / Spec
1. Metadata block (with `**Doc Purpose**` section)
2. State diagram or workflow visualization
3. State/entity definitions (tables)
4. Business rules (numbered)
5. Events/transitions (tables)
6. Functional requirements (FR-numbered)
7. Open questions (checkboxes)

### Project Brief
1. Metadata block
2. `## **Executive Summary**` (genuinely 2-4 sentences — one paragraph with bold **Current state:** / **Future state:** inline labels)
3. `## **Problem Definition (What?)**` with `### **Pain Points**` (numbered bold items)
4. `## **Product Hypothesis (Why?)**`
5. `## **Solution / Approach (How?)**`
6. `## **Timeline & Rollout**`
7. `## **Open Questions**` (checkboxes)

### Eval Framework
1. Metadata block
2. `## **What the Assistant Does**` (numbered capabilities)
3. `## **Phase 1: Baseline Readout ✅ COMPLETE**` sections, each with:
   - `### **What We Validated**` / `### **What We're Measuring and Why**`
   - Metrics table (Metric | Target | Result)
   - `### **What Phase N Told Us**` / `### **What Phase N Did NOT Tell Us**`
4. `## **Open Questions**` (checkboxes)

### Launch Plan
1. Metadata block
2. `## **Launch Calendar**` (table: Phase | Dates | Key Activities | Status | DRIs)
3. `## **Week 1: Internal Rollout (Apr 14)**` sections with:
   - Decision tables
   - "Ready to ship when:" checkbox lists
4. `## **Rollback Plan**`

### Strategy Doc
1. Heavy metadata block (Product Line, Contributors, Reference Documents)
2. `# **Overview**`
3. `## **Vision**` (answers "What does the world look like when we're done?")
4. `## **Strategy**` with numbered strategic pillars (`### **1. Name**`)
5. `## **Roadmap**` (table: Initiative | Focus | Impact | Status)
6. `## **KPIs**` (table)
7. `## **Risks**`
8. `## **What We're NOT Doing**`

---

## Voice DNA

Starter defaults for clear, human writing. Customize these in `library/reference/me.md` as you develop your own voice. The formatting rules and banned phrases below are universal good defaults.

### Writing Rules

- **Sharp.** Open with the point, not the setup. If there's a conclusion, don't bury it.
- **Human.** Short sentences do the heavy lifting. Mix short declarative punches with longer explanatory sentences.
- **Specific.** Name things concretely. Real people, real systems, real numbers. Specificity makes docs actionable.
- **Physical verbs.** "Ship," "cut," "build," "break," "fix." Not "leverage," "utilize," "facilitate."
- **Parenthetical asides.** Use them for transparency: "(there's nuance)", "(mostly)", "(I might be wrong here)". The parenthetical acknowledges complexity; the sentence outside it stays clean.
- **Honest hedging.** When you're uncertain, say so plainly. "I'm not sure about this" beats "it may potentially be worth considering." Hedge with honesty, not with qualifiers.
- **Specificity over jokes.** A concrete detail ("32 open tickets, most probably resolved") beats a clever quip. The detail IS the persuasion.
- **No padding.** Every sentence earns its place. If removing a sentence doesn't change the meaning, remove it.

### Formatting Rules

- **Short paragraphs.** 1-3 sentences. A wall of text signals unclear thinking.
- **Digits for numbers.** "3 teams" not "three teams." "~30 per month" not "approximately thirty."
- **Contractions.** "Don't," "isn't," "we're." Unless the formality demands otherwise.
- **Bold sparingly.** Bold key terms and labels. If everything is bold, nothing is.
- **No em dashes.** One or two per doc is fine. A paragraph full of them is not. Rewrite instead.

### Banned Phrases

**Dead AI language** — phrases that signal the writer is an LLM on autopilot:
- "Let's unpack this"
- "It's important to note that"
- "It's worth noting"
- "In today's _anything_"
- "Let's dive in / dive deep"
- "At the end of the day"
- "Moving forward"
- "In order to"
- "When it comes to"
- "It goes without saying"
- "Needless to say"
- "As we all know"

**Dead transitions** — filler that adds no information:
- "With that said"
- "Having said that"
- "That being said"
- "On that note"
- "With that in mind"
- "In light of the above"

**Engagement bait** — performative enthusiasm:
- "Great question!"
- "Absolutely!"
- "Love this!"
- "Super exciting"

**AI cringe** — words that scream "generated":
- "Delve"
- "Utilize" (use "use")
- "Leverage" as a verb (use "use" or a physical verb)
- "Facilitate"
- "Streamline" (say what actually changes)
- "Spearhead"
- "Synergy" / "synergize"
- "Ecosystem" (unless literally about biology or platform APIs)
- "Holistic"
- "Robust" (say what makes it strong)
- "Comprehensive" (say what it covers)
- "Cutting-edge"

**Generic insider claims:**
- "As someone who has done X for Y years"
- "In my experience"
- "From what I've seen"

(Show the experience through specifics, don't claim it.)

**The "This isn't X. This is Y." pattern:**
- "This isn't just a dashboard. This is a command center."
- "This isn't about technology. This is about people."

(Rewrite to say what it IS without the dramatic negation.)

### Writing Samples

_Add 2-4 short excerpts from your own writing during setup if you want
tighter voice matching. Include a mix of doc types: a spec section, a
decision doc, a stakeholder email, and an RFC proposal. Real writing
beats instructions._

---

## Anti-Patterns

- **No restating exec summaries.** If the exec summary says it, the detail section shouldn't repeat it in different words.
- **No preamble.** Don't open with "In order to understand the context..." or "As our company grows..." Start with the point.
- **No "we believe" missionary language.** State hypotheses as product decisions, not beliefs.
- **No audience hedging.** Don't write "for non-technical stakeholders" — just write clearly.
- **No decorative formatting.** Every bold, table, and bullet earns its place.
- **No standalone Recommendations section.** Weave recommendations into the proposal/solution narrative.
- **No passive voice for decisions.** "We decided" or "Dana decided" —
  not "It was decided."
- **No Mermaid for UI concepts.** Mermaid is for state machines and workflows. ASCII and tables for UI.
- **No unbold headers.** Every `##` gets `**bold**` inside it.
- **No colon after bold list leads.** `- **Term.** Explanation` not `- **Term:** Explanation`
- **No corporate filler.** "We are proposing a strategic initiative to modernize..." — cut it.
- **No emdash overuse.** One or two per section is fine. A paragraph full of them is not.
- **No LLM-isms.** "Let's unpack this," "It's important to note that," "not X, it's Y" as a repeated construction.
- **No hedging clear recommendations.** "Might," "could potentially," "it may be worth considering" — if you have an opinion, say it.
- **No abstract descriptions without grounding.** "Improve the user experience" (how? for whom? what changes?)
- **No repetition across paragraphs.** Don't restate the same point in different words in consecutive paragraphs.
