# Novelty Scout

## Purpose

Find novelty risks, missing related work, missing baselines, and role-model papers before the paper makes strong claims. This skill uses search as evidence for review; it does not decide acceptance and does not prove full-paper novelty by itself.

## When To Use

- Before writing Abstract or Introduction novelty claims.
- Before Related Work finalization.
- Before paper-redteam review.
- When reviewers complain that related work is missing.

## Inputs

Required:

- target venue and adjacent venues;
- year range;
- working title;
- abstract or project summary;
- contribution bullets;
- method keywords;
- task/dataset/baseline names.

Optional:

- current BibTeX;
- must-cite papers;
- user-provided PDFs;
- known direct competitors.

## Primary Source

Use `cspapers.org` for title/abstract-level CS conference search when the target area is covered. See:

- `docs/cspapers-integration.md`
- `workflows/cspapers-assisted-review.md`
- `skills/novelty-scout/query-guide.md`
- `examples/cspapers-hit-classification-template.md`

## Procedure

1. Generate query families.
   Use exact title, method+task, dataset+task, central abstract claim, baseline+task, technical phrase, acronym, and acronym expansion.

2. Select venue groups.
   Use target and adjacent venues. For ML/CV, search CVPR, ICCV, ECCV, ICLR, ICML, and NeurIPS by default.

3. Retrieve top hits.
   Record title, venue, year, score, index, and abstract when available.

4. Classify hits.
   Use: direct overlap, same task, same method, same dataset, missing baseline, related work, role model, irrelevant.

5. Compare against bibliography.
   Mark cited, missing, unknown, or not needed.

6. Translate into writing constraints.
   Recommend claim weakening, citation addition, baseline addition, or full-paper inspection.

7. Feed high-risk findings into `paper-redteam`.

## Rubric

| Hit Class | Meaning | Action |
|---|---|---|
| Direct overlap | Same problem and similar method/claim by title/abstract | Inspect full paper; cite/contrast; weaken novelty |
| Same task | Same task/benchmark with different method | Consider baseline or related work |
| Same method | Similar technique in different task | Clarify methodological novelty |
| Same dataset | Uses central dataset/benchmark | Check evaluation comparability |
| Missing baseline | Likely should be compared in experiments | Add baseline or justify omission |
| Related work | Contextual but not direct competitor | Cite if relevant |
| Role model | Strong venue paper to emulate | Use for structure/style only |

## Output Contract

Return:

```text
Search scope:
Query log:
Top retrieved papers:
Hit classification table:
Missing related work:
Missing baseline candidates:
Novelty risks:
Claim wording changes:
Full-paper inspection needed:
Sources checked:
```

## Venue Adaptation

- ICLR/NeurIPS/ICML: search concept/method/task terms and adjacent ML papers.
- CVPR/ECCV: search dataset/task/method and recent visual benchmark papers.
- AAAI: search broad AI venues and task communities.
- TMI: cspapers coverage is incomplete for medical journals; supplement with PubMed, IEEE Xplore, Semantic Scholar, and TMI-specific sources.
- arXiv: treat preprint overlap as important but distinguish venue-reviewed papers.

## Limits

- cspapers indexes titles and abstracts, not full papers.
- Search score is retrieval priority, not academic review score.
- Do not claim plagiarism, duplicate submission, or full overlap without full-paper inspection.
- Do not add citations unless the cited work was actually checked.

## Mini Example

Finding:

```text
Query "diffusion model medical image segmentation" retrieves a CVPR 2023 paper titled "Ambiguous Medical Image Segmentation Using Diffusion Models".
```

Writing implication:

```text
Do not claim "first diffusion model for medical image segmentation" unless full-paper inspection supports a narrower claim. Related Work should cite or distinguish the CVPR 2023 paper, and Experiments should explain task/dataset/method differences.
```

## Sources Reviewed

Original synthesis based on cspapers.org public API behavior, project cspapers integration notes, and related-work/reviewer workflows.
