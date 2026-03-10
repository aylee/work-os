---
name: decision
description: Record a decision with full context, options considered, and rationale.
disable-model-invocation: true
---

Record a decision with full context and rationale.

## Usage

```
/decision which support tool to use
/decision api versioning strategy for external api
```

## Workflow

### Step 1: Load Calibration Material

Before writing, read:
- `library/reference/me.md` — voice principles

**Draft mandate:** Focus on substance, coverage, and argument structure. The template
handles formatting. Get the thinking right — breadth and depth matter more than polish
in v1. Voice and formatting refinement happen in `/editor`.

### Step 2: Gather Context

- Ask about the decision: What was decided? Who was involved? What were the alternatives?
- Search existing docs in `desk/` and `memory/decisions/` for related decisions or research
- If `.claude/notion.yaml` is configured: use `notion-search` if relevant context lives in Notion

### Step 3: Create the Decision Record

- Read `library/templates/decision.md` for the template structure (if it exists)
- Save to `memory/decisions/` with format: `YYYY-MM-DD-brief-description.md`
- **If the decision relates to an active binder project**, also note the decision in that binder's Last Session block when updating it at session end
- Fill in all sections:
  - Context: What led to this decision
  - Options: As a table (Option | Pro | Con)
  - Decision: Bold decision line with rationale. `**Decision:** [Choice]. [Rationale.]`
  - Attribution: `Per [Name]: *"[Quote]"*` if a stakeholder drove the decision
  - Consequences: What changes as a result

### Step 4: Writing Style

- Options in a comparison table, not separate subsections
- Decision framed as: Option A / Option B -> **Decision:** [choice]. [rationale.]
- Be concise but complete — someone reading this in 6 months should understand why

## Tools Used

- Read, Write, Glob (file operations)
- Notion MCP: `notion-search`, `notion-fetch` (context gathering — only if `.claude/notion.yaml` is configured)
