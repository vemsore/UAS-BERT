"""
=========================================================
EVALUATE INDOBERT

UAS Analisis Sentimen
Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import torch

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

# =====================================================
# PATH
# =====================================================

ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = ROOT / "model" / "best_model"

TEST_DATA = ROOT / "dataset" / "split" / "test.csv"

LABEL_ENCODER = ROOT / "model" / "label_encoder.pkl"

OUTPUT_DIR = ROOT / "output" / "evaluation"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# =====================================================
# LOAD
# =====================================================

print("=" * 60)
print("LOAD MODEL")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_DIR
)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model.to(device)

model.eval()

print("Device :", device)

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(TEST_DATA)

print()

print("Test Dataset :", len(df))

encoder = joblib.load(LABEL_ENCODER)

# =====================================================
# PREDICT
# =====================================================

predictions = []

labels = []

texts = []

print()

print("=" * 60)
print("PREDICT")
print("=" * 60)

for _, row in df.iterrows():

    text = str(row["full_text"])

    label = int(row["label_id"])

    encoding = tokenizer(

        text,

        truncation=True,

        padding="max_length",

        max_length=64,

        return_tensors="pt"

    )

    encoding = {
        k: v.to(device)
        for k, v in encoding.items()
    }

    with torch.no_grad():

        output = model(**encoding)

    pred = torch.argmax(
        output.logits,
        dim=1
    ).item()

    predictions.append(pred)

    labels.append(label)

    texts.append(text)
# =====================================================
# EVALUATION
# =====================================================

print()

print("=" * 60)
print("CALCULATE METRICS")
print("=" * 60)

accuracy = accuracy_score(
    labels,
    predictions
)

precision, recall, f1, _ = precision_recall_fscore_support(
    labels,
    predictions,
    average="weighted",
    zero_division=0
)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
# =====================================================
# CLASSIFICATION REPORT
# =====================================================

target_names = list(encoder.classes_)

report = classification_report(
    labels,
    predictions,
    target_names=target_names,
    digits=4,
    zero_division=0
)

report_path = OUTPUT_DIR / "classification_report.txt"

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write(report)

print()

print("Classification Report")

print(report)

print("Saved :")

print(report_path)
# =====================================================
# SAVE JSON
# =====================================================

evaluation = {

    "accuracy": float(accuracy),

    "precision": float(precision),

    "recall": float(recall),

    "f1_score": float(f1)

}

evaluation_path = OUTPUT_DIR / "evaluation.json"

with open(
    evaluation_path,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        evaluation,
        f,
        indent=4
    )

print()

print("Saved :")

print(evaluation_path)
# =====================================================
# SAVE PREDICTION
# =====================================================

prediction_df = pd.DataFrame({

    "text": texts,

    "label_true": encoder.inverse_transform(labels),

    "label_pred": encoder.inverse_transform(predictions)

})

prediction_path = OUTPUT_DIR / "prediction.csv"

prediction_df.to_csv(
    prediction_path,
    index=False,
    encoding="utf-8-sig"
)

print()

print("Saved :")

print(prediction_path)
# =====================================================
# CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(
    labels,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=encoder.classes_
)

fig, ax = plt.subplots(figsize=(6,6))

disp.plot(
    ax=ax,
    colorbar=False
)

plt.tight_layout()

cm_path = OUTPUT_DIR / "confusion_matrix.png"

plt.savefig(
    cm_path,
    dpi=300
)

plt.close()

print()

print("Saved :")

print(cm_path)
# =====================================================
# SUMMARY
# =====================================================

print()

print("=" * 60)
print("EVALUATION SUMMARY")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print()

print("Output Folder")

print(OUTPUT_DIR)

print()

print("=" * 60)
print("SELESAI")
print("=" * 60)