# Human coding: O\*NET abilities to the seven facets

**Status: ready to send. The coders aren't named yet, and nothing is coded.**

On 2026-11-23 Bear decided (decision 6) that fellows or TAs code the human gold set. This folder holds the human side of the abilities-to-facets crosswalk. The machine draft is kept apart, in `/Users/bear/Documents/CoWork/the-human-share/data/machine-labels/onet-abilities-facet-crosswalk/` (project rule 6).

signed_off_by:
signed_off_on:

## What to send each coder

Send each coder **two files and nothing else**:

| Coder | Files | Row order |
|---|---|---|
| coder-01 | `CODEBOOK.md` and `coder-01.tsv` | first to last, as in O\*NET |
| coder-02 | `CODEBOOK.md` and `coder-02.tsv` | last to first, so tiredness doesn't fall on the same items |

Coders must not see the machine labels, this README, the project's other files or each other's sheets. The guide asks them not to use AI tools.

**Names stay out of the repo.** If the key from coder ID to person is written down, it goes in `coders-private.tsv` in this folder, which `.gitignore` keeps out of git.

## Plan once the sheets come back

1. **Check the sheets.** Each should have 52 rows, valid facet names, and fit values that match `no_fit`.
2. **Human against human.** Report agreement on the primary facet: percent and Cohen's kappa, overall and by O\*NET category. This tests whether the facet definitions can be applied reliably by people.
3. **Settle the disagreements.** A third person (Bear, or a third coder given a sheet with the same blank columns) picks the gold label for each disagreement. Both coders' original labels are kept beside it.
4. **Human against machine.** Compare the gold labels with machine runs A and B. Report kappa and say where they differ.
5. **Sign-off.** Bear fills in `signed_off_by` and `signed_off_on`, here and in `/Users/bear/Documents/CoWork/the-human-share/data/manifest.yaml`.

Steps 1, 2 and 4 are the agent's job. Steps 3 and 5 are a person's.

## Files

| File | What it is |
|---|---|
| `CODEBOOK.md` | The coders' guide: the rules, the facet definitions word for word, and how to fill in the sheet |
| `coder-01.tsv`, `coder-02.tsv` | Blank sheets with 52 rows each |
| `review-sheet.tsv` | The blank template the coder sheets were made from. Don't send it. |

## Attribution

The ability names and descriptions come from `Content Model Reference.txt` in O\*NET 31.0. O\*NET asks for this text:

> This page includes information from the O\*NET 31.0 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET® is a trademark of USDOL/ETA.

**What we changed:** the project kept the 52 ability rows and added empty columns for coding. USDOL/ETA has not approved, endorsed, or tested these modifications.
