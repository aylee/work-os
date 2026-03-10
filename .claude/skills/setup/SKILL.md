---
name: setup
description: Onboarding wizard — personalize your work-os with identity, voice, areas, projects, and integrations.
disable-model-invocation: true
---

The onboarding wizard for work-os. A multi-step conversation that personalizes the system to you — your identity, writing voice, life areas, active projects, and integrations. Run it once to bootstrap, or re-run anytime to update.

## Usage

```
/setup
```

## Workflow

### Step 0: Detect State

Read `library/reference/me.md`. Check if it still contains `[YOUR NAME]` or `[Your Name]` placeholder text.

**If placeholders found (fresh install):**
- Say: "Welcome to work-os. Let's set it up for you. This takes about 5 minutes — I'll walk you through identity, writing voice, areas, projects, and optional integrations."

**If no placeholders (already personalized):**
- Say: "Looks like setup has already run. Want to re-run a specific section, or start fresh?"
- Offer choices: Identity, Voice, Areas, Desk, Integrations, Tooling, or Full Re-run
- If the user picks a section, jump to that step. If full re-run, proceed from Step 1.

---

### Step 1: Identity

Gather core identity information through conversation:

**Ask:**
- "What's your name?"
- "What's your role? (e.g., PM, engineer, designer, founder)"
- "What company or org are you with? (or 'independent' if solo)"
- "How technical are you? (This helps me calibrate — options: non-technical, technical enough, very technical)"

**Produce:**

1. **Update `library/reference/me.md`** — Replace all `[YOUR NAME]` / `[Your Name]` placeholders with the real name. Fill in the identity section at the top:

```markdown
# About Me

**Name:** {name}
**Role:** {role}
**Company:** {company}
**Technical level:** {level}
```

2. **Update `CLAUDE.md`** — If CLAUDE.md contains a `{USER_NAME}` placeholder in the header or intro, replace it with the user's name.

---

### Step 2: Writing Voice

Present two paths:

**"Do you have 2-3 docs you've written that represent your voice? I can analyze them to calibrate."**

#### Path A: Has Examples

- Accept pasted text or file paths
- Read/analyze the provided writing samples
- Extract patterns:
  - Sentence length tendencies (short and punchy? long and layered?)
  - Vocabulary level (casual, professional, technical)
  - Structure preferences (headers? bullets? flowing prose?)
  - Distinctive habits (em dashes, parentheticals, rhetorical questions, specific phrases)
  - Tone (direct, warm, authoritative, conversational)
- Write findings to `library/reference/me.md` under a `## Voice` section:

```markdown
## Voice

**Calibrated from:** {N} writing samples ({date})

**Tendencies:**
- {pattern 1}
- {pattern 2}
- {pattern 3}

**Anti-patterns (avoid these):**
- {anti-pattern 1}
- {anti-pattern 2}
```

- If `library/reference/writing-guide.md` exists, update its Voice DNA section with the same findings. If it doesn't exist, skip — the me.md Voice section is sufficient.

#### Path B: Skip for Now

- Say: "No problem. I'll ship with generic defaults. Your voice profile will fill in over time as you use `/editor` — it learns from your edits."
- Leave me.md Voice section with a placeholder:

```markdown
## Voice

*Not yet calibrated. Run `/setup` with writing samples, or use `/editor` — your voice profile builds over time.*
```

---

### Step 3: Areas

Show the default area structure:

```
areas/
  work/       — Your job, career, professional projects
  health/     — Physical and mental health
  finances/   — Money, budgets, investments
  personal/   — Relationships, hobbies, personal growth
```

**Ask:** "These are your life areas — domains you maintain ongoing. Want to add, remove, or rename any?"

- If adding: create the directory and a starter `AREA.md` with the area name as H1 and a placeholder description
- If removing: confirm, then remove the directory
- If renaming: move the directory

**Deep-fill work area:**

**Ask:** "Let's fill in your work context. Tell me about your company — what does it do, what's your team, what are you focused on this quarter?"

Update `areas/work/AREA.md` with:
- Company name and what it does (1-2 sentences)
- Team/role context
- Current focus / Big Rocks (if the user provides them)

If the user has an org prefix convention for projects (e.g., `acme-` for Acme Corp projects), note it:

**Ask:** "Do your work projects use a prefix? (e.g., 'acme-' for Acme Corp binders). This helps organize the desk. Enter a prefix or skip."

If provided, note the convention in `areas/work/AREA.md` under a Conventions section.

---

### Step 4: Desk

**Ask:** "What are you actively working on? Name 1-3 projects. Just a name and one-liner for each."

For each project:
1. Create `desk/{name}/BINDER.md` (using org prefix if set in Step 3)
2. Populate with:

```markdown
---
status: active
type: project
---

# {Project Name}

{one-liner description}

## Context

*Fill in key people, links, and resources as you work.*

## Last Session

*No sessions yet. Run `/open {name}` to start working.*
```

**Check for dummy binders:** If `desk/` contains example/dummy binders from the template (check for names like `example-project`, `demo`, or BINDER.md files with placeholder content), ask:

"I see some example binders in desk/. Want me to remove them?"

If yes, delete the dummy binder directories.

---

### Step 5: Integrations

**Say:** "Optional integrations. Skip any you don't use."

#### Notion

**Ask:** "Do you use Notion? If so, I can connect it for context gathering (meeting notes, goals, project pages)."

If yes:
- Create `.claude/notion.yaml` with a starter structure:

```yaml
# Notion Database Registry
# Add database URLs here. Skills will use these for context gathering.
# Format: name: { url: "https://notion.so/...", description: "..." }

databases: {}
  # Example:
  # goals:
  #   url: "https://www.notion.so/your-workspace/abc123"
  #   description: "Goals and OKRs database"
  # meetings:
  #   url: "https://www.notion.so/your-workspace/def456"
  #   description: "Meeting notes database"
```

- Tell the user: "Add your database URLs to `.claude/notion.yaml` when ready. Skills like `/brief`, `/spec`, and `/research` will use them for context."
- Update CLAUDE.md routing table if it has a Notion row — confirm it points to `.claude/notion.yaml`

#### Linear

**Ask:** "Do you use Linear for project management?"

If yes:
- Note in `areas/work/AREA.md` that Linear is used
- Suggest adding the Linear MCP server to `.claude/settings.json` if not already present

#### Slack

**Ask:** "Do you use Slack?"

If yes:
- Suggest adding the Slack MCP server to `.claude/settings.json` if not already present
- Note that Claude can search and read Slack channels when configured

#### Google Drive

**Ask:** "Do you use Google Drive for shared docs?"

If yes:
- Note in `areas/work/AREA.md` that Google Drive is used for shared documents
- Suggest relevant MCP setup if available

---

### Step 6: Tooling

**Say:** "A few optional tooling recommendations."

**Terminal:**
- "For the best Claude Code experience, consider:"
  - **cmux** (https://www.cmux.dev/) — vertical tabs, sidebar, notifications bell. Built for agentic workflows.
  - **Ghostty** (https://ghostty.org/) — fast, minimal, great keybindings. Pairs well with tmux.
  - **VS Code terminal** — works fine if you prefer staying in your editor.

**Brewfile:**
If `library/dotfiles/Brewfile` exists:
- Ask: "There's a Brewfile with recommended tools. Want to install them? (`brew bundle --file=library/dotfiles/Brewfile`)"
- If yes, run the install

**Dotfiles:**
If `library/dotfiles/` contains config files:
- List what's available (e.g., gitconfig, shell aliases, editor config)
- Ask if the user wants to symlink any of them

---

### Step 7: Cleanup + Commit

**Summary:** Display everything that was created or modified:

```markdown
## Setup Complete

**Identity:** {name}, {role} at {company}
**Voice:** {calibrated from N samples | defaults, will calibrate over time}
**Areas:** {list of areas}
**Projects:** {list of binders created}
**Integrations:** {list of configured integrations, or "none yet"}

### Files modified:
- library/reference/me.md
- CLAUDE.md
- areas/work/AREA.md
- desk/{project}/BINDER.md (x N)
- .claude/notion.yaml (if configured)
```

**Cleanup:** If any template placeholder files remain (dummy binders, example content), offer to remove them.

**Commit:** If `.git/` exists:
- Ask: "Want me to commit this as your initial setup?"
- If yes, stage all changed files and commit:

```
git add -A
git commit -m "Initial work-os setup for {name}"
```

---

### Step 8: What's Next

Close with a quick-start guide:

```markdown
## Get Started

Here are 4 commands to try:

1. **`/desk`** — See your weekly plan and project status
2. **`/open {project}`** — Open a project and start working
3. **`/brief {topic}`** — Write a project brief or 1-pager
4. **`/shape {question}`** — Think through a problem before building

Other useful skills:
- `/spec` — Write a product spec
- `/rfc` — Propose an approach for debate
- `/research` — Structured research and analysis
- `/decision` — Record a decision with rationale
- `/editor` — Polish a document's voice and formatting
- `/reflect` — Weekly review and course correction
- `/recent` — See recently edited files
- `/sessions` — Manage Claude Code session history

Your system improves over time. Corrections go to `memory/corrections/`,
and `/reflect` closes the loop by turning patterns into system upgrades.
```

---

## Design Principles

- **Conversational, not scripted.** Each step is a dialogue. Ask, listen, produce. Don't dump forms.
- **Progressive disclosure.** Core setup (Steps 1-4) takes 3 minutes. Integrations and tooling are optional.
- **Idempotent.** Re-running any step updates in place rather than duplicating. Detect existing state before writing.
- **No silent writes.** Always show what will be created/modified before doing it. Ask for confirmation on destructive operations.

## Tools Used

- Read, Write, Edit, Glob (file operations)
- Bash (brew bundle, git commit, directory operations)
- Notion MCP tools (only during integration setup, if user opts in)
