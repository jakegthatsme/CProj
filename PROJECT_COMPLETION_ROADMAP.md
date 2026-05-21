# Project Completion Roadmap — CProj v6

Strategic guide for completing the sixth-pass constitutional project: which work goes in Claude Code, which in claude.ai, in what order, with what model. The sixth pass closes the coverage gaps the fifth-pass audit found and migrates the entire corpus to a completeness-gated set of forty-two documents under a new naming convention. The seventh pass synthesizes.

---

## Current State

**Done:**
- Sixth-pass planning document (`project/Sixth_Pass_Planning_Document.md`) — the 42-document arc, the seven new documents, the five new threads, the v6 naming map (Section VII), the phase order (Section IX), the deliverable list (Section X), the bibliography additions (Section XI), the seventh-pass synthesis milestone (Section XII).
- Sixth-pass conventions (`PROJECT_CONVENTIONS.md`) — the completeness-check gate (Section 7), the filler-discipline audit (Section 6), the naming convention and output paths (Section 8), the self-contained execution-plan requirement (Section 10).
- Sixth-pass `CLAUDE.md` — the three-stage workflow, the self-audit protocols, the session-start protocol.
- The Session 0 scaffolding instruction (`project/Claude_Code_Kickoff_Prompt_v6.md`).
- Fifth-pass substrate available as input: the seven substantively-drafted v5 documents (1, 2, 3, A, M, W, R) in `v5_completed/`; the thirty-five v5 execution plans in `outputs/`; the v4 source documents; the relocations holding files; the v4 bibliography.

**Remaining:** scaffold the v6 structure (Stage 0); produce forty-two v6 execution plans (Stage 1); draft forty-two v6 documents through the completeness-check gate (Stage 2); then the seventh-pass synthesis as a separate project milestone.

**Count note:** a sixth-pass loss-check corrected the fifth-pass plan's miscount. The verifiable figures: thirty-five active fifth-pass documents (the fifth-pass plan claimed thirty-seven) plus the historical Document 6; thirty-five v5 execution plans (the fifth-pass plan claimed thirty-four). The v6 active arc is forty-two documents (thirty-five v5 active plus seven new), forty-three including Document 6. There is no Document 5.

---

## Venue Strategy

The sixth pass is set up to run primarily in Claude Code: the scaffolding kickoff, `CLAUDE.md`, and the self-contained execution plans are all built for the file-system-and-git venue. claude.ai is the consultation-and-review venue.

| Work | Venue | Why |
|------|-------|-----|
| Stage 0 scaffolding (directories, input verification, manifest) | Claude Code | File-system task; runs `Claude_Code_Kickoff_Prompt_v6.md` |
| Stage 1 — author/migrate the 42 execution plans | Claude Code | File-system access for v5 plans (migration source), planning document, cross-references; git for incremental commits; bulk authoring is lower per-plan cost |
| Stage 2 — draft the 42 documents through the gate | Claude Code | File-system access for v4 sources, v5 drafts, plans, relocations, cross-document citations; git for incremental commits; the completeness-check audits run as bash one-liners |
| Review of the most consequential documents (III.01 Biocultural Governance, XIII.01 Decision Rights Synthesis, XIV.01 Capstone, the seven new documents) | claude.ai | Chat-format deliberative review before committing to repo; the consequential drafts warrant a close read |
| Seventh-pass synthesis (corpus-wide reading, G v7 capstone, derivative) | Claude Code + claude.ai | 1M-context corpus reads in Claude Code; deliberative synthesis work in either venue |

If you prefer to draft any of the consequential documents in claude.ai rather than Claude Code, the self-contained execution plans support it: paste the plan and the cross-referenced v6 documents, draft, run the completeness check, then commit to repo.

---

## Model

**Opus 4.7 (1M context) throughout.** The project's scholarly register — multi-traditional canonical engagement at primary-source depth, the "primary articulators / Western recovery" analytical move, the "what survives / what does not" treatments, no-bullets-in-analytical-sections, named scholars and works with dates — was calibrated against Opus across the planning and the fifth-pass drafting. Shallower models produce competent prose but consistently thinner engagement with the Indigenous, Eastern, African, Islamic, Latin American, Caribbean, Pacific Islander, Jewish, dalit, Black-radical, disability-justice, and neurodivergent primary articulators. Calibration drift compounds across forty-two documents.

The 1M context is load-bearing specifically for Document XIV.01 (capstone, cross-cites every other document), Document XIII.01 (decision-rights synthesis, integrates every prior architectural commitment), and the seventh-pass synthesis (corpus-wide end-to-end reading). For mid-arc documents, 200K is sufficient but 1M is safer and the cost differential is small relative to the substantive depth.

---

## Order of Operations

### Stage 0 — Scaffolding and verification (one Claude Code session)

Run `project/Claude_Code_Kickoff_Prompt_v6.md`. It creates `project/source_documents/v6_completed/` and `outputs/v6_plans/`, verifies `v5_completed/` and `relocations/`, verifies every input file is present, builds the 42-document setup manifest, writes a `MANIFEST.md` into each output folder, reports a count reconciliation and any missing-input flags, and stops for confirmation. It authors nothing and creates no placeholder content files. Confirm the scaffolding before Stage 1.

Estimated: 1 session.

### Stage 1 — Author and migrate the 42 execution plans (Claude Code)

Produce forty-two v6 execution plans into `outputs/v6_plans/`, one per active document, all under the v6 naming convention. No fifth-pass plan is used in place. The forty-two break down as:

- **Seven new** (Climate Displacement, Land, Health, Care, Pedagogy, Harm Response, Labor) — authored fresh from the canon specified in `Sixth_Pass_Planning_Document.md` Section IV.
- **Eleven revised** (Cultural Disturbance, Cognitive-Informational Disturbance, Biocultural Governance, Cradle-to-Cradle, Built Environment, E-Democracy, Neurodivergent Polis, the four Decision Rights) — fifth-pass plan content carried forward plus new thread content.
- **One major revision** (Capstone) — comparison gestures for all five new threads plus integration of the four new Part-level documents.
- **Twenty-three migrated** — fifth-pass plan content copied into a newly-named v6 file, cross-references tightened, then verified for ten-section completeness and the self-contained-skill-firing requirement.

Each plan must be self-contained and fire its own skills per `PROJECT_CONVENTIONS.md` Section 10. The order within Stage 1: new plans first (they have no migration source), then revised, then migrated (the migrations are mechanical and can be batched). All run under the `execution-plan-writing` skill.

Estimated: 2–3 Claude Code sessions (the nineteen new/revised/major plans are the substantive work; the twenty-three migrations are low-cost).

### Stage 2 — Draft the 42 documents through the completeness-check gate (Claude Code)

Draft the forty-two documents in strict phase order (`Sixth_Pass_Planning_Document.md` Section IX; work queue in `CLAUDE.md`). Every document — including the seven substantively-drafted v5 documents, which are migrated through the gate rather than passed straight through — must pass the eight-criterion completeness check before it is renamed under the v6 convention and written to `project/source_documents/v6_completed/`.

**Per Claude Code session:**

1. Open Claude Code in the CProj repo. Confirm Opus 4.7 and 1M context.
2. Claude reads `CLAUDE.md` (Session Start Protocol) and identifies the next document by phase order.
3. Claude reports current state and asks "Ready to draft <document> (<phase>). Proceed?"
4. Confirm. Claude reads the plan, the v4 source or v5 draft (per the plan's Source Requirements), the relocations file if any, and the Phase α exemplar most analogous to the document type.
5. Claude drafts the document, runs the completeness check (eight criteria), and writes to `v6_completed/` under the v6 name only if the check passes; if it fails, Claude remediates and re-checks.
6. Claude commits, pushes, and checkpoints with the completeness-check report.
7. Confirm or correct, then proceed.

**Phase order and rough session counts:**

- Phase v6.α — 1, 2, 3 (cross-reference revisions + gate migration): ~1 session.
- Phase v6.β — A (migrate), 4, B (+ threads), C, I: ~2–3 sessions.
- Phase v6.γ — M (migrate + arts/culture thread), L, K: ~2 sessions.
- Phase v6.δ — Built Environment, Energy, Food, Materials (+ tech thread), **Land (new), Health (new), Care (new)**: ~4 sessions (heaviest material-substrate phase).
- Phase v6.ε — S, T, U (+ threads), V, W (migrate), 7, 8, 9, 10, **Climate Displacement (new)**: ~4 sessions.
- Phase v6.ζ — E, F (+ thread), H, J (+ thread), **Pedagogy (new), Harm Response (new), Labor (new)**: ~3–4 sessions.
- Phase v6.η — R (migrate), the four Decision Rights (+ threads): ~2 sessions.
- Phase v6.θ — Decision Rights Synthesis: ~1 session (consequential).
- Phase v6.ι — Capstone (expanded): ~1 session (consequential, 1M context).

**Total Stage 2:** roughly 20–24 Claude Code sessions.

### Stage 3 — v6 bibliography consolidation (Claude Code)

Read `project/bibliography_consolidated_v4.md`, the v5 additions in `Fifth_Pass_Planning_Document.md` Section VII, the v6 additions in `Sixth_Pass_Planning_Document.md` Section XI, and every v6 document for the references each cites. Compose `outputs/v6_plans/bibliography_consolidated_v6.md`.

Estimated: 1 session.

### Seventh Pass — Synthesis as project milestone (separate)

The seventh pass does not commence until the sixth pass is substantively complete (all forty-two documents through the gate and in `v6_completed/`). It is specified in `Sixth_Pass_Planning_Document.md` Section XII: corpus-wide end-to-end reading; tension-and-contradiction identification; the final-form Document XIV.01 capstone at synthesis standing (the sixth-pass capstone is a planning-and-anticipation document; the seventh-pass capstone is the actual synthesis); targeted revisions to v6 documents where coordination problems surface; and a public-facing condensed monograph or essay-form derivative. A seventh-pass planning document is authored when the sixth pass nears completion.

Estimated: 15–25 sessions (corpus reading, capstone synthesis, targeted revisions, the derivative).

---

## Estimated Total Effort

- Stage 0 (scaffolding): 1 session.
- Stage 1 (42 plans): 2–3 sessions.
- Stage 2 (42 documents through the gate): 20–24 sessions.
- Stage 3 (v6 bibliography): 1 session.

**Sixth-pass total: roughly 24–29 Claude Code sessions**, plus optional claude.ai review sessions for the consequential documents.

**Seventh-pass (separate milestone): roughly 15–25 sessions.**

Calendar time depends on cadence. The phase-by-phase structure tolerates interruption — each session leaves the repo in a coherent state, and the completeness-check gate means anything in `v6_completed/` is finished, not partial.

---

## Quality Controls

**Completeness-check gate (Stage 2).** The eight-criterion gate (`PROJECT_CONVENTIONS.md` Section 7) is the admission control for `v6_completed/`. Nothing incomplete enters the folder. Each document carries its completeness-check report.

**Filler-discipline audit.** Every drafted document and plan runs the twelve-term filler-density audit and the doubled-word scan at completion (`PROJECT_CONVENTIONS.md` Section 6; bash one-liner in `CLAUDE.md`). "Substantive" under five per one thousand words; no term above its failure threshold unless load-bearing.

**Loss-check protocol.** Every deliverable cross-checks against its plan, the v6 plan, and the v5 plan to confirm nothing load-bearing was dropped, and confirms Part placement and ordinal against the Section VII naming map. This protocol caught the fifth-pass count miscount.

**Per-document checkpoint in Claude Code.** Per-document by default; relaxed batching of up to four for clean cross-reference-revision migrations; mandatory single-checkpoint for the seven new documents, the consequential documents (III.01, XIII.01, XIV.01), and any document where ambiguity arose.

**Per-document review in claude.ai.** The consequential documents warrant a close read before committing to repo.

**Cross-document coherence.** Watch for register drift away from the Phase α exemplars; primary-articulator absorption into Western recovery vocabulary; duplication where cross-citation is specified; synthesis-into-architecture where cultivation framing is specified.

**The Phase α v5 exemplars are calibration anchors.** When in doubt about register, re-read Document 1, 2, or 3 v5.

---

## Failure Modes to Watch For

1. **Drift away from primary-articulator standing.** If a v6 document absorbs the Indigenous, Eastern, African, Islamic, Latin American, Caribbean, Pacific Islander, Jewish, or dalit traditions into Western recovery vocabulary rather than engaging them in their own analytical registers, the cultivation framing's epistemic warrant fails. The project's most consequential failure mode.

2. **Synthesis-into-architecture.** If a v6 document synthesizes the multi-traditional canon into a single architectural register, the decolonial critique that cultivation-as-not-synthesis answers becomes unanswerable. Watch especially in III.01 (ontology), XIII.01 (cultivation protocol), and XIV.01 (capstone).

3. **Re-introduction of design-imposition framing.** If a v6 document describes the constitutional architecture as engineered, designed, or specified in advance of cultivation conditions, the framing has slipped. Watch especially in the Part XII structural-commitment documents.

4. **Duplication where cross-citation is specified.** Watch for Built Environment reproducing Cradle-to-Cradle material, or Cognitive-Informational Disturbance reproducing the cultural-diagnostic media-axis material, or the climate-redesign document reproducing the physical-environmental disturbance diagnostic.

5. **Filler-density inflation.** The fifth-pass failure mode that the sixth-pass discipline targets. "Completeness-not-length"; match the analytical depth of the Phase α exemplars; do not pad with gestural project-terminology. Run the audit.

6. **Skipping the gate.** Writing a document to `v6_completed/` before it has passed the completeness check, or skipping the filler-audit or loss-check. The gate exists because the fifth pass executed thinly behind a fully-planned architecture.

7. **Naming or count drift.** Preserving fifth-pass numbers/letters in v6 filenames, or silently adding or dropping a document from the forty-two-document arc. The loss-check's arc-integrity step catches this.

8. **Skipping ambiguity escalation.** When the plan, the source, the relocations file, or a cross-referenced document disagree, escalate. The cost of pausing is small; the cost of guessing wrong compounds across documents.

---

## After Sixth-Pass Completion

The sixth pass produces:

1. The forty-two v6 documents in `project/source_documents/v6_completed/`, each through the completeness-check gate, named under the v6 convention.
2. The consolidated v6 bibliography.
3. The historical Document 6 (`Historical_Phase_One_Synthesis.md`), preserved and cited by the capstone but outside the active arc.
4. A documentary archive of the methodology — the planning documents, the plans, the v4 sources, the relocations holding files, the Phase α exemplars.

The v6 corpus is the substrate for the seventh-pass synthesis, which is where the corpus becomes a unified theoretical work rather than a collection of related documents. The substantive analytical commitments are produced in the sixth pass; the synthesis-as-work happens in the seventh.

The next-250-years framing in the decision-rights synthesis is intergenerational; the analytical work this project produces is the substrate for that long cultivation. Each pass is one analytical pass; future passes may revisit any of the substantive treatments as the cultivation work proceeds across generations.
