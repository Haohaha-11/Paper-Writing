# Repository Distillation Record: Official Templates

## Basic Information

- ICLR repository: https://github.com/ICLR/Master-Template
- ICLR commit: `a28d335b0d46a3c39b205704a65faf41c9748433`
- CVPR repository: https://github.com/cvpr-org/author-kit
- CVPR commit: `291758547e923160eb4d37079b7b9f0dfce82355`
- Last checked: 2026-07-15

## Why They Are Relevant

Official author kits are the only acceptable source for templates. Third-party template copies should not be treated as authoritative.

## Architecture

ICLR:

- yearly folders such as `iclr2026/`
- `iclr2026_conference.tex`
- `iclr2026_conference.sty`
- `iclr2026_conference.bst`
- supporting `natbib.sty`, `fancyhdr.sty`, `math_commands.tex`
- archived zips for older years

CVPR:

- `main.tex`
- `rebuttal.tex`
- `cvpr.sty`
- `ieeenat_fullname.bst`
- split `sec/*.tex`
- `preamble.tex`
- figure example

## Valuable Components

- Official source path and commit.
- Known root files and style files.
- Rebuttal template for CVPR.
- Yearly foldering for ICLR.

## Components Not Needed

- No direct editing of upstream files.
- No assumption that README contains all annual rules.

## Reusable Ideas

- Store template import records in `templates/registry.yaml`.
- Keep `templates/upstream/` pristine.
- Keep `templates/patched/` only for project-specific wrappers.
- Add checksums per file.

## Code That May Be Reused

Template files may be used for paper initialization if redistribution/license terms are verified or if downloaded from official source during init.

## License Risks

Both first-pass checks found no repo-level `LICENSE` file. Treat redistribution as unresolved until verified. Store provenance and prefer on-demand retrieval when possible.

## Security Risks

- Templates can include build behaviors and packages. Compile in a controlled toolchain.
- Annual template updates can silently change formatting. Lock per project.

## Proposed Integration

- `paper-writing template update --venue iclr --year 2026`
- `paper-writing init --venue iclr --year 2026`
- Lock `template.lock` in the paper project.

## Minimal Prototype

Support ICLR and CVPR template registry entries with commit, retrieved date, and checksum fields.

## Open Questions

- Official source and redistribution terms for IEEE TMI / IEEEtran.
- Whether to store template zips or reconstruct from upstream files.

## Final Decision

- [x] Conceptual reference only
- [x] Official upstream source

