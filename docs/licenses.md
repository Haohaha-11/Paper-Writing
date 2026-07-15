# Licenses

Last checked: 2026-07-15

This is an engineering risk register, not legal advice.

| Source | License observed | Reuse stance |
|---|---|---|
| K-Dense Scientific Agent Skills | MIT at repo level; individual skill metadata may vary | Ideas and schema concepts are compatible; do not blindly copy individual skills without checking per-skill metadata |
| PaperDebugger | AGPL-3.0 | Conceptual reference only unless this project intentionally adopts AGPL-compatible distribution |
| jiarui-liu/overleaf AI Tutor | AGPL-3.0 | Conceptual reference only; do not copy code, prompts, or skill markdown into an MIT-style project |
| SakanaAI AI-Scientist | Custom Responsible AI-derived source code license | Conceptual reference only; do not use as dependency for v0.1 |
| arxiv-latex-cleaner | Apache-2.0 | Can be optional dependency or wrapped CLI, preserving notice/license |
| xu-cheng/latex-action | MIT | Can be used directly in generated GitHub workflow |
| ICLR/Master-Template | No repo-level license found in first pass | Treat as official author kit; verify redistribution terms before vendoring |
| cvpr-org/author-kit | No repo-level license found in first pass | Treat as official author kit; verify redistribution terms before vendoring |

## Project License Recommendation

Use MIT or Apache-2.0 for Paper-Writing-Hao if the goal is broad reuse. That requires:

- no copied AGPL code or prompt text;
- no copied AI-Scientist implementation;
- clear notices for Apache/MIT dependencies;
- official templates stored with their own provenance and license metadata;
- generated paper text disclosed according to target venue rules and user policy.

