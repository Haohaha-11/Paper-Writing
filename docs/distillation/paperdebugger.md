# Repository Distillation Record: PaperDebugger

## Basic Information

- Repository: PaperDebugger/PaperDebugger
- URL: https://github.com/PaperDebugger/PaperDebugger
- License: AGPL-3.0
- Main language: Go and TypeScript
- Last checked: 2026-07-15
- Commit: `527afed307371d213c495e0444f64eb3666c617c`

## Why It Is Relevant

PaperDebugger works inside real Overleaf projects and demonstrates how an assistant can read a full LaTeX project, respond to selected text, show diffs, and keep user approval in the loop.

## Architecture

- Go backend with HTTP/gRPC services.
- Browser extension / webapp integration.
- Project service storing full content and instructions.
- Toolkit tools for files and LaTeX.
- Frontend component for diff/copy/insert actions.

## Valuable Components

- Read-only default posture: suggestions first, user applies changes.
- Selected-text revision workflow.
- Diff visualization before insertion.
- Project instructions and user instructions in prompt context.
- LaTeX section structure and section-source tools.

## Components Not Needed

- Full browser extension.
- MongoDB-backed service architecture.
- OAuth and Overleaf account integration.
- AGPL implementation code.

## Reusable Ideas

- `get_document_structure`: section tree as a tool.
- `read_section_source`: section-scoped source extraction with line numbers.
- Text patch UI semantics: show diff, copy, apply.
- Tool-call budget and project-context prompt design.

## Code That May Be Reused

Do not reuse code in an MIT/Apache v0.1 because of AGPL.

## License Risks

High. AGPL code reuse can impose network-source obligations. Treat this as conceptual reference only unless the whole project accepts AGPL-compatible licensing.

## Security Risks

- Full paper content enters LLM context.
- Browser insertion can overwrite selected text.
- Current `locate_section` implementation is marked TODO, so do not assume it is complete.

## Proposed Integration

- Implement independent LaTeX section indexer.
- Implement patch-based revision and dry-run mode.
- Add a `review report -> patch -> user approval -> write` lifecycle.

## Minimal Prototype

`paper-writing review --section Introduction --dry-run` prints a report and a unified diff without writing files.

## Open Questions

- How much Overleaf interoperability is needed before v0.2.
- Whether to produce a browser extension later or stay CLI-first.

## Final Decision

- [x] Conceptual reference only

