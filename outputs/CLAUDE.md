# CLAUDE.md — CProj v5 Document Drafting

This repository contains the fifth-pass constitutional project. Plan authoring is complete: **thirty-two full execution plans** exist in `outputs/` — the original twenty-eight plus the four formerly-stub plans for M, W, R, and D-Synthesis, which were authored in claude.ai sessions and now contain full Sections 3 through 10. The current task is to **draft the v5 project documents** from those plans.

This file is read at the start of every Claude Code session in this repo. The rules below override Claude Code defaults where they conflict. **All necessary skill content is inlined in Section IX of this file** so that a session in any Claude Code environment can operate without depending on user-skills installed at the OS level.

---

## I. Project Context

The fifth-pass architecture is specified in `project/Fifth_Pass_Planning_Document.md`. The load-bearing triad: **biocultural governance** as constitutional ontology, **eco-mimetic policy-making** as operational method, **disturbance-adapted implementation** as temporal orientation. Indigenous and Eastern traditions are primary articulators; the Western CAS, ecology, biomimicry, and disturbance-ecology canons are recent and partial recovery. Five disturbance regimes: cultural, biological, physical-environmental, cognitive-and-informational, political-economic. "Grown, not built" is colloquial summary.

The arc contains thirty-seven documents across fourteen Parts. Three Phase α v5 documents have been drafted: Documents 1, 2, 3 in `project/source_documents/v5_completed/`. Document 6 is preserved as historical Phase-One synthesis (`project/source_documents/Capstone_Synthesis.md`); it is not load-bearing and is cited only where relevant by Document G. The remaining v5 documents are to be drafted under this plan.

---

## II. Repository File Structure

The canonical repository is `github.com/jakegthatsme/CProj` (branch `main`). The expected directory layout under the repo root is:

```
CProj/
├── CLAUDE.md                              [this file]
├── PROJECT_COMPLETION_ROADMAP.md          [strategic roadmap, human-facing]
├── Claude_Code_Kickoff_Prompt.md          [session kickoff template]
├── .gitignore
│
├── outputs/                               [the 32 execution plans]
│   ├── Execution_Plan_Document_1.md       [Phase α exemplar plan]
│   ├── Execution_Plan_Document_2.md       [Phase α exemplar plan]
│   ├── Execution_Plan_Document_3.md       [Phase α exemplar plan]
│   ├── Execution_Plan_Document_A.md
│   ├── Execution_Plan_Document_4.md
│   ├── Execution_Plan_Document_B.md
│   ├── Execution_Plan_Document_C.md
│   ├── Execution_Plan_Document_I.md
│   ├── Execution_Plan_Document_K.md
│   ├── Execution_Plan_Document_L.md
│   ├── Execution_Plan_Document_M.md       [authored in claude.ai]
│   ├── Execution_Plan_Document_N.md
│   ├── Execution_Plan_Document_O.md
│   ├── Execution_Plan_Document_P.md
│   ├── Execution_Plan_Document_Q.md
│   ├── Execution_Plan_Document_R.md       [authored in claude.ai]
│   ├── Execution_Plan_Document_S.md
│   ├── Execution_Plan_Document_T.md
│   ├── Execution_Plan_Document_U.md
│   ├── Execution_Plan_Document_V.md
│   ├── Execution_Plan_Document_W.md       [authored in claude.ai]
│   ├── Execution_Plan_Document_7.md
│   ├── Execution_Plan_Document_8.md
│   ├── Execution_Plan_Document_9.md
│   ├── Execution_Plan_Document_10.md
│   ├── Execution_Plan_Document_E.md
│   ├── Execution_Plan_Document_F.md
│   ├── Execution_Plan_Document_H.md
│   ├── Execution_Plan_Document_J.md
│   ├── Execution_Plan_Document_D-1.md
│   ├── Execution_Plan_Document_D-2.md
│   ├── Execution_Plan_Document_D-3.md
│   ├── Execution_Plan_Document_D-4.md
│   ├── Execution_Plan_Document_D-Synthesis.md   [authored in claude.ai]
│   └── Execution_Plan_Document_G.md
│
└── project/
    ├── Fifth_Pass_Planning_Document.md          [single source of truth, architecture]
    ├── Fourth_Pass_Planning_Document.md         [historical]
    ├── bibliography_consolidated_v4.md          [v4 bibliography; v5 additions in planning doc §VII]
    ├── question_resolution_answers.md           [fourth-pass question-resolution; historical]
    │
    ├── source_documents/                        [v4 source documents as preserve/respec substrate]
    │   ├── Document_One_Founding_Texts_and_1787_Implementation.md
    │   ├── Document_Two_Federalist_AntiFederalist_Records_Read_Against_Founding_Texts.md
    │   ├── Document_Three_Founders_Hindsight.md
    │   ├── Document_A_Multi_Traditional_Canonical_Commitment.md
    │   ├── Founders_Biology_Ecology_Anthropology.md            [Document 4 v4 source]
    │   ├── Document_B_Five_Axis_Diagnostic.md
    │   ├── Document_C_Oligarchy_Dark_Money.md
    │   ├── Document_I_Multi_Eyed_Seeing_Constitutional_Method.md
    │   ├── Document_K_CAS_Emergence.md                         [or similar v4 filename]
    │   ├── Document_L_*.md                                     [if v4 substrate present]
    │   ├── Document_E_Currency_Architecture.md
    │   ├── Document_F_E_Democracy_Structural_Public_Check.md
    │   ├── Document_H_Multi_Generational_Rectification.md
    │   ├── Document_J_Neurodivergent_Polis.md
    │   ├── Capstone_Synthesis.md                               [Document 6, preserved historical]
    │   │
    │   └── v5_completed/                                       [drafted v5 documents]
    │       ├── Document_One_Founding_Texts_and_1787_Implementation_v5.md
    │       ├── Document_Two_Federalist_AntiFederalist_Records_Read_Against_Founding_Texts_v5.md
    │       └── Document_Three_Founders_Hindsight_v5.md
    │
    ├── relocations/                             [holding files for relocations to Document L]
    │   ├── Document_4_relocations.md
    │   ├── Document_7_relocations.md
    │   └── Document_9_relocations.md
    │
    └── exemplar_plans/                          [Phase α plan exemplars; historical calibration]
        ├── Execution_Plan_Document_1.md
        ├── Execution_Plan_Document_2.md
        └── Execution_Plan_Document_3.md
```

**Session-start file verification.** Before drafting, run a quick directory check to confirm the actual repo state matches the expected layout above. If subdirectories under `project/` (notably `v5_completed/`, `relocations/`, `exemplar_plans/`) do not yet exist in the repository, create them with `mkdir -p` rather than treating their absence as ambiguity. The four claude.ai-authored plans (M, W, R, D-Synthesis) may need to be committed to `outputs/` before the first Claude Code drafting session if they have not been pushed.

**Note on environment paths.** This repository is consumed from two environments:
- **Claude Code** sessions read files at paths relative to the repository root (e.g., `outputs/Execution_Plan_Document_A.md`, `project/source_documents/Document_B_Five_Axis_Diagnostic.md`).
- **claude.ai** sessions read project knowledge mounted at `/mnt/project/` with a flat directory structure (all project files at one level). When a plan's Section 9 names an output path under `/mnt/user-data/outputs/<filename>`, Claude Code writes to the corresponding repository path `project/source_documents/v5_completed/<filename>` and commits.

---

## III. Your Task

Draft the v5 project documents from the execution plans in `outputs/` in strict phase order. Each plan is self-contained and supplies the substantive task, required threads, source requirements, structural requirements, cross-references, and what-to-avoid for the document it specifies.

### Drafting Work Queue (Phase Order — Do Not Reorder)

- **Phase β** — 5 documents: A, 4, B, C, I
- **Phase γ** — 2 documents in Claude Code: K, L  *(Document M is authored in claude.ai)*
- **Phase δ** — 4 documents: N, O, P, Q
- **Phase ε** — 8 documents in Claude Code: S, T, U, V, 7, 8, 9, 10  *(Document W is authored in claude.ai)*
- **Phase ζ** — 4 documents: E, F, H, J
- **Phase η** — 4 documents in Claude Code: D-1, D-2, D-3, D-4  *(Document R is authored in claude.ai)*
- **Phase θ** — Document D-Synthesis is authored in claude.ai
- **Phase ι** — 1 document: G (Capstone, drafted last in Claude Code)

**Total drafted in Claude Code: twenty-eight documents.** Documents M, W, R, and D-Synthesis are drafted in claude.ai per the specifications in their execution plans. Document G is drafted in Claude Code after D-Synthesis is complete and present in `project/source_documents/v5_completed/`.

If a v5 document corresponding to one of the claude.ai documents (M, W, R, D-Synthesis) is already present at session start, treat it as substrate available for downstream documents that cross-reference it. If absent, proceed with the documents that do not depend on it and note the dependency.

---

## IV. Drafting Protocol

For each document, the session proceeds as follows.

**Read the plan.** `outputs/Execution_Plan_Document_<id>.md` is the canonical specification. It names the substantive task or targeted-edit task, the required threads, the primary articulators, the source requirements, the cross-references, and the constraints. The plan is self-contained; you do not need the planning document to draft from it.

**Check for an existing v5 file before drafting.** Before beginning a new draft, run `ls project/source_documents/v5_completed/` and inspect whether a file matching the plan's Section 9 output filename already exists. If it does, do not overwrite it without confirmation. Treat the existing file as either resumable substrate (if it appears partial) or as already-complete output (if it appears complete) and escalate to the user under Section VII (Ambiguity Handling) for the resolution.

**Read the v4 source if applicable.** For preserved-with-edits documents (per the plan's Status field), the v4 source in `project/source_documents/` is preserved in full; the plan's targeted edits add, extend, or re-frame at specified insertion points. For re-specified documents, the v4 source is substrate drawn on without duplication. For new documents (no v4 source), the plan supplies the substantive specification directly.

**Read the relocations holding files where the plan specifies coordination.** For Documents 4, 7, 9, and L, the files in `project/relocations/` specify section-extraction, shared-substrate, or cross-citation relocations to Document L. The holding files name the specific sections of the v4 sources that move and the analytical framing under which Document L absorbs them.

**Read cross-referenced v5 documents where they already exist.** Documents later in the phase order draw on earlier-phase documents. If Document G is being drafted last, it draws on every prior v5 document via cross-citation, not duplication.

**Draft to the v5 output path specified in the plan.** The plan's Section 9 names the output path under `/mnt/user-data/outputs/`. In this repository the corresponding local path is `project/source_documents/v5_completed/`. Use the filename the plan specifies.

**Apply the move-don't-regenerate principle.** Preserve substantive v4 content in preserved-with-edits documents; do not rewrite. For re-specified documents, draw on v4 substrate without duplicating. For relocated material, preserve the analysis in its move; do not reproduce in the source document.

**Honor the scholarly register.** No bullets in analytical sections. Integrated citations with dates and named works. Indigenous and Eastern primary articulators stand at primary-articulator standing, not as comparative supplement. The "what survives / what does not" analytical move adapted to each document's task.

### Length and Metrics Discipline

This is operational, not gestural. The fifth-pass project's standard for completeness is `completeness-not-length` (inlined in Section IX). The following rules apply to every drafting session and to every v5 document produced:

1. **Do not target a word count, page count, paragraph count, or section count.** Plans do not specify length targets; if one appears anywhere in the prompt, the plan, or the v4 source, ignore it. A draft is complete when its analytical commitments have been met, not when an arbitrary metric has been reached.

2. **Do not include length framing in the document itself.** No "this section, in roughly N words, addresses..." constructions; no "the remainder of this part is roughly X pages"; no "[Continue to roughly N words]" placeholders; no introductory paragraph that promises a specific length.

3. **Do not produce running status updates in the chat that report word counts.** A single `wc -w` at the natural midpoint and a single `wc -w` at the end is enough verification. Word counts are not progress indicators.

4. **Do not pad to a length the document "should" be.** If the Required Threads of the plan have been engaged at engagement depth (not gestural depth), the document is complete regardless of length. A 12,000-word document that engages every thread is finished; a 25,000-word document that gestures at half its threads is not.

5. **Do not abbreviate consequential threads to fit a length the document "should not" exceed.** No upper-bound metric governs either. If the Required Threads warrant deeper engagement than a typical document, draft to engagement depth.

The discipline is operationalized in the Drift-Check Protocol (Section V) and the self-audit checklist there.

### Skills Application Discipline

Each plan's Section 3 names the skills the drafting session must apply. The default set is `scholarship-mode`, `completeness-not-length`, `direct-to-output-drafting`, and `usage-efficiency`. Plans for consequential documents (M, D-Synthesis) and breadth-of-engagement documents (W, R) additionally specify `pre-drafting-consultation` and/or `long-research-splitting`. **The full content of all six skills is inlined in Section IX of this file.** A drafting session does not need to load user-skills from an external location; the rules are present here. The skills are referenced in plans by name; the operational content is in Section IX.

---

## V. Drift-Check Protocol (Per Document)

Self-audit after each document drafted, against this checklist:

- Does the document execute every Required Thread from the plan?
- Are the primary articulators each plan names engaged at primary-articulator standing in their own analytical registers?
- Does the document avoid synthesis-into-architecture across traditions?
- Is the move-don't-regenerate principle honored for v4 substrate?
- Are the cross-references concrete and consistent with the plan?
- Is the scholarly register consistent with the Phase α v5 exemplars in `project/source_documents/v5_completed/`?
- Does the document conform to the plan's What-to-Avoid section?
- **Does the document contain any word-count framing, length targets, or page/section/paragraph counts in its own register?** If yes, remove them — the document's register is scholarly and the metric framing is contagion from defaults the project rejects.
- **Did the drafting session resist the tendency to inflate to an implicit length target or to abbreviate to a perceived ceiling?** Completeness, not length, governs.

**Per-document checkpoint with the user.** Report after each document the file written, the threads executed, the self-audit result, any drift indicators or ambiguities encountered, and the next document.

**Relaxed checkpoint for preserved-with-edits propagation.** For documents whose plan is preserved-with-edits (Targeted-Edit Task / Required Edit Threads in Sections 4 and 5), batch up to four documents in a single checkpoint when each is a clean propagation. For re-specified documents (Substantive Task / Required Threads), one document per checkpoint by default.

**Mandatory checkpoint regardless of relaxation:** the consequential documents (M, D-Synthesis, G — and any document where ambiguity arises), the documents drafted in claude.ai (M, W, R, D-Synthesis), and the final Document G capstone get a per-document checkpoint without batching.

**At phase transitions** (e.g., last of Phase β to first of Phase γ), prepend the checkpoint with `## Phase Transition — entering Phase <letter>` and a brief re-read note confirming the Phase α v5 exemplars have been consulted for register calibration.

---

## VI. Session Start Protocol

At the start of every session:

1. Read this CLAUDE.md.
2. Verify the file structure matches Section II. Run `ls outputs/ && ls project/ && ls project/source_documents/ 2>/dev/null && ls project/source_documents/v5_completed/ 2>/dev/null && ls project/relocations/ 2>/dev/null`. If `project/source_documents/v5_completed/` does not exist, create it with `mkdir -p project/source_documents/v5_completed`.
3. List `project/source_documents/v5_completed/` to see which v5 documents already exist.
4. Identify the next document in the work queue (Section III) by phase order.
5. Read the corresponding plan in `outputs/Execution_Plan_Document_<id>.md`.
6. Read the Phase α v5 exemplar most analogous to the next document's type (preserved-with-edits or re-specified or new) for register calibration. The three exemplars are at:
   - `project/source_documents/v5_completed/Document_One_Founding_Texts_and_1787_Implementation_v5.md` (preserved-with-edits exemplar)
   - `project/source_documents/v5_completed/Document_Two_Federalist_AntiFederalist_Records_Read_Against_Founding_Texts_v5.md` (preserved-with-edits exemplar)
   - `project/source_documents/v5_completed/Document_Three_Founders_Hindsight_v5.md` (preserved-with-edits exemplar; for re-specified or new register, draw also from the plan's Section 7 structural requirements)
7. Ask the user: "Ready to draft Document <id> ([Phase letter]). Proceed?"

Wait for confirmation before drafting.

---

## VII. Ambiguity Handling

The plan is the canonical specification. If the plan unambiguously names the substantive task, threads, sources, and cross-references, proceed.

If a plan specification is ambiguous, the source files contradict the plan, a cross-referenced upstream document is absent, the relocations holding files diverge from the plan's expectations, **or a target v5 file already exists in `project/source_documents/v5_completed/`**, stop and ask the user immediately. Do not guess. Do not pick the most likely interpretation. The user has chosen explicit ambiguity escalation as the policy.

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

## VIII. File-Write Conventions

- All v5 documents go to `project/source_documents/v5_completed/`.
- Use the filename specified in each plan's Section 1 / Section 9. Where the plan names `/mnt/user-data/outputs/<filename>`, write to `project/source_documents/v5_completed/<filename>` in this repo.
- Markdown format. No front-matter.
- Title line: as specified in the plan, typically including the document designation in title.
- Commit after each document: `git add project/source_documents/v5_completed/<filename> && git commit -m "Draft Document <id> v5" && git push`.

---

## IX. Skills (Inlined Content)

The following six skills are the substantive rule sets for v5 drafting work. They are inlined here so that Claude Code sessions in any environment can apply them without depending on user-skills installed at the OS level. Where a plan's Section 3 references a skill by name, that skill's content is below.

### IX.1 — scholarship-mode

**Conventions for long-form scholarly writing.** Long-form scholarly writing operates at a different register from explanation, business prose, or general writing. This skill specifies the form; the substantive commitments are the user's.

**Core rules:**

*Prose only in body sections.* No bullet points, numbered lists, or table layouts in analytical sections. Lists are for inventories (references, primary sources, abbreviations) — not argument. The connectives between claims are part of the analytical work and disappear when atomized into bullets.

*Sentences carry analytical weight.* Allow long sentences with subordinating clauses where the analytical structure requires them. Avoid the choppy short-sentence style of business prose. Argument that has been broken into bullet points is argument that has been weakened.

*Integrate citations into the sentence.* Cite as part of the sentence that uses the source ("Smith's *Title* of 2017 specifies X"), not as appended drop-ins. The citation does analytical work; it is not bibliographic decoration.

*First-mention conventions are load-bearing.* On first mention give the full author name, the work title, and the year. For Indigenous scholars, include tribal affiliation in parentheses where the scholar has identified themselves with one. For other identity markers, include where it is analytically relevant to the engagement.

*Use the integrated references-list convention.* All sources cited in the body appear in a final References section. Format: Author. *Title* (Year). DOI or URL. Books: canonical Amazon product page or publisher page. Articles: DOI. Primary legal/constitutional documents: official repository. The references list is the document's only permitted bullet-equivalent structure.

*No business-prose apparatus.* No executive summaries at the top, no "key takeaways" boxes, no "TL;DR." Scholarly readers read the document. Section headings help; meta-commentary on what each section is about to do does not.

*Engage opposing views substantively.* Treat critiques as analytical contributions, not obstacles. The strength of a scholarly argument is partly the strength of the opposing view it has engaged.

**Quotation and source engagement:**

*Paraphrase substantively rather than block-quoting.* Long block quotations are a sign that integration has not happened. Use short quotations (under fifteen words, integrated into the sentence) where exact wording is analytically load-bearing; paraphrase otherwise.

*Engage primary sources directly when claims rest on them.* Do not rely on secondary commentary for claims that turn on what a primary text says.

**Avoid:**

*Hedging that masks lack of engagement.* "Some have argued" without naming who is not engagement. Name the source.

*Summary-of-summaries.* A draft that summarizes what others have said about what others have said has not done analytical work.

*Mixed registers within one document.* Pick the register and maintain it.

### IX.2 — completeness-not-length

**Evaluate long-form drafts by whether their analytical commitments have been met rather than by word count.** A draft is finished when its analytical commitments have been met, not when an arbitrary word count has been reached. This skill specifies how to evaluate completeness substantively.

**Core rules:**

*Word counts are proxies, not standards.* Target word counts in prompts are useful guidance for scope but not standards of completeness. A 30,000-word draft that has fully engaged its commitments is finished; a 45,000-word draft that has gestured at half its commitments is not.

*Read the prompt's commitments, then check the draft against them.* What did the introduction say the document would do? What did the table of contents name? What did each section's opening commit to engaging? These are the completeness criteria — not the word target.

*Flag gestures rather than engagement.* A section that names a topic and moves on has gestured; a section that has engaged it has done analytical work the reader can identify. Gestures-where-engagement-was-promised are completeness problems.

*Treat consequential sections at proportional depth.* If the prompt identifies a section as "the most consequential" or "the load-bearing move," its depth should reflect that prominence. Equal depth across consequential and routine sections is itself a gap.

*Asymmetric engagement is a gap.* If a section commits to engaging four critiques and engages two substantively while gesturing at two, fill the gap — do not let parallel structure mask uneven coverage.

**Workflow for evaluating completeness:**

1. List the commitments the prompt and draft made (introduction, TOC, section openings).
2. Read the relevant sections directly. Do not rely on memory of what was drafted, especially for long documents — self-assessment from memory is unreliable. Use `view` or `grep` to inspect the actual content before naming gaps.
3. Identify gaps as (a) gestures where engagement was promised, (b) asymmetric depth where parallel depth was promised, or (c) missing threads that were committed to.
4. Report gaps concretely, not as length deficits.
5. Recommend filling the gaps, not expanding to hit a word target.

**Avoid:**

*Padding to meet a target.* Examples that add no analytical weight, restating points across sections, recapping the introduction in the conclusion. Anti-patterns; they hurt the document.

*Calling a draft complete because it has hit a length.* Length-driven completion produces analytically incomplete documents.

*Refusing to flag gaps because the user did not ask.* When evaluating or assembling a draft, surface completeness gaps even if not asked. The user can override.

*Claiming gaps without inspection.* Self-assessment from memory of long drafts is unreliable. A retracted gap claim wastes more tokens than the inspection would have. If a gap is named, it must have been verified by reading the relevant section first.

### IX.3 — direct-to-output-drafting

**Write long-form deliverables directly to the final output file from the start rather than drafting segments separately and concatenating later.** Long deliverables drafted as separate segments and later concatenated produce five to seven housekeeping tool calls per segment that do not contribute to the work. This skill specifies the direct-write alternative.

**Core rules:**

*Write to the final output file from the start.* Create the output file when drafting begins. Append each part as it is drafted. The final file exists from the first part forward; no concatenation step is needed.

*Verify at meaningful checkpoints, not after every part.* A `wc -w` after every segment is ritual, not verification. Verify at natural seams: roughly the halfway point, after the final part, before delivering. Verification is load-bearing only when it informs a decision.

*Skip the working-file/output-file split for single-file deliverables.* For a single-file document, the working and final files are the same. Drafting in `/home/claude/` and copying to the output location doubles file operations without producing better output. For Claude Code in this repo: draft directly to `project/source_documents/v5_completed/<filename>`.

*Use append operations.* When adding the next section, append to the existing file with `cat >>` or equivalent. Do not view-then-rewrite the whole file; that costs tokens proportional to file size on every append.

**When the segment pattern is correct instead.** Three contexts justify segments-then-concatenate: the deliverable is multiple files (chapter files, episode scripts); the session is at risk of timing out and segments-as-savepoints prevent total loss (see `long-research-splitting` in Section IX.5); the user has explicitly requested segment files for review. Outside these, direct-write is the default.

**Workflow:**

1. Determine the output path before drafting. For v5 documents in this repo: `project/source_documents/v5_completed/<filename>`.
2. Create the file with the title and any front matter (Section VIII says no front-matter — title line only).
3. For each part, append using `bash_tool` with `cat >>` or equivalent.
4. At the natural midpoint and at the end, verify with `wc -w` and `tail`.
5. Commit and push after the document is complete (Section VIII commit convention).

**Avoid:**

*Reading back the full draft at every checkpoint.* Burns tokens on verification the drafting itself just produced. View only when something specific needs to be checked.

*Re-running `ls`, `wc`, or `view` for status updates the user did not ask for.* Status updates are not free; produce them only when load-bearing.

*Long post-presentation summaries.* The document is the artifact. Two to four sentences of contextualizing commentary is enough.

### IX.4 — usage-efficiency

**Rules for minimizing token usage without sacrificing output quality.** Every message costs tokens; input cost grows with every turn (the full history is re-read each message); a full file regeneration costs roughly 40–60x more than a surgical edit. The rules below are the project's discipline for keeping drafting costs low.

**Response length rules:**

*For edits to existing files:* Use `str_replace` with minimal context. Don't echo the whole file. Never paste back unchanged code — edit only what changes.

*For new content:* Add only the new content, inserted at a specific point.

*After a code edit:* 3–5 short summary points maximum explaining what changed. Don't describe content the user can read themselves.

*Post-file summaries:* After creating or editing a file, state what changed and what to verify. Don't write paragraph-length descriptions of every section.

**File editing decision tree:**

```
Is this a new file?
├── YES → Create it (create_file)
└── NO → Is the change < 30% of the file?
    ├── YES → Use str_replace (one or more targeted edits)
    └── NO → Is the architecture changing fundamentally?
        ├── YES → Rebuild (confirm with user first)
        └── NO → Still use str_replace, even if it takes 5-6 edits
              (6 edits × 500 tokens = 3,000 << 1 rebuild × 25,000 tokens)
```

**Before editing:**
1. `view` ONLY the section you need (use view_range). Don't view the whole file if you only need lines 50–80.
2. Make one edit.
3. If another edit is needed in a different section, `view` that section, then edit.
4. If another edit is needed in the same area, re-view (your earlier output is stale after a successful edit).

**Avoid redundant tool calls.** Don't `view` a file you just created. Don't `bash` to check something you can infer from context. Don't search for things already in the conversation. Combine related bash commands: `cmd1 && cmd2 && cmd3` instead of three separate calls.

**Move-don't-regenerate.** For v5 documents that are preserved-with-edits per the plan's Status field, do not rewrite the v4 source. Preserve it and apply targeted edits. For re-specified documents, the v4 source is substrate to draw on; do not duplicate it.

**Conversation management.** Suggest the user start a new chat when: the conversation exceeds roughly 30 messages; the conversation contains large stale code blocks; the task has shifted to a completely different topic; multiple full rebuilds have happened. Do not suggest a new chat when: the user is mid-debugging; context from earlier is critical and not captured in files; the user just asked a quick question.

**Quality gates that are worth the token cost.** Some things should not be skipped to save tokens: always `view` before editing (prevents failed str_replace attempts, which waste more tokens); always read the plan and the Phase α exemplars before drafting; always present files to the user so they can see their work. A correct 500-token edit is cheaper than a broken 200-token edit that requires three more rounds of debugging.

### IX.5 — long-research-splitting

**How to split very long, multi-threaded research-and-writing requests into paired runs and assemble them into one coherent document.** Use whenever a v5 document covers four or more major distinct threads, asks for fully unabridged treatment, or has previously timed out or truncated. For this project: M, W, R, and D-Synthesis (the four claude.ai documents) and Document G (the capstone) are typical candidates; among Claude Code documents, the broader-engagement documents (K, L, 7, 8) may warrant it.

**When to split.** Split when two or more of these apply: the document covers four or more major distinct threads; the user has explicitly asked for unabridged or fully developed treatment; a single run has already failed or stalled. Do not split a unified topic just because the command is long — distinct threads are the requirement, not word count.

**Identifying the seam.** A good seam runs between parts that can each be researched independently without losing argumentative force. Common natural seams:

- Diagnostic vs. prescriptive — critique stands alone; prescription assumes the diagnosis but need not repeat it.
- Theory vs. application — conceptual framework vs. its instantiation in cases.
- History/genealogy vs. contemporary stakes — how we got here vs. what to do now.

For the v5 drafting work, each plan's Section 5 Required Threads typically suggests natural seams. The execution plans for M, W, R, and D-Synthesis explicitly name suggested seams in their Skills to Load (Section 3) `long-research-splitting` notes.

**Segment-to-disk protocol for single-session drafting.** For very long documents drafted in a single Claude Code session, write named segment files to a working location after each major part is complete. This prevents total loss if the session terminates:

```
/tmp/cproj_drafting/<doc_id>_part1.md
/tmp/cproj_drafting/<doc_id>_part2.md
/tmp/cproj_drafting/<doc_id>_part3.md
/tmp/cproj_drafting/<doc_id>_closing.md
```

(Use `/tmp/cproj_drafting/` rather than the repo working tree to avoid committing partial drafts. The final concatenation goes to the repo.)

Concatenate all segments into the final output file only after all parts are complete:

```bash
cat /tmp/cproj_drafting/<doc_id>_*.md > project/source_documents/v5_completed/<filename>_v5.md
```

Verify with `wc -w` and a tail check before committing.

**Paired-run protocol for cross-session drafting.** When a document must be split across multiple Claude Code sessions:

- Run 1 produces Parts One and Two plus a brief opening paragraph situating the entire document in the project arc. The opening allows Run 2 to pick up cleanly.
- Run 2 produces Parts Three and Four plus a closing integration section that ties back to Parts One and Two. The closing reads as if the whole document were written together.
- Both runs share the same project context (this CLAUDE.md), plan specification, and stylistic conventions. The plan in `outputs/` is the canonical specification for both runs.
- Each run's command must state which parts it covers and which are out of scope. Explicit scope prevents the model from covering missing parts thinly.

**Assembly protocol.** After both runs complete (or all segments are written), assemble the final document by: starting with Run 1's opening paragraph as the document's introduction; following with Run 1's Parts; continuing with Run 2's Parts without a section break; closing with Run 2's integration section; merging both reference sections into one deduplicated bibliography alphabetized by author surname. Read end to end before presenting. Fix: redundant scholar re-introductions (keep first, trim second to a name reference), inconsistencies in framing or claims between halves, gaps where one half assumes the other covered something it didn't, tonal drift. Write bridging paragraphs rather than re-running research.

**Avoid.** Do not split a unified topic just because the command is long. Do not launch both runs in parallel — Run 2 benefits from Run 1's framing. Do not announce the splitting strategy in the document — the user sees one document; splitting is implementation detail.

### IX.6 — pre-drafting-consultation

**Standard pre-drafting check on model fit, style fit, intellectual scoping, and citation-base fit before any substantial drafting begins.** This skill prevents producing thousands of words in the wrong frame, register, or scope. For this project: required for M and D-Synthesis (the project's two most consequential drafting tasks); recommended for any document where ambiguity or scope question arises before drafting begins.

**When to use.** Trigger on: drafts likely to exceed 2,000 words; multi-part documents; scholarly or analytical work where analytical scope is non-obvious; tasks where the prompt's stated and implied scopes appear to mismatch. Do not trigger on: edits to existing work (the existing work is the scope); short drafts; resumed sessions where a prior session has already done the consultation (check transcript or context for prior consultation before re-firing).

**The four checks.** Run these before drafting. Each gets one to three sentences in the consultation.

*1. Model fit.* For this project: Opus 4.7 (1M context). Note where a different model would be a better choice. Sonnet 4.6 produces shallower engagement with the non-Western primary articulators and is not recommended for the project's consequential documents.

*2. Style fit.* Does the requested register match the analytical work? The fifth-pass register is scholarly: integrated citations, no bullets in analytical sections, primary-articulator standing for non-Western traditions. Flag register-task mismatches.

*3. Intellectual scoping.* Does the plan's analytical scope match the document's complexity? Are there Required Threads the draft cannot accommodate without splitting? Are there gaps the plan does not name but the work surfaces? Name the consequential ones.

*4. Citation-base fit.* Are the sources the plan names available in `project/bibliography_consolidated_v4.md` or the planning document Section VII v5 additions? If sources will need web research beyond what is present, name the rough scope. Flag missing sources the plan requires.

**Output format.** Two to four short paragraphs in this order: a one-sentence task framing, the consultation across the four checks (combine where appropriate), and a concrete recommended path forward. End with: "Shall I proceed on that basis?" or equivalent. Keep the consultation under 400 words. The user retains authority to override.

**Avoid.** Belaboring the obvious; if a check has nothing to flag, say "no flags here" or skip it entirely. Asking the user to make small choices the prompt already implies. Treating the consultation as a refusal to start; the default after the consultation is to proceed with the recommended path, and the user only needs to respond if they want to override.

---

## X. What to Avoid

- Drafting multiple consequential documents in one response without checkpoint.
- Treating the work queue as suggestions rather than strict phase order.
- Duplicating substantive material across documents where the plan specifies cross-citation.
- Synthesizing the multi-traditional canon into one architectural register.
- Treating Indigenous, Eastern, African, Islamic, Latin American, Caribbean, Pacific Islander, Jewish, dalit, Black-radical, disability-justice, or neurodivergent traditions as comparative supplement to a primarily-Western frame.
- Rewriting v4 source content in preserved-with-edits documents; the move-don't-regenerate principle governs.
- Inventing scholars, works, or traditions not in the plan, the planning document, or the bibliography.
- Inferring intent on ambiguous specifications instead of escalating per Section VII.
- Continuing past a checkpoint without user confirmation.
- **Including word counts, page counts, paragraph counts, or any length-target framing in the draft itself.** No "this section, in roughly N words..."; no "[Continue to N words]" placeholders; no length-of-section advertisements in introductory paragraphs.
- **Self-targeting a length during drafting.** Plans do not name length targets; the project's commitment is `completeness-not-length`. A draft is complete when its analytical commitments have been met, regardless of length.
- **Treating word-count discrepancies between v5 documents as failure modes.** Document M may be longer than Document A or shorter; the standard is per-document analytical completeness, not cross-document parity.

---

## XI. Model and Venue Note

Drafting in Claude Code: use Opus 4.7 (1M context). Documents M, W, R, and D-Synthesis are authored in claude.ai per their plans; Document G is authored in Claude Code after D-Synthesis is complete in claude.ai and present in `project/source_documents/v5_completed/`. The 1M context is load-bearing for Document G (capstone reading of the full arc) and for any late-phase document that cross-references many prior v5 documents.

See `PROJECT_COMPLETION_ROADMAP.md` in repo root for the human-facing strategic roadmap on which work belongs in which venue, the order of operations across Claude Code and claude.ai sessions, and the post-drafting project state.
