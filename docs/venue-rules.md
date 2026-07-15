# Venue Rules

Last checked: 2026-07-15

Venue rules change yearly. This file defines how to store them; it is not yet the source of truth for 2027+ submissions.

## Separation Model

```text
venues/<venue>/style.md              # stable writing expectations
venues/<venue>/<year>/rules.yaml     # annual policy and formatting rules
venues/<venue>/<year>/sources.yaml   # official URLs and retrieval metadata
venues/<venue>/<year>/checklist.md   # human-readable submission checklist
```

## `rules.yaml` Schema Draft

```yaml
venue: iclr
year: 2026
type: conference
status: draft
retrieved_at: "2026-07-15"

official_sources:
  - title: Official template
    url: https://github.com/ICLR/Master-Template
    commit: a28d335b0d46a3c39b205704a65faf41c9748433

page_limit:
  submission_main: 9
  rebuttal_main: 10
  camera_ready_main: null
  references_count_toward_limit: false
  appendix_allowed: true

policies:
  anonymous_review: true
  supplementary_allowed: true
  ethics_statement: recommended
  reproducibility_statement: recommended
  llm_disclosure: required_if_used
  arxiv_policy: verify_official

checks:
  require_no_author_names_in_submission: true
  require_no_acknowledgments_in_submission: true
  require_valid_references: true
  require_no_undefined_refs: true
```

## v0.1 Venue Priority

1. ICLR
2. CVPR
3. IEEE TMI

NeurIPS, ICML, ECCV, AAAI, and arXiv should be stubbed in the registry but not claimed as verified until their official pages and templates are locked.

## Second-Round Official Rule Stubs

These stubs record official sources found on 2026-07-15. They are not final enforcement data until converted into per-year `rules.yaml` files with tests.

| Venue | Official source | Initial enforceable checks |
|---|---|---|
| ICLR 2026 | `https://iclr.cc/Conferences/2026/AuthorGuide` | double blind; 9-page submission main text; 10-page discussion/camera-ready limit; references and appendices outside page limit; optional ethics/reproducibility statements; LLM usage disclosure if significant. |
| NeurIPS 2026 | `https://neurips.cc/Conferences/2026/MainTrackHandbook` | 9 content pages; references, appendices, and checklist outside content page count; 50 MB PDF limit; yearly LaTeX style required; anonymization and no acknowledgments at submission. |
| CVPR 2026 | `https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines` | double blind; no author-identifying acknowledgments/supplement/link leaks; OpenReview profile requirements; author list restrictions after deadlines. |
| ICML 2026 | `https://icml.cc/Conferences/2026/AuthorInstructions` | 8-page main body; references and appendices in same PDF; LaTeX-only; 50 MB submission PDF limit; anonymized submissions; no non-anonymous URLs. |
| ECCV 2026 | `https://eccv.ecva.net/Conferences/2026/SubmissionPolicies` | 14 pages including figures/tables; references-only pages allowed after limit; Springer LNCS style; 2026 author kit required. |
| AAAI-26 | `https://aaai.org/conference/aaai/aaai-26/policies-for-aaai-26-authors/` | author presentation policies; AAAI-26 author kit; AI-generated paper text prohibited except as experimental-analysis object; LLM editing/polishing author-written text allowed. |
| IEEE TMI | `https://ieeetmi.org/submission-checklist/` | regular/special initial submissions: 10 pages including references; challenge papers: 14 pages including references; PDF under 40 MB; paper-type-specific supporting documents; figures/tables in main text. |
| arXiv | `https://info.arxiv.org/help/submit_tex.html` | include local style/macros; include `.bib`/`.bbl` as needed; avoid referee mode; handle index/glossary artifacts; clean hidden files before announcement. |

## Important Rule

Third-party files such as AI Tutor `02_venues/*.md` are useful for knowing what to check, but they are not official policy sources. Any page limits, anonymity requirements, checklist requirements, LLM disclosure rules, and dates must be verified from the official venue or publisher source before being enforced.
