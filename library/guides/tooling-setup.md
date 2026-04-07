# Tooling Setup

CLI tools, runtime expectations, dotfiles, and optional integrations for
work-os.

---

## Agent Runtimes

work-os supports two usage modes:

- **Claude Code** for the full slash-command workflow under
  `.claude/skills/`
- **Codex** through the shared repo contract in `AGENTS.md`, the binder
  and area structure, and local `cc_state/`

The repo contract is shared. The UX is not identical.

`cc_state/` is the shared local working-state directory for both tools.
Keep it untracked and use it for active plans, notes, traces, and
spikes.

## Install the runtimes

### Claude Code

Anthropic's current recommended install path is the native installer:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

On macOS, Homebrew is also supported:

```bash
brew install --cask claude-code
```

Start Claude Code with `claude` and complete the login flow on first
launch.

### Codex

OpenAI's current Codex CLI install path is:

```bash
npm install -g @openai/codex
```

On macOS, Homebrew is also supported:

```bash
brew install codex
```

Start Codex with `codex` and sign in with ChatGPT or an API key on
first launch.

---

## Brewfile

The root `Brewfile` contains terminal and CLI tools that pair well with
agent-driven work. Install them with:

```bash
brew bundle --file=Brewfile
```

| Tool | What it does | Why it's here |
| --- | --- | --- |
| **bat** | `cat` with syntax highlighting and line numbers | Easier file inspection in the terminal |
| **fzf** | Fuzzy finder | Fast navigation through files and command history |
| **gh** | GitHub CLI | Pull requests, issues, and reviews without leaving the terminal |
| **glow** | Terminal markdown renderer | Read briefs, specs, and reviews comfortably |
| **jq** | JSON processor | Parse config and API responses |
| **ripgrep** | Fast search (`rg`) | Core text search for repo exploration |
| **tldr** | Simplified man pages | Quick syntax refreshers |
| **tree** | Directory tree viewer | Easy binder and repo overviews |
| **ghostty** | Terminal emulator | Fast terminal with simple config |

---

## Terminal Recommendation

Any solid terminal works. Three good options:

### cmux

Best if you want a purpose-built environment for multiple long-running
agent sessions.

### Ghostty

Best if you want speed, simple configuration, and a native-feeling
terminal. A starter config lives at `library/dotfiles/ghostty/config`.

### VS Code Terminal

Best if you prefer working inside your editor and can live without some
terminal-native session features.

---

## Dotfiles

The `library/dotfiles/` directory contains optional configs you can
symlink into place.

### What's included

```text
library/dotfiles/
  claude/
    settings.json    # Claude Code user settings starter
  ghostty/
    config           # Ghostty config starter
```

### How to use them

**Option 1: Symlink**

```bash
ln -sf $(pwd)/library/dotfiles/claude/settings.json ~/.claude/settings.json
mkdir -p ~/.config/ghostty
ln -sf $(pwd)/library/dotfiles/ghostty/config ~/.config/ghostty/config
```

**Option 2: Copy**

```bash
cp library/dotfiles/claude/settings.json ~/.claude/settings.json
cp library/dotfiles/ghostty/config ~/.config/ghostty/config
```

Codex does not currently need repo-local dotfiles here. Its repo-facing
behavior comes from `AGENTS.md` and the workspace structure.

---

## Optional Integrations

External tools are optional. The repo works fine with only local files.

### Notion

Use Notion if you want Claude Code to read structured work context from
your databases.

Setup:

1. Get a Notion API key at https://www.notion.so/my-integrations
2. Create an integration and share only the databases you need
3. Copy `.claude/notion.yaml.example` to `.claude/notion.yaml`
4. Add your database URLs to `.claude/notion.yaml`
5. Add the MCP server to your Claude settings if you want live access

`.claude/notion.yaml` should stay local and untracked.

### Linear

Use Linear MCP if you want issue and project context during Claude Code
sessions.

### Slack

Use Slack MCP if you want Claude to search or read workspace
conversations.

### Google Drive

Use Google Drive MCP if important shared docs live outside the repo.

---

## Security Notes

- Keep repo-tracked config files free of secrets.
- Prefer environment variables over hardcoded API keys.
- Treat `.claude/notion.yaml` and any user-local settings as private.
- Only grant integrations access to the specific data they need.
