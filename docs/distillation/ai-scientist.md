# Repository Distillation Record: SakanaAI AI-Scientist

## Basic Information

- Repository: SakanaAI/AI-Scientist
- URL: https://github.com/SakanaAI/AI-Scientist
- License: The AI Scientist Source Code License, Responsible AI-derived
- Main language: Python
- Last checked: 2026-07-15
- Commit: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`

## Why It Is Relevant

AI-Scientist shows a complete automated research-to-paper pipeline: experiments, notes, LaTeX template, section-by-section writeup, citation rounds, compile/fix loop, LLM review, and improvement.

## Architecture

- `templates/<experiment>/` with `experiment.py`, `plot.py`, `prompt.json`, `seed_ideas.json`, and `latex/template.tex`.
- `perform_writeup.py` for section drafting, citation addition, refinement, and LaTeX compile.
- `perform_review.py` for PDF-to-text extraction and NeurIPS-style review JSON.
- Example papers and review benchmark data.

## Valuable Components

- Section-by-section drafting order.
- Per-section tips as structured writing guidance.
- Two-pass refinement: immediate section critique, then full-paper consistency refinement.
- Citation addition as a separate, source-backed loop.
- Compile and fix loop that checks references, figures, duplicate sections, and `chktex`.
- Review ensemble and meta-review idea.

## Components Not Needed

- Idea generation.
- Autonomous experiment execution.
- LLM-written code execution.
- Full Aider integration.
- Bundled ICLR 2024 template files.

## Reusable Ideas

- A workflow state machine: outline -> section draft -> section critique -> citation pass -> full consistency pass -> compile check.
- Explicit result-to-text constraints: do not hallucinate experimental results.
- LaTeX validation before considering a draft complete.
- Internal review report in structured JSON.

## Code That May Be Reused

Do not reuse in v0.1 due to custom license and scope mismatch.

## License Risks

High. The license includes use restrictions and mandatory disclosure clauses around machine-generated scientific manuscripts. Avoid dependency or code reuse unless reviewed.

## Security Risks

High. The project warns that it executes LLM-written code. This project should not execute unknown experiment code or agent-generated shell scripts in v0.1.

## Proposed Integration

- Reimplement only the workflow concepts.
- Add clear AI assistance disclosure support, driven by venue rules and user settings.
- Keep all code execution constrained to LaTeX compile/lint/export commands.

## Minimal Prototype

`paper-writing write-section abstract --dry-run` builds context, applies `abstract-writing`, and emits a patch plus checklist.

## Open Questions

- How to represent workflow state across runs.
- Whether to support review ensembles in v0.2.

## Final Decision

- [x] Conceptual reference only

