# The Human Share

**Working title:** *The Human Share: Measuring What AI-Era Jobs Ask of People, and Whether Courses Teach It.* Part of the Irreducibly Human project.

## Executive summary

This repo holds the data foundation for a research paper and its tool. The paper argues that O\*NET, and the AI exposure indices built on it, measure only part of what jobs ask of people. Job listings, course graded work and observed AI-usage data can fill the gap.

The tool has three uses:
1. Search for courses by job or goal.
2. Give courses feedback on how well they align with job-market demand.
3. Compare how a course uses AI with how the job uses AI.

**Current phase: 2 (Acquire), in part.** Phase 1 is done. On 2026-11-23 Bear answered, in chat, decisions 1, 2, 3, 5, 6, 7 and 13 of `INVENTORY_REPORT.md`. Five open sources were downloaded with provenance and checksums. A use limit was set, and O\*NET 31.0 was pinned (both below). The abilities-to-facets crosswalk was rebuilt as a machine draft, and fellows or TAs will code its human gold set (see the report's sign-off log). Everything else in Phase 2 still waits on the open decisions. Nothing is analysed and nothing is scraped. Phase 3 waits for sign-off.

## The argument

1. **Seven facets of work.** Irreducibly Human is a faceted classification, not a hierarchy. Every task or job gets a profile across all seven facets, and no facet ranks above another. Machine reach is recorded per facet (or per descriptor); it is not an ordering of the facets.
2. **O\*NET's blind spot.** O\*NET's 52 abilities descend from Fleishman's psychometric taxonomy, which was built for personnel selection by factor analysis of individual differences. A draft crosswalk maps 47 of the 52 abilities to just two facets (Pattern & Association, Embodied & Sensorimotor). Four facets have no abilities at all.
3. **Exposure indices inherit the blind spot.** Published AI exposure indices built on O\*NET inherit it. They also disagree with each other more as exposure rises.
4. **Other data can fill the gap.**
   - Job listings carry recency and seniority, which O\*NET lacks.
   - Course assessments show what is actually practised.
   - Usage data shows how AI is actually used in tasks.
5. **Teaching principle.** By the end of a course, its use of AI should match the job's. Any divergence must be declared, and justified by a capacity the job itself requires, such as catching AI errors.

## Research questions

| RQ | Question |
|---|---|
| RQ1 | How well do O\*NET descriptors and published AI exposure indices cover the seven facets? |
| RQ2 | Can job listings measure demand for the upper facets using demand conditions ("sign off on", "no established process", "root-cause analysis") rather than soft-skill adjectives? Does facet demand vary more by seniority within an occupation than across occupations? |
| RQ3 | What share of tasks in job listings has no match in O\*NET tasks or DWAs? Is that residual disproportionately supervisory work: reviewing AI output, evaluating models, verifying agent-written code? |
| RQ4 | How does the phase profile of courses' graded work (requirements, design, build, review, deploy) compare with the phase profile of job listings for matched titles? |
| RQ5 | How does course AI use (banned, delegated, engaged) compare with observed job AI use (automation versus augmentation, by task)? |

## Facet definitions (schema: do not modify)

| Facet | Definition |
|---|---|
| Pattern & Association | Statistical pattern-matching at scale, including classification, prediction, retrieval and generation. |
| Embodied & Sensorimotor | Physical skill and sensorimotor intelligence. |
| Social & Personal | Genuine relationship, trust and interpersonal judgment. |
| Metacognitive & Supervisory | Plausibility auditing, problem formulation, and knowing when to distrust machine output. |
| Causal & Counterfactual | Variable selection, causal structure, intervention and counterfactual reasoning. |
| Collective & Distributed | Intelligence that emerges from groups of people in relationship. |
| Existential & Wisdom | Interpretive judgment, values integration, and knowing which question is worth asking. |

## Phase gates

| Phase | What happens | Gate |
|---|---|---|
| 0. Setup | This file. Nothing downloaded. | Done 2026-11-22 |
| 1. Inventory | Find what exists across repos, the Mac and the Explorer cluster. Record it in `data/manifest.yaml`; write `INVENTORY_REPORT.md`. | Done 2026-11-22 |
| 2. Acquire | Download only the open datasets a person approves, with provenance and checksums. Anything licensed or needing an account or API key becomes a human action item. | **In part**: decisions 1, 2, 3, 5, 6, 7 and 13 answered 2026-11-23; the rest wait |
| 3. Harmonize | Crosswalk every dataset to O\*NET-SOC 2019 (rolls up to SOC 2018), against O\*NET 31.0 (decision 7); build join tables; report coverage per source and across all sources. | After sign-off |

## Rules

1. **Never fabricate.** Anything not found is written "not found".
2. **Labour is separated.** The agent searches, downloads approved open data, transforms and reports. The person decides scope, licensing, facet definitions and sign-off.
3. **No access workarounds.** No account registration, no credentials that weren't given, no scraping of sites whose terms forbid it (LinkedIn, Indeed).
4. **Verify current facts at the source.** Release versions and dates come from the source, not from memory.
5. **Provenance on everything.** Each dataset records source, licence, version and retrieval date. The sign-off fields stay blank until a person fills them in.
6. **Machine labels stay separate.** Model-made facet tags carry the model name and version and are kept apart from any human-coded gold set.
7. **Storage.** Large raw data goes to the Explorer cluster (`/projects/aiskunks/`), not git. Git holds manifests, code and small derived tables. Licensed data never goes in a public repo.
8. **The AI Exposure Explorer's production code is never modified** (`/Users/bear/Documents/CoWork/bear-textbooks/books/Irreducibly-Human`).

## Standing decisions by Bear

These come from Bear's answers to the decisions in `INVENTORY_REPORT.md`. They add to the rules above and do not replace them.

| Date | Decision | What it binds |
|---|---|---|
| 2026-11-23 | 3, option (b) | LinkedIn and Indeed job postings scraped by third parties (the Kaggle sets asaniczka/1-3m-linkedin-jobs-and-skills-2024, scrapifier/indeed-usa-job-postings and arnabk123/data-science-data-analyst-and-ml-jobs-from-indeed) are used for **aggregate counts only, never quoting posting text**. We still never scrape LinkedIn or Indeed ourselves (rule 3). The Glassdoor scrapes in the Kaggle archive are not covered. |
| 2026-11-23 | 7, option (a) | **O\*NET 31.0 (August 2026) is the project's reference release.** Every descriptor, task and DWA is read from `explorer:/projects/aiskunks/onet/31.0/`. The 30.3 file renames are accepted. Work Styles (rebuilt in 30.1 by an AI-expert hybrid method) is flagged as partly machine-made wherever it is used. 30.2 is used only as a bridge for IDs in sources built on it. If a later O\*NET release appears, the project stays on 31.0 unless a person decides again. |
| 2026-11-23 | 13 | **The repo is private:** https://github.com/nikbearbrown/the-human-share. Raw downloads (`data/raw/`) and any key from coder IDs to names stay out of git. Large raw data stays on the cluster (rule 7). There is no licence file until a person names the owner. |

## Layout

| Path | Contents |
|---|---|
| `/Users/bear/Documents/CoWork/the-human-share/PROJECT.md` | This file |
| `/Users/bear/Documents/CoWork/the-human-share/data/manifest.yaml` | One entry per dataset |
| `/Users/bear/Documents/CoWork/the-human-share/INVENTORY_REPORT.md` | Status, which RQs can be answered now, decisions needed, and the sign-off log |
| `/Users/bear/Documents/CoWork/the-human-share/data/raw/` | Small open downloads, one dated folder per source with `SOURCE.txt` (gitignored) |
| `/Users/bear/Documents/CoWork/the-human-share/data/machine-labels/` | Model-made labels, each with the model name and version, its instructions and its runs (rule 6). First: `onet-abilities-facet-crosswalk/` |
| `/Users/bear/Documents/CoWork/the-human-share/data/gold/` | Human coding sheets, kept apart from the machine labels. Blank until a person codes them |
| `/Users/bear/Documents/CoWork/the-human-share/scripts/` | Small scripts that made the derived tables and checks |
| https://github.com/nikbearbrown/the-human-share | Private GitHub remote (decision 13). Holds everything here except `data/raw/` and coder keys |
| `explorer:/projects/aiskunks/the-human-share/` | Large raw files (`raw/`), Slurm fetch scripts and logs (`fetch-logs-<date>/`), `README.txt` |

Note on naming: the brief says "Discovery cluster". Northeastern's current cluster is **Explorer**, and the project's storage is there (`/projects/aiskunks`). The brief's `nikbearbrown/skills-lexicon` was renamed `nikbearbrown/irreducibly-human-work-lexicon` on 2026-11-22; the old URL redirects.
