"""
==========================================================
PREPROCESSING

Analisis Sentimen Kebijakan Publik

Menggunakan IndoBERT

Nama :
Rekhan Fadhillah Syahputra

NIM :
2313500122
==========================================================
"""

import re
import pandas as pd

from config import *
from utils import Console

Console.title("PREPROCESSING DATASET")

# ==========================================================
# LOAD DATASET
# ==========================================================

raw_path = RAW_DIR / RAW_FILENAME

df = pd.read_csv(raw_path)

Console.success(f"Dataset berhasil dibaca : {len(df)} data")

Console.title("FILTER BAHASA")

sebelum = len(df)

df = df[df["lang"]=="in"]

sesudah = len(df)

Console.success(f"Sebelum : {sebelum}")

Console.success(f"Sesudah : {sesudah}")

Console.title("DROP KOLOM")

drop_columns = [

"id_str",

"created_at",

"username",

"favorite_count",

"retweet_count",

"reply_count",

"quote_count",

"lang"

]

df = df.drop(

columns=drop_columns,

errors="ignore"

)

Console.success("Kolom tidak diperlukan dihapus.")

Console.title("REMOVE URL")

df["full_text"] = df["full_text"].str.replace(

r"http\S+",

" ",

regex=True

)

df["full_text"] = df["full_text"].str.replace(

r"www\S+",

" ",

regex=True

)

Console.success("URL dihapus")

Console.title("REMOVE MENTION")

df["full_text"] = df["full_text"].str.replace(

r"@\w+",

" ",

regex=True

)

Console.success("Mention dihapus")

Console.title("REMOVE RT")

df["full_text"] = df["full_text"].str.replace(

r"^RT[\s]+",

"",

regex=True

)

Console.success("RT dihapus")

Console.title("REMOVE HTML")

df["full_text"] = df["full_text"].str.replace(

r"&amp;",

"dan",

regex=True

)

df["full_text"] = df["full_text"].str.replace(

r"&gt;",

"",

regex=True

)

df["full_text"] = df["full_text"].str.replace(

r"&lt;",

"",

regex=True

)

Console.success("HTML dibersihkan")

Console.title("MENYIMPAN DATASET")

clean_dir = DATASET_DIR / "clean"

clean_dir.mkdir(

parents=True,

exist_ok=True

)

output = clean_dir / "dataset_clean_2313500122.csv"

df.to_csv(

output,

index=False,

encoding="utf-8-sig"

)

Console.success(f"Dataset tersimpan : {output}")

Console.title("SELESAI")