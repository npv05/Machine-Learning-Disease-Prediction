from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from prediction import predict

app = FastAPI(title="Disease Prediction API")


# ── HEALTH CHECK ───────────────────────────────────────────────
@app.get("/")
def home():
    return {"message": "Disease Prediction API is running"}


# ── DIABETES ───────────────────────────────────────────────────
@app.get("/predict/diabetes")
def predict_diabetes(
    Pregnancies: int,
    Glucose: float,
    BloodPressure: float,
    SkinThickness: float,
    Insulin: float,
    BMI: float,
    DiabetesPedigreeFunction: float,
    Age: int
):
    input_data = {
        'Pregnancies'             : Pregnancies,
        'Glucose'                 : Glucose,
        'BloodPressure'           : BloodPressure,
        'SkinThickness'           : SkinThickness,
        'Insulin'                 : Insulin,
        'BMI'                     : BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age'                     : Age,
        'glucose_insulin'         : Glucose * Insulin,
        'bmi_age'                 : BMI * Age,
        'glucose_bp_ratio'        : Glucose / (BloodPressure + 1),
        'skin_bmi'                : SkinThickness * BMI,
        'anomaly_flag'            : 0
    }
    label, conf = predict('diabetes', input_data)
    return {"disease": "Diabetes", "prediction": label, "confidence": f"{conf}%"}


# ── HEART DISEASE ──────────────────────────────────────────────
@app.get("/predict/heart")
def predict_heart(
    age: int,
    trestbps: float,
    chol: float,
    thalach: float,
    oldpeak: float
):
    input_data = {
        'age'           : age,
        'trestbps'      : trestbps,
        'chol'          : chol,
        'thalach'       : thalach,
        'oldpeak'       : oldpeak,
        'thalach_age'   : thalach * age,
        'chol_bp_ratio' : chol / (trestbps + 1),
        'anomaly_flag'  : 0
    }
    label, conf = predict('heart', input_data)
    return {"disease": "Heart Disease", "prediction": label, "confidence": f"{conf}%"}


# ── BREAST CANCER ──────────────────────────────────────────────
@app.get("/predict/cancer")
def predict_cancer(
    mean_radius: float,
    mean_texture: float,
    mean_perimeter: float,
    mean_area: float,
    mean_smoothness: float,
    mean_compactness: float,
    mean_concavity: float,
    mean_concave_points: float,
    worst_radius: float,
    worst_area: float
):
    input_data = {
        'mean radius'           : mean_radius,
        'mean texture'          : mean_texture,
        'mean perimeter'        : mean_perimeter,
        'mean area'             : mean_area,
        'mean smoothness'       : mean_smoothness,
        'mean compactness'      : mean_compactness,
        'mean concavity'        : mean_concavity,
        'mean concave points'   : mean_concave_points,
        'radius_area'           : mean_radius * mean_area,
        'compactness_concavity' : mean_compactness * mean_concavity,
        'worst_radius_area'     : worst_radius * worst_area,
        'anomaly_flag'          : 0
    }
    label, conf = predict('cancer', input_data)
    return {"disease": "Breast Cancer", "prediction": label, "confidence": f"{conf}%"}


# ── GENE (ALL/AML) ─────────────────────────────────────────────
@app.get("/predict/gene")
def predict_gene(
    mean_expression: float,
    std_expression: float,
    max_expression: float,
    min_expression: float,
    expression_range: float,
    mutation_flag: int
):
    input_data = {
        'mean_expression'  : mean_expression,
        'std_expression'   : std_expression,
        'max_expression'   : max_expression,
        'min_expression'   : min_expression,
        'expression_range' : expression_range,
        'mutation_flag'    : mutation_flag,
        'anomaly_flag'     : 0
    }
    label, conf = predict('gene', input_data)
    return {"disease": "Gene (ALL/AML)", "prediction": label, "confidence": f"{conf}%"}