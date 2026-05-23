# Bibliography and Footnote Conventions — CProj v6 Operating Protocol

This protocol specifies strict rules for citation, bibliography, and footnotes in v6 documents. It supplements `scholarship-mode` (which governs integrated-citation register) and the `Formulaic_Thinness_Audit.md` protocol (which governs analytical engagement). All v6 documents drafted in Stage 2 must comply; migration documents (the seven substantively-drafted v5 exemplars) are remediated to compliance at their next touch.

The discipline is auditable. The audit script `project/tools/formulaic_audit.py` enforces the rules at the document gate.

## I. Inline Citation Discipline (under `scholarship-mode`)

Integrated citations remain the default register. The form on first mention is:

> *Author full name (tribal affiliation where applicable)* in *Work Title* (*Publisher*, *Year*) articulates …

Subsequent mentions may shorten to *Author surname* + *short title* or *Author surname (Year)*. The first-mention conventions are load-bearing for primary articulators and Indigenous scholars; tribal affiliation appears in parentheses after the name on every first mention without exception.

For journal articles, the first-mention form is:

> *Author full name* in "*Article Title*" (*Journal Volume, no. Issue, Year, pp. start–end*) specifies …

For legal-architectural primary texts (acts, treaties, conventions, declarations, covenants, protocols, directives, charters, constitutions, court cases) the first-mention form is:

> *Full Title of Instrument* (*Jurisdiction or Court, Year*; *Reporter Citation where applicable*) provides …

Federalist Papers cite as *The Federalist* No. N (Author, Date). Court cases cite with full reporter where available.

## II. Bibliography Discipline (Strict)

### II.A — Every cited source has a Bibliography entry

Every inline citation in the body — every named work, named act, named treaty, named court case, named Federalist Paper, named primary text — has a corresponding entry in the document's References section. There are no orphan inline citations. The audit fails the document where any inline citation lacks a Reference entry.

### II.B — Every Bibliography entry has at least one body citation

References sections do not pad. Every entry in the Bibliography corresponds to at least one inline citation in the body. Bibliography entries without body citation are removed at remediation (or moved to a separate "Further Reading" section explicitly labelled as such, which the audit treats as non-load-bearing). The audit fails the document where the Reference-to-body ratio exceeds 1.5 entries per body-cited work.

### II.C — Bibliography format is strict

**Books.** *Author Last, First* (*Author Last, First*, eds., for edited volumes). *Title in Italics*. *Publisher*, *Year*. *DOI or URL where available*.

> Example. Coulthard, Glen Sean (Yellowknives Dene). *Red Skin, White Masks: Rejecting the Colonial Politics of Recognition*. University of Minnesota Press, 2014.

**Journal Articles.** *Author Last, First*. "*Article Title*." *Journal* *Volume*, no. *Issue* (*Year*): *pp.–pp*. *DOI*.

> Example. Crenshaw, Kimberlé. "Demarginalizing the Intersection of Race and Sex: A Black Feminist Critique of Antidiscrimination Doctrine, Feminist Theory and Antiracist Politics." *University of Chicago Legal Forum* 1989, no. 1 (1989): 139–167.

**Acts and Statutes.** *Full Title*. *Jurisdiction*, *Year*. *Citation*.

> Example. Well-being of Future Generations (Wales) Act 2015. *Welsh Government*, 2015. *2015 anaw 2*.

**Treaties, Conventions, Declarations, Covenants, Protocols, Directives.** *Full Title*. *Issuing Body*, *Year of Adoption*. *Entry into Force where relevant*. *URL*.

> Example. International Covenant on Economic, Social and Cultural Rights. *United Nations General Assembly*, 1966. *Entered into force 3 January 1976*.

**Constitutions.** *Constitution of Jurisdiction*. *Year of Adoption*. *Article references in body cite as Article N, Section M*.

> Example. Constitution of the Republic of Ecuador. 2008. *Articles 71–74 (Rights of Nature)*.

**Court Cases.** *Case Name in Italics*. *Citation*. *Court*, *Year*.

> Example. *Citizens United v. Federal Election Commission*. 558 U.S. 310. United States Supreme Court, 2010.

**Federalist Papers.** *The Federalist No. N*. *Author*. *Date of publication*.

> Example. *The Federalist No. 51*. James Madison. 8 February 1788.

**Indigenous Primary Articulators (Oral Tradition and Mediated Texts).** Where the source is oral-tradition-as-mediated-text (e.g., the Kaianerekowa / Haudenosaunee Great Law), cite the mediating scholar and the tradition together: *Mediating Scholar (Tribal Affiliation)*. *Title of Mediating Work*. *Publisher*, *Year*. *Mediating the [Tradition] of [People]*.

> Example. Lyons, Oren (Onondaga), et al., eds. *Exiled in the Land of the Free: Democracy, Indian Nations, and the U.S. Constitution*. Clear Light Publishers, 1992. *Mediating the Kaianerekowa (Great Law of Peace) of the Haudenosaunee*.

### II.D — Bibliography organization

References sections are organized by analytical-thematic grouping (e.g., "Reproductive Justice and the Material Conditions of Reproductive Autonomy", "Defense, Military, and War Powers", "Cross-Referenced v6 Documents"). Within each grouping, entries are alphabetized by author surname (or by instrument name where there is no individual author).

For migration documents, the v5 References section is preserved as substrate; remediation adds the v6 additions as new entries within the existing grouping structure and updates cross-referenced v6 document entries.

### II.E — Cross-referenced v6 documents

Each v6 document referenced in the body appears in a dedicated "Cross-Referenced v6 Documents" sub-section of References, listed as:

> Document *Identifier* — *Document Short Title*.

> Example. Document XII.01 — Eco-Mimetic Policy-Making.

These entries do not require publisher / year / DOI; the cross-reference is to the project's internal architecture, not to external publication. The list is for traceability and does not count against the Reference-to-body ratio described in II.B.

## III. Footnote Discipline (Optional but Strict When Used)

Integrated citations are the default. Footnotes are optional, but when used must follow the rules below.

### III.A — When footnotes are appropriate

Footnotes are used for:

1. *Page references* for quoted material that the body's integrated citation does not carry inline (e.g., when paraphrasing is more analytically efficient but page-precision is needed).
2. *Source elaboration* where the inline citation names the work and year but the analytical claim requires additional bibliographic context (edition, translator, original publication date, etc.).
3. *Tangential analytical remarks* whose inclusion in body prose would interrupt the analytical flow but which the engaged scholar would want to surface.
4. *Disambiguation* between multiple works by the same author cited in close proximity.

Footnotes are not used for:

1. Padding citation density without adding new content.
2. Hiding analytical work that should be in the body.
3. Citing the same source already cited inline in the same paragraph.

### III.B — Footnote format

Footnotes use Markdown footnote syntax: `[^N]` inline, `[^N]: footnote text` at the end of the section or document.

The footnote text format follows the same conventions as Bibliography entries (II.C), with the addition of page references where applicable:

> Example body. The seven-generations criterion operates as decision rule at the moment of decision rather than as cultivation framing applied after the fact.[^1]
>
> [^1]: See Lyons, *Exiled in the Land of the Free*, pp. 31–35, on the operational distinction between the deliberative-protocol and ratification phases of the Grand Council process.

### III.C — Footnote-to-bibliography linkage

Every footnote that cites a source carries either:

1. *Short form* (Author surname + short title + page reference), when the full citation appears in the Bibliography; or
2. *Full form* (full bibliographic entry), when the cited source is being introduced only in the footnote and is not previously cited in body.

In case (2), the source is also added to the Bibliography at the next document touch. The audit fails the document where any footnote source is missing from the Bibliography.

### III.D — Footnote numbering

Footnotes are numbered sequentially across the document. Markdown rendering handles renumbering automatically; do not reuse footnote markers.

## IV. Audit Rules

The `project/tools/formulaic_audit.py` script enforces the following bibliography checks at the document gate:

1. *Orphan inline citation*: any inline `*Italic Title* (Year)` or `"Quoted Title" (Year)` or named act/treaty/case in body must appear in References. **Fail** otherwise.
2. *Orphan Reference entry*: any References entry not corresponding to an inline citation. **Warn** (does not fail; flagged for remediation).
3. *Missing format elements*: References entries missing publisher (for books), journal+volume+year (for articles), reporter (for court cases), or year (for any instrument). **Warn**.
4. *Footnote-bibliography linkage*: every footnote citing a source has corresponding Bibliography entry. **Fail** otherwise.
5. *Tribal affiliation*: every Indigenous scholar first-mentioned in body has tribal affiliation in parentheses; every Bibliography entry for an Indigenous scholar carries tribal affiliation. **Warn** (manual review for confirmed Indigenous scholars).

The audit reports the bibliography section alongside the formulaic-thinness section in the document gate report.

## V. Migration Path

The seven substantively-drafted v5 exemplars (I.01, I.02, I.03, I.04, II.08, III.01, XII.01) carry v5 Bibliography sections. At the next remediation touch they are brought to v6 strict format:

- Inline citations checked against Bibliography for orphans (fail-condition).
- Bibliography format checked against the rules in II.C.
- Tribal affiliations added where missing.
- Cross-Referenced v6 Documents sub-section added if absent.

The remediation is conducted under the move-don't-regenerate principle: the v5 analytical content is preserved; only the bibliography and citation form is brought to v6 standard.

## VI. Integration with the Document Gate

The eight-criterion completeness check (`CLAUDE.md` Self-Audit Protocols) is extended by criterion 9 (formulaic-thinness audit, per `Formulaic_Thinness_Audit.md`) and by criterion 10 (bibliography-and-footnote audit, per this protocol). A document admitted to `v6_completed/` passes all ten criteria.

## VII. Audit Order at the Gate

1. Filler-discipline audit (`CLAUDE.md`).
2. Doubled-word scan (`CLAUDE.md`).
3. Cross-reference resolution scan (every Document X reference resolves).
4. Formulaic-thinness audit (`Formulaic_Thinness_Audit.md`).
5. Bibliography-and-footnote audit (this protocol).
6. Loss-check (`CLAUDE.md`).
7. Drift-check (`CLAUDE.md`).
8. Eight-criterion (now ten-criterion) completeness check.

A document passes when all eight audits and the ten criteria hold.
