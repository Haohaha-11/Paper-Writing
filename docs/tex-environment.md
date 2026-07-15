# TeX Environment

Last checked: 2026-07-15

The local environment was upgraded to compile real conference/journal templates.

## Installed Packages

Installed via `apt-get` on Ubuntu 24.04:

- `latexmk`
- `texlive-latex-recommended`
- `texlive-latex-extra`
- `texlive-fonts-recommended`
- `texlive-publishers`
- `texlive-science`
- `texlive-xetex`
- `biber`

## Verified Tools

- `latexmk`: 4.83
- `pdflatex`: pdfTeX 3.141592653-2.6-1.40.25, TeX Live 2023/Debian
- `xelatex`: XeTeX 3.141592653-2.6-0.999995, TeX Live 2023/Debian
- `IEEEtran.cls`: found via `kpsewhich`
- `llncs.cls`: found via `kpsewhich`

## Compile Validation

See `templates/compile-validation.md`.

Templates compiled successfully from temporary working copies:

- ICLR 2026
- CVPR 2026
- ECCV 2026
- NeurIPS 2026
- ICML 2026
- minimal TMI/IEEEtran example

AAAI-26 was not compiled because the official author kit link was blocked by Cloudflare in this environment.
