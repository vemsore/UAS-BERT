"""
=========================================================
INDOBERT TOKENIZER

UAS Analisis Sentimen

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

from pathlib import Path

from transformers import AutoTokenizer

try:
    from app.config import MODEL_NAME
except ModuleNotFoundError:
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[2]
    sys.path.append(str(ROOT))

    from app.config import MODEL_NAME

# ==========================================================
# PATH
# ==========================================================

ROOT = Path(__file__).resolve().parents[2]

TOKENIZER_DIR = ROOT / "model" / "tokenizer"

TOKENIZER_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# DOWNLOAD TOKENIZER
# ==========================================================

print("=" * 60)
print("DOWNLOAD TOKENIZER")
print("=" * 60)

print()

print("Model")

print(MODEL_NAME)

print()

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

print()

print("=" * 60)
print("SAVE TOKENIZER")
print("=" * 60)

tokenizer.save_pretrained(
    TOKENIZER_DIR
)

print()

print("Saved")

print(TOKENIZER_DIR)

print()

print("=" * 60)
print("VOCAB SIZE")
print("=" * 60)

print(tokenizer.vocab_size)

print()

print("=" * 60)
print("SPECIAL TOKEN")
print("=" * 60)

print("CLS :", tokenizer.cls_token)

print("SEP :", tokenizer.sep_token)

print("PAD :", tokenizer.pad_token)

print("UNK :", tokenizer.unk_token)

print()

print("=" * 60)
print("SELESAI")
print("=" * 60)