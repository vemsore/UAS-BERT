"""
TEST DATASET LOADER
"""

from pathlib import Path

from app.training.dataset_loader import (
    SentimentDataset,
    load_dataframe
)

ROOT = Path(__file__).resolve().parents[2]

TRAIN = ROOT / "dataset" / "split" / "train.csv"

print("=" * 60)
print("TEST DATASET LOADER")
print("=" * 60)

df = load_dataframe(TRAIN)

print("Jumlah Data :", len(df))

dataset = SentimentDataset(df)

print()

print("Sample")

sample = dataset[0]

for key, value in sample.items():

    print(key)

    print(value)

    print()