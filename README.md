# Work-OS

work-os is an opinionated starter workspace for PMs, founders, and
other knowledge workers using Claude Code and Codex.

It ships with fictional demo projects, plans, commitments, and
reference material so you can try the workflow before personalizing it.

## Quickstart

### Claude Code

1. Install Claude Code:

   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   Official docs now recommend the native installer. If you prefer
   Homebrew on macOS, `brew install --cask claude-code` also works.

2. Clone the repo and open Claude Code:

   ```bash
   git clone https://github.com/aylee/work-os.git
   cd work-os
   claude
   ```

3. Sign in on first launch, then run:

   ```text
   /desk
   ```

The demo workspace already includes a weekly plan, two sample binders,
commitments, and a backburner. No setup is required to see the system
work.

### Codex

1. Install Codex:

   ```bash
   npm install -g @openai/codex
   ```

   On macOS, `brew install codex` is also supported.

2. Clone the repo and start Codex:

   ```bash
   git clone https://github.com/aylee/work-os.git
   cd work-os
   codex
   ```

3. Sign in with ChatGPT or an API key on first launch, then start with
   a prompt like:

   ```text
   Read AGENTS.md and docs/agent-guide.md, then summarize the current demo desk using areas/work/plans.md and desk/*/BINDER.md.
   ```

Codex does not use Claude slash commands. It uses the same repo
structure and shared agent contract.

## Make It Yours

After trying the demo, run `/setup` in Claude Code to replace the demo
identity and work context with your own. Setup is meant to personalize
user-owned files such as:

- `library/reference/me.md`
- `areas/work/AREA.md`
- `desk/*/BINDER.md`
- `.claude/notion.yaml` if you opt into integrations

It does not rewrite the shared repo contract in `AGENTS.md`,
`CLAUDE.md`, or `docs/agent-guide.md`.

For multi-session work, keep local working notes in `cc_state/`. That
directory is per-clone, gitignored, and intentionally untracked.

## Claude vs Codex

| Runtime | What you get |
| --- | --- |
| Claude Code | Full slash-command workflow via `.claude/skills/` (`/desk`, `/open`, `/setup`, `/brief`, `/review`, and more) |
| Codex | First-class support through `AGENTS.md`, `docs/agent-guide.md`, the binder/area structure, templates, and local `cc_state/` |

The repo aims for shared structure across both tools, not slash-command
parity.

## Maintainer Workflow

Maintainers should start with
`library/guides/maintainer-workflow.md` for the canonical workflow for
maintaining, auditing, and publishing work-os. Run
`python3 library/scripts/audit_public_hygiene.py` before publishing to
catch placeholder leakage and demo-content drift; the audit details live
in `library/guides/maintainer-hygiene.md`.

## What You Get

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Canonical cross-tool repo contract |
| `docs/agent-guide.md` | Detailed shared guide for Claude Code and Codex |
| `desk/` | Active project binders, one directory per workstream |
| `areas/` | Durable work context such as strategy, plans, commitments |
| `library/` | Reference docs, templates, guides, scripts, dotfiles |
| `memory/` | Committed corrections, decisions, reviews, session exports |
| `cc_state/` | Hot working state for plans, notes, traces |
| `.claude/skills/` | Claude Code slash commands |

Track what you owe people in `areas/work/commitments.md`, what is queued
in `areas/work/backburner.md`, and what matters this week in
`areas/work/plans.md`.

## Claude Code Skills

work-os currently ships with 14 Claude Code slash commands. The most
important ones are:

- `/desk` for weekly focus and desk state
- `/open <project>` for binder-based project work
- `/brief`, `/spec`, `/rfc`, `/research`, and `/decision` for drafting
- `/review` for weekly reflection and system cleanup
- `/setup` for personalization

See `library/guides/skills-reference.md` for the full list.

## Working Model

### Writing

The writing workflow is:

1. Shape the problem.
2. Draft with the right template or skill.
3. Iterate in conversation.
4. Polish with editing guidance.

### Memory

The system compounds through a simple loop:

```text
Capture -> Store -> Analyze -> Apply
```

- `cc_state/` holds active, local working state
- `memory/` holds committed corrections, decisions, reviews, and session
  exports

## Requirements

- macOS or Linux
- git recommended, not required
- [Claude Code](https://code.claude.com/docs/en/quickstart) for the
  full slash-command UX
- [Codex](https://developers.openai.com/codex/quickstart) supported
  through the repo contract and markdown structure
- Optional: [Homebrew](https://brew.sh) for CLI tools in `Brewfile`

[Ghostty](https://ghostty.org/) is the recommended terminal for
work-os.

## No Git? No Problem

The core system is still just markdown files in folders. Without git,
you lose history and some convenience, but the workspace still functions:

- Skills that commit will skip the commit step
- `/recent` falls back to file modification dates
- `/review` can display results in conversation instead of writing a
  review file

Works fine in Google Drive, Dropbox, iCloud, or any synced folder.

## Project Structure

```text
work-os/
├── AGENTS.md                  # Canonical cross-tool repo contract
├── CLAUDE.md                  # Thin Claude shim pointing to AGENTS.md
├── Brewfile                   # CLI tools
├── docs/
│   └── agent-guide.md         # Shared detailed agent guide
├── .claude/
│   ├── settings.json          # Safe repo defaults for Claude Code
│   ├── notion.yaml.example    # Integration template
│   └── skills/                # Claude Code slash commands
├── desk/                      # Project binders
│   └── z_archive/             # Archived binders
├── areas/                     # Work context and planning
├── library/                   # References, templates, guides, scripts
├── memory/                    # Committed corrections, decisions, reviews
├── cc_state/                  # Working state (plans, traces, spikes)
└── scratch/                   # Throwaway thinking
```

## License

See [LICENSE](LICENSE).
