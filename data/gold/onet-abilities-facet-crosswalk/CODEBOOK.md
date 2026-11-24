# Coding guide: O\*NET abilities and the seven facets of work

**What you're doing:** reading 52 short descriptions of human abilities and labelling each one with the facet of work it belongs to. It should take about 30 to 60 minutes (an estimate).

**What you need:** this guide and your sheet, `coder-01.tsv` or `coder-02.tsv`. Either opens in Excel or Google Sheets.

## Ground rules

These keep your labels a true human judgment.

1. **Work alone.** Don't discuss items with the other coder until you have both handed in.
2. **Don't use AI tools** (ChatGPT, Claude, Copilot, Gemini or any other) to read, suggest or check labels. Your own judgment is the point.
3. **Use only this guide and your sheet.** Don't look up how others have mapped these abilities.
4. **There are no right answers to aim for.** No facet is expected to get any particular number of abilities, and it's fine if some facets get none.

## The seven facets

Use these definitions as written.

| Facet | Definition |
|---|---|
| Pattern & Association | Statistical pattern-matching at scale, including classification, prediction, retrieval and generation. |
| Embodied & Sensorimotor | Physical skill and sensorimotor intelligence. |
| Social & Personal | Genuine relationship, trust and interpersonal judgment. |
| Metacognitive & Supervisory | Plausibility auditing, problem formulation, and knowing when to distrust machine output. |
| Causal & Counterfactual | Variable selection, causal structure, intervention and counterfactual reasoning. |
| Collective & Distributed | Intelligence that emerges from groups of people in relationship. |
| Existential & Wisdom | Interpretive judgment, values integration, and knowing which question is worth asking. |

The facets are not a ranking. No facet is "higher" than another.

## What to label

Label **what the ability is, as its description defines it.** Don't label:
- the jobs that use the ability; or
- how easy it would be for a computer to do.

## How to fill in your sheet

Each row is one ability. Fill in these columns:

| Column | What to enter |
|---|---|
| `primary_facet` | The one facet whose definition best describes the ability. Copy the name exactly from the table above. If no facet fits, write `no_fit`. Don't force a fit. |
| `secondary_facets` | Other facets that clearly describe part of the same ability, separated by semicolons. Leave it empty if there are none. Don't add a facet just because the ability is often used in that kind of work. |
| `fit` | How well the primary facet describes the ability: `strong` (plainly covers it), `partial` (covers part of it) or `weak` (the closest one, but a poor match). Write `n/a` if you wrote `no_fit`. |
| `note` | Optional. A few words on any hard call. |
| `coded_on` | The date you finish, as YYYY-MM-DD. |

Leave `coder_id` as it is. Please don't add your name to the sheet.

## When you're done

Save the sheet in the same format, keeping its name, and send it back to whoever sent it to you. If any row was hard to call, use the `note` column rather than leaving it blank.
