# Repository Distillation Record: arxiv-latex-cleaner

## Basic Information

- Repository: google-research/arxiv-latex-cleaner
- URL: https://github.com/google-research/arxiv-latex-cleaner
- License: Apache-2.0
- Main language: Python
- Last checked: 2026-07-15
- Commit: `bcc1460cc4be72ddac08f22c54b23f23f14b102d`

## Why It Is Relevant

It already solves the core arXiv export problem: copy a LaTeX project into a clean upload directory, remove auxiliary files/comments, keep only referenced assets, optionally resize/compress images, and handle some TikZ/SVG cases.

## Architecture

- CLI entrypoint.
- YAML config support.
- File splitting into root/non-root TeX, figures, non-TeX assets.
- Comment and command/environment deletion.
- Referenced-file detection.
- Image resize/compress/PNG-to-JPG logic.
- Unit tests with fixture projects.

## Valuable Components

- Work on copied output folder, not original project.
- Remove comments and auxiliary files.
- Keep only referenced assets.
- Allow custom delete commands and regex replacements.
- Optional image compression and conversion.

## Components Not Needed

- Directly exposing every cleaner option as v0.1 CLI surface.
- Treating cleaner output as sufficient without recompilation/reporting.

## Reusable Ideas

- `paper-writing export arxiv` should wrap cleaner, then compile and emit a report.
- Keep a project-level `arxiv-export.yaml`.
- Add page-size, file-size, missing-reference, and PDF sanity checks around cleaner.

## Code That May Be Reused

Can be used as an optional dependency or invoked as a subprocess, preserving Apache-2.0 notices.

## License Risks

Low, Apache-2.0 is permissive. Preserve license notices.

## Security Risks

- Cleanup can remove comments or files unexpectedly if run on source directory. Always export to copied directory.
- Image conversion can change file names and references; verify by recompiling.

## Proposed Integration

```bash
paper-writing export arxiv --config arxiv-export.yaml
```

The command should output:

- clean directory path
- zip/tar path
- removed files list
- changed image list
- compile result
- arXiv readiness checklist

## Minimal Prototype

Call `arxiv_latex_cleaner` on a fixture project, zip the output, and verify original files are unchanged.

## Open Questions

- Whether to vendor a thin Python wrapper or require external installation.
- Whether to reimplement unused-asset detection for tighter integration.

## Final Decision

- [x] Optional dependency
- [x] Direct dependency candidate

