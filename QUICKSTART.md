# Quickstart

Use this repo as a paper-writing operating manual.

## New Paper

1. Fill `examples/paper-context-template.md`.
2. Read the target venue folder under `venues/`.
3. If the problem is still open, run `workflows/idea-to-paper.md`.
4. If the problem is locked, run `workflows/draft-to-submission.md`.
5. Use `skills/paper-strategist/SKILL.md`.
6. Use `skills/novelty-scout/SKILL.md` before strong novelty claims.
7. Use `skills/claim-evidence-auditor/SKILL.md` before abstract/introduction finalization.
8. Use `skills/paper-redteam/SKILL.md` before submission.

## Idea Development

1. Fill `examples/frontier-problem-map-template.md` while running `skills/research-scout/SKILL.md`.
2. Fill `examples/research-problem-framing-template.md` while running `skills/research-problem-framer/SKILL.md`.
3. Fill `examples/falsification-sprint-template.md` while running `skills/pre-experiment-planner/SKILL.md`.
4. Continue to `workflows/draft-to-submission.md` only after the problem survives falsification.

## Existing Draft

1. Fill any missing context in `examples/paper-context-template.md`.
2. Select the target venue checklist.
3. Run `workflows/review-existing-draft.md`.
4. Apply section-specific skills from `skills/`.
5. Record unresolved risks in the review report.

## Local Private Projects

1. Put real unpublished paper projects under `projects/<paper-name>/`.
2. Keep `projects/` contents local; this repository ignores real project files by default.
3. Copy `examples/paper-context-template.md` into the local project.
4. Run `scripts/extract_latex_context.py projects/<paper-name>` before asking an agent to inspect a LaTeX draft.
5. Move only synthetic, sanitized examples into `examples/` for public sharing.

## Rebuttal

1. Paste reviews into `examples/rebuttal-response-template.md`.
2. Use `skills/rebuttal-planner/SKILL.md`.
3. Separate evidence-backed responses from wording-only clarifications.
4. Track paper changes required for camera-ready.
