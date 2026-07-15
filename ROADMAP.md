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

- Optional lightweight scripts for validation, source checking, template checksum, and cspapers API experiments.
- GitHub Actions LaTeX compile workflow using `xu-cheng/latex-action`.
- LaTeX scanner prototype for roots, inputs, bibliographies, figures, style files, and appendices.
- Full section-writing pack: related work, method, experiments, results, discussion, conclusion, limitations, ethics, appendix.
- Rebuttal planner and revision editor skills.
- Internal reviewer workflow with structured comments.
- Venue rule packs for NeurIPS, ICML, ECCV, AAAI, and arXiv after official template imports are locked.
- Better citation verification.

## v0.3

- CLI or package only if the document-first workflow proves stable.
- Camera-ready workflow.
- Role-model paper comparison.
- Evaluation fixtures for skill quality and regression.
- Optional structured conversion via LaTeXML/plasTeX for HTML/XML inspection.
