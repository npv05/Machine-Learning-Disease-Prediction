### AI-Based Multi-Disease Prediction System with Mutation Enhancement

A machine learning system that predicts 4 diseases — Breast Cancer, Heart Disease,
Diabetes, and Gene Expression (ALL/AML) — using a Hybrid Random Forest + XGBoost model
with mutation-based feature engineering.

---

## 📋 Project Overview

| Detail | Info |
|---|---|
| Project Type | College Final Year Project |
| Domain | Bioinformatics + Machine Learning |
| Languages | Python 3.13 |
| ML Models | Random Forest + XGBoost (Hybrid) |
| Frontend | Streamlit |
| Backend API | FastAPI |

---

## 🧬 Datasets Used

| Disease | Dataset | Source | Samples |
|---|---|---|---|
| Breast Cancer | Wisconsin Breast Cancer Dataset | Kaggle | 569 |
| Heart Disease | Cleveland Heart Disease Dataset | Kaggle | 302 |
| Diabetes | Pima Indians Diabetes Dataset | Kaggle | 768 |
| Gene Expression | ALL/AML Leukemia Dataset | Kaggle | 72 |

---

## ⚙️ Development Environment Setup

### Requirements
- Python 3.13
- Windows 10/11
- VS Code
- Virtual Environment (venv)

### Step 1 — Clone or download the project
```bash
cd D:\
mkdir project
cd project
```

### Step 2 — Create virtual environment
```bash
python -m venv venv
```

### Step 3 — Activate virtual environment
```bash
venv\Scripts\activate
```

### Step 4 — Install all libraries
```bash
pip install -r requirements.txt
```

---

## 📦 Libraries Used

| Library | Version | Purpose |
|---|---|---|
| pandas | latest | Data loading and manipulation |
| numpy | latest | Numerical operations |
| scikit-learn | latest | ML models and preprocessing |
| xgboost | latest | XGBoost classifier |
| joblib | latest | Saving and loading models |
| matplotlib | latest | Plotting graphs |
| seaborn | latest | Beautiful visualizations |
| streamlit | latest | Web dashboard UI |
| fastapi | latest | REST API backend |
| uvicorn | latest | ASGI server for FastAPI |
| requests | latest | HTTP requests from Streamlit to FastAPI |
| pydantic | latest | Data validation for FastAPI |
| biopython | latest | Biological data processing |
| pyod | latest | Anomaly detection |

---

## 🚀 How to Run the Project

### Step 1 — Run all modules in order (first time only)
```bash
python src/preprocessing.py
python src/feature_engg.py
python src/mutations_features.py
python src/anomaly_detection.py
python src/model_training.py
python src/evaluation.py
```

### Step 2 — Start the FastAPI backend
Open Terminal 1:
```bash
cd D:\nandini\project\src
python api_full.py
```

### Step 3 — Start the Streamlit dashboard
Open Terminal 2:
```bash
cd D:\nandini\project
streamlit run src/dashboard/main.py
```

### Step 4 — Open in browser
- **Dashboard:** http://localhost:8501
- **API docs:** http://127.0.0.1:8000/docs

---

## 🤖 Model Performance

| Disease | Accuracy | AUC |
|---|---|---|
| Breast Cancer | 95.61% | ~0.98 |
| Heart Disease | 78.69% | ~0.85 |
| Diabetes | 75.32% | ~0.82 |
| Gene (ALL/AML) | 86.67% | ~0.90 |

---

## 📊 Key Innovations

1. **Hybrid Model** — Combines Random Forest and XGBoost using soft voting for higher accuracy than either model alone
2. **Mutation Feature Engineering** — Extracts gene expression statistics (mean, std, range, mutation flag) as additional biological signals
3. **Anomaly Detection** — Uses Isolation Forest to flag unusual patient samples before prediction
4. **Multi-Disease System** — Single unified system predicts across 4 completely different diseases
5. **FastAPI Backend** — Production-ready REST API with input validation and structured responses

---

## 👩‍💻 Developer

**Nandini**
Bioinformatics ML Project
April 2026