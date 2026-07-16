# Research Problem Framer

## Purpose

Evaluate and sharpen candidate research problems before method design, using a falsifiable problem-first rubric rather than a solution-first idea list.

## When To Use

Use this skill after an initial literature scan and before investing in method design or full experiments. It is especially useful when there are several possible ideas and the project needs to decide which problem to lock, revise, or kill.

## Inputs

- Frontier problem map from `research-scout`.
- Candidate problem list.
- Closest papers and preliminary observations.
- User assets and constraints.
- Possible decisive tests or pre-experiments.

## Procedure

1. Convert each candidate into a one-line contradiction.
2. Score each candidate from 0 to 3 on all rubric dimensions.
3. Reject or revise candidates with any critical dimension below 2.
4. Require at least one score of 3 in violated assumption, falsifiability, or novelty boundary before recommending a primary direction.
5. Build an idea bank using `examples/idea-bank-template.md`.
6. Build a candidate comparison table.
7. Write the problem statement, novelty boundary, and non-claim for the best candidate.
8. Design a falsification sprint before method design.
9. Apply provenance gates: unchecked observations cannot become paper claims.
10. Run multi-perspective critique from closest-work, feasibility, mechanism, reviewer-attack, venue-fit, and domain/ethics perspectives.
11. Anticipate reviewer attacks and map each one to a control, baseline, or wording boundary.

## Candidate Scoring Rubric

Score each dimension from 0 to 3.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Violated assumption | No assumption | Minor practice | Recognizable default | Central field belief |
| Surprise | Expected | Mildly interesting | Non-obvious | Strong reversal or paradox |
| Falsifiability | No direct test | Expensive/ambiguous | Feasible test | Simple decisive diagnostic |
| Consequence | Local metric | One model/task | Several settings | Changes evaluation or workflow |
| Novelty boundary | Already solved | Crowded/incremental | Clear residual gap | Distinct unresolved question |
| Mechanism | Pure speculation | Generic story | Testable explanation | Competing mechanisms separable |
| Breadth | Single run | Single dataset | Multiple conditions | Stable across meaningful regimes |
| Resource fit | Infeasible | Major missing assets | Feasible | Unusually enabled by user assets |

Treat a candidate as strong only if no critical dimension is below 2. Require a 3 in violated assumption, falsifiability, or novelty boundary before recommending it as the primary direction.

## Frontier Problem Map

Use this table instead of an architecture summary:

| Work | Default belief challenged | Diagnostic observation | Proposed mechanism | Consequence | Residual boundary |
|---|---|---|---|---|---|
| Paper A |  |  |  |  |  |
| Paper B |  |  |  |  |  |

## Candidate Comparison

| Candidate | Contradiction | Closest work | Decisive test | Main risk | Decision |
|---|---|---|---|---|---|
| Candidate 1 |  |  |  |  | Lock/revise/kill |

Do not rank candidates by novelty alone. Prefer a slightly less novel candidate with a decisive experiment and major consequence over an exotic but untestable idea.

## Problem Statement Template

### One-line contradiction

The field expects A, yet under C, B occurs.

### Full statement

Current work assumes A because reason. However, source or preliminary observation shows B under C. If reproducible, this means consequence D. We hypothesize M, while alternatives M2/M3 remain possible. The research question is Q.

### Novelty boundary

Closest paper establishes:

It does not establish:

This project must demonstrate:

### Non-claim

State what the project is not claiming. This prevents novelty inflation and keeps the scope defensible.

## Falsification Sprint Template

| Test | Variable isolated | Positive result | Result that kills the problem | Control |
|---|---|---|---|---|
| Test 1 |  |  |  |  |
| Test 2 |  |  |  |  |

Include one test for each of these questions:

- Does the phenomenon exist?
- Is it robust across meaningful conditions?
- Is the proposed mechanism better than the strongest alternative?
- Does the failure have the claimed consequence?
- Can a simple baseline remove it?

## Worked Example

### Weak formulation

Existing whole-slide MIL methods do not adaptively select task-specific key instances.

Why it is weak:

- It is solution-shaped.
- "Task-specific" and "key instances" are generic.
- It does not identify a violated belief or measured failure.
- Many attention, prompt, and retrieval papers can claim to address it.

### Stronger formulation

Patch encoders are increasingly treated as general-purpose models, yet whole-slide aggregators are still retrained for every label, and task-agnostic slide compression occurs before the model knows whether the task depends on rare presence, phenotype proportions, or spatial relations. Can a model infer the diagnostic aggregation rule from a few labeled slides and condition what it preserves without updating its weights?

Problem ladder:

- Observation: Different pathology tasks reward different aggregation families; generic in-context MIL has only limited full-scale pathology evidence.
- Contradiction: General-purpose patch representations have not produced general-purpose diagnostic aggregation.
- Mechanism hypothesis: Task-agnostic compression discards information needed by label functions with different set semantics.
- Consequence: Every new task still requires training, and fixed slide embeddings may be insufficient for some labels.
- Question: Can few labeled slides specify the aggregation rule before compression?
- Falsifier: If one fixed aggregator dominates across task families, task-conditioned compression retains no more information, or context changes only the decision threshold, reject the problem.

This is strong because the method is not the starting point. The observed aggregation-rule shift and compression loss must be established first.

## Common Reviewer Attacks

Anticipate these before locking a problem:

- "This is only an application of an existing method." Define the domain-specific unresolved barrier.
- "The phenomenon is caused by parameter count or tuning." Use matched baselines.
- "The model uses dataset identity, site, or label prevalence." Use balanced and cross-environment controls.
- "The claimed capability is inferred from accuracy only." Add direct interventions and property-specific metrics.
- "The problem appears on one benchmark." Replicate across meaningful regimes.
- "The explanation is post hoc." Separate observed failure from mechanism and test alternatives.
- "The proposed solution contains unnecessary modules." Tie every component to a diagnosed failure.

## Rubric

- Candidate scores are explicit and justified.
- The primary direction has no critical score below 2.
- The problem is framed as a contradiction or violated assumption, not as a proposed architecture.
- The falsification sprint can kill the problem before large-scale experiments.
- Reviewer attacks are answered with controls, baselines, or non-claims.

## Venue Adaptation

- ICLR/NeurIPS/ICML: prioritize violated assumptions, decisive diagnostics, and mechanism alternatives.
- CVPR/ECCV: require visual or dataset-level evidence that the problem exists beyond one benchmark.
- AAAI: connect the problem to a broader AI capability, evaluation weakness, or human-facing consequence.
- IEEE TMI: require clinical relevance, multi-site controls, privacy boundaries, and external validation planning.
- arXiv: preserve the full candidate comparison and falsification outcomes for transparency.

## Output Contract

Return:

- scored candidate table;
- idea bank and decision records;
- frontier problem map;
- candidate comparison table;
- locked/revised/killed decision for each candidate;
- problem statement for the locked candidate;
- novelty boundary and non-claim;
- falsification sprint plan;
- anticipated reviewer attacks and defenses;
- provenance-gated claim list;
- multi-perspective critique summary;
- decision on whether to proceed to method design.

## Sources Reviewed

- User-provided "Research Problem Rubric and Templates" skill content.
- Project `research-scout`, `novelty-scout`, and `paper-strategist` workflow patterns.
