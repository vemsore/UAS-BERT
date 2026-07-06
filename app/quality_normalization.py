"""
===========================================
QUALITY NORMALIZATION

Analisis Sentimen

IndoBERT

Rekhan Fadhillah Syahputra

2313500122
===========================================
"""

import re
import pandas as pd

from config import *
from utils import Console

Console.title("QUALITY NORMALIZATION")
ASSETS_DIR = ROOT_DIR / "assets"
dataset = DATASET_DIR/"normalized"/"dataset_normalized_2313500122.csv"

df = pd.read_csv(dataset)

Console.success(f"Dataset : {len(df)}")

Console.title("LOAD SLANG DICTIONARY")

slang = pd.read_csv(
ASSETS_DIR/"kamus_slang.csv"
)

slang_dict = dict(

zip(

slang["slang"],

slang["formal"]

)

)

Console.success(

f"Kamus : {len(slang_dict)} kata"

)

def reduce_character(text):

    text = re.sub(

        r'(.)\1{2,}',

        r'\1',

        text

    )

    return text

Console.title("REDUCE CHARACTER")

df["full_text"] = df["full_text"].apply(

reduce_character

)

Console.success(

"Repeated Character selesai"

)

def normalize(text):

    words = text.split()

    hasil = []

    for w in words:

        hasil.append(

            slang_dict.get(

                w,

                w

            )

        )

    return " ".join(hasil)

Console.title("NORMALIZE SLANG")

df["full_text"] = df["full_text"].apply(

normalize

)

Console.success(

"Slang berhasil dinormalisasi"

)

df["full_text"] = df["full_text"].str.replace(

r"\s+",

" ",

regex=True

)

df["full_text"] = df["full_text"].str.strip()

Console.title("SAVE")

quality = DATASET_DIR/"quality"

quality.mkdir(

parents=True,

exist_ok=True

)

output = quality/"dataset_quality_2313500122.csv"

df.to_csv(

output,

index=False,

encoding="utf-8-sig"

)

Console.success(

f"Dataset disimpan : {output}"

)
Console.title("HASIL")

print(df.head())
Console.title("INFO")

print(df.info())
Console.title("SELESAI")

Console.success(

f"Total Data : {len(df)}"

)