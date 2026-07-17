# Paper-Writing-Hao

GitHub-native paper writing system for authors and AI agents.

This repo helps you move from literature research to a locked research problem, then into drafting, review, revision, and venue-specific polishing for arXiv, ICLR, NeurIPS, CVPR, ICML, ECCV, AAAI, and IEEE TMI.

It is not a one-click paper generator. It is a reusable writing system, review system, and local LaTeX workspace.

## What Is Ready

- Research scouting and problem framing for idea generation.
- Section-writing skills for abstracts, introductions, related work, methods, experiments, results, discussion, limitations, conclusions, appendices, and captions.
- Review skills for claim evidence, novelty, redteam simulation, and revision planning.
- Venue rule folders for ICLR, CVPR, NeurIPS, ICML, ECCV, AAAI, IEEE TMI, and arXiv.
- Imported official template bundles with checksums and import records.
- Local TeX Live compilation and template smoke validation.
- Synthetic examples and walkthroughs.
- Local/private paper project support under `projects/`.

## How To Use

### 1. If you are still looking for an idea

Start with:

1. `workflows/idea-to-paper.md`
2. `skills/research-scout/SKILL.md`
3. `skills/research-problem-framer/SKILL.md`
4. `skills/pre-experiment-planner/SKILL.md`

Use the templates in `examples/` to keep the search, problem selection, and falsification sprint structured.

### 2. If your problem is already locked

Start with:

1. `workflows/draft-to-submission.md`
2. `skills/paper-strategist/SKILL.md`
3. `skills/novelty-scout/SKILL.md`
4. `skills/claim-evidence-auditor/SKILL.md`
5. `skills/paper-redteam/SKILL.md`

### 3. If you have a real paper project

Put it under:

```text
projects/<paper-name>/
```

Compile from that folder with `latexmk`. The resulting PDF will sit next to your main `.tex` file unless you choose a custom output path.

## Local Project Workflow

For a paper project in `projects/my-paper/`:

```bash
cd /Hao/Paper-Writing-Hao/projects/my-paper
latexmk -pdf main.tex
```

Use `scripts/extract_latex_context.py` before asking an agent to inspect or edit the LaTeX tree.

## Repository Map

```text
Paper-Writing-Hao/
  skills/        writing, review, and ideation skills
  workflows/     end-to-end paper workflows
  venues/        official-source venue rules and checklists
  templates/     imported template bundles and provenance
  examples/      synthetic templates and walkthroughs
  projects/      local/private paper projects
  docs/          design notes, distillation notes, and environment docs
```

## Templates And Environment

Imported template files live under `templates/upstream/`.

Important files:

- `templates/import-manifest.json`
- `templates/checksums.sha256`
- `templates/import-records/`
- `templates/compile-validation.md`
- `docs/tex-environment.md`

Useful checks:

```bash
python3 scripts/validate_repo.py
sha256sum -c templates/checksums.sha256
python3 scripts/compile_templates.py --check
```

## Current Limits

- This repo does not provide an Overleaf-style web editor.
- AAAI-26 template import is still pending because the official kit was not accessible from this environment.
- Exact official IEEE/TMI template selector artifacts are still pending; current validation uses TeX Live IEEEtran.

## Safety

- Keep unpublished manuscripts local or in a private repository.
- Do not paste confidential drafts into untrusted services.
- Do not invent citations, datasets, metrics, or venue rules.
- Do not claim venue compliance without checking the official source.
- Do not silently update official templates in existing paper projects.

## Contributing

Contributions are welcome, especially:

- new venue rule files backed by official sources;
- clearer writing skills with explicit output contracts;
- corrected template provenance or checksums;
- synthetic examples that do not reveal unpublished work;
- review workflows for specific paper types.

Please avoid submitting copied third-party prompt text unless the license and provenance are clear.

## License

MIT. See `LICENSE`.

Template files under `templates/upstream/` retain their upstream terms. Check each import record before redistributing or modifying them.
