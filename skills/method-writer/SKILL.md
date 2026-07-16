# Method Writer

## Purpose

Draft or revise the Method section so that reviewers can understand what the method does, why it should work, and how to reproduce the key algorithmic choices.

## When To Use

- Turning an idea or implementation into a paper-ready Method section.
- Checking whether notation, assumptions, and algorithm steps are clear.
- Revising a rejected paper whose method was considered vague or underspecified.
- Preparing method content for ICLR, NeurIPS, CVPR, ICML, ECCV, AAAI, or TMI.

## Inputs

Required:

- paper thesis and contribution map;
- method summary;
- problem formulation;
- inputs, outputs, assumptions, and notation;
- algorithm or model architecture;
- training/inference procedure;
- implementation constraints that affect claims.

Optional:

- pseudocode;
- diagrams;
- equations;
- ablation plan;
- reproducibility checklist.

## Procedure

1. Define the task and notation before introducing the method.
2. State assumptions and scope conditions explicitly.
3. Separate problem formulation, model design, optimization/training, and inference.
4. Explain the mechanism behind the claimed improvement.
5. Add algorithmic details only when they affect reproducibility or claims.
6. Cross-check method claims against planned experiments.
7. Move purely engineering details to appendix unless they are central to the contribution.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Problem formulation | Inputs, outputs, assumptions clear | Method starts without task definition |
| Mechanism | Explains why the method should work | Only lists components |
| Reproducibility | Key hyperparameters/procedure recoverable | Missing training/inference details |
| Claim alignment | Method supports contribution bullets | Method includes unrelated features |
| Notation | Minimal and consistent | Overloaded or undefined symbols |

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize conceptual mechanism, assumptions, algorithmic clarity, and ablations.
- CVPR/ECCV: connect method modules to visual evidence and architecture diagrams.
- AAAI: keep method broadly understandable to AI reviewers outside a narrow subfield.
- TMI: include medical-imaging preprocessing, modality assumptions, validation constraints, and clinical-scope caveats.
- arXiv: include enough implementation detail for public reproducibility.

## Output Contract

Return:

```text
Method diagnosis:
Notation plan:
Section outline:
Missing assumptions:
Reproducibility gaps:
Suggested method text or patch plan:
Experiment links:
```

## Common Failure Modes

- Introducing a module without explaining the failure mode it addresses.
- Using notation before defining it.
- Claiming generality while making dataset-specific design choices.
- Hiding key training/inference details in code only.
- Adding complexity that is not evaluated in ablations.

## Mini Example

Weak:

```text
We add an uncertainty module to improve segmentation.
```

Stronger:

```text
Given image \(x\), the model predicts a distribution over masks by sampling latent noise \(z\) through a diffusion decoder. This design lets the model represent multiple plausible boundaries when annotator masks disagree.
```

## Sources Reviewed

Original synthesis based on the repository's strategist, claim-evidence, review, and venue-rule workflows.
