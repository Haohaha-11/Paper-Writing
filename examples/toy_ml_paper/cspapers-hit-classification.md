# cspapers Hit Classification: Synthetic Example

This example demonstrates the format. It is not a live query log.

| Query | Hit Title | Venue | Year | Score | Abstract Checked | Class | Draft Citation Status | Action |
|---|---|---:|---:|---:|---|---|---|---|
| diffusion model medical image segmentation | Ambiguous Medical Image Segmentation Using Diffusion Models | CVPR | 2023 | 0.84 | yes | direct overlap | missing | inspect full paper; cite and distinguish |
| uncertainty segmentation annotator disagreement | Probabilistic Masks for Ambiguous Segmentation | NeurIPS | 2024 | 0.62 | no | same task | missing | retrieve abstract/full paper |
| ensemble uncertainty lesion segmentation | Ensembles for Calibrated Medical Segmentation | MICCAI | 2022 | n/a | yes | missing baseline | missing | consider baseline or justify exclusion |
| diffusion mask calibration | Calibrated Generative Segmentation | ICLR | 2025 | 0.51 | yes | same method | missing | cite if relevant |

## Novelty Risks

- The phrase "first diffusion method for ambiguous medical segmentation" is unsafe.
- The draft should distinguish itself from diffusion segmentation papers by dataset, uncertainty target, and calibration metric.
- Ensemble baselines may be expected if the paper discusses uncertainty.

## Claim Wording Changes

Unsafe:

```text
We are the first to use diffusion for ambiguous medical image segmentation.
```

Safer:

```text
We study diffusion-mask sampling for calibration under synthetic annotator disagreement and compare it against deterministic and ensemble baselines.
```

## Full-Paper Inspection Needed

- Ambiguous Medical Image Segmentation Using Diffusion Models
- Calibrated Generative Segmentation
