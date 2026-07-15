# Skill Output Contracts

All skills must return structured output. Free-form prose is allowed only after the required fields.

## Report Contract

```text
Skill:
Input scope:
Target venue:
Summary:
Findings:
Evidence gaps:
Recommended changes:
Patch suggestions:
Residual risks:
Sources checked:
```

## Patch Suggestion Contract

```text
Target file:
Target section:
Current issue:
Replacement text:
Reason:
Evidence dependency:
LaTeX safety notes:
```

## Review Contract

```text
Reviewer role:
Decision-critical concerns:
Major weaknesses:
Minor weaknesses:
Questions for authors:
Required fixes:
Nice-to-have fixes:
Risk after fixes:
```

## Claim-Evidence Contract

Use `examples/claim-evidence-matrix-template.md`.

## Rebuttal Contract

Use `examples/rebuttal-response-template.md`.

## Required Source Notes

If a skill uses external search, venue rules, or template information, it must list the files and URLs checked. If a fact was not checked, label it as unchecked.
