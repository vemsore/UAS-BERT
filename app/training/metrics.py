"""
=========================================================
METRICS

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)

# ==========================================================
# COMPUTE METRICS
# ==========================================================

def compute_metrics(eval_pred):
    """
    Digunakan oleh HuggingFace Trainer
    """

    logits, labels = eval_pred

    predictions = np.argmax(logits, axis=-1)

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

    return {

        "accuracy": round(float(accuracy), 4),

        "precision": round(float(precision), 4),

        "recall": round(float(recall), 4),

        "f1": round(float(f1), 4)

    }

# ==========================================================
# FORMAT METRICS
# ==========================================================

def print_metrics(metrics: dict):

    print("=" * 60)

    print("EVALUATION METRICS")

    print("=" * 60)

    print(f"Accuracy : {metrics['accuracy']:.4f}")

    print(f"Precision: {metrics['precision']:.4f}")

    print(f"Recall   : {metrics['recall']:.4f}")

    print(f"F1 Score : {metrics['f1']:.4f}")

    print("=" * 60)