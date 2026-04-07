# Maintainer Hygiene

Public demo content in work-os should stay polished, fictional, and
free of setup residue.

This guide covers the audit side of maintenance. For the canonical
maintainer workflow, upstream-sync runbook, and publish checklist, start
with `library/guides/maintainer-workflow.md`.

## Run the audit

From the repo root:

```bash
python3 library/scripts/audit_public_hygiene.py
```

The script exits non-zero when it finds public-hygiene problems.

## What it checks

### Placeholder leakage

The audit scans tracked files plus non-ignored untracked files for
common setup scaffolding markers: generic name and company placeholders,
dummy email links, org-slug placeholders, and starter workspace URLs.

Those markers are allowed only in files that are intentionally generic
starter material.

### Demo structure

The audit also checks two coarse repo-level guardrails:

- `areas/work/AREA.md` must explicitly describe the shipped company or
  workspace as fictional.
- Any project directory under `desk/` that contains markdown files must
  include a `BINDER.md` manifest.

These checks are intentionally simple. They are there to catch obvious
drift early, not to create release bureaucracy.

## Intentional generic files

Keep the allowlist small and reviewable. Today it includes only:

- `.claude/notion.yaml.example`
- `.claude/skills/setup/SKILL.md`
- `library/reference/me.md`
- `library/templates/`

Everything else in the shipped repo should read like finished public
starter content, not like incomplete setup.

## When to run it

Run the audit before:

- merging changes to `README.md`, `docs/`, `.claude/`, or `library/`
  that affect onboarding or setup
- changing shipped demo content under `areas/`, `desk/`, or `memory/`
- cutting a public release or tagging a starter refresh

## Demo-content guardrail

When you update the shipped example workspace, keep one coherent
fictional story across:

- `areas/work/AREA.md`
- `areas/work/plans.md`
- active and archived binders in `desk/`
- shipped example decisions or reviews in `memory/`

If you change the demo company, roles, or current projects, update the
area file and the affected binders in the same pass so the starter still
reads like one workspace.

## Updating the allowlist

Treat allowlist changes as public-contract changes.

Only add a file if it is genuinely meant to stay generic in every fresh
clone, such as:

- reusable templates
- setup-owned starter reference files
- setup documentation that must show starter scaffolding literally

When that happens:

1. Update `ALLOWLIST_PATHS` or `ALLOWLIST_PREFIXES` in
   `library/scripts/audit_public_hygiene.py`.
2. Update this guide in the same commit.
3. Keep the new entry as narrow as possible. Prefer a single file path
   over a broad directory prefix.
