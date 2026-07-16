# Draft To Submission Workflow

## Goal

Turn a research idea, partial results, or rough draft into a venue-aware submission package without hiding unresolved evidence gaps.

## Inputs

- Filled `examples/paper-context-template.md`.
- Target venue folder under `venues/`.
- Current LaTeX source or section drafts.
- Figure/table inventory.
- Experiment log, dataset notes, and baseline list.

## Steps

1. Lock the target venue and paper type.
2. Run `paper-strategist` to define thesis, contributions, reviewer contract, and section plan.
3. Run `novelty-scout` before using strong novelty, first, or state-of-the-art claims.
4. Draft or revise sections in this order:
   - `abstract-writer`
   - `introduction-writer`
   - `related-work-writer`
   - `method-writer`
   - `experiments-writer`
   - `results-writer`
   - `discussion-writer`
   - `limitations-ethics-writer`
   - `conclusion-writer`
   - `appendix-writer`
5. Run `figure-caption-writer` on all figures and tables.
6. Run `claim-evidence-auditor` on the abstract, introduction, method claims, and result claims.
7. Run `venue-compliance-review.md`.
8. Run `paper-redteam` for reviewer simulation and AC-style risk synthesis.
9. Run `revision-editor` to convert audit findings into a prioritized edit list.
10. Run `page-compressor` only after evidence and venue risks are resolved.
11. Compile the LaTeX source and inspect the generated PDF.

## Output

- Submission readiness report.
- Claim-evidence matrix.
- Venue compliance checklist.
- Redteam review report.
- Prioritized revision list.
- Final compile status.

## Stop Conditions

Stop and ask for author input when:

- a main result is missing, contradicted, or not reproducible;
- a citation is needed for a factual claim but no source is available;
- a venue rule is unclear or has changed since the local source file was last checked;
- the paper would need fabricated numbers, datasets, or experiments to proceed.
