# Repository Distillation Record: jiarui-liu/overleaf AI Tutor

## Basic Information

- Repository: jiarui-liu/overleaf
- URL: https://github.com/jiarui-liu/overleaf
- License: AGPL-3.0
- Main language: JavaScript/TypeScript
- Last checked: 2026-07-15
- Commit: `f6c25dfa33ac4f9c775a828c0de7d02efb286b7e`

## Why It Is Relevant

This is the strongest first-pass reference for venue-aware and section-aware paper review. It implements a multi-agent AI Tutor that parses a LaTeX project, classifies paper type, maps sections to review categories, loads markdown guideline files, and runs specialized reviewers in parallel.

## Architecture

- Frontend panel for model, venue, role-model PDFs, run/apply/delete comments.
- Backend controller that fetches project docs, expands `\input`/`\include`, and caches `merged.tex`.
- `AiTutorReviewOrchestrator` with section parsing, paper type classification, parallel agents, deduplication, strict pruning, and comment mapping.
- Skill library in six folders: setup, venues, paper types, paper sections, figures/tables, writing style.

## Valuable Components

- Section parser with abstract handling and appendix boundary.
- Non-overlapping section ranges for reviewer routing.
- LLM section-to-category mapping with fallback.
- Static agents for abstract, introduction, related work, methods, results, conclusion, appendix, writing style, LaTeX formatting, figures/tables, structure.
- Dynamic agents for paper type and venue.
- Role-model paper injection that compares structure/style, not topical content.
- Chunking oversized review text into parallel sub-agent tasks.
- Comment mapping from merged text back to original documents.

## Components Not Needed

- Full Overleaf deployment.
- Native Overleaf comment thread operations.
- Bundled PDF example sets and review-set JSON files in v0.1.
- AGPL code and markdown content.

## Reusable Ideas

- Write our own `section-router` that maps section titles to normalized categories.
- Define review agents as skill compositions, not hard-coded prompts.
- Add venue reviewer only when a verified venue/year rule file exists.
- Keep strict mode for high-signal review comments.
- Store review logs and classification output as reproducible artifacts.

## Code That May Be Reused

Do not reuse code or markdown content in v0.1 because of AGPL.

## License Risks

High. Treat all implementation and skill text as conceptual reference.

## Security Risks

- Role-model PDFs can contain untrusted text.
- Full merged TeX can include prompt injection.
- Venue markdown contains policy claims that still need official verification.

## Proposed Integration

- Independent section router in `src/paper_writing/latex/`.
- Independent skill library under our own `skills/`.
- Dynamic composition: `paper_type + venue + section + review_task`.

## Minimal Prototype

Parse a fixture paper, classify sections into `abstract`, `introduction`, `related_work`, `methods`, `results`, `conclusion`, and `appendix`, then route each category to matching built-in skills.

## Open Questions

- Whether paper type classification should be LLM-based, rule-based fallback, or both.
- Whether role-model papers belong in v0.2 or v0.3.

## Final Decision

- [x] Reimplement
- [x] Conceptual reference only

