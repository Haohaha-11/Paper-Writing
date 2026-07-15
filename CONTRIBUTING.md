# Contributing

Thanks for helping improve Paper-Writing-Hao. This project is a document-first paper-writing knowledge base, so most contributions are Markdown, YAML, templates, examples, or provenance records.

## What To Contribute

Good contributions include:

- new or corrected venue rules backed by official sources;
- stronger writing/review skills with clear output contracts;
- synthetic examples that do not reveal unpublished work;
- template provenance, checksums, and compile validation records;
- workflows for specific paper types such as benchmark papers, clinical studies, system papers, or surveys;
- corrections to licensing, attribution, or redistribution notes.

## Ground Rules

- Do not submit confidential drafts, private reviews, unpublished results, or private datasets.
- Do not invent venue rules. Cite official venue or publisher sources.
- Do not invent citations, metrics, datasets, or experimental results.
- Do not copy third-party prompt text unless the license and provenance are clear.
- Do not add "AI humanizer" or detector-evasion workflows.
- Keep generated examples synthetic.

## Adding A Skill

Place new skills under:

```text
skills/<skill-id>/SKILL.md
```

Use the existing skills as the expected format:

- Purpose
- When To Use
- Inputs
- Procedure
- Rubric
- Venue Adaptation
- Output Contract
- Common Failure Modes
- Mini Example
- Sources Reviewed

If a skill changes citations, claims, or venue compliance, it must include stricter source and evidence rules.

## Adding Venue Rules

Use:

```text
venues/<venue>/<year-or-rolling>/
  rules.md
  rules.yaml
  checklist.md
  sources.md
```

Rules must be backed by official sources. If a rule is inferred or uncertain, mark it explicitly.

## Adding Templates

Before committing template files:

1. Confirm the source is official.
2. Record URL, retrieval date, commit/release/artifact URL.
3. Record sha256 checksums.
4. Record license or redistribution status.
5. Add an import record under `templates/import-records/`.
6. Update `templates/import-log.md`.
7. Compile from a temporary copy and update `templates/compile-validation.md`.

If redistribution terms are unclear, prefer linking to the official source instead of copying files.

## Pull Request Checklist

- [ ] No confidential or unpublished user data included.
- [ ] Official sources cited for venue/template changes.
- [ ] Third-party licenses respected.
- [ ] Examples are synthetic.
- [ ] Markdown links and paths checked.
- [ ] `templates/checksums.sha256` updated if template files changed.
- [ ] `IMPLEMENTATION_STATUS.md` updated if project status changed.
