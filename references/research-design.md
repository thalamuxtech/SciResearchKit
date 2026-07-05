# Research Design

Phase 1. Use this when you frame a question, set hypotheses, or design a study. A weak design cannot be fixed by analysis. Get this right first.

## Step 1. Sharpen the question

A research question is specific, answerable, and tied to a gap. Test your question against these:

- Specific. It names the population, the variables, and the outcome.
- Answerable. Available data or a feasible study can answer it.
- Novel. It addresses a real gap, confirmed by the literature review.
- Relevant. The answer changes practice, theory, or future work.

Use a structured frame where the field has one:

- PICO for clinical questions: Population, Intervention, Comparison, Outcome.
- PECO for exposure studies: Population, Exposure, Comparison, Outcome.
- FINER to screen feasibility: Feasible, Interesting, Novel, Ethical, Relevant.

## Step 2. State hypotheses

- Write the null and the alternative for each confirmatory test.
- State the direction if theory predicts one.
- Separate confirmatory hypotheses from exploratory aims. Label each.
- Pre-specify confirmatory hypotheses before you see the data. This protects against hypothesizing after results are known.

## Step 3. Choose the design

Match the design to the question and the claim you want to make. The design sets the ceiling on your claim strength.

| Question type | Design options | Claim ceiling |
|---------------|----------------|---------------|
| Does X cause Y | Randomized controlled trial, randomized experiment | Causal |
| Does X associate with Y over time | Prospective cohort | Strong association |
| Does X associate with Y now | Cross-sectional, case control | Association |
| What is the state of X | Descriptive, survey, registry | Description |
| How and why | Qualitative, mixed methods | Mechanism, context |
| Does method A beat method B | Benchmark with held-out test, ablation | Comparative performance |

## Step 4. Define variables and measures

- Define each variable in operational terms. State how you measure it.
- State the scale: nominal, ordinal, interval, ratio.
- Name the primary outcome. One primary outcome protects power and interpretation. List secondary outcomes separately.
- State known confounders and how the design handles them: randomization, matching, restriction, or statistical adjustment.

## Step 5. Plan sampling and units

- Define the unit of analysis and the unit of randomization. They are not always the same.
- State the sampling frame and the recruitment path.
- State inclusion and exclusion criteria.
- Address clustering. Clustered data need methods that respect the structure.

## Step 6. Address bias and validity

- Internal validity. Can the design support the causal or comparative claim. Name the threats.
- External validity. To whom does the result generalize. State the bounds.
- Selection bias. Who enters the sample and who drops out.
- Measurement bias. Blinding, instrument calibration, and rater agreement.
- Confounding. Variables that affect both exposure and outcome.

## Step 7. Plan for power

Power belongs in design, not after data collection. See `methods-and-statistics.md` for the power calculation. Set the target effect size, alpha, and power before you collect data.

## Machine learning and computational studies

For model and algorithm work, the design questions shift:

- Define the task, the dataset, and the split. No test leakage across train and test.
- Name the baselines. A result without a baseline is not a result.
- Pre-specify the primary metric and the evaluation protocol.
- Plan ablations to isolate the contribution of each component.
- State compute, seeds, and the number of runs. Report variance across seeds.

## Quality gate for design

1. The question is specific, answerable, novel, and relevant.
2. Confirmatory hypotheses are stated and separated from exploratory aims.
3. The design supports the intended claim strength and no more.
4. The primary outcome is single and pre-specified.
5. Confounders and biases are named with a handling plan.
6. A power plan exists with target effect size, alpha, and power.
7. For computational work, baselines, splits, metrics, and seeds are pre-specified.
