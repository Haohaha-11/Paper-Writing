# Research Scout

## Purpose

Build a field map from recent and classic papers before proposing or locking a paper idea.

## When To Use

Use this skill at the beginning of a project, when the author has a broad topic, keyword set, dataset, domain problem, or preliminary observation but has not yet locked the research question.

## Inputs

- Topic keywords and target domain.
- Target venue family if known.
- Seed papers, if available.
- User assets: datasets, compute, models, collaborators, evaluation access.
- Time window for recent papers and list of classic papers to inspect.

## Procedure

1. Split the area into research threads, not model families only.
2. Collect classic papers that define the problem, default assumptions, metrics, and evaluation workflow.
3. Collect recent papers that represent the current frontier.
4. For each paper, extract:
   - problem addressed;
   - default belief or assumption;
   - diagnostic observation;
   - method idea;
   - evidence type;
   - unresolved boundary.
5. Build a frontier problem map.
6. Mark crowded directions, under-tested assumptions, contradictory findings, missing diagnostics, and evaluation weaknesses.
7. Produce candidate problem seeds for `research-problem-framer`.

## Rubric

- The output distinguishes classic foundations from recent frontier work.
- The map is organized by problem and assumption, not by architecture names alone.
- Every candidate problem is traceable to at least one source or observation.
- The output identifies what is already solved, what is crowded, and what remains unresolved.
- The output avoids inventing citations, paper claims, or benchmark results.

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize assumptions, mechanisms, diagnostics, and generalization across tasks.
- CVPR/ECCV: emphasize visual evidence, dataset bias, benchmark saturation, and failure modes.
- AAAI: emphasize broad AI relevance, reasoning, interaction, society-facing constraints, or general task framing.
- IEEE TMI: emphasize clinical validity, multi-site robustness, privacy, and external validation.
- arXiv: preserve unresolved questions and source trail for later venue targeting.

## Output Contract

Return:

- search scope and sources checked;
- classic paper list;
- recent paper list;
- frontier problem map;
- crowded direction list;
- unresolved assumption list;
- candidate problem seeds;
- required follow-up searches.

## Common Failure Modes

- Listing architectures without identifying the field belief they challenge.
- Treating newest papers as strongest papers.
- Treating citation count as correctness.
- Generating ideas before mapping the frontier.
- Claiming novelty without checking closest work.

## Mini Example

Weak: "Survey recent MIL methods and propose a new attention model."

Better: "Map whether whole-slide aggregation methods assume one fixed label semantics per task, then inspect whether rare-presence, proportion, and spatial-relation tasks break that assumption differently."

## Sources Reviewed

- Project design notes in `docs/design_v1.md`.
- Project writing research notes in `docs/writing-skills-research.md`.
- Existing `novelty-scout` and `paper-strategist` skills.
