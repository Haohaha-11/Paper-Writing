# Rebuttal Plan: Synthetic Example

## Review Cluster

- Reviewer IDs: R1, R2
- Issue: Novelty and clinical scope are overstated.
- Decision impact: high

## Response Strategy

- Acknowledge: The original wording was too broad.
- Clarify: The paper studies a synthetic uncertainty benchmark, not clinical deployment.
- Evidence: Add related-work comparison and ablation table.
- Revision: Rewrite abstract/introduction claims and add limitations.
- Residual limitation: No real clinical validation.

## Draft Response

Thank you for pointing out the novelty and scope concerns. We agree that the original wording was too broad. We have revised the abstract and introduction to state that our evaluation is a controlled synthetic study of annotator disagreement, not evidence of clinical deployment. We also added a related-work paragraph distinguishing our calibration-focused synthetic setup from prior diffusion segmentation papers and added an ablation over sampling steps and uncertainty loss weight.

## Paper Changes

- Section: Abstract
  - Change: remove "first" and "clinical utility" wording.
  - Evidence added: synthetic calibration result summary.
  - Remaining risk: no real clinical validation.

- Section: Related Work
  - Change: add diffusion segmentation and probabilistic segmentation comparison.
  - Evidence added: inspected related papers.
  - Remaining risk: full baseline coverage still depends on available implementations.

- Section: Limitations
  - Change: state synthetic-only scope and need for real multi-reader validation.
  - Evidence added: none; this is a scope clarification.
  - Remaining risk: target venue may still expect real-data validation.
