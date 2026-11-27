# The Human Share

**Measuring what AI-era jobs ask of people, and whether courses teach it.** Part of the Irreducibly Human project.

[Read the project plan](PROJECT.md) · [How to contribute](CONTRIBUTING.md)

**We're inviting collaborators.** Review one claim, check a source, or take on one of the tasks listed below. You don't need to review the whole paper to help. To join, follow [Getting started](CONTRIBUTING.md#getting-started) in the contributor guide.

## Abstract

*Working abstract. A rough methods manuscript is available. It reports no study results.*

Published measures of AI exposure are built on O\*NET's descriptors of occupations. This paper asks how much of what jobs ask of people those descriptors cover. It uses the seven-facet classification of work from the Irreducibly Human project. In a draft crosswalk, 47 of O\*NET's 52 abilities fall into two facets, and four facets have none. We propose to test whether three other sources can fill the gap: job listings, which carry recency and seniority; courses' graded work, which shows what is practised; and observed AI-usage data, which shows how AI is used in tasks. The paper also proposes a teaching principle: by the end of a course, its use of AI should match the job's, and any difference should be declared and justified. The crosswalk is a machine draft that still needs independent human coding.

## Where the draft is

The [rough methods manuscript and Critique review](critiq-output/) are available. The underlying plan is [PROJECT.md](PROJECT.md), which sets out the argument and the five research questions.

## What needs to be done

- Code the abilities-to-facets crosswalk by hand, with independent coders.
- Settle the open decisions about which data sources to use ([INVENTORY_REPORT.md](INVENTORY_REPORT.md)).
- Acquire the remaining sources. Only some have been downloaded.
- Run the analysis for each research question. Nothing has been analysed.
- Review and revise the rough manuscript.

## How to contribute

Start with [Getting started](CONTRIBUTING.md#getting-started) in the [contributor guide](CONTRIBUTING.md): read the draft or plan, pick one thing to do, and email Nik to be added as a collaborator. The guide lists each kind of contribution with where to start and what to send, the rules for this repo, how to submit, and how credit and authorship work.

- **A quick contribution:** open an issue about one claim, source or decision. You don't need to review the whole paper.
- **To become an author:** take on a component of the work, help write the paper, approve the final version and agree to be accountable for it. The guide explains each step.

## What is here

| File | What it is |
|---|---|
| [PROJECT.md](PROJECT.md) | The argument, the research questions, the facet definitions and the current phase |
| [INVENTORY_REPORT.md](INVENTORY_REPORT.md) | The inventory of data sources, with the decisions made and still open |
| [data/manifest.yaml](data/manifest.yaml) | Every dataset considered, with its provenance and terms |
| [Fall 2026 and Spring 2027 syllabus corpus](data/course-corpus.tsv) | Section metadata and provenance; see [coverage and coding rules](data/README.md) |
| [data/gold/](data/gold/) | The hand-coding kit for the O\*NET abilities-to-facets crosswalk |
| [data/machine-labels/](data/machine-labels/) | The machine-drafted crosswalk and the comparison between its runs |
| [scripts/](scripts/) | Scripts that extract the abilities and compare label runs |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Ways to help, the rules for this repo, and authorship |

Raw third-party data is not in this repo. Each source's licence governs redistribution.
