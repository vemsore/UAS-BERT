"""
=========================================================
SPLIT DATASET

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split

# =====================================================
# PATH
# =====================================================

ROOT = Path(__file__).resolve().parents[2]

GOLD_DATASET = ROOT / "dataset" / "gold" / "dataset_gold_2313500122.csv"

OUTPUT_DIR = ROOT / "dataset" / "split"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =====================================================
# LOAD DATASET
# =====================================================

print("=" * 60)
print("SPLIT DATASET")
print("=" * 60)

df = pd.read_csv(GOLD_DATASET)

print(f"Dataset : {len(df)}")

# =====================================================
# VALIDASI
# =====================================================

required_columns = [
    "full_text",
    "label"
]

for col in required_columns:

    if col not in df.columns:

        raise Exception(f"Kolom '{col}' tidak ditemukan.")

# =====================================================
# HAPUS LABEL KOSONG
# =====================================================

df = df.dropna(subset=["label"])

df = df[df["label"] != ""]

df = df.reset_index(drop=True)

print()

print("Jumlah Data Setelah Validasi")

print(len(df))

# =====================================================
# LABEL DISTRIBUTION
# =====================================================

print()

print("Distribusi Label")

print(df["label"].value_counts())

# =====================================================
# SPLIT 80 / 20
# =====================================================

train_df, temp_df = train_test_split(

    df,

    test_size=0.20,

    random_state=42,

    shuffle=True,

    stratify=df["label"]

)

# =====================================================
# SPLIT 10 / 10
# =====================================================

valid_df, test_df = train_test_split(

    temp_df,

    test_size=0.50,

    random_state=42,

    shuffle=True,

    stratify=temp_df["label"]

)

# =====================================================
# SAVE
# =====================================================

train_path = OUTPUT_DIR / "train.csv"

valid_path = OUTPUT_DIR / "valid.csv"

test_path = OUTPUT_DIR / "test.csv"

train_df.to_csv(

    train_path,

    index=False,

    encoding="utf-8-sig"

)

valid_df.to_csv(

    valid_path,

    index=False,

    encoding="utf-8-sig"

)

test_df.to_csv(

    test_path,

    index=False,

    encoding="utf-8-sig"

)

# =====================================================
# HASIL
# =====================================================

print()

print("=" * 60)

print("HASIL SPLIT")

print("=" * 60)

print(f"Train      : {len(train_df)}")

print(f"Validation : {len(valid_df)}")

print(f"Test        : {len(test_df)}")

print()

print("=" * 60)

print("DISTRIBUSI LABEL")

print("=" * 60)

print()

print("TRAIN")

print(train_df["label"].value_counts())

print()

print("VALIDATION")

print(valid_df["label"].value_counts())

print()

print("TEST")

print(test_df["label"].value_counts())

print()

print("=" * 60)

print("FILE")

print("=" * 60)

print(train_path)

print(valid_path)

print(test_path)

print()

print("SELESAI")