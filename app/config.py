"""
===========================================================
CONFIG PROJECT

UAS ANALISIS SENTIMEN
INDOBERT

Nama :
Rekhan Fadhillah Syahputra

NIM :
2313500122
===========================================================
"""

from pathlib import Path

# =========================================================
# ROOT PROJECT
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

APP_DIR = ROOT_DIR / "app"

# =========================================================
# DATASET
# =========================================================

DATASET_DIR = ROOT_DIR / "dataset"

RAW_DIR = DATASET_DIR / "raw"

CLEAN_DIR = DATASET_DIR / "clean"

NORMALIZED_DIR = DATASET_DIR / "normalized"

QUALITY_DIR = DATASET_DIR / "quality"

ASSISTANT_DIR = DATASET_DIR / "assistant"

LABELED_DIR = DATASET_DIR / "labeled"

# =========================================================
# ASSETS
# =========================================================

ASSETS_DIR = ROOT_DIR / "assets"

ASSETS_RAW_DIR = ASSETS_DIR / "raw"

ASSETS_GENERATED_DIR = ASSETS_DIR / "generated"

# =========================================================
# MODEL
# =========================================================

MODEL_DIR = ROOT_DIR / "model"

# =========================================================
# OUTPUT
# =========================================================

OUTPUT_DIR = ROOT_DIR / "output"

LOG_DIR = OUTPUT_DIR / "logs"

REPORT_DIR = OUTPUT_DIR / "report"

# =========================================================
# AUTO CREATE DIRECTORY
# =========================================================

folders = [

    DATASET_DIR,

    RAW_DIR,

    CLEAN_DIR,

    NORMALIZED_DIR,

    QUALITY_DIR,

    ASSISTANT_DIR,

    LABELED_DIR,

    ASSETS_DIR,

    ASSETS_RAW_DIR,

    ASSETS_GENERATED_DIR,

    MODEL_DIR,

    OUTPUT_DIR,

    LOG_DIR,

    REPORT_DIR

]

for folder in folders:

    folder.mkdir(

        parents=True,

        exist_ok=True

    )

# =========================================================
# DATASET
# =========================================================

RAW_FILENAME = "dataset_raw_2313500122.csv"

NORMALIZED_FILENAME = "dataset_normalized_2313500122.csv"

QUALITY_FILENAME = "dataset_quality_2313500122.csv"

ASSISTANT_FILENAME = "dataset_assistant_2313500122.csv"

# =========================================================
# TRAINING
# =========================================================

TRAIN_SIZE = 0.8

VALID_SIZE = 0.1

TEST_SIZE = 0.1

RANDOM_STATE = 42

MAX_LENGTH = 128

BATCH_SIZE = 16

EPOCHS = 5

LEARNING_RATE = 2e-5

# =========================================================
# CRAWLER
# =========================================================

LIMIT = 8000

SEARCH_KEYWORD = """
(
"Pajak" OR
"PPN" OR
"BBM" OR
"Subsidi" OR
"Bensin" OR
"Pemerintah" OR
"Korupsi" OR
"UKT" OR
"Beasiswa" OR
"Bansos" OR
"BPJS" OR
"Demo" OR
"Presiden" OR
"Menteri" OR
"DPR" OR
"MPR" OR
"Kabinet" OR
"IKN" OR
"Danantara" OR
"Rupiah" OR
"MBG"
)

lang:id

since:2014-01-01

until:2026-07-10
"""

TWITTER_AUTH_TOKEN = "154b300260539d4684aa453ec8e57ae667c8ed98"

# ==========================================================
# DEEP LEARNING CONFIGURATION
# ==========================================================

# HuggingFace Model
MODEL_NAME = "indobenchmark/indobert-base-p1"

# Maximum token per tweet
MAX_LENGTH = 64

# Training
TRAIN_BATCH_SIZE = 4
VALID_BATCH_SIZE = 4

# Karena RAM hanya 8GB
GRADIENT_ACCUMULATION_STEPS = 4

# Fine-tuning
LEARNING_RATE = 2e-5
WEIGHT_DECAY = 0.01

# Epoch
NUM_EPOCHS = 5

# Random Seed
RANDOM_STATE = 42

# Early Stopping
EARLY_STOPPING_PATIENCE = 2

# Save Best Model
LOAD_BEST_MODEL_AT_END = True

# Logging
LOGGING_STEPS = 25

# Evaluation
EVAL_STRATEGY = "epoch"

# Save
SAVE_STRATEGY = "epoch"

# =====================================================
# HUGGING FACE MODEL
# =====================================================

HF_REPO_ID = "Avemsoer/indobert-sentiment"

MODEL_LOCAL_DIR = MODEL_DIR / "best_model"

TOKENIZER_LOCAL_DIR = MODEL_DIR / "tokenizer"