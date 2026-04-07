# Personal Information Architecture

Decision on how to organize information across systems.

## The Two Core Systems

| System | Role | What lives here |
|--------|------|-----------------|
| **Notion** | Database layer | Horizons of focus (Visions > Goals > Areas > Projects > Tasks), meeting notes, relational views, shared content |
| **work-os** | Working surface + memory | Binders (active specs/research), areas (domain context + Notion pointers), library (reference), memory (feedback loop) |

Supporting systems (optional — add what you use):

| System | Role | What goes here | Interface |
|--------|------|----------------|-----------|
| Company project tracker (Linear, Jira, etc.) | Work tracking | Engineering tickets, sprints, cycles | Browser / MCP |
| Google Drive / Confluence | Shared files | Decks, spreadsheets, docs others collaborate on | Browser |
| ~/Documents | Filing cabinet | PDFs, scans, legal docs you *receive* | Finder |

## The Decision Rules

- **Received it?** → ~/Documents
- **Tracking eng work?** → Your project tracker (Linear, Jira, etc.)
- **Tracking goals/plans/tasks?** → Notion
- **Writing it solo?** → work-os
- **Others need to edit it?** → Google Drive / Confluence
- **Team needs to reference it?** → Notion

## The Flow

```
Think in Notion → Draft in work-os → Ship to target repo or shared docs
                                   ↘ Share a deck? → Google Drive
                                   ↘ Side project? → ~/code/receipt-parser/
```

## Notion = Database Layer

Notion owns the full horizons of focus graph with relational databases:
- **Visions** → Goals → Areas → Projects → Tasks
- Meeting notes, external brain, reading list

Areas in work-os point TO Notion for detail. work-os doesn't replicate the graph.
`areas/work/AREA.md` links to Notion Goals database. `.claude/notion.yaml` has all database URLs (if configured).

## Work-OS = Working Surface + Memory

Work-os is where things get written and where the system learns. Two functions:

**Working surface** — the lifecycle:
1. **Draft** — Create artifact in a binder at `desk/`, iterate with Claude Code
2. **Ship** — Hand off to target repo, Notion, shared docs, or a ~/code/ project repo
3. **Archive** — Whole binder moves to `desk/z_archive/` intact

**Memory** — the feedback loop:
1. **Capture** — Sessions auto-export, corrections filed, decisions logged
2. **Store** — Append-only sessions, individual correction files, permanent decisions
3. **Analyze** — `/review` groups corrections by domain, spots patterns
4. **Apply** — System change made, correction deleted, review written

## Key Boundaries

1. **~/Documents = only files you *receive*.** PDFs, scans, legal docs. If you wrote it, it doesn't go here.

2. **Notion and work-os overlap is intentional.** Notion for sharing and discussing with the team. work-os for versioned solo iteration. Areas point to Notion for relational data.

3. **Shared docs = collaboration format.** If a doc needs to be a Google Slide, Sheet, or Doc because others edit it, it goes in shared docs. Solo writing work belongs in work-os.

4. **Project tracker = the eng work tracker.** Don't duplicate ticket status in work-os. Pull status across systems as needed.

5. **Code projects live in `~/code/`**, separate from work-os. work-os
holds PM artifacts (specs, research), `~/code/` holds the actual code.

6. **`.claude/notion.yaml` = the Notion database registry** (if configured). Machine-readable URLs for Goals, Projects, Tasks, Meeting Notes. Skills read this directly. Don't duplicate these URLs elsewhere.

## Project Structure

**For company work (example: SignalPath):**
- PM artifacts → `work-os/desk/mobile-app-redesign/mobile-redesign-brief.md`
- Code → `~/code/signalpath-app/`

**For side ventures:**
- PM artifacts → `work-os/desk/receipt-parser/notes.md`
- Code → `~/code/receipt-parser/`

**For personal scripts:**
- Just put everything in `~/code/daily-screenshot/`
- README.md *is* the spec
- Don't over-engineer personal projects

## ~/code Organization

Keep it flat until it gets messy. Don't pre-organize with subfolders like `tools/` or `sandbox/`. When it bugs you, clean it up.
