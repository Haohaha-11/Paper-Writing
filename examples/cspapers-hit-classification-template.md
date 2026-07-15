# cspapers Hit Classification Template

| Query | Hit Title | Venue | Year | Score | Abstract Checked | Class | Draft Citation Status | Action |
|---|---|---:|---:|---:|---|---|---|---|
|  |  |  |  |  | yes/no | direct overlap / same task / same method / same dataset / missing baseline / related work / role model | cited / missing / not needed | cite / compare / inspect full paper / ignore |

## Classification Rules

- Direct overlap: title/abstract suggests the same problem and substantially similar method or claim.
- Same task: same benchmark or task, but method differs.
- Same method: similar technique applied to different task.
- Same dataset: uses central dataset or benchmark relevant to evaluation.
- Missing baseline: likely should appear in experiments.
- Related work: useful context but not a direct competitor.
- Role model: strong target-venue paper to emulate structurally or rhetorically.

## Reviewer Objection Template

```text
The draft may understate related work around <topic>. cspapers query <query> retrieved <paper> (<venue> <year>), whose title/abstract suggests <overlap>. The paper should cite, compare, or explicitly distinguish this work before making the claim <claim>.
```
