# Page Compressor

## Purpose

Reduce paper length while preserving scientific meaning, evidence, citations, equations, and LaTeX safety. This skill is for page-limit pressure, not for hiding missing evidence.

## When To Use

- Paper exceeds page limit.
- Abstract/introduction is too verbose.
- Related Work is a citation list rather than focused positioning.
- Camera-ready changes create page overflow.

## Inputs

Required:

- target venue page limit;
- section text or full draft;
- protected content list: equations, theorem statements, claims, citations, figures, tables, labels, refs.

Optional:

- target word/page reduction;
- venue checklist;
- claim-evidence matrix;
- reviewer-required text that must not be removed.

## Compression Order

1. Remove redundant motivation.
2. Collapse repeated definitions.
3. Replace long transitions with direct topic sentences.
4. Merge overlapping related-work sentences.
5. Compress implementation details that can move to appendix.
6. Shorten captions only if they remain self-contained.
7. Remove content only after marking the scientific cost.

## Protected Content

Do not remove or silently alter:

- claims tied to contribution bullets;
- citations supporting claims;
- equations and theorem assumptions;
- labels, refs, citations, and figure/table references;
- limitations, ethics, reproducibility, and venue-required checklist text;
- reviewer-requested clarifications.

## Rubric

| Dimension | Strong Compression | Bad Compression |
|---|---|---|
| Meaning | Same claims, fewer words | Claim scope changes |
| Evidence | Evidence preserved | Results/citations removed |
| LaTeX safety | Commands intact | Labels/refs/cites broken |
| Venue safety | Required sections preserved | Checklist/ethics removed |
| Readability | Tighter flow | Dense and cryptic |

## Venue Adaptation

- ICLR/NeurIPS/ICML: preserve limitations, reproducibility details, checklist-related content, and ablation explanations.
- CVPR/ECCV: preserve figure captions, visual evidence, baseline details, and supplement pointers.
- AAAI: preserve policy-sensitive wording around AI-generated text and author-written contributions.
- TMI: preserve references in the page count, validation details, clinical caveats, privacy/IRB language, and conference-extension disclosures.
- arXiv: preserve public links, acknowledgments, and source-package references only when appropriate for the public version.

## Output Contract

Return:

```text
Target reduction:
Compression strategy:
Compressed text or patch suggestions:
Removed content:
Evidence at risk:
LaTeX safety notes:
Residual page risk:
```

## Common Failure Modes

- Removing limitations to save space.
- Compressing away dataset/protocol details needed for reproducibility.
- Breaking LaTeX commands during sentence editing.
- Removing citations but leaving claims.
- Making prose shorter but less reviewable.

## Mini Example

Verbose:

```text
It is worth noting that the proposed method, which is described in detail in the following section, can be applied to the problem of lesion segmentation in a way that is able to account for ambiguity.
```

Compressed:

```text
The proposed method models ambiguity in lesion segmentation.
```

## Sources Reviewed

Original synthesis based on patch-first editing constraints, LaTeX safety notes, and page-limit workflows in this repository.
