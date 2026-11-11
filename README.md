# LLM Mechanical Engineering Eval

A small benchmark for checking how well large language models handle **applied mechanical and automotive engineering** problems: gears, hydraulics, fasteners, thermal expansion, vehicle dynamics, engines and brakes.

It has 20 questions with reference answers, a 5-part grading rubric, and scripts to collect responses and score them. It was built the way AI-trainer evaluation work is done: clear prompts, a fixed rubric, documented common errors, and severity flags for unsafe advice.

## What's inside

```
questions/questions.json   20 questions with reference answers, key values and common errors
rubric.md                  0-2 scoring on correctness, units, reasoning, assumptions, safety
model_responses/           one markdown file per model (paste responses here)
grades.csv                 one row per question per model
scripts/make_templates.py  creates the response files and grades.csv
scripts/score.py           averages by model, by criterion and by topic
findings.md                write-up of failure patterns
```

## How to run an evaluation

```bash
# 1. Create the templates for the models you want to test
python scripts/make_templates.py chatgpt claude gemini

# 2. Ask each model every question (new chat per question, no system prompt),
#    and paste the answers into model_responses/<model>.md

# 3. Grade each response with rubric.md and fill in grades.csv

# 4. Score it
python scripts/score.py --md      # prints the tables and writes results.md

# 5. Write up the patterns in findings.md
```

## Question topics

Gears, unit conversion, hydraulics, thermal expansion, fastener preload, stopping distance, engine power, compression ratio, voltage drop, TTY bolts, lug nut torque pattern, gas laws (tire pressure), springs, belt speed, pedal ratio, brake fluid compatibility, shear stress, factor of safety, injector duty cycle, hydraulic jack.

Each question lists the **common errors** to check for, for example using gauge pressure instead of absolute in the tire pressure question, or single shear instead of double shear.

## Why these questions

They're chosen to catch the mistakes that matter in practice: unit slips, missing factors of 2, and confident-sounding advice that would be unsafe in a shop. That's why the rubric includes a safety criterion and a `CRITICAL` flag.

## Results (Nov 10, 2026)

| Model | Avg score (/10) | Wrong final answers |
|---|---|---|
| Claude (Opus 5.5) | 10.00 | 0 |
| ChatGPT (free, default) | 9.90 | 0 |
| Gemini (free, automatic) | 9.85 | 0 |

All three models got every final answer right. The small score differences come from caveats, consistency and shop judgment. For example, one model called a 0.6 V starter cable drop "close to acceptable", and another showed a widget that contradicted its own written answer. The main takeaway is that this question set is too easy for current models, and version 2 needs harder multi-step and judgment questions. See [`findings.md`](findings.md) for the full write-up and [`results.md`](results.md) for the tables.

## How this was built

1. **Wrote the questions.** I picked 20 problems from day-to-day automotive and mechanical work (gears, hydraulics, fasteners, brakes, engines, electrical, materials). Each one has a worked reference answer, key values, and the mistakes it's designed to catch.
2. **Designed the rubric.** Five criteria (correctness, units, reasoning, assumptions, safety) scored 0–2, plus severity flags for unsafe or made-up answers.
3. **Wrote the tooling.** `make_templates.py` builds the response files and grading sheet, and `score.py` averages the scores by model, criterion and topic and writes `results.md`.
4. **Collected the answers.** On Nov 10, 2026, I sent the questions to ChatGPT, Claude and Gemini through their web apps, in two batches of 10, each in a new chat with no system prompt. The answers are saved in `model_responses/`.
5. **Graded.** I scored every answer against the reference and the rubric, with a one-line note for each deduction in `grades.csv`.
6. **Scored and wrote it up.** I ran `score.py --md` and wrote up the failure patterns, limitations and version 2 ideas in `findings.md`.

**Limitations:** one run per model, batched prompts, and consumer apps with default settings. The grading was AI-assisted, using one of the tested models, so every deduction is written out to be checked. Details are in `findings.md`.

## Author

Daniel Gomez – ASE-certified (Brakes) mobile mechanic and AI data annotator, Miami, FL.

## License

MIT
