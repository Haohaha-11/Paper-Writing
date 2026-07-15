# LaTeX Parser Options

Last checked: 2026-07-15

The paper-writing system needs LaTeX awareness, but it should not pretend that parsing arbitrary TeX is easy. The practical route is to combine tolerant parsing, explicit project scanning, and compile-time validation.

## Requirements

- discover root files, `\input`, `\include`, bibliography files, figure assets, style files, and appendices;
- extract a stable section tree for Introduction, Related Work, Method, Experiments, Results, Discussion, Limitations, Ethics, Appendix, and venue-specific sections;
- preserve labels, refs, citations, equations, figures, tables, comments, and custom macros during edits;
- generate small patches rather than full-file rewrites;
- support arXiv export checks and camera-ready packaging;
- use LaTeX compilation as the final source of truth.

## Candidate Tools

| Tool | Fit | Strengths | Risks | v0.1 decision |
|---|---|---|---|---|
| `pylatexenc.latexwalker` | Snippet/block parser | Simple Python API; explicitly represents parsed LaTeX as node classes. | Its docs say it is not a full LaTeX engine. | Good candidate for section/block extraction. |
| `TexSoup` | Tolerant document navigation/editing | Fault-tolerant Python package for searching, navigating, and modifying LaTeX; permissive BSD-2-Clause license. | Tolerant parsing can hide semantic mistakes; benchmark claims should be reproduced locally before relying on them. | Good candidate for v0.1 experiments. |
| `plasTeX` | Python document framework | Provides a DOM, macro/package model, renderers, and TeX stream/context APIs. | More complex than needed for first scanner; custom macro support may require work. | Evaluate after v0.1 parser tests. |
| `LaTeXML` | Structured conversion | Mature TeX/LaTeX to XML/HTML/MathML/ePub/JATS converter; useful for semantic export. | Perl stack; heavier dependency; package bindings determine success. | Optional later converter, not core v0.1 parser. |
| `tree-sitter-latex` | Incremental syntax tree | Useful for editor-like incremental parsing and syntax-aware ranges. | Syntax tree alone does not resolve TeX macros, includes, bibliography, or build semantics. | Later editor/LSP integration candidate. |

## Recommended v0.1 Architecture

```text
LatexProjectScanner
  - finds roots, inputs, includes, bibliographies, figures, styles
  - normalizes paths and reports missing assets

LatexBlockExtractor
  - extracts section and environment spans
  - keeps byte/line ranges for patch generation
  - starts with pylatexenc or TexSoup behind an adapter

LatexPatchEngine
  - applies section-scoped edits
  - refuses edits that cross protected environments unless explicitly requested

LatexCompiler
  - runs latexmk/xelatex/pdflatex
  - parses warnings/errors
  - serves as correctness oracle
```

## Acceptance Tests

Create fixtures before choosing the parser permanently:

- single-file ICLR paper with sections, figures, tables, citations, equations;
- multi-file CVPR paper using `\input` and nested figure paths;
- NeurIPS paper with checklist and appendix;
- IEEE TMI paper with first-page footnote, references, figures in text, and no biographies;
- arXiv package with custom `.sty`, `.bib`, `.bbl`, glossary/index artifacts;
- intentionally broken labels, missing figures, duplicate bibliography keys, unclosed environments.

## Sources

- pylatexenc `latexwalker`: https://pylatexenc.readthedocs.io/en/latest/latexwalker/
- TexSoup: https://github.com/alvinwan/TexSoup
- plasTeX docs: https://plastex.github.io/plastex/plastex/index.html
- LaTeXML: https://github.com/brucemiller/LaTeXML
- tree-sitter-latex: https://github.com/latex-lsp/tree-sitter-latex
