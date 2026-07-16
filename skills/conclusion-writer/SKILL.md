# Conclusion Writer

## Purpose

Draft or revise a concise conclusion that restates the proven contribution without adding new unsupported claims.

## When To Use

- Finalizing a paper after Results and Limitations are stable.
- Shortening a conclusion for page limits.
- Removing overbroad final claims.
- Preparing a public arXiv version.

## Inputs

Required:

- paper thesis;
- final contribution list;
- main verified results;
- limitations;
- target venue.

Optional:

- abstract;
- introduction contribution bullets;
- reviewer concerns.

## Procedure

1. Restate the problem and contribution in one sentence.
2. Summarize the strongest evidence without repeating detailed numbers unless needed.
3. State the implication within proven scope.
4. Preserve limitations and future work boundaries.
5. Remove new claims, new citations, or new experiments introduced only in the conclusion.
6. Keep it short unless the venue expects a longer discussion.

## Rubric

| Dimension | Strong | Weak |
|---|---|---|
| Closure | Reinforces paper thesis | Starts a new argument |
| Evidence | Mentions verified support | Adds unsupported claims |
| Scope | Matches limitations | Overgeneralizes |
| Brevity | Concise and memorable | Repeats introduction |
| Consistency | Aligns with abstract/results | Contradicts earlier caveats |

## Venue Adaptation

- ICLR/NeurIPS/ICML: emphasize conceptual takeaway and evidence scope.
- CVPR/ECCV: connect method/result to visual task implications.
- AAAI: keep broader AI relevance but avoid unsupported societal claims.
- TMI: avoid clinical deployment language unless validated; emphasize medical-imaging scope.
- arXiv: include public artifact pointers only if ready and allowed.

## Output Contract

Return:

```text
Conclusion diagnosis:
Revised conclusion:
New unsupported claims removed:
Scope caveats preserved:
Optional shorter version:
```

## Common Failure Modes

- Adding "clinical impact" or "real-world deployment" only in conclusion.
- Repeating the abstract nearly verbatim.
- Introducing future work as if it were completed.
- Omitting limitations after strong claims.

## Mini Example

Weak:

```text
Our method will improve clinical segmentation systems.
```

Stronger:

```text
These synthetic experiments suggest that modeling mask distributions can improve calibration under controlled annotator disagreement; validating the same behavior on real multi-reader clinical datasets remains future work.
```

## Sources Reviewed

Original synthesis based on claim-evidence, limitations, and venue-specific writing workflows in this repository.
