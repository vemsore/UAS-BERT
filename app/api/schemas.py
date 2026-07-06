"""
===========================================
Pydantic Schema
===========================================
"""

from pydantic import BaseModel


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    text: str
    label: str
    confidence: float
    probability: dict