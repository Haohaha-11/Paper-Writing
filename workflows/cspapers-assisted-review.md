# cspapers-Assisted Review Workflow

## Goal

Use cspapers.org as retrieval evidence for novelty, related-work, and baseline review. This workflow does not replace human or LLM review; it supplies evidence.

## Inputs

- Target venue:
- Year range:
- Title:
- Abstract:
- Contributions:
- Method keywords:
- Dataset/task names:
- Baselines:
- Existing bibliography:

## Steps

1. Build query families using `skills/novelty-scout/query-guide.md`.
2. Search target and adjacent venues.
3. Retrieve abstracts for top hits when available.
4. Classify each hit using `examples/cspapers-hit-classification-template.md`.
5. Compare hits against existing bibliography.
6. Create reviewer objections from actual overlaps or missing citations.
7. Feed findings into `paper-redteam`.

## Output

- query log;
- hit classification table;
- missing related-work list;
- missing baseline list;
- novelty-risk claims;
- claim wording changes.

## Rules

- Search relevance is not review score.
- Title/abstract overlap is preliminary.
- Full-paper overlap requires full-paper inspection.
- Do not add citations unless the cited paper was checked.
