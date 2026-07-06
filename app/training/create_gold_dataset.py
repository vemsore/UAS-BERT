"""
=========================================================
CREATE GOLD DATASET

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

import json
import pandas as pd
from pathlib import Path

# =========================================================
# PATH
# =========================================================

ROOT = Path(__file__).resolve().parents[2]

assistant_csv = ROOT / "dataset" / "assistant" / "dataset_assistant_2313500122.csv"

review_json = ROOT / "review" / "data" / "review_progress.json"

gold_csv = ROOT / "dataset" / "gold" / "dataset_gold_2313500122.csv"

gold_csv.parent.mkdir(parents=True, exist_ok=True)

# =========================================================
# LOAD DATA
# =========================================================

print("=" * 60)
print("CREATE GOLD DATASET")
print("=" * 60)

df = pd.read_csv(assistant_csv)

print(f"Dataset Assistant : {len(df)}")

# =========================================================
# LOAD REVIEW
# =========================================================

if review_json.exists():

    with open(review_json, "r", encoding="utf-8") as f:

        review = json.load(f)

    review = review.get("review", {})

else:

    review = {}

print(f"Review Manual : {len(review)}")

# =========================================================
# FINAL LABEL
# =========================================================

labels = []

for i, row in df.iterrows():

    idx = str(i)

    if idx in review:

        labels.append(review[idx]["label"])

    else:

        labels.append(row["suggestion"])

df["label"] = labels

# =========================================================
# SAVE
# =========================================================

df.to_csv(gold_csv, index=False, encoding="utf-8-sig")

print("=" * 60)
print("DATASET GOLD")
print("=" * 60)

print(df["label"].value_counts())

print()

print(f"Saved : {gold_csv}")