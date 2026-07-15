# Introduction Writer

## Purpose

Draft or revise an introduction that turns the paper strategy into a persuasive, fair, and evidence-backed story. The introduction should make reviewers understand why the problem matters, what gap remains, what the paper contributes, and how the paper proves it.

## When To Use

- Writing the first Introduction.
- Revising a rejected paper's framing.
- Aligning Introduction claims with experiments.
- Shortening or sharpening a long motivation section.

## Inputs

Required:

- paper thesis;
- target venue and paper type;
- contribution map;
- available results and figures;
- related-work summary;
- known limitations.

Optional:

- current Introduction;
- novelty-scout report;
- claim-evidence matrix;
- target page budget.

## Recommended Paragraph Roles

1. Problem anchor.
   Start with the concrete task, setting, or failure mode. Avoid generic "X is important" openings.

2. Why existing approaches are insufficient.
   Describe the gap fairly and specifically. Do not attack prior work without evidence.

3. Key insight.
   State the mechanism or observation that makes the proposed approach plausible.

4. Approach overview.
   Explain what the paper does at a high level without implementation overload.

5. Evidence preview.
   Preview datasets, experiments, theory, systems evaluation, or clinical validation.

6. Contributions.
   List 2-4 testable contributions, each tied to later evidence.

## Procedure

1. Identify all promises made by the current introduction.
2. Remove promises not supported by the paper.
3. Reorder paragraphs so motivation leads to gap, gap leads to insight, insight leads to evidence.
4. Make contribution bullets falsifiable.
5. Check that each contribution appears later in method/results/discussion.
6. Move detailed literature taxonomy to Related Work unless it is necessary for motivation.
7. Produce a patch plan instead of a blind rewrite when source text is provided.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Opening | Concrete problem and stakes | Generic field overview |
| Gap | Specific and fair | Vague "existing methods fail" |
| Insight | Explains why the method should work | Only names the method |
| Contributions | Testable and evidence-linked | Marketing or implementation list |
| Flow | Each paragraph earns the next | Disconnected background blocks |
| Scope | Clear assumptions and limits | Overclaims broad impact |

## Venue Adaptation

- ICLR/NeurIPS/ICML: foreground conceptual novelty, learning problem, and rigorous empirical/theoretical proof.
- CVPR/ECCV: use figure-driven motivation and clear dataset/task/baseline setup.
- AAAI: state broad AI relevance and avoid policy-sensitive generated-text framing.
- TMI: foreground medical-imaging motivation, validation scope, patient/data context, and clinical caveats.
- arXiv: preserve public readability and add non-anonymous links only when appropriate.

## Output Contract

Return:

```text
Introduction diagnosis:
Paragraph role plan:
Revised contribution bullets:
Claim-evidence alignment:
Suggested rewrite or patch plan:
Reviewer risks:
```

## Common Failure Modes

- Opening with a broad, interchangeable sentence.
- Spending a full page on motivation before stating the actual gap.
- Listing contributions that are not evaluated later.
- Introducing baselines or datasets only in Experiments, leaving reviewers confused early.
- Making "first" claims before novelty search.

## Mini Example

Weak contribution bullet:

```text
We design a powerful and flexible network for segmentation.
```

Stronger contribution bullet:

```text
We introduce a boundary-uncertainty module that produces multiple plausible lesion masks and show that it improves calibration under inter-rater disagreement.
```

## Sources Reviewed

Original synthesis based on the project distillation notes for section-aware review, claim-evidence auditing, and reviewer-risk workflows.
