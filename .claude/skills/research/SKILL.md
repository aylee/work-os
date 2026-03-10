---
name: research
description: Conduct structured research and analysis. Searches local files, optionally Notion, uses web search, outputs structured findings.
disable-model-invocation: true
---

Conduct structured research and analysis on a topic.

## Usage

```
/research helpscout alternatives
/research vendor evaluation for support tooling
```

## Workflow

### Step 1: Load Calibration Material

Before writing, read:
- `library/reference/me.md` — voice and tone principles

**Draft mandate:** Focus on substance, coverage, and argument structure. The template
handles formatting. Get the thinking right — breadth and depth matter more than polish
in v1. Voice and formatting refinement happen in `/editor`.

### Step 2: Scope the Research

Ask clarifying questions:
- What's the specific question to answer?
- What's the context? (Why now? What decision does this inform?)
- Any constraints? (Budget, timeline, technical requirements)

### Step 3: Gather Context

- Read `areas/work/AREA.md` to understand which project this relates to (if it exists)
- If `.claude/notion.yaml` is configured: use `notion-search` to find what already exists on this topic in Notion, then `notion-fetch` on relevant results — don't duplicate research that's already done
- Search existing docs in `desk/` and `library/` for related analysis
- Use web search for external research (vendor info, market data, comparisons)

### Step 4: Create the Analysis

**Check for a matching binder first.** Search `desk/*/BINDER.md` for a binder matching the project. If your org uses a prefix convention (e.g., `acme-`), check both prefixed and unprefixed names. If a binder exists with `status: active` or `status: parked`, create the file inside that binder directory. Otherwise, create a new binder at `desk/` root.

- Read `library/templates/research.md` for the template structure (if it exists)
- Save to binder: `desk/{binder}/{project}-{descriptor}.md`
- Add YAML frontmatter: `status: draft` and `type: research`
- Structure findings clearly:
  - Current state (what we know today)
  - Findings (organized by theme, not chronologically)
  - Options table (with pros, cons, effort)
  - Clear recommendation

### Step 5: Writing Style

Follow the voice from `library/reference/me.md`:
- Lead with the bottom line — recommendation first, then supporting evidence
- Be honest about uncertainty — call out what you don't know
- Use tables for comparisons
- Link sources

## Tools Used

- Read, Write, Glob, Grep (file operations)
- Notion MCP: `notion-search`, `notion-fetch` (existing research — only if `.claude/notion.yaml` is configured)
- WebSearch (external research)
