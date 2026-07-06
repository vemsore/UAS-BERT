"""
=========================================================
CONFIDENCE ENGINE

Rekhan Fadhillah Syahputra
2313500122

Analisis Sentimen
Deep Learning IndoBERT

=========================================================
"""

from typing import Dict


class ConfidenceEngine:

    def __init__(self):

        self.review_threshold = 0.65

    # =====================================================

    def calculate(self, result: Dict):

        pos = result["positive_score"]
        neg = result["negative_score"]

        booster = result["booster_score"]
        negation = result["negation_score"]
        policy = result["policy_score"]

        total_token = max(
            len(result["tokens"]),
            1
        )

        # -----------------------------------------
        # menentukan label
        # -----------------------------------------

        if pos > neg:

            label = "positive"

        elif neg > pos:

            label = "negative"

        else:

            label = "neutral"

        # -----------------------------------------
        # selisih score
        # -----------------------------------------

        diff = abs(pos - neg)

        # -----------------------------------------
        # density score
        # -----------------------------------------

        density = (pos + neg) / total_token

        # -----------------------------------------
        # booster effect
        # -----------------------------------------

        booster_bonus = booster * 0.03

        # -----------------------------------------
        # policy effect
        # -----------------------------------------

        policy_bonus = policy * 0.02

        # -----------------------------------------
        # negation penalty
        # -----------------------------------------

        negation_penalty = negation * 0.02

        # -----------------------------------------
        # confidence
        # -----------------------------------------

        confidence = (

            0.45 +

            diff * 0.15 +

            density * 0.25 +

            booster_bonus +

            policy_bonus -

            negation_penalty

        )

        confidence = max(

            0,

            min(

                confidence,

                1

            )

        )

        # -----------------------------------------
        # need review
        # -----------------------------------------

        need_review = confidence < self.review_threshold

        return {

            "label": label,

            "confidence": round(

                confidence,

                4

            ),

            "need_review": need_review

        }


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    sample = {

        "tokens":[

            "program",

            "pemerintah",

            "sangat",

            "membantu",

            "mahasiswa"

        ],

        "positive_score":2,

        "negative_score":0,

        "booster_score":1,

        "negation_score":0,

        "policy_score":2

    }

    engine = ConfidenceEngine()

    hasil = engine.calculate(sample)

    print("="*60)

    for k,v in hasil.items():

        print(f"{k:15} : {v}")

    print("="*60)