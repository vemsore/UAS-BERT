# Analisis Sentimen Program Makan Bergizi Gratis Menggunakan IndoBERT

## Deskripsi

Project ini merupakan implementasi Fine-Tuning IndoBERT
untuk klasifikasi sentimen masyarakat Indonesia terhadap
Program Makan Bergizi Gratis.

Kategori:

- Positive
- Neutral
- Negative

--------------------------------------------------

## Dataset

Jumlah data :
1521 Tweet

Distribusi

Positive : 826
Negative : 479
Neutral  : 216

--------------------------------------------------

## Teknologi

Python
PyTorch
Transformers
FastAPI
IndoBERT
HTML
CSS
JavaScript

--------------------------------------------------

## Struktur Folder

app/
backend/
dashboard/
review/
dataset/
model/
output/

--------------------------------------------------

## Cara Menjalankan

1.

python -m uvicorn backend.main:app --reload

2.

cd dashboard

python -m http.server 5500

3.

Buka

http://127.0.0.1:5500

--------------------------------------------------

## Hasil Evaluasi

Accuracy : 64.05 %

Precision : 62.72 %

Recall : 64.05 %

F1 Score : 63.18 %

--------------------------------------------------

## Author

Rekhan Fadhillah Syahputra

2313500122

Universitas Budi Luhur


UAS-BERT-2313500122
│
├── app
├── backend
├── dashboard
├── dataset
├── model
├── output
│
├── README.md
├── LICENSE
├── requirements.txt
├── package.json
├── .gitignore
│
├── run_project.bat
├── start_api.bat
├── start_dashboard.bat
└── stop_project.bat