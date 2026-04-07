#!/usr/bin/env python3
"""Audit public demo hygiene for work-os."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[2]

ALLOWLIST_PATHS = {
    ".claude/notion.yaml.example",
    ".claude/skills/setup/SKILL.md",
    "library/reference/me.md",
}

ALLOWLIST_PREFIXES = (
    "library/templates/",
)

PLACEHOLDER_PATTERNS = (
    ("generic all-caps name placeholder", re.compile(r"\[YOUR" + r" NAME\]")),
    ("generic title-case name placeholder", re.compile(r"\[Your" + r" Name\]")),
    ("generic company placeholder", re.compile(r"\[Your" + r" Company\]")),
    ("generic role placeholder", re.compile(r"\[Your" + r" role[^\]]*\]")),
    ("generic describe placeholder", re.compile(r"\[Describe" + r" [^\]]+\]")),
    ("generic user token", re.compile(r"\{USER" + r"_NAME\}")),
    ("generic company token", re.compile(r"\{COMP" + r"ANY\}")),
    ("dummy email placeholder", re.compile(r"your@" + r"email\.com")),
    ("dummy mailto placeholder", re.compile(r"mailto:" + r"email")),
    ("dummy org slug placeholder", re.compile(r"\byour-" + r"org\b")),
    (
        "Notion workspace placeholder",
        re.compile(r"https://www\.notion\.so/your-" + r"workspace/"),
    ),
)


def main() -> int:
    placeholder_issues = check_placeholder_leakage()
    structure_issues = check_demo_structure()

    if not placeholder_issues and not structure_issues:
        print("Public hygiene audit passed.")
        print(
            "Checked placeholder leakage, demo binder structure, and the "
            "fictional-demo marker."
        )
        return 0

    print("Public hygiene audit failed.")

    if placeholder_issues:
        print("\nPlaceholder leakage:")
        for issue in placeholder_issues:
            print(f"- {issue}")

    if structure_issues:
        print("\nDemo structure:")
        for issue in structure_issues:
            print(f"- {issue}")

    return 1


def check_placeholder_leakage() -> list[str]:
    issues: list[str] = []

    for rel_path in iter_candidate_paths():
        if is_allowlisted(rel_path):
            continue

        text = read_text(REPO_ROOT / rel_path)
        if text is None:
            continue

        for label, pattern in PLACEHOLDER_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                issues.append(f"{rel_path}:{line_no} contains {label}")

    return issues


def check_demo_structure() -> list[str]:
    issues: list[str] = []

    area_path = REPO_ROOT / "areas/work/AREA.md"
    area_text = read_text(area_path)
    if area_text is None:
        issues.append("areas/work/AREA.md is missing or unreadable")
    elif "fictional" not in area_text.lower():
        issues.append(
            "areas/work/AREA.md must explicitly say the shipped company/workspace "
            "is fictional"
        )

    desk_root = REPO_ROOT / "desk"
    if not desk_root.exists():
        issues.append("desk/ is missing")
        return issues

    for directory in sorted(path for path in desk_root.rglob("*") if path.is_dir()):
        markdown_files = sorted(
            child.name for child in directory.iterdir() if child.is_file() and child.suffix == ".md"
        )
        if not markdown_files:
            continue
        if "BINDER.md" not in markdown_files:
            rel_dir = directory.relative_to(REPO_ROOT).as_posix()
            issues.append(f"{rel_dir} has markdown files but no BINDER.md")

    return issues


def iter_candidate_paths() -> list[str]:
    git_paths = git_ls_files()
    if git_paths is not None:
        return git_paths

    paths: list[str] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        try:
            rel_path = path.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            continue
        if rel_path.startswith(".git/") or rel_path.startswith("cc_state/"):
            continue
        paths.append(rel_path)
    return sorted(paths)


def git_ls_files() -> list[str] | None:
    try:
        proc = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None

    if proc.returncode != 0:
        return None

    return sorted(path for path in proc.stdout.splitlines() if path)


def is_allowlisted(rel_path: str) -> bool:
    if rel_path in ALLOWLIST_PATHS:
        return True
    return any(rel_path.startswith(prefix) for prefix in ALLOWLIST_PREFIXES)


def read_text(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None

    if b"\x00" in data:
        return None

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="replace")


if __name__ == "__main__":
    sys.exit(main())
