# Abstract Writer

## Purpose

Draft or revise an abstract that makes a clear, evidence-backed promise about the paper. The abstract should help reviewers understand the problem, gap, method, result, and implication without exaggerating unsupported claims.

## When To Use

- Creating the first abstract from a paper context.
- Revising an abstract after experiments change.
- Compressing an abstract for venue constraints.
- Checking whether an abstract overclaims novelty or results.

## Inputs

Required:

- target venue and paper type;
- one-sentence thesis;
- main contributions;
- strongest verified result;
- task, dataset, metric, or validation protocol when central;
- known limitations or scope constraints.

Optional:

- current abstract;
- target word limit;
- novelty-scout report;
- claim-evidence matrix.

## Abstract Structure

Use this five-move structure unless the venue strongly suggests otherwise:

1. Problem: what concrete problem matters?
2. Gap: what is missing or insufficient in prior work?
3. Method/insight: what does this paper introduce?
4. Evidence: what result supports the claim?
5. Implication: what changes, within the proven scope?

## Procedure

1. Extract all claims from the current abstract or paper context.
2. Mark each claim as problem, gap, method, result, implication, or unsupported.
3. Require at least one concrete evidence sentence if the paper has experimental or empirical claims.
4. Replace vague adjectives with measurable scope: "improves Dice by X", "reduces memory by Y", "validated on Z", or "under assumption A".
5. Remove or weaken "first", "novel", "state-of-the-art", "robust", "clinical-grade", and similar terms unless backed by evidence.
6. Ensure the abstract does not introduce claims absent from the paper body.
7. Produce a revised abstract plus a claim-risk note.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Problem | Specific task/context | Generic field opening |
| Gap | Fair limitation in prior work | Strawman or vague "challenging" claim |
| Method | Clear mechanism or insight | Name-only method description |
| Evidence | Concrete result/validation | No numbers, datasets, or support |
| Scope | Honest implication | Broad conclusion beyond evidence |
| Readability | One coherent paragraph | List of disconnected claims |

## Venue Adaptation

- ICLR/NeurIPS/ICML: highlight conceptual insight and evidence for generality.
- CVPR/ECCV: name visual task, dataset family, and key empirical comparison when possible.
- AAAI: avoid generated-text policy issues; keep writing clearly author-owned.
- TMI: include modality/task/validation scope when central, and avoid clinical deployment claims unless validated.
- arXiv: make the abstract understandable to readers outside the exact review community.

## Output Contract

Return:

```text
Revised abstract:
Move breakdown:
Claim-evidence notes:
Risky phrases:
Missing facts:
Optional shorter version:
```

## Common Failure Modes

- Abstract only describes the method and never states the result.
- Abstract claims "state-of-the-art" but gives no benchmark or comparison.
- Abstract starts with a broad field slogan.
- Abstract includes citations or detailed related-work arguments that belong elsewhere.
- Abstract promises clinical utility without validation evidence.

## Mini Example

Weak:

```text
Deep learning has achieved great success in medical imaging. We propose a novel framework for robust segmentation and show good results.
```

Stronger:

```text
Ambiguous lesion boundaries make deterministic medical image segmentation unreliable when expert annotations disagree. We introduce an uncertainty-aware diffusion segmentation model that samples plausible boundary hypotheses and calibrates them against annotator variability. On two MRI lesion datasets, the model improves Dice and expected calibration error over deterministic and ensemble baselines. These results suggest that modeling annotation ambiguity can improve segmentation reliability in retrospective imaging studies.
```

## Sources Reviewed

Original synthesis based on the project's writing-skill research notes, claim-evidence design, paper-redteam workflow, and venue-specific rule files.
