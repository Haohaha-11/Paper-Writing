# Paper-Writing-Hao

A GitHub-native research paper writing system for authors and AI agents.

Paper-Writing-Hao collects paper-writing skills, venue rules, review workflows, template provenance, and reusable artifacts for writing and polishing papers for arXiv, ICLR, NeurIPS, CVPR, ICML, ECCV, AAAI, and IEEE TMI.

It is not a one-click paper generator. The goal is to help researchers produce clearer, better-grounded, venue-aware manuscripts while keeping humans responsible for claims, evidence, citations, and final edits.

## What This Project Provides

- Agent-readable writing skills for strategy, abstracts, introductions, related work, methods, experiments, results, discussion, limitations/ethics, conclusions, appendices, captions, evidence checks, reviewer simulation, novelty scouting, revision, compression, and rebuttal planning.
- Venue rule folders for ICLR, CVPR, NeurIPS, ICML, ECCV, AAAI, IEEE TMI, and arXiv.
- Imported and checksummed LaTeX templates for major ML/CV venues.
- Real compile validation using TeX Live and `latexmk`.
- Structured workflows for draft-to-submission writing, full-paper writing, section rewrites, venue compliance review, pre-submission review, rebuttal, camera-ready preparation, and arXiv export.
- Reusable templates for paper context, claim-evidence matrices, review reports, rebuttal responses, and cspapers-assisted related-work checks.
- Lightweight scripts for repository validation, LaTeX project scanning, and template smoke compilation.

## Current Status

This repository is document-first. It is designed to be read and executed by humans, Claude Code, Codex, Cursor, ChatGPT, or similar coding/research agents.

There is no CLI or web app. The project is a GitHub-native knowledge base and workflow pack by design.

Verified locally on 2026-07-15:

| Target | Status |
|---|---|
| ICLR 2026 template | imported, checksummed, compile pass |
| CVPR 2026 author kit | imported, checksummed, compile pass |
| NeurIPS 2026 template | imported, checksummed, compile pass |
| ICML 2026 template | imported, checksummed, compile pass |
| ECCV 2026 template | imported, checksummed, compile pass |
| IEEE TMI / IEEEtran minimal example | compile pass |
| AAAI-26 author kit | not imported yet; official link was blocked by Cloudflare in this environment |

See `templates/compile-validation.md`, `templates/import-log.md`, and `IMPLEMENTATION_STATUS.md`.

## Quickstart

For a new paper:

1. Fill `examples/paper-context-template.md`.
2. Read the target venue folder under `venues/`.
3. Follow `workflows/draft-to-submission.md`.
4. Use `skills/paper-strategist/SKILL.md` to define the paper thesis and contribution map.
5. Use `skills/novelty-scout/SKILL.md` before making strong novelty claims.
6. Use `skills/claim-evidence-auditor/SKILL.md` before finalizing the abstract and introduction.
7. Use `skills/paper-redteam/SKILL.md` before submission.

For an existing draft:

1. Fill missing facts in `examples/paper-context-template.md`.
2. Select the venue checklist.
3. Follow `workflows/review-existing-draft.md`.
4. Apply the relevant skills from `skills/`.
5. Record unresolved risks in `examples/review-report-template.md`.

For synthetic walkthroughs, see:

- `examples/toy_ml_paper/`
- `examples/toy_iclr_paper/`
- `examples/toy_cvpr_paper/`
- `examples/toy_tmi_paper/`

## Repository Map

```text
Paper-Writing-Hao/
  AGENTS.md                 # Instructions for AI agents
  QUICKSTART.md             # Short usage guide
  IMPLEMENTATION_STATUS.md  # What is landed and what remains pending
  CONTRIBUTING.md           # Contribution guidelines
  THIRD_PARTY.md            # Third-party sources and template provenance notes
  skills/                   # Writing and review skills
  venues/                   # Venue rules, checklists, and official sources
  workflows/                # End-to-end writing and review workflows
  templates/                # Imported templates, checksums, provenance records
  examples/                 # Reusable paper/review/rebuttal artifacts
  docs/                     # Design notes and research records
```

## Core Principles

1. Evidence before polish.
   Every strong claim should be backed by an experiment, citation, derivation, design constraint, or clearly stated assumption.

2. Venue rules must come from official sources.
   Third-party summaries are useful hints, not authority.

3. Suggestions before edits.
   Agents should produce reports or patch suggestions before changing paper text.

4. No hallucinated citations.
   Citation-changing work must report provenance.

5. No detector-evasion workflows.
   This project supports clarity, evidence, and scholarly voice, not "humanizer" or AIGC-detector bypass features.

## Key Skills

- `paper-strategist`: paper thesis, contribution map, section plan.
- `abstract-writer`: evidence-grounded abstract drafting and revision.
- `introduction-writer`: motivation, gap, insight, and contribution framing.
- `related-work-writer`: citation-grounded positioning.
- `method-writer`: method structure, notation, algorithms, and mechanism clarity.
- `experiments-writer`: setup, datasets, baselines, metrics, and reproducibility.
- `results-writer`: result narrative, ablations, robustness, and evidence claims.
- `discussion-writer`: evidence-bounded interpretation and implications.
- `limitations-ethics-writer`: limitations, broader impact, privacy, and deployment boundaries.
- `conclusion-writer`: concise contribution recap and future-work boundaries.
- `appendix-writer`: appendix structure and supplement hygiene.
- `figure-caption-writer`: evidence-grounded captions for figures and tables.
- `claim-evidence-auditor`: claim-to-evidence matrix.
- `paper-redteam`: simulated reviewer and AC review.
- `novelty-scout`: related-work and novelty risk search, including cspapers-assisted checks.
- `revision-editor`: ranked revision plan after review or audit.
- `page-compressor`: length reduction while preserving LaTeX and evidence.
- `rebuttal-planner`: response strategy and revision planning.

See `skills/README.md`.

## Templates And TeX Environment

Imported template files live under `templates/upstream/`.

Important metadata:

- `templates/import-manifest.json`
- `templates/checksums.sha256`
- `templates/import-records/`
- `templates/compile-validation.md`

The local validation environment uses Ubuntu 24.04, TeX Live 2023/Debian, and `latexmk` 4.83. See `docs/tex-environment.md`.

Useful checks:

```bash
python3 scripts/validate_repo.py
sha256sum -c templates/checksums.sha256
python3 scripts/extract_latex_context.py templates/upstream/iclr/2026
python3 scripts/compile_templates.py --check
```

## Safety And Scope

This project handles unpublished research material. Use it carefully.

- Do not paste confidential drafts into untrusted services.
- Do not let agents invent experimental results or citations.
- Do not claim official venue compliance without checking the relevant venue source.
- Do not silently update official templates in existing paper projects.
- Do not treat search relevance as a review score or acceptance predictor.

## Roadmap

Near-term work:

- finish AAAI-26 template import once an accessible official artifact is available;
- import exact IEEE/TMI template selector artifacts;
- add more filled examples using synthetic toy papers;
- expand citation verification and official-source freshness checks.

See `ROADMAP.md`.

## Contributing

Contributions are welcome, especially:

- new venue rule files backed by official sources;
- improved writing skills with clear output contracts;
- corrected template provenance or checksums;
- synthetic examples that do not reveal unpublished work;
- review workflows for specific paper types.

Please avoid submitting copied third-party prompt text unless the license and provenance are clear.

## License

MIT. See `LICENSE`.

Template files under `templates/upstream/` retain their upstream terms. Check each import record before redistributing or modifying them.
