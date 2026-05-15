# Project Completion Roadmap — CProj v5

Strategic guide for finishing the fifth-pass constitutional project: which
work goes in Claude Code, which in claude.ai, in what order, with what
model.

---

## Current State

**Done:**
- Five-pass planning document (`project/Fifth_Pass_Planning_Document.md`).
- Phase α v5 exemplar documents drafted: Documents 1, 2, 3 in
  `project/source_documents/v5_completed/`.
- Three Phase α exemplar plans in `project/exemplar_plans/`.
- Twenty-eight full execution plans in `outputs/Execution_Plan_Document_<id>.md`.
- Four stub plans (M, W, R, D-Synthesis) in `outputs/` reserved for claude.ai
  authoring.
- Three reconstructed relocations holding files in `project/relocations/`.
- Document 6 preserved as historical Phase-One synthesis, not requiring
  re-drafting.

**Remaining:** draft thirty-one v5 project documents (twenty-seven in Claude
Code, four in claude.ai), then the Document G capstone in Claude Code.

---

## Venue Strategy

| Work | Venue | Why |
|------|-------|-----|
| Author plans for M, W, R, D-Synthesis (four stubs) | claude.ai | CLAUDE.md reserved these for claude.ai; M and D-Synthesis are flagged as the project's two most consequential drafting tasks |
| Draft v5 documents A, 4, B, C, I, K, L, N, O, P, Q, S, T, U, V, 7, 8, 9, 10, E, F, H, J, D-1, D-2, D-3, D-4 (twenty-seven) | Claude Code | File-system access for v4 sources, plans, relocations, cross-document citations; git integration for incremental commits |
| Draft v5 documents M, W, R, D-Synthesis (four) | claude.ai | Stub plans reserve them for claude.ai; foundational/integrative documents benefit from chat-format deliberative depth |
| Draft v5 Document G (Capstone) | Claude Code | Cross-cites every prior document; 1M-context file reads beat re-pasting into chat |
| Compose v5 bibliography | Claude Code | File-system task; routine consolidation of v4 bibliography plus the additions specified in planning document Section VII |

---

## Model

**Opus 4.7 (1M context) throughout.** The project's scholarly register —
multi-traditional canonical engagement at primary-source depth, "primary
articulators / Western recovery" analytical move, "what survives / what does
not" treatments, no-bullets-in-analytical-sections, named scholars and works
with dates — was calibrated against Opus across plan authoring. Sonnet 4.6
will produce competent prose but consistently shallower engagement with the
Indigenous, Eastern, African, Islamic, Latin American, Caribbean, Pacific
Islander, Jewish, dalit, Black-radical, disability-justice, and neurodivergent
primary articulators. Calibration drift compounds across thirty-one documents.

The 1M context is load-bearing specifically for Document G (capstone,
cross-cites every other document) and Document D-Synthesis (cultivation-
protocol synthesis, integrates every prior architectural commitment). For
mid-arc documents, 200K is sufficient but 1M is safer and the cost
differential is small relative to the substantive depth.

---

## Order of Operations

### Stage 1 — claude.ai sessions for the four stub plans

Author the four execution plans that are currently stubs. Each session takes
one plan to completion. Recommended order: M first (Part III, ontological
grounding), then W (Part II, integrating cross-regime architecture), then R
(Part XII, eco-mimetic policy-making method), then D-Synthesis (Part XIII,
cultivation-protocol synthesis).

**Why this order:** M's biocultural-governance ontology is upstream of W, R,
and D-Synthesis. W's interactions architecture is upstream of R (eco-mimetic
method works against the disturbance landscape W specifies). D-Synthesis
integrates everything and comes last.

**For each claude.ai session, paste:**

```
I'm authoring execution plan <M | W | R | D-Synthesis> for the CProj fifth-
pass project. The plan is currently a stub in the repository
(github.com/jakegthatsme/cproj, file outputs/Execution_Plan_Document_<id>.md).

The planning document is at project/Fifth_Pass_Planning_Document.md; for
this plan the relevant specification is in Section II (line specifying
Document <id>) and in the Part <number> description in Section I.

I'll paste the full planning document and the three Phase α exemplar plans
(Plans 1, 2, 3) as calibration anchors. The exemplars set the register and
structural depth — please match.

The plan must contain ten sections per CLAUDE.md: Document Identification;
Load-Bearing Triad (canonical block plus 1–3 sentences of document-specific
application); Skills to Load; Substantive Task; Required Threads (each
naming scholars, works, analytical commitment); Source Requirements;
Structural Requirements; Cross-References (upstream and downstream); Output
Requirements; What to Avoid.

Indigenous and Eastern primary articulators stand at primary-articulator
standing, not as comparative supplement; the Western recovery canon is named
as such. No word counts. Scholarly prose, no bullets in analytical sections.

[Paste Fifth_Pass_Planning_Document.md, the three Phase α exemplar plans,
and any plans already authored that bear on this one — for M, that's all
plans; for W, the plans for B, S, T, U, V, C; for R, plans for K, M, and
the Part XII documents; for D-Synthesis, every plan.]
```

After each plan is drafted in claude.ai, save it to
`outputs/Execution_Plan_Document_<id>.md` in the repo, replacing the stub,
and commit.

### Stage 2 — Claude Code sessions to draft Phase β through Phase η documents

Begin Claude Code sessions to draft the v5 project documents in strict
phase order per the work queue in CLAUDE.md.

**Per Claude Code session:**

1. Open Claude Code in the CProj repo. Confirm Opus 4.7 model. Confirm 1M
   context if available.
2. Claude Code reads CLAUDE.md automatically (Session Start Protocol).
3. Claude reports current state and asks "Ready to draft Document <id>.
   Proceed?"
4. Confirm. Claude reads the plan, the v4 source (if any), the relocations
   file (if any), and the Phase α v5 exemplar most analogous to the document
   type.
5. Claude drafts the document to
   `project/source_documents/v5_completed/<filename>_v5.md`, commits, and
   pushes.
6. Claude checkpoints (single document for re-specified; up to four batched
   for clean preserved-with-edits propagation; mandatory single for
   consequential documents per CLAUDE.md).
7. Confirm or correct, then proceed to the next document.

**Realistic per-session output:**
- 2–4 documents per session for preserved-with-edits propagation (Plans I,
  E, F, H, J, 10).
- 1–2 documents per session for re-specified documents (most of the queue:
  A, 4, B, C, K, L, 7, 8, 9, the Part VI material-substrate documents,
  the Part II disturbance-regime documents).
- 1 document per session for consequential documents (none in this stage —
  the consequential ones are in claude.ai).
- The four D-series structural-commitments documents (D-1 through D-4) are
  shorter than typical re-specified documents because they specify formal
  bounded-decision-right architecture with cross-citation; 2 per session is
  realistic.

**Stage 2 phase order:**

- Phase β (5 documents): A, 4, B, C, I — estimated 2–3 Claude Code sessions.
- Phase γ (2 documents in Claude Code): K, L — estimated 2 sessions. **At
  this point pause Claude Code work and run the claude.ai sessions for the
  M, W, R plans** (if not already done in Stage 1). Then resume.
- Phase δ (4 documents): N, O, P, Q — estimated 2 sessions.
- Phase ε (8 documents in Claude Code): S, T, U, V, 7, 8, 9, 10 — estimated
  3–4 sessions.
- Phase ζ (4 documents): E, F, H, J — estimated 1–2 sessions.
- Phase η (4 documents in Claude Code): D-1, D-2, D-3, D-4 — estimated 2
  sessions.

**Total Stage 2:** roughly 12–16 Claude Code sessions to complete Phase β
through Phase η in Claude Code.

### Stage 3 — claude.ai sessions to draft the four documents M, W, R, D-Synthesis

After their plans are authored (Stage 1), and after the dependencies are
complete in Claude Code (Stage 2), draft the four documents themselves in
claude.ai. Each is a full session.

Recommended order matches Stage 1 plan-authoring order: **M, W, R, D-Synthesis**.

**For each claude.ai session, paste:**

```
I'm drafting Document <M | W | R | D-Synthesis> for the CProj fifth-pass
project. The execution plan for this document is in the repository at
outputs/Execution_Plan_Document_<id>.md. The plan is the canonical
specification — substantive task, required threads, source requirements,
structural requirements, cross-references, what-to-avoid.

[Paste the execution plan.]

[Paste any cross-referenced v5 documents already drafted — for M, paste
Document A and Document 4 v5 drafts; for W, paste B, S, T, U, V, C drafts;
for R, paste K and the Part XII documents; for D-Synthesis, paste every
v5 document already drafted.]

Draft the v5 document per the plan. Scholarly register throughout.
Indigenous and Eastern primary articulators at primary-articulator standing.
No bullets in analytical sections. Move-don't-regenerate where the plan
specifies. completeness-not-length is the standard.
```

After each document is drafted, save to
`project/source_documents/v5_completed/<filename>_v5.md` in the repo and
commit.

### Stage 4 — Claude Code session to draft Document G (Capstone)

Final stage. By this point all other v5 documents are in
`project/source_documents/v5_completed/`. Open a Claude Code session, Opus
4.7, 1M context. Claude reads CLAUDE.md, identifies Plan G as the final
document, reads Plan G plus every existing v5 document for cross-citation
substrate, drafts the capstone reading.

**Document G is the only document that cross-cites every other v5 document.**
The 1M context is essential here.

Estimated: 1 session.

### Stage 5 — v5 bibliography consolidation

Claude Code session. Read `project/bibliography_consolidated_v4.md`. Read
the planning document Section VII (BIBLIOGRAPHY V5 ADDITIONS). Read every
v5 document for the references each cites. Compose
`project/source_documents/v5_completed/bibliography_consolidated_v5.md` (or
similar path) integrating v4 with the v5 additions and any new sources the
v5 drafting introduced.

Estimated: 1 session.

---

## Estimated Total Effort

- Stage 1 (four claude.ai plan-authoring sessions): 4 sessions.
- Stage 2 (twenty-seven documents in Claude Code): 12–16 sessions.
- Stage 3 (four claude.ai document-drafting sessions): 4 sessions.
- Stage 4 (Document G in Claude Code): 1 session.
- Stage 5 (v5 bibliography in Claude Code): 1 session.

**Total: roughly twenty-five sessions across both venues.**

Calendar time depends on cadence. Doable over 2–4 weeks at one session per
day; 8–12 weeks at one session every few days; longer with lighter cadence.
The phase-by-phase structure tolerates interruption — each session leaves
the repo in a coherent state.

---

## Quality Controls

**Per-document checkpoint in Claude Code.** CLAUDE.md specifies the
checkpoint protocol. Per-document by default; relaxed batching of up to four
for clean preserved-with-edits propagation; mandatory single-checkpoint for
consequential documents.

**Per-document review in claude.ai.** Read the document carefully after
generation; the consequential nature of M, W, R, D-Synthesis warrants close
review before saving to repo.

**Cross-document coherence.** Watch for: register drift away from the Phase
α exemplars; primary-articulator absorption into Western recovery vocabulary;
duplication where cross-citation is specified; synthesis-into-architecture
where cultivation framing is specified.

**The Phase α v5 exemplars are calibration anchors.** When in doubt about
register, re-read Document 1, 2, or 3 v5.

---

## Can I Discard Everything But the v5 Files Once Drafting Is Complete?

**During drafting: no.** Every file in the repo is load-bearing for the
drafting work — v4 sources are read for preserved content, plans are read
as drafting specifications, relocations files are read for section
extraction, planning document specifies architecture, bibliography supplies
citation discipline, Phase α v5 exemplars supply register calibration,
existing v5 documents supply cross-citation substrate.

**After drafting is complete: yes, with one caveat.** The final v5 project
consists of:

- The thirty-four v5 documents in `project/source_documents/v5_completed/`
  (or wherever you settle the output path — recommend a single folder).
- The v5 consolidated bibliography (Stage 5 output).
- Document 6 preserved as historical (`project/source_documents/Capstone_Synthesis.md`),
  cited by Document G but not load-bearing.

The v5 documents are self-contained scholarly deliverables. They cite v4
sources by reference (Pauline Maier 1997, Niane 1965, Hallaq 2013, etc.) the
way any scholarly work cites its sources — without requiring the v4 source
files to be present in the same folder.

**The caveat:** if you want the project to be reproducible (i.e., a future
researcher should be able to see exactly what substrate the v5 documents
were drafted from, what relocations were specified, what plans governed
each drafting session), keep the working files archived: the v4 sources,
the planning document, the plans, the relocations holding files, the Phase
α exemplars. These document the project's methodology and the work that
produced the v5 deliverables. For a published version of the project, only
the v5 documents (plus bibliography) are necessary.

**Recommended:** at end of drafting, create a `v5_published/` folder
containing only the v5 documents and the v5 bibliography, suitable for
publication or distribution. Keep the rest of the repo as `working_archive/`
or similar — accessible for future reference but separated from the
publishable artifacts.

---

## Failure Modes to Watch For

1. **Drift away from primary-articulator standing.** If a v5 document
   absorbs the Indigenous, Eastern, African, Islamic, Latin American,
   Caribbean, Pacific Islander, Jewish, or dalit traditions into Western
   recovery vocabulary rather than engaging them in their own analytical
   registers, the cultivation framing's epistemic warrant fails. This is
   the project's most consequential failure mode.

2. **Synthesis-into-architecture.** If a v5 document synthesizes the
   multi-traditional canon into a single architectural register, the
   decolonial critique that cultivation-as-not-synthesis was designed to
   answer becomes unanswerable. Watch especially in Document M (ontology),
   Document D-Synthesis (cultivation protocol), and Document G (capstone).

3. **Re-introduction of design-imposition framing.** The fifth-pass framing
   replaces design-imposition with cultivation. If a v5 document describes
   the constitutional architecture as engineered, designed, or specified in
   advance of cultivation conditions, the framing has slipped. Watch
   especially in the Part XII structural-commitments documents.

4. **Duplication where cross-citation is specified.** Watch for Document N
   reproducing Q's cradle-to-cradle material, or Document U reproducing B's
   media-axis material, or Document 8 reproducing T's climate-disturbance
   diagnostic. The cross-citation discipline preserves the analytical
   division of labor.

5. **Word-count-driven inflation.** The plans say "completeness-not-length"
   for a reason. Long is not better. Match the analytical depth of the
   Phase α v5 exemplars; do not pad.

6. **Skipping the ambiguity escalation.** CLAUDE.md preserves the explicit
   ambiguity-escalation policy. When the plan, the source, the relocations
   file, or a cross-referenced document disagree, escalate. The cost of
   pausing is small; the cost of guessing wrong compounds across documents.

---

## After Completion

The project produces:

1. The fifth-pass constitutional project as scholarly deliverable — thirty-
   four v5 documents plus consolidated v5 bibliography.
2. A documentary archive of the methodology — plans, planning document, v4
   sources, relocations holding files, Phase α exemplars.
3. A position paper on biocultural governance, eco-mimetic policy-making,
   and disturbance-adapted implementation as constitutional commitments,
   with the cultivation framing as the project's analytical answer to the
   renovation-versus-decolonial question.

The next-250-years framing in Document D-Synthesis is intergenerational; the
analytical work this project produces is the substrate for that long
cultivation. The drafting work itself is one analytical pass; future passes
may revisit any of the substantive treatments as the cultivation work
proceeds across generations.
