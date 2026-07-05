# Paper Writing

Phase 5. Use this to draft and edit any section. Pair every writing task with `writing-style.md` and `claims-and-language.md`. The structure below follows IMRaD, the standard for empirical papers.

## Section order and what each does

| Section | Job | Common length |
|---------|-----|---------------|
| Title | Name the contribution in one line | 1 line |
| Abstract | State the problem, method, result, and implication | 150 to 250 words |
| Introduction | Set the gap and state the contribution | 0.5 to 1 page |
| Related work | Position against prior work | 0.5 to 1 page |
| Methods | Give enough to reproduce | 1 to 2 pages |
| Results | Report findings without interpretation | 1 to 2 pages |
| Discussion | Interpret, bound, and connect | 1 to 1.5 pages |
| Conclusion | State the contribution and next step | 1 paragraph |

Write the methods and results first. They anchor the rest. Write the abstract last.

## Title

- Name the contribution and the scope. State the object, the method, and the domain.
- Avoid vague openers and filler.
- For a dataset or tool, name it and state what it links or enables.

## Abstract

Four moves in order:

1. The problem and the gap. One or two sentences.
2. What you did. The method in plain terms.
3. What you found. The key result with a number where possible.
4. What it means. The implication, hedged to match the evidence.

Keep it self-contained. No citations. No abbreviations you do not define.

## Introduction

A four-paragraph shape works:

1. The broad problem and why it matters, with evidence.
2. The specific gap. What prior work has not solved.
3. Your contribution. State it as a numbered list where the venue allows.
4. A roadmap sentence if the venue expects one.

End the introduction with a clear, specific contribution statement. Reviewers look for it.

## Methods

- Follow `methods-and-statistics.md`.
- Write to the reproducibility bar. A reader repeats the work from this section.
- Use past tense for what you did. Use present tense for what the method does in general.

## Results

- Follow `analysis-and-results.md`.
- Report findings. Do not interpret.
- Lead with the primary outcome.

## Discussion

A disciplined discussion has five parts in order:

1. Restate the main finding in one sentence, hedged to the evidence.
2. Interpret. What the finding suggests, with the mechanism if the data support one.
3. Compare to prior work. Where you agree and where you differ.
4. Limitations. State them before the conclusion. Name the design constraint, the sample bound, and the measurement limit.
5. Implications and next steps.

Every interpretive sentence uses a hedge from the approved list and a scope qualifier. Use scientist language: based on our observations, this finding suggests, these data are consistent with.

## Conclusion

- State the contribution in one or two sentences.
- State the next step.
- No new results. No new claims.

## Editing pass

Run these passes in order on a full draft:

1. Structure. Each section does its job and nothing else. Results do not interpret. Discussion does not report new data.
2. Claims. Each claim matches the evidence ladder. Each interpretive sentence is hedged and scoped.
3. Citations. Each citation passes the three tests in `citations.md`.
4. Style. Apply the full `writing-style.md` self-check. Remove em dashes, banned words, semicolons, and asterisks.
5. Numbers. Text matches tables and figures.
6. Cut. Remove every sentence that adds nothing.

## Quality gate for paper writing

1. Each section performs its assigned job.
2. The contribution is stated clearly in the introduction.
3. Results report without interpreting. Discussion interprets with hedges and scope.
4. Limitations appear before the conclusion.
5. The abstract is self-contained and covers problem, method, result, implication.
6. The style self-check passes with no banned words and no em dashes.
7. Citations pass the three tests.
