# Second-Round Research

Last checked: 2026-07-15

This pass answers whether the initial repository list is enough for the original goal: a project that helps write arXiv, ICLR, NeurIPS, CVPR, ICML, ECCV, AAAI, and IEEE TMI papers.

Short answer: the original list is enough for a v0.1 system skeleton, but not enough for a trustworthy venue-aware writing product. The missing pieces are official annual policy sources, a locked template registry for every target venue, a LaTeX structure parser strategy, TMI-specific manuscript checks, and project-owned writing/review skills.

## What Was Added

### Official Venue Sources

The first pass only fully pinned ICLR and CVPR templates. The second pass confirms that the project needs an official-source layer for every target venue:

| Venue | Source status | Notes |
|---|---|---|
| ICLR 2026 | Verified official guide and template URL | 9-page submission main text, 10 pages for rebuttal/camera-ready, official template zip from `ICLR/Master-Template`. |
| NeurIPS 2026 | Verified official CFP, main track handbook, and template zip URL | 9 content pages, references/appendices/checklist outside content page count, 50 MB submission PDF limit, yearly LaTeX style required. |
| CVPR 2026 | Verified official author guidelines and first-pass official author kit repo | Double-blind review, OpenReview profile requirements, author-list freeze rules. |
| ICML 2026 | Verified official CFP, author instructions, and style zip URL | 8-page submission body, references/impact statement/appendices outside body count, LaTeX-only submissions, 50 MB submission PDF limit. |
| ECCV 2026 | Verified official submission policies and paper kit repo link | 14 pages including figures/tables in Springer LNCS style, references allowed beyond limit, new 2026 template required. |
| AAAI-26 | Verified official author policies and author kit link | Strong AI-generated-text policy: generated text is prohibited except as part of experimental analysis; editing/polishing author-written text is allowed. |
| IEEE TMI | Verified official checklist and manuscript template pointer | Initial regular/special issue submissions limited to 10 pages including references; challenge papers limited to 14 pages; PDF below 40 MB; TMI has paper-type-specific checklists. |
| arXiv | Verified official TeX submission help | Needs export rules for included style files/macros, `.bib`/`.bbl`, glossary/index files, no referee mode, and hidden-file cleanup. |

### LaTeX Parser Gap

The initial repository list includes compilation and arXiv cleanup, but not a robust LaTeX project parser. This is a real gap because the system needs to:

- locate section boundaries and map text to venue/section skills;
- inspect labels, refs, citations, figures, tables, appendices, and supplements;
- create patchable edits without corrupting LaTeX;
- produce export reports for arXiv and camera-ready packages.

The recommended v0.1 path is a hybrid parser:

1. use a conservative project scanner for `\input`, `\include`, bibliography files, figures, and build roots;
2. use `pylatexenc.latexwalker` or `TexSoup` for tolerant section/block extraction;
3. use actual LaTeX compilation as the final correctness oracle;
4. keep LaTeXML/plasTeX as later optional converters when structured XML/HTML export is needed.

See `docs/latex-parser-options.md`.

### TMI-Specific Gap

TMI is not just "another IEEE template." It needs journal-style and medical-imaging checks:

- manuscript type routing: regular/special issue, challenge paper, invited review, revision/resubmission;
- page-limit and file-size checks by paper type;
- conference-extension disclosure and overlap checks;
- supplementary-file type restrictions;
- first-page acknowledgments/affiliation formatting;
- clinical/medical-imaging reporting expectations: validation protocol, dataset provenance, privacy/consent/IRB language where applicable, challenge gold-standard/evaluation setup when relevant.

This should become a dedicated `venue:tmi` skill set, not only an IEEEtran template wrapper.

## Design Decision

Do not treat third-party AI-writing projects as policy sources. Use them to learn workflow patterns, then build our own registry and checks from official pages.

For v0.1, implement these capabilities in this order:

1. Official source registry with retrieval date and URL.
2. Template registry with checksums and immutable per-paper locks.
3. Venue rules YAML for ICLR, CVPR, TMI first; stub NeurIPS, ICML, ECCV, AAAI, arXiv.
4. LaTeX project scanner plus tolerant section extraction.
5. Compile/check/export commands.
6. Project-owned paper-writing skills by venue, section, and paper type.

## Sources

- ICLR 2026 Author Guide: https://iclr.cc/Conferences/2026/AuthorGuide
- ICLR template: https://github.com/ICLR/Master-Template
- NeurIPS 2026 CFP: https://neurips.cc/Conferences/2026/CallForPapers
- NeurIPS 2026 Main Track Handbook: https://neurips.cc/Conferences/2026/MainTrackHandbook
- CVPR 2026 Author Guidelines: https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines
- CVPR author kit: https://github.com/cvpr-org/author-kit
- ICML 2026 CFP: https://icml.cc/Conferences/2026/CallForPapers
- ICML 2026 Author Instructions: https://icml.cc/Conferences/2026/AuthorInstructions
- ECCV 2026 Submission Policies: https://eccv.ecva.net/Conferences/2026/SubmissionPolicies
- ECCV 2026 paper kit repo linked from official page: https://github.com/paolo-favaro/paper-template
- AAAI-26 Author Policies: https://aaai.org/conference/aaai/aaai-26/policies-for-aaai-26-authors/
- IEEE TMI home and author links: https://ieeetmi.org/
- IEEE TMI Submission Checklist: https://ieeetmi.org/submission-checklist/
- arXiv TeX submission help: https://info.arxiv.org/help/submit_tex.html
