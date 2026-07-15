# Security

Last checked: 2026-07-15

Status note: v0.1 is document-first and does not run shell commands. This file records safety requirements for future tooling, scripts, CI helpers, or a possible CLI.

Paper writing agents touch unpublished research, author identities, private results, and LaTeX files that can execute commands during compilation. The default stance must be local-first, least privilege, and human-approved writes.

## Main Risks

- Prompt injection from papers, BibTeX, comments, review text, and downloaded templates.
- Accidental leakage of anonymous submission identity.
- Hallucinated citations or fabricated venue rules.
- Shell execution through LaTeX packages, `--shell-escape`, minted, or custom build scripts.
- Destructive cleanup during arXiv export.
- Third-party license contamination from AGPL or custom-licensed reference projects.
- Network calls that send unpublished paper text to unapproved services.

## Required Controls

- Default to dry-run for review and revision.
- Require explicit approval for file writes.
- Do not enable LaTeX shell escape by default.
- Keep official template imports checksummed and immutable.
- Keep third-party upstream clones outside the project tree.
- Store provenance for every venue rule and template.
- Make citation-changing workflows verify sources and emit a citation provenance report.
- Run skill validation and security checks before publishing built-in skills.

## Skill Security

Each skill must declare:

- `allowed_operations`
- network requirements
- shell command requirements
- citation mutation permissions
- file write permissions

Borrow the idea of K-Dense's skill scanning pipeline, but implement a narrower validator first. Security scanning should be added before accepting community skills.

## LaTeX Security

`paper-writing compile` should:

- use `latexmk` without shell escape by default;
- surface shell-escape requirements as warnings;
- run in a container or devcontainer in CI;
- parse logs for undefined references/citations and fatal errors;
- keep generated files out of source patches unless explicitly requested.

`paper-writing export arxiv` should work on a copied output directory, never the source project.
