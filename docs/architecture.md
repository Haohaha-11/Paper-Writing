# Architecture

Last checked: 2026-07-15

Paper-Writing-Hao should be a venue-aware paper writing knowledge base, not a one-shot paper generator. The v0.1 product is an agent-readable GitHub repository containing skills, venue rules, template provenance, examples, and human-reviewed workflows for writing and revising real papers.

## System Boundaries

The first version should contain four independent subsystems:

1. Skill system: structured writing/review/revision skills with safety constraints and output contracts.
2. Venue/template system: official-source rules, page limits, anonymity rules, checklist expectations, and template provenance.
3. Example/artifact system: paper context, claim-evidence matrix, review report, and rebuttal templates.
4. Workflow system: full-paper writing, section rewrite, internal review, rebuttal, camera-ready, and arXiv release.

These subsystems must not depend on a single agent host. Claude Code, Codex, Cursor, ChatGPT, and future agents should load the same Markdown records.

## Core Data Flow

```text
paper idea or draft
  -> paper context template
  -> venue checklist
  -> skill selection
  -> workflow execution
  -> report / patch suggestion / artifact
  -> human approval
  -> paper revision
```

## Project Context Model

Future LaTeX tooling may build:

- `root_file`: detected by config or `\documentclass`.
- `source_files`: TeX files included by `\input`, `\include`, and root-adjacent TeX files.
- `expanded_text`: merged view with source markers for mapping patches back to files.
- `sections`: title, level, source path, line range, char range, appendix flag.
- `labels`: `\label{}` definitions and references.
- `citations`: citation keys and BibTeX files.
- `assets`: referenced and unreferenced figures/tables.
- `compile_state`: engine, command, logs, warnings, PDF metadata.

The jiarui-liu/overleaf AI Tutor shows a useful pattern: parse sections first, classify section categories second, then route only relevant text to each reviewer. For this project, implement that routing independently and with tests.

## Skill Composition

Skills should be orthogonal and composable:

```text
academic-writing
+ machine-learning-paper
+ introduction-writing
+ contribution-positioning
+ iclr-style
+ concise-revision
```

Avoid venue monoliths. Stable venue style belongs in `venues/<venue>/style.md`; annual, mutable rules belong in `venues/<venue>/<year>/rules.yaml`.

## Revision Model

All revision workflows should default to patch-based output:

- `dry_run`: generate report and patch only.
- `apply`: write only after explicit user approval.
- `history`: store patch metadata for rollback.
- `diff`: show exact changed ranges.

PaperDebugger and AI Tutor both reinforce this rule: suggestions should be anchored to source locations, not dumped as opaque regenerated sections.

## v0.1 Architecture

The minimal version should provide:

- `README.md` as the repo entry point.
- `skills/` as the agent-readable skill library.
- `venues/` as the source-backed venue rules/checklist library.
- `workflows/` as the operating procedures.
- `templates/` as the template provenance registry.
- `examples/` as reusable input/output artifacts.

Tooling, validation scripts, and CLI behavior are v0.2+ candidates, not v0.1 requirements.
