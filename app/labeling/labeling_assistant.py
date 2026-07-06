"""
=========================================================
SMART LABELING ASSISTANT

Nama  : Rekhan Fadhillah Syahputra
NIM   : 2313500122

Analisis Sentimen Deep Learning IndoBERT

=========================================================
"""

import os
import sys

from pathlib import Path

import pandas as pd
from tqdm import tqdm

# -------------------------------------------------------
# supaya app dapat dikenali
# -------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

# -------------------------------------------------------
# Import Project
# -------------------------------------------------------

from app.config import (
    DATASET_DIR,
    OUTPUT_DIR,
    ASSETS_DIR
)

from app.labeling.sentiment import SentimentEngine
from app.labeling.confidence import ConfidenceEngine

# =====================================================
# CLASS
# =====================================================

class LabelingAssistant:

    def __init__(self):

        print("="*60)
        print("SMART LABELING ASSISTANT")
        print("="*60)

        self.input_file = (
            DATASET_DIR
            / "quality"
            / "dataset_quality_2313500122.csv"
        )

        self.output_dir = (
            DATASET_DIR
            / "assistant"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.output_file = (
            self.output_dir
            / "dataset_assistant_2313500122.csv"
        )

        print(f"Dataset : {self.input_file}")

        # -----------------------------
        # Load Engine
        # -----------------------------

        self.sentiment = SentimentEngine(
            ASSETS_DIR / "generated"
        )

        self.confidence = ConfidenceEngine()

        print("Sentiment Engine  : OK")
        print("Confidence Engine : OK")
        print("="*60)

    # =====================================================
    # LOAD DATASET
    # =====================================================

    def load_dataset(self):

        if not self.input_file.exists():

            raise FileNotFoundError(
                f"Dataset tidak ditemukan : {self.input_file}"
            )

        df = pd.read_csv(
            self.input_file
        )

        if "full_text" not in df.columns:

            raise Exception(
                "Kolom full_text tidak ditemukan."
            )

        df = df.copy()

        df["full_text"] = (
            df["full_text"]
            .astype(str)
            .fillna("")
        )

        print(f"Jumlah Data : {len(df)}")

        return df
    
    # =====================================================
    # PROCESS LABELING
    # =====================================================

    def process(self):

        df = self.load_dataset()

        hasil = []

        print("=" * 60)
        print("PROSES LABELING")
        print("=" * 60)

        for _, row in tqdm(
            df.iterrows(),
            total=len(df),
            desc="Labeling"
        ):

            text = row["full_text"]

            # ---------------------------------------
            # Sentiment Analysis
            # ---------------------------------------

            sentiment_result = self.sentiment.analyze(text)

            # ---------------------------------------
            # Confidence Analysis
            # ---------------------------------------

            confidence_result = self.confidence.calculate(
                sentiment_result
            )

            hasil.append({

                "full_text": text,

                "positive_score":
                    sentiment_result["positive_score"],

                "negative_score":
                    sentiment_result["negative_score"],

                "booster_score":
                    sentiment_result["booster_score"],

                "negation_score":
                    sentiment_result["negation_score"],

                "policy_score":
                    sentiment_result["policy_score"],

                "confidence":
                    confidence_result["confidence"],

                "suggestion":
                    confidence_result["label"],

                "need_review":
                    confidence_result["need_review"],

                "positive_words":
                    ", ".join(
                        sentiment_result["positive_words"]
                    ),

                "negative_words":
                    ", ".join(
                        sentiment_result["negative_words"]
                    ),

                "booster_words":
                    ", ".join(
                        sentiment_result["booster_words"]
                    ),

                "negation_words":
                    ", ".join(
                        sentiment_result["negation_words"]
                    ),

                "policy_words":
                    ", ".join(
                        sentiment_result["policy_words"]
                    ),

                # Reviewer nanti mengisi kolom ini
                "final_label": ""

            })

        hasil = pd.DataFrame(hasil)

        return hasil
    
    # =====================================================
    # SAVE RESULT
    # =====================================================

    def save_result(self, hasil_df):

        print("=" * 60)
        print("MENYIMPAN DATASET")
        print("=" * 60)

        hasil_df.to_csv(
            self.output_file,
            index=False,
            encoding="utf-8-sig"
        )

        print(f"Dataset berhasil disimpan :")
        print(self.output_file)

        print()

        print("=" * 60)
        print("STATISTIK LABEL")
        print("=" * 60)

        print(
            hasil_df["suggestion"].value_counts()
        )

        print()

        print("=" * 60)
        print("REVIEW")
        print("=" * 60)

        print(
            hasil_df["need_review"].value_counts()
        )

        print()

        print("=" * 60)
        print("CONFIDENCE")
        print("=" * 60)

        print(
            hasil_df["confidence"].describe()
        )

        print()

        print("=" * 60)
        print("SELESAI")
        print("=" * 60)
    # =====================================================
    # RUN
    # =====================================================

    def run(self):

        hasil = self.process()

        self.save_result(hasil)
        # =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    app = LabelingAssistant()

    app.run()