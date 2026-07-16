# Idea To Paper Workflow

## Goal

Move from a broad research direction to a defensible paper plan through literature mapping, problem focusing, falsification, method design, experiments, and writing.

## Stages

1. Research latest and classic papers.
2. Focus the research problem.
3. Run pre-experiments.
4. Design the method.
5. Run main and supplementary experiments.
6. Write and revise the paper.

## Inputs

- Broad topic, domain, or preliminary observation.
- Target venue family if known.
- User assets: data, models, compute, collaborators, clinical/domain access, annotation budget.
- Seed papers or keywords.
- Constraints: timeline, page target, anonymity, private data boundaries.

## Stage 1: Latest And Classic Papers

Run `research-scout` and fill `examples/research-query-tree-template.md` plus `examples/frontier-problem-map-template.md`.

Outputs:

- classic paper list;
- recent frontier paper list;
- frontier problem map;
- unresolved assumptions;
- candidate problem seeds.

Do not generate final paper ideas before this map exists.

## Stage 2: Focus The Problem

Run `research-problem-framer` and fill `examples/idea-bank-template.md` plus `examples/research-problem-framing-template.md`.

Required outputs:

- scored candidate table;
- candidate comparison;
- one-line contradiction;
- full problem statement;
- novelty boundary;
- non-claim;
- falsification sprint;
- reviewer attack map.

Decision rule:

- lock a candidate only if no critical dimension is below 2;
- require a 3 in violated assumption, falsifiability, or novelty boundary;
- revise or kill solution-shaped ideas that lack a measured failure.

## Stage 3: Pre-Experiments

Run `pre-experiment-planner`, fill `examples/falsification-sprint-template.md`, and maintain `examples/pre-experiment-ledger-template.md`; then execute the sprint outside this repository.

Each pre-experiment must answer at least one of:

- Does the phenomenon exist?
- Is it robust across meaningful conditions?
- Is the proposed mechanism better than the strongest alternative?
- Does the failure have the claimed consequence?
- Can a simple baseline remove it?

Stop if the kill condition is met. Revise the problem instead of forcing a method.

## Stage 4: Method Design

Run `paper-strategist` and `method-writer`.

The method must be derived from the diagnosed failure:

- every component maps to a failure, mechanism, or control;
- the method does not become the starting point of the story;
- alternatives remain explicit until experiments separate them.

## Stage 5: Main And Supplementary Experiments

Run `experiments-writer` and `results-writer`.

Main experiments should establish:

- the phenomenon matters;
- the proposed method addresses the diagnosed failure;
- strong baselines do not remove the problem;
- results are robust across meaningful regimes.

Supplementary experiments should cover:

- ablations;
- sensitivity;
- negative cases;
- extra baselines;
- implementation details;
- additional visualizations or proofs.

## Stage 6: Paper Writing

Run `draft-to-submission.md`.

Recommended skill order:

1. `abstract-writer`
2. `introduction-writer`
3. `related-work-writer`
4. `method-writer`
5. `experiments-writer`
6. `results-writer`
7. `discussion-writer`
8. `limitations-ethics-writer`
9. `conclusion-writer`
10. `appendix-writer`
11. `figure-caption-writer`
12. `claim-evidence-auditor`
13. `paper-redteam`
14. `revision-editor`
15. `page-compressor`

## Output

- literature map;
- locked problem statement;
- novelty boundary and non-claim;
- falsification sprint report;
- method-design rationale;
- main/supplementary experiment plan;
- paper strategy;
- draft-to-submission checklist.

## Stop Conditions

Stop before method design when:

- the closest paper already establishes the core claim;
- the phenomenon disappears under a simple control;
- the decisive test is not feasible with available assets;
- the problem has no consequence beyond a local metric;
- the mechanism cannot be separated from obvious alternatives.
