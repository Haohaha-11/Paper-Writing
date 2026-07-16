# Results Writer

## Purpose

Turn verified experimental outputs into a precise Results narrative. This skill helps authors state what the results show, what they do not show, and how figures/tables support the paper's claims.

## When To Use

- Writing result paragraphs from tables and figures.
- Revising overclaimed result text.
- Aligning Results with Abstract and Introduction claims.
- Preparing figure/table callouts.

## Inputs

Required:

- tables and figures;
- metric definitions;
- baseline names;
- key numerical findings;
- claim-evidence matrix.

Optional:

- statistical tests;
- seed variance;
- qualitative examples;
- failure cases.

## Procedure

1. Identify the claim each table/figure supports.
2. State the comparison before interpreting the number.
3. Report exact metrics and conditions when central.
4. Distinguish main results, ablations, qualitative results, and failure cases.
5. Avoid causal explanations unless the experiment isolates the cause.
6. Add caveats for small datasets, high variance, or missing baselines.
7. Ensure result statements match Abstract/Introduction wording.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Specificity | Names metric, baseline, setting | Says "better" |
| Claim alignment | Supports stated contribution | New claims appear only in Results |
| Interpretation | Explains what result means | Repeats table values |
| Scope | Notes limitations | Generalizes beyond setup |
| Visual linkage | Figures are referenced meaningfully | Figures are decorative |

## Venue Adaptation

- ICLR/NeurIPS/ICML: connect results to hypotheses, ablations, and robustness.
- CVPR/ECCV: balance quantitative results with qualitative examples and failure cases.
- AAAI: keep result interpretation accessible to broad AI reviewers.
- TMI: avoid clinical utility claims unless validation supports them; report cohort/protocol limits.
- arXiv: include complete result context and artifact availability.

## Output Contract

Return:

```text
Result narrative:
Table/figure claim map:
Overclaimed statements:
Missing caveats:
Suggested paragraphs or patch plan:
Residual risks:
```

## Common Failure Modes

- Saying "significant" without statistical support.
- Explaining every number instead of the decisive pattern.
- Claiming robustness from one dataset.
- Omitting negative or failure cases that affect scope.
- Introducing new claims not prepared in Introduction.

## Mini Example

Weak:

```text
Our method achieves 0.82 Dice and is better than baselines.
```

Stronger:

```text
On the synthetic ambiguous-boundary benchmark, the diffusion-mask model improves expected calibration error over deterministic U-Net while maintaining comparable Dice, supporting the claim that sampling mask alternatives improves uncertainty representation rather than merely increasing overlap accuracy.
```

## Sources Reviewed

Original synthesis based on the project's experiments, claim-evidence, and redteam workflows.
