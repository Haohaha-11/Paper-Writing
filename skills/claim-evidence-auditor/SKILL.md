# Claim Evidence Auditor

## Purpose

Check whether the paper's claims are backed by evidence. This skill protects the manuscript from overclaiming, hallucinated citations, unsupported novelty, and reviewer objections that the paper does not prove what it promises.

## When To Use

- Before finalizing the abstract and introduction.
- Before pre-submission review.
- After adding new results or changing claims.
- Before rebuttal, to separate defensible claims from claims that should be softened.

## Inputs

Required:

- title, abstract, introduction, and conclusion;
- contribution list;
- results, figures, tables, theorems, or validation evidence;
- bibliography or citation notes;
- target venue.

Optional:

- novelty-scout report;
- reviewer comments;
- experiment logs;
- appendix material.

## Claim Types

- Novelty: first, new, novel, unexplored, previously unstudied.
- Performance: better, state-of-the-art, improves, outperforms.
- Efficiency: faster, smaller, cheaper, scalable.
- Robustness/generalization: robust, transferable, works across domains.
- Clinical/practical utility: clinically useful, deployable, reliable, expert-level.
- Theoretical: guarantees, bounds, convergence, optimality.
- Reproducibility: open-source, easy to reproduce, standardized.
- Causal/mechanistic: because, due to, explains, demonstrates mechanism.

## Evidence Types

| Evidence | Examples | Strength Notes |
|---|---|---|
| Direct result | table, figure, metric, ablation | Strong when protocol is clear |
| Citation | inspected paper supporting local sentence | Strong only if citation support is verified |
| Derivation/theorem | proof, bound, formal argument | Strong only if assumptions are stated |
| Dataset/protocol | benchmark, cohort, split, validation setup | Supports scope, not necessarily performance |
| Qualitative example | image, case study, visualization | Usually partial evidence |
| Assumption | stated condition or scope limit | Valid only when claim is scoped |

## Procedure

1. Extract strong claims.
   Focus on title, abstract, introduction, contribution bullets, results, conclusion, and limitation-sensitive language.

2. Normalize each claim.
   Rewrite the claim as a testable proposition: "The paper claims X under condition Y."

3. Assign claim type.
   Use the claim taxonomy above.

4. Link evidence.
   Find exact figure/table/result/citation/proof/assumption supporting the claim.

5. Rate evidence strength.
   Use: strong, partial, missing, contradicted, unverifiable.

6. Recommend action.
   Keep, weaken, move to future work, add evidence, add citation, add caveat, or remove.

7. Check venue-sensitive claims.
   For TMI, clinical claims need validation scope. For ML/CV conferences, SOTA/generalization claims need recent baselines and ablations.

## Rubric

| Rating | Meaning | Required Action |
|---|---|---|
| Strong | Claim directly supported by evidence in the paper | Keep, maybe clarify scope |
| Partial | Evidence supports part of the claim | Weaken or add missing evidence |
| Missing | No evidence found | Remove or mark as future work |
| Contradicted | Evidence conflicts with claim | Rewrite urgently |
| Unverifiable | Evidence may exist but was not provided | Ask user for source or mark unchecked |

## Venue Adaptation

- ICLR/NeurIPS/ICML: scrutinize novelty, generalization, ablations, theoretical assumptions, and reproducibility claims.
- CVPR/ECCV: scrutinize visual-quality claims, dataset diversity, baseline recency, and qualitative/quantitative agreement.
- AAAI: scrutinize broad AI significance claims and AI-generated-text policy compliance.
- TMI: scrutinize clinical utility, validation protocol, patient/privacy/IRB language, external validation, and generalization claims.
- arXiv: mark unchecked public-version claims and ensure anonymous-review claims are not accidentally preserved.

## Output Contract

Use `skills/claim-evidence-auditor/output-format.md`.

Minimum output:

```text
Summary:
High-risk claims:
Claim-evidence matrix:
Claims to weaken:
Claims to remove:
Evidence to add:
Citation support to verify:
Residual risks:
```

## Common Failure Modes

- Treating future work as completed evidence.
- Treating anecdotal examples as benchmark evidence.
- Treating search relevance as novelty proof.
- Allowing "robust" without stress tests or domain-shift evidence.
- Allowing "clinical utility" without clinical validation scope.
- Allowing "state-of-the-art" without current baselines.

## Mini Example

Claim:

```text
Our method is robust across imaging protocols.
```

Audit:

```text
Type: robustness/generalization
Evidence found: single-center MRI dataset with one acquisition protocol
Strength: missing
Action: weaken to "performs consistently across the internal test split" or add multi-protocol/external validation.
```

## Sources Reviewed

Original synthesis based on claim-evidence workflows, reviewer simulation patterns, cspapers novelty checks, and TMI medical-imaging constraints in this repository.
