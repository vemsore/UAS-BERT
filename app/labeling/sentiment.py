"""
=========================================================
SENTIMENT ENGINE

Rekhan Fadhillah Syahputra
2313500122

Analisis Sentimen
Deep Learning IndoBERT

=========================================================
"""

from typing import Dict

from app.labeling.assets_loader import AssetsLoader
from app.labeling.tokenizer import IndonesianTokenizer


class SentimentEngine:

    def __init__(self, assets_dir):

        loader = AssetsLoader(assets_dir)

        assets = loader.load_all()

        self.positive = assets["positive"]
        self.negative = assets["negative"]
        self.policy = assets["policy"]
        self.booster = assets["booster"]
        self.negation = assets["negation"]

        self.tokenizer = IndonesianTokenizer()

    # ======================================================
    # ANALYZE
    # ======================================================

    def analyze(self, text: str) -> Dict:

        tokens = self.tokenizer.tokenize(text)

        positive_score = 0
        negative_score = 0
        booster_score = 0
        negation_score = 0
        policy_score = 0

        positive_words = []
        negative_words = []
        booster_words = []
        negation_words = []
        policy_words = []

        previous_token = ""

        for token in tokens:

            # -------------------------------
            # Booster
            # -------------------------------

            if token in self.booster:

                booster_score += 1

                booster_words.append(token)

            # -------------------------------
            # Policy
            # -------------------------------

            if token in self.policy:

                policy_score += 1

                policy_words.append(token)

            # -------------------------------
            # Negation
            # -------------------------------

            if token in self.negation:

                negation_score += 1

                negation_words.append(token)

                previous_token = token

                continue

            # -------------------------------
            # Positive
            # -------------------------------

            if token in self.positive:

                if previous_token in self.negation:

                    negative_score += 1
                    negative_words.append(token)

                else:

                    positive_score += 1
                    positive_words.append(token)

            # -------------------------------
            # Negative
            # -------------------------------

            elif token in self.negative:

                if previous_token in self.negation:

                    positive_score += 1
                    positive_words.append(token)

                else:

                    negative_score += 1
                    negative_words.append(token)

            previous_token = token

        # -----------------------------------
        # Booster Effect
        # -----------------------------------

        positive_score += booster_score * 0.5

        negative_score += booster_score * 0.5

        return {

            "tokens": tokens,

            "positive_score": round(positive_score,2),

            "negative_score": round(negative_score,2),

            "booster_score": booster_score,

            "negation_score": negation_score,

            "policy_score": policy_score,

            "positive_words": positive_words,

            "negative_words": negative_words,

            "booster_words": booster_words,

            "negation_words": negation_words,

            "policy_words": policy_words

        }


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    from config import ASSETS_DIR

    engine = SentimentEngine(

        ASSETS_DIR / "generated"

    )

    kalimat = """

    pemerintah sangat membantu mahasiswa
    melalui subsidi pendidikan

    """

    hasil = engine.analyze(kalimat)

    print("="*60)

    for k,v in hasil.items():

        print(f"{k:20} : {v}")

    print("="*60)