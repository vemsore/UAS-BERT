"""
=========================================================
ASSETS LOADER

Rekhan Fadhillah Syahputra
2313500122

Analisis Sentimen
Deep Learning IndoBERT
=========================================================
"""

from pathlib import Path

class AssetsLoader:

    def __init__(self, assets_dir):

        self.assets_dir = Path(assets_dir)

    # --------------------------------------------------

    def load_txt(self, filename):

        file = self.assets_dir / filename

        with open(
            file,
            encoding="utf-8"
        ) as f:

            data = {

                line.strip().lower()

                for line in f

                if line.strip()

            }

        return data

    # --------------------------------------------------

    def load_positive(self):

        return self.load_txt(

            "positive_words.txt"

        )

    # --------------------------------------------------

    def load_negative(self):

        return self.load_txt(

            "negative_words.txt"

        )

    # --------------------------------------------------

    def load_stopwords(self):

        return self.load_txt(

            "stopwords.txt"

        )

    # --------------------------------------------------

    def load_booster(self):

        return self.load_txt(

            "booster_words.txt"

        )

    # --------------------------------------------------

    def load_negation(self):

        return self.load_txt(

            "negation_words.txt"

        )

    # --------------------------------------------------

    def load_policy(self):

        return self.load_txt(

            "policy_words.txt"

        )

    # --------------------------------------------------

    def load_root(self):

        return self.load_txt(

            "root_words.txt"

        )

    # --------------------------------------------------

    def load_all(self):

        return {

            "positive": self.load_positive(),

            "negative": self.load_negative(),

            "stopwords": self.load_stopwords(),

            "booster": self.load_booster(),

            "negation": self.load_negation(),

            "policy": self.load_policy(),

            "root": self.load_root()

        }
