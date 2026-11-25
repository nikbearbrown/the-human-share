# Help build The Human Share

*The Human Share: Measuring What AI-Era Jobs Ask of People, and Whether Courses Teach It* argues that O\*NET, and the AI exposure indices built on it, measure only part of what jobs ask of people. Job listings, graded coursework and observed AI-usage data can fill the gap. The argument and the five research questions are in [PROJECT.md](PROJECT.md).

**Where it stands:** this repo is the paper's data foundation. There is no manuscript yet and nothing has been analysed. The data inventory is done, and some decisions about which sources to download are still open ([INVENTORY_REPORT.md](INVENTORY_REPORT.md)).

**If you have an hour:** read the argument in [PROJECT.md](PROJECT.md) and [open an issue](https://github.com/nikbearbrown/the-human-share/issues/new) naming one step you would keep, change or qualify, with a source or example.

## Getting started

Follow these steps in order. Steps 1 to 3 get you access. Steps 4 to 9 take one contribution from start to finish.

1. **Read first.** Read the [README](README.md), then the [project plan](PROJECT.md). Allow about an hour. You don't need to follow every detail, but you should know what the paper claims and what it does not.
2. **Choose one thing to do.** Pick one row from the table under [Pick a way to help](#pick-a-way-to-help), and narrow it to one section, one source, one case or one result. If you can't decide, review one section of the project plan.
3. **Email Nik** at bear@bearbrown.co with the subject "The Human Share: contributor". Include:
   - your name and your GitHub username;
   - the contribution you chose and what exactly you will look at;
   - whether you hope to become an author or want to help without authorship.

   Nik will add you to the repository as a collaborator. GitHub then emails you an invitation, which you must accept within seven days.
4. **Claim the work.** Check the [open issues](https://github.com/nikbearbrown/the-human-share/issues) to make sure nobody is already doing it. Then [open an issue](https://github.com/nikbearbrown/the-human-share/issues/new) that says what you are taking on, and assign it to yourself.
5. **Make a branch.** Clone the repository and create a branch named `your-name/short-description`, for example `priya/check-aioe-licence`. Do not commit to `main`. If you don't use git, edit the file on GitHub with the pencil button and choose "Create a new branch" when you save.
6. **Do the work.** Follow what the table asks you to send for the row you chose. Keep one branch to one piece of work.
7. **Open a pull request.** Say what you changed, how you checked it, and where you used an AI tool. Write "Closes #" and your issue's number so the two are linked, and request a review from `nikbearbrown`.
8. **Respond to the review.** Nik or another author will comment. Revise on the same branch until it is agreed, and it will be merged.
9. **Present your work.** Come to Nik's Tuesday meeting or his office hours with a short, clear presentation of what you have done. Cover what you set out to do, what you did, what you found and the evidence for it, and what you will do next or need help with. Do this each time you attend, even when the work is unfinished. Nik will send the meeting details when he adds you.
10. **Keep your record.** Your issues and pull requests are the record of what you did. If you hope to be an author, keep a list of them, because the paper's contribution statement is drawn from it.
11. **Take the next step.** Pick another piece of work. If you want to be an author, tell Nik early and read [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors).

You can also help without access. Anyone can open an issue on this repository without emailing first.

## Pick a way to help

| Contribution | Where to start | What to send |
|---|---|---|
| **Code the abilities-to-facets crosswalk by hand** | [Gold-set README](data/gold/onet-abilities-facet-crosswalk/README.md) and [codebook](data/gold/onet-abilities-facet-crosswalk/CODEBOOK.md) | The paper's first claim rests on mapping O\*NET's 52 abilities to the seven facets. The current mapping is a machine draft and needs independent human coders. Open an issue to be assigned a coder ID before you start, and code without looking at the machine labels. |
| **Challenge the machine draft** | [Machine-label README](data/machine-labels/onet-abilities-facet-crosswalk/README.md) and its comparison file | Pick an ability where the two runs disagree, or where you think both are wrong. Give the ability, the facet you would assign and your reason. |
| **Check a data source** | [data/manifest.yaml](data/manifest.yaml) and the [inventory report](INVENTORY_REPORT.md) | Pick one dataset. Confirm its version, licence and what it measures, with a link to the primary source. Say if redistribution is restricted. |
| **Suggest a source for an under-measured facet** | Research questions in [PROJECT.md](PROJECT.md) | A dataset, survey or study that measures supervisory, causal, collective or judgment work. Give the population, years and access terms. |
| **Review the research questions** | [PROJECT.md](PROJECT.md) | An alternative explanation, a confound, or a measure that would not show what the question asks. |
| **Recommend a journal Northeastern covers in full** | [Recommend a journal](#recommend-a-journal-northeastern-covers-in-full), below | One recommended journal and a runner-up, with the evidence that section asks for. Every contributor does this once. |

## Rules for this repo

- **Don't change the facet definitions.** They are a fixed schema shared with other projects. If you think one is wrong, open an issue.
- **Coder names stay out of the repo.** Coding sheets carry coder IDs only.
- **No raw third-party data.** Each source's licence governs redistribution, so raw downloads are kept out of git.

## Recommend a journal Northeastern covers in full

Every contributor is asked to do this once. Northeastern's library has agreements with publishers that pay the open-access publishing fee for its authors. The library's page says the agreements are "open to all current Northeastern faculty, students and staff who are corresponding authors." Nik is the corresponding author on this paper, so they apply. Your job is to find a journal that is a good fit for this paper and whose fee is covered in full.

1. **Know the paper.** Read the abstract and the draft, or the plan if there is no draft yet. Note the field, the method, the kind of article (research, review, tool, dataset) and its likely length.
2. **Open the library's list.** Read [Open access publishing at Northeastern](https://library.northeastern.edu/resource_discovery/open-access-publishing/) and use its journal search, [SciFree for Northeastern](https://search.scifree.se/northeastern).
3. **Keep only full coverage.** Some agreements pay 100% of the fee and some only give a discount. A discount does not count. Some publishers also cap the number of articles they cover in a year, so note any cap the page states.
4. **Shortlist three journals** and check each one on the publisher's own site:
   - **Scope:** does the journal's aims and scope cover this paper's question and method?
   - **Article type:** does the journal accept this kind of article, and does the agreement cover that type?
   - **Precedent:** two or three recent papers in the journal that are close to this one, with links.
   - **Preprints and public drafts:** this paper's draft is in a public repository. Does the journal allow that, and is its review double-blind?
   - **Practical limits:** length limit, typical time to a first decision, and any data or code requirements.
5. **Recommend one journal and a runner-up.** [Open an issue](https://github.com/nikbearbrown/the-human-share/issues/new) titled "Venue recommendation: " and the journal's name. Give your reasons, the links you used and the date you checked each fact.

Confirm coverage on the library's page or the publisher's page yourself. Do not rely on memory or on an AI tool's answer, because the agreements and their caps change.

## How to submit

For a discussion, [open an issue](https://github.com/nikbearbrown/the-human-share/issues/new) with the file or section, your evidence, and a proposed next step. For an edit, open a focused pull request from a branch (collaborators) or from a fork (everyone else). Say what you changed and how you checked it. If you use an AI-generated answer, verify its citations and claims before submitting it.

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
