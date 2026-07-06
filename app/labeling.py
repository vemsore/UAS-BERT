"""
========================================================
LABELING DATASET

Analisis Sentimen

IndoBERT

Rekhan Fadhillah Syahputra
2313500122
========================================================
"""

import pandas as pd

from transformers import pipeline

from config import *

from utils import Console

Console.title("AUTO LABELING")

dataset = DATASET_DIR/"quality"/"dataset_quality_2313500122.csv"

df = pd.read_csv(dataset)

Console.success(f"Dataset : {len(df)}")

Console.title("LOAD MODEL")

classifier = pipeline(

"sentiment-analysis",

model="w11wo/indonesian-roberta-base-sentiment-classifier"

)

Console.success("Model berhasil dimuat")