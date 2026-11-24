# O\*NET abilities to the seven facets: machine draft

**Status: MACHINE DRAFT, not signed off.** These are model-made labels (project rule 6). They are not ground truth and must not be cited as Bear's crosswalk. The human coding sheet is kept apart from them, in `/Users/bear/Documents/CoWork/the-human-share/data/gold/onet-abilities-facet-crosswalk/`.

signed_off_by:
signed_off_on:

## Executive summary

**The rebuild reproduces the shape of the lost draft.** Two blind runs agreed on the primary facet for 50 of 52 abilities (Cohen's kappa 0.93).

- **Most abilities fall into two facets.** Both runs put 45 abilities in Pattern & Association or Embodied & Sensorimotor; run A put 46. The brief says its draft put 47 there.
- **Three facets got no ability at all**, as primary or secondary, in either run: Social & Personal, Collective & Distributed and Existential & Wisdom.
- **Causal & Counterfactual was nearly empty too.** It got no primary in run A, so four facets were empty there, as the brief says. In run B it got one weak primary (Visualization).
- **Metacognitive & Supervisory got one ability in both runs:** Problem Sensitivity, a strong fit.
- **Four abilities fit no facet in either run:** Deductive Reasoning, Number Facility, Selective Attention and Time Sharing.

**A caution for the paper: part of the Pattern & Association count is a default.** Both runs graded Oral Comprehension, Written Comprehension and Information Ordering as *weak* fits. They put them there only because no other facet's definition names comprehension or following rules. Leaving out every weak fit still leaves 43 (run A) and 41 (run B) of the 52 in the two facets. So the claim holds either way, but the paper should report both counts.

## Why it was rebuilt

The brief cites a draft crosswalk, `onet-abilities-facet-crosswalk.md`, but it was not found on the Mac, the Explorer cluster or Google Drive. On 2026-11-23 Bear answered decision 5 with "Rebuild it".

This is a **new** crosswalk, built from the facet definitions. It is not a copy of the lost draft, so its counts may differ from the ones the brief quotes.

## Method

1. **Source.** The 52 abilities, with O\*NET's own descriptions, were taken from `Content Model Reference.txt` in O\*NET 31.0.
   - File: `explorer:/projects/aiskunks/onet/31.0/db_31_0_text/`, sha256 f7105e22c282736566a2d4e31859b688a5781d309c1569a0b06aea15b4fcd86e.
   - The abilities are the element IDs `1.A.[1-4].x.n`.
   - They are the same 52 IDs rated in `Abilities.txt` (sha256 c80469ecc7d303b821068628ddd937afab8d726b0bf632bee05aca7c5356fc61).
   - By category: 21 cognitive, 10 psychomotor, 9 physical and 12 sensory.
   - The table is `abilities.tsv`.
2. **Instructions.** `instructions.md` gives:
   - the seven facet definitions, word for word from `/Users/bear/Documents/CoWork/the-human-share/PROJECT.md`;
   - one primary facet per ability, or `no_fit`;
   - optional secondary facets;
   - a fit grade;
   - a one-sentence rationale.

   The instructions don't mention the brief's claim about the crosswalk, or any expected distribution.
3. **Two blind runs.**
   - Two separate Claude Code subagents labelled all 52 abilities on 2026-11-23. Each could read only `instructions.md` and `abilities.tsv`.
   - Neither saw the other's labels, the brief, `PROJECT.md` or the facets pilots.
   - Run A worked from the first row to the last; run B from the last to the first, to expose order effects.
   - Model: `claude-opus-5-5` (Claude Opus 5.5) in both runs, as each run reported it. Each run made 4 tool calls.
   - The run transcripts confirm that neither opened any file except those two.
   - Outputs: `run-a.tsv` and `run-b.tsv`.
4. **Comparison.** `comparison.tsv` sets the two runs side by side. The agreement figures below come from `/Users/bear/Documents/CoWork/the-human-share/scripts/compare-label-runs.py` (stdlib Python), which also checked every row: 52 IDs, valid facet names, and fit values consistent with `no_fit`. `abilities.tsv` was made by `/Users/bear/Documents/CoWork/the-human-share/scripts/extract-onet-abilities.py`.

The session agent that wrote this folder had read the brief's claim, so it did not label anything. It only extracted the source table, wrote the instructions and compared the runs.

## Results

### Primary facet counts

| Facet | Run A | Run B |
|---|---:|---:|
| Pattern & Association | 14 | 14 |
| Embodied & Sensorimotor | 32 | 31 |
| Social & Personal | 0 | 0 |
| Metacognitive & Supervisory | 1 | 2 |
| Causal & Counterfactual | 0 | 1 |
| Collective & Distributed | 0 | 0 |
| Existential & Wisdom | 0 | 0 |
| no_fit | 5 | 4 |

**Secondary facets.** Run A listed Pattern & Association twice (Problem Sensitivity, Rate Control), Causal & Counterfactual twice (Inductive Reasoning, Visualization) and Embodied & Sensorimotor once (Speech Recognition). Run B listed only Embodied & Sensorimotor, once (Speech Recognition).

**Fit grades.**

| Run | Strong | Partial | Weak | n/a |
|---|---:|---:|---:|---:|
| A | 35 | 9 | 3 | 5 |
| B | 28 | 14 | 6 | 4 |

### Agreement

**Agreement:** 50 of 52 on the primary facet (0.962); Cohen's kappa 0.930.

**By O\*NET category:** cognitive 19 of 21, psychomotor 10 of 10, physical 9 of 9, sensory 12 of 12.

The two disagreements:

| Ability | Run A | Run B |
|---|---|---|
| Mathematical Reasoning (1.A.1.c.1) | no_fit | Metacognitive & Supervisory (weak), through "problem formulation" |
| Visualization (1.A.1.f.2) | Embodied & Sensorimotor (partial), secondary Causal & Counterfactual | Causal & Counterfactual (weak), through "intervention and counterfactual reasoning" |

### Abilities that need a person's judgment most

- **No fit in both runs:** Deductive Reasoning, Number Facility, Selective Attention, Time Sharing.
- **Weak in both runs (Pattern & Association):** Oral Comprehension, Written Comprehension, Information Ordering.
- **Weak in one run:** Originality (Pattern & Association), plus the two disagreements above.

### Where the 52 went

- **Embodied & Sensorimotor:** all 10 psychomotor and all 9 physical abilities; 11 of the 12 sensory abilities; and Spatial Orientation. Run A also put Visualization here.
- **Speech Recognition**, the 12th sensory ability, went to Pattern & Association in both runs, with Embodied & Sensorimotor as secondary.
- **Pattern & Association** took 13 cognitive abilities plus Speech Recognition:
  - comprehension and expression
  - Fluency of Ideas and Originality
  - Inductive Reasoning
  - Information Ordering
  - Category Flexibility
  - Memorization
  - the closure and perceptual-speed abilities

`comparison.tsv` has every ability with both runs' labels. The full rationales are in the run files.

## Limits

- **Two runs of one model are not two coders.** Agreement between them measures the model's consistency, not validity. Only the human sheet can test validity.
- **The facet definitions are one line each.** Several abilities sit between facets because of that, not because of the labeller. The disagreement list shows where.
- **Labels describe each ability as O\*NET defines it.** They are not about how jobs use the ability, or how exposed it is to AI.

## Attribution

The ability names and descriptions are from `Content Model Reference.txt` in O\*NET 31.0. O\*NET asks for this text:

> This page includes information from the O\*NET 31.0 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET® is a trademark of USDOL/ETA.

**What we changed:** the project kept the 52 ability rows, added category columns and added model-made facet labels. USDOL/ETA has not approved, endorsed, or tested these modifications.
