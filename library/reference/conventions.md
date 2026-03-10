# Conventions

File naming, frontmatter, and lifecycle rules for work-os artifacts.

## File Naming

`{project}-{descriptor}.md` in kebab-case. Project prefix groups related files.

- Include doc type suffix when ambiguous: `onboarding-overhaul-spec.md`
- Skip when clear: `platform-vision-v2.md`

## Frontmatter

Every work artifact gets YAML frontmatter:

```yaml
---
status: draft | active | shipped | archived
type: spec | brief | rfc | research | decision | eval-framework | launch-plan | implementation-plan | strategy | log | analysis | area
---
```

## Binder Naming

Everything on the desk is a binder. `ls desk/` = list of projects.

- **Org prefix** for work project binders (e.g., `acme-billing/`, `acme-onboarding/`). Pick a short prefix for your company or team and use it consistently.
- **No prefix** for personal or meta projects (e.g., `bookkeeping/`, `side-project/`)

## Binder Lifecycle

Active → ship outputs → archive the binder.

| Status | Where | Meaning |
|--------|-------|---------|
| `active` | `desk/` | Actively working on it |
| `parked` | `desk/` | On hold, will return |
| `shipped` | `desk/` | Outputs delivered, archive candidate |
| `archived` | `desk/z_archive/` | Done — whole binder moved intact |

**When work ships, possible destinations:**
1. **Publish to Notion** — artifact becomes a Notion page
2. **Publish to shared docs** — artifact becomes a Google Doc, Confluence page, etc. for sharing
3. **Move to library/** — evergreen reference material gets promoted
4. **Archive** — whole binder moves to `desk/z_archive/`

These combine. A spec might publish to Notion, an eval framework promotes to library/, then the whole binder archives.

**Binders are intact units.** While active, nothing leaves the binder. Shipped specs inside an active binder stay — they're project context. When the binder is done, it moves whole.

## Binder File Creation

When `/spec`, `/brief`, `/rfc`, etc. target a project that has an active binder, create the file inside that binder directory. Check `desk/{project}/BINDER.md` before creating a new binder.
