# CLAUDE.md — CProj Execution-Plan Authoring

This repository contains the fifth-pass constitutional project. The current
task is to author **twenty-eight execution plans** for the project's
remaining documents, with three additional **plan stubs** (M, W, R) reserved
for separate authoring in claude.ai.

This file is read at the start of every Claude Code session in this repo.
The rules below override Claude Code defaults where they conflict.

---

## Project Context

The fifth-pass architecture is specified in `project/Fifth_Pass_Planning_Document.md`.
The load-bearing triad: **biocultural governance** as constitutional ontology,
**eco-mimetic policy-making** as operational method, **disturbance-adapted
implementation** as temporal orientation. Indigenous and Eastern traditions
are primary articulators; the Western CAS, ecology, biomimicry, and
disturbance-ecology canons are recent and partial recovery. Five disturbance
regimes: cultural, biological, physical-environmental, cognitive-and-
informational, political-economic. "Grown, not built" is colloquial summary.

The arc contains thirty-seven documents across fourteen Parts. The Phase α
plans (Documents 1, 2, 3) have been written and are stored at
`project/exemplar_plans/`. These three plans are **calibration anchors** —
the canonical reference for register, length, structure, and analytical depth
of every plan you write.

---

## Your Task

Author execution plans in **strict phase order** for the documents listed in
the work queue below. Each plan goes to `outputs/Execution_Plan_Document_<id>.md`.

### Work Queue (Phase Order — Do Not Reorder)

**Phase β** — 5 plans: A, 4, B, C, I
**Phase γ** — 2 plans: K, L *(Document M is a STUB — see below)*
**Phase δ** — 4 plans: N, O, P, Q
**Phase ε** — 8 plans: S, T, U, V, 7, 8, 9, 10 *(Document W is a STUB)*
**Phase ζ** — 4 plans: E, F, H, J
**Phase η** — 4 plans: D-1, D-2, D-3, D-4 *(Document R is a STUB)*
**Phase ι** — 1 plan: G

**Total: 28 full plans + 3 stubs = 31 deliverables.**

### Stub Treatment for M, W, R

Documents M (biocultural-governance ontology), W (disturbance-regime
interactions), and R (eco-mimetic policy-making) will be authored separately
in claude.ai. Write a stub file for each at the phase-appropriate moment
(M during Phase γ, W during Phase ε, R during Phase η). A stub contains:

- Section 1 (Document Identification) — fully filled out per planning document.
- Section 2 (Load-Bearing Triad) — fully filled out, same text as full plans.
- Every other section header present, with content replaced by:
  `> **TODO** — This plan to be authored separately in claude.ai. See planning document Section II for substantive specification.`
- A top-of-file note: `> **STUB** — Reserved for claude.ai authoring; do not draft from this stub.`

---

## Plan Structure (All Plans, Every Phase)

Every plan contains these ten sections in order. Sections that have no
content are omitted, not retained as empty headers.

1. **Document Identification** — designation, Part placement, output path, status.
2. **Load-Bearing Triad** — biocultural governance / eco-mimetic policy-making / disturbance-adapted implementation; one short section; same canonical text in every plan (see "Canonical Triad Block" below).
3. **Skills to Load** — short list with one-line notes per skill.
4. **Substantive Task** *(or "Targeted-Edit Task" for preserved-with-edits)* — prose paragraph.
5. **Required Threads** *(or "Required Edit Threads")* — each thread named with scholars, works, analytical commitment.
6. **Source Requirements** — primary, secondary, bibliography references.
7. **Structural Requirements** — scholarly register, citations, no bullets in analytical sections.
8. **Cross-References** — upstream and downstream documents in the arc.
9. **Output Requirements** — output path, format, `completeness-not-length` standard.
10. **What to Avoid** — document-specific anti-patterns only.

### Canonical Triad Block

Use this exact text for Section 2 in every full plan and every stub:

```
The fifth-pass project rests on a load-bearing triad: **biocultural
governance** as constitutional ontology (the polity is a complex adaptive
system cultivated across nested spatial and temporal scales as a biocultural
formation, with biological substrate and cultural plurality coupled, grounded
in the biocultural-diversity and biocultural-rights literatures); **eco-
mimetic policy-making** as operational method (ecology, CAS theory,
biomimicry, and disturbance-ecology concepts inspire how laws are passed,
written, and tested); **disturbance-adapted implementation** as temporal
orientation (intergenerational architecture cultivated to absorb a plural
disturbance landscape comprising five named regimes — cultural, biological,
physical-environmental, cognitive-and-informational, political-economic —
and their interactions). The Indigenous and Eastern traditions are the
principle's primary articulators; the Western complex-adaptive-systems,
ecology, biomimicry, and disturbance-ecology canons are recent and partial
recovery. "Grown, not built" is usable as colloquial summary phrase.
```

After the canonical block, add one to three sentences specific to the
document at hand stating how the triad bears on its task.

---

## Core Authoring Rules

- **One plan per file.** Filename: `Execution_Plan_Document_<id>.md`.
- **Self-contained.** Each plan is consumable by a session that has not seen
  the planning document. Substantive specifications go in the plan, not as
  external references.
- **No word counts. No page counts. No output metrics.** Thoroughness is the
  standard. `completeness-not-length` governs.
- **Substantive, not procedural.** Name scholars, works, traditions, threads,
  primary sources, cross-references. Do not specify paragraphs, sections,
  or page lengths.
- **Scholarly register.** Plans are written in scholarly prose. No bullets
  in analytical sections of the plan. The "Skills to Load" and the document
  identification metadata can be brief; the substantive sections are prose.
- **Move-don't-regenerate** governs all preserved-with-edits plans. For
  re-specified plans, draw on the existing source files in `project/` as
  substrate without duplicating their substance into the plan.
- **Mirror the Phase α exemplars in register, length, and structural depth.**
  When in doubt about how much detail to include, re-read the corresponding
  thread treatment in Plan 1, 2, or 3.

---

## Drift-Check Protocol (Critical)

You will pause after **every single plan** to checkpoint with the user. The
checkpoint is non-negotiable. After writing each plan file, you must:

1. **Re-read the three Phase α exemplar plans at the start of each new Phase**
   (β, γ, δ, ε, ζ, η, ι) before writing the first plan of that phase. State
   at the top of your post-write checkpoint message that you have done this
   when transitioning between phases.

2. **Self-audit each plan against this checklist:**
   - Does Section 2 contain the canonical triad block verbatim?
   - Does Section 2 include one to three sentences of document-specific application?
   - Are all ten sections present (or properly omitted, not empty)?
   - Are scholars and works named specifically rather than gestured at?
   - Is the register consistent with the Phase α exemplars?
   - Are cross-references concrete (e.g., "Document M, Part III") not vague?
   - Is the plan free of word counts and procedural specifications?
   - For preserved-with-edits: does the plan say "Targeted-Edit Task" and "Required Edit Threads" in Sections 4 and 5?

3. **Report to the user with this format:**
   ```
   ## Checkpoint — Plan <id> ([Phase letter])

   File written: outputs/Execution_Plan_Document_<id>.md
   Word approx: <rough number, just for sense of scale, not a target>

   Self-audit:
   - [✓ or ✗] Canonical triad block present
   - [✓ or ✗] Document-specific triad application (1-3 sentences)
   - [✓ or ✗] All ten sections present
   - [✓ or ✗] Scholars and works named specifically
   - [✓ or ✗] Register matches Phase α exemplars
   - [✓ or ✗] Cross-references concrete
   - [✓ or ✗] No word counts / procedural specs
   - [✓ or ✗] Section 4/5 naming correct for plan type

   Drift indicators: <any concerns about drift from Phase α calibration>
   Ambiguities encountered: <any places where planning document was unclear>

   Next plan: <id>
   Proceed? (waiting for user confirmation)
   ```

4. **Wait for user confirmation before writing the next plan.** Do not
   batch-write. Do not proceed on your own initiative. The user reviews
   each plan and either says "proceed" or gives correction.

5. **At phase transitions** (e.g., last plan of Phase β to first plan of
   Phase γ), prepend the checkpoint with:
   ```
   ## Phase Transition — entering Phase <letter>

   Re-reading Phase α exemplars (Plans 1, 2, 3) for calibration anchor...
   [confirm re-read complete]
   ```

---

## Ambiguity Handling

If the planning document does not unambiguously specify what a plan should
contain for a given document — for instance, a document where the planning
document only sketches the substantive task in a single sentence, or where
multiple readings of the planning document would yield different plans —
**stop and ask the user immediately**. Do not guess. Do not pick the most
likely interpretation. The user has chosen explicit ambiguity escalation as
the policy.

The escalation format:

```
## Ambiguity — Plan <id>

Planning document specification: <quote the relevant section>

Possible readings:
1. <reading A and what plan it would produce>
2. <reading B and what plan it would produce>

My recommendation: <which reading and why, briefly>

Awaiting your resolution before writing this plan.
```

Wait for user response. Do not write the plan until resolved.

---

## File-Write Conventions

- All plans go to `outputs/Execution_Plan_Document_<id>.md`.
- Use `<id>` exactly as the planning document specifies: numeric (4, 7, 8, 9, 10), single-letter (A, B, C, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W), or compound (D-1, D-2, D-3, D-4, D-Synthesis).
- Markdown format. No front-matter.
- Title line: `# Execution Plan — Document <id>: *<Title>*`

---

## What to Avoid

- Drafting two plans in one response without checkpoint.
- Treating the work queue as suggestions rather than strict order.
- Filling Section 2 with paraphrased triad text rather than the canonical block.
- Specifying paragraph counts, page counts, or section depths.
- Re-arguing the load-bearing triad (state it once, apply it).
- Inventing scholars, works, or traditions not in the planning document or the bibliography.
- Inferring intent on ambiguous planning-document passages instead of escalating.
- Continuing past a checkpoint without user confirmation.

---

## Reference Files in This Repo

- `project/Fifth_Pass_Planning_Document.md` — single source of truth for the architecture.
- `project/bibliography_consolidated_v4.md` — bibliography v4 (v5 not yet written).
- `project/exemplar_plans/Execution_Plan_Document_1.md` — Phase α exemplar.
- `project/exemplar_plans/Execution_Plan_Document_2.md` — Phase α exemplar.
- `project/exemplar_plans/Execution_Plan_Document_3.md` — Phase α exemplar.
- `project/<document source files>` — the fourth-pass drafted documents and holding files referenced as source material in re-specified plans.

---

## Session Start Protocol

At the start of every session:

1. Read this CLAUDE.md.
2. Read `project/Fifth_Pass_Planning_Document.md` Section II (document arc).
3. Read the three Phase α exemplar plans in `project/exemplar_plans/`.
4. List the current state of `outputs/` to see which plans are already written.
5. Identify the next plan in the work queue.
6. Ask the user: "Ready to write Plan <id> ([Phase letter]). Proceed?"

Wait for confirmation before writing.
