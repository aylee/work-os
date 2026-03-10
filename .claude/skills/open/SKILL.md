---
name: open
description: Open a project binder — load its context, show where you left off, and get ready to work.
disable-model-invocation: true
---

Open a project binder and load its full context for a working session.

## Usage

```
/open my-project
/open website
/open bookkeeping
```

The argument is a project name (matches binder directory name). Case-insensitive, partial matches OK.

## Workflow

### Step 1: Find the Binder

Search for a binder directory matching the argument:
- Try exact match first: `desk/{name}/BINDER.md`
- If your org uses a prefix convention (e.g., `acme-`), also try `desk/{prefix}{name}/BINDER.md`
- Then try partial match: `desk/*{name}*/BINDER.md`
- If no match found, list available binders and ask which one.
- Skip `desk/z_archive/` unless the user explicitly asks to open an archived binder.

### Step 2: Read BINDER.md

Read the full BINDER.md. Extract:
- Project name, status, type
- External links (from frontmatter — Linear, Notion, GitHub, etc.)
- Context section (key people, related resources)
- Last Session (date, what happened, open items, next)

### Step 3: Load Area Context

Based on the binder's location or prefix:
- If the binder relates to work → Read `areas/work/AREA.md` if not already loaded
- Other binders → Load relevant area context if it exists

### Step 4: List Binder Contents

List all files in the binder directory (excluding BINDER.md itself). Show their names, frontmatter status, and type so the user knows what's available to work on.

### Step 5: Present Resume Summary

Display a concise orientation:

```markdown
## {Project Name}

{one-liner description}

**Status:** {status} | **Last session:** {date}

### Where We Left Off
{Last Session content — what happened, open items, next}

### Files in This Binder
- `{filename}` — {type} · {status}
- ...

What do you want to work on?
```

### Step 6: Session Tracking

When the user finishes working on this binder (either explicitly says so, or moves to a different topic), prompt two things:

1. "Want me to update the Last Session in BINDER.md?"
2. "Anything the system got wrong, or an insight worth capturing? (Goes to `memory/corrections/`)"

**BINDER.md update** — If yes, update the Last Session block with:
- Today's date
- What happened this session
- What's still open
- What to do next

If `.git/` exists, commit the BINDER.md update.

**Correction capture** — If the user notes a correction, create a new file in `memory/corrections/` with this format:

```yaml
---
date: YYYY-MM-DD
domain: tooling | writing | architecture | workflow | naming | conventions
status: open
source: session
---

## What happened
[What was suboptimal]

## Should have been
[What the correct behavior looks like]

## Why
[Root cause or context]
```

## Tools Used

- Glob, Read (find and parse binders)
- Edit (update Last Session)
- Bash (git commit, if `.git/` exists)
