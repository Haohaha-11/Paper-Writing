# Paper Context

## Metadata

- Working title: Boundary Tokens for Synthetic-to-Real Scene Parsing
- Target venue: CVPR 2026
- Paper type: method paper
- Blind review: yes

## Thesis

Explicit boundary tokens can improve scene parsing transfer when trained with synthetic annotations and calibrated using a small real validation split.

## Contributions

1. Boundary token representation for segmentation transformers.
2. Synthetic-to-real adaptation loss using boundary consistency.
3. Analysis of boundary error reduction across rare classes.

## Evidence Inventory

| Asset | Status | Needed Before Submission |
|---|---|---|
| Main comparison table | synthetic placeholder | run full benchmark |
| Ablation table | partial | add token count and loss weight sweeps |
| Qualitative figure | planned | ensure examples are representative |
| Failure cases | missing | add cluttered/night scenes |

## Review Risks

- Comparison to recent domain adaptation baselines may be incomplete.
- Qualitative figures could overstate gains if examples are cherry-picked.
- Boundary metric needs a clear definition and implementation note.
