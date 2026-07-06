"""
=========================================================
TRAIN INDOBERT

UAS Analisis Sentimen
Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

import json
from pathlib import Path

import torch
from transformers import AutoModelForSequenceClassification

from app.training.dataset_loader import (
    SentimentDataset,
    load_dataframe,
)

from app.training.trainer_builder import (
    build_trainer,
)

from app.training.train_config import (
    TRAIN_DATASET,
    VALID_DATASET,
    BEST_MODEL_DIR,
    MODEL_DIR,
)

# ==========================================================
# PATH
# ==========================================================

ROOT = Path(__file__).resolve().parents[2]

PRETRAINED_DIR = ROOT / "model" / "pretrained"

# ==========================================================
# LOAD DATASET
# ==========================================================

print("=" * 60)
print("LOAD DATASET")
print("=" * 60)

train_df = load_dataframe(TRAIN_DATASET)
valid_df = load_dataframe(VALID_DATASET)

print(f"Train Dataset : {len(train_df)}")
print(f"Valid Dataset : {len(valid_df)}")

# ==========================================================
# CREATE DATASET
# ==========================================================

print()
print("=" * 60)
print("CREATE DATASET")
print("=" * 60)

train_dataset = SentimentDataset(train_df)
valid_dataset = SentimentDataset(valid_df)

print(f"Train Object : {len(train_dataset)}")
print(f"Valid Object : {len(valid_dataset)}")

# ==========================================================
# LOAD MODEL
# ==========================================================

print()
print("=" * 60)
print("LOAD PRETRAINED MODEL")
print("=" * 60)

model = AutoModelForSequenceClassification.from_pretrained(
    PRETRAINED_DIR,
    num_labels=3
)

print(model.__class__.__name__)

# ==========================================================
# DEVICE
# ==========================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model.to(device)

print()
print(f"Device : {device}")

if torch.cuda.is_available():

    print(
        "GPU :",
        torch.cuda.get_device_name(0)
    )

else:

    print("GPU tidak tersedia, menggunakan CPU.")

# ==========================================================
# BUILD TRAINER
# ==========================================================

print()
print("=" * 60)
print("BUILD TRAINER")
print("=" * 60)

trainer = build_trainer(
    model=model,
    train_dataset=train_dataset,
    valid_dataset=valid_dataset,
)

print("Trainer berhasil dibuat.")

print()
print("=" * 60)
print("READY TO TRAIN")
print("=" * 60)

# ==========================================================
# START TRAINING
# ==========================================================

print()
print("=" * 60)
print("START TRAINING")
print("=" * 60)

try:

    train_result = trainer.train()

except KeyboardInterrupt:

    print()

    print("Training dihentikan oleh user.")

    raise

except Exception as e:

    print()

    print("Training gagal.")

    print(e)

    raise
# ==========================================================
# SAVE MODEL
# ==========================================================

print()

print("=" * 60)
print("SAVE BEST MODEL")
print("=" * 60)

BEST_MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)

trainer.save_model(BEST_MODEL_DIR)

train_dataset.tokenizer.save_pretrained(
    BEST_MODEL_DIR
)

print()

print("Best Model :")

print(BEST_MODEL_DIR)

# ==========================================================
# SAVE TRAIN METRICS
# ==========================================================

print()

print("=" * 60)
print("SAVE TRAIN METRICS")
print("=" * 60)

train_metrics = train_result.metrics

train_metrics_path = MODEL_DIR / "train_metrics.json"

with open(
    train_metrics_path,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        train_metrics,
        f,
        indent=4
    )

print()

print("Saved :")

print(train_metrics_path)

# ==========================================================
# FINAL EVALUATION
# ==========================================================

print()

print("=" * 60)
print("FINAL EVALUATION")
print("=" * 60)

eval_metrics = trainer.evaluate()

metrics_path = MODEL_DIR / "metrics.json"

with open(
    metrics_path,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        eval_metrics,
        f,
        indent=4
    )

print()

for key, value in eval_metrics.items():

    print(f"{key:<30}: {value}")

# ==========================================================
# TRAIN MODEL
# ==========================================================

print()
print("=" * 60)
print("START TRAINING")
print("=" * 60)

train_result = trainer.train()

print()
print("=" * 60)
print("TRAINING FINISHED")
print("=" * 60)

# ==========================================================
# SAVE MODEL
# ==========================================================

print()
print("=" * 60)
print("SAVE BEST MODEL")
print("=" * 60)

trainer.save_model(BEST_MODEL_DIR)

train_dataset.tokenizer.save_pretrained(BEST_MODEL_DIR)

print("Model disimpan di :")

print(BEST_MODEL_DIR)

# ==========================================================
# SAVE TRAIN RESULT
# ==========================================================

metrics = train_result.metrics

metrics_path = MODEL_DIR / "train_metrics.json"

with open(
    metrics_path,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        metrics,
        f,
        indent=4
    )

print()

print("Training Metrics")

for key, value in metrics.items():

    print(f"{key:<25}: {value}")

print()

print("Saved :")

print(metrics_path)

# ==========================================================
# SUMMARY
# ==========================================================

print()

print("=" * 60)
print("TRAINING SUMMARY")
print("=" * 60)

print()

print("Best Model")

print(BEST_MODEL_DIR)

print()

print("Training Metrics")

print(train_metrics_path)

print()

print("Evaluation Metrics")

print(metrics_path)

print()

print("=" * 60)
print("SELESAI")
print("=" * 60)