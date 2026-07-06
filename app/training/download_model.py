"""
=========================================================
DOWNLOAD PRETRAINED MODEL

UAS Analisis Sentimen
=========================================================
"""

from pathlib import Path

from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer
)

from app.config import MODEL_NAME

ROOT = Path(__file__).resolve().parents[2]

PRETRAINED_DIR = ROOT / "model" / "pretrained"

PRETRAINED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("=" * 60)
print("DOWNLOAD PRETRAINED MODEL")
print("=" * 60)

print("\nModel :", MODEL_NAME)

print("\nDownloading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

print("Downloading model...")

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=3
)

print("\nSaving tokenizer...")

tokenizer.save_pretrained(PRETRAINED_DIR)

print("Saving model...")

model.save_pretrained(PRETRAINED_DIR)

print("\n" + "=" * 60)
print("SELESAI")
print("=" * 60)

print(PRETRAINED_DIR)