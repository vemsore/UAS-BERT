"""
=========================================================
DATASET LOADER

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""

from pathlib import Path

import pandas as pd
import torch

from torch.utils.data import Dataset

from transformers import AutoTokenizer

from app.config import MAX_LENGTH

ROOT = Path(__file__).resolve().parents[2]

TOKENIZER_PATH = ROOT / "model" / "tokenizer"


TOKENIZER = AutoTokenizer.from_pretrained(TOKENIZER_PATH)

class SentimentDataset(Dataset):

    def __init__(self, dataframe):

        self.df = dataframe.reset_index(drop=True)

        self.tokenizer = TOKENIZER

    def __len__(self):

        return len(self.df)

    def __getitem__(self, index):

        text = str(self.df.loc[index, "full_text"])

        label = int(self.df.loc[index, "label_id"])

        encoding = self.tokenizer(

            text,

            truncation=True,

            padding="max_length",

            max_length=MAX_LENGTH,

            return_attention_mask=True,

            return_tensors="pt"

        )

        return {

            "input_ids":

                encoding["input_ids"].flatten(),

            "attention_mask":

                encoding["attention_mask"].flatten(),

            "labels":

                torch.tensor(

                    label,

                    dtype=torch.long

                )

        }


def load_dataframe(path):

    return pd.read_csv(path)