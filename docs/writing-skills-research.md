# Writing Skills Research

Last checked: 2026-07-15

This pass focuses on writing-oriented skills and agents, not LaTeX compilation or venue template handling. The goal is to decide what writing skills `Paper-Writing-Hao` should implement as project-owned skills.

## Bottom Line

Yes, the writing-skill ecosystem is worth searching and distilling. It fills a major gap in the original repository list.

The strongest pattern across current projects is not "one giant paper writer." The better architecture is a skill stack:

1. strategy skill: paper positioning, contribution map, novelty and evidence plan;
2. section-writing skills: abstract, introduction, related work, method, experiments, results, discussion, conclusion, limitations, ethics, appendix;
3. evidence/citation skill: claim-evidence matrix and citation verification;
4. review skill: simulated reviewer/AC, flaw prioritization, rebuttal planning;
5. polishing skill: clarity, compression, terminology consistency, LaTeX-preserving edits;
6. venue adapter: ICLR/NeurIPS/CVPR/ICML/ECCV/AAAI/TMI/arXiv-specific constraints.

Do not copy third-party prompt text into this repo unless its license and upstream provenance are both clear. Prefer distilling workflow ideas into our own skills.

## Candidate Projects

| Project | License | Fit | What to learn | Decision |
|---|---|---:|---|---|
| `Master-cai/Research-Paper-Writing-Skills` | MIT | 5 | ML/CV/NLP section writing, claim-evidence alignment, self-review, paper-section workflows. | High-value reference; preserve attribution if reusing any MIT text, but better to reimplement. |
| `lishix520/academic-paper-skills` | MIT | 4 | Strategist/composer split, staged planning, gap validation, reviewer scoring, quality gates. | Strong architecture reference; adapt to ML/medical imaging venues. |
| `zLanqing/codex-claude-academic-skills` | MIT | 5 | Chinese-first academic workflow, research-writing plus office/report plus scientific toolkit, no-fabrication rules, info-source categorization. | Very useful for Chinese-user UX and source-grounding rules. |
| `SNL-UCSB/paper-writing-skill` | MIT | 4 | Rhetorical moves, five-stage writing pipeline, compression, figure synthesis, red-team protocol. | Good for section and figure skills; domain-specific parts should be generalized. |
| `yunshenwuchuxun/latex-paper-skills` | MIT | 5 | Topic-to-PDF workflow, LaTeX-aware skill layout, citation verification, issue CSV contract, empirical/review paper split. | Closest to this project's target shape; use as conceptual architecture reference. |
| `xf686/Meet-Reviewer-2` | MIT | 4 | Reviewer-panel simulation, AC meta-review, line-grounded fix list, impact x effort prioritization. | Good model for pre-submission red-team skill. |
| `google-research/paper-orchestra` | Apache-2.0 | 4 | Multi-agent paper generation from raw materials, outline/literature/section/refinement/plotting roles, LaTeX output. | Useful pipeline reference; do not make v0.1 depend on it. |
| `Future-House/paper-qa` | Apache-2.0 | 5 | Scientific-document RAG with citations, contradiction detection, document indexing. | Candidate optional dependency for evidence/citation-grounded writing. |
| `stanford-oval/storm` | MIT | 3 | Pre-writing research, outline generation, multi-perspective question asking, cited report generation. | Useful for related-work and background drafting, not for submission-ready papers. |
| `assafelovic/gpt-researcher` | Apache-2.0 | 3 | Deep research reports with citations, web/local research agent design, domain customization. | Useful for literature-search workflow, not a paper-writing core. |
| `Agents4Academia-AI/auto-reviewer` | MIT | 3 | Claim/evidence maps, novelty/rigor checks, self-critique pipeline. | Watch/evaluate; low maturity but aligned with review skill. |
| `swkim101/cspapers.org` | MIT | 4 | Fast CS conference paper search by query, year range, and venue; open API; title/abstract index from Semantic Scholar. | Useful backend/source for novelty, related-work, and role-model-paper review; not a standalone full-paper reviewer. |

## Excluded Or Caution Areas

Some searched projects focus on "humanizer", "anti-AI detector", or "de-AIGC" behavior. Do not make detector evasion a product feature. A legitimate polishing skill should improve clarity, specificity, citation grounding, compression, and author voice while preserving factual claims and LaTeX.

Also avoid importing skills whose licenses are missing, unclear, or whose upstream source material has unclear redistribution rights.

## Recommended Skill Taxonomy

### Core Writing

- `paper-strategist`: converts idea + results + target venue into claim map, contribution bullets, reader promise, and section plan.
- `abstract-writer`: writes/rewrites abstract under venue length/style constraints; checks problem, gap, method, result, implication.
- `introduction-writer`: builds motivation, gap, key insight, contribution list, and evidence preview.
- `related-work-writer`: citation-grounded taxonomy, contrastive positioning, no strawman claims.
- `method-writer`: notation, problem formulation, algorithm description, assumptions, complexity, implementation details.
- `experiments-writer`: dataset/protocol/baseline/metric/ablation/significance structure.
- `results-writer`: converts verified numbers and figures into claims; refuses unsupported performance claims.
- `limitations-ethics-writer`: venue-specific limitations, broader impact, ethics, reproducibility, clinical caveats for TMI.
- `conclusion-writer`: compresses contribution and scope without adding new claims.

### Review And Revision

- `paper-redteam`: simulated R1/R2/R3/AC review with line-grounded weaknesses and impact x effort fixes.
- `novelty-scout`: searches target-venue and adjacent-venue papers for title/abstract-level overlap, missing baselines, related-work gaps, and role-model papers.
- `rebuttal-planner`: maps reviewer comments to response strategy, evidence needed, experiments to add, and wording constraints.
- `revision-editor`: applies scoped LaTeX patches, preserves citations/labels/equations, and emits a change log.
- `page-compressor`: reduces length while preserving claims, citations, equations, and venue-required sections.

### Evidence And Citation

- `claim-evidence-auditor`: every major claim must link to a result, citation, derivation, or stated assumption.
- `citation-context-checker`: verifies that cited papers support the local sentence and are not used as generic placeholders.
- `literature-matrix-builder`: builds a comparison table by problem, method, dataset, metric, limitation, and relation to this paper.
- `bibtex-metadata-checker`: detects missing fields, duplicate keys, suspicious venues, and uncited references.

### Venue Adapters

- `venue-iclr`, `venue-neurips`, `venue-cvpr`, `venue-icml`, `venue-eccv`, `venue-aaai`, `venue-tmi`, `venue-arxiv`.
- Each adapter should provide page/checklist constraints, section expectations, anonymity rules, disclosure rules, and phrase-level style warnings.
- TMI needs additional medical-imaging checks for clinical relevance, dataset provenance, consent/IRB/privacy language, validation protocol, and challenge-paper reporting.

## v0.1 Skill Build Order

1. `paper-strategist`
2. `abstract-writer`
3. `introduction-writer`
4. `claim-evidence-auditor`
5. `paper-redteam`
6. `novelty-scout`
7. `page-compressor`
8. `venue-iclr`
9. `venue-cvpr`
10. `venue-tmi`

This covers the highest-value author workflow before implementing every section and every venue.

## cspapers Review-Rule Note

The public `swkim101/cspapers.org` repository does not expose full-paper review rules. It exposes a title/abstract search engine and API, which can support review rules in this project.

Use it as the retrieval backend for `novelty-scout` and `related-work-auditor`:

- search draft title, abstract claims, method keywords, datasets, and baselines;
- compare against target and adjacent venues;
- flag missing recent related work;
- flag novelty risks for "first", "novel", "state-of-the-art", and similar claims;
- produce role-model papers and candidate baselines.

Do not treat cspapers relevance `score` as an accept/reject score. It is retrieval evidence only.

See `docs/cspapers-integration.md`.

## Sources

- Research Paper Writing Skills: https://github.com/Master-cai/Research-Paper-Writing-Skills
- Academic Paper Skills: https://github.com/lishix520/academic-paper-skills
- Codex/Claude Academic Skills: https://github.com/zLanqing/codex-claude-academic-skills
- SNL-UCSB paper-writing-skill: https://github.com/SNL-UCSB/paper-writing-skill
- latex-paper-skills: https://github.com/yunshenwuchuxun/latex-paper-skills
- Meet Reviewer 2: https://github.com/xf686/Meet-Reviewer-2
- PaperOrchestra: https://github.com/google-research/paper-orchestra
- PaperQA2: https://github.com/Future-House/paper-qa
- STORM: https://github.com/stanford-oval/storm
- GPT Researcher: https://github.com/assafelovic/gpt-researcher
- Auto Reviewer: https://github.com/Agents4Academia-AI/auto-reviewer
- cspapers.org: https://github.com/swkim101/cspapers.org
