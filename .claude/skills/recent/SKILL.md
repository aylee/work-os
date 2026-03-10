---
name: recent
description: Show recently edited work files, pulled from git history or file modification times.
disable-model-invocation: true
---

Show recently edited work files — like a "recent docs" view powered by git or filesystem timestamps.

## Usage

```
/recent              # last 7 days (default)
/recent 3d           # last 3 days
/recent 2w           # last 2 weeks
```

The argument is a time window: a number followed by `d` (days) or `w` (weeks). Default is `7d`.

## Workflow

### Step 1: Parse the Time Window

If the user passed an argument (e.g., `3d`, `2w`), convert it to the appropriate time value:
- `3d` -> 3 days
- `2w` -> 2 weeks
- No argument -> 7 days

### Step 2: Get Recently Modified Files

**If `.git/` exists (preferred):**

Run:

```bash
git log --diff-filter=ACMR --name-only --pretty=format:"COMMIT_DATE:%ai" --since="{time window}" -- desk/
```

Parse the output to build a map of `file -> most recent date`. Each `COMMIT_DATE:` line sets the date for the filenames that follow it. A file may appear multiple times — keep only the most recent date.

Filter out any files that no longer exist on disk (deleted since the commit).

**If `.git/` doesn't exist (fallback):**

Use filesystem modification times. Run:

```bash
find desk/ -name "*.md" -type f -mtime -{days} -exec stat -f "%m %N" {} \;
```

On Linux, use `stat -c "%Y %n"` instead. Parse the output to build a map of `file -> modification timestamp`. Sort by timestamp descending.

### Step 3: Read Frontmatter

For each file, read just the first 10 lines to extract `status:` and `type:` from the YAML frontmatter. If a file has no frontmatter, use `-` as placeholder for both fields.

### Step 4: Group and Display

Group files by binder (the binder directory under `desk/` — e.g., `my-project`, `website`, `bookkeeping`).

Within each group, sort by most recent date (newest first). **For files inside binder directories, show the binder name as a prefix** (e.g., `my-project/vision-spec.md`).

**Also include binder-level activity:** For each binder that had its BINDER.md updated in the time window, show the binder with its Last Session date and next action — even if no individual files changed. This captures session-end updates that represent real work.

Format dates as relative labels:
- Today -> `today`
- Yesterday -> `yesterday`
- This week -> weekday name (e.g., `Monday`)
- Older -> `Mon DD` (e.g., `Feb 15`)

Display:

```markdown
## Recent — last {N} {days/weeks}

### {binder} ({count} files)

**Binders:**
- **{binder}/** — Last session: {date}. Next: {next action}.

**Files:**
- **{filename}** — {type} · {status} · {date}
- **{filename}** — {type} · {status} · {date}
```

If there are no recently modified files, say: "No work files changed in the last {window}. Try a wider window: `/recent 2w`"

## Tools Used

- Bash (git log or stat/find for file modification times)
- Read (frontmatter extraction)
