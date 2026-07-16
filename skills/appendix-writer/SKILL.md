# Appendix Writer

## Purpose

Organize appendix material so it supports the main paper without hiding essential claims or evidence from the main text.

## When To Use

- Preparing supplementary proofs, implementation details, extended tables, prompts, datasets, or additional figures.
- Moving content out of the main paper due to page limits.
- Checking whether the main text improperly depends on appendix-only evidence.

## Inputs

Required:

- target venue appendix/supplement rules;
- main paper claim-evidence matrix;
- candidate appendix materials;
- main text references to appendix.

Optional:

- supplementary file policy;
- anonymous-review constraints;
- camera-ready changes.

## Procedure

1. Classify appendix material: proof, implementation, extra experiment, dataset detail, failure case, prompt, ethics, or supplement.
2. Check whether any main claim relies only on appendix evidence.
3. Add clear cross-references from main text.
4. Keep appendix sections searchable and self-contained.
5. Preserve anonymity and venue supplement rules.
6. Move non-essential detail to appendix; keep decisive evidence in main text.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Main-text independence | Core claims supported in main paper | Main proof hidden in appendix |
| Organization | Clear appendix sections | Dump of leftovers |
| Referencing | Main text points to appendix | Appendix unreferenced |
| Compliance | Follows venue supplement rules | Anonymous leaks or wrong file type |
| Reproducibility | Useful implementation detail | Missing key settings |

## Venue Adaptation

- ICLR/NeurIPS/ICML: appendices are common for proofs, extended experiments, and reproducibility details.
- CVPR/ECCV: supplement may include additional visual examples, videos, or implementation details; anonymity still matters.
- AAAI: verify author-kit and supplement rules before relying on appendix.
- TMI: supplementary file types are constrained; challenge or conference-extension materials need careful handling.
- arXiv: appendix can be public, but ensure source package compiles cleanly.

## Output Contract

Return:

```text
Appendix inventory:
Main-claim dependency risks:
Recommended appendix structure:
Cross-reference plan:
Venue compliance notes:
Materials to move back to main text:
```

## Common Failure Modes

- Putting decisive evidence only in appendix.
- Leaving appendix material unreferenced.
- Including identity-revealing supplement content in anonymous review.
- Treating appendix as unlimited space for unclear writing.

## Mini Example

Weak appendix heading:

```text
More Results
```

Stronger:

```text
Appendix B: Calibration Across Random Seeds
```

## Sources Reviewed

Original synthesis based on venue rules, arXiv export notes, and paper-redteam workflows.
