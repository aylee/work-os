---
name: sessions
description: List, search, and export Claude Code sessions across all repos.
disable-model-invocation: true
---

Manage Claude Code session history. Sessions are stored as UUID-named .jsonl files in `~/.claude/projects/{escaped-path}/`. Exports are full conversation transcripts in `memory/sessions/`. Auto-export via `library/scripts/export-session.sh` (delegates to `export-session.py`).

## Usage

```
/sessions list [N]       # List recent sessions (default: 10)
/sessions search <query> # Search across exported sessions
/sessions export         # Export all unexported sessions to memory/sessions/
/sessions reexport       # Re-export all sessions (overwrite existing)
```

## Modes

### `/sessions list [N]`

List recent sessions across all repos.

1. **Scan** `~/.claude/projects/*/` for `.jsonl` files
2. **For each file**, extract:
   - **Repo name**: derive from the directory name (e.g., `-Users-you-code-my-project` -> `my-project`). The escaped path uses hyphens for path separators.
   - **Session ID**: the UUID filename (without .jsonl)
   - **Date**: from the first line's `timestamp` field
   - **Topic signal**: from the first `type: "user"` message's content (first ~100 chars)
   - **Size**: file size in KB
3. **Cross-reference** with `memory/sessions/` to check if already exported:
   - Read each exported .md file's frontmatter `session_id` field
   - Mark matching sessions as "exported"
4. **Sort** by date (newest first), limit to N (default 10)
5. **Display** as a table

### `/sessions search <query>`

Search across exported session transcripts.

1. Grep for the query in `memory/sessions/*.md`
2. Display matches with filename and surrounding context
3. Limit to 10 most recent matches

### `/sessions export`

Run the export script. The script should be at `library/scripts/export-session.py`. If it exists:

```bash
python3 library/scripts/export-session.py
```

Exports all unexported sessions across all repos. Renders full conversation transcripts. Junk sessions auto-filtered.

If the script doesn't exist, inform the user and suggest creating it or manually exporting sessions.

### `/sessions reexport`

```bash
python3 library/scripts/export-session.py --reexport
```

Wipes and re-exports everything from scratch.

## Export Format

Each exported session is a readable markdown transcript:

```markdown
---
date: YYYY-MM-DD
repo: {repo-name}
session_id: {uuid}
type: session-export
---

# Session: {repo} (YYYY-MM-DD)

> First user message (topic signal)

---

**> User message**

Claude response text here.

  - Tool: summary
  - Tool: summary

More response text.
```

**What's included:** User prompts (bold), Claude text responses, tool call one-liners.
**What's excluded:** Thinking blocks, tool results, system messages, progress events.

## Configuration

The export script determines the output directory. By default, it should write to `memory/sessions/` relative to the repo root. If you need to customize this, set the `WORK_OS` environment variable to your repo's absolute path:

```bash
export WORK_OS=~/code/work-os
```

## Tools Used

- Bash (run export script, file listing, grep for search)
- Read (exported session files)
- Glob (find exported sessions in memory/sessions/)
