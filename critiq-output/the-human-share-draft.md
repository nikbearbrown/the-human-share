# The Human Share: Measuring What AI-Era Jobs Ask of People, and Whether Courses Teach It

*Rough methods manuscript. No empirical results are reported.*

## Abstract

An occupational inventory, a vacancy advertisement and a course assessment characterize different kinds of evidence about work. This study proposes a measurement protocol that links them without assuming that an advertised skill is exercised at work or that an assessment proves mastery. The protocol describes work on seven non-ranked capacity facets and six work phases, compares the coverage of the occupational inventory with contemporary recruitment language, and contrasts graded course opportunities with recruiting demand. Observed vendor AI use is a separate evidence layer. The present contribution is an auditable design; data acquisition and independent coding are incomplete.

## Introduction

What is the capacity that a novice is actually asked to demonstrate? Running an analysis, deciding whether it is credible and negotiating whether to act on it may appear in the same assignment but put different demands on a person. Similarly, a tool name in a vacancy does not establish any of those demands. A common vocabulary can make the comparison inspectable, provided absence from one source is not mistaken for absence from work.

The study asks five questions. How much of the seven-facet schema appears in occupational descriptors and in the descriptors underlying published AI exposure measures? Do explicit demand conditions differ by seniority within the same occupation? Which posting tasks lack a supported occupation-task or detailed-work-activity match? How does the phase profile of graded coursework compare with recruiting language? How does the stated role of AI in coursework compare with observed vendor use in corresponding work tasks? None of these asks whether a capacity is uniquely human in principle.

## Methods

The [project plan](../PROJECT.md) specifies O*NET 31.0 and the fixed [course corpus](../data/course-corpus.tsv). Record the O*NET-SOC code and release for each join, and preserve unmatched and uncertain records. Attribute O*NET to the U.S. Department of Labor, Employment and Training Administration under [the database license](https://www.onetcenter.org/license_db.html). This paper does not read or update the production Explorer: it uses a pinned release independently of an older dashboard import. [NEEDS: reproducible dataset and analysis manifest with the exact releases, access restrictions and join inventories.]

For occupational coverage, blind independent coders to the existing machine crosswalk, record primary and secondary facet labels when the evidence supports them, and retain disagreements. Publish aggregate coverage with the unit named: a unique descriptor, a task or an occupation is not interchangeable. A concentrated crosswalk of abilities would not show that O*NET as a whole omits a facet; repeat against supported task and work-activity units. Treat source descriptors and index scores as separate objects and do not distribute restricted scores. Candidate machine labels are not ground truth.

For ads, classify explicit conditions of work, not adjectives or product names. [ASSUMPTION: use one eligible, deduplicated ad per source-employer opening and estimate the share containing at least one reviewable signal for a specified facet.] Record exact-match, plausible and unmatched task links separately. Independently audit a stratified sample of positives, negatives and unresolved mappings before interpreting residuals. Compare seniority strata within occupation and report ad counts and description coverage. If seniority is unclassified or if descriptions are absent, do not code a negative. Compare estimates under alternative seniority definitions and matching cutoffs; do not choose those cutoffs after seeing outcomes.

For courses, code documented graded work rather than catalog descriptions. Use understand, plan, produce, check, sustain and coordinate. Preserve those six phases in the analysis, with any five-phase reporting view explicitly mapped in the [phase schema](../data/phase-schema/five-to-six.tsv). Treat syllabi shared across sections as one document in document-level summaries and report section-level sensitivity. Record unknown assessment weights as missing; present equal-assessment and graded-weight profiles separately where they can be calculated. Preserve assignment-level provenance without publishing private course materials.

For AI comparisons, distinguish prohibited use, delegated work and required human engagement in course instructions. Compare their distribution descriptively with vendor-reported use measures only where source and evaluation units permit a documented link. Neither AI exposure nor use in one platform establishes time saved or fewer human tasks. [NEEDS: approved task-usage inputs and a prespecified bridge.]

## Results to report

No analytical result is available. The first table should show flows from source records to eligible, coded and matched units, by source. The first figure should show descriptor and task facet coverage separately, with unknown and uncertain fractions rather than implicit zeros. The second should compare phase profiles for matched course and role pairs, label whether percentages are of assignments or ads, and include comparison-selection criteria. Report human–human and model–human agreement before adjudication, not just a pooled agreement score.

## Discussion

The intended output is an evidence trail for curriculum choices. A gap between assessment and recruitment may indicate a missing opportunity, an incomplete syllabus, employer signaling, a bad crosswalk, or a defensible teaching sequence with unaided fundamentals. A low match is a prompt to inspect the evidence, not grounds to grade a course or label a worker. Counts from approved third-party posting sources remain aggregate only; licensed data, raw posting text, student material, and coder identities do not appear in public outputs. Classroom performance and labor-market outcomes would need separate studies and appropriate review.
