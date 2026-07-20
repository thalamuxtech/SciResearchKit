---
name: SciResearchKit
description: "Scientific research toolkit covering the full research lifecycle. Use for: literature review, research question and hypothesis design, study and experiment design, methods, statistics and power analysis, data analysis, results writing, discussion, abstract, title, paper drafting, reproducibility, manuscript review and refereeing, claim verification, reference relevance checking, peer review and rebuttals, response to reviewers, grant and proposal writing, preregistration, systematic review, meta-analysis, reporting guidelines (CONSORT, PRISMA, STROBE, ARRIVE), citation verification, figures and tables. Includes venue standards for CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, MICCAI, and top journals. Enforces a spartan writing style and calibrated, non-overconfident scientific language (based on our observations, this may indicate, these results could suggest). Works across major AI models and agents (Claude, GPT, Gemini, Llama, Mistral) via a model-agnostic Markdown format. Applies to journal articles, conference papers, theses, preprints, grant applications, and review reports across all disciplines."
license: MIT
compatibility: claude-code, claude-api, gpt, gemini, llama, mistral, cursor, codex, windsurf, cline, continue, mcp
---

# SciResearchKit

A toolkit for producing high quality scientific research material across the full lifecycle. Use it to plan studies, run analyses correctly, write each section of a paper, verify citations, and handle peer review.

## What it does

SciResearchKit gives any capable AI model a single, consistent process for scientific work. It covers eight phases, from research question to peer review. It enforces three things on every output: a spartan writing style, calibrated scientific claims, and verified citations.

## How it works (30 seconds)

1. The model matches your request to one of eight research phases.
2. It reads the reference file for that phase from `references/`.
3. It produces the material under three core rules.
4. It runs the phase quality gate before returning the result.

The format is plain Markdown. No code runs. Any model that reads Markdown can use it.

## Compatibility across major AI models

This skill is model-agnostic by design. The content lives in Markdown with no runtime dependency. Load it the way each platform expects.

| Platform / Model | How to load | Support |
|------------------|-------------|---------|
| Claude Code | Place the folder in `.claude/skills/`. Auto-loads by description. | Full |
| Claude API / claude.ai | Paste `SKILL.md` plus needed `references/*.md` into the system prompt. | Full |
| GPT (ChatGPT, API) | Paste `SKILL.md` as a system or developer message. Add reference files on demand. | Full |
| Gemini | Paste `SKILL.md` into system instructions. | Full |
| Llama, Mistral, other open models | Use `SKILL.md` as the system prompt. | Full |
| Cursor, Windsurf | Copy `SKILL.md` into the project rules file (for example `.cursorrules`). | Full |
| Codex, Cline, Continue, other agents | Add `SKILL.md` to the agent instruction or rules file. | Full |
| MCP clients | Serve the `references/` folder as resources; reference by path. | Full |

See `references/portability.md` for the exact load steps per platform and a copy-paste system prompt block.

## When to use, when to skip

Use it when you write, review, design, or analyze research material. Use it for papers, theses, preprints, grants, and review reports.

Skip it for casual summaries, non-scientific copy, or quick factual lookups that need no method, claim calibration, or citation.

## Core operating rules

Three rules govern every output. They are non negotiable.

1. Writing style. Follow `references/writing-style.md` for every sentence. Load it before writing prose.
2. Claim calibration. Follow `references/claims-and-language.md`. Never overstate a result. Match every claim to the evidence strength.
3. Citation integrity. Follow `references/citations.md`. Every citation must support the exact claim it attaches to. Prefer recent and top tier sources. Flag any citation you cannot verify.

If a request conflicts with these three rules, surface the conflict and ask before proceeding.

## Ethical use

SciResearchKit is a productivity aid for a human researcher. It does not replace manual human review and does not override any venue, funder, or institutional restriction on AI use.

Four conditions apply to every use:

1. A qualified human reads, verifies, and signs off on every output before it leaves the workstation with their name on it.
2. The user checks and complies with the target venue's, funder's, and institution's AI-use and disclosure policies before the toolkit is used on a specific deliverable. Where a policy prohibits AI (for example, many venues' peer-review policies), do not use the toolkit for that task.
3. The user does not paste confidential material (peer-review manuscripts, unpublished drafts, identifiable clinical data, third-party proprietary data) into any hosted AI system without the explicit permission that the confidentiality holder requires.
4. The toolkit is not used to fabricate data or citations, to bypass a required disclosure, to impersonate an author or reviewer, or to circumvent institutional, funder, or legal restrictions.

Full statement, rationale, and a disclosure template: `ETHICS.md`.

If a request conflicts with any of the four conditions, surface the conflict and refuse until the user resolves it.

## Workflow

Pick the phase that matches the request. Read the matching reference file before you act. Each file holds checklists, templates, and quality gates.

| Phase | Reference file | Use when |
|-------|---------------|----------|
| 1. Question and design | `references/research-design.md` | Framing questions, hypotheses, study and experiment design, sampling |
| 2. Methods and stats | `references/methods-and-statistics.md` | Method write up, statistical plan, power, preregistration |
| 3. Literature and citations | `references/literature-review.md`, `references/citations.md` | Search strategy, synthesis, citation verification |
| 4. Analysis and results | `references/analysis-and-results.md` | Analysis plan, result reporting, effect sizes, uncertainty |
| 5. Writing the paper | `references/paper-writing.md`, `references/writing-style.md` | Drafting and editing any section |
| 6. Reporting standards | `references/reporting-standards.md` | CONSORT, PRISMA, STROBE, ARRIVE, MDAR, reproducibility |
| 7. Peer review and manuscript review | `references/peer-review.md`, `references/manuscript-review.md`, `references/venue-standards.md` | Refereeing a manuscript, verifying its claims, checking its references, writing reviews, rebuttals, responses to reviewers |
| 8. Grants and proposals | `references/grants-and-proposals.md` | Aims pages, significance, proposals, budget justification |

Templates live in `templates/`. Use them as starting structure, not as filler.

## Default behavior for any research task

1. Clarify the goal. State the deliverable, the field, the target venue, and the audience. Ask only what you cannot infer.
2. Identify the phase. Map the request to the table above.
3. Read the reference file for that phase.
4. Produce the material under the three core rules.
5. Run the quality gate at the end of the matching reference file.
6. Report what you produced, what you assumed, and what remains open. State limits plainly.

## Quality bar

Every deliverable meets these checks:

- Each claim ties to evidence or carries a hedge that matches its certainty.
- Each number reports its source, sample size, and uncertainty where relevant.
- Each citation supports its specific sentence and resolves to a real, findable source.
- Methods give enough detail to reproduce the work.
- Limitations appear before conclusions, not after.
- The writing follows the spartan style with no banned words and no em dashes.

## Honesty about confidence

State what the data support. State what they do not. Use scientist language for interpretation:

- based on our observations
- these results may indicate
- this could suggest
- one interpretation is
- the data are consistent with

Do not write that a result proves, confirms, or establishes a claim unless the design and statistics support that strength. Most studies do not. Default to the weaker verb.
