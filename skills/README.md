# Skills

Skills are reusable instructions for authors and AI agents. Each skill should produce a report, patch suggestion, or structured artifact. Skills should not silently rewrite paper source files.

The v0.1 skills are original project-owned instructions distilled from the research notes in `docs/writing-skills-research.md`. They are inspired by patterns from existing academic-writing and review-agent projects, but the skill text here is not copied from those projects.

## Recommended Order

For a new paper:

1. `paper-strategist`
2. `novelty-scout`
3. `abstract-writer`
4. `introduction-writer`
5. `related-work-writer`
6. `claim-evidence-auditor`
7. `paper-redteam`
8. `page-compressor`

For an existing draft:

1. `claim-evidence-auditor`
2. `novelty-scout`
3. `paper-redteam`
4. section-specific writer skill
5. `page-compressor`

For reviews/rebuttal:

1. `paper-redteam` if doing a self-review first
2. `rebuttal-planner`
3. `claim-evidence-auditor` for disputed claims
4. `page-compressor` for final response or camera-ready constraints

## v0.1 Skill Pack

| Skill | Role | Status |
|---|---|---|
| `paper-strategist` | paper thesis, contribution map, reviewer contract | deepened v0.1 |
| `abstract-writer` | problem-gap-method-result-implication abstract | deepened v0.1 |
| `introduction-writer` | paragraph roles, contribution framing, evidence preview | deepened v0.1 |
| `related-work-writer` | citation-grounded taxonomy and positioning | deepened v0.1 |
| `claim-evidence-auditor` | claim extraction, evidence rating, risk actions | deepened v0.1 |
| `paper-redteam` | simulated reviewers and AC meta-review | deepened v0.1 |
| `novelty-scout` | cspapers-assisted novelty and missing-related-work scan | deepened v0.1 |
| `page-compressor` | length reduction with LaTeX/evidence safety | deepened v0.1 |
| `rebuttal-planner` | reviewer issue clustering and response strategy | deepened v0.1 |

## What A Good Skill Run Should Produce

Use `output-contracts.md` for required fields and `checklists.md` before running a skill.

At minimum, a good run should include:

- the input scope reviewed;
- venue and paper type assumptions;
- concrete findings;
- evidence gaps;
- recommended changes;
- patch suggestions when source text is provided;
- residual risks.

## Safety

- Do not invent citations, datasets, numbers, or claims.
- Do not add venue compliance claims unless backed by official venue sources.
- Preserve LaTeX commands, labels, refs, citations, equations, and figure/table references.
- Prefer small patch suggestions over full-section rewrites.
- Mark unchecked facts explicitly.

## Source Policy

These skills may list inspirations and reviewed sources, but they should remain original project text. If third-party skill text is copied in the future, keep it separate, preserve its license, and do not mix it into the project-owned skills without review.
