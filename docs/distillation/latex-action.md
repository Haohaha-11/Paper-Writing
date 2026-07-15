# Repository Distillation Record: latex-action

## Basic Information

- Repository: xu-cheng/latex-action
- URL: https://github.com/xu-cheng/latex-action
- License: MIT
- Main language: Shell and GitHub Action YAML
- Last checked: 2026-07-15
- Commit: `678ab28985c76971307abab772f8e218e7fcf1ec`

## Why It Is Relevant

It is a mature GitHub Action for compiling LaTeX with a full TeX Live container. It supports multiple engines, multiple root files, custom packages/fonts, pre/post compile scripts, and PDF artifact upload.

## Architecture

- Composite action.
- Docker image selection by TeX Live version and OS.
- `latexmk` default compiler.
- Inputs for engine, args, extra packages, fonts, pre/post scripts.

## Valuable Components

- `root_file` input.
- TeX Live version pinning.
- Default `latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode`.
- Artifact upload pattern.
- Support for XeLaTeX/LuaLaTeX.

## Components Not Needed

- Custom Docker image selection in the first CLI generator unless users opt in.
- Shell escape by default.

## Reusable Ideas

- Generate `.github/workflows/compile.yml`.
- Add `lint.yml`, `arxiv-check.yml`, and `release-pdf.yml` later.
- Pin TeX Live once venue template import is locked.

## Code That May Be Reused

Use the public action directly in workflow YAML.

## License Risks

Low, MIT.

## Security Risks

- GitHub Actions with arbitrary LaTeX can run risky packages if shell escape is enabled.
- Docker action needs Docker runtime on GitHub hosted runners, which is acceptable.

## Proposed Integration

Generate:

```yaml
- uses: xu-cheng/latex-action@v4
  with:
    root_file: main.tex
    texlive_version: 2026
```

Then upload PDF artifact with `actions/upload-artifact`.

## Minimal Prototype

Add `paper-writing init` option that writes `compile.yml` for the selected template.

## Open Questions

- Whether to pin action by tag or full commit.
- How to parse workflow logs into PR comments.

## Final Decision

- [x] Direct dependency

