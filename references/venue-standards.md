# Venue Standards

Use this to match a review or a submission to the target venue. Each venue sets its own length, review scale, and priorities. Calibrate the recommendation and the emphasis of a review to the venue, not to a generic standard.

Always confirm the current call for papers. Page limits, scales, and dates change yearly. The figures below are typical recent values, not a substitute for the official call.

## Computer vision and machine learning conferences

These run double-blind, value novelty and strong empirical comparison, and reject for weak baselines or thin evaluation as readily as for poor writing.

### CVPR (IEEE/CVF Conf. on Computer Vision and Pattern Recognition)
- Format. 8 pages plus references; double-blind; supplementary allowed and reviewed at the reviewer's discretion.
- Review. Strengths/weaknesses, rating, confidence; rebuttal phase, then reviewer discussion; ratings such as borderline through strong accept.
- Priorities. Technical novelty, fair and current baselines, ablations that isolate the contribution, reproducibility.
- Common reject reasons. Missing recent baselines, single-dataset claims, no ablation, overclaimed state-of-the-art.

### ICCV / ECCV (Int. Conf. on Computer Vision; European Conf. on Computer Vision)
- Format. Similar to CVPR (8 pages plus references; double-blind). ECCV runs in even years, ICCV in odd years.
- Review and priorities. As CVPR. ECCV uses a paper-specific scale with a rebuttal.

### NeurIPS / ICML / ICLR (machine learning)
- Format. NeurIPS and ICML roughly 8 to 9 pages plus references and appendix; ICLR 9 pages, on OpenReview with public reviews.
- Review. Soundness, contribution, presentation rated separately at NeurIPS; OpenReview discussion at ICLR; reproducibility checklist expected.
- Priorities. Clear claims matched to evidence, theoretical or empirical rigor, ablations, broad and fair comparison, reproducibility.

### AAAI, ACL/EMNLP/NAACL, KDD, MM
- Format and scale vary; most run double-blind with author response.
- Priorities. Strong empirical comparison and clear novelty. ACL-family venues weigh reproducibility and a dedicated limitations section, now often required.

## Medical imaging venues

### MICCAI (Int. Conf. on Medical Image Computing and Computer-Assisted Intervention)
- Format. About 8 pages plus references, LNCS template, double-blind; supplementary often not reviewed or limited; rebuttal phase.
- Priorities. Clinical relevance, methodological soundness, validation on adequate data, and honest reporting of limitations.
- Workshops (for example MULTITAB, MIRASOL). Shorter scope, often "8 pages plus references," supplementary sometimes not supported; resource and focused-contribution papers are in scope. Confirm per workshop.

### Other medical-imaging venues
- IEEE ISBI. Short papers (about 4 to 5 pages), double-blind; concise method plus validation.
- SPIE Medical Imaging. Conference proceedings with broad scope.
- Journals: IEEE TMI, Medical Image Analysis (MedIA), Radiology: Artificial Intelligence. Full-length, single or double-blind, multiple revision rounds; expect thorough validation, reporting-guideline compliance, and statistical rigor.

## Journals (general)

- Scales. Major revision, minor revision, reject, accept; multiple rounds; an associate editor weighs reviews.
- Expectations beyond conferences. Full reproducibility, reporting-guideline compliance (see `reporting-standards.md`), data and code availability, and detailed statistics with effect sizes and intervals.
- Reporting guidelines by study type. CONSORT (trials), PRISMA (systematic reviews), STROBE (observational), TRIPOD and CLAIM (prediction and imaging AI), ARRIVE (animal). Check the journal's required checklist.

## How venue choice changes a review

- Conference vs journal. A conference review judges a fixed submission against a bar; a journal review can ask for substantial new work across revisions. Scope your requests to what the format allows. Do not demand a year of new experiments for an 8-page conference paper.
- Workshop vs main track. A workshop welcomes focused, early, or resource contributions. Judge against the workshop's stated scope, not the main-track novelty bar.
- Page limits shape fairness. If the venue is 8 pages, do not fault the authors for omitting detail that does not fit; ask them to move it to supplementary or a repository instead.
- Double-blind. Do not penalize anonymized links or withheld DOIs. These are required at submission and filled at camera-ready.

## Recommendation calibration

Map your judgment to the venue's scale, and make the borderline call explicit:

- Clear accept. Claims supported, evaluation sound, contribution fits the venue.
- Weak accept / borderline. Sound core with fixable gaps. State the few conditions that would settle it.
- Weak reject / borderline. Promising but the evidence does not yet support the central claim. Name what is missing.
- Reject. A flaw in design, evidence, or novelty that the current format cannot repair. State it plainly and fairly.

State what would move your recommendation up one step. That single sentence is often the most useful part of the review.
