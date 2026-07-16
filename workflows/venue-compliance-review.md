# Venue Compliance Review Workflow

## Goal

Check whether a paper is aligned with the selected venue's official rules before polishing prose.

## Inputs

- Target venue folder under `venues/`.
- Main LaTeX file or compiled PDF.
- Source archive layout if submitting to arXiv or a publisher portal.
- Current venue website or official instructions if the local venue file is stale.

## Steps

1. Read `rules.md`, `rules.yaml`, `checklist.md`, and `sources.md` for the selected venue.
2. Confirm the local rule file's `Last checked` date.
3. If any rule is stale, ambiguous, or high-impact, re-check the official venue source before enforcing it.
4. Inspect page count, file size, anonymity, acknowledgments, author metadata, checklist requirements, supplementary material, and bibliography placement.
5. For LaTeX projects, run `scripts/extract_latex_context.py` and inspect:
   - root files;
   - included files;
   - bibliography files;
   - figure paths;
   - style/class files;
   - appendix markers.
6. For imported templates, verify `templates/checksums.sha256`.
7. If a local TeX environment is available, run `scripts/compile_templates.py --check` to confirm template smoke tests still pass.
8. Record pass/fail/unknown for each rule.

## Output

```markdown
# Venue Compliance Report

Target venue:
Paper type:
Rule files checked:
Official sources rechecked:
LaTeX root:
Compile status:

## Blocking Issues

## Warnings

## Unknowns

## Passed Checks

## Required Author Decisions
```

## Rule

Do not claim compliance when a rule is unknown. Mark it as `unknown` and point to the source that must be checked.
