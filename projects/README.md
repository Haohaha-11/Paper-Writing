# Local Paper Projects

This directory is reserved for real paper projects that use Paper-Writing-Hao as a local writing and review workspace.

## Default Rule

Real paper projects placed here are ignored by Git by default.

Keep this public repository as the reusable writing system. Keep unpublished manuscripts, experiment outputs, private reviews, author identities, clinical details, and confidential data artifacts local or in a private repository.

## Suggested Layout

```text
projects/
  my-iclr-paper/
    paper-context.md
    main.tex
    sections/
    figures/
    refs.bib
    reviews/
  my-tmi-paper/
    paper-context.md
    manuscript.tex
    experiments/
    figures/
```

## How To Use

1. Create a local project directory under `projects/`.
2. Copy or adapt `examples/paper-context-template.md`.
3. Select the target venue under `venues/`.
4. Run `workflows/draft-to-submission.md` for a new paper or `workflows/review-existing-draft.md` for an existing draft.
5. Use `scripts/extract_latex_context.py projects/<paper-name>` before asking an agent to review or edit a LaTeX project.
6. Keep generated reports inside the local project unless they are synthetic or intentionally public.

## Do Not Commit

- unpublished manuscripts;
- real experimental results or private benchmark tables;
- non-public datasets, paths, credentials, or IRB/ethics details;
- reviewer comments, rebuttals, or editorial decisions;
- author-identifying metadata for anonymous submissions;
- private collaborator notes;
- PDFs or source archives prepared for confidential submission.

## Public Examples

If you want to share a workflow example, create a synthetic version under `examples/` instead of committing a real paper project.
