# Analysis and Results

Phase 4. Use this for the analysis plan and the results section. Results report what you found. They do not interpret. Interpretation belongs in the discussion.

## Run the pre-specified plan first

- Execute the confirmatory analysis you pre-specified before you explore.
- Report the pre-specified result whether or not it supports your hypothesis. A null result is a result.
- Run exploratory analysis after, and label every part of it as exploratory.

## What a result reports

Each result carries four parts:

1. The estimate. The effect size, the difference, the coefficient, or the metric.
2. The uncertainty. The confidence interval or the credible interval.
3. The test. The statistic, the degrees of freedom, and the p value where used.
4. The sample. The n the result rests on.

A p value alone is not a result. An estimate without an interval is not a result.

## Effect sizes

Report the effect size in interpretable units.

- Mean difference with its unit.
- Standardized effect such as Cohen d or odds ratio, with the interval.
- For models, the metric with its variance across runs or folds.
- Relative and absolute change. Absolute change protects against misreading a large relative change on a tiny base.

## Reporting numbers

- Report to a precision the data support. Do not write five decimals on a sample of twenty.
- Report exact p values rather than only a threshold, except for very small values, which you state as below a bound.
- State the direction of every effect.
- Match every number in the text to the matching number in a table or figure.

## Tables and figures

- A figure shows a pattern. A table gives exact values. Pick the one that serves the reader.
- Every figure and table stands alone. The caption states what it shows, the sample, and the units.
- Show uncertainty in figures with error bars or bands, and state what they represent.
- Do not truncate an axis to exaggerate an effect.
- Label axes with units. Define every abbreviation in the caption.

## Negative and null results

- Report them plainly. State that the test did not detect an effect.
- Do not interpret a null as proof of no effect unless you ran an equivalence test.
- Underpowered nulls are uninformative. State the power.

## Machine learning results

- Report the primary metric on the held-out test set, with variance across seeds.
- Compare against the baselines you pre-specified.
- Report ablations that isolate each component.
- State the split, the data leakage checks, and the selection of the reported checkpoint.
- Report compute and runtime where they bear on the claim.

## Separation of results and interpretation

- Results section: what you found. Estimates, intervals, tests, samples.
- No mechanism, no comparison to theory, no "this shows" in the results section.
- Save interpretation for the discussion, under the claim ladder in `claims-and-language.md`.

## Quality gate for analysis and results

1. The pre-specified analysis ran and is reported regardless of outcome.
2. Exploratory analysis is labeled.
3. Each result reports estimate, uncertainty, test, and sample.
4. Effect sizes appear with intervals in interpretable units.
5. Numbers in text match tables and figures.
6. Figures show uncertainty and use honest axes.
7. The results section reports findings without interpreting them.
