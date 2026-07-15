# Repository Evaluation

Last checked: 2026-07-15

This document summarizes the first distillation pass over the repositories listed in `docs/design_v1.md`. Scores are 1-5. The decision column is intentionally conservative: permissive dependencies can be wrapped, copyleft or custom-licensed projects should only be used as conceptual references unless the whole project intentionally adopts compatible terms.

| Project | Commit checked | License | Relevance | Architecture | Code Quality | Docs | Activity | License | Extensible | Agent Compat. | LaTeX | Eval | Total / 50 | Decision |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| K-Dense Scientific Agent Skills | `fc0b9f6` | MIT, per-skill metadata | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 2 | 4 | 43 | Reimplement skill infrastructure; cite as conceptual/source-format reference |
| PaperDebugger | `527afed` | AGPL-3.0 | 5 | 4 | 3 | 3 | 4 | 1 | 3 | 4 | 4 | 2 | 33 | Conceptual reference only for project context, section tools, diff UX |
| jiarui-liu/overleaf AI Tutor | `f6c25df` | AGPL-3.0 | 5 | 5 | 3 | 5 | 4 | 1 | 5 | 3 | 4 | 3 | 38 | Conceptual reference for venue x section x paper-type routing |
| SakanaAI AI-Scientist | `1de1dbc` | Custom Responsible AI-derived license | 4 | 4 | 3 | 4 | 4 | 1 | 3 | 2 | 4 | 4 | 33 | Conceptual reference only for writeup/review pipeline |
| google-research/arxiv-latex-cleaner | `bcc1460` | Apache-2.0 | 5 | 4 | 4 | 4 | 3 | 5 | 3 | 2 | 5 | 4 | 39 | Optional dependency or wrapper for `paper-writing export arxiv` |
| xu-cheng/latex-action | `678ab28` | MIT | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 2 | 5 | 4 | 42 | Direct GitHub Actions integration |
| ICLR/Master-Template | `a28d335` | No repo-level license found | 5 | 3 | 3 | 2 | 4 | 2 | 3 | 1 | 5 | 1 | 29 | Official upstream; store provenance and checksum, do not mutate |
| cvpr-org/author-kit | `2917585` | No repo-level license found | 5 | 4 | 4 | 4 | 5 | 2 | 3 | 1 | 5 | 3 | 36 | Official upstream; store provenance and checksum, do not mutate |

## Immediate Decisions

- Build our own MIT-compatible skill schema, validator, registry, and loader. Use K-Dense as a format reference, not as a source of paper-writing prompts.
- Use the jiarui-liu/overleaf AI Tutor as the strongest reference for routing review work by section, paper type, venue, and role model papers. Do not copy AGPL code or markdown skill text.
- Use PaperDebugger mainly for real-editor workflow ideas: full project context, selected-text revision, diff display, and read-only default behavior.
- Treat AI-Scientist as a pipeline reference only. Its license and autonomous code execution model are not suitable for v0.1 reuse.
- Wrap `arxiv-latex-cleaner` as an optional installed dependency first. Add a project-specific report layer around it.
- Generate GitHub Actions workflow using `xu-cheng/latex-action@v4`, with pinned TeX Live version once each venue template is locked.
- Official templates should be pulled from official upstreams into a provenance-controlled registry. Annual rules must be verified from official conference/journal pages, not from third-party summaries.

## Second-Round Conclusion

The first repository list is sufficient for a v0.1 architecture, but not sufficient by itself for the full product. The project must add:

- an official venue-source registry for ICLR, NeurIPS, CVPR, ICML, ECCV, AAAI, IEEE TMI, and arXiv;
- a template import/checksum workflow for every annual template or publisher artifact;
- a LaTeX parser/scanner layer independent of the upstream writing-agent projects;
- a dedicated IEEE TMI skill/checklist layer instead of a generic IEEE preset;
- project-owned writing and review skills so copyleft/custom-licensed prompts are not copied into this repository.

See `docs/second-round-research.md`, `docs/latex-parser-options.md`, and `docs/tmi-notes.md`.

## Writing-Skill Addendum

A separate writing-skill search found enough useful skill/agent projects to justify a dedicated project-owned writing pack. The best external patterns are strategist/composer separation, section-specific rhetorical moves, claim-evidence auditing, red-team reviewer simulation, citation-grounded RAG, and LaTeX-preserving revision.

The project should not copy third-party prompts by default. Even when a repo is MIT or Apache-2.0, writing guidance often derives from notes, papers, or examples with their own provenance. Implement original skills and keep source links in the distillation docs.

See `docs/writing-skills-research.md`.
