# Frameworks & Mental Models

Reusable thinking tools for prioritization, architecture, and decision-making.

## Theory of Constraints (TOC)

The dominant lens for prioritization. Everything starts with identifying the constraint.

1. **IDENTIFY** the system's constraint
2. **EXPLOIT** the constraint (maximize efficiency without major investment)
3. **SUBORDINATE** everything to the constraint (align other processes)
4. **ELEVATE** the constraint (only after steps 2-3 are exhausted)
5. **REPEAT** — find the next constraint

Watch for hidden constraints: "work to do work" — context switching, tool fragmentation, interruptions. Sometimes the real constraint isn't the task itself but the friction around it.

## OODA Loop

Boyd's cycle for fast decision-making under uncertainty. The advantage goes to whoever cycles faster.

1. **OBSERVE** — Gather raw information. What's actually happening? (Metrics, user feedback, ops complaints, system data.)
2. **ORIENT** — Make sense of it. Apply mental models, past experience, and context to form a picture. This is the hardest and most important step — bad orientation means everything downstream is wrong.
3. **DECIDE** — Pick a course of action. Commit, don't deliberate forever.
4. **ACT** — Execute. Then immediately observe the result and loop again.

**Why it matters for product work**: The team that ships a rough solution, observes how it performs, reorients, and iterates will beat the team that spends months perfecting a spec. Especially true for AI agents where you can't predict failure modes from a desk — you have to observe them in production.

**The trap**: Skipping Orient and jumping from Observe to Act. "We got bad feedback, ship a fix." Without orientation (why is this happening? what's the underlying pattern?), you're just reacting.

## Wide and Deep

Build foundational capabilities broadly first, then go deep on one use case before expanding. The goal is finding the **global maximum**, not getting stuck on a local one.

**The pattern**: Lay a wide foundation → pick the highest-leverage vertical → go deep → prove value → expand to the next vertical. Each deep pass validates the foundation and reveals what's missing before you scale.

**Why it matters**: Going narrow-and-deep first locks you into local optima — you build something perfectly tuned to one case that can't generalize. Going wide-and-shallow builds infrastructure nobody uses. Wide-then-deep finds the global maximum because the broad foundation forces you to think about the general case before optimizing.

**How to spot local maxima**: You're stuck in one when adding more effort yields diminishing returns but the broader system isn't improving. The fix isn't working harder on the current thing — it's stepping back to the wide view and picking a different vertical.

**Examples**:
- **Platform design**: Build the common data model and API layer (wide), then go deep on the most painful workflow. What you learn reshapes the platform before you've committed to a rigid architecture.
- **Process improvement**: Map the full end-to-end process (wide), then fix the biggest bottleneck (deep). Don't optimize step 3 before understanding how steps 1-7 connect.
- **Learning a domain**: Survey the whole landscape first (wide), then drill into the area with the most leverage (deep). Prevents over-indexing on the first interesting thing you find.

**Contrast**:
- "Narrow and deep" — can't generalize, paints you into a corner
- "Wide and shallow" — infrastructure nobody uses, no proof of value
- "Wide and deep" — general foundation + proven depth = the position you want

## Phased Rollout with Stage Gates

Don't ship everything at once. Move through phases, and don't advance until you've earned it.

1. **Shadow / Backtest** — Run in parallel with no production impact. Compare your output to the current baseline (human or system). **Use when**: you don't yet know if the thing works. **Exit when**: performance meets or exceeds baseline on a meaningful sample.

2. **Human-in-the-Loop** — New system generates output, humans review 100%. **Use when**: you trust the output enough to show it to people but not enough to act on it. **Exit when**: review patterns stabilize — humans are mostly approving, and the edits they make are predictable.

3. **Selective Automation** — High-confidence outputs skip human review. Low-confidence still gets reviewed. Sampling-based QC on the automated ones. **Use when**: you can reliably score confidence and the cost of a mistake is recoverable. **Exit when**: error rate on automated outputs is within tolerance for a sustained period.

4. **Full Automation** — System runs autonomously. Humans handle exceptions only. **Use when**: the previous phase has been stable long enough that you trust the tail cases.

**Define exit criteria before you start each phase, not after.** If you can't articulate what "good enough to advance" looks like, you're not ready to start.

**Common mistakes**:
- Skipping Shadow and going straight to Human-in-the-Loop because "we need to move fast." You'll discover failure modes in production that you could have caught cheaply.
- Staying in Human-in-the-Loop forever because nobody wants to own the decision to automate. Set a review date.
- Not doing sampling-based QC in Phase 3. The whole point of selective automation is that you're still checking — just not checking everything.

## Anti-Patterns

Recurring traps. Each one sounds obvious in isolation but is surprisingly tempting in practice.

- **Local optimization at expense of global** — Speeding up one step while the overall system stays slow (or gets worse). **When you'll be tempted**: a team is excited about a measurable improvement to their piece. **The fix**: always ask "does this improve end-to-end throughput?" before celebrating.

- **Framework theater** — Dashboards, metrics, and processes that exist to feel productive rather than to drive decisions. **When you'll be tempted**: after a crisis, when the instinct is "we need more visibility." **The fix**: for every metric, name the decision it informs. If you can't, kill it.

- **Solving the wrong layer** — Building sophisticated solutions to problems that don't exist yet, or building infrastructure when the real issue is process. **When you'll be tempted**: when the technical solution is more interesting than the human one. **The fix**: ask "what's the cheapest thing we could do to test whether this matters?"

- **Premature abstraction** — Creating frameworks, platforms, and shared services before you have enough concrete use cases to know what the abstraction should look like. **When you'll be tempted**: after the second use case, when the pattern "feels obvious." **The fix**: wait for the third use case. Two points make a line, three points confirm direction.

- **Consensus as cover** — Seeking broad alignment not because you need input but because you want shared blame if it fails. **When you'll be tempted**: high-stakes decisions where you already know the right answer. **The fix**: make the call, document your reasoning, move on. You can course-correct faster than you can align.

## Practical Patterns

Recurring patterns from writing specs, research, and working with engineering.

### Spec Writing

- **Start from user pain, not system architecture.** Every strong spec opens with the problem from the user's perspective, then builds to the solution.
- **"Day in the life" narratives** work better than abstract feature descriptions. Walk through a real scenario.
- **Two-user-table format** for multi-persona products. Table with Role, Who, What They Care About. Forces you to think about each audience explicitly.
- **JTBD for requirements**: When a new manager inherits 40 open jobs →
  I want one prioritized view of what to fix first → So that I can take
  action without reading 5 reports. Keeps features tied to real needs.
- **Explicit non-goals** prevent scope creep. State what you're NOT building. Stakeholders will assume everything is in scope unless you say otherwise.
- **Always include open questions.** Signals what you don't know yet and invites the right conversations before engineering starts.
- **Mermaid diagrams for workflows and state machines.** State transitions are hard to describe in prose. A diagram communicates the system in seconds.
- **Use real examples.** Real numbers, real scenarios. Concrete is actionable. Abstract is not.

### Research

- **Lead with the recommendation**, then back it up with evidence. Decision-makers want the bottom line first.
- **Options tables** (option, pros, cons, effort) make it easy to compare. Every research doc should have one.
- **Quantify when possible.** "$50K/year" and "49% completion rate" are actionable. "It costs a lot" is not.
- **Search before writing anything.** Don't duplicate research that already exists.

### Version Control

- **Version docs with suffixes (-v1, -v2)**, not git branches. Keeps evolution visible in the directory listing. Git tracks fine-grained changes within each version.
- **Commit often with descriptive messages.** Future you wants to see "Add phased rollout to spec" not "update docs."

### Eng Handoff

- **Specs need to be specific enough that eng doesn't guess intent.** Include file paths, constant names, exact behavior.
- **Technical considerations should be practical, not theoretical.** What files to modify, what tests to add, what edge cases to watch for.
- **Check for unresolved open questions before handoff.** If there are open questions, the spec isn't ready.
