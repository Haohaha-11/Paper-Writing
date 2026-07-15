# Implementation Status

Last updated: 2026-07-15

This file tracks what has been landed in the GitHub-native version of the project.

## Landed In v0.1 Skeleton

- [x] Top-level repo entry: `README.md`, `QUICKSTART.md`, `AGENTS.md`, `LICENSE`.
- [x] Skill library structure under `skills/`.
- [x] Venue library structure under `venues/`.
- [x] Workflow library under `workflows/`.
- [x] Template provenance area under `templates/`.
- [x] Example artifact templates under `examples/`.
- [x] Research/design notes under `docs/`.

## Landed After Skeleton

- [x] Machine-readable `rules.yaml` for ICLR 2026.
- [x] Machine-readable `rules.yaml` for CVPR 2026.
- [x] Machine-readable `rules.yaml` for IEEE TMI rolling.
- [x] Machine-readable `rules.yaml` for arXiv rolling.
- [x] Source-backed stub `rules.yaml` for NeurIPS 2026.
- [x] Source-backed stub `rules.yaml` for ICML 2026.
- [x] Source-backed stub `rules.yaml` for ECCV 2026.
- [x] Source-backed stub `rules.yaml` for AAAI-26.
- [x] Template import record template.
- [x] Template checksum policy.
- [x] Template import log.
- [x] Global skill output contracts.
- [x] Global skill checklists.
- [x] Paper redteam report template.
- [x] Claim-evidence auditor output format.
- [x] Novelty scout cspapers query guide.
- [x] cpapers-assisted review workflow.
- [x] cspapers hit classification template.
- [x] Deepened v0.1 skill pack: strategist, abstract, introduction, related work, claim-evidence, redteam, novelty, compression, rebuttal.
- [x] TeX Live environment installed and verified: `latexmk`, `pdflatex`, `xelatex`, IEEEtran, and LNCS.
- [x] Imported ICLR 2026 template with sha256 records.
- [x] Imported CVPR 2026 author kit with sha256 records.
- [x] Imported NeurIPS 2026 formatting zip with sha256 records.
- [x] Imported ICML 2026 style zip with sha256 records.
- [x] Imported ECCV 2026 paper kit with sha256 records.
- [x] Copied TeX Live IEEEtran assets for TMI/IEEE-style compile validation.
- [x] Compiled ICLR, CVPR, ECCV, NeurIPS, ICML, and minimal TMI examples successfully.
- [x] Added release-support files: `CONTRIBUTING.md`, `CITATION.cff`, and `THIRD_PARTY.md`.
- [x] Added repository validation script and GitHub Actions workflow.
- [x] Added synthetic toy paper walkthrough under `examples/toy_ml_paper/`.

## Still Pending

- [ ] License/redistribution review for copied template files.
- [ ] AAAI-26 author kit import; official `https://aaai.org/authorkit26/` returned Cloudflare error in this environment.
- [ ] Exact official IEEE/TMI template selector artifact import; current TMI validation uses TeX Live IEEEtran.
- [ ] More detailed venue rules for NeurIPS, ICML, ECCV, and AAAI.
- [ ] Full section-writing skills for Methods, Experiments, Results, Discussion, Limitations, Ethics, and Appendix.
- [ ] More concrete examples filled with sample paper content.
- [ ] Optional GitHub Actions workflow for LaTeX compilation.

## Current Rule

v0.1 remains document-first. Do not add CLI/package scaffolding unless the project direction changes.
