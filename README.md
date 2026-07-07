# 🇮🇩 IndoBERT Sentiment Analysis for Indonesian Public Opinion on the Free Nutritious Meal Program

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![License](https://img.shields.io/badge/License-MIT-success)
![Status](https://img.shields.io/badge/Status-Production-success)

---

## 📖 Overview

This project implements an **Indonesian Sentiment Analysis System** using **IndoBERT** that has been fine-tuned to classify public opinions regarding the **Program Makan Bergizi Gratis (MBG)** into three sentiment categories:

- 😊 Positive
- 😐 Neutral
- 😠 Negative

The project covers the complete Machine Learning pipeline starting from data collection, preprocessing, manual labeling, model training, evaluation, deployment, and web visualization.

The trained model is deployed using **FastAPI** on **Railway**, while the frontend dashboard is hosted on **Vercel**, making the application accessible from anywhere through a web browser.

---

# ✨ Features

- Twitter/X Dataset Processing
- Text Cleaning
- Case Folding
- URL Removal
- Username Removal
- Emoji Removal
- Indonesian Text Normalization
- Slang Word Conversion
- Manual Labeling Assistant
- Confidence Validation
- Gold Dataset Generation
- Train / Validation / Test Split
- Fine-Tuning IndoBERT
- Model Evaluation
- FastAPI REST API
- Railway Cloud Deployment
- HuggingFace Model Repository
- Vercel Dashboard
- Real-Time Sentiment Prediction

---

# 🏗 System Architecture

```
Twitter / X
      │
      ▼
Crawler Dataset
      │
      ▼
Cleaning & Preprocessing
      │
      ▼
Normalization
      │
      ▼
Quality Checking
      │
      ▼
Manual Labeling
      │
      ▼
Gold Dataset
      │
      ▼
Train / Validation / Test Split
      │
      ▼
Fine-Tuning IndoBERT
      │
      ▼
Evaluation
      │
      ▼
Hugging Face Hub
      │
      ▼
Railway FastAPI
      │
      ▼
Vercel Dashboard
```

---

# 📂 Dataset

The dataset contains Indonesian public opinions related to the **Free Nutritious Meal Program (MBG)** collected from Twitter/X.

| Category | Total |
|----------|------:|
| Positive | 826 |
| Neutral | 216 |
| Negative | 479 |
| **Total** | **1521** |

Dataset Pipeline

```
Raw Dataset
        │
        ▼
Cleaning
        │
        ▼
Normalization
        │
        ▼
Quality Checking
        │
        ▼
Manual Labeling
        │
        ▼
Gold Dataset
```

---

# ⚙️ Preprocessing Pipeline

The preprocessing stage consists of several sequential steps:

### 1. Crawling

Collect tweets related to the Free Nutritious Meal Program.

### 2. Cleaning

- Remove URL
- Remove Mention
- Remove Hashtag
- Remove Emoji
- Remove HTML
- Remove Duplicate Characters
- Remove Punctuation

### 3. Case Folding

Convert all text into lowercase.

Example

```
Program MBG Sangat Bagus
↓

program mbg sangat bagus
```

### 4. Tokenization

Split sentences into individual tokens.

### 5. Stopword Removal

Remove common Indonesian stopwords.

### 6. Normalization

Convert slang words into formal Indonesian vocabulary.

Example

```
gk
↓

tidak

bgt
↓

banget
```

### 7. Quality Checking

Ensure every sentence is suitable for manual labeling.

---

# 🏷 Labeling Process

Labeling is performed manually using the built-in labeling assistant.

Three sentiment labels are used:

| Label | Description |
|--------|-------------|
| Positive | Supports or appreciates the program |
| Neutral | Informative or objective opinion |
| Negative | Criticism or dissatisfaction |

After manual labeling, a **Gold Dataset** is generated.

---

# 🤖 Model

Base Model

```
indobenchmark/indobert-base-p1
```

Framework

- PyTorch
- HuggingFace Transformers

Output Classes

- Positive
- Neutral
- Negative

---

# 🏋 Training Configuration

| Parameter | Value |
|-----------|------|
| Model | IndoBERT Base |
| Optimizer | AdamW |
| Scheduler | Linear |
| Epoch | Configurable |
| Batch Size | Configurable |
| Learning Rate | Configurable |

---

# 📊 Evaluation Result

| Metric | Score |
|---------|------:|
| Accuracy | **64.05%** |
| Precision | **62.72%** |
| Recall | **64.05%** |
| F1 Score | **63.18%** |

Classification Performance

| Label | Precision | Recall | F1 |
|-------|----------:|-------:|---:|
| Positive | 72.83% | 80.72% | 76.57% |
| Neutral | 31.58% | 27.27% | 29.27% |
| Negative | 59.52% | 52.08% | 55.56% |

---

# ☁ Deployment

The trained model is uploaded to Hugging Face Hub.

```
HuggingFace Hub

↓

Railway

↓

FastAPI

↓

Vercel Dashboard
```

Deployment Components

- HuggingFace Model Repository
- Railway API
- FastAPI Backend
- Vercel Frontend Dashboard

---

# 🌐 REST API

## Endpoint

```
POST /predict
```

Example Request

```json
{
    "text":"Program makan bergizi gratis sangat membantu masyarakat."
}
```

Example Response

```json
{
    "label":"positive",
    "confidence":0.9977,
    "probability":{
        "negative":0.0012,
        "neutral":0.0011,
        "positive":0.9977
    }
}
```

---

# 💻 Dashboard

The frontend dashboard provides:

- Real-time prediction
- Confidence score
- Probability visualization
- Copy result feature
- Responsive interface
- Railway API integration

---

# 📁 Project Structure

```
UAS-BERT-2313500122
│
├── app
│   ├── api
│   ├── deployment
│   ├── predictor
│   ├── training
│   └── labeling
│
├── dashboard
│   ├── css
│   ├── js
│   └── index.html
│
├── dataset
│
├── model
│
├── output
│
├── review
│
├── requirements.txt
├── README.md
├── LICENSE
├── run_project.bat
├── start_api.bat
├── start_dashboard.bat
└── stop_project.bat
```

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/vemsore/UAS-BERT.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run API

```bash
uvicorn app.api.main:app --reload
```

Run Dashboard

```bash
cd dashboard

python -m http.server 5500
```

Open Browser

```
http://127.0.0.1:5500
```

---

# 📦 Technology Stack

- Python 3.11
- PyTorch
- HuggingFace Transformers
- FastAPI
- Railway
- Vercel
- HTML
- CSS
- JavaScript
- Scikit-Learn
- Pandas
- NumPy

---

# 🛣 Roadmap

- ✅ Dataset Crawling
- ✅ Cleaning
- ✅ Normalization
- ✅ Manual Labeling
- ✅ Gold Dataset
- ✅ Fine-Tuning IndoBERT
- ✅ Evaluation
- ✅ FastAPI
- ✅ Railway Deployment
- ✅ Vercel Dashboard
- ⬜ Docker Deployment
- ⬜ User Authentication
- ⬜ Batch Prediction
- ⬜ Monitoring Dashboard

---

# 👨‍💻 Author

**Rekhan Fadhillah Syahputra**

NIM: **2313500122**

Computer Systems Engineering

Universitas Budi Luhur

GitHub

https://github.com/vemsore

HuggingFace

https://huggingface.co/Avemsoer

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for complete license information.

---

⭐ If you find this project useful, please consider giving it a star on GitHub.