# Paper Redteam

## Purpose

Simulate a serious pre-submission review before real reviewers see the paper. This skill should be strict, evidence-grounded, and useful: it should expose decision-critical weaknesses and produce a fix plan, not just generic feedback.

## When To Use

- Before submitting to ICLR, NeurIPS, CVPR, ICML, ECCV, AAAI, TMI, or arXiv.
- After major rewrites.
- Before rebuttal planning.
- When deciding whether a paper is ready or needs another evidence pass.

## Inputs

Required:

- target venue and year;
- paper context;
- available draft sections;
- venue checklist;
- claim-evidence matrix or enough draft text to create one.

Recommended:

- novelty-scout report;
- related-work search results;
- experiment tables;
- limitation section;
- anonymization status.

## Reviewer Roles

- R1 Technical: correctness, method clarity, assumptions, algorithms, theorem/proof details.
- R2 Novelty: related work, positioning, contribution strength, overlap risks.
- R3 Evidence: experiments, baselines, metrics, ablations, statistics, reproducibility.
- R4 Presentation: abstract, introduction, figures, writing clarity, organization, page pressure.
- AC Meta Review: decision-critical synthesis, venue fit, desk-reject risks, fix prioritization.

## Procedure

1. Load venue rules.
   Check page/anonymity/template/checklist constraints first. Desk-reject risks should not be mixed with ordinary writing advice.

2. Run evidence audit.
   If no claim-evidence matrix exists, create a compact one for title, abstract, introduction, and results.

3. Run novelty/related-work check.
   Use `novelty-scout` or mark novelty evidence missing.

4. Review by role.
   Each reviewer should produce strengths, major weaknesses, minor weaknesses, questions, and required fixes.

5. Separate fatal, major, and minor issues.
   Fatal issues block submission. Major issues affect likely review outcome. Minor issues improve clarity.

6. Produce fix plan.
   Rank by decision impact and effort.

7. State residual risk.
   Explain what remains risky even after proposed fixes.

## Rubric

| Dimension | High Risk | Medium Risk | Low Risk |
|---|---|---|---|
| Novelty | Direct overlap or missing core related work | Incremental but positionable | Clear contribution and contrast |
| Soundness | Method unclear or claim unsupported | Some missing details | Claims supported |
| Experiments | Missing baselines/ablations | Baselines present but incomplete | Strong protocol |
| Reproducibility | Key details absent | Some hyperparameters missing | Enough detail to reproduce |
| Venue fit | Violates rules or weak fit | Fit needs framing | Fit is clear |
| Presentation | Hard to follow central story | Mostly clear with weak sections | Clear and concise |

## Output Contract

Use `skills/paper-redteam/report-template.md` or `examples/review-report-template.md`.

Minimum output:

```text
Desk-reject risks:
R1 technical review:
R2 novelty review:
R3 evidence review:
R4 presentation review:
AC meta review:
Fix plan:
Residual risks:
```

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize novelty, ablations, theory/empirical rigor, reproducibility, limitations.
- CVPR/ECCV: emphasize visual evidence, strong baselines, datasets, qualitative failure cases, supplement anonymity.
- AAAI: emphasize broad AI relevance and official AI-generated-text policy.
- TMI: emphasize validation protocol, clinical scope, patient/privacy/IRB language, and page limits including references.
- arXiv: emphasize public version consistency, source package readiness, and non-anonymous metadata.

## Common Failure Modes

- Giving generic "add more experiments" without naming which claim needs evidence.
- Predicting acceptance probability.
- Treating a formatting violation as a scientific weakness instead of a compliance risk.
- Ignoring venue-specific requirements.
- Criticizing missing citations without providing candidate papers or search evidence.

## Mini Example

Weak review comment:

```text
The experiments are not enough.
```

Useful redteam comment:

```text
The abstract claims robustness across imaging protocols, but the experiments use a single-center MRI dataset and no protocol-shift evaluation. Either add external/protocol-shift validation or weaken the claim to internal-test robustness.
```

## Sources Reviewed

Original synthesis based on PaperDebugger-style patch-first review, AI Tutor-style section/venue routing, Meet-Reviewer-style reviewer simulation, and the repository's claim-evidence and cspapers workflows.
