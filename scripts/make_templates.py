"""Create the response files and grades.csv template.

Usage:
    python scripts/make_templates.py chatgpt claude gemini
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = json.loads((ROOT / "questions" / "questions.json").read_text(encoding="utf-8"))
CRITERIA = ["correctness", "units", "reasoning", "assumptions", "safety"]


def main(models):
    for model in models:
        out = ROOT / "model_responses" / f"{model}.md"
        if out.exists():
            print(f"skip {out.name} (exists)")
            continue
        lines = [f"# {model} responses\n",
                 "Paste each answer exactly as the model gave it. Use a new chat for each question.\n"]
        for q in QUESTIONS:
            lines += [f"\n## {q['id']}\n", f"**Prompt:** {q['question']}\n", "**Response:**\n", "\n"]
        out.write_text("".join(lines), encoding="utf-8")
        print(f"created {out.relative_to(ROOT)}")

    grades = ROOT / "grades.csv"
    if grades.exists():
        print("skip grades.csv (exists)")
        return
    with grades.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "topic", "model", *CRITERIA, "flag", "notes"])
        for model in models:
            for q in QUESTIONS:
                w.writerow([q["id"], q["topic"], model, *[""] * len(CRITERIA), "", ""])
    print(f"created grades.csv ({len(models) * len(QUESTIONS)} rows)")


if __name__ == "__main__":
    main(sys.argv[1:] or ["chatgpt", "claude", "gemini"])
