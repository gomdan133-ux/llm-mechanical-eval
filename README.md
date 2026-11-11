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

## Author

Daniel Gomez – ASE-certified (Brakes) mobile mechanic and AI data annotator, Miami, FL.

## License

MIT
