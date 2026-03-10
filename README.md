# Work-OS

A personal operating system for knowledge workers, powered by [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

Clone it. Try `/desk`. Then make it yours.

## Try It (2 minutes)

**Step 1.** Install Claude Code if you haven't:

    npm install -g @anthropic-ai/claude-code

Full instructions: https://docs.anthropic.com/en/docs/claude-code

**Step 2.** Open your terminal -- Ghostty, VS Code, Terminal.app, whatever you use.

**Step 3.** Clone and open the repo:

    git clone https://github.com/aylee/work-os.git
    cd work-os
    claude

**Step 4.** Type `/desk` and press Enter.

The repo ships with demo data -- two sample projects, a weekly plan, a backburner. `/desk` reads all of it and synthesizes your priorities. No setup needed to see it work.

## Make It Yours

Once you've seen the demo, type `/setup`. It walks you through replacing the sample data with your real work -- name, role, projects, writing voice. Takes about 5 minutes.

## What You Get

| Directory | Purpose |
|-----------|---------|
| `desk/` | Active project binders -- one folder per workstream |
| `areas/` | Work context -- company, role, priorities |
| `library/` | Reference docs, templates, guides, scripts |
| `memory/` | Corrections, decisions, reviews, session transcripts |
| `scratch/` | Throwaway thinking |

Track what you owe people (`areas/work/commitments.md`) and what's waiting in the wings (`areas/work/backburner.md`).

Plus 14 slash commands that read your context and produce real output -- briefs, specs, RFCs, research docs, decision records, and more.

## Skills

### Orientation
| Skill | What it does |
|-------|-------------|
| `/desk` | Weekly focus, desk state, suggested priorities |
| `/morning` | Quick daily briefing -- where you are, what matters today |
| `/open <project>` | Open a project binder, load context, resume where you left off |

### Writing
| Skill | What it does |
|-------|-------------|
| `/shape` | Understand a request before acting -- requirements gathering |
| `/brief <topic>` | Write a project brief or 1-pager |
| `/spec <topic>` | Write or iterate on a product spec / PRD |
| `/rfc <topic>` | Write an RFC -- propose approaches, frame tradeoffs |
| `/research <topic>` | Structured research and analysis |
| `/decision <topic>` | Record a decision with full context and rationale |
| `/editor <file>` | Editing pass -- tighten voice, fix formatting, sharpen structure |

### System
| Skill | What it does |
|-------|-------------|
| `/review` | Weekly review -- archive the week, surface patterns, set direction |
| `/recent` | Recently edited files (like a "recent docs" view) |
| `/sessions` | List, search, and export Claude Code session history |

### Setup
| Skill | What it does |
|-------|-------------|
| `/setup` | Onboarding wizard -- personalize everything |

## The Writing System

Four stages, each with its own skill and context budget:

1. **Shape** (`/shape`) -- Define scope and intent before building
2. **Draft** (`/brief`, `/spec`, `/rfc`, `/research`, `/decision`) -- Substance and coverage
3. **Iterate** (conversation) -- Add, remove, restructure, sharpen
4. **Polish** (`/editor`) -- Voice, formatting, sentence craft

Drafting skills load your identity and voice principles. `/editor` loads the full style guide with examples.

## The Memory System

The system learns from itself through a feedback loop:

```
Capture --> Store --> Analyze --> Apply
```

- **Sessions** auto-export as readable transcripts
- **Corrections** capture what went wrong and why
- **Decisions** record point-in-time rationale
- **Reviews** (`/review`) synthesize weekly, spot patterns, propose system changes

Fewer open corrections = system improving.

## After Setup

```
/desk              # See what's on your plate
/morning           # Quick daily briefing
/open my-project   # Jump into a project
/brief new feature # Draft a project brief
/shape big idea    # Think through a request before building
```

See `library/guides/getting-started.md` for a full orientation.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (required)
- macOS or Linux
- Optional: [Homebrew](https://brew.sh) (run `brew bundle` for CLI tools)
- Optional: git (skills degrade gracefully without it)

### Terminal

Any terminal works. We recommend:

- **[cmux](https://www.cmux.dev/)** -- Vertical tabs, sidebar, notifications bell. Built for Claude Code.
- **[Ghostty](https://ghostty.org/)** -- Fast, minimal, keyboard-driven.
- **VS Code** with the Claude Code extension also works great.

## No Git? No Problem

The core system is markdown files in folders. Git enhances it but isn't required:

- Skills that commit will skip the commit step
- `/recent` falls back to file modification dates
- `/review` displays the review in conversation instead of writing a file
- `/setup` asks about git and adapts accordingly

Works fine in Google Drive, Dropbox, iCloud, or any synced folder.

## Project Structure

```
work-os/
├── CLAUDE.md                  # System instructions (routing table, conventions)
├── Brewfile                   # CLI tools
├── .claude/
│   ├── settings.json          # Permissions
│   ├── notion.yaml.example    # Notion integration template
│   └── skills/                # 14 slash commands
├── desk/                      # Project binders (one folder per project)
│   └── z_archive/             # Shipped projects
├── areas/                     # Work context (company, role, priorities)
├── library/
│   ├── reference/             # me.md, writing-guide, frameworks, conventions
│   ├── templates/             # 10 document templates
│   ├── guides/                # Getting started, skills reference, tooling
│   ├── scripts/               # Session export tool
│   └── dotfiles/              # Terminal and editor configs
├── memory/
│   ├── corrections/           # What went wrong + why
│   ├── decisions/             # Point-in-time rationale
│   ├── reviews/               # Weekly synthesis
│   └── sessions/              # Exported conversation transcripts
└── scratch/                   # Throwaway thinking
```

## License

MIT
