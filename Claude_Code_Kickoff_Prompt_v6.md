# Claude Code Kickoff — v6 Session 0: Scaffolding and Verification

This is the **first** v6 Claude Code session. Its only job is to build the file structure, verify every input is present, and produce a setup manifest. **Do not author any execution plan and do not draft any document in this session.** Plan-authoring (Stage 1) and document-drafting (Stage 2) happen in subsequent sessions, after this scaffolding is confirmed.

The sixth pass migrates the entire corpus to new files. Nothing is reused in place: all 42 execution plans and all 42 documents are created fresh under the v6 naming convention. The 23 fifth-pass plans that carry no new thread content are migrated by copying their content into newly-named v6 files; they are not left in `outputs/` to be used in place.

---

## Read First

1. `CLAUDE.md` (repo root) — v6 session protocol.
2. `project/PROJECT_CONVENTIONS.md` — Sections 7 (completeness-check gate), 8 (naming + output paths).
3. `project/Sixth_Pass_Planning_Document.md` — Section VII (the 42-document naming map), Section X (the plan deliverable list).

The Section VII naming map is the authority for every v6 filename. The "Was" column in that map gives the fifth-pass designation for tracing each document back to its v5 plan and source.

---

## Tasks (in order)

### Task 1 — Create the directory structure

Create these directories if absent:

```
project/source_documents/v6_completed/
outputs/v6_plans/
```

Verify these exist; create if absent:

```
project/source_documents/v5_completed/
project/relocations/
```

### Task 2 — Verify input files are present

Report present/absent for each. Do not create or modify these — only verify.

**Planning and convention files (repo root and `project/`):**
- `CLAUDE.md`
- `PROJECT_CONVENTIONS.md`
- `project/Sixth_Pass_Planning_Document.md`
- `project/Fifth_Pass_Planning_Document.md`
- `project/Fourth_Pass_Planning_Document.md`
- `project/PROJECT_COMPLETION_ROADMAP.md`
- `project/bibliography_consolidated_v4.md`

**Fifth-pass drafted exemplars (calibration anchors) in `project/source_documents/v5_completed/`** — the v5 drafts of the seven substantively-drafted documents (fifth-pass designations 1, 2, 3, A, M, W, R). These are migrated through the completeness-check gate in Stage 2; verify they are present as input.

**Fifth-pass execution plans in `outputs/`** — the 35 v5 plans (one per active v5 document). These are the migration source for the 23 plans that carry no new thread content and the revision source for the 11 revised plans and the capstone revision. Verify how many are present.

**Fourth-pass source documents in `project/source_documents/`** — the v4 substrate the stub documents draw on. Verify the directory is populated.

**Relocations holding files in `project/relocations/`:**
- `Document_4_relocations.md`
- `Document_7_relocations.md`
- `Document_9_relocations.md`

### Task 3 — Build the 42-document setup manifest

Produce a manifest table with one row per active document (42 rows), in Section VII order. Columns:

1. **v6 name** — the `<RomanNumeral>.<NN>_<Title>_v6.md` filename.
2. **Was** — the fifth-pass designation.
3. **Plan action** — `new` (7 docs), `revise` (11 docs + 1 capstone = 12), or `migrate` (23 docs).
4. **Plan in `v6_plans/`?** — No at Session 0 for all (Stage 1 produces them).
5. **Doc in `v6_completed/`?** — No at Session 0 for all (Stage 2 produces them).
6. **Input substrate present?** — for `new` docs: none expected (authored from canon); for `revise`/`migrate` docs: the v5 plan and (where it exists) the v5 draft or v4 source. Report present/absent.

Add a final row for the historical Document 6: v6 name `Historical_Phase_One_Synthesis.md`, action `preserve` (rename + move, no gate, no plan).

### Task 4 — Write the manifest files

Write two manifest files so the intended structure is visible without creating incomplete content files (the completeness-check gate forbids incomplete files in `v6_completed/`):

- `outputs/v6_plans/MANIFEST.md` — lists all 42 intended plan filenames with their plan action and current status (all "not yet authored" at Session 0).
- `project/source_documents/v6_completed/MANIFEST.md` — lists all 42 intended document filenames plus the historical document, with current status (all "not yet drafted" at Session 0).

Do **not** create empty or placeholder `.md` content files for the documents or plans themselves. The manifests record the structure; the real files are created with full content in Stages 1 and 2.

### Task 5 — Report and checkpoint

Output:

1. **Directories created** — which were created, which already existed.
2. **Input verification** — the present/absent results from Task 2, flagging any missing inputs.
3. **Count reconciliation** — confirm 42 active documents (43 with the historical Document 6); 35 v5 plans found (or report the actual count and any discrepancy against the expected 35); 7 new plans, 12 revised/major, 23 migrated = 42 plans to produce in Stage 1.
4. **The 42-document manifest** from Task 3.
5. **Work queue** — Stage 1: 42 plans (7 new, 12 revised/major, 23 migrated). Stage 2: 42 documents drafted through the completeness-check gate, in phase order.
6. **Missing-input flags** — anything in Task 2 that came back absent and would block Stage 1 or Stage 2.

Then **stop and await confirmation** before beginning Stage 1. Do not author plans.

---

## Do NOT (this session)

- Author any execution plan.
- Draft any document.
- Create empty or placeholder content files for plans or documents (manifests only).
- Reuse any v5 file in place — every v6 plan and document is created fresh under its v6 name in Stages 1 and 2.
- Modify any v5 source file, v5 plan, or v5 draft (they are read-only input).
- Modify the planning documents or conventions.

---

## After This Session

Once the scaffolding is confirmed, Stage 1 authors the 42 v6 execution plans into `outputs/v6_plans/` under the `execution-plan-writing` skill (the 7 new and 12 revised/major are authored with new or revised content; the 23 migrated are content-copied from their v5 plans and renamed, then checked for the ten-section completeness and the self-contained-skill-firing requirement per `CLAUDE.md`). Stage 2 then drafts the 42 documents into `project/source_documents/v6_completed/`, each through the completeness-check gate, in the phase order in `Sixth_Pass_Planning_Document.md` Section IX.
