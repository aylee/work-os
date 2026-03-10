---
name: spec
description: Write or iterate on a product spec / PRD. Uses templates, loads voice calibration, pulls context from local files and optionally Notion.
disable-model-invocation: true
---

Write or iterate on a product spec or PRD.

## Usage

```
/spec payments redesign
/spec <existing-file-path>
```

## Workflow

### Step 1: Load Calibration Material

Before writing, read these files:
- `library/reference/me.md` — voice and tone principles

**Draft mandate:** Focus on substance, coverage, and argument structure. The template
handles formatting. Get the thinking right — breadth and depth matter more than polish
in v1. Voice and formatting refinement happen in `/editor`.

### Step 2: Understand the Topic

If a file path is given, read the existing spec and ask what to change.

If a topic is given:
- Read `areas/work/AREA.md` to identify which project this relates to and for company/product context (if it exists)
- If `.claude/notion.yaml` is configured: use `notion-search` to find existing Notion pages about this topic (prior research, meeting notes, related specs), then `notion-fetch` on the most relevant results to gather background
- Search `desk/` and `memory/decisions/` for related docs

### Step 3: Determine Location

**Check for a matching binder first.** Search `desk/*/BINDER.md` for a binder matching the project. If your org uses a prefix convention (e.g., `acme-`), check both prefixed and unprefixed names. If a binder exists with `status: active` or `status: parked`, create the file inside that binder directory.

If no binder matches, create a new binder directory at `desk/` root:
- Use your org prefix if applicable: `desk/{prefix}{project}/`
- Otherwise: `desk/{project}/`

File naming: `{project}-{descriptor}.md` (e.g. `payments-redesign-spec.md`)

### Step 4: Create or Update

**If new spec:**
- Read `library/templates/spec.md` for the template structure (if it exists)
- Create a new file with the naming convention above
- Add YAML frontmatter: `status: draft` and `type: spec`
- Follow the template structure: Doc Purpose -> Requirements Overview (bucketed) -> JTBD -> FR -> Success Criteria -> Non-Goals -> Open Questions
- Pre-fill sections with context gathered from existing files
- Leave open questions as checkboxes where you need input

**If existing spec:**
- Read the current file
- Apply the requested changes
- Preserve the overall structure and voice

### Step 5: Writing Style

Follow the voice principles from `library/reference/me.md`:
- Lead with the point, not the setup
- Name things concretely — real systems, real roles, real numbers
- Recommend, don't hedge
- Say what you're NOT doing

### Step 6: Review

After writing, summarize:
- What was created or changed
- Open questions that need answers
- Suggested next steps:
  - If the spec needs eng review first -> suggest handing off to engineering
  - If implementation is non-trivial -> suggest executing in a separate focused session
  - If implementation is small (< 5 files) -> suggest executing directly in a single session

## Tools Used

- Read, Write, Glob, Grep (file operations)
- Notion MCP: `notion-search`, `notion-fetch` (context gathering — only if `.claude/notion.yaml` is configured)
