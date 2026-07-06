"""
=========================================================
LABEL ENCODER

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

from pathlib import Path

import joblib

import pandas as pd

from sklearn.preprocessing import LabelEncoder

# ==========================================================
# PATH
# ==========================================================

ROOT = Path(__file__).resolve().parents[2]

TRAIN_PATH = ROOT / "dataset" / "split" / "train.csv"

VALID_PATH = ROOT / "dataset" / "split" / "valid.csv"

TEST_PATH = ROOT / "dataset" / "split" / "test.csv"

MODEL_DIR = ROOT / "model"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

# ==========================================================
# LOAD DATASET
# ==========================================================

print("=" * 60)
print("LABEL ENCODER")
print("=" * 60)

train_df = pd.read_csv(TRAIN_PATH)

valid_df = pd.read_csv(VALID_PATH)

test_df = pd.read_csv(TEST_PATH)

print()

print("Train :", len(train_df))

print("Valid :", len(valid_df))

print("Test  :", len(test_df))

# ==========================================================
# LABEL ENCODER
# ==========================================================

encoder = LabelEncoder()

encoder.fit(train_df["label"])

# ==========================================================
# TRANSFORM
# ==========================================================

train_df["label_id"] = encoder.transform(train_df["label"])

valid_df["label_id"] = encoder.transform(valid_df["label"])

test_df["label_id"] = encoder.transform(test_df["label"])

# ==========================================================
# SAVE ENCODER
# ==========================================================

joblib.dump(

    encoder,

    ENCODER_PATH

)

# ==========================================================
# SAVE DATASET
# ==========================================================

train_df.to_csv(

    TRAIN_PATH,

    index=False,

    encoding="utf-8-sig"

)

valid_df.to_csv(

    VALID_PATH,

    index=False,

    encoding="utf-8-sig"

)

test_df.to_csv(

    TEST_PATH,

    index=False,

    encoding="utf-8-sig"

)

# ==========================================================
# RESULT
# ==========================================================

print()

print("=" * 60)

print("LABEL MAPPING")

print("=" * 60)

for idx, label in enumerate(encoder.classes_):

    print(

        f"{idx} -> {label}"

    )

print()

print("=" * 60)

print("ENCODER")

print("=" * 60)

print(

    ENCODER_PATH

)

print()

print("SELESAI")