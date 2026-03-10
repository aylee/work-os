---
name: brief
description: Write a project brief or 1-pager. Uses templates, loads voice calibration, pulls context from local files and optionally Notion.
disable-model-invocation: true
---

Write a project brief or 1-pager for stakeholder communication.

## Usage

```
/brief integration response plan
/brief <existing-file-path>
```

## Workflow

### Step 1: Load Calibration Material

Before writing, read these files:
- `library/reference/me.md` — voice and tone principles

**Draft mandate:** Focus on substance, coverage, and argument structure. The template
handles formatting. Get the thinking right — breadth and depth matter more than polish
in v1. Voice and formatting refinement happen in `/editor`.

### Step 2: Understand the Topic

If a file path is given, read the existing brief and ask what to change.

If a topic is given:
- Read `areas/work/AREA.md` for relevant context (if it exists)
- If `.claude/notion.yaml` is configured: use `notion-search` to find existing Notion pages about this topic, then `notion-fetch` on relevant results to gather background
- Search `desk/` and `library/` for related docs

### Step 3: Determine Location

**Check for a matching binder first.** Search `desk/*/BINDER.md` for a binder matching the project. If your org uses a prefix convention (e.g., `acme-`), check both prefixed and unprefixed names. If a binder exists with `status: active` or `status: parked`, create the file inside that binder directory.

If no binder matches, create a new binder directory at `desk/` root:
- Use your org prefix if applicable: `desk/{prefix}{project}/`
- Otherwise: `desk/{project}/`

File naming: `{project}-{descriptor}.md` (e.g. `integration-response-brief.md`)

### Step 4: Create or Update

**If new brief:**
- Read `library/templates/brief.md` for the template structure (if it exists)
- Create a new file with the naming convention above
- Add YAML frontmatter: `status: draft` and `type: brief`
- Follow the template: Executive Summary (with Current state/Future state) -> Problem Definition (numbered pain points) -> The Numbers -> Product Hypothesis -> Solution/Approach -> Timeline -> Non-Goals -> Open Questions
- Pre-fill sections with context gathered from existing files

**If existing brief:**
- Read the current file
- Apply the requested changes
- Preserve the overall structure and voice

### Step 5: Writing Style

Follow the voice principles from `library/reference/me.md`:
- Lead with the point, not the setup
- Name things concretely — real numbers, real people, real costs
- Recommend, don't hedge
- Say what you're NOT doing

### Step 6: Review

After writing, summarize:
- What was created or changed
- Open questions that need answers
- Suggested next steps:
  - If the brief is solid and requirements need detailing -> suggest `/spec`
  - If the brief needs stakeholder input -> name who and what question
  - If this is a small effort that doesn't need a spec -> suggest executing the implementation directly

## Tools Used

- Read, Write, Glob, Grep (file operations)
- Notion MCP: `notion-search`, `notion-fetch` (context gathering — only if `.claude/notion.yaml` is configured)
