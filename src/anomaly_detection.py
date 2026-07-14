#Module 5
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

# ── LOAD ENGINEERED DATA ───────────────────────────────────────
cancer   = pd.read_csv('data/engineered/cancer_engineered.csv')
heart    = pd.read_csv('data/engineered/heart_engineered.csv')
diabetes = pd.read_csv('data/engineered/diabetes_engineered.csv')
gene     = pd.read_csv('data/engineered/gene_mutation_features.csv')

print("Loaded all engineered datasets")
print("Cancer:", cancer.shape)
print("Heart:", heart.shape)
print("Diabetes:", diabetes.shape)
print("Gene:", gene.shape)


# ── HELPER FUNCTION ────────────────────────────────────────────
def detect_anomalies(df, target_col, dataset_name):
    # Separate features from label
    X = df.drop(columns=[target_col])

    # Remove non-numeric columns if any
    X = X.select_dtypes(include=[np.number])

    # Isolation Forest
    # contamination=0.05 means we expect ~5% of data to be anomalies
    iso = IsolationForest(contamination=0.05, random_state=42)
    preds = iso.fit_predict(X)

    # Isolation Forest returns -1 for anomaly, 1 for normal
    # Convert to 0 = normal, 1 = anomaly
    df['anomaly_flag'] = (preds == -1).astype(int)

    anomaly_count = df['anomaly_flag'].sum()
    normal_count  = (df['anomaly_flag'] == 0).sum()

    print(f"\n{dataset_name}:")
    print(f"  Total samples : {len(df)}")
    print(f"  Normal        : {normal_count}")
    print(f"  Anomalies     : {anomaly_count}")

    return df, iso


# ── RUN ANOMALY DETECTION ON ALL DATASETS ─────────────────────
cancer,   iso_cancer   = detect_anomalies(cancer,   'target',       'Cancer')
heart,    iso_heart    = detect_anomalies(heart,     'target',       'Heart')
diabetes, iso_diabetes = detect_anomalies(diabetes,  'Outcome',      'Diabetes')
gene,     iso_gene     = detect_anomalies(gene,      'cancer_label', 'Gene')


# ── SAVE UPDATED DATASETS ──────────────────────────────────────
os.makedirs('data/engineered', exist_ok=True)
os.makedirs('models', exist_ok=True)

cancer.to_csv('data/engineered/cancer_engineered.csv',     index=False)
heart.to_csv('data/engineered/heart_engineered.csv',       index=False)
diabetes.to_csv('data/engineered/diabetes_engineered.csv', index=False)
gene.to_csv('data/engineered/gene_mutation_features.csv',  index=False)

# Save anomaly detectors — needed in prediction module
joblib.dump(iso_cancer,   'models/iso_cancer.pkl')
joblib.dump(iso_heart,    'models/iso_heart.pkl')
joblib.dump(iso_diabetes, 'models/iso_diabetes.pkl')
joblib.dump(iso_gene,     'models/iso_gene.pkl')

print("\nUpdated datasets saved with anomaly_flag column")
print("Anomaly detectors saved to models/")


# ── FINAL SUMMARY ─────────────────────────────────────────────
print("\n====== Module 5 Complete ======")
print("anomaly_flag column added to all 4 datasets")
print("  0 = normal sample")
print("  1 = anomalous sample")
print("Ready to move to Module 6 — Hybrid Model Training")