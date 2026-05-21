# Stage 2 Session Plan — CProj v6 Document Drafting

This file is the operating guide for Stage 2 of the sixth pass: drafting the forty-two active v6 documents from the execution plans in `outputs/v6_plans/`. Stage 1 (all forty-two execution plans) is complete. This plan exists so that any new Claude Code session can pick up Stage 2 without re-deriving context. Read it alongside `CLAUDE.md` (which carries the canonical Stage-2 protocol, the completeness-check gate, and the file-write conventions).

## Branch

All v6 work — the forty-two execution plans and the completed v6 documents — lives on branch **`claude/kickoff-prompt-v6-M03uX`**, pushed to origin. Every Stage-2 session must work on that branch. A session started on any other branch will not see the plans or the completed documents.

## The focused session — unit of work

One session drafts **one document** (or one small clean batch of cross-reference migrations). Each v6 execution plan is fully self-contained, so a session needs only its plan plus the substrate the plan names — not the planning documents.

Per-document workflow inside a session:

1. Read `CLAUDE.md`, then this file.
2. List `project/source_documents/v6_completed/` to see which documents already exist; identify the next document by phase order (the Session Sequence below).
3. Read the document's plan: `outputs/v6_plans/Execution_Plan_<id>_v6.md`.
4. Read the substrate the plan's Section 6 names — the v5 draft and/or v4 source, any relocations holding file in `project/relocations/`, and any already-completed v6 cross-referenced documents in `v6_completed/`.
5. Read a Phase-α exemplar (`I.02`, `I.03`, or `I.04`) for register calibration.
6. Draft directly to `project/source_documents/v6_completed/<id>_v6.md`, engaging every Required Thread at engagement depth, in scholarly register.
7. Run the gate: the filler-density audit (`substantive` under five per one thousand words; no candidate term above its failure threshold), the doubled-word scan (zero genuine artifacts — verified proper-noun repetitions such as "Yorta Yorta" or "Cobble Cobble" are false positives), the cross-reference resolution scan (every "Document X" reference resolves to a real v6 document), the eight-criterion completeness check, and the loss-check.
8. Commit and push; report a per-document checkpoint.

## Three document types — session weights

- **Cross-reference migrations (light).** The seven substantively-drafted v5 exemplars — fifth-pass designations 1, 2, 3, A, M, W, R. Their v5 drafts are complete; the v6 task is to copy the v5 draft, translate every internal cross-reference to v6 form ("Document `<RomanNumeral>.<NN>`"), add a forward-pointer paragraph to the seven new documents and five new threads, and gate. `I.01`–`I.04` are done. **`III.01` (M), `II.08` (W), `XII.01` (R) remain** — each plan carries a "Stage-2 drafting note" stating this explicitly.
- **Substantive drafts from filler-stubs (heavy — the bulk).** The six "moderate depth" documents (fifth-pass 4, B, C, I, K, L) and the roughly twenty-five true stubs. The v5 files are short (≈6–9k words) gestural-padding scaffolds — measured at 14–41 `substantive` hits per one thousand words, the framing-layer-stub signature. Each requires a genuine multi-thread scholarly document drafted to v6 depth. **One focused session per document.** The eleven revised-plan documents additionally weave their Section-X new thread content.
- **New documents (heavy).** The seven sixth-pass additions — `II.09` Climate Displacement, `VI.01` Land, `VI.06` Health, `VI.07` Care, `XII.06` Pedagogy, `XII.07` Harm Response, `XII.08` Labor — drafted from canon, no v5 substrate. One focused session each; `pre-drafting-consultation` fires before drafting.

## Two policies established in the Stage-1/Stage-2 transition

A new session will not know these unless it reads this file:

1. **Migration, not re-drafting, for the seven substantively-drafted exemplars.** Documents 1, 2, 3, A, M, W, R have complete v5 drafts. The v6 task is to migrate the existing draft through the gate — translate cross-references, add forward-pointers (and, for `III.01`/M only, apply the new arts-and-language-and-cultural-production thread as genuine new content) — **not** to re-execute the plan's Section 4–10 task from scratch. Each affected plan carries a Stage-2 drafting note. The other thirty-five documents are drafted substantively from their plans.
2. **`substantive`-density policy for the migrated exemplars.** For the seven migrated exemplars, inherited `substantive` density up to 8 per one thousand words is accepted as faithful migration (move-don't-regenerate governs). Above 8, apply a **targeted `substantive`-reduction pass** — substituting or removing gestural uses only, no analytical rewrite — which the audit protocol explicitly authorizes. `I.01` was accepted at 7.5. `III.01`/M (v5 at 11.3) and the migrations of W and R get the targeted reduction. For documents drafted substantively from stubs, the standard `substantive` < 5 target governs the new prose directly.

## Status

**Complete (committed, pushed):** Stage 0 scaffolding and manifests; all forty-two Stage 1 execution plans; the cross-plan audit and seven Stage-2 plan annotations; Stage 2 documents `I.01`, `I.02`, `I.03`, `I.04`.

**Remaining:** thirty-eight documents.

## Session sequence — strict phase order

Drafting proceeds in the phase order of `Sixth_Pass_Planning_Document.md` Section IX. The fifth-pass designation is given in parentheses for traceability.

- **Phase v6.α** — `I.02` (1), `I.03` (2), `I.04` (3). **Done.**
- **Phase v6.β** — `I.01` (A) **done**; remaining: `II.01` (4), `II.02` (B), `II.03` (C), `VII.01` (I).
- **Phase v6.γ** — `III.01` (M — migration + arts/culture thread), `IV.01` (L), `V.01` (K).
- **Phase v6.δ** — `VI.01` (Land, new), `VI.02` (P), `VI.03` (O), `VI.04` (Q), `VI.05` (N), `VI.06` (Health, new), `VI.07` (Care, new).
- **Phase v6.ε** — `II.04` (S), `II.05` (T), `II.06` (U), `II.07` (V), `II.08` (W — migration), `II.09` (Climate Displacement, new), `VIII.01` (7), `IX.01` (8), `X.01` (9), `XI.01` (10).
- **Phase v6.ζ** — `XII.02` (E), `XII.03` (F), `XII.04` (H), `XII.05` (J), `XII.06` (Pedagogy, new), `XII.07` (Harm Response, new), `XII.08` (Labor, new).
- **Phase v6.η** — `XII.01` (R — migration), `XII.09` (D-1), `XII.10` (D-2), `XII.11` (D-3), `XII.12` (D-4).
- **Phase v6.θ** — `XIII.01` (D-Synthesis).
- **Phase v6.ι** — `XIV.01` (G — capstone; reads the full v6 corpus end-to-end, 1M context load-bearing).

Dependency constraints fixing the order: `III.01` (biocultural-governance ontology) precedes the Part-IV-onward documents that presuppose it; the new Part-VI documents precede `XII.11` (provisioning decision rights); the new Part-XII documents precede the decision-rights cluster and the capstone; `XIII.01` precedes `XIV.01`.

## Checkpoints

Per `CLAUDE.md`: cross-reference-revision documents may be batched up to four per checkpoint; substantive drafts and new documents check in one at a time. Mandatory single-checkpoint for the seven new documents, for `III.01`, `XIII.01`, and `XIV.01`, and for any document where ambiguity arises. Each document additionally carries its eight-criterion completeness-check report at the gate.

## New-session prompt

The simplest prompt is two words: **"continue plan"**. `CLAUDE.md`'s Continue-Plan Protocol defines it — a new session reads `CLAUDE.md`, self-orients (branch, stage, next document in phase order), drafts that document through the gate, commits, pushes, and reports, with no document, file, folder, branch, or phase named by the user. Widen the scope when wanted: "continue plan through Phase v6.γ" or "continue plan until an issue arises."

An explicit prompt also works if a specific document is wanted out of order:

> Draft CProj v6 Stage 2 document **`<id>`** on branch `claude/kickoff-prompt-v6-M03uX`. Read `CLAUDE.md` and `project/Stage2_Session_Plan.md`, then the plan and substrate, draft to `v6_completed/`, pass the gate, commit and push.
