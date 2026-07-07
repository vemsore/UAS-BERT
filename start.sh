#!/usr/bin/env bash

echo "======================================="
echo "Starting UAS IndoBERT API"
echo "======================================="

uvicorn app.api.main:app \
    --host 0.0.0.0 \
    --port $PORT