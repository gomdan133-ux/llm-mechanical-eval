# Findings

> Fill this in after grading. It's the part reviewers read most, so write it like a short report.

## Summary

- Models tested: ChatGPT (version: ___), Claude (version: ___), Gemini (version: ___)
- Date tested: ___
- Best overall: ___ (avg ___ / 10)

## Failure patterns

Write one short section per pattern you saw, with the question IDs as evidence. Things to look for:

- **Unit handling**: did a model mix up lb-ft and N·m, or forget mph to m/s? (Q02, Q06, Q07)
- **Absolute vs gauge**: did it use gauge pressure in the gas law? (Q12)
- **Double counting / missing factors**: double shear, 2 revs per cycle, clearance volume (Q08, Q17, Q19)
- **Safety-critical advice**: TTY bolts, brake fluid types (Q10, Q16)
- **Confident but wrong**: answers with no hedging that were wrong

## Example

> **Q__ – model __**: The model said ___. The correct answer is ___ because ___. In a shop this mistake would lead to ___.

## What I'd change in training data

Two or three concrete suggestions, for example "more examples that make the model state absolute vs gauge pressure explicitly".
