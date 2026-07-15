# Repository Distillation Record: K-Dense Scientific Agent Skills

## Basic Information

- Repository: K-Dense-AI/claude-scientific-skills
- URL: https://github.com/K-Dense-AI/claude-scientific-skills
- License: MIT repo-level; individual skills also declare license metadata
- Main language: Markdown and Python
- Last checked: 2026-07-15
- Commit: `fc0b9f692459ea7d9e5a5c64948a5878e1bce274`

## Why It Is Relevant

It is the strongest reference for an agent-compatible skill repository: one directory per skill, `SKILL.md` frontmatter, references/scripts/assets, installation instructions across agent hosts, and security scanning.

## Architecture

- `skills/<skill>/SKILL.md`
- optional `references/`, `scripts/`, `assets/`, `examples/`
- repo-level docs listing skills and usage
- Python security scanner that loads all skills and emits `SECURITY.md`

## Valuable Components

- Agent-readable `SKILL.md` as the primary contract.
- Metadata fields for version, author, license, required env vars, and host compatibility.
- Progressive loading: primary skill file first, references only when needed.
- Security scanning as a first-class workflow.
- Explicit warning that installing every skill increases risk and context cost.

## Components Not Needed

- Broad scientific database/package skills unrelated to writing.
- Network-heavy skills.
- Prompt text that is not paper-writing specific.

## Reusable Ideas

- Skill schema and validator.
- Skill registry generated from file metadata.
- Per-skill versioning and provenance.
- Security scan pipeline before publishing skills.
- Agent-host neutral packaging.

## Code That May Be Reused

Avoid direct reuse in v0.1. Reimplement a narrower validator and registry to fit this project.

## License Risks

Low for repo-level ideas because MIT is permissive. Still check each skill's `license` metadata before copying any individual skill content.

## Security Risks

Skills can instruct agents to run commands, install packages, make network calls, or edit files. Paper-Writing-Hao should enforce declared permissions and dry-run behavior.

## Proposed Integration

- Reimplement skill schema in `src/paper_writing/skills/`.
- Add `paper-writing skill validate`.
- Add a registry index generated from built-in skills.

## Minimal Prototype

Create three skills: `academic-writing`, `abstract-writing`, `introduction-writing`. Validate required metadata and output contract.

## Open Questions

- Whether to support the exact Agent Skills frontmatter fields or a strict subset.
- Whether to publish skills under `.agents/skills` compatible layout in addition to the project layout.

## Final Decision

- [x] Reimplement
- [x] Conceptual reference only

