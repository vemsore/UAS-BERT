import subprocess
import shutil
from pathlib import Path

import pandas as pd

from checker import run_all
from config import *
from utils import Console

# =====================================================
# CHECK ENVIRONMENT
# =====================================================

run_all()

Console.title("CRAWLING DATA X")

# =====================================================
# FOLDER tweet-harvest
# =====================================================

tweet_folder = ROOT_DIR / "tweets-data"

tweet_folder.mkdir(
    exist_ok=True
)

output_filename = RAW_FILENAME

# =====================================================
# COMMAND
# =====================================================

command = [

    "npx",

    "--yes",

    "tweet-harvest@2.6.1",

    "-o",

    output_filename,

    "-s",

    SEARCH_KEYWORD,

    "--tab",

    "LATEST",

    "-l",

    str(LIMIT),

    "--token",

    TWITTER_AUTH_TOKEN

]

Console.title("MENJALANKAN TWEET HARVEST")

result = subprocess.run(
    command,
    shell=True,
    cwd=ROOT_DIR,
    text=True
)

if result.returncode != 0:

    Console.error("Tweet Harvest gagal")

    exit()

Console.success("Tweet Harvest selesai")

# =====================================================
# CEK FILE HASIL CRAWLING
# =====================================================

Console.title("MEMERIKSA HASIL CRAWLING")

csv_path = tweet_folder / output_filename

if not csv_path.exists():

    Console.error("CSV tidak ditemukan")

    exit()

Console.success("CSV berhasil ditemukan")

# =====================================================
# MEMBACA DATASET
# =====================================================

Console.title("MEMBACA DATASET")

df = pd.read_csv(csv_path)

Console.success(f"Jumlah Tweet : {len(df)}")

# =====================================================
# VALIDASI KOLOM
# =====================================================

Console.title("VALIDASI KOLOM")

print(df.columns.tolist())
required_columns = [

"id_str",

"created_at",

"username",

"full_text",

"favorite_count",

"retweet_count",

"reply_count",

"quote_count",

"lang"

]

missing = [

col

for col in required_columns

if col not in df.columns

]

if missing:

    Console.error(

        f"Kolom tidak ditemukan : {missing}"

    )

    exit()

Console.success("Semua kolom tersedia")

df = df[required_columns]

Console.title("MENGHAPUS DATA KOSONG")

before = len(df)

df = df.dropna(subset=["full_text"])

after = len(df)

Console.success(

    f"Data kosong dihapus : {before-after}"

)

before = len(df)

df = df[

df["full_text"].astype(str).str.strip()!=""

]

after = len(df)

Console.success(

    f"Tweet kosong : {before-after}"

)

Console.title("MENGHAPUS DUPLIKAT")

before = len(df)

df = df.drop_duplicates(

subset=["full_text"]

)

after = len(df)

Console.success(

    f"Duplicate : {before-after}"

)

Console.title("MENYIMPAN DATASET")

save_path = RAW_DIR / RAW_FILENAME

df.to_csv(

save_path,

index=False,

encoding="utf-8-sig"

)

Console.success(

    f"Dataset disimpan : {save_path}"

)

Console.title("RINGKASAN DATASET")

print(df.head())

print()

print(df.info())

print()

print(df.describe(include="all"))

Console.title("CRAWLING SELESAI")

Console.success(

f"Dataset akhir : {len(df)} tweet"

)