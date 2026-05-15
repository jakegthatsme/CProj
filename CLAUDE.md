# CLAUDE.md — CProj v5 Document Drafting

This repository contains the fifth-pass constitutional project. Plan authoring
is complete: thirty-two execution plans exist in `outputs/` (twenty-eight full,
four stubs: M, W, R, D-Synthesis). The current task is to **draft the v5
project documents** from those plans.

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

The arc contains thirty-seven documents across fourteen Parts. Three Phase α
v5 documents have been drafted: Documents 1, 2, 3 in
`project/source_documents/v5_completed/`. Document 6 is preserved as
historical Phase-One synthesis (`project/source_documents/Capstone_Synthesis.md`);
it is not load-bearing and is cited only where relevant by Document G. The
remaining v5 documents are to be drafted under this plan.

---

## Your Task

Draft the v5 project documents from the execution plans in `outputs/` in
strict phase order. Each plan is self-contained and supplies the substantive
task, required threads, source requirements, structural requirements, cross-
references, and what-to-avoid for the document it specifies.

### Drafting Work Queue (Phase Order — Do Not Reorder)

**Phase β** — 5 documents: A, 4, B, C, I
**Phase γ** — 2 documents: K, L *(Document M is authored in claude.ai)*
**Phase δ** — 4 documents: N, O, P, Q
**Phase ε** — 8 documents: S, T, U, V, 7, 8, 9, 10 *(Document W is authored in claude.ai)*
**Phase ζ** — 4 documents: E, F, H, J
**Phase η** — 4 documents: D-1, D-2, D-3, D-4 *(Document R is authored in claude.ai)*
**Phase θ** — Document D-Synthesis is authored in claude.ai
**Phase ι** — 1 document: G

**Total drafted in Claude Code: twenty-eight documents.** Documents M, W, R,
and D-Synthesis are drafted in claude.ai per the stub specifications in their
execution plans. Document G is drafted in Claude Code after D-Synthesis is
complete.

If a v5 document corresponding to one of the claude.ai stubs (M, W, R,
D-Synthesis) is already present at session start, treat it as substrate
available for downstream documents that cross-reference it. If absent,
proceed with the documents that do not depend on it and note the dependency.

---

## Drafting Protocol

For each document, the session proceeds as follows.

**Read the plan.** `outputs/Execution_Plan_Document_<id>.md` is the canonical
specification. It names the substantive task or targeted-edit task, the
required threads, the primary articulators, the source requirements, the
cross-references, and the constraints. The plan is self-contained; you do
not need the planning document to draft from it.

**Read the v4 source if applicable.** For preserved-with-edits documents
(per the plan's Status field), the v4 source in `project/source_documents/`
is preserved in full; the plan's targeted edits add, extend, or re-frame at
specified insertion points. For re-specified documents, the v4 source is
substrate drawn on without duplication. For new documents (no v4 source),
the plan supplies the substantive specification directly.

**Read the relocations holding files where the plan specifies coordination.**
For Documents 4, 7, 9, and L, the files in `project/relocations/` specify
section-extraction, shared-substrate, or cross-citation relocations to
Document L. The holding files name the specific sections of the v4 sources
that move and the analytical framing under which Document L absorbs them.

**Read cross-referenced v5 documents where they already exist.** Documents
later in the phase order draw on earlier-phase documents. If Document G is
being drafted last, it draws on every prior v5 document via cross-citation,
not duplication.

**Draft to the v5 output path specified in the plan.** The plan's Section 9
names the output path under `/mnt/user-data/outputs/`. In this repository
the corresponding local path is `project/source_documents/v5_completed/`.
Use the filename the plan specifies.

**Apply the move-don't-regenerate principle.** Preserve substantive v4
content in preserved-with-edits documents; do not rewrite. For re-specified
documents, draw on v4 substrate without duplicating. For relocated material,
preserve the analysis in its move; do not reproduce in the source document.

**Honor the scholarly register.** No bullets in analytical sections.
Integrated citations with dates and named works. Indigenous and Eastern
primary articulators stand at primary-articulator standing, not as
comparative supplement. The "what survives / what does not" analytical move
adapted to each document's task. `completeness-not-length` governs.

---

## Drift-Check Protocol (Per Document)

Self-audit after each document drafted, against this checklist:

- Does the document execute every Required Thread from the plan?
- Are the primary articulators each plan names engaged at primary-articulator
  standing in their own analytical registers?
- Does the document avoid synthesis-into-architecture across traditions?
- Is the move-don't-regenerate principle honored for v4 substrate?
- Are the cross-references concrete and consistent with the plan?
- Is the scholarly register consistent with the Phase α v5 exemplars in
  `project/source_documents/v5_completed/`?
- Does the document conform to the plan's What-to-Avoid section?

**Per-document checkpoint with the user.** Report after each document the
file written, the threads executed, the self-audit result, any drift
indicators or ambiguities encountered, and the next document.

**Relaxed checkpoint for preserved-with-edits propagation.** For documents
whose plan is preserved-with-edits (Targeted-Edit Task / Required Edit
Threads in Sections 4 and 5), batch up to four documents in a single
checkpoint when each is a clean propagation. For re-specified documents
(Substantive Task / Required Threads), one document per checkpoint by
default.

**Mandatory checkpoint regardless of relaxation:** the consequential
documents (M, D-Synthesis, G — and any document where ambiguity arises),
the documents drafted in claude.ai (M, W, R, D-Synthesis), and the final
Document G capstone get a per-document checkpoint without batching.

**At phase transitions** (e.g., last of Phase β to first of Phase γ),
prepend the checkpoint with `## Phase Transition — entering Phase <letter>`
and a brief re-read note confirming the Phase α v5 exemplars have been
consulted for register calibration.

---

## Ambiguity Handling

The plan is the canonical specification. If the plan unambiguously names
the substantive task, threads, sources, and cross-references, proceed.

If a plan specification is ambiguous, the source files contradict the
plan, a cross-referenced upstream document is absent, or the relocations
holding files diverge from the plan's expectations, **stop and ask the user
immediately**. Do not guess. Do not pick the most likely interpretation.
The user has chosen explicit ambiguity escalation as the policy.

The escalation format:

```
## Ambiguity — Document <id>

Plan specification: <quote the relevant section>

Conflicting condition: <quote source file, cross-reference, or holding file>

Possible readings:
1. <reading A and what document it would produce>
2. <reading B and what document it would produce>

My recommendation: <which reading and why, briefly>

Awaiting your resolution before drafting this document.
```

Wait for user response. Do not draft until resolved.

---

## File-Write Conventions

- All v5 documents go to `project/source_documents/v5_completed/`.
- Use the filename specified in each plan's Section 1 / Section 9. Where
  the plan names `/mnt/user-data/outputs/<filename>`, write to
  `project/source_documents/v5_completed/<filename>` in this repo.
- Markdown format. No front-matter.
- Title line: as specified in the plan, typically including the document
  designation in title.

---

## Skills to Load

Per each plan's Section 3, load:
- `scholarship-mode` for register and citation discipline
- `completeness-not-length` for completeness evaluation
- `direct-to-output-drafting` for writing edits directly to the output file
- `usage-efficiency` for the move-don't-regenerate discipline

---

## What to Avoid

- Drafting multiple consequential documents in one response without
  checkpoint.
- Treating the work queue as suggestions rather than strict phase order.
- Duplicating substantive material across documents where the plan specifies
  cross-citation.
- Synthesizing the multi-traditional canon into one architectural register.
- Treating Indigenous, Eastern, African, Islamic, Latin American, Caribbean,
  Pacific Islander, Jewish, dalit, Black-radical, disability-justice, or
  neurodivergent traditions as comparative supplement to a primarily-Western
  frame.
- Rewriting v4 source content in preserved-with-edits documents; the move-
  don't-regenerate principle governs.
- Inventing scholars, works, or traditions not in the plan, the planning
  document, or the bibliography.
- Inferring intent on ambiguous specifications instead of escalating.
- Continuing past a checkpoint without user confirmation.

---

## Reference Files in This Repo

- `outputs/Execution_Plan_Document_<id>.md` — the canonical specification
  for each v5 document.
- `project/Fifth_Pass_Planning_Document.md` — single source of truth for the
  architecture; not required for drafting once plans are read.
- `project/bibliography_consolidated_v4.md` — v4 bibliography (v5 additions
  specified in the planning document Section VII).
- `project/source_documents/<doc>.md` — v4 source documents used as
  preserved-with-edits or re-specified substrate per each plan.
- `project/source_documents/v5_completed/Document_One_..._v5.md`,
  `Document_Two_..._v5.md`, `Document_Three_..._v5.md` — Phase α v5
  exemplars and calibration anchors for the v5 document register.
- `project/relocations/Document_4_relocations.md`,
  `Document_7_relocations.md`, `Document_9_relocations.md` — holding files
  specifying material that relocates from Documents 4, 7, 9 to Document L.
- `project/exemplar_plans/Execution_Plan_Document_1.md` through `..._3.md` —
  Phase α plan exemplars (historical; plans are now in `outputs/`).

---

## Session Start Protocol

At the start of every session:

1. Read this CLAUDE.md.
2. List `project/source_documents/v5_completed/` to see which v5 documents
   already exist.
3. Identify the next document in the work queue by phase order.
4. Read the corresponding plan in `outputs/Execution_Plan_Document_<id>.md`.
5. Read the Phase α v5 exemplar most analogous to the next document's type
   (preserved-with-edits or re-specified or new) for register calibration.
6. Ask the user: "Ready to draft Document <id> ([Phase letter]). Proceed?"

Wait for confirmation before drafting.

---

## Model and Venue Note

Drafting in Claude Code: use Opus 4.7 (1M context). Documents M, W, R, and
D-Synthesis are authored in claude.ai per their stub plans; Document G is
authored in Claude Code after D-Synthesis is complete in claude.ai and
present in `project/source_documents/v5_completed/`. The 1M context is
load-bearing for Document G (capstone reading of the full arc) and for any
late-phase document that cross-references many prior v5 documents.

See `PROJECT_COMPLETION_ROADMAP.md` in repo root for the human-facing
strategic roadmap on which work belongs in which venue, the order of
operations across Claude Code and claude.ai sessions, and the post-drafting
project state.
