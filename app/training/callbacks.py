"""
=========================================================
TRAIN CALLBACKS
=========================================================
"""

import csv
from pathlib import Path

from transformers import TrainerCallback

ROOT = Path(__file__).resolve().parents[2]

LOG_FILE = ROOT / "model" / "training_log.csv"


class CSVLoggerCallback(TrainerCallback):

    def __init__(self):

        self.header_written = False

    def on_log(self, args, state, control, logs=None, **kwargs):

        if logs is None:
            return

        file_exists = LOG_FILE.exists()

        with open(
            LOG_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=logs.keys()
            )

            if not file_exists:

                writer.writeheader()

            writer.writerow(logs)