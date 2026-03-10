#!/usr/bin/env python3
"""
export-session.py — Export Claude Code JSONL sessions to readable markdown transcripts.

Usage:
  export-session.py                         # Export all unexported sessions from all repos
  export-session.py ~/code/my-project       # Export from one repo
  export-session.py --reexport              # Re-export all sessions (overwrite existing)
  echo '{"session_id":...}' | export-session.py --hook  # SessionEnd hook (stdin)
"""

import json
import os
import re
import sys
from pathlib import Path

# Point WORK_OS to your work-os directory, or set the environment variable.
WORK_OS = Path(os.environ.get("WORK_OS", Path.home() / "code" / "work-os"))
SESSIONS_DIR = WORK_OS / "memory" / "sessions"
CLAUDE_DIR = Path.home() / ".claude" / "projects"

SESSIONS_DIR.mkdir(parents=True, exist_ok=True)


def slugify(text: str, max_len: int = 50) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")[:max_len].rstrip("-")
    return s or "session"


def get_exported_ids() -> set[str]:
    ids = set()
    for f in SESSIONS_DIR.glob("*.md"):
        in_frontmatter = False
        for line in f.open():
            stripped = line.strip()
            if stripped == "---":
                if not in_frontmatter:
                    in_frontmatter = True
                    continue
                else:
                    break  # end of frontmatter, no session_id found
            if in_frontmatter and stripped.startswith("session_id:"):
                ids.add(stripped.split(":", 1)[1].strip())
                break
    return ids


def summarize_tool(name: str, inp: dict) -> str:
    """One-line summary of a tool call."""
    if name == "Read":
        p = inp.get("file_path", "")
        return f"Read {Path(p).name}" if p else "Read file"
    if name == "Write":
        p = inp.get("file_path", "")
        return f"Write {Path(p).name}" if p else "Write file"
    if name == "Edit":
        p = inp.get("file_path", "")
        return f"Edit {Path(p).name}" if p else "Edit file"
    if name == "Glob":
        return f"Glob `{inp.get('pattern', '')}`"
    if name == "Grep":
        return f"Grep `{inp.get('pattern', '')}`"
    if name in ("Bash", "bash"):
        cmd = inp.get("command", "")
        # First line, truncated
        first = cmd.split("\n")[0][:80]
        return f"Bash: `{first}`"
    if name in ("Agent", "Task"):
        desc = inp.get("description", inp.get("prompt", ""))[:80]
        st = inp.get("subagent_type", "")
        label = st if st else "Agent"
        return f"{label}: {desc}"
    if name == "WebFetch":
        return f"WebFetch {inp.get('url', '')[:60]}"
    if name == "WebSearch":
        return f"WebSearch `{inp.get('query', '')[:60]}`"
    if name == "Skill":
        return f"Skill /{inp.get('skill_name', '?')}"
    if name == "ToolSearch":
        return f"ToolSearch `{inp.get('query', '')}`"
    if name == "AskUserQuestion":
        return f"Asked: {inp.get('question', '')[:80]}"
    # MCP tools
    if name.startswith("mcp__"):
        parts = name.split("__")
        short = "__".join(parts[-2:]) if len(parts) >= 3 else name
        return f"{short}"
    return name


def extract_user_text(content) -> str | None:
    """Extract human-written text from a user message."""
    if isinstance(content, str):
        # Strip command wrapper tags
        text = re.sub(r"<command-message>.*?</command-message>", "", content, flags=re.DOTALL)
        text = re.sub(r"<command-name>.*?</command-name>", "", text, flags=re.DOTALL)
        text = re.sub(r"<command-args>.*?</command-args>", "", text, flags=re.DOTALL)
        text = re.sub(r"<local-command-caveat>.*?</local-command-caveat>", "", text, flags=re.DOTALL)
        text = re.sub(r"<local-command-stdout>.*?</local-command-stdout>", "", text, flags=re.DOTALL)
        text = re.sub(r"<system-reminder>.*?</system-reminder>", "", text, flags=re.DOTALL)
        text = re.sub(r"<task-notification>.*?</task-notification>", "", text, flags=re.DOTALL)
        text = text.strip()
        if not text:
            return None
        # Detect slash commands
        cmd_match = re.search(r"<command-name>(/\w+)</command-name>", content)
        if cmd_match:
            return cmd_match.group(1)
        return text
    if isinstance(content, list):
        texts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                t = item.get("text", "").strip()
                # Skip skill prompt injections and system content
                if t and not t.startswith("Base directory for this skill:"):
                    texts.append(t)
            elif isinstance(item, dict) and item.get("type") == "image":
                texts.append("[image]")
        return "\n".join(texts) if texts else None
    return None


def render_session(jsonl_path: Path) -> tuple[str, str, str]:
    """Parse JSONL and return (date, first_topic, markdown_body)."""
    lines = []
    session_date = None
    first_user_text = None
    tool_batch: list[str] = []

    def flush_tools():
        nonlocal lines, tool_batch
        if tool_batch:
            lines.append("")
            for t in tool_batch:
                lines.append(f"  - {t}")
            lines.append("")
            tool_batch = []

    for raw_line in jsonl_path.open():
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        try:
            msg = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        msg_type = msg.get("type")

        # Skip noise
        if msg_type in ("file-history-snapshot", "progress", "system", "queue-operation", "isSnapshotUpdate"):
            continue

        # Extract date from first user message
        if msg_type == "user" and not session_date:
            ts = msg.get("timestamp", "")
            if ts and len(ts) >= 10:
                session_date = ts[:10]

        role = (msg.get("message") or {}).get("role")
        content = (msg.get("message") or {}).get("content")

        if msg_type == "user" and role == "user":
            text = extract_user_text(content)
            if text:
                if first_user_text is None:
                    first_user_text = text
                flush_tools()
                lines.append(f"**> {text}**")
                lines.append("")

        elif msg_type == "assistant" and role == "assistant" and isinstance(content, list):
            for item in content:
                if not isinstance(item, dict):
                    continue
                if item.get("type") == "text":
                    text = item.get("text", "").strip()
                    if text:
                        flush_tools()
                        lines.append(text)
                        lines.append("")
                elif item.get("type") == "tool_use":
                    summary = summarize_tool(item.get("name", "?"), item.get("input", {}))
                    tool_batch.append(summary)
                # Skip thinking blocks

    flush_tools()

    if not session_date:
        from datetime import date
        session_date = date.today().isoformat()

    body = "\n".join(lines).strip()
    topic = (first_user_text or "session")[:120]

    return session_date, topic, body


def export_session(jsonl_path: Path, repo_name: str, session_id: str) -> Path | None:
    """Export one JSONL file to a markdown transcript. Returns output path or None."""
    size_kb = jsonl_path.stat().st_size // 1024
    if size_kb < 2:
        return None

    session_date, topic, body = render_session(jsonl_path)

    if not body.strip():
        return None

    # Skip sessions with no real substance (errors, aborted, single tool call)
    # Count lines that are actual Claude text (not user prompts, tool summaries, or blanks)
    substance_lines = [
        l for l in body.split("\n")
        if l.strip()
        and not l.startswith("**>")
        and not l.startswith("  - ")
        and not l.startswith("- ")
        and not l.startswith("API Error:")
        and not l.startswith("[Request interrupted")
        and not l.startswith("No response")
        and len(l.strip()) > 20  # skip one-word filler lines
    ]
    if len(substance_lines) < 3:
        return None

    slug = slugify(topic)
    output = SESSIONS_DIR / f"{session_date}-{slug}.md"

    # Handle collisions
    if output.exists():
        counter = 2
        while (SESSIONS_DIR / f"{session_date}-{slug}-{counter}.md").exists():
            counter += 1
        output = SESSIONS_DIR / f"{session_date}-{slug}-{counter}.md"

    frontmatter = f"""---
date: {session_date}
repo: {repo_name}
session_id: {session_id}
type: session-export
---"""

    header = f"# Session: {repo_name} ({session_date})"
    topic_line = topic.split("\n")[0][:120]

    output.write_text(f"{frontmatter}\n\n{header}\n\n> {topic_line}\n\n---\n\n{body}\n")
    return output


def repo_name_from_dir(dir_name: str) -> str:
    """Derive repo name from Claude project dir name.

    Add your own repos here. The key is the escaped directory path
    (slashes replaced with hyphens), and the value is the short name
    you want to appear in session exports.

    Example:
        "-Users-jane-code-my-app": "my-app",
        "-Users-jane-code-work-os": "work-os",
    """
    # Add your repos here:
    known = {
        # "-Users-yourname-code-work-os": "work-os",
        # "-Users-yourname-code-my-project": "my-project",
    }
    if dir_name in known:
        return known[dir_name]
    # Fallback: strip prefix, take last segment
    name = re.sub(r"^-Users-\w+-code-", "", dir_name)
    # Don't split on hyphens — they're part of repo names
    return name or dir_name


def export_project_dir(project_dir: Path, exported_ids: set[str], reexport: bool = False):
    repo = repo_name_from_dir(project_dir.name)
    for jsonl_file in sorted(project_dir.glob("*.jsonl")):
        sid = jsonl_file.stem
        if not reexport and sid in exported_ids:
            continue
        result = export_session(jsonl_file, repo, sid)
        if result:
            print(f"Exported: {result.name}")


def main():
    args = sys.argv[1:]
    reexport = "--reexport" in args
    args = [a for a in args if a != "--reexport"]

    # Hook mode
    if "--hook" in args:
        hook_input = json.loads(sys.stdin.read())
        sid = hook_input.get("session_id", "")
        transcript = hook_input.get("transcript_path", "")
        cwd = hook_input.get("cwd", "")
        if not sid or not transcript or not Path(transcript).is_file():
            return
        repo = Path(cwd).name if cwd else "unknown"
        export_session(Path(transcript), repo, sid)
        return

    exported_ids = set() if reexport else get_exported_ids()

    if args:
        # Single repo mode
        repo_path = Path(args[0]).resolve()
        escaped = str(repo_path).replace("/", "-")
        project_dir = CLAUDE_DIR / escaped
        if project_dir.is_dir():
            export_project_dir(project_dir, exported_ids, reexport)
    else:
        # All repos
        for project_dir in sorted(CLAUDE_DIR.iterdir()):
            if project_dir.is_dir() and not project_dir.name.startswith("."):
                export_project_dir(project_dir, exported_ids, reexport)


if __name__ == "__main__":
    main()
