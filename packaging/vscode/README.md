# SciResearchKit for VS Code

<p align="center">
  <img src="https://raw.githubusercontent.com/thalamuxtech/SciResearchKit/main/srk_logo_hero.png" alt="SciResearchKit logo" width="360">
</p>

Load the [SciResearchKit](https://github.com/thalamuxtech/SciResearchKit) scientific-research skill directly inside your editor. The extension ships an offline copy of `SKILL.md`, `ETHICS.md`, all thirteen reference files, and all four templates, and adds a small command set to insert or open them.

Model-agnostic. Works alongside GitHub Copilot Chat, Continue, Cline, Cursor, or a plain paste into a hosted LLM system-prompt slot.

## Commands

Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type "SciResearchKit":

| Command | What it does |
|---|---|
| `SciResearchKit: Insert system prompt (SKILL.md + ETHICS.md)` | Inserts the full system prompt at the cursor (or opens a new document if no editor is active) |
| `SciResearchKit: Copy system prompt to clipboard` | Copies SKILL.md + ETHICS.md so you can paste it into an LLM's system-prompt field |
| `SciResearchKit: Open SKILL.md` | Opens the router file in a new document |
| `SciResearchKit: Open ETHICS.md (ethical-use notice)` | Opens the ethics notice in a new document |
| `SciResearchKit: Open reference...` | Quick-pick over the thirteen reference files (writing-style, citations, methods-and-statistics, ...) |
| `SciResearchKit: Open template...` | Quick-pick over the four templates (IMRaD paper, response-to-reviewers, specific aims, preregistration) |

## Ethical use

SciResearchKit is a productivity aid for a human researcher. It does not replace manual human review, and it does not override any restriction on AI use imposed by a journal, conference, funder, institution, or ethics body.

Four conditions apply to every use:

1. A qualified human reads, verifies, and signs off on every output before it is submitted or published.
2. The user checks and complies with venue, funder, and institutional AI-use and disclosure policies. Many venues and funders prohibit AI in peer review and grant review — do not use the toolkit for tasks the applicable policy places off-limits.
3. Do not upload confidential material (unpublished manuscripts under review, identifiable clinical data, third-party proprietary data) to a hosted AI system without the specific permission the confidentiality holder requires.
4. Do not use the toolkit to fabricate data or citations, to bypass a required disclosure, to impersonate an author or reviewer, or to circumvent institutional or legal restrictions on AI in research.

Full statement, rationale, and disclosure template: run `SciResearchKit: Open ETHICS.md (ethical-use notice)` after installation, or read [`ETHICS.md`](https://github.com/thalamuxtech/SciResearchKit/blob/main/ETHICS.md) in the repository.

## Privacy

The extension reads only from its own installation directory. No network calls, no telemetry, no workspace scanning.

## License

MIT. Use of the toolkit is additionally subject to the ethical-use conditions above.
