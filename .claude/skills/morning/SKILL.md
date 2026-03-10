---
name: morning
description: Daily briefing — here's where you are and what matters today.
disable-model-invocation: true
---

Daily briefing. Reads weekly plan, binders, and goals to produce a "here's where you are" briefing. Lighter than `/desk` — no curation flow, just synthesis.

## Usage

```
/morning
```

## Workflow

### Step 1: This Week's Intentions

Read `areas/work/plans.md` -> `## This Week`.

If present and fresh, display as the anchor.
If empty or stale, note it and suggest running `/desk` for the weekly curation flow.

### Step 2: Active Binders

Glob `desk/*/BINDER.md` (exclude `desk/z_archive/`). Read each and extract:
- Project name, status, Last Session date, Next action

Flag any active binder with Last Session 14+ days old as **stale**.

### Step 3: Goal Cross-Reference

If `areas/work/AREA.md` has a Big Rocks or Goals section, read it. For each goal with linked projects:
- Check if the linked binder was touched recently (from Step 2 Last Session dates)
- Flag misalignment: goal deadline approaching but linked project stale

If `.claude/notion.yaml` is configured and has a Goals database URL, optionally fetch current goals for cross-reference.

If all projects are active, skip this section.

### Step 4: Output

```markdown
## This Week
{plans.md contents, or "No weekly plan set — run /desk to curate."}

## Today
Based on this week's plan and desk state:
1. {suggestion — concrete, actionable}
2. {suggestion}
3. {suggestion}

## Attention
- {Stale: project/ (not touched in N days)}
- {Misalignment: Goal X depends on project Y, last touched N days ago}
```

Omit any Attention items that don't apply. If nothing needs attention, omit the section entirely.

## What This Skill Does NOT Do

- No weekly curation (that's `/desk`)
- No correction synthesis (that's `/review`)
- No writing to files — this is read-only

## Tools Used

- Glob (find binders)
- Read (areas/work/plans.md, areas/work/AREA.md, binder files)
- Bash (date calculations for staleness)
