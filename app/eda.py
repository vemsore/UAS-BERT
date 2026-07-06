"""
=========================================================
EDA

Analisis Sentimen Kebijakan Publik

Menggunakan IndoBERT

Nama :

Rekhan Fadhillah Syahputra

NIM :

2313500122

=========================================================
"""

import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from wordcloud import WordCloud

from config import *
from utils import Console

Console.title("EDA DATASET")

# =====================================================
# LOAD DATASET
# =====================================================

dataset = RAW_DIR / RAW_FILENAME

df = pd.read_csv(dataset)

Console.success(f"Dataset : {len(df)} data")

# =====================================================
# MEMBUAT FOLDER OUTPUT
# =====================================================

figure_dir = OUTPUT_DIR / "figure"

report_dir = OUTPUT_DIR / "report"

figure_dir.mkdir(parents=True, exist_ok=True)

report_dir.mkdir(parents=True, exist_ok=True)

Console.title("STATISTIK DATASET")

print(df.describe(include="all"))

print()

print(df.info())

Console.title("DISTRIBUSI BAHASA")

lang_count = df["lang"].value_counts()

print(lang_count)

plt.figure(figsize=(8,8))

lang_count.plot(

kind="pie",

autopct="%1.1f%%"

)

plt.title("Distribusi Bahasa")

plt.ylabel("")

plt.tight_layout()

plt.savefig(

figure_dir/"bahasa.png",

dpi=300

)

plt.close()

Console.title("PANJANG TWEET")

df["panjang"] = df["full_text"].astype(str).apply(len)

print(df["panjang"].describe())

plt.figure(figsize=(10,6))

plt.hist(

df["panjang"],

bins=30

)

plt.title("Distribusi Panjang Tweet")

plt.xlabel("Jumlah Karakter")

plt.ylabel("Frekuensi")

plt.tight_layout()

plt.savefig(

figure_dir/"histogram_panjang.png",

dpi=300

)

plt.close()

Console.title("WORD CLOUD")

text = " ".join(

df["full_text"].astype(str)

)

wc = WordCloud(

width=1600,

height=800,

background_color="white"

).generate(text)

plt.figure(figsize=(16,8))

plt.imshow(

wc,

interpolation="bilinear"

)

plt.axis("off")

plt.tight_layout()

plt.savefig(

figure_dir/"wordcloud.png",

dpi=300

)

plt.close()