# Paper Strategist

## Purpose

Turn a research idea, draft, or result bundle into a defensible paper plan before drafting begins. This skill is the first gate for paper quality: it decides what the paper is really claiming, what evidence is needed, and what reviewers are likely to attack.

## When To Use

- Starting a new paper from notes, experiments, or a rough idea.
- Repositioning a rejected or weak draft.
- Choosing between ICLR/CVPR/NeurIPS/ICML/ECCV/AAAI/TMI/arXiv targets.
- Checking whether the current contribution story is strong enough to support a full paper.

## Inputs

Required:

- target venue and year;
- working title or one-paragraph project summary;
- paper type: method, benchmark, system, theory, application, clinical study, challenge paper, survey, or extension;
- main contributions;
- available evidence: experiments, figures, tables, theorems, user/reader studies, clinical validation, or ablations;
- known related work and direct competitors.

Optional:

- draft abstract or introduction;
- target page limit;
- code/data release plan;
- privacy/IRB constraints for medical papers;
- rejected reviews or prior reviewer comments.

## Procedure

1. Classify the paper type.
   Decide what kind of proof the paper needs. A method paper needs mechanism and experiments; a benchmark paper needs dataset/task validity; a TMI paper needs validation scope and clinical relevance.

2. Extract the central thesis.
   Write one sentence in the form: "This paper shows that <method/idea> enables <outcome> for <task/context>, supported by <main evidence>."

3. Separate contributions from features.
   A contribution is a claim a reviewer can evaluate. A feature is merely something the system does.

4. Build the claim hierarchy.
   Create one central claim, 2-4 supporting claims, and evidence required for each.

5. Identify the reviewer contract.
   State what the paper must prove for a fair reviewer to accept the story.

6. Identify likely attacks.
   List novelty, soundness, baseline, ablation, clarity, reproducibility, ethics, and venue-fit risks.

7. Produce the section plan.
   Map each claim to Introduction, Method, Experiments, Results, Related Work, Limitations, and Appendix.

8. Decide what not to claim.
   Remove or weaken claims whose evidence is missing or unlikely to be added before submission.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Thesis | One clear, testable paper promise | Vague topic description |
| Contributions | 2-4 evaluable claims | Feature list or marketing bullets |
| Evidence plan | Every claim maps to result/citation/derivation | Claims rely on intuition |
| Reviewer fit | Anticipates venue-specific objections | Ignores target venue norms |
| Scope | Honest limits and assumptions | Overclaims beyond evidence |

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize conceptual contribution, rigorous ablations, reproducibility, and limitation clarity.
- CVPR/ECCV: emphasize visual evidence, dataset coverage, baselines, qualitative/quantitative alignment, and figure-driven storytelling.
- AAAI: keep claims broadly AI-relevant and comply with the official AI-generated-text policy.
- TMI: make clinical/medical-imaging relevance, validation protocol, patient/privacy context, and generalization scope explicit.
- arXiv: prepare a public-facing version; do not preserve anonymous-review wording by accident.

## Output Contract

Return:

```text
One-sentence thesis:
Paper type:
Target venue fit:
Contribution map:
Claim-evidence requirements:
Section plan:
Figure/table plan:
Likely reviewer objections:
Claims to weaken or remove:
Next actions:
```

## Common Failure Modes

- Treating "we propose a framework" as a contribution without saying what it proves.
- Hiding the most important result until late in the paper.
- Claiming novelty before checking recent target-venue papers.
- Planning an experiments section that does not answer the introduction's promises.
- Using clinical language in a TMI paper without validation that supports clinical scope.

## Mini Example

Weak contribution:

```text
We propose a new diffusion framework for medical image segmentation.
```

Stronger contribution:

```text
We show that uncertainty-aware diffusion sampling improves ambiguous lesion boundary segmentation on two annotated MRI datasets, with gains in Dice and calibration over deterministic baselines.
```

Why stronger: it names the mechanism, task, evidence type, and comparison target.

## Sources Reviewed

This skill is an original synthesis inspired by repository-level research notes in `docs/writing-skills-research.md`, especially strategist/composer workflows, reviewer simulation patterns, claim-evidence auditing, and venue-aware section routing.
