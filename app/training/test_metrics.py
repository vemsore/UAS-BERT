"""
TEST METRICS
"""

import numpy as np

from app.training.metrics import (
    compute_metrics,
    print_metrics
)

# =====================================================
# Dummy Prediction
# =====================================================

labels = np.array([

    0,
    1,
    2,
    0,
    1,
    2

])

logits = np.array([

    [0.90,0.05,0.05],

    [0.10,0.80,0.10],

    [0.05,0.05,0.90],

    [0.70,0.20,0.10],

    [0.20,0.60,0.20],

    [0.10,0.10,0.80]

])

metrics = compute_metrics(

    (

        logits,

        labels

    )

)

print_metrics(metrics)