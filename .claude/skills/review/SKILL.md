---
name: review
description: Weekly review — close the loop, archive the week, set direction for next.
disable-model-invocation: true
---

Weekly review that archives This Week, synthesizes the past week's work, surfaces corrections and patterns, and sets direction. Closes the compounding loop: capture > analyze > apply.

## Usage

```
/review
```

## Workflow

### Step 1: Gather the Week's Work

**Binders:** Find all `desk/*/BINDER.md` files (excluding `desk/z_archive/`). Read each and extract the Last Session block. Filter to binders where the Last Session date falls within the past 7 days.

**Corrections:** List files in `memory/corrections/`. Read any with `status: open`. Group by `domain` tag.

**Decisions:** List files in `memory/decisions/`. Read any with a date prefix (YYYY-MM-DD) from the past 7 days.

### Step 2: Compare Planned vs Actual

Read `areas/work/plans.md`.

Display what was planned alongside what actually happened this week (from binder activity in Step 1). Use a side-by-side or annotated format:

```markdown
## Planned vs Actual

**Planned:**
{plans.md contents}

**What happened:**
- {binder} — {what shipped/progressed}
- {binder} — {what shipped/progressed}

**Unplanned work:**
- {anything that came up not in the plan}

**Carried:**
- {planned items that didn't land}
```

This section gets archived into the review file.

### Step 3: Analyze Corrections

Present all open corrections grouped by domain. Look for:
- **Recurring patterns** — multiple corrections in the same domain = systemic issue
- **Promotion candidates** — patterns mature enough to graduate to `library/`
- **Quick wins** — corrections with obvious system fixes (update a skill, fix CLAUDE.md)

For each open correction or pattern, propose a concrete system change:
- "This correction suggests updating [skill/file]"
- "These N corrections about [domain] suggest [change]"

Ask the user which to act on. Then:
1. Make the changes (edit skills, CLAUDE.md, reference docs, conventions)
2. Delete resolved correction files from `memory/corrections/`

### Step 4: Look Ahead — Backburner + Commitments Review

If `areas/work/commitments.md` exists, read it. Surface any items that look stale or overdue. Ask: "Any commitments to mark done or update?"

If `areas/work/backburner.md` exists, read it. Present the current backburner items grouped by person or theme.

Ask: "Any backburner items to promote for next week? Any new items to add?"

If promoting: remove from backburner.md (git has history).
If adding: append to the appropriate section.

Then ask: "What are your top priorities for next week?"

Combine the answer with open items from active binders to draft next week's priorities.

### Step 5: Write the Review

**If `.git/` exists:** Create `memory/reviews/YYYY-WNN.md` where YYYY is the year and WNN is the ISO week number.

**If `.git/` doesn't exist:** Display the review in the conversation instead of writing to a file.

Format:

```markdown
---
week: YYYY-WNN
date-range: YYYY-MM-DD to YYYY-MM-DD
---

# Week NN Review

## Planned vs Actual

**Planned:**
{plans.md contents}

**What happened:**
- **project/** — What shipped/progressed.

**Unplanned:**
- Anything not in the original plan.

**Carried:**
- Items that didn't land this week.

## Desk
- **project/** — What happened. Next: what's next.
- **project/** — What happened. Next: what's next.
- Stale: **project/** (not touched in N days)

## Corrections
- {domain}: {summary} [applied | keep | retracted]

## Patterns
Cross-project observations, if any. Omit section if nothing notable.

## Next Week
- [ ] Priority 1
- [ ] Priority 2
- [ ] Priority 3
```

### Step 6: Update Plans

Update `areas/work/plans.md` with next week's priorities:

- If the user provided next week's priorities in Step 4, write them as the new `## This Week` using the standard format
- Otherwise, leave it empty (just the heading) so `/desk` will trigger the curation flow on Monday

### Step 7: Commit

**If `.git/` exists:** Stage and commit the review file plus any updated files:

```
git add memory/reviews/YYYY-WNN.md areas/work/plans.md areas/work/backburner.md memory/corrections/ library/...
git commit -m "Add weekly review WNN"
```

**If `.git/` doesn't exist:** Skip this step. The files are already saved.

## Tools Used

- Glob, Read (find binders, read corrections, decisions, areas/work/plans.md, backburner.md)
- Edit, Write (create review file, update areas/work/plans.md, update backburner.md, delete resolved corrections)
- Bash (git log for file activity, git commit — only if `.git/` exists)
