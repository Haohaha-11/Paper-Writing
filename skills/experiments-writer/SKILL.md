# Experiments Writer

## Purpose

Draft or revise the Experiments section so that the evidence directly answers the paper's claims. Experiments should be a proof plan, not a collection of convenient results.

## When To Use

- Planning experiments before submission.
- Revising an experiments section after reviewer-style feedback.
- Checking baseline, metric, dataset, and ablation coverage.
- Preparing a venue-specific empirical story.

## Inputs

Required:

- claim-evidence matrix;
- datasets and splits;
- baselines;
- metrics;
- implementation and training protocol;
- main results;
- ablations.

Optional:

- statistical tests;
- seed variance;
- qualitative examples;
- failure cases;
- compute budget.

## Procedure

1. Map each main claim to an experiment or analysis.
2. Define datasets, splits, metrics, and evaluation protocol before reporting numbers.
3. Justify baselines and include recent target-venue competitors where applicable.
4. Present main results first, then ablations, robustness, efficiency, and failure analysis.
5. Explain what each table or figure proves.
6. Separate empirical findings from speculation.
7. Mark missing evidence that should weaken claims.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Claim coverage | Every main claim has evidence | Results do not answer claims |
| Baselines | Recent and relevant | Convenient or outdated only |
| Protocol | Datasets/splits/metrics clear | Evaluation setup ambiguous |
| Ablations | Test key method choices | Cosmetic or missing |
| Statistics | Variance/significance when needed | Single number overinterpreted |
| Failure analysis | Honest limits | Only best-case results |

## Venue Adaptation

- ICLR/NeurIPS/ICML: include ablations, reproducibility details, and robustness/generalization checks.
- CVPR/ECCV: include strong visual baselines, qualitative examples, and failure cases.
- AAAI: make the experimental story understandable across AI subfields.
- TMI: specify modality, cohort, split, external validation, reader/clinical protocol, and privacy constraints where applicable.
- arXiv: include full experimental detail and public artifacts when possible.

## Output Contract

Return:

```text
Experiment plan:
Claim-to-experiment map:
Dataset/protocol checks:
Baseline gaps:
Ablation gaps:
Result narrative:
Missing evidence:
Suggested section text or patch plan:
```

## Common Failure Modes

- Reporting SOTA without recent baselines.
- Using ablations that do not test the core mechanism.
- Omitting dataset split details.
- Making clinical or deployment claims from retrospective/internal experiments.
- Overexplaining tables while not stating what they prove.

## Mini Example

Weak:

```text
Table 1 shows our method performs better.
```

Stronger:

```text
Table 1 tests the central claim that sampling mask distributions improves calibration under annotator disagreement. The diffusion decoder reduces expected calibration error relative to deterministic and ensemble baselines while preserving Dice.
```

## Sources Reviewed

Original synthesis based on claim-evidence auditing, paper-redteam experimental rubrics, and venue rules.
