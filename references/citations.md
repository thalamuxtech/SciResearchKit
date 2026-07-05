# Citations

A citation makes a promise: the cited source supports the exact sentence it attaches to. Break that promise and you mislead readers and reviewers. This file sets the rule for verified, relevant, current citations.

## Three tests every citation passes

1. Support test. The source supports the specific claim, not a loosely related topic. Read the source claim, not the title.
2. Existence test. The source resolves to a real, findable record with a DOI, a stable URL, or a full bibliographic entry.
3. Priority test. The source is recent and top tier where such a source exists. Recent and authoritative beat old and obscure.

A citation that fails any test gets fixed or removed.

## Support test in practice

- Attach the citation to the sentence it backs, not to the paragraph.
- If a sentence makes two claims, it needs a source for each, or a split into two sentences.
- Do not cite a review when you mean the primary study. Cite the primary source for a specific finding. Cite the review for the state of a field.
- Do not cite a preprint as if peer reviewed. Mark preprints as preprints.
- Quote or paraphrase the source claim accurately. Do not stretch a hedged finding into a firm one.

## Existence test in practice

- Every reference resolves to a DOI, a PubMed ID, an arXiv ID, an ISBN, or a stable institutional URL.
- Confirm author list, year, venue, and title match the real record.
- Watch for model-generated citations. AI models invent plausible references. Treat every citation you did not personally retrieve as unverified until checked.
- When you cannot verify a citation, flag it in the output with a clear marker and ask the user to confirm or supply the source.

## Priority test in practice

Rank candidate sources in this order:

1. Recent and top tier. A current paper in a leading venue or journal.
2. Foundational and top tier. The original high-impact source for a method or concept.
3. Recent and mid tier. A current paper in a credible venue.
4. Older or lower tier. Use only when no better source exists, and say why.

Signals of top tier: leading field journals and conferences, high citation counts relative to age, reputable groups, replication by others. Recency matters most in fast-moving fields. State the field norm when it affects the choice.

## What needs a citation

- Every factual claim you did not generate from your own data.
- Every method, dataset, tool, or instrument you used.
- Every prior result you compare against.
- Every definition or framework you adopt.

What does not need a citation: your own results, common knowledge in the field, and your own reasoning.

## Verification workflow

When the user gives you citations or asks you to add them:

1. Extract each citation and the claim it supports.
2. For each, run the support, existence, and priority tests.
3. Retrieve the source record. Confirm the bibliographic fields.
4. Confirm the source backs the claim. Read the relevant section, not the abstract alone.
5. Mark each citation: verified, needs better source, or unverifiable.
6. Return the marked list. Replace weak sources. Flag unverifiable ones for the user.

## Honesty rule for unverifiable citations

Never present an unverified citation as verified. If you cannot retrieve and confirm a source, say so. State: based on available access, this citation is unverified, please confirm the DOI or supply the source. Do not fabricate a DOI, a page range, or an author list to fill the gap.

## Reference formatting

- Match the target venue style exactly. Common styles: APA, Vancouver, IEEE, Nature, Chicago.
- Keep one style across the whole document.
- Include DOIs where the style allows.
- For preprints, include the repository and the identifier, and mark the version.

## Quality gate for citations

Before returning any cited text:

1. Each citation attaches to the specific claim it supports.
2. Each reference resolves to a real, findable record.
3. Sources skew recent and top tier, with exceptions justified.
4. No citation is presented as verified unless you confirmed it.
5. Reference style is consistent and matches the venue.
6. Every unverifiable citation is flagged for the user.
