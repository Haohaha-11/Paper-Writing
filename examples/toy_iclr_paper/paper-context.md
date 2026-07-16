# Paper Context

## Metadata

- Working title: Calibrated Contrastive Prototypes for Low-Label Recognition
- Target venue: ICLR 2026
- Paper type: method paper
- Blind review: yes

## Thesis

Prototype-based contrastive learning can improve calibration under label scarcity when prototype uncertainty is explicitly modeled during training.

## Contributions

1. A prototype uncertainty objective for low-label classification.
2. A calibration-aware sampling strategy for hard examples.
3. Synthetic evaluation on three small-label benchmarks.

## Current Evidence

| Claim | Evidence | Status |
|---|---|---|
| Improves expected calibration error | synthetic experiment table | needs full run log |
| Preserves accuracy | synthetic benchmark comparison | needs seed variance |
| Works under 1 percent labels | synthetic ablation | needs sensitivity analysis |

## Known Risks

- Novelty risk against prior calibrated contrastive learning papers.
- Experimental risk if gains disappear under stronger augmentations.
- Need clear distinction between calibration and uncertainty estimation.
