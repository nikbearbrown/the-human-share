# The Human Share: Phase 1 inventory report

Inventory taken 2026-11-22; updated 2026-11-27.

**Update 2026-11-23:** Bear approved the small open downloads ("Approve small ones"). Three sources were fetched with checksums: the Yale Budget Lab workbook, Microsoft's working-with-ai data and the O\*NET-SOC 2010-to-2019 crosswalk (see the sign-off log at the end). Later the same day Bear chose "Latest + 2025-03-27" for the Anthropic Economic Index (decision 2). The 2025-03-27 release is on the Mac; the 2026-06-26 release (296 MB) is on the Explorer cluster. Bear then ruled on decision 3: LinkedIn and Indeed data scraped by third parties may be used for aggregate counts only, never quoting text. On decision 5 he said "Rebuild it": the abilities-to-facets crosswalk was rebuilt as a machine draft, from two blind model runs, and a blank human coding sheet sits beside it. Everything else still waits on the decisions below. Nothing has been analysed beyond checking that the files open and that their codes join.

**Update 2026-11-24 to 2026-11-27:** Bear set the course corpus (decision 9): his 8 courses plus the 12 confirmed SEIS Fall syllabi. The list is in `/Users/bear/Documents/CoWork/the-human-share/data/course-corpus.tsv`. While recording it I found that three of the eight course folders are no longer on the Mac. Their GitHub repos are intact (see decision 9). Bear then chose the phase schema (decision 4): the six phases of A New Shape for Work, with the brief's five mapped onto them. The draft map is in `/Users/bear/Documents/CoWork/the-human-share/data/phase-schema/`. On 2026-11-25 Bear chose Sustain for its deploy row, the one row Bear's documents left open, so every row of the map is now set; the map is not yet signed off. On 2026-11-26 Bear allowed the two unlicensed indices, AIOE and DAIOE, for research with a citation, never redistributed (decision 12). On 2026-11-27 Bear chose to leave the live Explorer database as it is and have the paper state its version gap (decision 8). The same day Bear chose to keep the GitHub repo public, which replaces the private setting of decision 13.

## Executive summary

**Most of the foundation already exists.** The manifest (`/Users/bear/Documents/CoWork/the-human-share/data/manifest.yaml`) records 66 datasets:

| Status | Count |
|---|---:|
| have | 36 |
| partial | 13 |
| missing | 12 |
| needs a human | 5 |

(Counts after the 2026-11-23 downloads and decisions 3, 5, 8 and 12. Decision 12 moved DAIOE from needs a human to missing: it may be used, but isn't downloaded. Decision 8 moved the Explorer database there too: it isn't held and isn't needed. On 2026-11-22 the counts were 30, 11, 17 and 8.)

**What is already in hand:**
- **The full current O\*NET release (31.0, August 2026)** is on the Explorer cluster.
- **Two exposure indices (Eloundou, Felten AIOE) and the BLS AI exposure categories** are on disk.
- **One day of 53,331 job descriptions** and a daily feed of about 85,000 postings, with titles only.
- **Bear's own course repositories, with graded work:** 8 courses and about 350 files named as assignments, rubrics, exams, quizzes or projects.
- **The 22 SEIS Fall syllabi**, plus the work lexicon (3,754 entries).

**No research question can be fully answered yet.** Four things block them:
1. **The abilities-to-facets crosswalk: rebuilt as a machine draft (2026-11-23).** The brief's draft was not found, so it was rebuilt from the facet definitions (decision 5). Two blind runs agree on 50 of 52 abilities (kappa 0.93) and reproduce the brief's pattern: 45 to 46 abilities fall into Pattern & Association or Embodied & Sensorimotor. Three facets get no ability at all. It is still a machine label: RQ1 can start, but it can't report the crosswalk as ground truth until a person codes the blank sheet (decision 6).
2. **Usage data: now in hand (2026-11-23).** The AEI 2026-06-26 release has automation and augmentation shares for 2,797 tasks, 745 DWAs, 210 IWAs and 716 occupations; 2025-03-27 adds a per-task baseline. Two limits: neither covers Claude Code, so coding work is under-represented; and the course side (assignment-level AI coding) doesn't exist yet.
3. **Exposure sources: now mostly in hand.** The Yale file and Microsoft's data were downloaded on 2026-11-23. But the Yale file holds z-scores for only 778 occupations and no per-occupation Webb scores, so Webb is still missing. DAIOE may now be used with a citation (decision 12, 2026-11-26), but it isn't downloaded; the download needs its own yes.
4. **No human-coded gold set exists for facets yet.** Every facet and phase label so far is model- or rule-made, so under rule 6 none can stand as ground truth. Bear decided on 2026-11-23 that fellows or TAs will code it (decision 6). The crosswalk coding packet is ready, but the coders aren't named yet.

**Four source changes will break code written against older layouts:**
- **O\*NET 30.3 (May 2026)** split Skills, renamed the IWA and DWA files, and renamed columns.
- **O\*NET Work Styles was rebuilt in 30.1 (December 2025)** "by a new hybrid artificial intelligence-expert method". So part of O\*NET is now itself machine-made, which bears directly on RQ1.
- **The Anthropic Economic Index changed its schema in the 2026-06-26 release.**
- **O\*NET renumbered DWA and IWA IDs between 30.2 and 31.0** (`4.A.1.a.1.I01.D01` became `4.A.1.a.1.a.1`). The AEI 2026-06-26 release uses the old IDs: all match 30.2, none match 31.0. Names still match, so the join goes by name or through 30.2. (Found 2026-11-23.)

**Two corrections to the brief:**
- **The cluster is Explorer, not Discovery.** The project storage is `/projects/aiskunks`.
- **The lexicon repo is now `nikbearbrown/irreducibly-human-work-lexicon`.** The old `skills-lexicon` URL redirects.

**Thirteen decisions are listed below; 1, 2, 3, 4, 5, 6, 7, 8, 9, 12 and 13 are now answered** (2026-11-23 to 2026-11-27). The repo is a public GitHub repo (decision 13, changed 2026-11-27), the course corpus is set, and RQ4 uses six phases, with every row of the five-to-six map set (deploy → Sustain, 2026-11-25). One next step is a person's: naming two fellows or TAs and sending them the crosswalk packet. Signing off the phase map is another. AIOE and DAIOE may be used for research with a citation and are never redistributed (decision 12). The live Explorer database is left as it is, and the paper states its version gap (decision 8). Decisions 10 and 11 are still open.

## Status by dataset group

| Group | Have | Partial | Missing | Needs human | What it comes down to |
|---|---:|---:|---:|---:|---|
| A. O\*NET | 16 | 0 | 1 | 0 | **Complete.** O\*NET 31.0 (all 46 files) and 30.2 are on the cluster. The live Explorer database is on an older release (30.2 or earlier; the exact release is not found). Under decision 8 (2026-11-27) it is left as it is, the project doesn't use it, and the paper states the gap. |
| B. BLS | 1 | 1 | 0 | 2 | **Behind.** OEWS May 2024 is held; May 2025 is current. Employment Projections 2025–35 is not held. bls.gov blocks scripted downloads, so a person must fetch these in a browser. |
| C. Exposure indices | 4 | 1 | 2 | 0 | **Mostly held (2026-11-23).** Eloundou, AIOE, the Yale workbook and Microsoft are held. Eisfeldt is held only as z-scores inside the Yale file. Webb is missing: the Yale file has no per-occupation Webb values. DAIOE may be used with a citation (decision 12, 2026-11-26) but isn't downloaded. AIOE and DAIOE are never redistributed. |
| D. Observed AI usage | 2 | 1 | 5 | 0 | **Enough for RQ5 (2026-11-23).** The AEI 2026-06-26 release (on the cluster) and 2025-03-27 (on the Mac) are held, as is task_penetration. The other four dated releases and robot_exposure were not fetched (Bear chose "Latest + 2025-03-27"). |
| E. Job listings | 3 | 3 | 1 | 2 | **Usable, with a limit.** ATS feeds are tech-skewed: one day with text, daily without. The 1.15M-posting LinkedIn 2024 set with seniority (on the cluster) is cleared for aggregate counts only, never quoting text (decision 3, 2026-11-23); the same limit covers the Indeed sets in the Kaggle archive. The Reallocation Engine stores no listings. |
| F. Course materials | 7 | 2 | 2 | 0 | **The corpus is set (decision 9, 2026-11-24): Bear's 8 courses, with graded work, plus the 12 confirmed SEIS syllabi.** Those 12 hold 10 distinct texts; 9 are from other instructors and are syllabus only. MIT OCW is out. The catalog is still missing (the fetch was refused from here, and a new fetch needs its own yes). Three of Bear's course folders are no longer on the Mac, but their GitHub repos are intact. AI treatment is read from syllabi only. |
| G. Lexicon | 0 | 2 | 0 | 0 | **The lexicon is broad but unreviewed:** 0 of 3,754 entries are reviewed, 11% have relations, and it holds no work phases. **The abilities-to-facets crosswalk is a machine draft:** the brief's draft was not found, and it was rebuilt on 2026-11-23 (decision 5). Its human coding sheet is blank. |
| H. Crosswalks | 3 | 3 | 1 | 1 | **The key rollup for Phase 3 is held:** O\*NET-SOC 2019 to SOC 2018. The 2010-to-2019 crosswalk was downloaded on 2026-11-23. SOC 2010 to 2018 needs a browser download. The Yale file includes no crosswalk tables. |

## Which research questions can be answered now

| RQ | Can start now? | What's in hand | Blocked by |
|---|---|---|---|
| **RQ1**: coverage of the seven facets by O\*NET and exposure indices | **Partly (machine draft)** | All O\*NET descriptors (31.0); Eloundou, AIOE, BLS categories; Yale z-scores for six measures (778 occupations) and Microsoft (785 occupations, IWA level), both from 2026-11-23 | (a) the abilities-to-facets crosswalk is a machine draft (rebuilt 2026-11-23; two blind runs, kappa 0.93) until a person codes the blank sheet and signs off; (b) Webb has no per-occupation scores, and DAIOE is allowed (decision 12) but not downloaded; (c) facet tags for Skills, Knowledge, Work Activities and Work Context don't exist yet and would be machine labels until a person codes a sample |
| **RQ2**: demand conditions vs adjectives; seniority within vs across occupations | **Partly** | 53,331 descriptions (one day, ATS boards); a cue screen and a 12-posting pilot from the facets work; title-based seniority; the LinkedIn 2024 set (1.15M US postings with a seniority field), cleared for aggregate counts on 2026-11-23 | (a) no human gold set yet (decision 6: fellows or TAs will code it; the posting-line sample isn't drawn yet); (b) titles map to occupations for only 35% of LinkedIn postings; (c) results from the LinkedIn and Indeed sets can be reported only as counts and shares, never as quoted text |
| **RQ3**: share of listing tasks with no O\*NET match; is the residual supervisory? | **Partly** | O\*NET Task Statements, Tasks to DWAs and DWAs (31.0); 53,331 descriptions | (a) no task-line extraction or matching method yet; (b) to say "supervisory", the facet labels need the gold set |
| **RQ4**: phase profile of graded work vs listings | **Partly** | The corpus (decision 9): Bear's 8 courses with graded work, plus 9 syllabus texts from other instructors; posting phase emphasis by occupation (a-new-shape-for-work, on the LinkedIn 2024 set); draft phase tags for DWAs, IWAs and 47,118 phrases | (a) the phase schema is settled (decision 4, 2026-11-24: the six, with the brief's five mapped onto them), and every row of the map is set (deploy → Sustain, 2026-11-25), though the map isn't signed off; course graded work isn't phase-tagged yet; (b) course-to-job-title matching isn't built; (c) the other instructors' courses have syllabi only, no graded work, so their phase profile rests on what the syllabus describes |
| **RQ5**: course AI use vs job AI use (automation vs augmentation) | **Job side yes; course side no** | AEI 2026-06-26 (automation and augmentation by task, DWA, IWA, GWA and occupation; April–May 2026); AEI 2025-03-27 (per-task baseline); Microsoft IWA metrics; syllabus-level AI policies for Bear's courses (the other 9 corpus syllabi aren't read for AI policy yet) | (a) assignment-level AI coding (banned, delegated, engaged) isn't done, and for the other instructors' courses only syllabus-level coding is possible; (b) neither AEI file covers Claude Code; (c) joins need care: the 2026 DWA/IWA IDs are O\*NET 30.2 IDs, and the 2025 release uses 2010 codes (566 of its 3,364 tasks don't match 31.0 text) |

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
   - **Answered 2026-11-24: "Six, map the five", option (a).** RQ4 uses understand, plan, produce, check, sustain and coordinate. Course graded work will be tagged in the six directly; the five survive only as reporting names. The draft map is in `/Users/bear/Documents/CoWork/the-human-share/data/phase-schema/`.
     - **Four rows come from Bear's own Job Shape brief,** whose table pairs each of the six with a software name: requirements → Understand (Specify), design → Plan, build → Produce, review → Check (Verify). The rules behind the existing tags agree.
     - **Deploy → Sustain: Bear's call, 2026-11-25.** The brief pairs Sustain with "Operate" and never names deploy. The posting rules send CI/CD, DevOps and production support to Sustain, and those now report as deploy. The DWA rules send Install and Operate to Produce, so those 104 DWAs (38 Install, 66 Operate) report under build. Most are physical work; 5 are about computers or software. No DWA name contains "deploy". The DWA tags were not changed.
     - **Coordinate has no counterpart** among the five.
     - The existing tags (2,087 DWAs, 332 IWAs, 47,118 posting phrases) become RQ4's basis but stay draft, not gold, until the human sample from decision 6.

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
     - The live Explorer database still runs an older release. Decision 8 (2026-11-27) leaves it so, and the paper states the gap.

8. **Bring the live Explorer database up to date?** It runs an O\*NET release older than 30.3, and its BLS data stops at 2024.
   - Rule 8 forbids touching its production code, and I had no database credentials.
   - **Options:** leave it and note the version gap in the paper; or you check the version with the connection string.
   - **Answered 2026-11-27: "Note the gap".** The database is left as it is, and nobody queries it for this project (rules 3 and 8).
     - **What is known without credentials:** the import script, committed 2026-08-10, reads `Skills.xlsx`, `Technology Skills.xlsx` and `Work Values.xlsx`, which 31.0 no longer has. So the data came from 30.2 or an earlier release. No release number is recorded in the Explorer repo (searched 2026-11-27). Its BLS employment data covers 1999 to 2024.
     - **What the paper says:** the live AI Exposure Explorer runs an O\*NET release earlier than 30.3 (the exact release is not found) and BLS data through 2024. The paper's analyses use O\*NET 31.0 (decision 7), not the Explorer database.
     - **Manifest:** `explorer_neon_onet_bls` moved from needs_human to missing: not held, and not needed.

9. **Which courses are in the corpus?**
   - **(a) Bear's 8 courses.** They have graded work, but one instructor's style.
   - **(b) Plus the 12 confirmed SEIS Fall syllabi.** Broader, but syllabus only.
   - **(c) Plus MIT OCW.** CC BY-NC-SA; the NonCommercial term rules out a commercial tool.
   - Also: the Northeastern catalog refused connections from here, so it needs a browser fetch or the cluster.
   - **Answered 2026-11-24: "Mine plus SEIS", option (b).** The list is `/Users/bear/Documents/CoWork/the-human-share/data/course-corpus.tsv` (20 rows).
     - **Bear's 8 courses, with graded work.** The 7 with a GitHub repo are each pinned to the default-branch commit read on 2026-11-24. Design Engineering has no remote, so it is the local folder only.
     - **The 12 confirmed SEIS section syllabi,** each with its sha256.
       - They hold 10 distinct texts. Two pairs of sections (CSYE 7374 and CSYE 7380) differ only in section details, so the list marks each pair as one text.
       - One is Bear's own Branding and AI (CRN 16549).
       - That leaves 9 texts from other instructors, across 7 courses, all syllabus only.
     - **Not in the corpus:**
       - MIT OCW.
       - The 10 SEIS PDFs with conflicting metadata. These include Bear's own Prompt Engineering and Computational Skepticism PDFs, but those courses are in through their repos.
       - The 2 link-only sections and the 5 missing ones.
     - **Not covered:** the Northeastern catalog. Fetching it needs its own yes.
     - **Found while recording it:**
       - Three course folders seen on 2026-11-22 are gone from the Mac: Branding and AI, Conducting AI and Irreducibly Human. The last also held the AIOE clone.
       - They aren't in the Trash under those names, and all three GitHub repos are intact.
       - INFO 6205 is now at `/Users/bear/Documents/CoWork/bear-textbooks/books/Coursera_INFO_6205_Algorithms/`.
       - Three local checkouts have uncommitted changes, so they differ from GitHub. Before coding starts, a person picks which version counts: the GitHub commit or the working copy.

10. **USAJOBS API key?** It's free, but a person must register (name, email, phone, organisation, intended use). It adds federal and non-tech postings with structured fields. **Options:** register; or skip.

11. **Lightcast?** Commercial; one marketplace listing is US$90,200 for 12 months. **Options:** skip; ask about academic access; or buy. Not needed to start.

12. **Data without a licence:** AIOE (no licence file) and DAIOE (none stated). **Options:** use for research with a citation and don't redistribute; or exclude.
    - **Answered 2026-11-26: "Cite, don't redistribute".** Both may be used for research.
      - **Rechecked at the source that day.** AIOE's GitHub repo still reports no licence and is unchanged at adca5fc (2024-06-03). The DAIOE page still states no licence or terms of use.
      - **Citations, as each source asks.** AIOE: Felten, Raj & Seamans (2021), Strategic Management Journal 42(12):2195–2217. DAIOE: Engberg et al. (2024), "AI Unboxed and Jobs: A Novel Measure and Firm-Level Evidence from Three Countries", IZA DP 16717; the page also links a 2025 version of the paper.
      - **Never redistributed.** No AIOE or DAIOE file, and no per-occupation table of their scores, goes into git (public or private) or anything we share. Results derived from them are reported with the citation. The Yale workbook's AIOE z-scores are treated the same way.
      - **Still open:** whether the public search tool may show per-occupation AIOE or DAIOE scores. That reads as redistribution, so it needs a person's decision before the tool shows them.
      - **DAIOE is not downloaded.** Fetching it from its Google Drive folder needs its own yes, with the files and sizes listed first.

13. **Storage and repo.**
    - Raw downloads would go to a new cluster folder, `/projects/aiskunks/the-human-share/`, in kebab-case.
    - This repo is local only (git initialised, nothing committed).
    - **Options:** create a private GitHub repo `nikbearbrown/the-human-share` and commit the manifest and docs; or keep it local for now.
    - **Answered 2026-11-23: "Private repo".** Created at https://github.com/nikbearbrown/the-human-share.
      - **Visibility:** private when created; public by 2026-11-27 (see below).
      - **What's committed:** the docs, the manifest, the machine-label and gold folders, and the scripts.
      - **What stays out of git:**
        - `data/raw/` (each source's licence governs redistribution, and large files live on the cluster);
        - any `coders-private.tsv`;
        - everything on the cluster.
      - **No licence file was added.** Who owns the repo (Humanitarians AI Incorporated, or Nik Bear Brown personally) is a person's call.
    - **Changed 2026-11-27: "Keep it public".** On 2026-11-27 GitHub showed the repo as public. It had been created with `--private`. GitHub's event log shows the change by the nikbearbrown account, timestamped 2026-11-24 03:18 UTC; I can't tell more than that. Bear chose to keep it public, in line with the 2026-11-26 rule that paper repos are public. The public hai-research index already links to it.
      - **What was public already:** the first commit (scanned for secrets and personal names before it was pushed) and three commits of 2026-11-24 that add the README and contributor guide. None holds raw or third-party data.
      - **What this binds:** every commit is public, so rule 7 applies in full. No raw downloads, no licensed or unlicensed third-party data (decisions 3 and 12), no coder keys and no personal names go into git.
      - **Still open:** the licence. A public repo meant for contributors has none yet, and the owner is a person's call.

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
| 2026-11-24 | "Mine plus SEIS", in answer to "Which courses go in the corpus (decision 9)?" | Wrote `/Users/bear/Documents/CoWork/the-human-share/data/course-corpus.tsv`. It lists Bear's 8 courses, with the GitHub default-branch commit read through `gh` for the 7 that have a repo. It also lists the 12 confirmed SEIS section syllabi from the 2026-11-22 verification report, each with its sha256. I compared the text of the two same-instructor section pairs: each pair differs only in section details. In the manifest, the 8 course entries, the SEIS entry, the catalog and MIT OCW now record the decision. Four stale local paths (three courses and the AIOE clone) are corrected. Nothing was downloaded or cloned, and the seis-syllabi checkout was only read. |
| 2026-11-24 | "Six, map the five", in answer to "Which phase schema should RQ4 use (decision 4)?" | Read the six-phase definitions in A New Shape for Work (`docs/METHOD.md`) and the Job Shape brief (`docs/job-shape-brief.md`), at commit 366b575ccfaa, which matches GitHub `main`. The brief's own table pairs each phase with a software name, which settles four of the five rows; the posting and DWA rules agree. Wrote the draft map, with evidence and sha256 for each source, to `/Users/bear/Documents/CoWork/the-human-share/data/phase-schema/`. Deploy is marked as needing Bear's call. The manifest's IWA, DWA and lexicon entries now say the six-phase tags are RQ4's basis and still draft. Nothing was retagged or downloaded, and the A New Shape for Work repo was only read. |
| 2026-11-25 | "Sustain", in answer to "Which phase does deploy map to?" (the open row of decision 4) | Set the deploy row of `/Users/bear/Documents/CoWork/the-human-share/data/phase-schema/five-to-six.tsv` to Sustain, status "chosen by Bear 2026-11-25"; the other four rows stay draft. Counted the consequence in A New Shape for Work's `tags/dwa-phase-tags.tsv` at commit 366b575ccfaa (read only): 104 DWAs start with Install (38) or Operate (66) and are tagged Produce, so they report under build; 5 of them are about computers or software; no DWA name contains "deploy". The README, this report, PROJECT.md and memory record the call. The map's sign-off fields stay blank, and no tags were changed. |
| 2026-11-26 | "Cite, don't redistribute", in answer to "May AIOE and DAIOE be used for research even though they have no licence (decision 12)?" | Rechecked both sources first: the AIOE GitHub repo (licence null, commit adca5fc unchanged, README citation read through `gh`) and the DAIOE page (no licence or terms; suggested citation IZA DP 16717). In the manifest, `felten_aioe` keeps status have and gains the use limit; `daioe_dynamic_aioe` moves from needs_human to missing, with the limit and citation in its notes. Confirmed that no AIOE or DAIOE file is tracked in git: `data/raw/` is gitignored, and the tracked files only mention the names. PROJECT.md lists the limit. Nothing was downloaded. |
| 2026-11-27 | "Note the gap", in answer to "For decision 8, should the paper just note the Explorer database's older O\*NET version?" | Searched the Explorer repo (`/Users/bear/Documents/CoWork/bear-textbooks/books/Irreducibly-Human`, read only) for a recorded O\*NET release: none found. Its import script was committed 2026-08-10 (380b4a9) and reads files 31.0 no longer has, so the load used 30.2 or earlier. In the manifest, `explorer_neon_onet_bls` moved from needs_human to missing, with the decision and the wording the paper needs in its notes. PROJECT.md lists the decision. The database was not queried and the Explorer code was not touched. |
| 2026-11-27 | "Keep it public", in answer to "Should the-human-share stay public, replacing decision 13?" | Found the repo public while recording decision 8 (`gh repo view` reports PUBLIC). Read its event log and commits (read only): a PublicEvent by the nikbearbrown account timestamped 2026-11-24 03:18 UTC, and three commits of 2026-11-24 (README and CONTRIBUTING.md) on top of 38a3e24. Confirmed the O\*NET attribution is in the public crosswalk folders and that no raw or third-party data is tracked. Updated decision 13 here and in PROJECT.md. Visibility was not changed by me. |

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
