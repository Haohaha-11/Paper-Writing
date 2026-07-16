# Review Existing Draft Workflow

## Goal

Review a complete or near-complete paper as if it were a venue submission, then produce concrete revision actions.

## Inputs

- Main LaTeX root or PDF.
- Target venue and year.
- Filled or partial paper context.
- Figures, tables, appendix, and bibliography.

## Steps

1. Identify the draft root, target venue, paper type, and blind-review state.
2. If the draft is LaTeX, run `scripts/extract_latex_context.py` to collect roots, included files, figures, bibliographies, style files, and appendix markers.
3. Run `venue-compliance-review.md` before judging content quality.
4. Run `claim-evidence-auditor` on the full paper.
5. Run `novelty-scout` for missing related work and overstated positioning.
6. Run `paper-redteam` for reviewer simulation.
7. Apply section-specific skills only where the audit found meaningful risk.
8. Run `revision-editor` to convert all findings into a ranked patch plan.
9. Run `page-compressor` if the paper exceeds venue limits.

## Output

Use `examples/review-report-template.md` and include:

- scope reviewed;
- venue rule assumptions;
- blocking issues;
- likely reviewer concerns;
- claim-evidence failures;
- citation and novelty risks;
- section-level edit plan;
- residual author decisions.

## Review Standard

The workflow should not grade style in isolation. Treat writing quality as submission risk only when it affects clarity, evidence, positioning, reproducibility, venue compliance, or reviewer trust.
