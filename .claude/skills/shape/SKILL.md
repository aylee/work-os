---
name: shape
description: Understand a request before acting on it. Surfaces the problem, intent, context, and expected output. Use before plan mode or complex tasks.
disable-model-invocation: true
---

Understand a request before building anything. This is a PM doing requirements gathering — interrogating the what, why, context, and expected output so that downstream plans or execution address the real goals, not Claude's interpretation of them.

## Usage

```
/shape should we add a plan-reviewer agent?
/shape redesign the archive workflow
/shape offer escalation notifications
```

## Workflow

### Step 1: Understand What's Being Asked

Don't start solving. Start by asking:
- **What's the problem?** What's broken, missing, or not working? Be specific.
- **What's the intent?** Why does this matter? What outcome are you after?
- **What does done look like?** What artifact or result do you expect? (A file? A decision? A shipped feature? A Notion update?)

If the user gave a clear brief, don't re-ask what's already stated. Fill in the gaps only.

### Step 2: Gather Context

Based on what the user said, pull relevant existing context:
- If it's a project topic -> read `desk/{project}/BINDER.md` for where things stand
- If there's prior work -> search `desk/` and `memory/decisions/` for related docs
- If it relates to a work area -> read `areas/work/AREA.md` for strategy context
- If `.claude/notion.yaml` is configured and existing Notion work might exist -> `notion-search`

Don't exhaustively search everything. Pull what's relevant to the specific request.

### Step 3: Play Back Understanding

Present a brief-back — your understanding of the request, stated plainly:

```markdown
## Shape: {topic}

### Problem
What's actually wrong or missing. One paragraph, concrete.

### Intent
What the user is trying to achieve and why it matters now.

### Context
What already exists that's relevant — prior work, decisions, active binder state. Cite file paths.

### Expected Output
What "done" looks like — the specific artifact, change, or result.

### Scope
- **Includes:** ...
- **Does not include:** ...

### Assumptions & Open Questions
Things I'm treating as true but haven't confirmed:
- [ ] Assumption or question 1
- [ ] Assumption or question 2
```

This is a playback, not an essay. Keep each section to 1-3 sentences. The user should be able to scan it in 15 seconds and say "yes, that's right" or "no, you're missing X."

### Step 4: Get Confirmation

Ask the user: "Is this right? Anything I'm missing or getting wrong?"

Don't proceed until the framing is confirmed. This is the whole point — catch misalignment before it compounds.

### Step 5: Suggest Next Step

Based on the confirmed framing:
- Clear building task -> "Ready for plan mode" or "Small enough to just do"
- Open questions blocking -> "Resolve these first: ..."
- Needs research -> suggest `/research`
- Needs a decision -> suggest `/decision`
- Needs a doc (spec, brief, RFC) -> suggest the matching skill

## What `/shape` is NOT

- Not a plan. No implementation steps, file paths, or how-to.
- Not a spec. No FRs or acceptance criteria.
- Not a framework exercise. Frameworks from `library/reference/frameworks.md` may inform thinking but the output is a brief-back, not an analysis.
- Not saved to a file by default. It's a conversation artifact. Save only if the user asks.

## Tools Used

- Read, Glob, Grep (local file search)
- Notion MCP: `notion-search` (existing work — only if `.claude/notion.yaml` is configured)
