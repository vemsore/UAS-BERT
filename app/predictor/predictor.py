"""
=========================================================
INDOBERT PREDICTOR

UAS Analisis Sentimen

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

from pathlib import Path
from app.deployment.download_model import download_model
import joblib
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

# ==========================================================
# PATH
# ==========================================================

ROOT = Path(__file__).resolve().parents[2]

LOCAL_MODEL_DIR = ROOT / "model" / "best_model"

LABEL_ENCODER = ROOT / "model" / "label_encoder.pkl"

# ==========================================================
# LOAD MODEL
# ==========================================================

MODEL_DIR = Path(download_model())
print("=" * 60)
print("LOAD PREDICTOR")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_DIR
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_DIR
)

encoder = joblib.load(
    LABEL_ENCODER
)

device = torch.device(

    "cuda"

    if torch.cuda.is_available()

    else "cpu"

)

model.to(device)

model.eval()

print("Device :", device)

print("=" * 60)
def softmax(logits):

    return torch.softmax(

        logits,

        dim=1

    )
def predict(text):

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

    probs = softmax(

        output.logits

    )

    confidence, pred = torch.max(

        probs,

        dim=1

    )

    label = encoder.inverse_transform(

        [pred.item()]

    )[0]

    probability = {}

    for idx, cls in enumerate(encoder.classes_):

        probability[cls] = round(

            float(

                probs[0][idx]

            ),

            4

        )

    return {

        "text": text,

        "label": label,

        "confidence": round(

            float(

                confidence.item()

            ),

            4

        ),

        "probability": probability

    }