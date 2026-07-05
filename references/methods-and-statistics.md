# Methods and Statistics

Phase 2. Use this for the methods section, the statistical plan, power analysis, and preregistration. Methods give enough detail to reproduce the work. Statistics match the design and the data.

## Methods section: the reproducibility standard

A reader with your data and your methods section reproduces your result. Write to that bar.

Include:

- Participants or samples. Source, eligibility, recruitment, final counts, and dropout with reasons.
- Materials. Instruments, reagents, datasets, and tools with versions and identifiers.
- Procedure. Step order, timing, conditions, and operator. Enough to repeat.
- Variables. Operational definitions and measurement scales.
- Analysis plan. Every test, model, and software package with version.
- Ethics. Approval body, protocol number, and consent process.
- Randomization and blinding. Method of sequence generation, allocation concealment, and who was blinded.

## Choosing the statistical test

Match the test to the outcome type, the number of groups, and the data structure.

| Outcome | Two groups | More than two | Association |
|---------|-----------|---------------|-------------|
| Continuous, normal | t test | ANOVA | Pearson correlation, linear regression |
| Continuous, non-normal | Mann-Whitney U | Kruskal-Wallis | Spearman correlation |
| Binary | Chi-square, Fisher exact | Logistic regression | Logistic regression |
| Count | Poisson, negative binomial | Poisson, negative binomial | Poisson regression |
| Time to event | Log-rank | Cox model | Cox model |
| Repeated or clustered | Mixed model, GEE | Mixed model, GEE | Mixed model |

Check the assumptions of each test before you use it. State which assumptions you checked and how.

## Power analysis

Run power before data collection. You need four of these five, and you solve for the fifth:

- Effect size. The smallest effect worth detecting, from theory or pilot data.
- Alpha. The false positive rate, often 0.05.
- Power. The true positive rate, often 0.80 or 0.90.
- Sample size.
- Variance or base rate.

State the source of the effect size. A power analysis built on an inflated effect size produces an underpowered study. Report the calculation and the software.

## Multiplicity and pre-specification

- Pre-specify the primary analysis. Label everything else exploratory.
- Correct for multiple comparisons. State the method: Bonferroni, Holm, or false discovery rate.
- Do not convert an exploratory finding into a confirmatory claim. Report it as exploratory.

## Common statistical errors to avoid

- Reading a non-significant p value as proof of no effect. It means the test did not detect an effect.
- Reporting p values without effect sizes and intervals.
- Ignoring clustering or repeated measures. Treat dependent observations with the right model.
- Dichotomizing a continuous variable without reason. This throws away information.
- Selecting predictors by univariate screening, then ignoring the selection in inference.
- Treating ordinal scales as interval without justification.

## Preregistration

Preregistration locks the plan before data. It separates confirmatory from exploratory work and protects credibility.

Register these before data collection:

- Hypotheses, including direction.
- Primary and secondary outcomes.
- Sample size and the stopping rule.
- The full analysis plan, including covariates and exclusions.
- The handling of missing data and outliers.

Platforms: OSF, AsPredicted, ClinicalTrials.gov for trials. Use the `templates/preregistration.md` template.

## Missing data and outliers

- State the missing data mechanism you assume: missing completely at random, at random, or not at random.
- State the method: complete case, multiple imputation, or a model-based approach. Justify it.
- Define outlier handling before analysis. Report results with and without exclusions.

## Reproducibility for computational methods

- Share code with a license and a version tag.
- Pin dependencies and report the environment.
- Set and report random seeds.
- Provide a runnable example or a one-command reproduction script.
- Report hardware and runtime where they affect results.

## Quality gate for methods and statistics

1. A reader could reproduce the study from the methods section.
2. Each test matches the outcome type and the data structure, with assumptions checked.
3. A power analysis exists with a justified effect size.
4. The primary analysis is pre-specified and exploratory work is labeled.
5. Multiplicity is corrected and the method is stated.
6. Missing data and outlier handling are stated and justified.
7. For computational work, code, seeds, and environment support reproduction.
