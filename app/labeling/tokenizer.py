"""
=========================================================
INDONESIAN TOKENIZER

Rekhan Fadhillah Syahputra
2313500122

Analisis Sentimen
Deep Learning IndoBERT

=========================================================
"""

import re


class IndonesianTokenizer:
    """
    Tokenizer sederhana untuk dataset yang sudah
    melalui proses preprocessing dan normalization.
    """

    def __init__(self):
        # hanya mengambil huruf a-z
        self.pattern = re.compile(r"[a-z]+")

    # =====================================================
    # TOKENIZE
    # =====================================================

    def tokenize(self, text: str):

        if text is None:
            return []

        text = str(text).lower()

        tokens = self.pattern.findall(text)

        return tokens

    # =====================================================
    # TOKEN COUNT
    # =====================================================

    def count(self, text):

        return len(self.tokenize(text))

    # =====================================================
    # UNIQUE TOKEN
    # =====================================================

    def unique(self, text):

        return sorted(set(self.tokenize(text)))

    # =====================================================
    # DETOKENIZE
    # =====================================================

    def detokenize(self, tokens):

        return " ".join(tokens)

    # =====================================================
    # NGRAM
    # =====================================================

    def ngrams(self, tokens, n=2):

        hasil = []

        if len(tokens) < n:
            return hasil

        for i in range(len(tokens) - n + 1):
            hasil.append(tuple(tokens[i:i+n]))

        return hasil

    # =====================================================
    # BIGRAM
    # =====================================================

    def bigram(self, text):

        return self.ngrams(
            self.tokenize(text),
            2
        )

    # =====================================================
    # TRIGRAM
    # =====================================================

    def trigram(self, text):

        return self.ngrams(
            self.tokenize(text),
            3
        )

    # =====================================================
    # TOKEN INFO
    # =====================================================

    def info(self, text):

        tokens = self.tokenize(text)

        return {
            "tokens": tokens,
            "jumlah": len(tokens),
            "unik": len(set(tokens))
        }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    tokenizer = IndonesianTokenizer()

    kalimat = """
    Program pemerintah sangat membantu masyarakat
    """

    print("=" * 60)

    print(tokenizer.info(kalimat))

    print("=" * 60)

    print(tokenizer.bigram(kalimat))

    print("=" * 60)

    print(tokenizer.trigram(kalimat))