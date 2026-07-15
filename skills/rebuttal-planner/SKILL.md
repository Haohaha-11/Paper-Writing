# Rebuttal Planner

## Purpose

Turn reviews into a clear response strategy, concise rebuttal text, and a revision plan. The goal is not to "win an argument"; it is to reduce reviewer uncertainty with evidence, clarification, and concrete changes.

## When To Use

- After receiving reviews.
- During author response or discussion periods.
- Before camera-ready revision planning.
- When deciding which new experiments or analyses are worth doing.

## Inputs

Required:

- all reviewer comments with reviewer IDs;
- target venue response rules;
- paper context and contribution map;
- current evidence/results;
- constraints on rebuttal length.

Optional:

- draft response;
- new experiment results;
- paper-redteam report;
- claim-evidence matrix.

## Procedure

1. Split comments into atomic issues.
   One reviewer paragraph may contain multiple issues.

2. Cluster issues.
   Use categories: novelty, correctness, experiments, baselines, clarity, citations, reproducibility, ethics, presentation, venue fit.

3. Assign decision impact.
   High impact issues affect soundness, novelty, or main evidence. Low impact issues are wording or presentation only.

4. Choose response type.
   Use: clarify, concede, correct misunderstanding, provide evidence, add experiment, add citation, revise text, or defer to limitations.

5. Draft response.
   Be concise, factual, respectful, and specific. Reference exact new evidence or planned revision.

6. Update revision plan.
   Every promised change must map to a paper section or artifact.

7. Mark residual risk.
   State what the response cannot fully solve.

## Response Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Specificity | Directly answers the issue | Generic thanks and restatement |
| Evidence | Points to result/text/change | Says "we believe" |
| Tone | Respectful and concise | Defensive or dismissive |
| Traceability | Maps to paper revision | No follow-up action |
| Honesty | Concedes real limitations | Overpromises |

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize evidence, ablations, theoretical assumptions, reproducibility, and limitations.
- CVPR/ECCV: emphasize visual examples, baseline fairness, dataset protocol, and supplement clarifications.
- AAAI: avoid promising AI-generated text changes that would violate official policy; frame edits as author-written revisions.
- TMI: respond carefully to clinical validation, dataset provenance, privacy/IRB, patient population, and conference-extension concerns.
- arXiv: use rebuttal planning mainly to prepare a public revision summary, not an official response.

## Output Contract

Return:

```text
Issue clusters:
Decision-critical issues:
Response strategy:
Draft rebuttal text:
New evidence needed:
Paper revisions promised:
Risks after response:
```

## Common Failure Modes

- Responding to reviewer tone instead of technical substance.
- Promising experiments that cannot be completed or included.
- Ignoring repeated concerns across reviewers.
- Using rebuttal space to summarize the paper instead of resolving uncertainty.
- Overclaiming new results without updating the paper.

## Mini Example

Reviewer:

```text
The paper claims robustness but evaluates only one dataset.
```

Weak response:

```text
We thank the reviewer and believe our method is robust.
```

Stronger response:

```text
We agree that the original wording was too broad. We will revise the claim to "robust on the internal test split" and add a limitation noting that external protocol-shift validation remains future work. We also add an ablation across three random splits in Table X to show stability within the available dataset.
```

## Sources Reviewed

Original synthesis based on reviewer simulation, claim-evidence auditing, and revision-planning workflows in this repository.
