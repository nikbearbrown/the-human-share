# Phase schema for RQ4: the brief's five phases mapped onto six

**Status: DRAFT map, not signed off.** Claude Code (claude-opus-5-5) drafted it on 2026-11-24 from Bear's own documents. Four of the five rows follow those documents directly. Bear chose the deploy row on 2026-11-25: Sustain. The map as a whole still waits for Bear's sign-off below.

signed_off_by:
signed_off_on:

## Executive summary

- **Decision 4 (2026-11-24):** Bear chose option (a), "Six, map the five".
  - RQ4 uses the six phases of A New Shape for Work: understand, plan, produce, check, sustain, coordinate.
  - Course graded work will be tagged in the six directly. That puts it on the same scale as the existing DWA, IWA and posting-phrase tags.
  - The brief's five phases (requirements, design, build, review, deploy) are kept only as names for reporting results, through this map.
- **Four rows come straight from the Job Shape brief's own table**, which pairs each of the six phases with a software name:

  | Brief's phase | Six-phase name | Job Shape's software name |
  |---|---|---|
  | requirements | Understand | Specify |
  | design | Plan | Design |
  | build | Produce | Build |
  | review | Check | Verify |

  The rules behind the existing tags send these words to the same phases.
- **Deploy maps to Sustain: Bear's call, 2026-11-25.** It was the one row the documents didn't settle.
  - The Job Shape brief pairs Sustain with "Operate" and never names deploy.
  - The existing rules split deploy-type work:
    - The posting rules send CI/CD, DevOps and production support to Sustain. These now report as deploy.
    - The DWA rules send the verbs Install and Operate to Produce. Those 104 DWAs (38 Install, 66 Operate) therefore report under build, not deploy.
  - Most of the 104 are physical work, such as installing flooring or operating drilling equipment. Five are about computers or software: "Install computer software.", "Install computer hardware.", "Install programs onto computer or computer-controlled equipment.", "Operate computer systems." and "Operate computers or computerized equipment.".
  - No DWA name contains "deploy".
  - The DWA tags were not changed. They live in A New Shape for Work and are still draft.
- **Coordinate has no counterpart among the five.** Course work tagged Coordinate shows up in the six-phase profile, but it has no name in the five-phase view.

The map with its evidence is in `/Users/bear/Documents/CoWork/the-human-share/data/phase-schema/five-to-six.tsv`.

## What decision 4 does and doesn't change

- **The six phases are A New Shape for Work's.** This folder doesn't redefine them. Their names, software names and example work activities are in that repo's `docs/METHOD.md`.
- **The existing phase tags become RQ4's basis, but they are not gold.**
  - What exists: 2,087 DWAs, 332 IWAs and 47,118 posting skill phrases.
  - All of them are draft and unreviewed, made by rules and a model (rule 6).
  - They still need the human sample from decision 6.
- **The DWA tags as they stand:** produce 845, sustain 290, coordinate 269, plan 231, understand 230, check 222.
- **Course graded work has no phase tags yet.** The corpus is set by decision 9: `/Users/bear/Documents/CoWork/the-human-share/data/course-corpus.tsv`.

## Sources

All of these are in `/Users/bear/Documents/CoWork/bear-textbooks/books/a-new-shape-for-work/`:
- **Repo:** https://github.com/nikbearbrown/a-new-shape-for-work (public).
  - `main` was at 366b575ccfaa on 2026-11-24, the same commit as the local checkout.
  - The local checkout's only changes are in `paper/`. The files below match the commit.
- **`docs/job-shape-brief.md`:** the Job Shape design brief "as pasted on 2026-11-21". Part 1 has the table of six phases with their software names. sha256 15d05c387e59f6f70cb45f491bbb72300896993af83ca8bc963e3a494d5b1001.
- **`docs/METHOD.md`:** the six phases as the prototype uses them, and how tags are set. sha256 9b8470251c0e47b3b86f5813774ade459807347e6a4a7e31a0abaa6589e09343.
- **`scripts/build_postings.py`:** the posting-phrase rules. sha256 cad2122443d3dc6b015c14c877edb2a1685eba5598f4f134f120c997a9430da2.
- **`scripts/dwa_tags.py`:** the DWA verb rules. sha256 45529c3c4ab32e477463c1eb31062f92fbb0e727cb990bd57a19cc6b35458d63.
- **`tags/`:** `dwa-phase-tags.tsv`, `iwa-phase-tags.tsv` and `skill-phrase-phase-tags.tsv`. The Install and Operate counts above come from `dwa-phase-tags.tsv` (sha256 121b7f9102f067f57c3d23a62673e7f8a2c779a598de0d7927e1fe8980e39bd0), read on 2026-11-25: DWAs whose name starts with that verb.

**Licence:** that repo's documentation and tags are CC BY 4.0 and its code is MIT. Copyright is held by Humanitarians AI Incorporated.
