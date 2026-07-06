"""
=========================================================
TRAIN CONFIG

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

from pathlib import Path

from app.config import (
    MODEL_NAME,
    MAX_LENGTH,
    TRAIN_BATCH_SIZE,
    VALID_BATCH_SIZE,
    GRADIENT_ACCUMULATION_STEPS,
    LEARNING_RATE,
    WEIGHT_DECAY,
    NUM_EPOCHS,
    RANDOM_STATE,
    EARLY_STOPPING_PATIENCE,
    LOAD_BEST_MODEL_AT_END,
    LOGGING_STEPS,
    EVAL_STRATEGY,
    SAVE_STRATEGY,
)

# =====================================================
# ROOT
# =====================================================

ROOT = Path(__file__).resolve().parents[2]

# =====================================================
# DATASET
# =====================================================

TRAIN_DATASET = ROOT / "dataset" / "split" / "train.csv"

VALID_DATASET = ROOT / "dataset" / "split" / "valid.csv"

TEST_DATASET = ROOT / "dataset" / "split" / "test.csv"

# =====================================================
# MODEL
# =====================================================

MODEL_DIR = ROOT / "model"

BEST_MODEL_DIR = MODEL_DIR / "best_model"

TOKENIZER_DIR = MODEL_DIR / "tokenizer"

LABEL_ENCODER = MODEL_DIR / "label_encoder.pkl"

# =====================================================
# OUTPUT
# =====================================================

OUTPUT_DIR = ROOT / "output"

CHECKPOINT_DIR = OUTPUT_DIR / "checkpoint"

LOG_DIR = OUTPUT_DIR / "logs"

for folder in [

    MODEL_DIR,

    BEST_MODEL_DIR,

    OUTPUT_DIR,

    CHECKPOINT_DIR,

    LOG_DIR

]:

    folder.mkdir(

        parents=True,

        exist_ok=True

    )

# =====================================================
# TRAINING CONFIG
# =====================================================

CONFIG = {

    "model_name": MODEL_NAME,

    "max_length": MAX_LENGTH,

    "train_batch_size": TRAIN_BATCH_SIZE,

    "valid_batch_size": VALID_BATCH_SIZE,

    "gradient_accumulation":

        GRADIENT_ACCUMULATION_STEPS,

    "learning_rate":

        LEARNING_RATE,

    "weight_decay":

        WEIGHT_DECAY,

    "epochs":

        NUM_EPOCHS,

    "random_state":

        RANDOM_STATE,

    "early_stopping":

        EARLY_STOPPING_PATIENCE,

    "logging_steps":

        LOGGING_STEPS,

    "evaluation_strategy":

        EVAL_STRATEGY,

    "save_strategy":

        SAVE_STRATEGY,

    "load_best_model":

        LOAD_BEST_MODEL_AT_END

}

# =====================================================
# SHOW CONFIG
# =====================================================

def show_config():

    print("=" * 60)

    print("TRAIN CONFIGURATION")

    print("=" * 60)

    for key, value in CONFIG.items():

        print(f"{key:<30}: {value}")

    print()

    print("=" * 60)

    print("DIRECTORY")

    print("=" * 60)

    print("Train Dataset :", TRAIN_DATASET)

    print("Valid Dataset :", VALID_DATASET)

    print("Test Dataset  :", TEST_DATASET)

    print()

    print("Tokenizer     :", TOKENIZER_DIR)

    print("Label Encoder :", LABEL_ENCODER)

    print("Best Model    :", BEST_MODEL_DIR)

    print("Output        :", OUTPUT_DIR)

    print("=" * 60)