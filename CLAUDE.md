# CLAUDE.md — CProj v6 Execution-Plan Authoring and Document Drafting

This repository contains the sixth-pass constitutional project. The sixth-pass planning is complete (`project/Sixth_Pass_Planning_Document.md`). The current Claude Code work covers two stages: (1) authoring the v6 execution-plan deliverables specified in the sixth-pass plan Section X — seven new plans, eleven plan revisions, one major G plan revision; (2) drafting the v6 documents from those plans in strict phase order.

This file is read at the start of every Claude Code session in this repo. The rules below override Claude Code defaults where they conflict.

---

## Project Context

The sixth-pass architecture is specified in `project/Sixth_Pass_Planning_Document.md`. The fifth-pass plan (`project/Fifth_Pass_Planning_Document.md`) remains authoritative for v5 per-document specifications not re-stated in the v6 plan. The load-bearing triad — biocultural governance, eco-mimetic policy-making, disturbance-adapted implementation — carries forward unchanged from v5. The total v6 active arc is forty-two documents across fourteen Parts: thirty-five active v5 documents plus seven new v6 documents (Health, Care, Land in Part VI; Pedagogy, Harm Response, Labor in Part XII; Climate Displacement in Part II), plus the historical Document 6 outside the active arc. A sixth-pass loss-check corrected the fifth-pass plan's miscount (claimed thirty-seven; verifiable thirty-five with plans plus Document 6; there is no Document 5). The sixth pass uses a position-based naming convention `<RomanNumeral>.<NN>_<Title>_v6.md` and a completeness-check gate: every active document passes the completeness check (this file, Self-Audit Protocols) and is renamed under the convention before entering `v6_completed/`. The full naming map is in `Sixth_Pass_Planning_Document.md` Section VII.

State at start of v6 work:
- Substantively drafted v5 documents (7): 1, 2, 3, A, M, W, R.
- Stub-state v5 documents requiring substantive drafting at v6 depth (22): O, P, S, T, V, 7, 8, 9, 10, E, H, I, K, L, D-Synthesis plus eleven that gain new thread content (D-1, D-2, D-3, D-4, F, U, B, J, Q, M-edits, N).
- Missing entirely (2): G (capstone, expanded at v6), D-Synthesis (no draft yet).
- Seven new v6 documents to author from scratch.

---

## Your Tasks (Three Stages)

### Stage 0: Scaffolding and Verification (First Session)

Run `project/Claude_Code_Kickoff_Prompt_v6.md` as the first v6 session. It creates the directory structure (`project/source_documents/v6_completed/`, `outputs/v6_plans/`, and verifies `v5_completed/` and `relocations/`), verifies every input file is present, builds the 42-document setup manifest, writes the two MANIFEST.md files, and reports. It does not author plans or draft documents. Confirm the scaffolding before Stage 1.

### Stage 1: Execution-Plan Authoring (Initial Sessions)

Produce the complete set of **forty-two** v6 execution plans into `outputs/v6_plans/`, one per active document, all under the v6 naming convention. **No fifth-pass plan is used in place.** The forty-two break down as seven new, eleven revised, one major revision, and twenty-three migrated. The deliverables are specified in `project/Sixth_Pass_Planning_Document.md` Section X; the full naming map is in Section VII.

**Seven new execution plans** for the new v6 documents:
- `Execution_Plan_II.09_Climate_Displacement_and_Belonging_v6.md` (Part II).
- `Execution_Plan_VI.01_Land_Relations_and_Property_v6.md` (Part VI).
- `Execution_Plan_VI.06_Health_as_Cultivation_v6.md` (Part VI).
- `Execution_Plan_VI.07_Care_Kinship_Social_Reproduction_v6.md` (Part VI).
- `Execution_Plan_XII.06_Pedagogy_as_Constitutional_Cultivation_v6.md` (Part XII).
- `Execution_Plan_XII.07_Harm_Response_Accountability_Repair_v6.md` (Part XII).
- `Execution_Plan_XII.08_Labor_as_Cultivation_v6.md` (Part XII).

**Eleven existing plan revisions** for documents gaining new thread content (specified in the v6 plan Section X). Each revision carries forward all v5 plan content and adds the new thread content, output under the document's v6 name.

**One major plan revision** for the capstone (`Execution_Plan_XIV.01_Capstone_Synthesis_v6.md`, was G) — adding comparison gestures for all five new threads plus integration of the four new Part-level documents (Climate Displacement, Health, Care, Harm Response) into the capstone synthesis.

**Twenty-three migrated plans** for the documents that carry no new thread content: copy the fifth-pass plan content into a new file named under the v6 convention (Section VII), apply minor cross-reference tightening, and verify each against the ten-section completeness check and the self-contained-skill-firing requirement. These are migrations, not rewrites — the v5 analytical specification is preserved, renamed, and brought up to the self-contained standard.

All plans are authored or migrated under the `execution-plan-writing` skill. Output path: `outputs/v6_plans/` in this repo. The fifth-pass plans in `outputs/` are read-only migration source.


### Stage 2: Document Drafting (Subsequent Sessions)

After Stage 1 completes, draft the v6 documents in strict phase order. The phase order is specified in `project/Sixth_Pass_Planning_Document.md` Section IX. Each document — including the seven substantively-drafted v5 documents — must pass the completeness-check gate (Self-Audit Protocols, below) before it is renamed under the v6 convention and written to `project/source_documents/v6_completed/`. The phase-order queue below uses fifth-pass designations as traceability labels; each maps to its v6 filename in `Sixth_Pass_Planning_Document.md` Section VII.

**Drafting work queue (Phase Order — Do Not Reorder):**

- **Phase v6.α** — Targeted-edit cross-reference revisions to Documents 1, 2, 3.
- **Phase v6.β** — Documents A (cross-ref revisions only — already drafted), 4, B (with new sexuality/gender + arts/culture threads), C, I.
- **Phase v6.γ** — Documents M (with new arts/culture thread — cross-ref revisions to drafted), L, K.
- **Phase v6.δ** — Documents N (with new arts/culture thread), O, P, Q (with new technology/AI positive thread), **Y (Health, new)**, **AA (Care, new)**, **EE (Land, new)**.
- **Phase v6.ε** — Documents S, T, U (with new media/press + technology/AI positive threads), V, W (cross-ref revisions only — drafted), 7, 8, 9, 10, **CC (Migration, new)**.
- **Phase v6.ζ** — Documents E, F (with new media/press thread), H, J (with new sexuality/gender thread), **Z (Pedagogy, new)**, **BB (Harm Response, new)**, **DD (Labor, new)**.
- **Phase v6.η** — Documents R (cross-ref revisions only — drafted), D-1 (with new sexuality/gender + war-powers threads), D-2 (with new sexuality/gender + war-powers threads), D-3 (with new sexuality/gender thread), D-4 (with new sexuality/gender thread).
- **Phase v6.θ** — Document D-Synthesis.
- **Phase v6.ι** — Document G expanded.

If a v6 document is already present at session start, treat it as substrate available for downstream documents that cross-reference it. If absent, proceed with the documents that do not depend on it and note the dependency.

---

## Drafting Protocol (Both Stages)

For each deliverable, the session proceeds as follows.

### Read the Plan or Source Specification

For Stage 1 (execution-plan authoring): read `project/Sixth_Pass_Planning_Document.md` Section IV (for new documents) or the existing fifth-pass plan `outputs/Execution_Plan_Document_<v5-id>.md` (for revisions; output the revised plan under the v6 name `outputs/v6_plans/Execution_Plan_<RomanNumeral>.<NN>_<Title>_v6.md`). The v6 plan's per-document specification gives the substantive task, primary canon, cross-references, and threading instructions sufficient to author the execution plan.

For Stage 2 (document drafting): `outputs/v6_plans/Execution_Plan_<RomanNumeral>.<NN>_<Title>_v6.md` is the canonical specification. It names the substantive task, the required threads, the primary articulators, the source requirements, the cross-references, and the constraints. The plan is self-contained; the planning document is not required at draft time.

### Read the v4/v5 Source if Applicable

For preserved-with-edits documents and re-specified documents at the v6 stage, the v5 source in `project/source_documents/v5_completed/` (where v5 drafts exist) or `project/source_documents/` (for documents at stub state) is preserved or drawn on per the plan's Source Requirements section.

### Read the Cross-Referenced v6 Documents Where They Already Exist

Documents later in the phase order draw on earlier-phase v6 documents. Read cross-referenced v6 documents from `project/source_documents/v6_completed/`. For Document G, the entire v6 corpus is read end-to-end (Opus 4.7's 1M context supports this).

### Draft to the v6 Output Path

The plan's Section 9 names the output path under `/mnt/user-data/outputs/v6_documents/` (claude.ai venue) or `project/source_documents/v6_completed/` (this repo). Use the filename the plan specifies. For execution plans, the output path is `/mnt/user-data/outputs/v6_plans/` (claude.ai) or `outputs/v6_plans/` (this repo).

### Apply the Move-Don't-Regenerate Principle

Preserve v5 content in preserved-with-edits documents; do not rewrite. For re-specified documents, draw on v5 substrate without duplicating. For relocated material, preserve the analysis in its move; do not reproduce in the source document.

### Honor the Scholarly Register

No bullets in analytical sections. Integrated citations with dates and named works. Indigenous and Eastern primary articulators stand at primary-articulator standing, not as comparative supplement. `completeness-not-length` governs. See `PROJECT_CONVENTIONS.md` Section 5 for full stylistic conventions.

---

## Self-Audit Protocols (Per Deliverable)

### Filler-Discipline Audit

Every drafted document and every drafted execution plan runs the filler-density audit at completion. The audit:

1. Counts hits and computes density per one thousand words for the standard twelve candidate terms: `substantive`, `analytical`, `framing`, `cultivation`, `tradition`, `canon`, `literature`, `primary`, `articulator`, `engagement`, `thread`, `biocultural`. Add document-specific candidates where the analytical terrain suggests them.

2. Reports each term's density. Above ten per one thousand words receives inspection: if the term is load-bearing semantic content (e.g., "thread" in a document centrally about threads), the density is acceptable; if it is gestural padding, the document is revised.

3. For "substantive" specifically: target under five per one thousand words. Above eight is a strong signal of filler. Above fifteen is failure requiring rewrite.

4. Runs a doubled-word scan (`\b(\w+)\s+\1\b`) to catch inline-cleanup artifacts.

Suggested bash one-liner for the audit:

```bash
f=<path to file>
w=$(wc -w < "$f")
echo "Total words: $w"
for word in substantive analytical framing cultivation tradition canon literature primary articulator engagement thread biocultural; do
  c=$(grep -oiE "\b${word}[a-z]*\b" "$f" | wc -l)
  d=$(awk -v w="$w" -v c="$c" 'BEGIN { printf "%.1f", (c*1000)/w }')
  printf "  %-15s %4d hits  (%5s per 1Kw)\n" "$word" "$c" "$d"
done
python3 -c "
import re, sys
text = open(sys.argv[1]).read()
doubles = re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE)
print(f'doubled-word matches: {len(doubles)}')
" "$f"
```

### Completeness-Check Gate

The sixth pass is a completeness-gated migration. Every active document — including the seven substantively-drafted v5 documents (1, 2, 3, A, M, W, R) — passes the completeness check before it is renamed under the v6 convention and admitted to `v6_completed/`. A document that fails does not enter `v6_completed/` until remediated and re-checked. The historical Document 6 is exempt (no plan, no required threads). A document passes when all eight criteria hold:

1. Every Required Thread named in the plan is executed in the draft.
2. Every primary articulator named in the plan is engaged at primary-articulator standing, with tribal/identity affiliation where applicable and full first-mention conventions.
3. Every cross-reference in the plan is present, concrete, and resolvable to a real document in the arc.
4. The filler-density audit passes: no candidate term above its failure threshold; "substantive" under five per one thousand words.
5. The loss-check (below) passes.
6. The doubled-word scan returns zero.
7. The scholarly register matches the Phase α v5 exemplars (1, 2, 3) on calibration.
8. The draft conforms to the plan's What-to-Avoid section.

The completeness-check report accompanies each document at the gate: each of the eight criteria recorded as pass or fail, and for any fail, what was remediated.

### Loss-Check Protocol (Criterion 5, detailed)

Every v6 deliverable runs a cross-pass loss-check before submission:

1. For new sixth-pass execution plans: verify all ten plan sections present (Document Identification; Load-Bearing Triad; Skills to Load; Substantive Task; Required Threads; Source Requirements; Structural Requirements; Cross-References; Output Requirements; What to Avoid).

2. For revised sixth-pass execution plans: verify all v5 content preserved; new thread content integrates without contradiction.

3. For drafted v6 documents: verify every Required Thread from the plan is executed; every primary articulator named in the plan is engaged at primary-articulator standing; every cross-reference is concrete; every What-to-Avoid item is honored. Cross-check against `Fifth_Pass_Planning_Document.md` Section I and Section III for v5 framings the document inherits. For the seven substantively-drafted v5 documents, cross-check the existing draft against its v6 plan (including thread additions) and the v5 framings.

4. Arc-integrity check: confirm the document's Part placement and ordinal match the Section VII naming map, and that no document has been silently added or dropped from the forty-two-document arc.

5. Where loss-check reveals a dropped item, revise the deliverable to restore the item before submission.

This protocol caught the fifth-pass count miscount during sixth-pass planning. It runs on every deliverable to catch this class of silent loss.

### Drift-Check Protocol

In addition to the above, run the drift-check from the v5 CLAUDE.md (preserved here):

- Does the document execute every Required Thread from the plan?
- Are the primary articulators each plan names engaged at primary-articulator standing in their own analytical registers?
- Does the document avoid synthesis-into-architecture across traditions?
- Is the move-don't-regenerate principle honored for v5 substrate?
- Are the cross-references concrete and consistent with the plan?
- Is the scholarly register consistent with the Phase α v5 exemplars in `project/source_documents/v5_completed/`?
- Does the document conform to the plan's What-to-Avoid section?
- Does the document operate under the load-bearing triad (biocultural governance, eco-mimetic policy-making, disturbance-adapted implementation)?

### Per-Document Checkpoint

Report after each document or plan deliverable: the file written (under its v6 name); the threads executed (for documents) or sections completed (for plans); the completeness-check report (eight criteria, for documents at the gate); the filler-discipline audit result; the loss-check result; the drift-check result; any drift indicators or ambiguities encountered; the next deliverable.

**Mandatory single-checkpoint:** the seven new v6 documents (Climate Displacement, Land, Health, Care, Pedagogy, Harm Response, Labor); the consequential documents (III.01 Biocultural Governance, XIII.01 Decision Rights Synthesis, XIV.01 Capstone); the forty-two v6 plan deliverables (seven new, eleven revisions, one major capstone revision, twenty-three migrations); any document where ambiguity arose. Every active document additionally requires its completeness-check report at the gate.

**Relaxed checkpoint for clean propagation:** the cross-reference-revision reports (Phase v6.α and the already-drafted v5 documents that need only cross-reference revisions plus their completeness check) may be batched up to four at a time; each still carries its own completeness-check report at the gate.

**Phase-transition note** at the boundary between phases: `## Phase Transition — entering Phase v6.<letter>` with brief re-read note confirming the Phase α exemplars and the v5 substantively-drafted exemplars have been consulted for register calibration.

---

## Ambiguity Handling

The plan is the canonical specification. If the plan unambiguously names the substantive task, threads, sources, and cross-references, proceed.

If a plan specification is ambiguous, the source files contradict the plan, a cross-referenced upstream document is absent, the v5 plan and v6 plan diverge on a point not explicitly reconciled, or the relocations holding files diverge from the plan's expectations, **stop and ask the user immediately**. Do not guess. Do not pick the most likely interpretation.

The escalation format:

```
## Ambiguity — Document <id>

Plan specification: <quote the relevant section>

Conflicting condition: <quote source file, cross-reference, or holding file>

Possible readings:
1. <reading A and what document it would produce>
2. <reading B and what document it would produce>

My recommendation: <which reading and why, briefly>

Awaiting your resolution before drafting this deliverable.
```

Wait for user response. Do not draft until resolved.

---

## Self-Contained Execution-Plan Requirement

Every v6 execution plan authored under Stage 1 must be completely self-contained. The plan operates as a standalone drafting specification readable without external context other than the named source files and cross-referenced execution plans for upstream documents. Specifically each plan must:

- **Fire the appropriate skills** in its Section 3 opening. The plan names every skill required to draft the document under v6 conventions, in load order: at minimum `scholarship-mode`, `completeness-not-length`, `direct-to-output-drafting`, `usage-efficiency`. Add `pre-drafting-consultation` for new documents under unsettled framing. Add `long-research-splitting` for documents at session-timeout risk.

- **Specify the load-bearing triad** under which the document operates, naming biocultural governance, eco-mimetic policy-making, and disturbance-adapted implementation, with the specific bearing of the triad on the document's analytical task.

- **Name the substantive task** with sufficient specificity that a fresh Claude Code session can draft the document from the plan alone.

- **Specify every Required Thread** including any new v6 threads applying to the document.

- **Name every primary articulator** at primary-articulator standing, with tribal affiliation for Indigenous scholars and full first-mention conventions (author, work, year).

- **Specify source requirements** with explicit paths for v4 substrate, v5 substrate, and any holding files.

- **Specify structural requirements** including no-bullets-in-analytical-sections, no-business-prose-apparatus, citation conventions.

- **Specify cross-references** to upstream and downstream documents by document designation and analytical role.

- **Specify output requirements** including the v6 output path and the filename convention.

- **Specify what to avoid** including the filler-discipline failure modes specific to the document's analytical terrain.

- **Specify the filler-discipline audit** terms the document should run at completion, including any document-specific candidate terms beyond the standard twelve.

- **Specify the loss-check protocol** the document should run, naming the upstream documents and planning sections to cross-check against.

Plans authored under this requirement do not depend on Claude reading the planning document at draft time. The plan is the consultation; the document is drafted from the plan.

---

## File-Write Conventions

- **V6 execution plans:** `outputs/v6_plans/Execution_Plan_<RomanNumeral>.<NN>_<Title>_v6.md`.
- **V6 drafted documents:** `project/source_documents/v6_completed/<RomanNumeral>.<NN>_<Title>_v6.md`.
- **All forty-two active documents are written fresh into `v6_completed/` under the v6 name after passing the completeness-check gate** — including the seven substantively-drafted v5 documents, which are migrated by running them through the completeness check, applying any v6 thread additions and cross-reference revisions, and writing the result under the v6 name. There is no separate `_v6_edits` mechanism.
- **Historical Document 6:** written as `project/source_documents/v6_completed/Historical_Phase_One_Synthesis.md` (no Part ordinal; outside the active arc and the gate).
- **Markdown format, no front-matter.**
- **Title line:** the document's v6 name and Part placement; the fifth-pass designation may be recorded on a header line for traceability only.

---

## Skills to Load (Per Each Plan's Section 3)

Standard skill load for v6 drafting work:

- `scholarship-mode` — register and citation discipline; no bullets in analytical sections; integrated citations with named scholars, works, and dates.
- `completeness-not-length` — evaluate the draft by whether analytical commitments are met, not by word count.
- `direct-to-output-drafting` — write edits directly to the output file rather than drafting in segments and concatenating.
- `usage-efficiency` — strict move-don't-regenerate discipline for v5 substrate and cross-cited documents.
- `execution-plan-writing` — for Stage 1 plan-authoring sessions only.
- `pre-drafting-consultation` — for new documents under unsettled framing where the consultation is part of the plan-authoring or drafting work.
- `long-research-splitting` — for very long documents at session-timeout risk; defaults to off, on when the deliverable exceeds approximately fifteen thousand words.

---

## What to Avoid

- Drafting multiple consequential documents or plans in one response without checkpoint.
- Treating the work queue as suggestions rather than strict phase order.
- Duplicating substantive material across documents where the plan specifies cross-citation.
- Synthesizing the multi-traditional canon into one architectural register.
- Treating Indigenous, Eastern, African, Islamic, Latin American, Caribbean, Pacific Islander, Jewish, dalit, Black-radical, disability-justice, or neurodivergent traditions as comparative supplement to a primarily-Western frame.
- Rewriting v5 source content in preserved-with-edits documents; the move-don't-regenerate principle governs.
- Inventing scholars, works, or traditions not in the plan, the v5 or v6 planning document, or the bibliography.
- Inferring intent on ambiguous specifications instead of escalating.
- Continuing past a checkpoint without user confirmation.
- Skipping the filler-discipline audit at deliverable completion.
- Skipping the loss-check protocol at deliverable completion.
- Authoring an execution plan that is not self-contained (relying on the planning document at draft time rather than supplying the equivalent specification in the plan itself).
- Preserving fifth-pass document numbers or letters in v6 filenames (use the position-based `<RomanNumeral>.<NN>_<Title>_v6.md` convention); writing a document into `v6_completed/` before it has passed the completeness-check gate.
- Citing the named scholar previously identified as biographically disqualified.
- Citing Anabaptist political theology through individual scholars with biographical-record disqualification (engage the analytical work without the personal citation).

---

## Reference Files in This Repo

- `project/Sixth_Pass_Planning_Document.md` — primary specification for v6 architecture; not required for drafting once plans are read.
- `project/Fifth_Pass_Planning_Document.md` — authoritative for v5 per-document specifications not re-stated in v6.
- `project/PROJECT_CONVENTIONS.md` — workflow conventions for v6 (this file aligns with PROJECT_CONVENTIONS.md Sections 6, 7, 8, 9, 10).
- `outputs/Execution_Plan_Document_<v5-id>.md` — v5 execution plans (preserved; revised versions output under v6 names).
- `outputs/v6_plans/Execution_Plan_<RomanNumeral>.<NN>_<Title>_v6.md` — v6 execution plans (new and revised).
- `project/bibliography_consolidated_v4.md` — v4 bibliography; v5 additions in v5 plan Section VII; v6 additions in v6 plan Section XI.
- `project/source_documents/<doc>.md` — v4 source documents.
- `project/source_documents/v5_completed/Document_One_..._v5.md` through `Document_Three_..._v5.md` — Phase α v5 exemplars and calibration anchors.
- `project/source_documents/v5_completed/Document_A_..._v5.md`, `Document_M_..._v5.md`, `Document_W_..._v5.md`, `Document_R_..._v5.md` — additional substantively-drafted v5 exemplars.
- `project/source_documents/v6_completed/` — v6 drafted documents (populated by Stage 2 work).
- `project/relocations/Document_4_relocations.md`, `Document_7_relocations.md`, `Document_9_relocations.md` — relocations holding files for Documents 4, 7, 9 to Document L.

---

## Session Start Protocol

At the start of every session:

1. Read this `CLAUDE.md`.
2. Read `project/PROJECT_CONVENTIONS.md` if any convention is unclear from `CLAUDE.md` alone.
3. Identify whether the session is Stage 0 (scaffolding), Stage 1 (plan-authoring), or Stage 2 (document-drafting).
4. **If `outputs/v6_plans/` and `project/source_documents/v6_completed/` do not yet exist, this is Stage 0:** run `project/Claude_Code_Kickoff_Prompt_v6.md`, produce the scaffolding and manifest, and stop for confirmation. Do not author plans or draft documents.
5. For Stage 1: list `outputs/v6_plans/` to see which v6 plans already exist; identify the next plan in the deliverable list (v6 plan Section X), in the order new → revised → migrated or as the user directs.
6. For Stage 2: list `project/source_documents/v6_completed/` to see which v6 documents already exist; identify the next document in the work queue by phase order.
7. Read the corresponding plan or planning-section.
8. Read the appropriate Phase α v5 exemplar (or v5-substantively-drafted exemplar most analogous to the next document's type) for register calibration.
9. Ask the user: "Ready to draft <deliverable> (<stage or phase>). Proceed?"

Wait for confirmation before drafting.

---

## Continue-Plan Protocol

When the user opens a session with **"continue plan"** — or "continue", "resume", "next", or any equivalent — it is a standing instruction to **self-orient and execute the next project deliverable** without the user naming any document, file, folder, branch, or phase. Treat "continue plan" as both the instruction and the proceed-confirmation: do not run the Session Start Protocol's step-9 question. Instead, state in one sentence what the next deliverable is, then do it.

Self-orientation algorithm:

1. **Branch.** All v6 work lives on branch `claude/kickoff-prompt-v6-M03uX` (the forty-two execution plans and every completed v6 document). Run `git branch --show-current`. If the session is not on that branch, `git fetch origin claude/kickoff-prompt-v6-M03uX` and bring the working tree to that branch's state (`git checkout`, or merge it into the harness-fixed branch). If that state cannot be reached, stop and tell the user — do not proceed on an empty or wrong branch.

2. **Determine the stage.**
   - If `outputs/v6_plans/` or `project/source_documents/v6_completed/` does not exist → **Stage 0**: run `project/Claude_Code_Kickoff_Prompt_v6.md`, produce the scaffolding and manifests, stop for confirmation.
   - If `outputs/v6_plans/` holds fewer than forty-two `Execution_Plan_*_v6.md` files → **Stage 1**: author the next missing plan per `Sixth_Pass_Planning_Document.md` Section X (order: seven new → eleven revised → one major → twenty-three migrated).
   - If all forty-two plans exist → **Stage 2**: document drafting.

3. **Stage 2 — find the next deliverable.** Read `project/Stage2_Session_Plan.md`. List `project/source_documents/v6_completed/`. The next deliverable is the first document in that file's Session Sequence (strict phase order v6.α → v6.ι) for which no `<id>_v6.md` file yet exists in `v6_completed/`. Draft it per the focused-session workflow and the two transition policies recorded in `Stage2_Session_Plan.md`: read its plan and the substrate the plan names, draft to `v6_completed/`, run the eight-criterion completeness-check gate (Self-Audit Protocols, above), commit, and push.

4. **Report and scope.** One "continue plan" completes one deliverable — one document, or one batch of up to four cross-reference-revision documents under the relaxed checkpoint — then gives the per-document checkpoint and names the next deliverable. The user may widen the scope explicitly ("continue plan through Phase v6.γ", "continue until an issue arises"); honor the stated width.

"Continue plan" does not override the Ambiguity Handling section: if the next step is genuinely ambiguous, a cross-referenced upstream document is missing, or a source contradicts a plan, stop and escalate in the required format rather than guessing.

---

## Model and Venue Note

Drafting in Claude Code: use Opus 4.7 (1M context). The 1M context is load-bearing for Document G (capstone reading of the full v6 corpus end-to-end) and for any late-phase document that cross-references many prior v6 documents. The 1M context is also load-bearing for the seventh-pass synthesis work specified in `Sixth_Pass_Planning_Document.md` Section XII (corpus-wide end-to-end reading).

See `PROJECT_COMPLETION_ROADMAP.md` in repo root for the human-facing strategic roadmap on which work belongs in which venue, the order of operations across Claude Code and claude.ai sessions, the post-Stage-1 and post-Stage-2 project state, and the seventh-pass milestone.
