---
name: editor
description: Make an editing pass on a document. Tighten voice, fix formatting, sharpen structure, and flag issues.
disable-model-invocation: true
---

Make an editing pass on an existing document.

## Usage

```
/editor desk/my-project/project-vision.md
/editor desk/my-project/project-vision.md — focus on the "Problem" section
/editor desk/my-project/project-vision.md — tighten for external audience
```

## Workflow

### Step 1: Load Calibration Material

Before editing, read these files to calibrate:
- `library/reference/me.md` — voice principles and anti-patterns
- `library/reference/writing-guide.md` — formatting rules, section patterns, micro-formatting conventions (if it exists)
- `library/reference/voice-examples.md` — annotated sentence-level examples (if it exists)
- `library/reference/doc-examples.md` — section-level structural examples by doc type (if it exists)

These define the target. Edits should move the doc toward these patterns. If some reference files don't exist yet, work from whichever are available.

### Step 2: Read the Document

Read the target file in full. Understand:
- What type of document is it? (spec, brief, RFC, eval framework, launch plan, strategy)
- Who is the audience? (Check metadata block, headers, or frontmatter)
- What's the current state? (rough draft, mostly there, polish pass)

If the user gave a focus area (a specific section, a concern like "too long" or "tighten for external audience"), note that — it sets the priority.

### Step 3: Check Formatting Compliance

Before editing prose, check the doc against `library/reference/writing-guide.md` patterns for its doc type (if writing-guide.md exists):

**Metadata block:**
- Does it use the bold-field format (`**Owner:**`, `**Status:**`, etc.)?
- Is the status in backticks?
- Are reviewers grouped by function?

**Headers:**
- Are all headers bold inside the markdown? (`## **Section Name**` not `## Section Name`)
- Does the H1 include the doc type prefix?
- Are section names purpose-driven?

**Micro-formatting:**
- Bold + period for list leads (`- **Term.** Explanation`)
- Checkbox format for open questions (`- [ ] Question`)
- Status annotations in section headers where applicable
- FR numbering if it's a PRD/spec

Fix formatting issues first — these are mechanical and shouldn't require judgment.

### Step 4: Make the Voice Pass

Edit the document directly. This is an editing pass, not a rewrite. Preserve the author's thinking, structure, and key phrasings. Change the words, not the ideas.

**What to tighten:**
- Cut filler words and throat-clearing ("In order to," "It's important to note that," "As mentioned above")
- Shorten sentences that try to do too much — break them up or trim
- Replace vague language with specifics where you can infer the concrete version from context
- Remove repetition — if the same point is made in two consecutive paragraphs, consolidate
- Fix emdash overuse — keep the good ones, convert the rest to commas, periods, or parentheses
- Kill LLM-isms: "Let's unpack," "it's worth noting," "not X, it's Y" (as a repeated pattern)

**What to check:**
- Does the opening lead with the point? If there's a setup paragraph before the thesis, consider cutting or inverting
- Are recommendations stated directly? Flag hedged language that buries a clear opinion
- Are non-goals explicit? If the doc proposes something, consider whether it should say what it's NOT proposing
- Does the doc match its audience? Internal docs should be conversational. External docs tighten up but stay clear.
- Is the exec summary genuinely brief (2-4 sentences)? It shouldn't restate what's explained in detail later.

**What NOT to do:**
- Don't restructure the document or move sections around (unless the user specifically asked for that)
- Don't add new content, examples, or sections — this is an editing pass, not a writing session
- Don't change technical terms, proper nouns, or domain-specific language
- Don't strip out all personality — casual precision is the goal, not sterile prose
- Don't add comments, annotations, or "Editor's note" markers in the file itself

### Step 5: Summarize the Pass

After editing, provide a brief summary:
- **What changed:** 3-5 bullet points on the main edits (e.g., "Tightened the Problem section opening — cut two setup paragraphs," "Fixed all headers to use bold formatting")
- **Formatting fixes:** List any formatting compliance changes made (metadata block, headers, list formatting)
- **What I flagged but didn't change:** Anything structural or substantive that might need the author's judgment
- **Suggested next pass:** If there's more to do, say what (e.g., "Tables in the appendix could be consolidated" or "Ready to ship")

### Step 6: Commit

If `.git/` exists, commit with a message like: `edit: tighten voice and fix formatting in {filename}`

## Editing Intensity by Document State

| State | What to do |
|---|---|
| **Rough draft** | Heavy pass. Fix formatting first, then cut aggressively, restructure sentences, flag structural issues. |
| **Mostly there** | Medium pass. Check formatting compliance, tighten phrasing, cut filler, check voice consistency. |
| **Polish** | Light pass. Fix awkward phrasing, catch repeated words, ensure opening and closing are strong. |
| **External-facing** | Formality check. Tighten register, remove internal shorthand, ensure it reads well without shared context. Keep the clarity. |

## Tools Used

- Read, Edit, Grep (file operations)
