# Skill Spec

Last checked: 2026-07-15

This spec is distilled from K-Dense Scientific Agent Skills and the AI Tutor skill library, but it is intentionally narrower: every skill must directly support paper writing, review, revision, venue compliance, evidence checking, or LaTeX safety.

## Directory Shape

```text
skills/<skill-id>/
├── SKILL.md
├── checklist.md
├── output-format.md
└── examples.md
```

Only `SKILL.md` is required. Extra folders are loaded lazily.

## Required Frontmatter

```yaml
---
id: introduction-writing
name: Introduction Writing
version: "0.1.0"
category: section
description: Improve or draft ML paper introductions.
triggers:
  sections: [introduction]
  tasks: [draft, rewrite, review]
inputs:
  required: [paper_context, section_text, target_venue]
outputs:
  type: patch_or_report
allowed_operations: [read, suggest_patch]
dependencies: [academic-writing, contribution-positioning]
license: MIT
sources:
  - title: Internal distillation notes
    url: docs/distillation/
---
```

## Required Body Sections

Each `SKILL.md` should contain:

- Overview
- When To Use
- Inputs
- Output Contract
- Procedure
- Quality Checks
- Failure Modes
- Examples
- References

## Output Contracts

Skills must declare one output type:

- `report`: no source changes.
- `patch`: unified diff or structured patch.
- `patch_or_report`: workflow decides.
- `artifact`: exported file, zip, PDF, or registry entry.

Patch-producing skills must never require direct overwrite as the only path.

## Safety Fields

Every skill must state:

- Whether it may run shell commands.
- Whether it may access network.
- Whether it may add citations.
- Whether it may modify LaTeX source.
- Whether it may modify templates.

Citation-changing skills need stricter contracts: they may only add citations backed by a verified source and must report provenance.

## v0.1 Skill Set

Start with:

- `paper-strategist`
- `abstract-writer`
- `introduction-writer`
- `related-work-writer`
- `claim-evidence-auditor`
- `paper-redteam`
- `novelty-scout`
- `page-compressor`
- `rebuttal-planner`

## Validation

Future validation scripts should check:

- Valid YAML frontmatter.
- Required fields.
- Unique `id`.
- Semantic version string.
- Existing dependency IDs.
- Valid output type.
- Declared license.
- No prohibited broad permissions by default.
- Test fixture presence for v0.1 built-in skills.
