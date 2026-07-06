"""
=========================================================
BUILD NLP ASSETS

Rekhan Fadhillah Syahputra
2313500122

Analisis Sentimen
Deep Learning IndoBERT

=========================================================
"""

from pathlib import Path
import pandas as pd

from config import *
from utils import Console

Console.title("BUILD NLP ASSETS")
ASSETS_DIR = ROOT_DIR / "assets"

ROOT = ASSETS_DIR

RAW = ROOT / "raw"

GENERATED = ROOT / "generated"

GENERATED.mkdir(
    parents=True,
    exist_ok=True
)

###############################################################
# HELPER
###############################################################

def clean_words(words):

    hasil = []

    for w in words:

        w = str(w).strip().lower()

        if len(w) < 2:
            continue

        hasil.append(w)

    return sorted(set(hasil))

###############################################################
# POSITIVE
###############################################################

Console.title("POSITIVE WORDS")

positive = []

###############################################################
# ID Opinion
###############################################################

file1 = RAW/"ID-OpinionWords-master"/"positive.txt"

with open(file1,encoding="utf-8") as f:

    positive += f.read().splitlines()

###############################################################
# InSet
###############################################################

file2 = RAW/"InSet-master"/"positive.tsv"

df = pd.read_csv(
    file2,
    sep="\t"
)

positive += df.iloc[:,0].tolist()

positive = clean_words(positive)

save = GENERATED/"positive_words.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n".join(positive))

Console.success(
    f"Positive : {len(positive)}"
)

###############################################################
# NEGATIVE
###############################################################

Console.title("NEGATIVE WORDS")

negative=[]

file1=RAW/"ID-OpinionWords-master"/"negative.txt"

with open(file1,encoding="utf-8") as f:

    negative+=f.read().splitlines()

file2=RAW/"InSet-master"/"negative.tsv"

df=pd.read_csv(
    file2,
    sep="\t"
)

negative+=df.iloc[:,0].tolist()

negative=clean_words(negative)

save=GENERATED/"negative_words.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(negative)
    )

Console.success(
    f"Negative : {len(negative)}"
)

###############################################################
# STOPWORDS
###############################################################

Console.title("STOPWORDS")

stop=[]

file=RAW/"NLP_bahasa_resources-master"/"combined_stop_words.txt"

with open(file,encoding="utf-8") as f:

    stop+=f.read().splitlines()

stop=clean_words(stop)

save=GENERATED/"stopwords.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(stop)
    )

Console.success(
    f"Stopwords : {len(stop)}"
)

###############################################################
# ROOT WORD
###############################################################

Console.title("ROOT WORD")

root=[]

file=RAW/"NLP_bahasa_resources-master"/"combined_root_words.txt"

with open(file,encoding="utf-8") as f:

    root+=f.read().splitlines()

root=clean_words(root)

save=GENERATED/"root_words.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(root)
    )

Console.success(
    f"Root Words : {len(root)}"
)

###############################################################
# BOOSTER
###############################################################

Console.title("BOOSTER")

booster=[

"sangat",
"amat",
"sekali",
"banget",
"teramat",
"terlalu",
"lebih",
"paling",
"makin",
"semakin"

]

save=GENERATED/"booster_words.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(booster)
    )

Console.success(
    f"Booster : {len(booster)}"
)

###############################################################
# NEGATION
###############################################################

Console.title("NEGATION")

negation=[

"tidak",
"tak",
"bukan",
"belum",
"jangan",
"enggak",
"ga",
"gak",
"gk",
"nggak",
"ngga"

]

save=GENERATED/"negation_words.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(negation)
    )

Console.success(
    f"Negation : {len(negation)}"
)

###############################################################
# POLICY WORDS
###############################################################

Console.title("POLICY WORDS")

policy=[

"bbm",
"subsidi",
"bansos",
"bpjs",
"ukt",
"ikn",
"presiden",
"menteri",
"dpr",
"mpr",
"kabinet",
"danantara",
"rupiah",
"inflasi",
"pajak",
"ppn",
"mahasiswa",
"kampus",
"korupsi",
"transparansi",
"efisiensi",
"anggaran",
"negara",
"apbn",
"ekonomi",
"politik",
"sosial"

]

save=GENERATED/"policy_words.txt"

with open(
    save,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(policy)
    )

Console.success(
    f"Policy : {len(policy)}"
)

Console.title("SELESAI")

Console.success(
    "Seluruh Asset berhasil dibuat."
)