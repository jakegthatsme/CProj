# Targeted Revision Targets — CProj v7 (Phase 7β → Phase 7δ punch list)

*Phase 7β deliverable. The Phase 7δ work specification. Each item names a document (or set), a location signature, the edit, and the category from `Corpus_Tension_Catalog_v7.md`. Phase 7δ edits are surgical (sentence- and paragraph-level cross-reference and prose fixes); no full-document rewrites (a full rewrite would trigger a new `_v7` ordinal, which the seventh-pass plan does not authorize for 7δ). Every item below is either a mechanical prose fix or a verify-then-decide. The `Phase_7delta_Revision_Log.md` records each as landed or explicitly deferred.*

*Items routed to the **v7 capstone (Phase 7γ)** rather than to 7δ surgical edits — the productive analytical tensions (catalog 1A–1D), the consolidated-structure synthesis (catalog 2A integrative portion, 3A, 3C), the war-powers deferral re-flag (3B), and the thread-asymmetry comparison gesture (4A) — are listed in the routing note at the end and are NOT 7δ punch-list items.*

---

## The two canonical fix-patterns (apply across P-1 through P-3)

The 7α cross-reference repair made every reference resolvable but produced two recurring prose artifacts where documents enumerated the now-consolidated clusters as sets or ranges. Phase 7δ replaces them with clean appositive prose:

- **Fix-pattern A — enumerated regime set.** Replace strings of the form
  `Documents II.02, II.02's biological-regime section, II.02's physical-environmental-regime section, II.02's cognitive-and-informational-regime section, and II.02's political-economic-regime section`
  with **"the five regime sections of Document II.02"** — or, where the surrounding sentence needs the regimes named in context, **"Document II.02's cultural, biological, physical-environmental, cognitive-and-informational, and political-economic regime sections."** Choose the shorter form unless the regimes are individually load-bearing in that sentence.

- **Fix-pattern B — broken D-series range.** Replace strings of the form
  `Documents XII.09 through XII.09's cognitive-and-intergenerational scale band`
  with **"the four scale bands of Document XII.09"** — or, where the bands are named in context, **"Document XII.09's foundational, public-check, provisioning, and cognitive-and-intergenerational scale bands."** Also fix enumerated-band sets ("XII.09's … scale band, … XII.09's … scale band") to **"Document XII.09's four scale bands."**

**Do NOT touch clean singleton appositives** — a standalone "Document II.02's biological-regime section" or "Document XII.09's provisioning scale band" is resolvable, precise, and correct. Only the enumerated sets and broken ranges are targets. This keeps 7δ surgical.

---

## P-1 — `II.08_Disturbance_Regime_Interactions_v7` (cross-reference insufficiency 5A) — **9 artifact lines**

The interaction document is the heaviest interaction-hub case because it repeatedly enumerates the five regime diagnostics as a set and refers to the D-series as a range. Apply fix-pattern A to the enumerated regime sets (header metadata line; the "assumes the regime-by-regime diagnostic substance of" line; the dependent-origination passage; the *ayni* passage; the pairwise-pathway citations) and fix-pattern B to "Documents XII.09 through XII.09's cognitive-and-intergenerational scale band" (the "those are the work of …" line). Approximately 9 sentence-level edits. Preserve all analytical content; change only the reference prose. Verify after editing that the dependent-origination and *ayni* passages still read with the regimes named where the argument needs them (those two passages name the regimes individually in service of the argument — use the named-in-context variant of fix-pattern A there).

## P-2 — `III.01_Biocultural_Governance_v7` (cross-reference insufficiency 5B) — **10 artifact lines**

The ontology document is the heaviest single case (10 artifact lines). Read the affected passages in full first (the document is large, ~32K words; do not rewrite — locate the artifact lines by the fix-pattern signatures and edit only those). Apply fix-patterns A and B. Because `III.01` is the load-bearing ontology and is referenced corpus-wide, give its repaired references priority and verify each edited sentence reads cleanly.

## P-3 — Corpus-wide artifact sweep (cross-reference insufficiency 5A/5B) — **~19 further documents**

Apply fix-patterns A and B to the remaining documents carrying artifact lines, detected by the signature grep. Per the Phase-7β detection run, the affected documents and approximate artifact-line counts are:

| Document | artifact lines | patterns |
|---|---|---|
| `XII.01_Eco_Mimetic_Policy_Making_v7` | 6 | A, B, enumerated-band set |
| `VIII.01_Minds_Markets_Sacred_v7` | 4 | B (and A) |
| `I.02_Founding_Texts_and_1787_Implementation_v7` | 3 | B |
| `II.03_Oligarchy_and_Dark_Money_v7` | 3 | A, B |
| `II.09_Climate_Displacement_and_Belonging_v7` | 3 | A, B |
| `IX.01_Constitutional_Climate_Redesign_v7` | 3 | B |
| `V.01_CAS_Emergence_Adaptive_Governance_v7` | 3 | B |
| `VI.04_Cradle_to_Cradle_v7` | 3 | B |
| `I.01_Declaration_as_Foundation_v7` | 2 | A, B |
| `I.03_Federalist_AntiFederalist_Records_v7` | 2 | B |
| `VI.02_Food_Soil_Agriculture_v7` | 2 | B |
| `VI.06_Health_as_Cultivation_v7` | 2 | B |
| `II.01`, `IV.01`, `VI.01`, `VI.03`, `VI.05`, `VI.07`, `VII.01` | 1 each | A or B |

Detection command (run at the start of 7δ to regenerate the live list, since counts may shift as edits land):
```
grep -rnE "II\.02's [a-z-]+-regime section, |XII\.09 through XII\.09's|XII\.09's [a-z-]+ scale band, |II\.02, II\.02's" project/source_documents/v7_completed/
```
Each is 1–6 sentence-level edits. Total corpus-wide artifact load is roughly 50 lines across ~21 documents (including P-1 and P-2). All are mechanical applications of fix-patterns A and B; none is a rewrite.

## P-4 — Stale provenance-label metadata (cross-reference insufficiency 5C) — **optional, batchable**

Each rebadged document's header note carries a "Sixth-pass position-based name: `<name>_v7`" label and v6-venue output-path metadata now bearing `_v7`/`v6_completed` mixed tokens. These are cosmetic (they resolve to nothing and do not orphan). **Optional.** If undertaken, batch as a single mechanical pass updating "Sixth-pass position-based name" → "Seventh-pass position-based name" and dropping the dead venue output-path lines. Defer unless the other punch-list items leave room; record as deferred in the revision log if not done.

## P-5 — `IV.01_Deep_Substrate` thin-vs-rich verification (thin-vs-rich 4C) — **[verify] then decide**

Read `IV.01` in full and scan its downstream uptake (how often and how substantively the deep-substrate meta-rights are invoked in Parts VI, XII, XIII). If the foundation is genuinely load-bearing but under-integrated, a one-to-two-sentence strengthening of the downstream invocation in `XIII.01` (the synthesis hub) is the surgical fix. If the cross-citation treatment is adequate to a foundational document, record as verified-adequate, no edit. Decide in 7δ; do not pre-commit an edit.

## P-6 — Eastern-articulator depth verification (thin-vs-rich 4B) — **[verify] then route**

Confirm the asymmetry between the stated co-equal Eastern/Indigenous standing and the realized Eastern analytical depth by a full read of the documents not yet read end-to-end (the I-series, Part VI, Part X, Part XI). If specific passages name Eastern traditions as a list where the argument warrants engaged apparatus, a surgical one-paragraph strengthening at the thinnest site is the 7δ fix. **Most of this item routes to the v7 capstone (Phase 7γ)** rather than to 7δ: the capstone's multi-traditional-canon thread (the Thread E equivalent) is the natural place to name the asymmetry honestly at synthesis standing. Record the verification finding; route the naming to 7γ and any single surgical strengthening to 7δ.

---

## Routed to the v7 capstone (Phase 7γ), NOT to 7δ surgical edits

These catalog items are integrative-synthesis work for the v7 capstone and are recorded here only to ensure the capstone plan picks them up; they are **not** 7δ punch-list edits:

- **1A–1D (productive analytical tensions):** performed at synthesis standing in the v7 capstone (cultivation-vs-design; renovation-vs-decolonial settled-but-live; disturbance-regime-vs-structural-commitment framing incommensurability; the specific cross-tradition seams).
- **2A integrative portion + 3A + 3C (the consolidated-structure synthesis):** the v7 capstone is the first and only document that reads the corpus at its consolidated 35-document structure, and it draws the implicit regime-to-scale-band mapping (`II.02`'s five regimes ↔ `XII.09`'s four scale bands, bridged by `II.08`'s cross-regime feedback conditions).
- **3B (war-powers deferral):** the v7 capstone re-flags defense-and-war-powers as eighth-pass-or-later candidate work, carrying forward the v6 capstone's Thread G flag rather than silently dropping it.
- **4A (thread asymmetry):** the v7 capstone's comparison-gesture work registers the defense-and-war-powers thread's thinness explicitly rather than presenting the five sixth-pass threads as evenly developed.

---

## Phase 7δ completion criterion

Phase 7δ is complete when: every P-1 through P-3 artifact line is repaired (re-run the detection grep → zero enumerated-set/broken-range artifacts; clean singleton appositives remain and are acceptable); P-4 is landed or explicitly deferred; P-5 and P-6 are verified-and-decided (edit landed or recorded as verified-adequate/routed-to-7γ); and `Phase_7delta_Revision_Log.md` records every item's disposition. No edit in 7δ alters analytical content or triggers a filename change.
