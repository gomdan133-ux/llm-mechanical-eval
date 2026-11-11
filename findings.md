# Findings

## Summary

- **Models tested:** ChatGPT (chatgpt.com, Free plan, default model), Claude (claude.ai, Opus 5.5, Medium effort), Gemini (gemini.google.com, free tier, automatic model)
- **Date tested:** Nov 10, 2026
- **Method:** 20 questions sent in two batches of 10, each batch in a new chat, no system prompt. Graded with `rubric.md` (0–2 on 5 criteria, max 10 per question).

| Model | Avg score (/10) | Wrong final answers | Responses with a deduction |
|---|---|---|---|
| Claude | 10.00 | 0 | 0 |
| ChatGPT | 9.90 | 0 | 2 |
| Gemini | 9.85 | 0 | 3 |

Full tables are in [`results.md`](results.md). Every grade has a one-line note in [`grades.csv`](grades.csv).

## Main finding: this question set is too easy for current models

All three models got **all 20 final answers right**, including the questions built to catch common mistakes:

- gauge vs absolute pressure in the tire question (Q12)
- double shear (Q17)
- two revolutions per cycle for the injector (Q19)
- adding clearance volume for compression ratio (Q08)
- DOT 5 vs DOT 5.1 brake fluid (Q16)

None of the `common_errors` listed in `questions.json` showed up. The scores only differ because of **caveats, consistency and practical shop judgment**, not math. To tell models apart, version 2 of this benchmark needs harder questions (see the end of this file).

## Where the models differed

**1. Practical shop judgment (Gemini, Q09).** Gemini worked out the 0.6 V cable drop correctly, but called it "borderline" and "close to acceptable" and didn't say what to do next. Claude and ChatGPT both said it was too high and told the tech to clean, tighten and retest the connections. In a shop, the "close to acceptable" answer could mean a slow-crank complaint goes home unfixed.

**2. Over-absolute safety statements (Gemini, Q10).** Gemini said TTY head bolts "must never be reused". That's safe as a default, but some manufacturers allow reuse after a bolt-length check. Claude named that exception, and ChatGPT pointed the reader to the service manual.

**3. Missing assumptions (Gemini, Q05).** The bolt clamp-load answer was correct, but it didn't mention that the nut factor K changes a lot with lubrication. That caveat matters when the result is used as a real preload.

**4. Internal inconsistency (ChatGPT, Q06).** The written answer was correct (86.05 m). But ChatGPT also put an interactive stopping-distance widget inside the answer, and that widget showed "40.2 + 51.4 = 91.6 m". A reader who looks at the widget sees a different answer than the text gives.

**5. Missing mechanism (ChatGPT, Q11).** It said a star pattern prevents rotor distortion, but didn't explain how: uneven clamping causes lateral runout, which leads to thickness variation and pedal pulsation. Claude explained the full chain and added staged tightening and a re-torque check.

## Example

> **Q09, Gemini:** The model said a 0.6 V drop is "close to acceptable." The usual limit for the positive side of the starting circuit is about 0.5 V, and many shops use 0.2–0.3 V per cable. In a shop, accepting that answer could leave a corroded terminal in place and cause repeat no-crank or slow-crank comebacks.

## Limitations

- **Small sample:** 20 questions, one run per model, no repeats. Answers can change from run to run.
- **Batched prompts:** the questions were asked 10 at a time, not one per chat. That may change how much detail a model gives each answer.
- **Consumer web apps, default settings:** the exact model versions behind ChatGPT and Gemini were not shown.
- **Grader conflict:** the grading was done with help from Claude, one of the models being tested. Every deduction is written out in `grades.csv` so a human can check it, and a second, independent grader is recommended.
- **Responses are condensed:** the files in `model_responses/` keep each final answer and the caveats that affected grading, but drop the math formatting.

## What I'd change for version 2 / training data

1. **Harder, multi-step problems.** Chain calculations together (for example pedal force → line pressure → clamp force → stopping distance) so that one unit slip carries through to the end.
2. **Questions without a single right answer.** Give a vague symptom or missing data and grade whether the model asks for, or states, the assumptions it needs.
3. **More shop-judgment questions.** Ask "is this acceptable and what do you do next?" with real specs. That's where the models actually differed.
4. **Training data note:** reward answers that give the next diagnostic step and name the OEM exceptions, not just a correct number.
