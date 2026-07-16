# Discussion Writer

## Purpose

Write or revise a Discussion section that interprets results, explains practical meaning, connects limitations to evidence, and avoids overstating conclusions.

## When To Use

Use this skill when a venue or journal expects a distinct Discussion section, or when Results, Limitations, and Conclusion are too compressed to explain what the findings mean.

## Inputs

- Paper context and target venue.
- Main result tables and figures.
- Claim-evidence matrix.
- Limitations and ethics notes.
- Reviewer or redteam concerns if available.

## Procedure

1. Identify the two or three findings that need interpretation beyond raw numbers.
2. For each finding, state what changed, why it may have changed, and what evidence supports that interpretation.
3. Separate measured results from hypotheses about mechanism.
4. Connect negative, mixed, or boundary-case results to limitations.
5. State practical implications only within the study design.
6. Add a paragraph on generalization boundaries when the work involves datasets, populations, deployment settings, or clinical/real-world use.
7. Remove claims that repeat the abstract without adding interpretation.

## Rubric

- Every interpretation is tied to a result, ablation, citation, or stated assumption.
- The section explains implications without creating new unsupported claims.
- Failure cases and limitations are treated as part of the argument, not as a disclaimer.
- The section is distinct from Results and Conclusion.
- Clinical, safety, fairness, privacy, and deployment implications are bounded by evidence.

## Venue Adaptation

- ICLR/NeurIPS/ICML: discussion may be folded into Results, Limitations, or Conclusion if space is tight.
- CVPR/ECCV: prioritize visual failure cases, robustness, and dataset shift.
- AAAI: connect implications to broader AI context and responsible use when relevant.
- IEEE TMI: be explicit about clinical scope, validation limits, privacy, and external validity.
- arXiv: preserve venue-specific discussion unless preparing a shortened technical report.

## Output Contract

Return:

- proposed discussion outline;
- finding-to-interpretation table;
- unsupported interpretation list;
- revised paragraphs or patch suggestions;
- limitations that should move to or from the Discussion section;
- residual author decisions.

## Common Failure Modes

- Repeating Results without interpretation.
- Turning speculation into a claim.
- Hiding weak evidence behind vague language.
- Making deployment or clinical claims from offline experiments.
- Adding limitations that contradict the abstract or contributions.

## Mini Example

Weak: "Our method performs better because it learns better features."

Better: "The largest gains appear in the low-label setting, which is consistent with the prototype uncertainty objective reducing overconfident assignments. This interpretation is supported by the calibration ablation, but not yet by a direct representation analysis."

## Sources Reviewed

- Existing project skills in `skills/`.
- Research notes in `docs/writing-skills-research.md`.
- Venue-facing expectations recorded under `venues/`.
