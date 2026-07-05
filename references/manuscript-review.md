# Manuscript Review

Use this to review a full manuscript as a referee. Pair it with `venue-standards.md` for the target venue and `claims-and-language.md` for judging claim strength. The goal is a review that is short, specific, and useful to the authors and the editor.

## What a referee owes

You owe three things: an honest judgment of whether the work supports its claims, a clear path the authors can act on, and a tone that critiques the work and not the people. Length is not rigor. A tight review that names the few decisive issues helps more than a long one that lists everything.

## Ground every comment in the paper

Before you write a single critique, read for what the paper actually says, not what you assume it says. Every comment ties to a specific location: a section, a figure, a table, an equation, or a line.

Do not raise a point the paper already addresses. A reviewer who asks for an ablation that is in Table 4, or a limitation already stated in Section 5, loses credibility and wastes the authors' rebuttal space. When you are unsure whether the paper covers something, search the text before raising it, and phrase it as a question if you remain unsure.

## Claim verification pass

This is the heart of the review. For each central claim, run these checks:

1. Locate the claim. Quote it or cite its location.
2. Find its support. Identify the figure, table, number, or citation meant to back it.
3. Test the match. Does the evidence support the exact claim, at the stated strength?
4. Classify the result:
   - Supported. The evidence matches the claim.
   - Overstated. The evidence is weaker than the claim (for example, an association written as causation, or a single dataset written as a general result). Point to `claims-and-language.md` and ask for the verb to be lowered or the scope narrowed.
   - Unsupported. No evidence is given. Ask for the experiment or the removal of the claim.
   - Contradicted. A number in the text disagrees with a table or figure. Name both values.

Pay attention to the abstract and conclusion, where claims tend to drift above what the results show. Check that every headline number in the abstract appears, identical, in the body.

## Reference relevance pass

Check the reference list for fit, not just format:

- Support. Does each cited work back the sentence it attaches to, or is it a loosely related topic citation? Flag citations that do not support their claim.
- Missing prior work. Name any directly relevant prior work the authors omit, especially work that weakens the novelty claim or that they should compare against. Be specific; give the reference.
- Currency. For a fast-moving field, flag a related-work section that stops two or three years short of the current state.
- Self-citation and padding. Note excessive self-citation or citations that add nothing.
- Inflated attribution. Flag a method credited to the wrong paper, or a survey cited where the primary source is meant.

Keep this pass proportionate. List the few citations that matter, not every formatting slip. Formatting and DOI consistency is a copy-edit note, not a major concern.

## Methods and statistics pass

Use `methods-and-statistics.md` as the checklist. The high-value referee checks:

- Reproducibility. Could you repeat the study from the methods section. Name what is missing.
- Test choice. Does each statistical test match the data and the design.
- Multiplicity and power. Are corrections applied. Is the study powered for its claims.
- Effect sizes and uncertainty. Are intervals and effect sizes reported, not p-values alone.
- Baselines and ablations. For a method paper, are the baselines fair and current, and do ablations isolate the contribution.
- Data leakage. Check the train/validation/test split for subject or patient leakage.

## Structuring the review

Keep it to these parts. Aim for one page for a workshop paper, two for a journal.

1. Summary. Two or three sentences on what the paper does and claims. This shows you read it.
2. Strengths. A few honest, specific sentences. Do not pad.
3. Major concerns. Numbered. Each one affects whether the conclusions hold. For each: state the issue, tie it to a location, and say what would resolve it.
4. Minor concerns. Numbered. Clarity, missing detail, presentation. Brief.
5. Questions to the authors. Things you could not determine from the text.
6. Recommendation. Match the venue scale (see `venue-standards.md`).

## Make concerns constructive

A useful concern is actionable. Convert each criticism into something the authors can do:

- Weak: "The evaluation is inadequate."
- Useful: "The single-dataset evaluation does not support the claim of general improvement (Sec. 4). Reporting on a second public dataset, or narrowing the claim to this dataset, would resolve this."

State what would change your score. If nothing could, say so and explain why, so the editor and authors understand the ceiling.

## Severity calibration

Sort issues by impact, and do not inflate. A wrong p-value that flips a conclusion is major. A British/American spelling mix is minor. Mixing the two ranks buries the decisive point and reads as a hostile review. If the paper is fundamentally sound with fixable gaps, say that plainly; a fair review states what is right, not only what is wrong.

## Tone and conduct

- Critique the work, not the authors. No dismissive or sarcastic language.
- Assume competence and good faith. Where you suspect an error, ask rather than accuse.
- Respect double-blind. Do not speculate about author identity, and do not penalize anonymized placeholders such as a withheld code link.
- Stay within scope. Review the paper submitted, not the paper you would have written.

## Quality gate for a manuscript review

1. Every comment ties to a specific location in the paper.
2. No comment asks for something the paper already contains.
3. Each central claim is verified against its evidence and classified.
4. Cited references are checked for relevance, and missing prior work is named with specifics.
5. Major and minor concerns are separated and ranked by impact.
6. Each major concern states what would resolve it.
7. The recommendation matches the venue scale.
8. The tone critiques the work, and the review follows the spartan style with no banned words and no em dashes.
