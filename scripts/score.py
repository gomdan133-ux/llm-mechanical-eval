"""Summarize grades.csv into per-model and per-topic scores.

Usage:
    python scripts/score.py            # prints a summary
    python scripts/score.py --md       # also writes results.md
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CRITERIA = ["correctness", "units", "reasoning", "assumptions", "safety"]
MAX = 2 * len(CRITERIA)


def load():
    rows = []
    with (ROOT / "grades.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if any(r[c].strip() == "" for c in CRITERIA):
                continue  # not graded yet
            for c in CRITERIA:
                v = int(r[c])
                if v not in (0, 1, 2):
                    raise ValueError(f"{r['question_id']}/{r['model']}: {c}={v} must be 0, 1 or 2")
                r[c] = v
            r["total"] = sum(r[c] for c in CRITERIA)
            rows.append(r)
    return rows


def summarize(rows):
    by_model = defaultdict(list)
    by_topic = defaultdict(lambda: defaultdict(list))
    flags = defaultdict(lambda: defaultdict(int))
    for r in rows:
        by_model[r["model"]].append(r)
        by_topic[r["topic"]][r["model"]].append(r["total"])
        if r["flag"].strip():
            flags[r["model"]][r["flag"].strip()] += 1

    out = ["# Results\n", f"Graded responses: {len(rows)}\n",
           "\n## Overall\n", "| Model | Questions | Avg score (/10) | " +
           " | ".join(c.title() for c in CRITERIA) + " | Flags |",
           "|---" * (4 + len(CRITERIA)) + "|"]
    for model, rs in sorted(by_model.items()):
        avg = sum(r["total"] for r in rs) / len(rs)
        crit = [f"{sum(r[c] for r in rs) / len(rs):.2f}" for c in CRITERIA]
        fl = ", ".join(f"{k}: {v}" for k, v in flags[model].items()) or "-"
        out.append(f"| {model} | {len(rs)} | {avg:.2f} | " + " | ".join(crit) + f" | {fl} |")

    models = sorted(by_model)
    out += ["\n## By topic (avg /10)\n", "| Topic | " + " | ".join(models) + " |",
            "|---" * (1 + len(models)) + "|"]
    for topic in sorted(by_topic):
        cells = []
        for m in models:
            s = by_topic[topic].get(m)
            cells.append(f"{sum(s) / len(s):.1f}" if s else "-")
        out.append(f"| {topic} | " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


def main():
    rows = load()
    if not rows:
        print("No graded rows yet. Fill in grades.csv (0/1/2 per criterion) first.")
        return
    report = summarize(rows)
    print(report)
    if "--md" in sys.argv:
        (ROOT / "results.md").write_text(report, encoding="utf-8")
        print("wrote results.md")


if __name__ == "__main__":
    main()
