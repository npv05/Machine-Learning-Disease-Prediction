#Module 6
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
import joblib
import os

# ── LOAD DATA ──────────────────────────────────────────────────
cancer   = pd.read_csv('data/engineered/cancer_engineered.csv')
heart    = pd.read_csv('data/engineered/heart_engineered.csv')
diabetes = pd.read_csv('data/engineered/diabetes_engineered.csv')
gene     = pd.read_csv('data/engineered/gene_mutation_features.csv')

print("All datasets loaded")


# ── TRAIN FUNCTION ─────────────────────────────────────────────
# Creates a FRESH hybrid model each time — fixes the overwriting bug
def train(df, target_col, name, drop_cols=[]):

    # Separate features and label
    remove = [target_col] + drop_cols
    remove = [c for c in remove if c in df.columns]

    X = df.drop(columns=remove).select_dtypes(include=[np.number])
    y = df[target_col]

    # Split: 80% train, 20% test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Create a FRESH hybrid model for each dataset
    rf  = RandomForestClassifier(n_estimators=100, random_state=42)
    xgb = XGBClassifier(n_estimators=100, random_state=42,
                        eval_metric='logloss', verbosity=0)
    hybrid = VotingClassifier(
        estimators=[('rf', rf), ('xgb', xgb)],
        voting='soft'
    )

    # Train
    hybrid.fit(X_train, y_train)

    # Evaluate
    y_pred   = hybrid.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\n── {name} ──")
    print(f"Samples  : {len(X)}")
    print(f"Features : {X.shape[1]}")
    print(f"Accuracy : {accuracy * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    return hybrid, X.columns.tolist()


# ── TRAIN ON ALL 4 DATASETS ────────────────────────────────────
model_cancer,   feat_cancer   = train(cancer,   'target',       'Breast Cancer')
model_heart,    feat_heart    = train(heart,     'target',       'Heart Disease')
model_diabetes, feat_diabetes = train(diabetes,  'Outcome',      'Diabetes')
model_gene,     feat_gene     = train(gene,      'cancer_label', 'Gene (ALL/AML)',
                                      drop_cols=['cancer'])


# ── SAVE MODELS ────────────────────────────────────────────────
os.makedirs('models', exist_ok=True)

joblib.dump(model_cancer,   'models/model_cancer.pkl')
joblib.dump(model_heart,    'models/model_heart.pkl')
joblib.dump(model_diabetes, 'models/model_diabetes.pkl')
joblib.dump(model_gene,     'models/model_gene.pkl')

joblib.dump(feat_cancer,    'models/features_cancer.pkl')
joblib.dump(feat_heart,     'models/features_heart.pkl')
joblib.dump(feat_diabetes,  'models/features_diabetes.pkl')
joblib.dump(feat_gene,      'models/features_gene.pkl')

print("\nAll models saved to models/")

print("\n====== Module 6 Complete ======")
print("Trained: Cancer, Heart, Diabetes, Gene")
print("Ready to move to Module 7 — Prediction Module")