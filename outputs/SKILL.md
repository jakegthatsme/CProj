---
name: execution-plan-writing
description: >
  Write per-document execution plans for the fifth-pass constitutional project.
  Fire when writing, revising, or reviewing any execution plan for a fifth-pass
  document; when the fifth-pass planning document specifies a per-document
  plan placeholder that needs to be turned into a self-contained drafting
  prompt; or on any request like "write the execution plan for Document X,"
  "produce the prompt for the next document," or equivalent. Loaded as a
  dependency by fifth-pass-planning. Can also be loaded standalone to write or
  rewrite a single plan without re-firing the full planning context.
---

# Execution-Plan Writing

Write self-contained execution plans, one per document, that a downstream
drafting session can consume without external dependencies. Each plan invokes
the skills it needs by name. No standing-context block. No word counts.
Thoroughness is the standard.

## Always View First

1. /mnt/skills/user/usage-efficiency/SKILL.md
2. /mnt/skills/user/scholarship-mode/SKILL.md
3. /mnt/skills/user/completeness-not-length/SKILL.md

If `fifth-pass-planning` has already fired in this session, do not re-view
the skills it has already loaded.

**Before drafting any plan, also:**

1. Check whether a stub for the document already exists in
   `outputs/Execution_Plan_Document_<id>.md` (via `project_knowledge_search`
   or, in Claude Code sessions, by listing `outputs/`). The four claude.ai-
   reserved documents (M, W, R, D-Synthesis) have canonical Sections 1–2
   pre-filled in their stubs; the authoring work is to write Sections 3–10
   under those canonical openers.
2. Pull the document's specification from `project/Fifth_Pass_Planning_Document.md`
   — specifically the Section II line naming the document and the Section I
   Part description. If the planning document is not in context, search
   project knowledge or ask the user to paste the relevant sections rather
   than guessing at the substantive task.
3. Pull `CLAUDE.md` from the repo for current preserved-with-edits status,
   phase-order placement, and reference-file conventions.

## Core Rules

**One plan per document, one file per plan.** Each execution plan is its own
markdown file in `/mnt/user-data/outputs/`. Filename:
`Execution_Plan_Document_<id>.md` where `<id>` is the document's fifth-pass
designation.

**Self-contained.** The plan must be consumable by a session that has not
seen the planning document or any prior conversation. It states the
load-bearing commitment in one paragraph; it names the skills the drafting
session must load; it specifies the substantive content commitments; it
specifies sources, citation conventions, and structural requirements; it
specifies the output path. Nothing more.

**Skill dependencies declared, not duplicated.** Each plan opens with a
"Skills to Load" section listing the skills the drafting session must view
before drafting. The plan does not restate the contents of those skills.
The drafting session is responsible for loading them.

**No word counts. No page counts. No output metrics.** Thoroughness is the
standard. Each analytical commitment must be engaged, not gestured at.
`completeness-not-length` governs.

**Substantive specification, not procedural.** The plan specifies what the
document must engage analytically — named scholars, named works, named
traditions, named threads, named primary sources, named cross-references to
other documents in the arc. It does not specify how many paragraphs,
sections, or pages.

**Load-bearing triad stated once, at the top.** The canonical triad block
is stated verbatim in Section 2 of each plan as the project's load-bearing
framing. The plan does not re-argue it; the drafting session applies it.

## Plan Structure

Every plan contains the following sections in order. Sections that have no
content for a particular document are omitted, not retained as empty headers.

### 1. Document Identification

Document designation, Part placement, target output path, status (preserved-
with-edits, re-specified, or new).

### 2. Load-Bearing Triad

Two paragraphs. The first is the canonical triad block, reproduced verbatim
across every plan so the drafting session encounters the same load-bearing
framing in the same words:

> The fifth-pass project's load-bearing triad: **biocultural governance** as
> constitutional ontology, **eco-mimetic policy-making** as operational
> method, **disturbance-adapted implementation** as temporal orientation.
> Indigenous and Eastern traditions are primary articulators; the Western
> CAS, ecology, biomimicry, and disturbance-ecology canons are recent and
> partial recovery. Five disturbance regimes are tracked across the arc:
> cultural, biological, physical-environmental, cognitive-and-informational,
> political-economic. "Grown, not built" is colloquial summary.

The second paragraph (one to three sentences) names how this document
applies the triad — which element it operationalizes, which disturbance
regime(s) it foregrounds, and the primary-articulator traditions whose
work the document carries at primary-articulator standing rather than as
comparative supplement.

### 3. Skills to Load

A short list of skills the drafting session must view before drafting,
each with a one-line note on why it is needed. The default set, per
CLAUDE.md, is:

- `scholarship-mode` — register, citation discipline, no bullets in
  analytical sections
- `completeness-not-length` — evaluate the draft by whether commitments
  were met, not by length
- `direct-to-output-drafting` — write the v5 document directly to its
  output file rather than drafting in segments and concatenating
- `usage-efficiency` — move-don't-regenerate discipline for preserved-
  with-edits substrate

Add document-specific skills (for instance `long-research-splitting` for
documents at high risk of session timeout, or `pre-drafting-consultation`
for documents whose substantive task is exceptionally consequential)
only where the document warrants them.

### 4. Substantive Task

Prose paragraph specifying the document's substantive analytical task under
the fifth-pass framing. What the document does, what it does not do, what
it assumes from other documents in the arc, what it provides for downstream
documents.

### 5. Required Threads

Each thread the document must engage, named with its scholars, works, and
the substantive analytical commitment. Threads are paragraphs of prose, not
bullets. Each thread states what the document must do with the thread,
not merely that the thread is present.

### 6. Source Requirements

Primary sources, secondary sources, and bibliography references the document
must engage. Indigenous and Eastern primary sources named directly. The
plan specifies which sources are load-bearing (must be engaged in depth)
and which are reference-level.

### 7. Structural Requirements

Form-level requirements: scholarly register, integrated citations, no bullets
in analytical sections, references section format. These are short pointers
to `scholarship-mode` rather than restatements of its content.

### 8. Cross-References

Other fifth-pass documents this document cites, depends on, or anticipates.
Specifies which are upstream (already drafted, cited) and which are
downstream (anticipated, pointed forward to).

### 9. Output Requirements

Output path; markdown format; references section organized by theme or
tradition; no word count target; `completeness-not-length` as the standard.

### 10. What to Avoid

Document-specific anti-patterns named concretely. The generic anti-patterns
(no bullets in analytical sections, no business-prose apparatus, no word-
count padding) are covered by the loaded skills and should not be re-
listed here. This section names risks that arise specifically from the
document's threads, traditions, and analytical task. Typical categories:

- **Synthesis-into-architecture** — collapsing multi-traditional primary
  articulators into a single architectural register. Name the specific
  collapse the document is at risk of.
- **Primary-articulator absorption** — describing Indigenous, Eastern,
  African, Islamic, Latin American, Caribbean, Pacific Islander, Jewish,
  dalit, Black-radical, disability-justice, or neurodivergent scholarship
  in Western recovery vocabulary. Name the specific traditions the
  document is most at risk of absorbing this way.
- **Design-imposition slip-back** — re-importing the founding-era design
  imposition framings the project rejects (originalism, unitary executive,
  the economy as primary system). Relevant where the document engages
  founding-era material directly.
- **Duplication of cross-cited material** — restating substance that the
  cross-referenced upstream documents already carry. Name the specific
  cross-references where duplication is the risk.
- **Gestural treatment of consequential threads** — Required Threads that
  the document is most at risk of naming without engaging. Name them.

These are categories; the plan must name the specific instances for the
document at hand.

## For Preserved-With-Edits Documents

When the plan is for a document the planning document or `CLAUDE.md` marks
as preserved-with-edits — drawing on a v4 source document at
`project/source_documents/Document_<x>.md` that is preserved in full while
the plan's targeted edits propagate the fifth-pass framing — the plan
structure shifts:

- Section 4 (Substantive Task) becomes "Targeted-Edit Task": specifies what
  edits propagate the fifth-pass framing into the preserved document.
- Section 5 (Required Threads) becomes "Required Edit Threads": each edit
  named with its insertion point, the existing text that frames it, and
  the substantive commitment the edit carries.
- Section 6 (Source Requirements) lists only new sources the edits introduce;
  existing sources in the preserved document are not re-listed.
- "Move, don't regenerate" governs throughout. Existing text is preserved
  unless the planning document specifies otherwise.

Documents 1, 2, and 3 are now drafted as Phase α v5 exemplars in
`project/source_documents/v5_completed/`; their plans are the historical
exemplars in `project/exemplar_plans/` and serve as register calibration
anchors for new plans rather than as targets for re-drafting. Current
preserved-with-edits documents are listed in `CLAUDE.md` and identified
by their plan's Status field.

## For the Four claude.ai-Reserved Stubs (M, W, R, D-Synthesis)

CLAUDE.md reserves four execution plans for claude.ai authoring rather than
Claude Code: Document M (Part III, biocultural-governance ontology),
Document W (Part II, cross-regime interactions), Document R (Part XII, eco-
mimetic policy-making method), and Document D-Synthesis (Part XIII,
cultivation-protocol synthesis). Each exists as a stub in
`outputs/Execution_Plan_Document_<id>.md` with canonical Section 1
(Document Identification) and Section 2 (Load-Bearing Triad) already
filled. The authoring work in claude.ai is to compose Sections 3 through
10 against the planning document's Section II specification and the Part
description in Section I.

Recommended authoring order per `PROJECT_COMPLETION_ROADMAP.md`: **M → W →
R → D-Synthesis**. M's biocultural-governance ontology is upstream of W,
R, and D-Synthesis. W's interactions architecture is upstream of R.
D-Synthesis integrates everything and comes last.

## What to Avoid

- Restating the load-bearing triad in every section. Once at the top.
- Embedding the standing context block from the fourth-pass workflow. The
  skill replaces it.
- Specifying word counts, page counts, section counts, or paragraph counts.
- Restating the contents of loaded skills. The drafting session loads them;
  the plan invokes them by name.
- Duplicating substance across plans. Each plan carries only its document's
  substance plus the minimum framing.
- Procedural over-specification. The plan tells the drafting session what
  analytical work to do, not how many tool calls to make.
