#Module 9
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, roc_auc_score,
    roc_curve, auc
)

# ── LOAD DATA ──────────────────────────────────────────────────
cancer   = pd.read_csv('data/engineered/cancer_engineered.csv')
heart    = pd.read_csv('data/engineered/heart_engineered.csv')
diabetes = pd.read_csv('data/engineered/diabetes_engineered.csv')
gene     = pd.read_csv('data/engineered/gene_mutation_features.csv')

# ── LOAD MODELS ────────────────────────────────────────────────
model_cancer   = joblib.load('models/model_cancer.pkl')
model_heart    = joblib.load('models/model_heart.pkl')
model_diabetes = joblib.load('models/model_diabetes.pkl')
model_gene     = joblib.load('models/model_gene.pkl')

feat_cancer   = joblib.load('models/features_cancer.pkl')
feat_heart    = joblib.load('models/features_heart.pkl')
feat_diabetes = joblib.load('models/features_diabetes.pkl')
feat_gene     = joblib.load('models/features_gene.pkl')

os.makedirs('outputs', exist_ok=True)
print("All models and data loaded")


# ── HELPER: get X and y ────────────────────────────────────────
def get_xy(df, target_col, feature_list, drop_cols=[]):
    remove = [target_col] + drop_cols
    remove = [c for c in remove if c in df.columns]
    X = df.drop(columns=remove).select_dtypes(include=[np.number])
    X = X[feature_list]
    y = df[target_col]
    return X, y


# ── PLOT 1: CONFUSION MATRIX ───────────────────────────────────
def plot_confusion_matrix(y_test, y_pred, name, labels):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    plt.title(f'Confusion Matrix — {name}')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    path = f'outputs/confusion_{name.lower().replace(" ", "_")}.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ── PLOT 2: ROC CURVE ──────────────────────────────────────────
def plot_roc_curve(model, X_test, y_test, name):
    try:
        y_prob      = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc     = auc(fpr, tpr)

        plt.figure(figsize=(6, 4))
        plt.plot(fpr, tpr, color='darkorange', lw=2,
                 label=f'AUC = {roc_auc:.2f}')
        plt.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'ROC Curve — {name}')
        plt.legend(loc='lower right')
        plt.tight_layout()
        path = f'outputs/roc_{name.lower().replace(" ", "_")}.png'
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"  Saved: {path} — AUC: {roc_auc:.2f}")
    except Exception as e:
        print(f"  ROC skipped: {e}")


# ── PLOT 3: FEATURE IMPORTANCE ─────────────────────────────────
def plot_feature_importance(model, feature_list, name, top_n=15):
    try:
        rf_model    = model.estimators_[0]
        importances = rf_model.feature_importances_
        feat_imp    = pd.Series(importances, index=feature_list)
        top_feats   = feat_imp.sort_values(ascending=False).head(top_n)

        plt.figure(figsize=(8, 5))
        top_feats.sort_values().plot(kind='barh', color='steelblue')
        plt.title(f'Top {top_n} Feature Importances — {name}')
        plt.xlabel('Importance Score')
        plt.tight_layout()
        path = f'outputs/feature_importance_{name.lower().replace(" ", "_")}.png'
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"  Saved: {path}")
    except Exception as e:
        print(f"  Feature importance skipped: {e}")


# ── EVALUATE ALL 4 DATASETS ────────────────────────────────────
datasets = [
    (cancer,   'target',       'Breast Cancer', model_cancer,
     feat_cancer,   ['Benign', 'Malignant'], []),

    (heart,    'target',       'Heart Disease', model_heart,
     feat_heart,    ['No Disease', 'Disease'], []),

    (diabetes, 'Outcome',      'Diabetes',      model_diabetes,
     feat_diabetes, ['Not Diabetic', 'Diabetic'], []),

    (gene,     'cancer_label', 'Gene ALL AML',  model_gene,
     feat_gene,     ['ALL', 'AML'], ['cancer']),
]

summary = []

for df, target, name, model, features, labels, drop in datasets:
    print(f"\n── {name} ──")

    X, y = get_xy(df, target, features, drop_cols=drop)

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    acc    = accuracy_score(y_test, y_pred)

    try:
        auc_score = roc_auc_score(y_test, y_prob)
    except:
        auc_score = 0.0

    print(f"  Accuracy : {acc * 100:.2f}%")
    print(f"  AUC Score: {auc_score:.2f}")
    print(classification_report(y_test, y_pred, target_names=labels))

    plot_confusion_matrix(y_test, y_pred, name, labels)
    plot_roc_curve(model, X_test, y_test, name)
    plot_feature_importance(model, features, name)

    summary.append({
        'Disease' : name,
        'Accuracy': f"{acc * 100:.2f}%",
        'AUC'     : f"{auc_score:.2f}"
    })


# ── SAVE SUMMARY CSV ───────────────────────────────────────────
summary_df = pd.DataFrame(summary)
summary_df.to_csv('outputs/evaluation_summary.csv', index=False)


# ── PRINT SUMMARY ──────────────────────────────────────────────
print("\n" + "="*45)
print("         FINAL EVALUATION SUMMARY")
print("="*45)
for row in summary:
    print(f"{row['Disease']:<20}: Accuracy={row['Accuracy']}  AUC={row['AUC']}")
print("="*45)
print("\nAll plots and summary saved to outputs/")

print("\n====== Module 9 Complete ======")
print("Saved: Confusion Matrices, ROC Curves, Feature Importances")
print("Saved: outputs/evaluation_summary.csv")
print("Ready to move to Module 10 — Streamlit Dashboard")