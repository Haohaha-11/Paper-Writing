# Quickstart

Use this repo as a paper-writing operating manual.

## 1. If You Need An Idea

1. Fill `examples/research-query-tree-template.md`.
2. Fill `examples/frontier-problem-map-template.md`.
3. Fill `examples/idea-bank-template.md`.
4. Fill `examples/research-problem-framing-template.md`.
5. Fill `examples/falsification-sprint-template.md`.
6. Fill `examples/pre-experiment-ledger-template.md`.
7. Follow `workflows/idea-to-paper.md`.

## 2. If The Problem Is Locked

1. Fill `examples/paper-context-template.md`.
2. Read the target venue folder under `venues/`.
3. Follow `workflows/draft-to-submission.md`.
4. Use `skills/paper-strategist/SKILL.md`.
5. Use `skills/novelty-scout/SKILL.md` before strong novelty claims.
6. Use `skills/claim-evidence-auditor/SKILL.md` before finalizing the abstract and introduction.
7. Use `skills/paper-redteam/SKILL.md` before submission.

## 3. If You Already Have A Draft

1. Fill any missing context in `examples/paper-context-template.md`.
2. Select the target venue checklist.
3. Run `workflows/review-existing-draft.md`.
4. Apply section-specific skills from `skills/`.
5. Record unresolved risks in the review report.

## 4. Local Private Projects

1. Put real unpublished paper projects under `projects/<paper-name>/`.
2. Keep `projects/` contents local; this repository ignores real project files by default.
3. Run `scripts/extract_latex_context.py projects/<paper-name>` before asking an agent to inspect a LaTeX draft.
4. Compile locally with `latexmk -pdf main.tex` inside the project directory.
5. The PDF appears next to your main `.tex` file unless you change the output path.

## 5. Rebuttal

1. Paste reviews into `examples/rebuttal-response-template.md`.
2. Use `skills/rebuttal-planner/SKILL.md`.
3. Separate evidence-backed responses from wording-only clarifications.
4. Track paper changes required for camera-ready.
