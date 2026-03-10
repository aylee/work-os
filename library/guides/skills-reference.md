# Skills Reference

All 14 skills organized by category. Each skill is a slash command you run in Claude Code.

---

## Orientation

Skills for understanding where you are and what to work on.

### `/desk`

**Orient -- what's on my plate?**

Shows your weekly focus, active binders, backburner highlights, and suggested focus for today. If no weekly plan exists, triggers a curation flow that drafts one from your active projects and Big Rocks.

**Usage:**
```
/desk
```

**When to use it:** Start of the day, start of the week, or whenever you need to re-orient. This is the command you'll use most.

**What it produces:** A synthesis of This Week priorities, desk state (all active binders with status), timely backburner items, and 2-3 suggested focus areas for today. If the weekly plan is stale, it writes a new one to `areas/work/plans.md`.

---

### `/morning`

**Daily briefing -- here's where you are and what matters today.**

A lighter version of `/desk`. Reads weekly plan, active binders, and Big Rocks to produce a "here's where you are" briefing. No curation flow, no file writes -- just synthesis.

**Usage:**
```
/morning
```

**When to use it:** Quick daily check-in. Use `/desk` for the full curation experience, `/morning` for a fast read-only briefing.

**What it produces:** This Week summary, 2-3 suggested actions for today, and attention flags (stale projects, misaligned goals). Omits sections that don't apply.

---

### `/open {project}`

**Open a project binder -- load context and resume where you left off.**

Loads a project's full context: BINDER.md manifest, area context, list of files, and the Last Session block showing where you left off. When you're done working, it offers to update the Last Session and capture any corrections.

**Usage:**
```
/open mobile-app-redesign
/open pricing
/open onboarding
```

The argument is a project name. Partial matches work. Case-insensitive.

**When to use it:** Beginning of any project work session. This is how you "open a project" -- it loads the context Claude needs to be useful.

**What it produces:** A resume summary with project status, where you left off, open items, and available files. At session end, updates BINDER.md with what happened.

---

## Writing

Skills for creating and refining documents. The writing workflow is: `/shape` (understand) --> draft skill (write) --> iterate (conversation) --> `/editor` (polish).

### `/shape {topic}`

**Understand a request before acting on it.**

Interrogates the problem, intent, context, and expected output before you start building. Produces a brief-back for you to confirm. Catches misalignment before it compounds.

**Usage:**
```
/shape should we add real-time notifications?
/shape redesign the settings page
/shape api rate limiting strategy
```

**When to use it:** Before any complex task. When someone says "figure out the thing" and you need to understand what "the thing" actually is. Before entering plan mode.

**What it produces:** A structured brief-back with Problem, Intent, Context, Expected Output, Scope, and Open Questions. Not saved to a file by default -- it's a conversation artifact.

---

### `/brief {topic}`

**Write a project brief or 1-pager.**

Creates a structured project brief using the template. Pulls context from your work area and Notion (if configured). Follows the pattern: Executive Summary --> Problem Definition --> The Numbers --> Product Hypothesis --> Solution --> Timeline --> Non-Goals --> Open Questions.

**Usage:**
```
/brief mobile onboarding redesign
/brief desk/mobile-app-redesign/mobile-redesign-brief.md   # edit existing
```

**When to use it:** When you need to communicate a project's "what and why" to stakeholders. The starting point for most projects.

**What it produces:** A markdown file in the appropriate binder with frontmatter (`status: draft`, `type: brief`). Suggests next steps: `/spec` if requirements need detailing, or execute the implementation directly if it's small enough.

---

### `/spec {topic}`

**Write or iterate on a product spec / PRD.**

Creates a structured spec with requirements, JTBD, functional requirements (numbered), success criteria, and non-goals. Pulls context from existing docs and Notion.

**Usage:**
```
/spec notification system requirements
/spec desk/mobile-app-redesign/onboarding-spec.md   # edit existing
```

**When to use it:** After the brief is solid and you need to detail the requirements. When eng needs to know exactly what to build.

**What it produces:** A markdown spec file with bucketed requirements, JTBD bullets, numbered FRs (FR-1.1, FR-1.2, etc.), success criteria, and open questions.

---

### `/rfc {topic}`

**Write or iterate on an RFC (Request for Comments).**

Creates a proposal for debate. Follows the pattern: Problem Statement --> Proposal --> Why This Approach --> Alternatives Considered --> Open Questions. Shows competing forces before proposing a resolution.

**Usage:**
```
/rfc human-ai collaboration patterns
/rfc caching strategy for the api layer
```

**When to use it:** When you need to propose an approach and invite debate. When there are real tradeoffs and you want to show you've considered alternatives.

**What it produces:** A markdown RFC file with frontmatter (`status: draft`, `type: rfc`). Includes the problem, competing approaches, and a clear recommendation.

---

### `/research {topic}`

**Conduct structured research and analysis.**

Gathers information from Notion, existing docs, and web search. Produces structured findings with a comparison table and recommendation. Asks clarifying questions about the specific question, context, and constraints.

**Usage:**
```
/research email provider alternatives
/research vendor evaluation for auth service
```

**When to use it:** When you need to evaluate options, compare vendors, or analyze a domain before making a decision. When you'd normally open 15 browser tabs.

**What it produces:** A markdown research file with Question, Current State, Findings (organized by theme), Options table (pros/cons/effort), and a Recommendation.

---

### `/decision {topic}`

**Record a decision with full context, options considered, and rationale.**

Creates a decision record that captures the context, alternatives, the decision itself, and consequences. Saved to `memory/decisions/` with a date prefix for chronological sorting.

**Usage:**
```
/decision which project management tool to adopt
/decision api versioning strategy
```

**When to use it:** When a meaningful choice has been made and you want future-you (or teammates) to understand why. Especially valuable for decisions that feel obvious now but won't in 6 months.

**What it produces:** A markdown file in `memory/decisions/YYYY-MM-DD-brief-description.md` with Context, Options table, Decision with attribution, and Consequences.

---

### `/editor {file-path}`

**Make an editing pass on a document.**

Loads all four reference files (me.md, writing-guide.md, voice-examples.md, doc-examples.md) and makes a tightening pass. Fixes formatting compliance first, then edits for voice -- cutting filler, shortening sentences, replacing vague language with specifics.

**Usage:**
```
/editor desk/q3-pricing/pricing-research.md
/editor desk/q3-pricing/pricing-research.md -- focus on the recommendation
/editor desk/q3-pricing/pricing-research.md -- tighten for external audience
```

**When to use it:** After writing a draft and iterating on the substance. This is the "polish" step -- it changes the words, not the ideas. Run it when you're happy with the content and want to tighten the presentation.

**What it produces:** Edits the file in place. Provides a summary of changes, formatting fixes, flagged-but-not-changed items, and suggested next pass.

---

## System

Skills for reflection, maintenance, and system health.

### `/review`

**Weekly review -- close the loop, archive the week, set direction for next.**

Weekly review that compares planned vs. actual, synthesizes corrections, reviews the backburner and commitments, and writes a review to `memory/reviews/`. Updates `areas/work/plans.md` with next week's priorities.

**Usage:**
```
/review
```

**When to use it:** End of the week (Friday or Sunday). This is how the system learns. The first few runs will be light -- the value compounds over months.

**What it produces:** A review file in `memory/reviews/YYYY-WNN.md` with Planned vs. Actual, Desk activity, Corrections analysis, Patterns, and Next Week priorities. Also updates `areas/work/plans.md`.

---

### `/recent`

**Show recently edited work files, pulled from git history.**

Displays files modified in the last N days, grouped by binder, with frontmatter metadata. Like a "recent docs" view for your repo.

**Usage:**
```
/recent           # last 7 days (default)
/recent 3d        # last 3 days
/recent 2w        # last 2 weeks
```

**When to use it:** When you need to find something you worked on recently. When you want to see what's been active across binders.

**What it produces:** A grouped display of recently modified files with type, status, and relative dates. Requires git (uses `git log` for file activity).

---

### `/sessions`

**List, search, and export Claude Code sessions across all repos.**

Manages session history. Sessions are stored as `.jsonl` files by Claude Code. This skill lists, searches, and exports them as readable markdown transcripts.

**Usage:**
```
/sessions list          # List 10 most recent sessions
/sessions list 20       # List 20 most recent
/sessions search pricing  # Search exported sessions for "pricing"
/sessions export        # Export all unexported sessions
```

**When to use it:** When you need to find a past conversation. When you want to search "what did I discuss about X?" When you want to export sessions for the memory system.

**What it produces:** For `list`: a table of recent sessions with repo, date, topic, and export status. For `search`: matching excerpts from exported transcripts. For `export`: markdown files in `memory/sessions/`.

---

## Setup

### `/setup`

**Onboarding wizard -- personalize your work-os.**

Multi-step conversation that configures identity, writing voice, life areas, active projects, and integrations. Run once to bootstrap, or re-run anytime to update a specific section.

**Usage:**
```
/setup
```

**When to use it:** Right after cloning the repo. Or anytime you want to update your identity, voice calibration, areas, or integrations.

**What it produces:** Updates to `library/reference/me.md`, `CLAUDE.md`, `areas/work/AREA.md`, project binders, and integration config files. Offers to commit the result.
