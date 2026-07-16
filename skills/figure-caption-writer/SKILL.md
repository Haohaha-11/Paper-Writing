# Figure Caption Writer

## Purpose

Write figures and captions that communicate evidence clearly. A good figure should make a claim easier to evaluate, not merely decorate the paper.

## When To Use

- Designing the paper's figure plan.
- Revising captions for clarity and reviewer usefulness.
- Checking whether figures support claims in Abstract, Introduction, or Results.
- Preparing CVPR/ECCV or TMI submissions where visual evidence is central.

## Inputs

Required:

- figure image or description;
- claim the figure supports;
- target venue;
- related section text;
- experimental setting or data source.

Optional:

- panel labels;
- metric definitions;
- qualitative examples;
- failure cases;
- accessibility constraints.

## Procedure

1. Identify the figure's purpose: overview, method diagram, quantitative result, qualitative result, failure case, dataset example, or ablation.
2. State the takeaway in the caption's first sentence.
3. Define panels, colors, symbols, and metrics.
4. Connect the figure to a claim in the paper.
5. Avoid hiding important experimental conditions in tiny text.
6. Check anonymity and data/privacy constraints.
7. Ensure the main text calls out the figure.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Takeaway | Caption states what to learn | Caption only names components |
| Self-contained | Panels/metrics clear | Reader must guess |
| Evidence link | Supports a paper claim | Decorative |
| Visual clarity | Readable and focused | Too dense or tiny |
| Compliance | Anonymous/privacy-safe | Leaks identity or sensitive data |

## Venue Adaptation

- ICLR/NeurIPS/ICML: use figures to explain mechanisms and summarize evidence compactly.
- CVPR/ECCV: qualitative figures and visual comparisons must be fair, readable, and not cherry-picked.
- AAAI: keep captions understandable to broad AI readers.
- TMI: protect patient privacy; include modality, view, and relevant clinical context when appropriate.
- arXiv: ensure public images have permissions and no anonymous-review artifacts.

## Output Contract

Return:

```text
Figure purpose:
Claim supported:
Caption draft:
Panel explanations:
Main-text callout:
Privacy/anonymity notes:
Revision risks:
```

## Common Failure Modes

- Captions that only say "Overview of our method."
- Figures that do not map to any claim.
- Qualitative examples without failure cases or selection criteria.
- Patient images without privacy/de-identification context.
- Tiny labels that are unreadable after conference formatting.

## Mini Example

Weak:

```text
Figure 2: Our model.
```

Stronger:

```text
Figure 2: The diffusion-mask decoder samples multiple plausible lesion boundaries conditioned on the same image, allowing the model to represent annotator disagreement rather than forcing a single deterministic mask.
```

## Sources Reviewed

Original synthesis based on CVPR/ECCV visual-evidence expectations, TMI privacy constraints, and the repository's claim-evidence workflow.
