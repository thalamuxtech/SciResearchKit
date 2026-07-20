# sciresearchkit

<p align="center">
  <img src="https://raw.githubusercontent.com/thalamuxtech/SciResearchKit/main/srk_logo_hero.png" alt="SciResearchKit logo" width="360">
</p>

Python distribution of [SciResearchKit](https://github.com/thalamuxtech/SciResearchKit), a model-agnostic Markdown skill that turns any capable LLM into a rigorous scientific-research collaborator. Eight phases, three hard rules, zero runtime.

The package bundles the full Markdown corpus (`SKILL.md`, `ETHICS.md`, thirteen reference files, four templates) and provides a small Python API for loading it into any Python-hosted LLM harness.

## Install

```bash
pip install sciresearchkit
```

## Quickstart

```python
import sciresearchkit as srk

# The recommended system prompt: SKILL.md + ETHICS.md
prompt = srk.system_prompt()

# Individual pieces
skill    = srk.get_skill()
ethics   = srk.get_ethics()
writing  = srk.get_reference("writing-style")
imrad    = srk.get_template("imrad-paper")

# Listings
srk.list_references()   # ['analysis-and-results', 'citations', ...]
srk.list_templates()    # ['imrad-paper', 'preregistration', ...]

# Filesystem handle to the bundled corpus
srk.data_dir()          # PosixPath('.../site-packages/sciresearchkit/data')
```

## Command line

```bash
sciresearchkit                        # print SKILL.md + ETHICS.md (system prompt)
sciresearchkit skill                  # print SKILL.md
sciresearchkit ethics                 # print ETHICS.md
sciresearchkit references             # list reference slugs
sciresearchkit reference writing-style
sciresearchkit templates              # list template slugs
sciresearchkit template imrad-paper
sciresearchkit path                   # print the bundled data directory
```

Pipe the prompt into a system-prompt slot:

```bash
sciresearchkit > srk_system_prompt.txt
```

## Ethical use

SciResearchKit is a productivity aid for a human researcher. It does not replace manual human review, and it does not override any restriction on AI use imposed by a journal, conference, funder, institution, or ethics body.

Four conditions apply to every use:

1. A qualified human reads, verifies, and signs off on every output before it is submitted or published.
2. The user checks and complies with the target venue's, funder's, and institutional AI-use and disclosure policies. Many venues and funders prohibit AI in peer review and grant review — do not use the toolkit for tasks the applicable policy places off-limits.
3. Do not upload confidential material (unpublished manuscripts under review, identifiable clinical data, third-party proprietary data) to a hosted AI system without the specific permission the confidentiality holder requires.
4. Do not use the toolkit to fabricate data or citations, to bypass a required disclosure, to impersonate an author or reviewer, or to circumvent institutional or legal restrictions on AI in research.

Full statement, rationale, and disclosure template: run `sciresearchkit ethics` or read [`ETHICS.md`](https://github.com/thalamuxtech/SciResearchKit/blob/main/ETHICS.md) in the repository.

## License

MIT. Use of the toolkit is additionally subject to the ethical-use conditions above.
