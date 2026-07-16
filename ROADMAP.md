# Roadmap

## v0.1

- GitHub-native project skeleton with `README.md`, `LICENSE`, `skills/`, `venues/`, `workflows/`, `templates/`, and `examples/`.
- Agent-readable skill specification and built-in writing skill pack.
- Project-owned writing skill pack: `paper-strategist`, `abstract-writer`, `introduction-writer`, `claim-evidence-auditor`, `paper-redteam`, `novelty-scout`, and `page-compressor`.
- `novelty-scout` cspapers.org integration for title/abstract-level related-work and novelty checks.
- Venue rule/checklist files for ICLR, CVPR, IEEE TMI, plus official-source stubs for NeurIPS, ICML, ECCV, AAAI, and arXiv.
- Template registry with official-source provenance and import policy.
- Workflow docs for full paper writing, section rewrite, pre-submission review, rebuttal, camera-ready, and arXiv export.
- Example artifacts: paper context, claim-evidence matrix, review report, and rebuttal response.
- TMI medical-imaging checklist for page count, file size, paper type, conference-extension disclosure, figures/tables, privacy, and validation.

## v0.2

- Landed: lightweight scripts for repository validation, template checksum verification, LaTeX context extraction, and template smoke compilation.
- Landed: manual GitHub Actions template smoke workflow.
- Landed: LaTeX scanner prototype for roots, inputs, bibliographies, figures, style/class files, and appendices.
- Landed: section-writing pack for methods, experiments, results, discussion, conclusion, limitations/ethics, appendix, figure/table captions, and revision editing.
- Landed: draft-to-submission, existing-draft review, and venue-compliance workflows.
- Landed: synthetic ICLR, CVPR, and TMI examples.
- Still open: more detailed current venue rule packs for NeurIPS, ICML, ECCV, AAAI, and arXiv after official rule freshness checks.
- Still open: citation verification beyond local bibliography/context checks.

## v0.3

- Compilable synthetic paper fixtures for at least ICLR, CVPR, and TMI.
- Citation verification workflow with DOI/arXiv/OpenReview/Semantic Scholar cross-checks.
- Official-source freshness checker for venue rules.
- Role-model paper comparison workflow.
- Evaluation fixtures for skill quality and regression.
- Optional structured conversion via LaTeXML/plasTeX for HTML/XML inspection.
- CLI or package only if the document-first workflow proves stable.
