# Related Work Writer

## Purpose

Create related work that is citation-grounded, fair to prior papers, and useful for positioning the current contribution. The goal is not to list papers; it is to explain the intellectual neighborhood of the paper and why the current work is still needed.

## When To Use

- Building Related Work from a bibliography and paper context.
- Checking whether recent target-venue papers are missing.
- Revising unfair or vague comparisons.
- Preparing reviewer-facing novelty and baseline defenses.

## Inputs

Required:

- paper thesis and contribution map;
- target venue and adjacent venues;
- current bibliography or must-cite list;
- direct competitors;
- method/task/dataset keywords.

Optional:

- cspapers-assisted review output;
- paper-qa or local PDF notes;
- reviewer comments about missing citations;
- venue-specific baseline expectations.

## Procedure

1. Build a taxonomy.
   Group prior work by technical axis, task, dataset, modeling assumption, or evaluation protocol. Avoid pure chronology.

2. Identify comparison roles.
   Mark each cited work as direct competitor, background, tool, dataset, baseline, theory, or role model.

3. Verify citation support.
   Each citation should support the sentence it appears in. Mark unchecked citations.

4. Search for missing work.
   Use cspapers.org and other sources to find recent target-venue or adjacent-venue papers.

5. Write contrastive positioning.
   For each group, say what prior work established, what limitation remains, and how this paper differs.

6. Connect to experiments.
   Direct competitors and baselines named in Related Work should be reflected in Experiments when appropriate.

7. Remove unfair claims.
   Replace "fails to" or "cannot" with precise, evidence-backed limitations unless the prior paper explicitly shows the failure.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Organization | Conceptual taxonomy | Chronological paper list |
| Citation grounding | Sentence-level support | Decorative citation clusters |
| Fairness | Accurate limits of prior work | Strawman comparisons |
| Recency | Includes recent target-venue work | Mostly old or convenient citations |
| Positioning | Explains why this paper is needed | Says "different" without reason |
| Baseline link | Competitors map to experiments | Related Work and Experiments disconnected |

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize conceptual, algorithmic, and empirical relationship to recent ML work.
- CVPR/ECCV: include visual task baselines, datasets, and recent conference papers.
- AAAI: maintain broad AI context and policy-compliant author-written text.
- TMI: include medical-imaging baselines, clinical/validation context, dataset provenance, and modality-specific prior work.
- arXiv: include enough context for broader readers while preserving technical precision.

## Output Contract

Return:

```text
Related work taxonomy:
Direct competitors:
Background citations:
Missing citations:
Possible missing baselines:
Risky comparison claims:
Suggested paragraphs or patch plan:
Unchecked citation support:
```

## Common Failure Modes

- Citing a paper because it has related keywords, not because it supports the sentence.
- Omitting recent papers from the exact target venue.
- Using Related Work to attack prior work too aggressively.
- Treating preprints and peer-reviewed venue papers as equivalent without context.
- Adding citations that were not actually inspected.

## Mini Example

Weak:

```text
Many works study segmentation [1,2,3,4]. Unlike them, we use diffusion.
```

Stronger:

```text
Deterministic segmentation networks optimize a single mask for each image and therefore struggle to represent annotator disagreement in ambiguous lesions. Recent probabilistic and ensemble approaches address uncertainty by sampling model parameters or latent variables, but they often require multiple forward passes without explicitly modeling boundary alternatives. Our work instead uses diffusion sampling to generate multiple plausible masks and evaluates calibration against inter-rater variability.
```

## Sources Reviewed

Original synthesis based on cspapers integration notes, citation-grounded RAG patterns, reviewer simulation workflows, and project venue rules.
