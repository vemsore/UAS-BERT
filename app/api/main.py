"""
===========================================
FASTAPI
===========================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.predictor.predictor import predict

from app.api.schemas import (
    PredictRequest,
    PredictResponse
)

app = FastAPI(

    title="Analisis Sentimen IndoBERT",

    version="1.0.0",

    description="REST API Analisis Sentimen Bahasa Indonesia"

)

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/")
def home():

    return {

        "status": "running",

        "model": "IndoBERT",

        "author": "Rekhan Fadhillah Syahputra"

    }


@app.post(
    "/predict",
    response_model=PredictResponse
)

def predict_sentiment(

    request: PredictRequest

):

    result = predict(

        request.text

    )

    return result