---
status: draft
type: implementation-plan
---

# **Implementation Plan: [Title]**

**Owner:** [Your Name](mailto:your@email.com)
**Status:** `DRAFT`
**Last Updated:** [date]
**Source Spec:** [Spec Title](path or url)
**Resources:** [Brief](path), [RFC](path)

---

## **Intent**

Why we're doing this, what success feels like, what to protect. Written for an agent that has never seen the spec — if it reads nothing else, it reads this.

[1-2 paragraphs in the owner's voice. Name the outcome, not the mechanism.]

**Priority signals:** When in doubt, optimize for [X] over [Y]. Protect [Z] at all costs.

## **Scope**

One paragraph: what this plan delivers, framed as the bridge between the spec and working output.

**Not in scope:**

- [Thing the spec covers that this plan defers]
- [Thing explicitly excluded from this implementation pass]

## **Mental Model**

How the system works (or will work) after this plan ships. Walk through the happy path. Name the key states, transitions, or rules.

[1-3 paragraphs. Plain English, not spec-language. A reviewer reads this to verify the logic before looking at task blocks.]

## **Architecture Decisions**

Constraints that apply to all tasks. Agents read this before starting any work.

- **[Decision].** One sentence explaining the choice and why. *Rejected: [alternative] because [reason].*
- **[Decision].** One sentence. *Rejected: [alternative] because [reason].*
- **[Decision].** One sentence.

Keep this to 3-7 decisions. If there are more, the plan is too big — split it.

## **Safeguards**

Invariants that must hold regardless of how tasks are implemented. Not choices — constraints.

- [Invariant — e.g., "No duplicate records for the same entity within 7 days"]
- [Guard against regression — e.g., "Existing notifications must not change"]
- [Hard limit — e.g., "API response time stays under 500ms"]

## **Task Overview**

| Phase | Task | Deliverable | Size | Status | Dependencies |
|-------|------|-------------|------|--------|--------------|
| 1 | T-1.1: [Task name] | [What it produces] | S | — | — |
| 1 | T-1.2: [Task name] | [What it produces] | M | — | — |
| 2 | T-2.1: [Task name] | [What it produces] | M | — | T-1.1 |
| 2 | T-2.2: [Task name] | [What it produces] | L | — | T-1.2 |

**Size guide:** **S** = single file or function. **M** = multiple files, clear boundaries. **L** = cross-cutting, may need `/compact` midway.

**Status values:** — (not started) · `done` · `in progress` · `blocked` · `re-scoped`

## **Phase 1: [Descriptive Name]**

One sentence: what this phase achieves and why it comes first.

**Checkpoint:** [What must be true before Phase 2 starts — e.g., "All tests pass," "Core types compile," "Database migrations applied"]

### **T-1.1: [Task Name]**

- **Goal.** One sentence — what the agent produces when done.
- **Context.** What the agent needs to know. Specific file paths, key interfaces, patterns to follow, constraints from Architecture Decisions above. Include concrete code snippets (actual SQL, function signatures) when modifying existing code.
- **Deliverable.** Exact files created or modified.
- **Acceptance Criteria.**
  - [Testable condition]
  - [Testable condition]
  - [Testable condition]
- **Size:** S
- **Dependencies:** None

### **T-1.2: [Task Name]**

- **Goal.** [One sentence]
- **Context.** [File paths, interfaces, patterns. Include code snippets when relevant.]
- **Deliverable.** [Exact files]
- **Acceptance Criteria.**
  - [Testable condition]
  - [Testable condition]
- **Size:** M
- **Dependencies:** None

## **Phase 2: [Descriptive Name]**

One sentence: what this phase achieves. Depends on Phase 1 checkpoint.

**Checkpoint:** [What must be true before the next phase or wrap-up]

### **T-2.1: [Task Name]**

- **Goal.** [One sentence]
- **Context.** [File paths, interfaces, patterns. Reference Phase 1 outputs if relevant.]
- **Deliverable.** [Exact files]
- **Acceptance Criteria.**
  - [Testable condition]
  - [Testable condition]
- **Size:** M
- **Dependencies:** T-1.1

Add phases as needed. Most implementation plans have 2-4 phases.

## **Execution Notes**

- **Agent mode.** [Subagents / Agent team / Single session] — which execution mode fits this plan.
- **State management.** Git commit after each phase. Update BINDER.md if this is a binder project.
- **Shared context.** [What goes in the agent prompt vs. what agents discover from the codebase]
- **Known risks.** [Anything that might break assumptions — e.g., "If the API schema changes, T-2.1 and T-2.3 need re-scoping"]

## **Open Questions**

- [ ] [Question that needs resolution before execution]
- [ ] [Question that needs resolution before execution]

## **Log**

Append-only. Each session adds an entry. Update the Task Overview status column to match.

### [date]

- **Completed:** T-1.1, T-1.2
- **Attempted:** T-1.3 — blocked because [reason]
- **Re-scoped:** T-2.1 now includes [change] due to [discovery]
- **Failed approaches:** [What was tried and why it didn't work]
- **Next:** [What the next session should pick up]
