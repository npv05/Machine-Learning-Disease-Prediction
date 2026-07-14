#Module 3
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

# ── LOAD PROCESSED DATA ────────────────────────────────────────
cancer   = pd.read_csv('data/processed/cancer.csv')
heart    = pd.read_csv('data/processed/heart.csv')
diabetes = pd.read_csv('data/processed/diabetes.csv')
gene     = pd.read_csv('data/processed/gene.csv')

print("Loaded successfully")
print("Cancer:", cancer.shape)
print("Heart:", heart.shape)
print("Diabetes:", diabetes.shape)
print("Gene:", gene.shape)


# ── CANCER: INTERACTION FEATURES ──────────────────────────────
# Combining mean + worst values gives a stronger signal
cancer['radius_area']          = cancer['mean radius']   * cancer['mean area']
cancer['compactness_concavity']= cancer['mean compactness'] * cancer['mean concavity']
cancer['worst_radius_area']    = cancer['worst radius']  * cancer['worst area']

print("\nCancer new columns added: radius_area, compactness_concavity, worst_radius_area")


# ── HEART: ENCODE CATEGORICAL + INTERACTION FEATURES ──────────
# These columns are categories stored as numbers — encode them
cat_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
cat_cols = [c for c in cat_cols if c in heart.columns]
heart = pd.get_dummies(heart, columns=cat_cols, drop_first=True)

# Interaction features
heart['thalach_age']     = heart['thalach'] * heart['age']
heart['chol_bp_ratio']   = heart['chol'] / (heart['trestbps'] + 1)

print("Heart categorical columns encoded")
print("Heart new columns added: thalach_age, chol_bp_ratio")
print("Heart shape after encoding:", heart.shape)


# ── DIABETES: INTERACTION FEATURES ────────────────────────────
diabetes['glucose_insulin']   = diabetes['Glucose'] * diabetes['Insulin']
diabetes['bmi_age']           = diabetes['BMI'] * diabetes['Age']
diabetes['glucose_bp_ratio']  = diabetes['Glucose'] / (diabetes['BloodPressure'] + 1)
diabetes['skin_bmi']          = diabetes['SkinThickness'] * diabetes['BMI']

print("\nDiabetes new columns added: glucose_insulin, bmi_age, glucose_bp_ratio, skin_bmi")


# ── GENE: NO MANUAL FEATURES ──────────────────────────────────
# Gene columns are already numbered expression values
# No interaction features needed — Module 4 handles gene-specific work
# Just drop the 'patient' column as it's an ID, not a feature
if 'patient' in gene.columns:
    gene = gene.drop(columns=['patient'])
    print("\nGene: dropped 'patient' column (ID column, not a feature)")
print("Gene shape:", gene.shape)


# ── SCALE ALL DATASETS ─────────────────────────────────────────
def scale_data(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    return X_scaled, y, scaler

X_cancer,   y_cancer,   scaler_cancer   = scale_data(cancer,   'target')
X_heart,    y_heart,    scaler_heart    = scale_data(heart,     'target')
X_diabetes, y_diabetes, scaler_diabetes = scale_data(diabetes,  'Outcome')

# Gene has no single target column yet — scaling done separately in Module 4
print("\nScaling done")
print("Cancer features:", X_cancer.shape[1])
print("Heart features:", X_heart.shape[1])
print("Diabetes features:", X_diabetes.shape[1])


# ── SAVE ENGINEERED DATASETS ───────────────────────────────────
os.makedirs('data/engineered', exist_ok=True)
os.makedirs('models', exist_ok=True)

X_cancer.assign(target=y_cancer.values).to_csv('data/engineered/cancer_engineered.csv',     index=False)
X_heart.assign(target=y_heart.values).to_csv('data/engineered/heart_engineered.csv',         index=False)
X_diabetes.assign(Outcome=y_diabetes.values).to_csv('data/engineered/diabetes_engineered.csv', index=False)
gene.to_csv('data/engineered/gene_engineered.csv', index=False)

# Save scalers — needed later in prediction module
joblib.dump(scaler_cancer,   'models/scaler_cancer.pkl')
joblib.dump(scaler_heart,    'models/scaler_heart.pkl')
joblib.dump(scaler_diabetes, 'models/scaler_diabetes.pkl')

print("\nEngineered datasets saved to data/engineered/")
print("Scalers saved to models/")


# ── FINAL SUMMARY ──────────────────────────────────────────────
print("\n====== Module 3 Complete ======")
print(f"Cancer   : {X_cancer.shape[1]} features")
print(f"Heart    : {X_heart.shape[1]} features")
print(f"Diabetes : {X_diabetes.shape[1]} features")
print(f"Gene     : {gene.shape[1]} columns (ready for Module 4)")
print("Ready to move to Module 4 — Mutation Feature Module")