# Claude Code Kickoff — v7 Session 0: Scaffolding, Planning Document, Redundancy Audit, Consolidation Plans

This is the **first** v7 Claude Code session. Its job is to build the v7 scaffolding, author the seventh-pass planning document, write the redundancy audit script, run the audit, and author the two consolidation execution plans. **Do not draft the consolidated documents in this session.** That is the next session's work (Phase 7α Step 3). **Do not perform tension-identification or capstone-synthesis work.** Those are Phases 7β and 7γ.

The seventh pass operates against a condensed v7 corpus consolidated from the 42 sixth-pass documents through two targeted consolidations:
- **Cluster A** — Part II disturbance-regime diagnostics: `II.02_Cultural` + `II.04_Biological` + `II.05_Physical_Environmental` + `II.06_Cognitive_Informational` + `II.07_Political_Economic` → `II.02_Five_Regime_Disturbance_Diagnostic_v7.md`
- **Cluster B** — Part XII decision-rights cluster: `XII.09_Foundational` + `XII.10_Public_Check` + `XII.11_Provisioning` + `XII.12_Cognitive_Intergenerational` → `XII.09_Bounded_Decision_Rights_Across_Nested_Scales_v7.md`

Net reduction: 42 → 35 active documents. Nine v6 documents superseded (archived, not deleted). The remaining 33 v6 documents continue under v7 names through cross-reference repair only.

The v6 cut-over: before the v7 session work begins, the active `CLAUDE.md` at the repo root (currently v6) is moved to `project/CLAUDE_v6_historical.md`, and `CLAUDE_v7.md` is renamed to `CLAUDE.md`. This kickoff assumes that cut-over has been performed; if it has not, perform it as the first action of this session.

---

## Read First

1. `CLAUDE.md` (repo root) — v7 session protocol (if the cut-over has happened) or `CLAUDE_v7.md` (if it has not).
2. `project/Sixth_Pass_Planning_Document.md` — Section XII (the planning-document specification of the seventh-pass milestone) and Section VII (the v6 42-document naming map, substrate for the v7 naming map).
3. `project/source_documents/v6_completed/XIV.01_Capstone_Synthesis_v6.md` Thread H (the v6 capstone's closing specification of what the seventh pass takes up).
4. The seventh-pass plan file (where this kickoff lives, if a planning agent placed it there) or this kickoff document itself as the operational reference.

---

## Tasks (in order)

### Task 0 — v6 → v7 CLAUDE.md cut-over

If `/home/user/CProj/CLAUDE.md` is the v6 file, perform the cut-over:

```bash
mv /home/user/CProj/CLAUDE.md /home/user/CProj/project/CLAUDE_v6_historical.md
mv /home/user/CProj/CLAUDE_v7.md /home/user/CProj/CLAUDE.md
```

Verify the active `CLAUDE.md` is the v7 file (first line should be `# CLAUDE.md — CProj v7 Condensation-and-Synthesis Pass`). Read it.

If the cut-over has already happened (no `CLAUDE_v7.md` at root; active `CLAUDE.md` is the v7 file), skip this task.

### Task 1 — Create the v7 directory structure

Create these directories if absent:

```
project/source_documents/v7_completed/
project/source_documents/v6_completed/_superseded_in_v7/
outputs/v7_plans/
outputs/v7_audits/
outputs/v7_derivative/
audits/
```

Verify these exist; do not modify their contents in this session:

```
project/source_documents/v6_completed/
outputs/v6_plans/
```

### Task 2 — Verify input files are present

Report present/absent for each. Do not create or modify these — only verify.

**Planning and convention files:**
- `CLAUDE.md` (now the v7 file)
- `project/CLAUDE_v6_historical.md` (the v6 archive)
- `project/PROJECT_CONVENTIONS.md`
- `project/Sixth_Pass_Planning_Document.md`
- `project/Formulaic_Thinness_Audit.md`

**V6 corpus in `project/source_documents/v6_completed/`** — verify 42 active documents are present (plus the historical Document 6 `Historical_Phase_One_Synthesis.md`, which remains outside the active arc). The nine to-be-superseded documents must all be present (they are the consolidation substrate):
- `II.02_Cultural_Disturbance_Diagnostic_v6.md`
- `II.04_Biological_Disturbance_Diagnostic_v6.md`
- `II.05_Physical_Environmental_Disturbance_Diagnostic_v6.md`
- `II.06_Cognitive_Informational_Disturbance_Diagnostic_v6.md`
- `II.07_Political_Economic_Disturbance_Diagnostic_v6.md`
- `XII.09_Foundational_Decision_Rights_v6.md`
- `XII.10_Public_Check_Decision_Rights_v6.md`
- `XII.11_Provisioning_Decision_Rights_v6.md`
- `XII.12_Cognitive_Intergenerational_Decision_Rights_v6.md`

**V6 execution plans in `outputs/v6_plans/`** — verify the nine corresponding v6 plans are present (they are the union-of-merged-plans substrate for the two v7 consolidation plans).

**Audit infrastructure** — verify existing audit tooling in `project/tools/` (if present) and `audits/` is reachable.

### Task 3 — Author `project/Seventh_Pass_Planning_Document.md`

Write the seventh-pass planning document. Length: planning-document register (`Sixth_Pass_Planning_Document.md` is the calibration anchor). Substantive but not exhaustive. Required sections:

- **Section I — Pass identity.** Seventh pass; condensation-and-synthesis pass; succession to sixth pass. The pass's character: it begins with the user-directed condensation (Phase 7α) and proceeds through the planning-document-specified work (Phases 7β through 7ε).
- **Section II — The condensed-corpus target.** 42 → 35 documents. Specify Cluster A and Cluster B; specify the four load-bearing standalones (III.01, XII.01, XIII.01, XIV.01) that do not consolidate; specify that the moderate consolidation scope was authorized after the redundancy survey identified these two clusters as the strongest candidates and the other plausible clusters (Part I founders' record; Part VI material substrates; the structural-commitment cluster XII.02–XII.05) as weaker candidates the v7 pass does not attempt.
- **Section III — The five-phase work specification.** 7α (this kickoff and Phase 7α Step 3 consolidation drafting), 7β (tension-identification read), 7γ (v7 capstone synthesis at synthesis standing), 7δ (targeted revisions), 7ε (public-facing derivative).
- **Section IV — The union-of-plans completeness-check gate.** The operational guarantee against substance loss. For each consolidated document, the gate is evaluated against the union of merged source v6 plans' Required Threads, primary articulators, source requirements, cross-references, and What-to-Avoid items.
- **Section V — Cross-reference repair specification.** The repair pattern (every reference to a superseded v6 document name updated to the consolidated v7 document name). The bulk-and-atomic discipline (repair runs in the same phase as the consolidations, before the corpus settles into v7 state).
- **Section VI — Archival treatment of superseded v6 documents.** Move (not delete) to `_superseded_in_v7/`. The v6 capstone is preserved in place at `v6_completed/`, not archived (replaced, not superseded). A README in `_superseded_in_v7/` records each supersession's target.
- **Section VII — The v7 naming map.** 35 active document names; the 9 superseded v6 documents and their consolidation targets; the gap convention (freed ordinals remain unfilled).
- **Section VIII — Skills load.** Carried forward from v6.
- **Section IX — Audit specifications.** Nine-criterion completeness-check gate; union-of-plans loss-check (Phase 7α); cross-reference resolvability audit (every phase); redundancy audit (Phase 7α deliverable; available throughout).
- **Section X — Phase deliverables.** Per phase, the specific files and audit reports.
- **Section XI — Relation to the sixth-pass planning document.** The Sixth_Pass_Planning_Document is preserved unchanged; the seventh-pass plan succeeds it. Section XII of the sixth-pass document is honored through Phases 7β through 7ε; the user-directed condensation is added at Phase 7α head.
- **Section XII — Deferred work.** The eighth pass is not specified in the seventh pass.

### Task 4 — Author `audits/redundancy_audit_v7.py`

Write the redundancy audit script. Specification:

- **Inputs:** the 42 v6 documents at `project/source_documents/v6_completed/` and the 32 v6 execution plans at `outputs/v6_plans/`.
- **Computations:**
  - *Cross-document analytical overlap.* For each pair of documents within the same Part, compute TF-IDF cosine similarity on 5-sentence rolling windows. High-similarity windows are duplication-event candidates. Report the pairs with similarity above a threshold (start at 0.4; calibrate against the v6 corpus's actual distribution).
  - *Plan-thread overlap matrix.* For each v6 execution plan, extract the Required Threads (Section 5 of the plan; the threads are markdown sub-headers under "## 5. Required Threads"). Build a thread × document matrix. Documents with high thread-overlap in the same Part are consolidation candidates.
  - *Cross-citation-vs-duplication mapping.* For every cross-reference (regex pattern: backtick-document-name like `` `II.04_Biological_Disturbance_Diagnostic_v6` ``) in every v6 document, classify whether the citing passage references the cited substance (appropriate cross-citation) or re-articulates the cited substance (duplication-event). Heuristic for re-articulation: a citing passage that contains the named primary articulators of the cited document at first-mention conventions is likely duplication; a citing passage that references the cited document by designation without re-articulating articulators is appropriate cross-citation.
- **Outputs:** structured report at `outputs/v7_audits/redundancy_audit_v7_report.md` with:
  - The cross-document overlap matrix (top-N highest-similarity pairs per Part)
  - The plan-thread overlap matrix (rendered as a table)
  - The cross-citation-vs-duplication mapping (one row per cross-reference, with classification)
  - A summary section identifying Cluster A and Cluster B (and any additional consolidation candidates the audit surfaces) with substantiation drawn from the computed metrics
- **Style:** Python 3; reproducible (idempotent on the v6 corpus); clearly named output; calibrated against the project's existing audit tooling pattern (see `project/Formulaic_Thinness_Audit.md` and the audit infrastructure under `project/tools/` or `audits/` if present).

### Task 5 — Run the audit and confirm cluster findings

Execute `python3 audits/redundancy_audit_v7.py`. Verify the report at `outputs/v7_audits/redundancy_audit_v7_report.md` exists and:

1. Identifies **Cluster A** (Part II regime diagnostics II.02 + II.04 + II.05 + II.06 + II.07) as a consolidation candidate.
2. Identifies **Cluster B** (Part XII decision-rights cluster XII.09 + XII.10 + XII.11 + XII.12) as a consolidation candidate.
3. Surfaces any additional consolidation candidates.

If additional candidates beyond Cluster A and B are surfaced, **stop and escalate** via the Ambiguity Handling protocol in `CLAUDE.md`. The user authorized moderate scope (two clusters); expanding beyond that requires explicit user decision.

If the audit fails to identify Cluster A or Cluster B as candidates, **stop and escalate** — this indicates the audit's heuristics are mis-calibrated or the survey's identification was wrong. Re-calibrate before proceeding.

### Task 6 — Author the two consolidated-document v7 execution plans

Author the two v7 execution plans under the `execution-plan-writing` skill, each self-contained per the v6 self-contained-execution-plan requirement (`PROJECT_CONVENTIONS.md` Section 10 equivalent).

**`outputs/v7_plans/Execution_Plan_II.02_Five_Regime_Disturbance_Diagnostic_v7.md`** — the consolidated Part II diagnostic plan. The plan:
- Document identification: `II.02_Five_Regime_Disturbance_Diagnostic_v7.md`; Part II, ordinal 02; status: consolidation from five v6 plans (II.02, II.04, II.05, II.06, II.07); v6 designators recorded as traceability.
- Load-bearing triad statement (carried forward unchanged).
- Skills (scholarship-mode, completeness-not-length, direct-to-output-drafting, usage-efficiency, long-research-splitting).
- Substantive task: five-regime diagnostic at consolidated standing with one major Part per regime (Cultural; Biological; Physical-Environmental; Cognitive-Informational; Political-Economic), preserving each regime's analytical apparatus in its own register.
- Required Threads: the **union** of all Required Threads from the five merged v6 plans, organized by regime. Every thread named in any merged plan must appear in the consolidated plan.
- Primary articulators: the union of all five merged plans' primary articulators, with tribal affiliations preserved.
- Source requirements: the union of all five plans' sources.
- Structural requirements: no bullets in analytical sections; integrated citations; References organized by regime.
- Cross-references: the union of all five plans' upstream and downstream cross-references, updated to v7 names where applicable.
- Output requirements: path to `v7_completed/`.
- What to avoid: the union of the five plans' What-to-Avoid items, plus the new consolidation-specific item — "no flattening of regime distinctions into single-regime synthesis vocabulary; each regime engaged in its own analytical apparatus with cross-regime hooks to `II.08_Disturbance_Regime_Interactions_v7`."

**`outputs/v7_plans/Execution_Plan_XII.09_Bounded_Decision_Rights_Across_Nested_Scales_v7.md`** — the consolidated Part XII decision-rights plan. Analogous union construction:
- Document identification: `XII.09_Bounded_Decision_Rights_Across_Nested_Scales_v7.md`; Part XII, ordinal 09; consolidation from four v6 plans (XII.09, XII.10, XII.11, XII.12); v6 designators recorded as traceability.
- Substantive task: nested-scales bounded-decision-rights specification with one major section per scale band (biosphere-ecozone; ecosystem-habitat; habitat-population; organism-organ-system-and-temporal), preserving each scale band's decision-rights specification in the four-element format (scope, scale, feedback, sunset-or-adaptation).
- Required Threads: union of all four merged plans' threads, organized by scale band.
- Primary articulators, sources, structural, cross-references, output: analogous union construction.
- What to avoid: union plus the new consolidation-specific item — "no collapsing of the four-element specification (scope, scale, feedback, sunset-or-adaptation) into single-clause enumeration at any scale band; each scale band's decision rights specified at the operational depth the v6 cluster carried."

Each plan must pass the ten-section self-contained-execution-plan check before drafting can commence in the next session.

### Task 7 — Checkpoint and commit

Report:

1. **Cut-over status** — confirm `CLAUDE.md` is now the v7 file and `project/CLAUDE_v6_historical.md` is preserved.
2. **Directories created** — which were created, which already existed.
3. **Input verification** — present/absent for every file in Task 2.
4. **Planning document** — `project/Seventh_Pass_Planning_Document.md` written; outline its eleven sections.
5. **Redundancy audit** — script at `audits/redundancy_audit_v7.py`; report at `outputs/v7_audits/redundancy_audit_v7_report.md`; cluster findings confirmed (Cluster A and Cluster B identified; any additional candidates escalated).
6. **Consolidation plans** — both v7 plans authored in `outputs/v7_plans/`; ten-section self-contained check confirmed for each.
7. **Next session's work** — Phase 7α Step 3: draft the two consolidated documents (one document per session by default given the consequential standing; the long-research-splitting skill applies). Then Step 4 (cross-reference repair) and Step 5 (archival).

Commit and push in two logical commits:
- Commit 1: cut-over + scaffolding + planning document.
- Commit 2: redundancy audit script + report + two consolidation plans.

Push to `claude/focused-franklin-AfoMw`.

Then **stop and await confirmation** before beginning Phase 7α Step 3 (consolidated document drafting).

---

## Do NOT (this session)

- Draft any consolidated v7 document. Consolidation drafting is Phase 7α Step 3, the next session's work.
- Perform any tension-identification or corpus-synthesis work. Those are Phases 7β and 7γ.
- Move any v6 document to `_superseded_in_v7/`. Archival happens at Phase 7α Step 5, after the consolidated documents pass the union-of-plans gate.
- Rename v6 files in `v6_completed/` to v7 names. The 33 unchanged v6 documents are rebadged through cross-reference repair (Phase 7α Step 4), not through file renames at this stage.
- Modify any v6 source document, v6 plan, or v6 drafted document. They are read-only input for the seventh pass.
- Modify the `Sixth_Pass_Planning_Document.md` or any v6 convention file. The seventh-pass plan is succession, not revision.
- Expand consolidation scope beyond Cluster A and B without user authorization. Escalate ambiguities; do not infer.

---

## After This Session

Once the kickoff is confirmed, Phase 7α Step 3 drafts the two consolidated documents (one per session by default, under `long-research-splitting`). Each consolidated document is drafted under the v7 execution plan authored in this session and passes the union-of-plans nine-criterion completeness-check gate. Phase 7α Step 4 then runs the cross-reference repair pass across the entire downstream v7 corpus. Phase 7α Step 5 archives the nine superseded v6 documents and rebadges the 33 unchanged v6 documents to v7 names with cross-reference-repair-only changes.

When Phase 7α is complete (35 v7 documents in `v7_completed/`; 9 archived in `_superseded_in_v7/`; cross-reference resolvability audit reports zero unresolved), Phase 7β opens: the corpus-wide tension-identification read at 1M context.
