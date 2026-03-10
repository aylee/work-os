---
name: desk
description: Orient — what's on your plate? This Week, desk state, backburner, suggested focus.
disable-model-invocation: true
---

Orient to the current state of work. Shows weekly focus, active binders, backburner highlights, and suggests today's focus.

## Usage

```
/desk
```

## Workflow

### Step 1: This Week

Read `areas/work/plans.md` and find the `## This Week` section.

**If present and fresh (date within 7 days):**
- Display the section prominently at the top
- This is the anchor — everything else supports it

**If empty or stale (>7 days since the week date):**
- Enter the **weekly curation flow** (see below)

### Step 2: Desk State

Find all `desk/*/BINDER.md` files (exclude `desk/z_archive/`). Read each and extract:
- **Project name** (from H1)
- **Status** (from frontmatter: active, parked, shipped)
- **One-liner** (first paragraph after H1)
- **Last Session date** (from the Last Session section)
- **Next** (from the Last Session -> Next line)

Group by status and display:

```markdown
## Desk

**Active:**
- **{binder}/** — {one-liner}. Last: {date}. Next: {next action}.

**Parked:**
- **{binder}/** — {one-liner}.
```

Sort active binders by last session date (most recent first). Flag any active binder with a last session 14+ days old as stale.

### Step 3: Backburner Highlights

Read `areas/work/backburner.md`. Scan for items that connect to what's currently active on the desk (e.g., a backburner item for someone working on an active binder's project). Surface 1-3 timely items, if any.

If no items seem timely, or if backburner.md doesn't exist, skip this section.

### Step 4: Suggested Focus

Based on This Week priorities + desk state + any timely backburner items, suggest 2-3 things to focus on today. Keep it concrete and actionable. Cross-reference `areas/work/AREA.md` Big Rocks section (if it exists) to ensure suggestions align with active goals.

```markdown
## Today

Based on This Week and desk state:
1. {suggestion}
2. {suggestion}
3. {suggestion}
```

---

## Weekly Curation Flow

Triggered when `## This Week` is empty or stale (start of week).

1. **Read inputs:**
   - Active binders' Next sections (from Step 2)
   - `areas/work/backburner.md` for promotion candidates (if it exists)
   - Most recent file in `memory/reviews/` — read its "Next Week" section if it exists
   - `areas/work/AREA.md` Big Rocks section for goal alignment (if it exists)

2. **Draft priorities:**
   - Present a draft grouped by theme/outcome (not by project)
   - Keep it terse — should read cleanly if pasted into Slack or a standup
   - Use the format:
     ```markdown
     ## This Week

     *Week of {Mon date}*

     - **{Theme}**
       - Item
       - Item
     - **{Theme}**
       - Item
     ```

3. **User edits** — wait for confirmation/changes

4. **Write** the final version to `areas/work/plans.md`'s `## This Week` section

---

## What This Skill Does NOT Do

- No Notion queries (use Notion tools directly if configured)
- No correction synthesis (that's `/reflect`)

## Tools Used

- Glob, Read (find binders, read areas/work/plans.md, read areas/work/AREA.md, read backburner.md, read reviews)
- Edit (write This Week section during curation flow)
