# Formulaic-Thinness Audit — CProj v6 Operating Protocol

This protocol supplements the filler-discipline audit (`CLAUDE.md` Self-Audit Protocols) at the document gate. The filler-discipline audit catches one failure mode — gestural padding inflating word count without analytical content (the "substantive" / "analytical" / "framing" density metric). The formulaic-thinness audit catches a complementary failure mode — *deflation* in which the formal apparatus (the four-element specification format; cross-citation to other documents; named-articulator lists) replaces analytical engagement, producing a draft that passes the filler audit because it is short and unpadded but reads as enumerated scaffold rather than as scholarly engagement.

The audit operationalizes a single discipline: every Required Thread that the plan designates for substantive engagement must do analytical work that a reader could not produce from the plan alone. A thread that recapitulates the plan's specification format without engaging the named literature, traditions, and primary articulators at scholarly depth fails — even if its filler density is exemplary.

## Failure Modes the Audit Catches

**Sub-right compression.** A thread enumerates multiple sub-rights or cluster elements (e.g., the seven Part-VI material-substrate cluster in `XII.11`; the multi-lens lenses in `XII.12`; a comparative-cases archive) and compresses each element into a single labelled-clause sentence ("scope — X; scale — Y; feedback — Z; sunset — W") rather than dedicating substantive specification to each element.

**Cross-citation-without-depth.** A thread permitted to cross-cite substantive content from another document satisfies the cross-citation but does not do the analytical work the cross-citation enables. The pattern "Document X specifies the substantive content; the present document specifies the formal architecture" is acceptable only if the formal-architecture work is then performed, not gestured at.

**Articulator listing without engagement.** Primary articulators named in the plan appear in the references list and in single-mention sentences ("the X tradition operating at primary-articulator standing") without being engaged with author, year, work title, and specific analytical claim attributed.

**Movement-and-tradition gesturing.** References to literatures, movements, or traditions appear without a single named work or articulator from the named literature/movement/tradition. "The broader X movement" suffices for scope-noting but not for engaged-at-primary-articulator-standing.

**Four-element-clause replacement.** The four-element specification format (scope/scale/feedback/sunset) collapses from paragraph-structuring apparatus into sentence-replacement apparatus, with each element reduced to a single noun phrase and the analytical specification displaced by the formal scaffold itself.

**Multi-element architecture as list.** Where the document specifies a multi-element commitment (multi-lens checks-and-balances; multi-tradition primary-articulator engagement; multi-criterion review architecture), each named element appears as cross-citation to its source document rather than receiving engagement in its own right.

## Diagnostic Measures

For each Required Thread, the audit computes the following:

1. **Scholar-engagement density.** Count named-scholar-year-work tuples (author named, publication year named, work title named) in the thread body. Target: ≥ 3 per substantive Required Thread; ≥ 1 per primary articulator named in the plan. A thread with fewer than 3 tuples or with named-plan-articulators missing from the body fails this check unless the thread is explicitly a synthesis or closing thread.

2. **Sub-right paragraph depth.** Where a thread enumerates ≥ 3 sub-rights or cluster elements, count words in each element's dedicated specification. Target: ≥ 150 words per element for analytical depth; < 100 words signals formulaic enumeration. A thread with > 50 percent of its enumerated elements under 100 words fails this check.

3. **Four-element-collapsed-clause sentences.** Count sentences that compress the four-element specification into a single labelled-clause sequence. Target: ≤ 2 per thread, used as overview or for sub-rights explicitly cross-cited to other documents. A thread with > 3 collapsed-clause sentences as its principal apparatus fails this check.

4. **Cross-citation ratio.** Compute the ratio of cross-citation sentences ("Document X specifies", "Document Y carries", "as articulated in Document Z") to original analytical sentences in the thread body. Target: cross-citation under 25 percent; > 40 percent signals cross-citation-without-depth.

5. **Tradition-and-movement concreteness.** For each tradition or movement named in the thread, verify at least one named work or articulator from that tradition/movement appears in the thread body. References to "the broader X movement" / "the X tradition" without any named instance fail this check.

A suggested bash one-liner for measures 1, 3, and 4:

```bash
f=<thread excerpt path or document path>
# Named-scholar-year tuples: rough heuristic — surname + parenthetical year
echo "named-scholar-year tuples (rough):"
grep -oE "[A-Z][a-zA-Z'-]+(\s+[A-Z][a-zA-Z'-]+)*'s\s+\*[^*]+\*\s+\([^)]*[0-9]{4}[^)]*\)" "$f" | wc -l
# Four-element-collapsed-clause sentences: pattern "scope ... scale ... feedback ... sunset"
echo "four-element-collapsed-clause sentences:"
grep -cE "[Ss]cope\s*[—-].*scale\s*[—-].*feedback.*sunset" "$f"
# Cross-citation sentences
echo "cross-citation sentence count:"
grep -cE "Document [IVX]+\.[0-9]+\s+(specifies|carries|articulates|operates)" "$f"
```

## Application at the Document Gate

The eight-criterion completeness-check gate (`CLAUDE.md` Self-Audit Protocols) is extended to a ninth criterion:

9. **The formulaic-thinness audit passes**: each Required Thread that the plan designates for substantive engagement meets the diagnostic-measures thresholds above; sub-right enumerations carry substantive paragraphs; named primary articulators are engaged with author-year-work tuples and attributed analytical claims; cross-citations add formal-architectural work beyond the cross-citation itself.

A document that fails the formulaic-thinness audit does not enter `v6_completed/` until the failing threads are remediated. Remediation deepens — does not pad — the failing threads: adds substantive engagement with named primary articulators; expands enumerated sub-rights to paragraph depth where the rights are the document's analytical content; replaces four-element-collapsed-clause sentences with substantive specification of each element where the right is the document's analytical apex; adds the analytical move the cross-citation enables.

## Exemptions

The audit does not apply to:

- **Migration documents** (the seven substantively-drafted fifth-pass exemplars: `I.01`, `I.02`, `I.03`, `I.04`, `III.01`, `II.08`, `XII.01`), which are governed by the move-don't-regenerate principle. The fifth-pass draft's analytical depth is the baseline; the migration's task is cross-reference translation and forward-pointer addition, not new analytical depth.
- **Opening and closing synthesis threads** that explicitly position the document within the broader arc rather than carrying substantive content of their own. These threads can be brief without failing the audit.
- **Plan-specified cross-citation threads** where the plan explicitly states the thread cross-cites without re-derivation. Even here, the cross-citation must add the analytical move at the document's own register (the bounded-decision-right register for the D-series; the cultivation-condition register for Part-XII documents; etc.); a thread that cross-cites without doing any work at its own register fails.

## Audit Order

At the document gate, audits run in this order:

1. Filler-discipline audit (catches padding).
2. Doubled-word scan (catches inline-cleanup artifacts).
3. Cross-reference resolution scan (every Document X reference resolves to a real v6 document).
4. Formulaic-thinness audit (catches deflation-as-enumeration).
5. Loss-check (catches dropped threads, articulators, cross-references).
6. Drift-check (catches register and triad drift).
7. Eight-criterion completeness check (extended to ninth criterion per this protocol).

A document passes when all seven audits pass and the eight-plus-one criteria hold.
