# Agent Instructions

This repository is a paper-writing knowledge base. Treat it as source-of-truth guidance for writing, reviewing, revising, and preparing research papers.

## Default Behavior

- Read `README.md` first.
- Use `examples/paper-context-template.md` to collect missing facts.
- Select relevant skills from `skills/`.
- Apply venue rules from `venues/`.
- Use workflows from `workflows/`.
- Produce reports and patch suggestions before changing paper text.

## Hard Rules

- Do not invent citations, datasets, metrics, results, theorem statements, or venue rules.
- Do not strengthen a claim unless evidence is present.
- Do not copy third-party prompts or copyrighted text into this repository.
- Do not use "AI humanizer" or detector-evasion workflows.
- Do not overwrite official templates; record provenance instead.
- Do not claim venue compliance unless the relevant official source has been checked.

## Preferred Output

For writing/review tasks, output:

```text
Summary:
Findings:
Evidence gaps:
Recommended changes:
Patch suggestions:
Residual risks:
```

For venue tasks, cite the relevant file under `venues/` and any official source URL listed there.
