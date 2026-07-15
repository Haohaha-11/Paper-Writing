# Claim Evidence Matrix: Synthetic Example

| Claim | Location | Type | Evidence | Strength | Risk | Action |
|---|---|---|---|---|---|---|
| Diffusion-mask sampling improves calibration under synthetic annotator disagreement. | Abstract, Contributions | performance | Synthetic ECE comparison against deterministic and ensemble baselines. | partial | medium | State "synthetic benchmark" explicitly; avoid real clinical claims. |
| The method models multiple plausible lesion boundaries. | Introduction, Method | mechanistic | Decoder samples multiple masks conditioned on image and noise seed. | strong | low | Keep, but define "plausible" through evaluation protocol. |
| The approach is useful for clinical segmentation. | Draft conclusion | clinical/practical utility | No clinical validation or reader study. | missing | high | Remove or weaken to "may motivate future clinical validation." |
| The paper is the first to use diffusion for ambiguous medical segmentation. | Draft abstract | novelty | Novelty-scout finds likely related CVPR 2023 title/abstract overlap. | contradicted | high | Remove "first"; cite and distinguish related work after full-paper inspection. |
| The synthetic dataset avoids patient privacy risk. | Ethics note | ethics/privacy | Dataset generation is synthetic and contains no patient data. | strong | low | Keep, mention synthetic-only limitation. |

## Summary

- Strong claims: 2
- Partial claims: 1
- Missing or contradicted claims: 2

## Required Changes

- Remove "clinical utility" language.
- Remove or heavily narrow "first diffusion method" claim.
- Add explicit synthetic-data scope to abstract and introduction.
- Add full-paper inspection for retrieved diffusion segmentation papers.
