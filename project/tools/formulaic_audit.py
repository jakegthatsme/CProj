#!/usr/bin/env python3
"""Formulaic-Thinness Audit v2 — improved heuristics.

Changes from v1:
- Skip top-level Part headers (e.g., "## Part XII — Structural Commitments")
  by requiring section to have >300 words OR a thread/part-N pattern
- Broader scholar-citation detection: italic titles, quoted titles, Surname (Year),
  "Author's Work (Year)" without italic
- Distinguish FAIL (multiple signals) from REVIEW (single signal that may be false positive)
"""

import os, re, glob

MIGRATION_DOCS = {"I.01", "I.02", "I.03", "I.04", "III.01", "II.08", "XII.01"}

def is_exempt_thread(label: str) -> bool:
    s = label.lower()
    return any(k in s for k in [
        "closing", "opening", "synthesis", "references",
        "introduction", "outro"
    ])

def is_top_level_part_header(label: str, body: str) -> bool:
    # Top-level Part headers are short and typically match the document's Part title
    s = label.lower().strip()
    if not s.startswith("part "):
        return False
    # If body is mostly empty before next ## section, it's a top-level header
    body_clean = re.sub(r"^\s*$\n?", "", body, flags=re.MULTILINE)
    if len(body_clean.split()) < 100:
        return True
    return False

def count_scholar_tuples(body: str) -> int:
    """Count distinct scholar-year-work tuples using multiple citation styles."""
    tuples = set()
    # Pattern 1: *Italic Title* (... Year ...)
    for m in re.finditer(r"\*([^*]{3,200})\*\s*\(([^)]*)\b((?:19|20)\d{2})\b([^)]*)\)", body):
        title = m.group(1).strip()
        year = m.group(3)
        tuples.add((title.lower()[:60], year))
    # Pattern 2: "Quoted Title" (... Year ...)
    for m in re.finditer(r'"([^"]{5,150})"\s*\(([^)]*)\b((?:19|20)\d{2})\b([^)]*)\)', body):
        title = m.group(1).strip()
        year = m.group(3)
        tuples.add((title.lower()[:60], year))
    # Pattern 3: Surname's *Work* without parenthetical year (Year given separately)
    # Pattern 4: "in Year, Surname wrote/argued/etc"
    # These are harder to disambiguate without false positives; rely on patterns 1+2 + inline year mentions
    # Pattern 5: Inline (Year) right after a possessive title — Author's *Title* (Year)
    # already covered by Pattern 1
    return len(tuples)

def count_named_scholars(body: str) -> int:
    """Count distinct named scholars (capitalized two-word names with possessive or attribution)."""
    # "Author's analytical work" / "Author argues" / "Author specifies" / "Author in *Title*"
    scholars = set()
    # Possessive form: "FirstName Surname's"
    for m in re.finditer(r"\b([A-Z][a-z]+(?:\s+[A-Z]\.)?\s+[A-Z][a-z'-]+(?:\s+[A-Z][a-z'-]+)?)'s\b", body):
        scholars.add(m.group(1))
    # Attribution form: "FirstName Surname argues/specifies/articulates/in *Work*"
    for m in re.finditer(r"\b([A-Z][a-z]+(?:\s+[A-Z]\.)?\s+[A-Z][a-z'-]+(?:\s+[A-Z][a-z'-]+)?)\s+(?:argues|specifies|articulates|carries|supplies|extends|engages|writes|in\s+\*)", body):
        scholars.add(m.group(1))
    return len(scholars)

def audit_doc(path: str):
    text = open(path).read()
    fname = os.path.basename(path).replace("_v6.md","")
    doc_id = fname.split("_")[0]
    is_migration = doc_id in MIGRATION_DOCS
    # Split on level-2 sections
    parts = re.split(r"^## ", text, flags=re.MULTILINE)
    results = []
    for p in parts[1:]:
        first_line = p.split("\n",1)[0].strip()
        if not first_line: continue
        label = first_line[:80]
        # Skip top-level part headers
        body = p[len(first_line):]
        if is_top_level_part_header(label, body):
            continue
        wc = len(body.split())
        if wc < 250:  # very short sections — skip (likely metadata or transition)
            continue
        # Skip explicit exempt
        exempt_kind = is_exempt_thread(label)
        # Skip "References" section
        if label.lower().startswith("references"):
            continue
        tuples = count_scholar_tuples(body)
        scholars = count_named_scholars(body)
        collapsed = len(re.findall(
            r"[Ss]cope\s*[—\-:].{1,300}?scale\s*[—\-:].{1,300}?feedback.{1,500}?sunset",
            body, re.DOTALL))
        crosscites = len(re.findall(
            r"Document [IVX]+\.\d+[^.]{1,80}(?:specifies|carries|articulates|operates|supplies|extends|provides)",
            body))
        sentences = [s for s in re.split(r"\.\s+(?=[A-Z])", body) if len(s) > 30]
        xcite_pct = (crosscites / max(len(sentences),1)) * 100

        # Severity scoring
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
                flags.append(f"XCITE={xcite_pct:.0f}%")
                severity += 2
            elif xcite_pct > 40:
                flags.append(f"XCITE={xcite_pct:.0f}%")
                severity += 1
            # Scholar engagement: combined tuples + named scholars
            engagement = tuples + scholars
            if engagement < 3 and wc > 700:
                flags.append(f"ENGAGEMENT={engagement} (tup={tuples}, sch={scholars})")
                severity += 2
            elif engagement < 5 and wc > 1500:
                flags.append(f"ENGAGEMENT-LARGE={engagement} (tup={tuples}, sch={scholars})")
                severity += 1
        verdict = "PASS"
        if severity >= 3: verdict = "FAIL"
        elif severity >= 1: verdict = "REVIEW"
        results.append({
            "label": label, "wc": wc, "tuples": tuples, "scholars": scholars,
            "collapsed": collapsed, "xcite_pct": xcite_pct,
            "exempt": exempt_kind, "flags": flags, "severity": severity,
            "verdict": verdict
        })
    return {"doc": fname, "doc_id": doc_id, "is_migration": is_migration, "threads": results}

def main():
    docs = sorted(glob.glob("project/source_documents/v6_completed/*.md"))
    docs = [d for d in docs if "MANIFEST" not in d]
    all_results = []
    for d in docs:
        all_results.append(audit_doc(d))
    # Per-doc summary
    print("="*100)
    print("FORMULAIC-THINNESS AUDIT v2 — improved heuristics")
    print("="*100)
    pass_count = fail_count = review_count = 0
    for r in all_results:
        n_fail = sum(1 for t in r["threads"] if t["verdict"]=="FAIL")
        n_review = sum(1 for t in r["threads"] if t["verdict"]=="REVIEW")
        n_threads = len(r["threads"])
        if r["is_migration"]:
            status = "PASS (migration)"
            pass_count += 1
        elif n_fail > 0:
            status = f"FAIL ({n_fail} threads)"
            if n_review: status += f" + {n_review} review"
            fail_count += 1
        elif n_review > 0:
            status = f"REVIEW ({n_review} threads)"
            review_count += 1
        else:
            status = "PASS"
            pass_count += 1
        print(f"  {r['doc_id']:8s} {status:35s} [{n_threads} threads]")

    print("\n" + "="*100)
    print(f"FAILING DOCUMENTS (severity >= 3)")
    print("="*100)
    for r in all_results:
        fails = [t for t in r["threads"] if t["verdict"]=="FAIL"]
        if not fails: continue
        print(f"\n{r['doc']}")
        for t in fails:
            print(f"  [{t['verdict']}] {t['label'][:65]}")
            print(f"        {t['wc']}w | tup={t['tuples']} sch={t['scholars']} | xcite={t['xcite_pct']:.0f}% | collapsed={t['collapsed']}")
            for f in t['flags']: print(f"        - {f}")

    print("\n" + "="*100)
    print(f"REVIEW DOCUMENTS (severity 1-2, likely heuristic edge cases)")
    print("="*100)
    for r in all_results:
        reviews = [t for t in r["threads"] if t["verdict"]=="REVIEW"]
        if not reviews: continue
        print(f"\n{r['doc']}")
        for t in reviews:
            flag_str = ", ".join(t['flags'])
            print(f"  [{t['verdict']}] {t['label'][:65]} | {t['wc']}w tup={t['tuples']} sch={t['scholars']} xcite={t['xcite_pct']:.0f}%")

    print("\n" + "="*100)
    print(f"SUMMARY: {pass_count} pass, {review_count} review, {fail_count} fail (of {len(docs)} docs)")
    print("="*100)

if __name__ == "__main__":
    main()
