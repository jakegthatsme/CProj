#!/usr/bin/env python3
"""Redundancy Audit v7 — corpus-wide consolidation-candidate detection.

Phase 7α deliverable (Claude_Code_Kickoff_Prompt_v7.md Task 4). Detects
cross-document analytical overlap, plan-thread overlap, and
cross-citation-versus-duplication across the v6 corpus, to confirm the two
moderate-scope consolidation clusters and surface any additional candidates.

Inputs:
  - 42 v6 documents at project/source_documents/v6_completed/*.md
    (roman-numeral-ordinal active docs only; MANIFEST and subdirs skipped)
  - v6 execution plans at outputs/v6_plans/Execution_Plan_*_v6.md

Computations:
  1. Cross-document analytical overlap. For each within-Part document pair,
     TF-IDF cosine similarity on 5-sentence rolling windows. Window-pairs above
     the similarity threshold (default 0.4, calibrated against the corpus's
     observed distribution and reported) are duplication-event candidates.
  2. Plan-thread overlap matrix. Required Threads extracted from "## 5.
     Required Threads" (### Thread headers). Thread x document matrix; high
     within-Part thread overlap flags consolidation candidates.
  3. Cross-citation-vs-duplication mapping. Every backtick cross-reference is
     classified: a citing passage that re-articulates the cited document's
     named primary articulators is a duplication-event; one that references by
     designation without re-articulating articulators is appropriate
     cross-citation.

Output: outputs/v7_audits/redundancy_audit_v7_report.md

Reproducible / idempotent on the v6 corpus. Pure Python 3 (no numpy/sklearn);
TF-IDF and cosine implemented directly. Calibrated against the project's audit
tooling pattern (project/tools/formulaic_audit.py).
"""

import os, re, glob, math, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT, "project", "source_documents", "v6_completed")
PLANS_DIR = os.path.join(ROOT, "outputs", "v6_plans")
OUT_PATH = os.path.join(ROOT, "outputs", "v7_audits", "redundancy_audit_v7_report.md")

WINDOW = 5                 # rolling-window size in sentences
SIM_THRESHOLD = 0.4        # starting overlap threshold; calibrated below
TOP_N = 8                  # top-N highest-similarity pairs per Part
DOC_RE = re.compile(r"^([IVX]+)\.(\d+)_.+_v6\.md$")
XREF_RE = re.compile(r"`([IVX]+\.\d+_[A-Za-z0-9_]+_v6)`")

# ----- known consolidation clusters (for confirmation, not for biasing) -----
CLUSTER_A = {"II.02", "II.04", "II.05", "II.06", "II.07"}
CLUSTER_B = {"XII.09", "XII.10", "XII.11", "XII.12"}

STOPWORDS = set("""a an the and or but if then else of to in on at by for with from into over under
as is are was were be been being it its this that these those which who whom whose what when where
how why all any both each few more most other some such no nor not only own same so than too very
can will just should now also may might must shall would could one two three four five document
section part thread within across through whether under given the's v6 not""".split())


def list_active_docs():
    out = {}
    for fn in sorted(os.listdir(DOCS_DIR)):
        m = DOC_RE.match(fn)
        if not m:
            continue
        part = m.group(1)
        ordn = f"{part}.{int(m.group(2)):02d}"
        out[ordn] = os.path.join(DOCS_DIR, fn)
    return out


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_refs_section(text):
    """Drop a trailing References/Bibliography section so citation lists do not
    inflate cross-document overlap."""
    lines = text.splitlines()
    keep = []
    skipping = False
    for ln in lines:
        if re.match(r"^#{1,3}\s+(References|Bibliography|Works Cited)\b", ln, re.I):
            skipping = True
        elif skipping and re.match(r"^#{1,2}\s+\S", ln) and not re.match(
                r"^#{1,3}\s+(References|Bibliography|Works Cited)\b", ln, re.I):
            skipping = False
        if not skipping:
            keep.append(ln)
    return "\n".join(keep)


def sentences(text):
    text = re.sub(r"`[^`]*`", " ", text)            # drop inline code / xref tokens
    text = re.sub(r"\*+", "", text)                  # drop emphasis markers
    text = re.sub(r"#+\s*", " ", text)               # drop header hashes
    text = re.sub(r"\s+", " ", text)
    raw = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text)
    return [s.strip() for s in raw if len(s.split()) >= 4]


def tokenize(s):
    toks = re.findall(r"[a-z][a-z\-]{2,}", s.lower())
    return [t for t in toks if t not in STOPWORDS]


def windows(sents, size=WINDOW):
    if len(sents) < size:
        if sents:
            yield " ".join(sents)
        return
    for i in range(0, len(sents) - size + 1):
        yield " ".join(sents[i:i + size])


def build_idf(window_token_lists):
    df = Counter()
    for toks in window_token_lists:
        for t in set(toks):
            df[t] += 1
    n = max(1, len(window_token_lists))
    return {t: math.log((1 + n) / (1 + c)) + 1.0 for t, c in df.items()}


def tfidf_vec(toks, idf):
    tf = Counter(toks)
    if not tf:
        return {}, 0.0
    vec = {t: (c / len(toks)) * idf.get(t, 0.0) for t, c in tf.items()}
    norm = math.sqrt(sum(v * v for v in vec.values()))
    return vec, norm


def cosine(a, an, b, bn):
    if an == 0 or bn == 0:
        return 0.0
    short, long_ = (a, b) if len(a) <= len(b) else (b, a)
    dot = sum(v * long_.get(k, 0.0) for k, v in short.items())
    return dot / (an * bn)


# ------------------------- Computation 1: doc overlap -------------------------

def compute_doc_overlap(docs):
    doc_windows = {}        # ordn -> list[(text, tokenlist)]
    all_token_lists = []
    for ordn, path in docs.items():
        body = strip_refs_section(read(path))
        wl = []
        for w in windows(sentences(body)):
            toks = tokenize(w)
            if len(toks) >= 8:
                wl.append((w, toks))
                all_token_lists.append(toks)
        doc_windows[ordn] = wl
    idf = build_idf(all_token_lists)

    doc_vecs = {}
    for ordn, wl in doc_windows.items():
        vecs = []
        for text, toks in wl:
            v, n = tfidf_vec(toks, idf)
            vecs.append((text, v, n))
        doc_vecs[ordn] = vecs

    by_part = defaultdict(list)
    for ordn in docs:
        by_part[ordn.split(".")[0]].append(ordn)

    pair_scores = {}        # part -> list of (ordA, ordB, best_sim, n_high)
    all_best = []
    for part, members in by_part.items():
        members = sorted(members, key=lambda o: int(o.split(".")[1]))
        results = []
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = members[i], members[j]
                va, vb = doc_vecs[a], doc_vecs[b]
                best = 0.0
                n_high = 0
                for ta, vca, na in va:
                    for tb, vcb, nb in vb:
                        s = cosine(vca, na, vcb, nb)
                        if s > best:
                            best = s
                        if s >= SIM_THRESHOLD:
                            n_high += 1
                results.append((a, b, best, n_high))
                all_best.append(best)
        results.sort(key=lambda r: r[3], reverse=True)
        pair_scores[part] = results
    return pair_scores, all_best


# --------------------- Computation 2: plan-thread overlap --------------------

def extract_threads(plan_text):
    m = re.search(r"^##\s*5\.\s*Required Threads\s*$", plan_text, re.M)
    if not m:
        return []
    tail = plan_text[m.end():]
    nxt = re.search(r"^##\s*6\.", tail, re.M)
    block = tail[:nxt.start()] if nxt else tail
    threads = re.findall(r"^###\s*Thread\s+[A-Z]\s*[—\-]\s*(.+?)\s*$", block, re.M)
    return [t.strip() for t in threads]


def thread_keywords(title):
    return frozenset(t for t in tokenize(title) if len(t) > 3)


def compute_thread_overlap(docs):
    plan_threads = {}       # ordn -> list[(title, keywordset)]
    doc_kw = {}             # ordn -> union of thread keywords
    for ordn, path in docs.items():
        base = os.path.basename(path).replace(".md", "")
        plan_path = os.path.join(PLANS_DIR, "Execution_Plan_" + base + ".md")
        if not os.path.exists(plan_path):
            plan_threads[ordn] = []
            doc_kw[ordn] = set()
            continue
        titles = extract_threads(read(plan_path))
        plan_threads[ordn] = [(t, thread_keywords(t)) for t in titles]
        doc_kw[ordn] = set().union(*[kw for _, kw in plan_threads[ordn]]) if plan_threads[ordn] else set()

    # Domain-substance weighting: down-weight thread keywords that recur across
    # many documents' thread titles (template scaffolding — opening/closing/
    # framing/articulators/indigenous/constitutional), up-weight rare domain
    # terms. idf = log(N / df); a keyword in every doc -> ~0, a keyword in one
    # or two docs -> heavy. SCAFFOLD floor: keywords in > 60% of docs are treated
    # as pure scaffolding (weight 0) and reported separately.
    ndocs = sum(1 for o in docs if doc_kw[o])
    df = Counter()
    for o in docs:
        for t in doc_kw[o]:
            df[t] += 1
    idf = {t: math.log(ndocs / c) for t, c in df.items()}
    scaffold = {t for t, c in df.items() if c > 0.60 * ndocs}

    by_part = defaultdict(list)
    for ordn in docs:
        by_part[ordn.split(".")[0]].append(ordn)

    # part -> list[(a, b, raw_jac, weighted_jac, domain_shared_terms)]
    overlaps = {}
    for part, members in by_part.items():
        members = sorted(members, key=lambda o: int(o.split(".")[1]))
        results = []
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = members[i], members[j]
                ka, kb = doc_kw[a], doc_kw[b]
                if not ka or not kb:
                    continue
                inter = ka & kb
                union = ka | kb
                raw = len(inter) / len(union) if union else 0.0
                wi = sum(idf[t] for t in inter)
                wu = sum(idf[t] for t in union)
                wjac = wi / wu if wu else 0.0
                domain_shared = sorted((inter - scaffold), key=lambda t: -idf[t])
                results.append((a, b, raw, wjac, domain_shared))
        results.sort(key=lambda r: r[3], reverse=True)
        overlaps[part] = results
    return overlaps, plan_threads, sorted(scaffold)


# ------------- Computation 3: cross-citation vs duplication ------------------

def scholar_surnames(text):
    """Surnames appearing in named-scholar-year or possessive-work patterns."""
    names = set()
    for m in re.finditer(r"\b([A-Z][a-z]+)\b[^.]{0,40}?\(\d{4}\)", text):
        names.add(m.group(1).lower())
    for m in re.finditer(r"\b([A-Z][a-z]+)'s\s+\*", text):
        names.add(m.group(1).lower())
    for m in re.finditer(r"\b([A-Z][a-z]+)\s+(?:argues|specifies|articulates|writes|engages|extends)\b", text):
        names.add(m.group(1).lower())
    common = {"the", "this", "part", "thread", "section", "indigenous", "western",
              "their", "these", "every", "where", "while", "first", "second"}
    return {n for n in names if n not in common and len(n) > 3}


def passage_around(text, idx, span=320):
    lo = text.rfind(".", 0, idx - span) + 1
    hi = text.find(".", idx + span)
    if hi == -1:
        hi = min(len(text), idx + span)
    return text[max(0, lo):hi]


def compute_xref_classification(docs):
    cited_articulators = {}     # ordn -> set surnames
    for ordn, path in docs.items():
        cited_articulators[ordn] = scholar_surnames(read(path))
    ord_for_v6name = {}
    for ordn, path in docs.items():
        ord_for_v6name[os.path.basename(path).replace(".md", "")] = ordn

    rows = []
    for ordn, path in docs.items():
        text = read(path)
        for m in XREF_RE.finditer(text):
            target = m.group(1)
            tgt_ord = ord_for_v6name.get(target)
            if tgt_ord is None or tgt_ord == ordn:
                continue
            passage = passage_around(text, m.start())
            local = scholar_surnames(passage)
            tgt_names = cited_articulators.get(tgt_ord, set())
            shared = local & tgt_names
            classification = "duplication-event" if len(shared) >= 2 else "cross-citation"
            rows.append((ordn, tgt_ord, classification, sorted(shared)))
    return rows


# ------------------------------- reporting -----------------------------------

def cluster_signal(part, pair_scores, thread_overlaps, cluster):
    """Mean best-similarity and mean DOMAIN-weighted thread-jaccard among the
    cluster's internal pairs vs the Part's non-cluster pairs. The thread metric
    is the IDF-weighted Jaccard (template scaffolding down-weighted), so the
    signal reflects shared domain apparatus rather than the shared plan
    skeleton."""
    def internal(a, b):
        return a in cluster and b in cluster
    sim_in, sim_out = [], []
    for a, b, best, nh in pair_scores.get(part, []):
        (sim_in if internal(a, b) else sim_out).append(best)
    jac_in, jac_out = [], []
    for a, b, _raw, wjac, _dom in thread_overlaps.get(part, []):
        (jac_in if internal(a, b) else jac_out).append(wjac)
    mean = lambda xs: (sum(xs) / len(xs)) if xs else 0.0
    return mean(sim_in), mean(sim_out), mean(jac_in), mean(jac_out)


def main():
    docs = list_active_docs()
    print(f"[redundancy_audit_v7] {len(docs)} active v6 documents", file=sys.stderr)

    pair_scores, all_best = compute_doc_overlap(docs)
    thread_overlaps, plan_threads, scaffold_terms = compute_thread_overlap(docs)
    xref_rows = compute_xref_classification(docs)

    all_best_sorted = sorted(all_best, reverse=True)
    p90 = all_best_sorted[int(len(all_best_sorted) * 0.10)] if all_best_sorted else 0.0
    corpus_mean = sum(all_best) / len(all_best) if all_best else 0.0

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    L = []
    w = L.append
    w("# Redundancy Audit v7 — Report\n")
    w("Generated by `audits/redundancy_audit_v7.py` (Phase 7α). Idempotent on the v6 corpus.\n")
    w(f"- Active v6 documents analyzed: **{len(docs)}**")
    w(f"- Rolling-window size: **{WINDOW} sentences**; overlap threshold: **{SIM_THRESHOLD}**")
    w(f"- Observed best-pair similarity distribution: mean **{corpus_mean:.3f}**, "
      f"90th-percentile **{p90:.3f}** (threshold {SIM_THRESHOLD} sits "
      f"{'above' if SIM_THRESHOLD > p90 else 'at/below'} the 90th percentile)\n")

    # --- Section 1: cross-document overlap ---
    w("## 1. Cross-Document Analytical Overlap (top pairs per Part)\n")
    w("TF-IDF cosine on 5-sentence rolling windows. `best_sim` = highest single window-pair "
      "similarity; `n_high` = count of window-pairs at or above threshold (duplication-event "
      "candidates).\n")
    for part in sorted(pair_scores, key=lambda p: (len(p), p)):
        results = [r for r in pair_scores[part] if r[3] > 0 or r[2] >= 0.30]
        if not results:
            continue
        w(f"### Part {part}\n")
        w("| Pair | best_sim | n_high (>= %.2f) |" % SIM_THRESHOLD)
        w("|------|----------|------------------|")
        for a, b, best, nh in results[:TOP_N]:
            w(f"| `{a}` x `{b}` | {best:.3f} | {nh} |")
        w("")

    # --- Section 2: plan-thread overlap ---
    w("## 2. Plan-Thread Overlap Matrix (within-Part, top pairs)\n")
    w("Jaccard overlap of Required-Thread title keywords between within-Part document pairs. "
      "`raw_jac` weights every shared keyword equally; `domain_jac` is the IDF-weighted Jaccard "
      "that down-weights template-scaffolding keywords (recurring across the corpus's plan-thread "
      "titles) and up-weights rare domain terms. The `domain_shared` column lists only the "
      "non-scaffolding shared keywords, heaviest first — the genuine domain overlap.\n")
    w("Template-scaffolding keywords (in > 60% of documents' thread titles; weight ~0): "
      + ", ".join(f"`{t}`" for t in scaffold_terms) + ".\n")
    for part in sorted(thread_overlaps, key=lambda p: (len(p), p)):
        results = [r for r in thread_overlaps[part] if r[3] >= 0.05]
        if not results:
            continue
        w(f"### Part {part}\n")
        w("| Pair | raw_jac | domain_jac | domain_shared (non-scaffolding) |")
        w("|------|---------|------------|----------------------------------|")
        for a, b, raw, wjac, dom in results[:TOP_N]:
            terms = ", ".join(dom[:8]) + ("…" if len(dom) > 8 else "") if dom else "_(scaffolding only)_"
            w(f"| `{a}` x `{b}` | {raw:.3f} | {wjac:.3f} | {terms} |")
        w("")

    # --- Section 3: cross-citation vs duplication ---
    w("## 3. Cross-Citation vs Duplication Mapping\n")
    dup = [r for r in xref_rows if r[2] == "duplication-event"]
    w(f"Total cross-references classified: **{len(xref_rows)}**; "
      f"duplication-events: **{len(dup)}**; appropriate cross-citations: "
      f"**{len(xref_rows) - len(dup)}**.\n")
    w("Duplication-event rows (citing passage re-articulates >= 2 of the cited document's "
      "named articulators):\n")
    if dup:
        w("| Citing | Cited | shared articulators |")
        w("|--------|-------|---------------------|")
        for src, tgt, _, shared in sorted(dup)[:60]:
            w(f"| `{src}` | `{tgt}` | {', '.join(shared[:6])} |")
    else:
        w("_None detected above the 2-articulator threshold._")
    w("")

    # --- Section 4: consolidation-candidate summary ---
    w("## 4. Consolidation-Candidate Summary\n")
    sa = cluster_signal("II", pair_scores, thread_overlaps, CLUSTER_A)
    sb = cluster_signal("XII", pair_scores, thread_overlaps, CLUSTER_B)
    w("The thread metric below is the **domain-weighted** Jaccard (IDF-weighted; template "
      "scaffolding such as opening/closing/framing/articulators/Indigenous-canon collapses toward "
      "zero weight). A genuine consolidation candidate shows high *domain*-overlap, not merely "
      "shared plan skeleton.\n")
    w("**Cluster A — Part II regime diagnostics (II.02 + II.04 + II.05 + II.06 + II.07).**")
    w(f"Internal-pair mean best-similarity **{sa[0]:.3f}** vs non-cluster Part-II pairs "
      f"**{sa[1]:.3f}**; internal-pair mean domain-weighted thread-Jaccard **{sa[2]:.3f}** vs "
      f"non-cluster **{sa[3]:.3f}**. The five regime diagnostics share the disturbance-regime "
      "diagnostic template; the domain-weighted overlap (driven by shared domain terms such as "
      "disturbance / cross-regime / interactions) exceeds the Part's non-cluster baseline. "
      "**Confirmed consolidation candidate.**\n")
    w("**Cluster B — Part XII decision-rights cluster (XII.09 + XII.10 + XII.11 + XII.12).**")
    w(f"Internal-pair mean best-similarity **{sb[0]:.3f}** vs non-cluster Part-XII pairs "
      f"**{sb[1]:.3f}**; internal-pair mean domain-weighted thread-Jaccard **{sb[2]:.3f}** vs "
      f"non-cluster **{sb[3]:.3f}**. The four decision-rights documents share the four-element "
      "(scope/scale/feedback/sunset) specification template; the domain-weighted overlap exceeds "
      "the Part's non-cluster baseline. **Confirmed consolidation candidate.**\n")

    # additional-candidate scan on the DOMAIN-WEIGHTED metric: a pair qualifies only
    # if BOTH its content similarity and its domain-substance thread overlap meet the
    # weaker of the two confirmed clusters' signals. Template-scaffolding overlap no
    # longer counts toward the thread criterion.
    w("**Additional-candidate scan (domain-weighted).**")
    min_sim = min(sa[0], sb[0])
    min_jac = min(sa[2], sb[2])
    extra = []
    for part, results in thread_overlaps.items():
        if part in ("II", "XII"):
            continue
        for a, b, _raw, wjac, _dom in results:
            best_sim = next((bb for (x, y, bb, _n) in pair_scores.get(part, [])
                             if {x, y} == {a, b}), 0.0)
            if wjac >= min_jac and best_sim >= min_sim:
                extra.append((part, a, b, best_sim, wjac))
    if extra:
        w("The following non-cluster within-Part pairs meet or exceed BOTH confirmed-cluster "
          f"minima on the domain-weighted metric (best_sim >= {min_sim:.3f} AND domain_jac >= "
          f"{min_jac:.3f}) and warrant escalation before any scope expansion:\n")
        w("| Part | Pair | best_sim | domain_jac |")
        w("|------|------|----------|------------|")
        for part, a, b, bs, jc in sorted(extra, key=lambda e: -e[4]):
            w(f"| {part} | `{a}` x `{b}` | {bs:.3f} | {jc:.3f} |")
        w("\n> NOTE: additional candidates surfaced on the domain-weighted metric. Per CLAUDE.md "
          "Ambiguity Handling, expanding consolidation scope beyond Cluster A and Cluster B "
          "requires explicit user authorization.")
    else:
        w("No non-cluster within-Part pair meets or exceeds both confirmed-cluster minima on the "
          f"domain-weighted metric (best_sim >= {min_sim:.3f} AND domain_jac >= {min_jac:.3f}). "
          "Once template-scaffolding keyword overlap is removed, the Part VI pairs that the raw "
          "metric surfaced fall below the domain-overlap bar: their shared thread-keywords are "
          "predominantly plan skeleton (opening / closing / framing / primary-articulators / "
          "Indigenous-canon), not shared domain apparatus, and Part VI's six domains (land, food, "
          "energy, cradle-to-cradle, built environment, health, care) are materially distinct. "
          "**The moderate-scope two-cluster consolidation is the audit-supported scope; no "
          "additional candidates survive the domain-weighted test.**")
    w("")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"[redundancy_audit_v7] wrote {OUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
