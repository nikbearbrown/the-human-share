# Course corpus and supporting data

[Course corpus](course-corpus.tsv) inventories the eight existing course-material records and the available Fall 2026 and Spring 2027 syllabi in the public Northeastern SEIS Newton snapshots. The unit for syllabus rows is a term and CRN. Section labels and titles for new records are schedule metadata, not verification that a PDF is the right syllabus.

| Term | Distinct CRNs on Newton | PDF-linked CRNs on Newton | Previously verified, off-index | Missing from Newton (HTTP 404) |
| --- | ---: | ---: | ---: | ---: |
| Fall 2026 | 121 | 113 | 1 | 8 |
| Spring 2027 | 106 | 44 | 0 | 62 |

Both indexes were checked November 27, 2026 against the November 23 collected manifests. The linked CRN coverage was unchanged; all 70 previously missing responses were rechecked and still returned 404. One Fall CRN is listed twice under different schedule groups and is counted once. The off-index Fall row is the existing DAMG 6310 syllabus, CRN 21970. See the [Fall index](http://newton.northeastern.edu:8080/fall2026/) and [Spring index](http://newton.northeastern.edu:8080/spring2027/).

- **Confirmed:** The 12 original Fall rows were previously checked. Their existing IDs and provenance are preserved, including two pairs with near-identical text marked to count once.
- **Candidates:** New PDF records stay in the inventory, with metadata indicators. A PDF response or a first-page match is not by itself a confirmed term, course and section. Confirm section identity and permitted use before coding.
- **Held:** 8 link-only rows, 8 known metadata conflicts, and 2 incomplete Fall schedule rows are included for traceability, not for coding. Link-only rows point to the department index rather than republishing document links flagged for access review.
- **Missing:** [Coverage log](course-corpus-missing.tsv) records the 70 sections without a PDF. They are not part of the syllabus corpus or a unit of evidence.

For text-level analysis, use `text_id` only after applying the coding eligibility rules. Exact PDF duplicates share one `text_id`; the inventory has 110 Fall and 43 Spring syllabus text IDs before screening. Near-duplicates beyond the two previously confirmed pairs have not been adjudicated. The eight course-material records retain their existing evidence level; syllabus-only records do not establish what students were graded on. The Branding and AI section overlaps with the existing course-material record and must not count as independent evidence of the same task.

The repo tracks metadata, public source pointers and SHA-256 digests, not instructor PDF copies or private access details. This collection covers the SEIS archive and the existing course materials, not all Northeastern colleges, Banner, or Canvas. Other data sources and their usage terms are listed in the [dataset manifest](manifest.yaml).
