# Peer Review

Phase 7. Use this to write a review report, a rebuttal, or a response to reviewers. Pair it with `templates/response-to-reviewers.md`.

## Writing a review report

For a full referee report on a manuscript, use `manuscript-review.md`, which gives the claim-verification pass, the reference-relevance pass, severity calibration, and the quality gate. Use `venue-standards.md` to match the review and the recommendation to the target venue (CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, MICCAI, journals). The short form:

1. Summary. State what the paper does in two or three sentences. This shows the authors you understood it.
2. Strengths. Name what works.
3. Major concerns. Issues that affect the validity of the conclusions. Number them.
4. Minor concerns. Issues of clarity, formatting, and presentation. Number them.
5. Recommendation. Match it to the venue scale.

Rules for reviewers:

- Tie each concern to a specific section, claim, or number.
- Do not raise a point the paper already addresses. Verify against the text first.
- Separate what affects validity from what affects polish, and rank by impact.
- State what would change your assessment. Make the path to acceptance concrete.
- Judge the work, not the authors. No dismissive language.
- Flag missing baselines, unverified claims, overconfident language, and absent limitations.
- Check the statistics against the design.

## Responding to reviewers

The response document decides borderline papers. Make the changes easy to see and the reasoning easy to follow.

Structure for each comment:

1. Quote the reviewer comment.
2. State your response.
3. State the exact change and where it appears, with the section and the line or page.

Use a clear visual convention. One option: black text for changes already in the revised manuscript, colored text for commitments still in progress. Define the convention at the top.

Rules for responses:

- Address every comment. Skip none, even the ones you disagree with.
- Agree where the reviewer is right. Fix it and say where.
- Where you disagree, give evidence, not opinion. Be respectful and firm.
- Do not promise what you will not deliver. A reviewer checks the next version.
- When a comment exposes a real limitation you cannot fully fix, state it as a limitation and scope the claim down.
- Keep the tone calm. Reviewers volunteer their time.

## Calibrating claims under review

Reviewers reject overconfident results and discussion sections. When a reviewer flags a claim:

- Lower the verb to match the evidence ladder in `claims-and-language.md`.
- Add the scope qualifier and the hedge.
- Move an over-reached conclusion into the limitations as an open question.

## Handling the four common rejection reasons

- Missing evidence for a claim. Add the experiment or remove the claim.
- Unaccounted-for data or exclusions. Characterize them and report the reason.
- No baseline or comparison. Add it.
- Overstated novelty. Build a comparison table and state the specific addition.

## Quality gate for peer review

1. Every reviewer comment has a response and a stated change.
2. Each response points to the exact location of the change.
3. Disagreements are backed by evidence and stated with respect.
4. Claims flagged as overconfident are lowered to match the evidence.
5. Commitments are realistic and will appear in the next version.
6. The tone is professional throughout.
