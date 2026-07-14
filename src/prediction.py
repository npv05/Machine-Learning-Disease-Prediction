#Module 7
import pandas as pd
import numpy as np
import joblib

# ── LOAD ALL MODELS AND SCALERS ────────────────────────────────
model_cancer   = joblib.load('models/model_cancer.pkl')
model_heart    = joblib.load('models/model_heart.pkl')
model_diabetes = joblib.load('models/model_diabetes.pkl')
model_gene     = joblib.load('models/model_gene.pkl')

scaler_cancer   = joblib.load('models/scaler_cancer.pkl')
scaler_heart    = joblib.load('models/scaler_heart.pkl')
scaler_diabetes = joblib.load('models/scaler_diabetes.pkl')

feat_cancer   = joblib.load('models/features_cancer.pkl')
feat_heart    = joblib.load('models/features_heart.pkl')
feat_diabetes = joblib.load('models/features_diabetes.pkl')
feat_gene     = joblib.load('models/features_gene.pkl')

le_gene = joblib.load('models/label_encoder_gene.pkl')

print("All models and scalers loaded successfully")
print("\nDiabetes features the model expects:")
print(feat_diabetes)


# ── HELPER: prepare input to match training features ───────────
def prepare_input(input_dict, feature_list):
    # Create a dataframe with all required columns set to 0.0 (float)
    df = pd.DataFrame(0.0, index=[0], columns=feature_list)

    # Fill in values from input_dict
    for col, val in input_dict.items():
        if col in feature_list:
            df[col] = float(val)

    return df


# ── PREDICTION FUNCTION ────────────────────────────────────────
def predict(disease, input_dict):

    if disease == 'cancer':
        X = prepare_input(input_dict, feat_cancer)
        pred = model_cancer.predict(X)[0]
        prob = model_cancer.predict_proba(X)[0]
        label = 'Malignant (Cancer)' if pred == 1 else 'Benign (No Cancer)'

    elif disease == 'heart':
        X = prepare_input(input_dict, feat_heart)
        pred = model_heart.predict(X)[0]
        prob = model_heart.predict_proba(X)[0]
        label = 'Heart Disease Detected' if pred == 1 else 'No Heart Disease'

    elif disease == 'diabetes':
        X = prepare_input(input_dict, feat_diabetes)
        pred = model_diabetes.predict(X)[0]
        prob = model_diabetes.predict_proba(X)[0]
        label = 'Diabetic' if pred == 1 else 'Not Diabetic'

    elif disease == 'gene':
        X = prepare_input(input_dict, feat_gene)
        pred = model_gene.predict(X)[0]
        prob = model_gene.predict_proba(X)[0]
        label = le_gene.inverse_transform([pred])[0]

    confidence = round(max(prob) * 100, 2)

    print(f"\n── Prediction Result ──")
    print(f"Disease   : {disease.upper()}")
    print(f"Prediction: {label}")
    print(f"Confidence: {confidence}%")

    return label, confidence


# ── TEST PREDICTIONS ───────────────────────────────────────────
# The feature names must exactly match what model was trained on
# Run this file first to print feat_diabetes, then use those names

print("\nTest 1 — Diabetes")
predict('diabetes', {
    'Pregnancies'             : 6,
    'Glucose'                 : 148,
    'BloodPressure'           : 72,
    'SkinThickness'           : 35,
    'Insulin'                 : 0,
    'BMI'                     : 33.6,
    'DiabetesPedigreeFunction': 0.627,
    'Age'                     : 50,
    'glucose_insulin'         : 148 * 0,
    'bmi_age'                 : 33.6 * 50,
    'glucose_bp_ratio'        : 148 / (72 + 1),
    'skin_bmi'                : 35 * 33.6,
    'anomaly_flag'            : 0
})

print("\nTest 2 — Heart")
predict('heart', {
    'age'             : 55,
    'trestbps'        : 130,
    'chol'            : 250,
    'thalach'         : 150,
    'oldpeak'         : 1.5,
    'thalach_age'     : 150 * 55,
    'chol_bp_ratio'   : 250 / (130 + 1),
    'anomaly_flag'    : 0
})

print("\n====== Module 7 Complete ======")
print("Prediction function ready for all 4 diseases")
print("Ready to move to Module 8 — Multi Disease Prediction")