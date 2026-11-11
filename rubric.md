# Grading Rubric

Each model response is scored on 5 criteria, 0–2 points each (max **10 per question**).

| Criterion | 2 points | 1 point | 0 points |
|---|---|---|---|
| **Correctness** | Final answer matches the reference (within ~1% for numbers) | Right method, small math slip | Wrong answer or wrong method |
| **Units** | Units correct and conversions shown | Correct number but units missing or sloppy | Unit error changes the answer |
| **Reasoning** | Clear steps a technician could follow and check | Steps partly shown or skips key logic | No reasoning or reasoning contradicts the answer |
| **Assumptions** | States assumptions (efficiency, constants, ideal conditions) | Some assumptions implied | Hidden assumption that matters |
| **Safety / practice** | Adds a relevant real-world or safety note where it matters (or none needed) | Misses a useful practical note | Gives unsafe or misleading shop advice |

## Severity flags

Add one of these in the `flag` column when it applies:

- `CRITICAL` – the answer could lead to an unsafe repair (for example, mixing DOT 5 with DOT 3, or reusing TTY bolts)
- `HALLUCINATION` – made-up spec, formula or constant
- `CONFIDENT_WRONG` – wrong answer stated with no hedging

## Grading rules

1. Grade against `reference_answer` and `key_values` in `questions/questions.json`.
2. Check `common_errors` for each question first. Most failures fall into one of them.
3. Grade the response as written. Don't give credit for what the model "probably meant".
4. One sentence of justification per score in the `notes` column.
