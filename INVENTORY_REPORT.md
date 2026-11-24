# The Human Share: Phase 1 inventory report

Inventory taken 2026-11-22; updated 2026-11-23.

**Update 2026-11-23:** Bear approved the small open downloads ("Approve small ones"). Three sources were fetched with checksums: the Yale Budget Lab workbook, Microsoft's working-with-ai data and the O\*NET-SOC 2010-to-2019 crosswalk (see the sign-off log at the end). Later the same day Bear chose "Latest + 2025-03-27" for the Anthropic Economic Index (decision 2). The 2025-03-27 release is on the Mac; the 2026-06-26 release (296 MB) is on the Explorer cluster. Bear then ruled on decision 3: LinkedIn and Indeed data scraped by third parties may be used for aggregate counts only, never quoting text. On decision 5 he said "Rebuild it": the abilities-to-facets crosswalk was rebuilt as a machine draft, from two blind model runs, and a blank human coding sheet sits beside it. Everything else still waits on the decisions below. Nothing has been analysed beyond checking that the files open and that their codes join.

## Executive summary

**Most of the foundation already exists.** The manifest (`/Users/bear/Documents/CoWork/the-human-share/data/manifest.yaml`) records 66 datasets:

| Status | Count |
|---|---:|
| have | 36 |
| partial | 13 |
| missing | 10 |
| needs a human | 7 |

(Counts after the 2026-11-23 downloads and decisions 3 and 5. On 2026-11-22 they were 30, 11, 17 and 8.)

**What is already in hand:**
- **The full current O\*NET release (31.0, August 2026)** is on the Explorer cluster.
- **Two exposure indices (Eloundou, Felten AIOE) and the BLS AI exposure categories** are on disk.
- **One day of 53,331 job descriptions** and a daily feed of about 85,000 postings, with titles only.
- **Bear's own course repositories, with graded work:** 8 courses and about 350 files named as assignments, rubrics, exams, quizzes or projects.
- **The 22 SEIS Fall syllabi**, plus the work lexicon (3,754 entries).

**No research question can be fully answered yet.** Four things block them:
1. **The abilities-to-facets crosswalk: rebuilt as a machine draft (2026-11-23).** The brief's draft was not found, so it was rebuilt from the facet definitions (decision 5). Two blind runs agree on 50 of 52 abilities (kappa 0.93) and reproduce the brief's pattern: 45 to 46 abilities fall into Pattern & Association or Embodied & Sensorimotor. Three facets get no ability at all. It is still a machine label: RQ1 can start, but it can't report the crosswalk as ground truth until a person codes the blank sheet (decision 6).
2. **Usage data: now in hand (2026-11-23).** The AEI 2026-06-26 release has automation and augmentation shares for 2,797 tasks, 745 DWAs, 210 IWAs and 716 occupations; 2025-03-27 adds a per-task baseline. Two limits: neither covers Claude Code, so coding work is under-represented; and the course side (assignment-level AI coding) doesn't exist yet.
3. **Exposure sources: now mostly in hand.** The Yale file and Microsoft's data were downloaded on 2026-11-23. But the Yale file holds z-scores for only 778 occupations and no per-occupation Webb scores, so Webb is still missing. DAIOE still needs a licence decision.
4. **No human-coded gold set exists for facets yet.** Every facet and phase label so far is model- or rule-made, so under rule 6 none can stand as ground truth. Bear decided on 2026-11-23 that fellows or TAs will code it (decision 6). The crosswalk coding packet is ready, but the coders aren't named yet.

**Four source changes will break code written against older layouts:**
- **O\*NET 30.3 (May 2026)** split Skills, renamed the IWA and DWA files, and renamed columns.
- **O\*NET Work Styles was rebuilt in 30.1 (December 2025)** "by a new hybrid artificial intelligence-expert method". So part of O\*NET is now itself machine-made, which bears directly on RQ1.
- **The Anthropic Economic Index changed its schema in the 2026-06-26 release.**
- **O\*NET renumbered DWA and IWA IDs between 30.2 and 31.0** (`4.A.1.a.1.I01.D01` became `4.A.1.a.1.a.1`). The AEI 2026-06-26 release uses the old IDs: all match 30.2, none match 31.0. Names still match, so the join goes by name or through 30.2. (Found 2026-11-23.)

**Two corrections to the brief:**
- **The cluster is Explorer, not Discovery.** The project storage is `/projects/aiskunks`.
- **The lexicon repo is now `nikbearbrown/irreducibly-human-work-lexicon`.** The old `skills-lexicon` URL redirects.

**Thirteen decisions are listed below; 1, 2, 3, 5, 6, 7 and 13 are now answered** (2026-11-23). The repo is now a private GitHub repo. The next step is a person's: naming two fellows or TAs and sending them the crosswalk packet. Of the open decisions, 9 (which courses are in the corpus) comes first, because the course side of RQ4 and RQ5 can't start without it.

## Status by dataset group

| Group | Have | Partial | Missing | Needs human | What it comes down to |
|---|---:|---:|---:|---:|---|
| A. O\*NET | 16 | 0 | 0 | 1 | **Complete.** O\*NET 31.0 (all 46 files) and 30.2 are on the cluster. The live Explorer database is on an older release (version unknown; I had no credentials to check). |
| B. BLS | 1 | 1 | 0 | 2 | **Behind.** OEWS May 2024 is held; May 2025 is current. Employment Projections 2025–35 is not held. bls.gov blocks scripted downloads, so a person must fetch these in a browser. |
| C. Exposure indices | 4 | 1 | 1 | 1 | **Mostly held (2026-11-23).** Eloundou, AIOE, the Yale workbook and Microsoft are held. Eisfeldt is held only as z-scores inside the Yale file. Webb is missing: the Yale file has no per-occupation Webb values. DAIOE has no licence. |
| D. Observed AI usage | 2 | 1 | 5 | 0 | **Enough for RQ5 (2026-11-23).** The AEI 2026-06-26 release (on the cluster) and 2025-03-27 (on the Mac) are held, as is task_penetration. The other four dated releases and robot_exposure were not fetched (Bear chose "Latest + 2025-03-27"). |
| E. Job listings | 3 | 3 | 1 | 2 | **Usable, with a limit.** ATS feeds are tech-skewed: one day with text, daily without. The 1.15M-posting LinkedIn 2024 set with seniority (on the cluster) is cleared for aggregate counts only, never quoting text (decision 3, 2026-11-23); the same limit covers the Indeed sets in the Kaggle archive. The Reallocation Engine stores no listings. |
| F. Course materials | 7 | 2 | 2 | 0 | **Bear's courses have graded work;** other SEIS courses have syllabi only. The catalog (fetch refused from here) and MIT OCW are missing. AI treatment is read from syllabi only. |
| G. Lexicon | 0 | 2 | 0 | 0 | **The lexicon is broad but unreviewed:** 0 of 3,754 entries are reviewed, 11% have relations, and it holds no work phases. **The abilities-to-facets crosswalk is a machine draft:** the brief's draft was not found, and it was rebuilt on 2026-11-23 (decision 5). Its human coding sheet is blank. |
| H. Crosswalks | 3 | 3 | 1 | 1 | **The key rollup for Phase 3 is held:** O\*NET-SOC 2019 to SOC 2018. The 2010-to-2019 crosswalk was downloaded on 2026-11-23. SOC 2010 to 2018 needs a browser download. The Yale file includes no crosswalk tables. |

## Which research questions can be answered now

| RQ | Can start now? | What's in hand | Blocked by |
|---|---|---|---|
| **RQ1**: coverage of the seven facets by O\*NET and exposure indices | **Partly (machine draft)** | All O\*NET descriptors (31.0); Eloundou, AIOE, BLS categories; Yale z-scores for six measures (778 occupations) and Microsoft (785 occupations, IWA level), both from 2026-11-23 | (a) the abilities-to-facets crosswalk is a machine draft (rebuilt 2026-11-23; two blind runs, kappa 0.93) until a person codes the blank sheet and signs off; (b) Webb has no per-occupation scores, and DAIOE has no licence; (c) facet tags for Skills, Knowledge, Work Activities and Work Context don't exist yet and would be machine labels until a person codes a sample |
| **RQ2**: demand conditions vs adjectives; seniority within vs across occupations | **Partly** | 53,331 descriptions (one day, ATS boards); a cue screen and a 12-posting pilot from the facets work; title-based seniority; the LinkedIn 2024 set (1.15M US postings with a seniority field), cleared for aggregate counts on 2026-11-23 | (a) no human gold set yet (decision 6: fellows or TAs will code it; the posting-line sample isn't drawn yet); (b) titles map to occupations for only 35% of LinkedIn postings; (c) results from the LinkedIn and Indeed sets can be reported only as counts and shares, never as quoted text |
| **RQ3**: share of listing tasks with no O\*NET match; is the residual supervisory? | **Partly** | O\*NET Task Statements, Tasks to DWAs and DWAs (31.0); 53,331 descriptions | (a) no task-line extraction or matching method yet; (b) to say "supervisory", the facet labels need the gold set |
| **RQ4**: phase profile of graded work vs listings | **Partly** | Bear's 8 courses with graded work; posting phase emphasis by occupation (a-new-shape-for-work, on the LinkedIn 2024 set); draft phase tags for DWAs, IWAs and 47,118 phrases | (a) phase schema mismatch: the brief has requirements, design, build, review and deploy, while the existing tags use six phases (decision 4); (b) course-to-job-title matching isn't built; (c) other SEIS courses have syllabi only, no graded work |
| **RQ5**: course AI use vs job AI use (automation vs augmentation) | **Job side yes; course side no** | AEI 2026-06-26 (automation and augmentation by task, DWA, IWA, GWA and occupation; April–May 2026); AEI 2025-03-27 (per-task baseline); Microsoft IWA metrics; syllabus-level AI policies for Bear's courses | (a) assignment-level AI coding (banned, delegated, engaged) isn't done; (b) neither AEI file covers Claude Code; (c) joins need care: the 2026 DWA/IWA IDs are O\*NET 30.2 IDs, and the 2025 release uses 2010 codes (566 of its 3,364 tasks don't match 31.0 text) |

## Decisions needed

1. **Approve the Phase 2 open downloads.** Large files go to the cluster. **Answered 2026-11-23: the small ones and the two AEI releases chosen in decision 2 are downloaded; robot_exposure was not approved.**

   | Dataset | Size | Licence | State |
   |---|---|---|---|
   | Yale Budget Lab file | 355 KB | not stated on the page | **downloaded 2026-11-23** |
   | Microsoft `working-with-ai` (7 CSVs) | about 3.2 MB (not "under 1 MB" as first written) | CC BY 4.0 | **downloaded 2026-11-23** |
   | O\*NET-SOC 2010-to-2019 crosswalk | 108 KB | CC BY 4.0 | **downloaded 2026-11-23** |
   | AEI 2026-06-26 | 296 MB | CC-BY | **downloaded 2026-11-23, to the cluster** |
   | AEI 2025-03-27 | 6.5 MB of data files (not 0.6 MB: that was one file) | CC BY | **downloaded 2026-11-23** |
   | AEI 2025-02-10, 2025-09-15, 2026-01-15, 2026-03-24 | 0.2 MB to about 147 MB | CC BY | not fetched (decision 2 chose b) |
   | AEI `robot_exposure` | about 100 MB | CC BY 4.0 | not approved |

   - **Options:** approve all; approve the small ones now and the AEI ones after decision 2; or approve item by item.
   - **Tradeoff:** the small files unblock most of RQ1 immediately. The AEI files are big and change schema between releases.
   - The cluster's rule is that fetches run as a Slurm job, and Bear says yes before it is submitted. This decision would be that yes.

2. **Which Anthropic Economic Index releases?** **Answered 2026-11-23: (b), "Latest + 2025-03-27". Both fetched.**
   - **(a) Latest only (2026-06-26, about 296 MB).** Automation and augmentation at task, DWA and IWA level in one schema. Simplest.
   - **(b) Plus 2025-03-27 (0.6 MB).** Adds an early per-task baseline cheaply.
   - **(c) All six.** A time series, but three schemas and mixed O\*NET vintages (the 2025-09 release documents O\*NET 20.1 tasks).
   - **Recommendation:** (b).

3. **Can LinkedIn and Indeed data scraped by third parties be used?** **Answered 2026-11-23: (b), aggregate counts only, never quoting text.** This covers the asaniczka LinkedIn set and the two Indeed posting sets on the allow-list. It does not cover the Glassdoor scrapes in the Kaggle archive, which were not part of the question. The brief forbids *us* scraping LinkedIn or Indeed. Kaggle sets such as asaniczka (ODC-By) and scrapifier Indeed (CC0) were scraped by others and carry open Kaggle licences.
   - **(a) Exclude.** The cleanest, but RQ2 then has no large set with seniority, and there is no US breadth outside tech ATS boards.
   - **(b) Use for aggregate counts only, never quoting text.** This is what a-new-shape-for-work does now.
   - **(c) Use fully, with a disclosure.**
   - Recommendation: (b) if you accept it, or (a) plus USAJOBS (decision 10) to add breadth.

4. **Phase schema for RQ4.** The brief has five phases (requirements, design, build, review, deploy). A New Shape for Work already uses six (understand, plan, produce, check, sustain, coordinate), with draft tags on every DWA, IWA and 47,118 posting phrases.
   - **(a) Adopt the six and map the brief's five onto them.** This reuses the existing tags.
   - **(b) Adopt the five.** Retag everything.
   - **(c) Keep both, joined by a fixed crosswalk.**
   - **Tradeoff:** (a) is fastest. The five read more naturally for software courses, but they fit non-software jobs poorly.

5. **Where is `onet-abilities-facet-crosswalk.md`?** I found it nowhere on the Mac, the cluster or Google Drive. The facets pilots quote its results but give no path.
   - **(a) You supply the file.**
   - **(b) Rebuild it from the facet definitions.** It would be a new machine label, not your draft, and would need your sign-off.
   - **Answered 2026-11-23: "Rebuild it".** The rebuild is in `/Users/bear/Documents/CoWork/the-human-share/data/machine-labels/onet-abilities-facet-crosswalk/`, and the blank human sheet is in `/Users/bear/Documents/CoWork/the-human-share/data/gold/onet-abilities-facet-crosswalk/`. It still needs a person to code that sheet and sign off (decision 6).

6. **Who codes the human gold set?** Every facet, phase and lexicon label is model- or rule-made. Claude-only coders agree with each other (kappa about 0.8), but rule 6 needs human codes. Metacognitive & Supervisory is the weakest facet (kappa 0.37 in one pair), and it is the facet RQ3 and RQ5 lean on most.
   - **Options:** you; TAs or fellows; external coders.
   - **Size:** about 200 posting lines plus about 100 syllabus or assignment units would test agreement.
   - **Answered 2026-11-23: "Fellows or TAs".**
     - The first piece is the crosswalk. A packet for two blind coders is in `/Users/bear/Documents/CoWork/the-human-share/data/gold/onet-abilities-facet-crosswalk/`: `CODEBOOK.md`, plus `coder-01.tsv` and `coder-02.tsv` in opposite row orders.
     - Coders are named only by ID in the repo.
     - Still to do:
       - Bear names the coders and sends the packets.
       - A third person settles disagreements.
       - The posting-line and syllabus samples are not drawn yet.

7. **Pin the O\*NET version.**
   - **(a) 31.0, current and recommended.** Accept the 30.3 renames and the AI-assisted Work Styles, and record that.
   - **(b) 30.2.** The old file layout, and still the new Work Styles.
   - Microsoft used O\*NET 29.0 and the AEI releases vary. Either way, tasks join by statement text or crosswalk.
   - **Answered 2026-11-23: "Pin 31.0".** The O\*NET releases page, rechecked that day, still says 31.0 is the current production release. What this means:
     - **File layout:** the 30.3 renames and the Skills split are accepted.
     - **Work Styles** was rebuilt in 30.1 by an AI-expert hybrid method. Wherever it's used, the paper flags it as partly machine-made.
     - **30.2 stays only as a bridge** for the AEI 2026-06-26 DWA and IWA IDs, which Phase 3 maps to 31.0 by name.
     - **Later releases:** if 31.1 or later appears, the project stays on 31.0 unless a person decides again.
     - The live Explorer database still runs an older release (decision 8).

8. **Bring the live Explorer database up to date?** It runs an O\*NET release older than 30.3, and its BLS data stops at 2024.
   - Rule 8 forbids touching its production code, and I had no database credentials.
   - **Options:** leave it and note the version gap in the paper; or you check the version with the connection string.

9. **Which courses are in the corpus?**
   - **(a) Bear's 8 courses.** They have graded work, but one instructor's style.
   - **(b) Plus the 12 confirmed SEIS Fall syllabi.** Broader, but syllabus only.
   - **(c) Plus MIT OCW.** CC BY-NC-SA; the NonCommercial term rules out a commercial tool.
   - Also: the Northeastern catalog refused connections from here, so it needs a browser fetch or the cluster.

10. **USAJOBS API key?** It's free, but a person must register (name, email, phone, organisation, intended use). It adds federal and non-tech postings with structured fields. **Options:** register; or skip.

11. **Lightcast?** Commercial; one marketplace listing is US$90,200 for 12 months. **Options:** skip; ask about academic access; or buy. Not needed to start.

12. **Data without a licence:** AIOE (no licence file) and DAIOE (none stated). **Options:** use for research with a citation and don't redistribute; or exclude.

13. **Storage and repo.**
    - Raw downloads would go to a new cluster folder, `/projects/aiskunks/the-human-share/`, in kebab-case.
    - This repo is local only (git initialised, nothing committed).
    - **Options:** create a private GitHub repo `nikbearbrown/the-human-share` and commit the manifest and docs; or keep it local for now.
    - **Answered 2026-11-23: "Private repo".** Created at https://github.com/nikbearbrown/the-human-share.
      - **Visibility:** private.
      - **What's committed:** the docs, the manifest, the machine-label and gold folders, and the scripts.
      - **What stays out of git:**
        - `data/raw/` (each source's licence governs redistribution, and large files live on the cluster);
        - any `coders-private.tsv`;
        - everything on the cluster.
      - **No licence file was added.** Who owns the repo (Humanitarians AI Incorporated, or Nik Bear Brown personally) is a person's call.

## How the search was done

- **The Mac.** I searched `/Users/bear/Documents`, `Downloads` and `Desktop` by file name for O\*NET, BLS, exposure, AEI and crosswalk files. I read the provenance notes in the job-shape, ai-exposure, ai-jobs, facets and lexicon folders.
- **The Explorer cluster (read-only SSH).** I listed `/projects/aiskunks/onet`, `kaggle/jobs`, `jobs` and `skills-lexicon-work`, and read their README and SOURCE files.
- **Google Drive.** I searched titles and full text for the crosswalk.
- **Source sites.** A sub-agent read the source pages, API listings and LICENSE files, and sent HEAD requests. No data files were fetched. Bear's earlier fetches carry their own provenance in each folder.
- **Not touched:** the AI Exposure Explorer code and database, and any account, key or credential.
- **A detail for RQ1 and RQ5:** the Yale file has no Anthropic Economic Index measure; the page doesn't mention it. So observed-usage data has to come from the AEI and Microsoft sources directly.

## Sign-off log

The manifest's `signed_off_by` and `signed_off_on` fields stay blank until a person fills them in. This log only records what was approved in chat and what was done.

| Date | What Bear said | What was done |
|---|---|---|
| 2026-11-23 | "Approve small ones", in answer to "Sign off and approve the small open downloads?" | Downloaded three open sources on the Mac, each into its own dated folder under `/Users/bear/Documents/CoWork/the-human-share/data/raw/`, each with a `SOURCE.txt` (URL, date, size, sha256, licence, row counts). They are kept out of git by `.gitignore` until decision 13. The manifest entries are updated. No AEI release, BLS file or Kaggle data was fetched. |
| 2026-11-23 | "Latest + 2025-03-27", in answer to "Which Anthropic Economic Index releases should I fetch?" | **2025-03-27:** the 9 CSV/TSV data files and 2 READMEs (6.5 MB) went to `/Users/bear/Documents/CoWork/the-human-share/data/raw/aei-release-2025-03-27/2026-11-23/`; the figures and notebooks were left out. **2026-06-26:** Slurm job 12089073 fetched the two CSVs and the documentation (296 MB) to `explorer:/projects/aiskunks/the-human-share/raw/aei-release-2026-06-26/2026-11-23/` in 54 seconds, with a README.txt per the cluster conventions. The Mac folder of the same name holds a pointer and the documentation. Both are pinned to Hugging Face dataset commit 4e5f69f, and every file's size and hash match Hugging Face's. No other release, and not robot_exposure, was fetched. |
| 2026-11-23 | "Counts only (b)", in answer to "Can we use LinkedIn and Indeed data that others scraped, for aggregate counts only (decision 3)?" | Recorded as a use limit, with nothing downloaded or opened. In the manifest, `kaggle_linkedin_2024_asaniczka` moved from needs_human to have, with the limit in its notes. `kaggle_jobs_archive` notes now name the three LinkedIn and Indeed sets the limit covers, and say the Glassdoor scrapes are not covered. PROJECT.md lists the limit under "Use limits decided by Bear". |
| 2026-11-23 | "Rebuild it", in answer to "Where is onet-abilities-facet-crosswalk.md (decision 5)?" | Searched once more for the original by ability names in the facets, lexicon and Irreducibly-Human folders: not found. Took the 52 abilities and their descriptions from O\*NET 31.0 `Content Model Reference.txt` on the cluster (sha256 checked; the same 52 IDs as `Abilities.txt`). Wrote labelling instructions with the seven facet definitions word for word and no expected distribution. Two Claude Code subagents (claude-opus-5-5) labelled all 52 blind, in opposite row orders; their transcripts show that each opened only the instructions and the ability table. Result: agreement 50/52 (kappa 0.930); 45–46 abilities in Pattern & Association or Embodied & Sensorimotor; no ability in Social & Personal, Collective & Distributed or Existential & Wisdom; Deductive Reasoning, Number Facility, Selective Attention and Time Sharing fit no facet in either run. Files: `/Users/bear/Documents/CoWork/the-human-share/data/machine-labels/onet-abilities-facet-crosswalk/`. A blank, blind human coding sheet: `/Users/bear/Documents/CoWork/the-human-share/data/gold/onet-abilities-facet-crosswalk/review-sheet.tsv`. The manifest entry moved from missing to partial. Nothing was downloaded from outside, and nothing is signed off. |
| 2026-11-23 | "Fellows or TAs", in answer to "Who codes the blind crosswalk sheet (decision 6)?" | Recorded as decision 6. In `/Users/bear/Documents/CoWork/the-human-share/data/gold/onet-abilities-facet-crosswalk/` I made a packet for two blind coders: `CODEBOOK.md` (the facet definitions word for word, the same rules the machine runs had, no AI tools, no conferring, no expected spread) and the sheets `coder-01.tsv` (O\*NET order) and `coder-02.tsv` (reverse order). Coders appear only as IDs. `.gitignore` keeps any `coders-private.tsv` key out of git. The README sets out the plan: human-against-human kappa, a third person settles disagreements, then the gold set is compared with the machine runs, then Bear signs off. Nobody was contacted, and no coder is named. |
| 2026-11-23 | "Pin 31.0", in answer to "Pin O\*NET 31.0 for the project (decision 7)?" | Rechecked https://www.onetcenter.org/db_releases.html that day: "The current production release of the O\*NET database is 31.0". The 31.0 entry in the manifest is marked pinned. Work Styles is flagged as partly machine-made, and 30.2 is kept as the bridge for the AEI DWA and IWA IDs. PROJECT.md lists the pin under "Standing decisions by Bear". Nothing was downloaded. |
| 2026-11-23 | "Private repo", in answer to "Create a private GitHub repo for The Human Share (decision 13)?" | Created the private repo https://github.com/nikbearbrown/the-human-share. Before committing I listed the files and scanned them for email addresses, tokens, passwords, connection strings and personal names (none found). Committed and pushed `main`: PROJECT.md, INVENTORY_REPORT.md, `data/manifest.yaml`, the machine-label and gold folders for the crosswalk, and two scripts. `data/raw/` and any coder key stay out of git, and no licence file was added. |

**What opening the files showed (2026-11-23):**
- **Yale:** a figures-and-tables workbook with 15 sheets. Per-occupation data covers 778 SOC 2018 occupations: z-scores for AIOE, Eloundou GPT-4 and human beta, Eisfeldt total and core, Tomlinson applicability, the PCA score and the cross-measure variance. **Webb has no per-occupation values**, the 867- and 710-occupation sets aren't in the file, and it has no crosswalk tables.
- **Microsoft (commit 550c00c):** 785 occupations and 332 IWAs, with user-side and AI-side metrics per IWA. Built on O\*NET 29.0 and Copilot conversations from January to September 2024.
- **O\*NET-SOC 2010-to-2019 crosswalk:** 1,164 rows, matching the source page.
- **AEI 2026-06-26:** long format (period × geography × node × metric), April and May 2026, 53 metrics.
  - `aei_claude_ai` (chat and Cowork; global, country, subregion): 1,636,573 rows.
  - `aei_1p_api` (global only): 491,705 rows.
  - Neither file covers Claude Code.
  - Automation and augmentation shares are published for 2,797 tasks, 745 DWAs, 210 IWAs, 35 GWAs and 716 occupations (claude_ai, global).
  - Task IDs are O\*NET 31.0 IDs (2,820 of 2,823), and all 718 occupation codes are in 31.0. DWA and IWA IDs are in the O\*NET 30.2 format (see the source-change note in the summary).
  - The documentation says "CC-BY" with no version. The manifest's earlier "CC BY 4.0" is corrected.
- **AEI 2025-03-27:** per-task collaboration ratios for 3,364 tasks (directive, feedback loop, task iteration, validation, learning, filtered); the README calls the first two automation patterns and the next three augmentation. It has no automation/augmentation bucket field.
  - The task statements use O\*NET-SOC 2010 codes (974 codes, dates up to 2015). The release does not name its O\*NET version.
  - 2,798 tasks match O\*NET 31.0 text exactly. The other 566 join through the 2010-to-2019 crosswalk.
- The inspection scripts and their outputs are in `explorer:/projects/aiskunks/the-human-share/fetch-logs-2026-11-23/`. They only read the data.
