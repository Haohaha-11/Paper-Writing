# arXiv Export Workflow

## Goal

Prepare a clean arXiv source package.

## Steps

1. Read `venues/arxiv/rolling/export-checklist.md`.
2. Remove venue-only anonymous metadata if submitting a public version.
3. Include required local style, class, bibliography, figure, glossary, and index files.
4. Remove build artifacts and hidden files.
5. Compile from the export package.
6. Record what was excluded.

## Rule

The arXiv package should compile independently of the author's local machine state.
