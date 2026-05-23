#!/usr/bin/env python3
"""Formulaic-Thinness Audit v3 — improved heuristics.

Improvements over v2:
  1. Broader scholar/source detection
     - *Italic Title* (...Year...)
     - "Quoted Title" (...Year...)
     - Possessive Author's *Work* (no year required)
     - "Author argues/specifies/articulates/extends/engages/writes" attribution
     - Inline (Year) after possessive
     - Acts/Treaties/Conventions: "X Act of YYYY", "X Convention YYYY",
       "Constitution of X (YYYY)", *Federalist* No. N, court citations
  2. Concrete-instance density
     - Named acts/treaties/conventions/declarations/covenants/protocols/directives + year
     - Named institutions/movements with founding year
     - Court cases (named-v-named with optional reporter)
     - Federalist Papers
  3. Severity scoring:
     - engagement = scholar_signals + 0.5 * concrete_instances
  4. Plan-aware check:
     - reads outputs/v6_plans/Execution_Plan_<id>_*_v6.md
     - extracts plan-named scholars from Section 5/6; verifies each appears in body
  5. Better label parsing and Part vs Thread vs Section detection
"""

import os, re, glob, sys

MIGRATION_DOCS = {"I.01", "I.02", "I.03", "I.04", "III.01", "II.08", "XII.01"}

def is_exempt_thread(label: str) -> bool:
    s = label.lower()
    return any(k in s for k in [
        "closing", "opening", "synthesis", "references",
        "introduction", "outro", "bibliography", "appendix"
    ])

def is_top_level_part_header(label: str, body: str) -> bool:
    s = label.lower().strip()
    if not (s.startswith("part ") or s.startswith("section ")):
        return False
    body_clean = re.sub(r"^\s*$\n?", "", body, flags=re.MULTILINE)
    if len(body_clean.split()) < 100:
        return True
    return False


def count_scholar_signals(body: str):
    """Return dict of citation-style counts (deduplicated)."""
    italic_tuples = set()
    quoted_tuples = set()
    possessive_works = set()
    named_scholars = set()
    attributions = set()

    # 1. *Italic Title* (...Year...)
    for m in re.finditer(r"\*([^*]{3,200})\*\s*\(([^)]*)\b((?:1[6-9]|20)\d{2})\b([^)]*)\)", body):
        title = m.group(1).strip().lower()[:80]
        italic_tuples.add((title, m.group(3)))

    # 2. "Quoted Title" (...Year...)
    for m in re.finditer(r'"([^"]{5,200})"\s*\(([^)]*)\b((?:1[6-9]|20)\d{2})\b([^)]*)\)', body):
        title = m.group(1).strip().lower()[:80]
        quoted_tuples.add((title, m.group(3)))

    # 3. Possessive: "Name's *Title*" — title may or may not have year
    for m in re.finditer(
            r"\b([A-Z][a-zA-Z'-]+(?:\s+[A-Z]\.)?(?:\s+[A-Z][a-zA-Z'-]+){0,3})'s\s+\*([^*]{3,200})\*",
            body):
        scholar = m.group(1)
        title = m.group(2).strip().lower()[:80]
        possessive_works.add((scholar, title))
        named_scholars.add(scholar)

    # 4. Attribution: "FirstName Surname [in *Work*] (verb)"
    attribution_verbs = (
        r"(?:argues|specifies|articulates|writes|extends|engages|carries|supplies|"
        r"notes|observes|articulated|argued|wrote|founded|develops|formulates|"
        r"shows|demonstrates|theorizes|analyses|analyzes|critiques)"
    )
    for m in re.finditer(
        rf"\b([A-Z][a-zA-Z'-]+(?:\s+[A-Z]\.)?(?:\s+[A-Z][a-zA-Z'-]+){{1,3}})"
        rf"(?:\s+in\s+\*[^*]+\*)?"
        rf"\s+{attribution_verbs}",
        body):
        scholar = m.group(1)
        attributions.add(scholar)
        named_scholars.add(scholar)

    # 5. Inline (Year) — "Author (Year)" pattern
    skip_words = {"document", "article", "act", "section", "title", "part",
                  "chapter", "amendment", "thread", "federalist", "covenant"}
    for m in re.finditer(r"\b([A-Z][a-zA-Z'-]+(?:\s+[A-Z][a-zA-Z'-]+){0,2})\s*\(((?:1[6-9]|20)\d{2})\)", body):
        scholar = m.group(1)
        first = scholar.split()[0].lower()
        if first in skip_words: continue
        named_scholars.add(scholar)

    return {
        "italic": italic_tuples,
        "quoted": quoted_tuples,
        "posses": possessive_works,
        "scholars": named_scholars,
        "attribs": attributions,
    }


def count_concrete_instances(body: str):
    """Count named acts, treaties, conventions, court cases, dated institutions, Federalist papers."""
    instances = set()

    # Acts: "X Act of YYYY" or "X Act (YYYY)" or "X Act, YYYY" or "X Act YYYY"
    for m in re.finditer(
        r"\b([A-Z][\w\-]*(?:\s+[A-Z][\w\-]*){0,8}\s+Act)\s*(?:of\s+|\(|,\s+)?((?:1[6-9]|20)\d{2})",
        body):
        instances.add(("act", m.group(1).lower()[:80], m.group(2)))

    # Convention/Treaty/Declaration/Covenant/Protocol/Directive/Accord/Charter + year
    for m in re.finditer(
        r"\b([A-Z][\w\-]*(?:\s+[A-Z][\w\-]*){0,8}\s+"
        r"(?:Convention|Treaty|Declaration|Covenant|Protocol|Directive|Accord|Charter|Compact|Resolution))"
        r"\s*(?:of\s+|\(|,\s+)?((?:1[6-9]|20)\d{2})",
        body):
        instances.add(("treaty", m.group(1).lower()[:80], m.group(2)))

    # Constitution of X (YYYY) — with year nearby
    for m in re.finditer(
        r"\b(?:Plurinational\s+)?Constitution of (?:the )?[A-Z][\w'\s-]+?\s*(?:of\s+)?\b((?:1[6-9]|20)\d{2})",
        body):
        instances.add(("constitution", m.group(0).lower()[:80], m.group(1)))

    # *Federalist* / The Federalist No. N
    for m in re.finditer(r"(?:\*The Federalist\*|The Federalist|\*Federalist\*|Federalist)\s+No\.?\s*\d+", body):
        instances.add(("federalist", m.group(0).lower(), ""))

    # Court case with reporter: "Name v. Name (NNN U.S. NNN, YYYY)" or "(YYYY)"
    for m in re.finditer(
        r"\b([A-Z][\w'-]+(?:\s+[A-Z][\w'-]+)?\s+v\.\s+[A-Z][\w'-]+(?:\s+[A-Z][\w'-]+){0,2})"
        r"\s*\([^)]*((?:1[6-9]|20)\d{2})[^)]*\)",
        body):
        instances.add(("case", m.group(1).lower(), m.group(2)))
    # Bare "Name v. Name" without reporter
    for m in re.finditer(r"\b([A-Z][\w'-]+\s+v\.\s+[A-Z][\w'-]+(?:\s+[A-Z][\w'-]+)?)\b", body):
        instances.add(("case-bare", m.group(1).lower(), ""))

    # Movement/institution founded/codified/etc. + YYYY
    for m in re.finditer(
        r"\b([A-Z][\w'-]+(?:\s+[A-Z][\w'-]+){0,4})\s+"
        r"(?:founded|codified|established|formed|launched|adopted|enacted|signed|drafted|published|articulated|coined)"
        r"\s+(?:in\s+)?((?:1[6-9]|20)\d{2})",
        body):
        instances.add(("inst", m.group(1).lower()[:80], m.group(2)))

    # "X of YYYY" as Court/Court decision-style: "Decision T-622/16" or similar
    for m in re.finditer(r"\bDecision\s+T-?\d+[/-]?\d+\b", body):
        instances.add(("decision", m.group(0).lower(), ""))

    # Named landmark date: "in YYYY" with capitalized noun phrase immediately before
    # (deduplicated against other patterns by set semantics)

    return instances


def count_collapsed_clauses(body: str) -> int:
    return len(re.findall(
        r"[Ss]cope\s*[—\-:].{1,300}?scale\s*[—\-:].{1,300}?feedback.{1,500}?sunset",
        body, re.DOTALL))


def count_cross_citations(body: str) -> int:
    return len(re.findall(
        r"Document [IVX]+\.\d+[^.]{1,80}"
        r"(?:specifies|carries|articulates|operates|supplies|extends|provides|engages|conducts|articulate)",
        body))


def load_plan_articulators(doc_id: str):
    """Best-effort extraction of named scholars from plan Sections 5 and 6.
    Returns set of last-names (lowercased)."""
    plans = glob.glob(f"outputs/v6_plans/Execution_Plan_{doc_id}_*_v6.md")
    if not plans:
        return set()
    text = open(plans[0]).read()
    # Section 5 (Required Threads) and Section 6 (Source Requirements)
    sections = re.split(r"^## \d+\.\s+", text, flags=re.MULTILINE)
    relevant = ""
    for s in sections:
        head = s.split("\n",1)[0].lower()
        if "required threads" in head or "source requirements" in head:
            relevant += "\n" + s
    if not relevant:
        return set()
    surnames = set()
    # Heuristic: "FirstName [Initial.] Surname" before a possessive, paren year, italic, or quoted title
    for m in re.finditer(
        r"\b([A-Z][a-z]+)\s+(?:[A-Z]\.\s+)?([A-Z][a-zA-Z'-]+)"
        r"(?:'s|\s+\(|\s+in\s+\*|,\s+\*|,\s+\")",
        relevant):
        surnames.add(m.group(2).lower())
    return surnames


def audit_doc(path: str, plan_check: bool = True):
    text = open(path).read()
    fname = os.path.basename(path).replace("_v6.md","")
    doc_id = fname.split("_")[0]
    is_migration = doc_id in MIGRATION_DOCS
    plan_scholars = load_plan_articulators(doc_id) if plan_check else set()

    parts = re.split(r"^## ", text, flags=re.MULTILINE)
    results = []
    body_full = ""
    for p in parts[1:]:
        first_line = p.split("\n",1)[0].strip()
        if not first_line: continue
        label = first_line[:80]
        body = p[len(first_line):]
        body_full += body
        if is_top_level_part_header(label, body):
            continue
        wc = len(body.split())
        if wc < 250 or label.lower().startswith("references"):
            continue
        exempt_kind = is_exempt_thread(label)

        sig = count_scholar_signals(body)
        instances = count_concrete_instances(body)
        collapsed = count_collapsed_clauses(body)
        crosscites = count_cross_citations(body)
        sentences = [s for s in re.split(r"\.\s+(?=[A-Z])", body) if len(s) > 30]
        xcite_pct = (crosscites / max(len(sentences),1)) * 100

        scholar_engagement = (
            len(sig["italic"]) + len(sig["quoted"]) +
            len(sig["posses"]) + len(sig["scholars"])
        )
        engagement_score = scholar_engagement + 0.5 * len(instances)

        flags = []
        severity = 0
        if not exempt_kind and not is_migration:
            if collapsed > 2:
                flags.append(f"COLLAPSED={collapsed}")
                severity += 3
            if xcite_pct > 50 and wc < 600:
                flags.append(f"XCITE-SHORT={xcite_pct:.0f}%@{wc}w")
                severity += 3
            elif xcite_pct > 50:
                flags.append(f"XCITE-HIGH={xcite_pct:.0f}%")
                severity += 2
            elif xcite_pct > 40:
                flags.append(f"XCITE={xcite_pct:.0f}%")
                severity += 1
            if engagement_score < 2 and wc > 700:
                flags.append(f"ENGAGEMENT-LOW={engagement_score:.1f}")
                severity += 2
            elif engagement_score < 4 and wc > 1500:
                flags.append(f"ENGAGEMENT-LARGE={engagement_score:.1f}@{wc}w")
                severity += 1

        verdict = "PASS"
        if severity >= 3: verdict = "FAIL"
        elif severity >= 1: verdict = "REVIEW"
        results.append({
            "label": label, "wc": wc,
            "italic": len(sig["italic"]), "quoted": len(sig["quoted"]),
            "posses": len(sig["posses"]), "scholars": len(sig["scholars"]),
            "instances": len(instances),
            "engagement": engagement_score,
            "collapsed": collapsed, "xcite_pct": xcite_pct,
            "exempt": exempt_kind, "flags": flags, "severity": severity,
            "verdict": verdict
        })

    plan_coverage = None
    if plan_scholars:
        present = set()
        body_lower = body_full.lower()
        for surname in plan_scholars:
            if re.search(rf"\b{re.escape(surname)}\b", body_lower):
                present.add(surname)
        missing = plan_scholars - present
        plan_coverage = {
            "plan_count": len(plan_scholars),
            "present_count": len(present),
            "missing": sorted(missing)
        }
    bib_report = audit_bibliography(text)
    return {"doc": fname, "doc_id": doc_id, "is_migration": is_migration,
            "threads": results, "plan_coverage": plan_coverage,
            "bibliography": bib_report}


def audit_bibliography(text: str):
    """Bibliography audit per Bibliography_and_Footnote_Conventions.md.
    Returns dict with:
      - body_citations: set of (title, year) tuples mined from body
      - refs_entries: list of bibliography entry lines
      - orphan_inline: body citations missing from References
      - orphan_refs: References entries with no corresponding body citation
      - footnotes: list of footnote markers
      - footnote_orphans: footnotes citing sources not in Bibliography
      - tribal_warns: Indigenous-scholar mentions possibly missing tribal affiliation
    """
    # Split body vs References section.
    # Strategy: find explicit "## References / ## Bibliography" heading first; if none,
    # detect bibliography by content shape (run of headings whose bodies are >50%
    # bibliography-pattern lines: "Author. *Title*. Publisher, Year." or "- Author, *Title*").
    refs_match = re.search(
        r"^##\s+(?:references|bibliography|works cited)\b.*\Z",
        text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if refs_match:
        refs_text = refs_match.group(0)
        body_text = text[: refs_match.start()]
    else:
        # Content-shape detection: find the first ## section after which bibliography pattern dominates
        bib_line_re = re.compile(
            r"^\s*[-*]?\s*[A-Z][\w'-]+(?:,\s+[A-Z][\w.\s'-]+)?(?:\s*\([^)]*\))?\.\s+"
            r"(?:\*[^*]+\*|\"[^\"]+\")",
            re.MULTILINE)
        sections = list(re.finditer(r"^##\s+(.+)$", text, re.MULTILINE))
        cutover = None
        for i, sm in enumerate(sections):
            start = sm.end()
            end = sections[i+1].start() if i+1 < len(sections) else len(text)
            chunk = text[start:end]
            bib_lines = len(bib_line_re.findall(chunk))
            total_lines = len([l for l in chunk.split("\n") if l.strip()])
            if total_lines >= 4 and bib_lines / max(total_lines,1) > 0.4:
                cutover = sm.start()
                break
        if cutover is not None:
            refs_text = text[cutover:]
            body_text = text[:cutover]
        else:
            refs_text = ""
            body_text = text

    # Mine body citations: italic titles with year, quoted titles with year, named acts with year,
    # treaties/conventions with year, Federalist No N, case names with year
    body_citations = set()
    for m in re.finditer(r"\*([^*]{3,150})\*\s*\(([^)]*)\b((?:1[6-9]|20)\d{2})\b", body_text):
        body_citations.add(("italic", m.group(1).strip().lower()[:80], m.group(3)))
    for m in re.finditer(r'"([^"]{5,150})"\s*\(([^)]*)\b((?:1[6-9]|20)\d{2})\b', body_text):
        body_citations.add(("quoted", m.group(1).strip().lower()[:80], m.group(3)))
    for m in re.finditer(
        r"\b([A-Z][\w\-]*(?:\s+[A-Z][\w\-]*){0,8}\s+Act)\s*(?:of\s+|\(|,\s+)?((?:1[6-9]|20)\d{2})",
        body_text):
        body_citations.add(("act", m.group(1).lower()[:80], m.group(2)))
    for m in re.finditer(
        r"\b([A-Z][\w\-]*(?:\s+[A-Z][\w\-]*){0,8}\s+"
        r"(?:Convention|Treaty|Declaration|Covenant|Protocol|Directive|Charter))"
        r"\s*(?:of\s+|\(|,\s+)?((?:1[6-9]|20)\d{2})",
        body_text):
        body_citations.add(("treaty", m.group(1).lower()[:80], m.group(2)))
    for m in re.finditer(
        r"\b([A-Z][\w'-]+(?:\s+[A-Z][\w'-]+)?\s+v\.\s+[A-Z][\w'-]+(?:\s+[A-Z][\w'-]+){0,2})"
        r"\s*\([^)]*((?:1[6-9]|20)\d{2})[^)]*\)",
        body_text):
        body_citations.add(("case", m.group(1).lower(), m.group(2)))

    # Mine References entries: each non-empty line that begins with a capital letter or italic title
    refs_lines = []
    if refs_text:
        for line in refs_text.split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("###"):
                continue
            if len(line) < 20:
                continue
            refs_lines.append(line)

    refs_normalized = " || ".join(l.lower() for l in refs_lines)

    # Check orphan inline citations (tolerant title-matching)
    orphan_inline = []
    for kind, title, year in body_citations:
        if not refs_text:
            orphan_inline.append((kind, title, year))
            continue
        # Try title fragments (first 30 / 40 / 50 chars; before colon)
        title_main = title.split(":")[0].strip()
        candidates = [title, title_main, title_main[:50], title_main[:40], title_main[:30], title_main[:20]]
        candidates = [c for c in candidates if len(c) >= 12]
        # Strip common subtitle separators and normalize
        found = False
        for c in candidates:
            if c in refs_normalized:
                found = True
                break
        if found:
            continue
        # Last-resort: distinctive words from title
        title_words = [w for w in re.findall(r"[a-z]{5,}", title_main) if w not in
                       {"about", "after", "again", "against", "every", "great", "their",
                        "there", "these", "thing", "world", "which", "where", "would"}]
        if len(title_words) >= 2:
            distinctive = " ".join(title_words[:3])
            if distinctive in refs_normalized:
                continue
        orphan_inline.append((kind, title, year))

    # Check orphan References entries: entries with no body citation match
    orphan_refs = []
    body_lower = body_text.lower()
    for entry in refs_lines:
        # Skip Cross-Referenced v6 Documents (special exemption)
        if entry.lower().startswith("document "):
            continue
        # Extract candidate title (italic-or-quoted) from entry
        title_match = re.search(r"\*([^*]{3,150})\*", entry) or re.search(r'"([^"]{5,150})"', entry)
        if not title_match:
            continue
        title = title_match.group(1).strip().lower()[:60]
        if not title: continue
        if title in body_lower:
            continue
        # Try fragment
        frag = title.split(":")[0][:30]
        if frag and frag in body_lower:
            continue
        orphan_refs.append(entry[:120])

    # Footnote handling: detect [^N] markers and [^N]: definitions
    footnote_markers = set(re.findall(r"\[\^(\d+)\]", body_text))
    footnote_defs = dict(re.findall(r"^\[\^(\d+)\]:\s*(.+)$", text, re.MULTILINE))
    footnote_orphans = []
    for n in footnote_markers:
        if n not in footnote_defs:
            footnote_orphans.append(n)

    # Tribal-affiliation warnings: Indigenous scholar names mentioned without parenthetical affiliation
    # Heuristic: scholars from a known affiliation list. Only check the FIRST mention; tolerant of
    # variants like "Citizen Potawatomi Nation", "Lower Brule Sioux", "Mohawk" alone.
    indigenous_scholars = [
        ("TallBear", ["Sisseton Wahpeton", "Sisseton"]),
        ("Estes", ["Lower Brule", "Sioux"]),
        ("Coulthard", ["Yellowknives", "Dene"]),
        ("Simpson", ["Mohawk", "Kanien", "Haudenosaunee"]),
        ("Kimmerer", ["Citizen Potawatomi", "Potawatomi"]),
        ("LaDuke", ["Anishinaabe", "Ojibwe"]),
        ("Lyons", ["Onondaga", "Haudenosaunee"]),
        ("Grande", ["Quechua"]),
        ("Driskill", ["Cherokee"]),
        ("Gone", ["Aaniiih", "Gros Ventre"]),
        ("Wildcat", ["Yuchi", "Muscogee"]),
        # Smith and Mohawk too ambiguous (common surnames) — drop from auto-check
    ]
    tribal_warns = []
    tribal_pattern = (r"\(\s*[A-Z][a-zA-Z\s]+"
                      r"(?:Nation|Tribe|Sioux|Dene|Mohawk|Oyate|Pueblo|Anishinaabe|"
                      r"Potawatomi|Cherokee|Quechua|Yuchi|Aaniiih|Onondaga|Seneca|"
                      r"Yellowknives|Lower Brule|Sisseton|Ojibwe|Kanien|Haudenosaunee|"
                      r"Cree|Inuit|Métis|Diné|Navajo|Maori|Ngāti|Aboriginal|First Nation)"
                      r"[^)]*\)")
    for surname, affiliations in indigenous_scholars:
        # Find FIRST mention of surname in body
        first_match = re.search(rf"\b{surname}\b", body_text)
        if not first_match: continue
        start = max(0, first_match.start()-20)
        end = min(len(body_text), first_match.end()+120)
        window = body_text[start:end]
        if any(a in window for a in affiliations): continue
        if re.search(tribal_pattern, window): continue
        tribal_warns.append(f"{surname} (expected {affiliations[0]})")

    return {
        "has_refs": bool(refs_text),
        "n_body_citations": len(body_citations),
        "n_refs_entries": len(refs_lines),
        "n_orphan_inline": len(orphan_inline),
        "n_orphan_refs": len(orphan_refs),
        "orphan_inline_samples": [f"{k}:{t[:40]}({y})" for k,t,y in list(orphan_inline)[:5]],
        "orphan_refs_samples": orphan_refs[:5],
        "n_footnotes": len(footnote_markers),
        "n_footnote_orphans": len(footnote_orphans),
        "n_tribal_warns": len(tribal_warns),
        "tribal_warns": tribal_warns[:5],
    }


def main():
    docs = sorted(glob.glob("project/source_documents/v6_completed/*.md"))
    docs = [d for d in docs if "MANIFEST" not in d]
    all_results = [audit_doc(d) for d in docs]

    print("="*100)
    print(f"FORMULAIC-THINNESS AUDIT v3 — {len(docs)} documents")
    print("="*100)
    pass_n = fail_n = review_n = 0
    for r in all_results:
        n_fail = sum(1 for t in r["threads"] if t["verdict"]=="FAIL")
        n_review = sum(1 for t in r["threads"] if t["verdict"]=="REVIEW")
        n_threads = len(r["threads"])
        if r["is_migration"]:
            status = "PASS (migration)"
            pass_n += 1
        elif n_fail > 0:
            status = f"FAIL ({n_fail} threads)" + (f" + {n_review} review" if n_review else "")
            fail_n += 1
        elif n_review > 0:
            status = f"REVIEW ({n_review} threads)"
            review_n += 1
        else:
            status = "PASS"
            pass_n += 1
        pc = r["plan_coverage"]
        pc_str = ""
        if pc and pc["plan_count"]:
            cov = (pc["present_count"]/pc["plan_count"])*100
            pc_str = f"  plan-cov: {pc['present_count']}/{pc['plan_count']}={cov:.0f}%"
        print(f"  {r['doc_id']:8s} {status:38s} [{n_threads} threads]{pc_str}")

    print("\n" + "="*100)
    print(f"FAILS (severity >= 3)")
    print("="*100)
    for r in all_results:
        fails = [t for t in r["threads"] if t["verdict"]=="FAIL"]
        if not fails: continue
        print(f"\n{r['doc']}")
        for t in fails:
            print(f"  [{t['verdict']}] {t['label'][:65]}")
            print(f"    {t['wc']}w | eng={t['engagement']:.1f} "
                  f"(italic={t['italic']} quoted={t['quoted']} posses={t['posses']} "
                  f"sch={t['scholars']} inst={t['instances']}) | "
                  f"xcite={t['xcite_pct']:.0f}% | collapsed={t['collapsed']}")
            for f in t['flags']: print(f"      - {f}")

    print("\n" + "="*100)
    print(f"REVIEWS (severity 1-2)")
    print("="*100)
    for r in all_results:
        reviews = [t for t in r["threads"] if t["verdict"]=="REVIEW"]
        if not reviews: continue
        print(f"\n{r['doc']}")
        for t in reviews:
            print(f"  [{t['verdict']}] {t['label'][:55]} | {t['wc']}w eng={t['engagement']:.1f} "
                  f"xcite={t['xcite_pct']:.0f}% | {', '.join(t['flags'])}")

    print("\n" + "="*100)
    print("PLAN-ARTICULATOR COVERAGE GAPS (docs missing > 3 plan-named scholars)")
    print("="*100)
    for r in all_results:
        pc = r["plan_coverage"]
        if pc and pc["plan_count"] >= 5 and len(pc["missing"]) > 3:
            print(f"  {r['doc_id']:8s} missing: {pc['missing'][:8]}")

    print("\n" + "="*100)
    print("BIBLIOGRAPHY-AND-FOOTNOTE AUDIT")
    print("="*100)
    bib_fail = 0
    bib_warn = 0
    for r in all_results:
        b = r["bibliography"]
        if not b: continue
        issues = []
        if not b["has_refs"]:
            issues.append("NO-REFS-SECTION")
        if b["n_orphan_inline"] > 0:
            issues.append(f"ORPHAN-INLINE={b['n_orphan_inline']}")
        if b["n_orphan_refs"] > 5:
            issues.append(f"ORPHAN-REFS={b['n_orphan_refs']}")
        if b["n_footnote_orphans"] > 0:
            issues.append(f"FN-ORPHANS={b['n_footnote_orphans']}")
        if b["n_tribal_warns"] > 0:
            issues.append(f"TRIBAL-WARN={b['n_tribal_warns']}")
        if not issues:
            continue
        # Severity: orphan-inline and fn-orphans are FAIL; orphan-refs > 5 and tribal-warn are WARN
        is_fail = (b["n_orphan_inline"] > 0) or (b["n_footnote_orphans"] > 0) or not b["has_refs"]
        marker = "FAIL" if is_fail else "WARN"
        if is_fail: bib_fail += 1
        else: bib_warn += 1
        print(f"  [{marker}] {r['doc_id']:8s} body-cites={b['n_body_citations']:3d} "
              f"refs={b['n_refs_entries']:3d} | {', '.join(issues)}")
        if b.get("orphan_inline_samples"):
            for s in b["orphan_inline_samples"]:
                print(f"        orphan-inline: {s}")
        if b.get("tribal_warns"):
            for s in b["tribal_warns"][:3]:
                print(f"        tribal-warn: {s}")

    print("\n" + "="*100)
    print(f"SUMMARY: {pass_n} pass, {review_n} review, {fail_n} fail (of {len(docs)} on formulaic-thinness)")
    print(f"         {bib_fail} bib-fail, {bib_warn} bib-warn (of {len(docs)} on bibliography)")
    print("="*100)

if __name__ == "__main__":
    main()
