# Pre-Experiment Planner

## Purpose

Design small falsification experiments that decide whether a research problem is real before committing to full method development.

## When To Use

Use this skill after `research-problem-framer` locks or revises a candidate problem, and before building the full method or running expensive main experiments.

## Inputs

- Problem statement and non-claim.
- Falsification sprint template.
- Available datasets, models, baselines, metrics, compute, and annotation resources.
- Known confounders and reviewer attacks.

## Procedure

1. Identify the minimum observation needed to show the phenomenon exists.
2. Isolate one variable per test.
3. Add controls for trivial explanations, leakage, dataset identity, tuning, parameter count, and label prevalence when relevant.
4. Define the result that supports the problem and the result that kills it.
5. Define stopping rules before running the tests.
6. Record every run in `examples/pre-experiment-ledger-template.md`.
7. Map positive outcomes to method-design requirements.
8. Map negative outcomes to revise/kill decisions.
9. Reflect on what each result supports and what it does not support before moving to method design.

## Rubric

- Each test has a kill condition.
- Each test isolates a variable.
- Controls target the strongest alternative explanation.
- The sprint is cheaper than full method development.
- Positive results directly affect method design.

## Venue Adaptation

- ICLR/NeurIPS/ICML: include mechanism diagnostics and simple baselines.
- CVPR/ECCV: include visual checks and cross-dataset or cross-condition validation when feasible.
- AAAI: include task framing and broader consequence checks.
- IEEE TMI: include site, scanner, privacy, label quality, and clinical-scope controls.
- arXiv: record both positive and negative results for transparent iteration.

## Output Contract

Return:

- pre-experiment table;
- required assets;
- expected runtime/cost;
- success and kill criteria;
- controls and matched baselines;
- decision tree after results;
- experiment ledger;
- reflection table;
- risks that remain for main experiments.

## Common Failure Modes

- Designing a mini version of the full paper instead of a decisive diagnostic.
- Running experiments without a kill condition.
- Measuring only accuracy when the problem concerns mechanism, calibration, robustness, privacy, or workflow.
- Ignoring simple baselines that could remove the phenomenon.

## Mini Example

Problem: fixed slide embeddings may discard task-specific set semantics.

Pre-experiment: compare one fixed aggregator against task-family-specific oracle aggregators on rare-presence, proportion, and spatial-relation labels with matched encoders and identical training budgets. Kill the problem if the fixed aggregator dominates or if task conditioning only changes the threshold.

## Sources Reviewed

- User-provided falsification sprint template.
- Existing experiment and result-writing skills in `skills/`.
