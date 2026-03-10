# Tooling Setup

CLI tools, terminal recommendations, dotfiles, and optional integrations.

---

## Brewfile

The `Brewfile` at the repo root includes CLI tools that work well with Claude Code. Install them all with:

```bash
brew bundle --file=Brewfile
```

Here's what each tool does and why it's included:

| Tool | What it does | Why it's here |
|------|-------------|---------------|
| **bat** | `cat` with syntax highlighting and line numbers | Easier to read file contents in the terminal. Claude Code uses it internally. |
| **fzf** | Fuzzy finder for files, commands, and history | Fast file navigation. `ctrl+r` for command history search. |
| **gh** | GitHub CLI | Create PRs, manage issues, and review code without leaving the terminal. |
| **glow** | Render markdown in the terminal | Read markdown files (briefs, specs, reviews) with formatting, right in the terminal. |
| **jq** | JSON processor | Parse API responses, config files, and Claude Code session data. |
| **ripgrep** | Fast search (`rg`) | Claude Code uses this for code search. Also useful for searching your own docs. |
| **tldr** | Simplified man pages | Quick reference for command syntax. `tldr tar` instead of `man tar`. |
| **tree** | Directory tree viewer | See your project structure at a glance. `tree desk/` shows all binders. |
| **ghostty** | Terminal emulator | Fast, minimal, native macOS terminal. See Terminal section below. |

---

## Terminal Recommendation

Claude Code runs in your terminal. The terminal you choose affects your experience. Three good options:

### cmux

**Best for:** People who want a purpose-built environment for agentic workflows.

[cmux](https://www.cmux.dev/) is a terminal built for working with AI agents. Key features:

- **Vertical sidebar tabs** -- each tab is a separate Claude Code session, visible at a glance
- **Notification bell** -- get notified when a long-running command finishes
- **Session management** -- name and organize your terminal sessions
- **Built-in split panes** -- no tmux configuration needed

cmux is not in the Brewfile by default (it's a paid app). If you want it, uncomment the line in the Brewfile or install directly from their site.

### Ghostty

**Best for:** People who want speed and simplicity.

[Ghostty](https://ghostty.org/) is a GPU-accelerated terminal emulator that's fast and minimal. Key features:

- **Native macOS feel** -- tabs, splits, and keybindings work like you'd expect
- **Very fast rendering** -- noticeable difference with large output
- **Simple config** -- a single config file, no Lua or complex scripting
- **Good font rendering** -- important when you're reading docs all day

The Brewfile includes Ghostty. After install, config lives at `~/.config/ghostty/config`. A starter config is included in `library/dotfiles/ghostty/config`.

### VS Code Terminal

**Best for:** People who want to stay in their editor.

The VS Code integrated terminal works fine with Claude Code. You lose some terminal-native features (tabs, notifications) but gain proximity to your editor. If you're already a VS Code user, start here and switch later if you feel limited.

---

## Dotfiles

The `library/dotfiles/` directory contains config files you can symlink to their expected locations.

### What's included

```
library/dotfiles/
  claude/
    settings.json    -- Claude Code user settings (permissions, MCP servers)
  ghostty/
    config           -- Ghostty terminal config
```

### How to use them

**Option 1: Symlink (recommended)**

Symlinks mean the config files in your repo are the source of truth. Changes sync automatically.

```bash
# Claude Code settings
ln -sf $(pwd)/library/dotfiles/claude/settings.json ~/.claude/settings.json

# Ghostty config
mkdir -p ~/.config/ghostty
ln -sf $(pwd)/library/dotfiles/ghostty/config ~/.config/ghostty/config
```

**Option 2: Copy**

If you don't want symlinks, copy the files:

```bash
cp library/dotfiles/claude/settings.json ~/.claude/settings.json
cp library/dotfiles/ghostty/config ~/.config/ghostty/config
```

The downside: changes to the repo copy won't propagate. You'll need to re-copy after updates.

### Adding your own dotfiles

To track additional configs (`.gitconfig`, `.zshrc`, shell aliases), add them to `library/dotfiles/` and create symlinks. Common additions:

```
library/dotfiles/
  git/
    .gitconfig
    .gitignore_global
  shell/
    .zshrc
    aliases.sh
```

---

## Optional Integrations

work-os skills can pull context from external tools via MCP (Model Context Protocol) servers. None of these are required -- the system works fully with just local files.

### Notion MCP

**What it enables:** Skills like `/brief`, `/spec`, and `/research` can search and read your Notion databases for context. Meeting notes, goals, project pages -- anything in Notion becomes available for context gathering.

**Setup:**

1. Get a Notion API key at https://www.notion.so/my-integrations
2. Create an integration and share your databases with it
3. Add the Notion MCP server to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@anthropic/claude-ai-mcp-notion"],
      "env": {
        "NOTION_API_KEY": "your-key-here"
      }
    }
  }
}
```

4. Add your database URLs to `.claude/notion.yaml`:

```yaml
databases:
  goals:
    url: "https://www.notion.so/your-workspace/abc123"
    description: "Goals and OKRs database"
  meetings:
    url: "https://www.notion.so/your-workspace/def456"
    description: "Meeting notes database"
```

### Linear MCP

**What it enables:** Claude can read and create Linear issues, check project status, and cross-reference your roadmap.

**Setup:**

1. Get a Linear API key from Settings > API
2. Add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "@anthropic/claude-ai-mcp-linear"],
      "env": {
        "LINEAR_API_KEY": "your-key-here"
      }
    }
  }
}
```

### Slack MCP

**What it enables:** Claude can search and read Slack channels. Useful for finding past discussions, pulling context from threads, and drafting messages.

**Setup:**

1. Your Slack workspace admin needs to approve the integration
2. Add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@anthropic/claude-ai-mcp-slack"],
      "env": {
        "SLACK_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Google Drive MCP

**What it enables:** Claude can read docs from your Google Drive. Useful when shared documents live outside your repo.

**Setup:** Follow the instructions at the Google Drive MCP server repository. Configuration is similar to the others -- add the server to `.claude/settings.json` with your credentials.

---

## Security Notes

- **API keys in settings.json:** The `.claude/settings.json` file may contain API keys. The `.gitignore` should exclude it from version control. If you're symlinking from `library/dotfiles/claude/settings.json`, make sure that file is also gitignored or that you use environment variables instead of hardcoded keys.
- **Environment variables:** The safer approach is to set API keys as environment variables in your shell profile and reference them in the MCP config. Most MCP servers support `${ENV_VAR}` syntax.
- **Notion permissions:** Only share the specific databases your integration needs. Don't give it access to your entire workspace.
