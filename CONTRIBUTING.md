# Help build The Human Share

*The Human Share: Measuring What AI-Era Jobs Ask of People, and Whether Courses Teach It* argues that O\*NET, and the AI exposure indices built on it, measure only part of what jobs ask of people. Job listings, graded coursework and observed AI-usage data can fill the gap. The argument and the five research questions are in [PROJECT.md](PROJECT.md).

**Where it stands:** this repo is the paper's data foundation. There is no manuscript yet and nothing has been analysed. The data inventory is done, and some decisions about which sources to download are still open ([INVENTORY_REPORT.md](INVENTORY_REPORT.md)).

**If you have an hour:** read the argument in [PROJECT.md](PROJECT.md) and [open an issue](https://github.com/nikbearbrown/the-human-share/issues/new) naming one step you would keep, change or qualify, with a source or example.

## Pick a way to help

| Contribution | Where to start | What to send |
|---|---|---|
| **Code the abilities-to-facets crosswalk by hand** | [Gold-set README](data/gold/onet-abilities-facet-crosswalk/README.md) and [codebook](data/gold/onet-abilities-facet-crosswalk/CODEBOOK.md) | The paper's first claim rests on mapping O\*NET's 52 abilities to the seven facets. The current mapping is a machine draft and needs independent human coders. Open an issue to be assigned a coder ID before you start, and code without looking at the machine labels. |
| **Challenge the machine draft** | [Machine-label README](data/machine-labels/onet-abilities-facet-crosswalk/README.md) and its comparison file | Pick an ability where the two runs disagree, or where you think both are wrong. Give the ability, the facet you would assign and your reason. |
| **Check a data source** | [data/manifest.yaml](data/manifest.yaml) and the [inventory report](INVENTORY_REPORT.md) | Pick one dataset. Confirm its version, licence and what it measures, with a link to the primary source. Say if redistribution is restricted. |
| **Suggest a source for an under-measured facet** | Research questions in [PROJECT.md](PROJECT.md) | A dataset, survey or study that measures supervisory, causal, collective or judgment work. Give the population, years and access terms. |
| **Review the research questions** | [PROJECT.md](PROJECT.md) | An alternative explanation, a confound, or a measure that would not show what the question asks. |

## Rules for this repo

- **Don't change the facet definitions.** They are a fixed schema shared with other projects. If you think one is wrong, open an issue.
- **Coder names stay out of the repo.** Coding sheets carry coder IDs only.
- **No raw third-party data.** Each source's licence governs redistribution, so raw downloads are kept out of git.

## How to submit

For a discussion, [open an issue](https://github.com/nikbearbrown/the-human-share/issues/new) with the file or section, your evidence, and a proposed next step. For an edit, fork, branch, and open a focused pull request. Say what you changed and how you checked it. If you use an AI-generated answer, verify its citations and claims before submitting it.

If you want to collaborate beyond a single contribution, open an issue describing what you'd like to take on, and read [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors) first.

## Credit and what we expect from authors

The author list isn't decided yet. We follow [Yale's guidance on authorship](https://provost.yale.edu/policies/academic-integrity/guidance-authorship-scholarly-or-scientific-publications). Under it, an author has done **all four** of these:

1. **Contributed to a component of the work:** its conception, design, conduct, analysis, or interpretation of at least part of the results.
2. **Helped write the paper:** drafted part of it, or revised it for substance, not just copy edits.
3. **Approved the final version** before submission.
4. **Agreed to be accountable** for the work, including helping answer questions about its accuracy or integrity.

Some contributions are valuable but don't by themselves make someone an author: a single issue, one checked source, or reviewing a finished draft to offer suggestions. Everyone who contributes that way is thanked by name in the acknowledgments, unless they ask not to be. To be an author, take on a component, such as coding the full crosswalk as an independent coder, building one of the measures behind a research question, or auditing a whole group of data sources, and then do the writing, approval and accountability steps too. An AI model can't be an author, since it can't approve the paper or answer for it.

If you want to be an author, we expect you to:

- **Read the whole paper,** not just your section. You're putting your name on all of it.
- **Think about it, then give feedback.** Does the method answer the question? Are the comparisons fair? Do the numbers in the text match the tables, figures and data?
- **Suggest changes when they matter.** Don't make a suggestion just to have made one. If you find nothing to change, say so; that's a useful answer. A real problem, raised clearly with a proposed fix, is the most valuable thing you can give.
- **Disclose AI assistance.** AI tools are fine for code and drafting, but say where you used them. You stay accountable for everything you contribute.
- **Keep a record of what you did:** what, when, and where it lives (issue, pull request, commit, figure). The paper's contribution statement is drawn from it and lists each author's [CRediT roles](https://credit.niso.org/).
- **Sign off only when you can stand behind it.** Before submission, every author confirms in writing that they have read the full paper, agree with it, and accept accountability for it. If something is wrong or unclear, say so before approval, not after publication.

Raise authorship early, and we'll revisit it as roles change. Author order follows contribution. If you think your work merits authorship and it isn't reflected, say so before the final draft. Sending an issue or pull request does not by itself settle authorship.

## Licence

No licence has been chosen for this repo yet. Until one is, ask before reusing its text or data elsewhere.
