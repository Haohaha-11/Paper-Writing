# cspapers.org Integration

Last checked: 2026-07-15

This note evaluates whether `swkim101/cspapers.org` can be used as a paper-review rule source for `Paper-Writing-Hao`.

## Finding

The public repository does not expose a full-paper reviewer or review rubric.

What is public:

- a CS conference paper search engine;
- a public HTTP API;
- title and abstract indexing;
- venue/year filters;
- relevance score from the Bleve search backend;
- abstract retrieval from the repository's raw indexed files.

What is not public in the repository:

- PDF upload or full-text ingestion;
- LLM reviewer prompts;
- review/rubric/scoring rules;
- novelty-decision thresholds;
- acceptance/rejection classifier;
- full-paper critique endpoint.

If there is a separate online feature that reviews full papers, it is not visible in the public `swkim101/cspapers.org` repository checked here.

## Public API Shape

The README documents this query shape:

```text
https://api.cspapers.org/?query=<query>&yearFrom=<year>&yearTo=<year>&venue=<venues>&orderBy=score&ascending=false&skip=0
```

The server accepts:

- `query`
- `must`
- `orderBy`
- `ascending`
- `venue`
- `yearFrom`
- `yearTo`
- `skip`

The response units contain:

- `title`
- `year`
- `venue`
- `index`
- `score`

The frontend retrieves abstracts from:

```text
https://raw.githubusercontent.com/swkim101/cspapers.org/main/{index}
```

## How To Use It In Our Review Process

Use cspapers as a retrieval backend, not as the reviewer itself.

Operational workflow: `workflows/cspapers-assisted-review.md`.

Hit classification template: `examples/cspapers-hit-classification-template.md`.

### `novelty-scout`

Inputs:

- paper title;
- abstract;
- contribution bullets;
- method keywords;
- dataset/task names;
- target venue;
- target year range.

Process:

1. Build multiple queries:
   - exact title phrase;
   - method + task;
   - dataset + task;
   - contribution keywords;
   - baseline names;
   - core claim sentence from abstract/introduction.
2. Search target venue and adjacent venues:
   - CV/ML: CVPR, ICCV, ECCV, ICLR, ICML, NeurIPS.
   - NLP: ACL, EMNLP, NAACL, ICLR, ICML, NeurIPS.
   - Systems/security: venue group from cspapers conference tree.
3. Retrieve titles and abstracts for top results.
4. Classify each hit:
   - direct overlap;
   - same task, different method;
   - same method, different task;
   - same dataset/benchmark;
   - missing baseline;
   - related-work candidate;
   - role-model paper.
5. Produce a review note:
   - novelty risks;
   - missing citations;
   - missing baselines;
   - stronger positioning language;
   - papers to cite or contrast against.

### `related-work-auditor`

Rules:

- If cspapers finds high-relevance target-venue papers not cited by the draft, flag them.
- If a draft claims "first", "novel", "new", "state-of-the-art", or "unexplored", run a targeted search and require evidence.
- If related work cites only old papers while recent target-venue hits exist, flag recency risk.
- If a benchmark/dataset appears in searched papers but not in the experiment section, flag possible missing baseline/evaluation.

### `paper-redteam` Integration

Use cspapers output as evidence for reviewer objections:

- "Novelty may be incremental because similar title/abstract-level work exists."
- "Related work misses recent papers from the target venue."
- "The claimed task/method combination appears in adjacent venues."
- "The paper should explain why these retrieved papers are not direct competitors."

The reviewer must not claim full-text overlap unless the full papers are separately retrieved and inspected.

## Why Not Use It Directly As Rules

cspapers' public `score` is a search relevance score, not an academic review score. It should not be converted directly into accept/reject judgments.

Recommended rule:

```text
cspapers score => retrieval priority
LLM/human rubric => review judgment
draft claims + retrieved abstracts => evidence for novelty/related-work critique
```

## Implementation Notes

- Use a normal browser-like `User-Agent`; the API may reject default script user agents.
- Cache responses by query and retrieval date.
- Store cspapers source provenance in the review report.
- Keep Semantic Scholar citation/data attribution because cspapers data comes from Semantic Scholar.
- Treat title/abstract-level evidence as preliminary until full papers are checked.

## Sources

- cspapers.org repo: https://github.com/swkim101/cspapers.org
- cspapers.org site: https://cspapers.org
- API documented in README: https://github.com/swkim101/cspapers.org#tips
- Server request/response types: https://github.com/swkim101/cspapers.org/blob/main/api.cspapers.org/types/types.go
- Server API handler: https://github.com/swkim101/cspapers.org/blob/main/api.cspapers.org/server/server.go
- Search backend: https://github.com/swkim101/cspapers.org/blob/main/api.cspapers.org/db/bleve/bleve.go
