"""
===========================================================
DATASET INSPECTOR

Analisis Sentimen IndoBERT

Nama : Rekhan Fadhillah Syahputra

NIM  : 2313500122
===========================================================
"""

from pathlib import Path

import pandas as pd

from config import *
from utils import Console

Console.title("DATASET INSPECTOR")

# =====================================================
# LOAD DATASET
# =====================================================

dataset_path = RAW_DIR / RAW_FILENAME

if not dataset_path.exists():

    Console.error("Dataset tidak ditemukan")

    exit()

df = pd.read_csv(dataset_path)

Console.success(f"Dataset berhasil dibaca ({len(df)} data)")

# =====================================================
# JUMLAH DATA
# =====================================================

Console.title("JUMLAH DATA")

print(df.shape)

# =====================================================
# KOLOM
# =====================================================

Console.title("KOLOM")

for c in df.columns:

    print("-", c)

# =====================================================
# MISSING VALUE
# =====================================================

Console.title("MISSING VALUE")

missing = df.isnull().sum()

print(missing)

# =====================================================
# DUPLICATE
# =====================================================

Console.title("DUPLICATE")

duplicate = df.duplicated(subset=["full_text"]).sum()

print(f"Duplicate : {duplicate}")

# =====================================================
# BAHASA
# =====================================================

Console.title("BAHASA")

print(df["lang"].value_counts())

# =====================================================
# PANJANG TWEET
# =====================================================

Console.title("PANJANG TWEET")

df["panjang_tweet"] = df["full_text"].astype(str).apply(len)

print(df["panjang_tweet"].describe())

# =====================================================
# URL
# =====================================================

Console.title("URL")

url = df["full_text"].str.contains(

r"http",

case=False,

regex=True

).sum()

print(f"Mengandung URL : {url}")

# =====================================================
# MENTION
# =====================================================

Console.title("MENTION")

mention = df["full_text"].str.contains(

r"@",

regex=True

).sum()

print(f"Mengandung Mention : {mention}")

# =====================================================
# HASHTAG
# =====================================================

Console.title("HASHTAG")

hashtag = df["full_text"].str.contains(

r"#",

regex=True

).sum()

print(f"Mengandung Hashtag : {hashtag}")

# =====================================================
# RETWEET
# =====================================================

Console.title("RETWEET")

rt = df["full_text"].str.startswith(

"RT"

).sum()

print(f"Retweet : {rt}")

# =====================================================
# SIMPAN REPORT
# =====================================================

report = OUTPUT_DIR / "report"

report.mkdir(

parents=True,

exist_ok=True

)

summary = report / "dataset_summary.txt"

with open(

summary,

"w",

encoding="utf-8"

) as f:

    f.write("DATASET SUMMARY\n\n")

    f.write(f"Jumlah Data : {len(df)}\n")

    f.write(

        f"Duplicate : {duplicate}\n"

    )

    f.write(

        f"URL : {url}\n"

    )

    f.write(

        f"Mention : {mention}\n"

    )

    f.write(

        f"Hashtag : {hashtag}\n"

    )

    f.write(

        f"Retweet : {rt}\n"

    )

Console.success(

"Report berhasil disimpan"

)

Console.title("SELESAI")