# Labelling instructions: O\*NET abilities to the seven facets

Both labelling runs got these instructions word for word. Run B also got one extra line: work from the last row to the first.

## Task

`abilities.tsv` (in this folder) lists the 52 abilities in O\*NET 31.0. Each row gives the ability's element ID, name, category and O\*NET's own description.

Label each ability with the facet or facets that describe **the capacity the ability measures, as O\*NET's description defines it**.

- Label what the ability is, not the jobs that use it.
- Don't label how hard it would be for a machine to do it.

## The seven facets

The facet definitions are fixed. Use them as written and don't reinterpret them.

| Facet | Definition |
|---|---|
| Pattern & Association | Statistical pattern-matching at scale, including classification, prediction, retrieval and generation. |
| Embodied & Sensorimotor | Physical skill and sensorimotor intelligence. |
| Social & Personal | Genuine relationship, trust and interpersonal judgment. |
| Metacognitive & Supervisory | Plausibility auditing, problem formulation, and knowing when to distrust machine output. |
| Causal & Counterfactual | Variable selection, causal structure, intervention and counterfactual reasoning. |
| Collective & Distributed | Intelligence that emerges from groups of people in relationship. |
| Existential & Wisdom | Interpretive judgment, values integration, and knowing which question is worth asking. |

The facets are a faceted classification, not a ranking. No facet is above another.

## Rules

1. **primary_facet** is the one facet whose definition best describes the capacity.
   - If no facet's definition describes it, write `no_fit`. Don't force a fit.
2. **secondary_facets** lists other facets whose definitions clearly describe part of the same capacity. Separate them with semicolons, or leave the field empty.
   - Don't list a facet just because the ability is often used in work that belongs to it.
3. **fit** says how well the primary facet's definition describes the ability:
   - `strong`: the definition plainly covers it.
   - `partial`: it covers part of the ability.
   - `weak`: the closest available, but a poor match.
   - With `no_fit`, write `n/a`.
4. **rationale** is one sentence. It names the words in the O\*NET description, and in the facet definition, that decided the label.
5. **Label each ability on its own.**
   - There is no expected number of abilities per facet.
   - Don't balance the labels across facets, and don't aim for any pattern.
6. **Use only the two sources here:** `abilities.tsv` and these instructions.
   - Don't open any other file.
   - Don't search the web.

## Output

Write a tab-separated file with this exact header and one row per ability, 52 rows in all:

```
element_id	ability	primary_facet	secondary_facets	fit	rationale
```

- Write facet names exactly as they appear in the table above, or `no_fit`.
- Don't put tabs or line breaks inside any field.
