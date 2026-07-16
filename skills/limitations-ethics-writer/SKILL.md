# Limitations Ethics Writer

## Purpose

Draft or revise Limitations, Ethics, Broader Impact, and medical/privacy caveats so that the paper is honest about scope and compliant with venue expectations.

## When To Use

- Before submission to venues requiring limitations, ethics, or reproducibility statements.
- For medical-imaging papers with privacy, consent, IRB, or clinical-scope concerns.
- After claim-evidence auditing identifies overbroad claims.
- Before arXiv release of a public version.

## Inputs

Required:

- target venue;
- claim-evidence matrix;
- datasets and data provenance;
- known failure modes;
- code/data release plan;
- human/clinical/privacy constraints when applicable.

Optional:

- model card or datasheet;
- IRB/consent/de-identification notes;
- compute/resource usage;
- societal impact notes.

## Procedure

1. List claims that require scope limits.
2. Identify dataset, benchmark, demographic, modality, and protocol limitations.
3. Identify evaluation limitations such as missing external validation, reader studies, or deployment testing.
4. State ethical/privacy constraints without revealing anonymous identities.
5. Distinguish limitations from future work.
6. Make the section concrete and concise; avoid generic disclaimers.
7. Ensure Abstract/Conclusion do not contradict the limitations.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Specificity | Names actual limits | Generic "more work needed" |
| Claim alignment | Limits match strong claims | Limitations unrelated to claims |
| Ethics | Data/privacy/consent handled | Ethical issues ignored |
| Honesty | Acknowledges missing validation | Hides core weaknesses |
| Usefulness | Helps reviewers assess scope | Boilerplate only |

## Venue Adaptation

- ICLR/NeurIPS/ICML: include limitations, reproducibility, societal impact, and data/model release caveats where required.
- CVPR/ECCV: discuss dataset bias, visual failure cases, annotation quality, and deployment risks.
- AAAI: comply with AI policy and broader impact expectations.
- TMI: address patient privacy, consent/IRB, de-identification, clinical validation, population/site/scanner generalization, and conference-extension disclosure.
- arXiv: remove anonymous-review-only text and ensure public claims remain scoped.

## Output Contract

Return:

```text
Limitations diagnosis:
Ethics/privacy checklist:
Claims needing caveats:
Draft limitations text:
Draft ethics/broader-impact text:
Contradictions with abstract/conclusion:
Residual risks:
```

## Common Failure Modes

- Treating limitations as future work only.
- Using a generic ethics paragraph that does not mention the actual data.
- Claiming clinical readiness without clinical validation.
- Omitting bias/generalization limits.
- Adding acknowledgments that break anonymity.

## Mini Example

Weak:

```text
Our work has some limitations and more research is needed.
```

Stronger:

```text
Our experiments use synthetic images and therefore do not establish clinical utility. The results test whether diffusion-mask sampling can represent controlled annotator disagreement, but external validation on real multi-reader datasets is required before medical deployment claims are appropriate.
```

## Sources Reviewed

Original synthesis based on TMI notes, venue rules, claim-evidence auditing, and paper-redteam workflows.
