# Revision Editor

## Purpose

Turn review reports, claim audits, and writing suggestions into a controlled revision plan with patch-ready changes. This skill is the bridge between critique and actual paper edits.

## When To Use

- After `paper-redteam`.
- After real reviewer comments.
- Before camera-ready revision.
- When multiple skills produce overlapping suggestions.

## Inputs

Required:

- target venue;
- current draft or section text;
- review findings;
- claim-evidence matrix;
- list of required changes.

Optional:

- rebuttal plan;
- page budget;
- template or anonymity constraints;
- Git diff from prior version.

## Procedure

1. Cluster requested changes by section.
2. Separate scientific changes from wording changes.
3. Identify changes requiring new evidence, citations, or experiments.
4. Create a patch plan with file/section targets.
5. Preserve LaTeX commands, labels, refs, citations, equations, and figure/table references.
6. Avoid conflicting edits across Abstract, Introduction, Results, and Conclusion.
7. Produce a revision log for human approval.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Traceability | Every edit maps to an issue | Unmotivated rewrite |
| Safety | LaTeX and citations preserved | Broken refs/cites |
| Claim control | Claims stay evidence-backed | Stronger unsupported claims |
| Consistency | Abstract/intro/results align | Sections contradict |
| Review usefulness | Prioritizes decision impact | Cosmetic edits first |

## Venue Adaptation

- ICLR/NeurIPS/ICML: preserve limitations/reproducibility and update checklist-sensitive text.
- CVPR/ECCV: preserve figure references, supplement anonymity, and visual evidence.
- AAAI: ensure all text remains author-owned and policy-compliant.
- TMI: preserve page-count-sensitive references, clinical caveats, and privacy/IRB language.
- arXiv: convert anonymous review text to public version where appropriate.

## Output Contract

Return:

```text
Revision plan:
Section-by-section changes:
Evidence/citation dependencies:
Patch suggestions:
Consistency checks:
Changes requiring human approval:
Residual risks:
```

## Common Failure Modes

- Applying all suggestions without prioritization.
- Fixing wording while leaving evidence gaps.
- Updating Abstract but not Conclusion.
- Breaking LaTeX during local edits.
- Removing limitations to save space.

## Mini Example

Issue:

```text
Novelty claim is too broad because related diffusion segmentation work exists.
```

Revision action:

```text
Abstract: replace "first diffusion method" with "we study diffusion-mask sampling for synthetic annotator disagreement." Related Work: add inspected diffusion segmentation papers. Introduction: clarify the narrower calibration-focused contribution.
```

## Sources Reviewed

Original synthesis based on patch-first editing, rebuttal planning, and claim-evidence workflows in this repository.
