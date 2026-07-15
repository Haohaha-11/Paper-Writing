# Template Registry

Last checked: 2026-07-15

Templates are supply-chain artifacts. They should be retrieved from official upstreams, checksummed, and locked by venue/year. Do not silently update templates in existing paper projects.

## Registry Shape

```yaml
templates:
  - venue: iclr
    year: 2026
    type: conference
    source:
      type: github
      repository: ICLR/Master-Template
      commit: a28d335b0d46a3c39b205704a65faf41c9748433
      retrieved_at: "2026-07-15"
      url: https://github.com/ICLR/Master-Template
    files:
      root: iclr2026/iclr2026_conference.tex
      style: iclr2026/iclr2026_conference.sty
      bibliography_style: iclr2026/iclr2026_conference.bst
    checksums:
      style_sha256: "<fill during template import>"
      bst_sha256: "<fill during template import>"
    license:
      status: unknown
      notes: "No repo-level LICENSE found in first pass; verify before redistribution."

  - venue: cvpr
    year: 2026
    type: conference
    source:
      type: github
      repository: cvpr-org/author-kit
      commit: 291758547e923160eb4d37079b7b9f0dfce82355
      retrieved_at: "2026-07-15"
      url: https://github.com/cvpr-org/author-kit
    files:
      root: main.tex
      style: cvpr.sty
      bibliography_style: ieeenat_fullname.bst
      rebuttal: rebuttal.tex
    checksums:
      style_sha256: "<fill during template import>"
      bst_sha256: "<fill during template import>"
    license:
      status: unknown
      notes: "No repo-level LICENSE found in first pass; verify before redistribution."
```

## Import Rules

- Store upstream commit, retrieval date, and checksum for every imported file.
- Keep pristine upstream templates separate from project-patched templates.
- Never overwrite a paper's locked template unless the user requests an update.
- Keep official template metadata separate from annual submission policy.
- Prefer official GitHub repositories or publisher pages over third-party collections.

## v0.1 Official Sources

| Venue | First source | Result |
|---|---|---|
| ICLR | `https://github.com/ICLR/Master-Template` | Contains yearly folders through `iclr2026/` plus archives |
| CVPR | `https://github.com/cvpr-org/author-kit` | README states updated for CVPR 2026; contains `main.tex`, `cvpr.sty`, `rebuttal.tex` |
| NeurIPS | `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` | Imported, checksummed, compile pass |
| ICML | `https://media.icml.cc/Conferences/ICML2026/Styles/icml2026.zip` | Imported, checksummed, compile pass |
| AAAI | AAAI-26 Author Kit linked from `https://aaai.org/conference/aaai/aaai-26/policies-for-aaai-26-authors/` | Not imported; `https://aaai.org/authorkit26/` returned Cloudflare error in this environment |
| ECCV | `https://github.com/paolo-favaro/paper-template` | Imported, checksummed, compile pass |
| IEEE TMI | `https://ieeetmi.org/submission-checklist/` and IEEE template selector | TeX Live IEEEtran assets copied/checksummed and minimal compile pass; exact IEEE/TMI artifact still pending |
| arXiv | `https://info.arxiv.org/help/submit_tex.html` | No venue template; export packaging rules source |

## Current Import Records

Operational import records now live under `templates/import-records/`.

- ICLR 2026: `templates/import-records/iclr-2026.md`
- CVPR 2026: `templates/import-records/cvpr-2026.md`
- NeurIPS 2026: `templates/import-records/neurips-2026.md`
- ICML 2026: `templates/import-records/icml-2026.md`
- ECCV 2026: `templates/import-records/eccv-2026.md`
- TMI / IEEEtran: `templates/import-records/tmi-rolling-texlive-ieeetran.md`
- AAAI-26 failed attempt: `templates/import-records/aaai-2026-failed.md`

Checksums are in `templates/checksums.sha256`; compile validation is in `templates/compile-validation.md`.
