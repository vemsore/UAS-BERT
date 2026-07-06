"""
==================================================
TEXT NORMALIZATION

Analisis Sentimen Kebijakan Publik

IndoBERT
==================================================
"""

import re
import pandas as pd

from config import *
from utils import Console

Console.title("TEXT NORMALIZATION")

clean_path = DATASET_DIR / "clean" / "dataset_clean_2313500122.csv"

df = pd.read_csv(clean_path)

Console.success(f"Dataset dibaca : {len(df)} data")
Console.title("CASE FOLDING")

df["full_text"] = df["full_text"].str.lower()

Console.success("Semua huruf menjadi lowercase")

Console.title("REMOVE EMOJI")

emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "]+",
    flags=re.UNICODE
)

df["full_text"] = df["full_text"].apply(
    lambda x: emoji_pattern.sub("", str(x))
)

Console.success("Emoji dihapus")

Console.title("REMOVE HASHTAG")

df["full_text"] = df["full_text"].str.replace(

"#",

"",

regex=False

)

Console.success("Hashtag dibersihkan")

Console.title("REMOVE PUNCTUATION")

df["full_text"] = df["full_text"].str.replace(

r"[^\w\s]",

" ",

regex=True

)

Console.success("Punctuation dihapus")

Console.title("REMOVE NUMBER")

df["full_text"] = df["full_text"].str.replace(

r"\d+",

" ",

regex=True

)

Console.success("Number dihapus")

Console.title("REMOVE MULTIPLE SPACE")

df["full_text"] = df["full_text"].str.replace(

r"\s+",

" ",

regex=True

)

df["full_text"] = df["full_text"].str.strip()

Console.success("Whitespace dirapikan")

Console.title("MENYIMPAN DATASET")

output_path = DATASET_DIR / "normalized"

output_path.mkdir(parents=True, exist_ok=True)

save_file = output_path / "dataset_normalized_2313500122.csv"

df.to_csv(save_file, index=False, encoding="utf-8-sig")

Console.success(f"Dataset disimpan : {save_file}")
Console.title("SAMPLE HASIL NORMALISASI")

print(df.head())
Console.title("INFO DATASET")

print(df.info())
Console.title("SELESAI")

Console.success(f"Total Dataset : {len(df)}")