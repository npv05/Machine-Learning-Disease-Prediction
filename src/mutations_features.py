#Module 4
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# ── LOAD RAW GENE DATA ─────────────────────────────────────────
train_raw = pd.read_csv('data/raw/data_set_ALL_AML_train.csv')
test_raw  = pd.read_csv('data/raw/data_set_ALL_AML_independent.csv')
actual    = pd.read_csv('data/raw/actual.csv')

print("Train raw shape:", train_raw.shape)
print("Test raw shape :", test_raw.shape)
print("Actual shape   :", actual.shape)

# ── STEP 1: CLEAN AND TRANSPOSE ────────────────────────────────
# The data has genes as rows, patients as columns
# We need patients as rows, genes as columns

# Keep only numeric patient columns (drop Gene Description, Accession, call columns)
def clean_gene_data(df):
    # Drop non-numeric columns and "call" columns
    # Patient expression columns are numeric — call columns contain letters like A/P
    numeric_cols = []
    for col in df.columns:
        try:
            pd.to_numeric(df[col])
            numeric_cols.append(col)
        except:
            pass

    df_clean = df[numeric_cols].copy()

    # Transpose: genes become columns, patients become rows
    df_transposed = df_clean.T
    df_transposed.columns = [f'gene_{i}' for i in range(df_transposed.shape[1])]
    df_transposed = df_transposed.reset_index(drop=True)

    return df_transposed

gene_train = clean_gene_data(train_raw)
gene_test  = clean_gene_data(test_raw)

print("\nAfter cleaning and transposing:")
print("Train shape:", gene_train.shape)
print("Test shape :", gene_test.shape)

# ── STEP 2: ATTACH LABELS ──────────────────────────────────────
train_labels = actual.iloc[:len(gene_train)]['cancer'].values
test_labels  = actual.iloc[len(gene_train):len(gene_train)+len(gene_test)]['cancer'].values

gene_train['cancer'] = train_labels
gene_test['cancer']  = test_labels

# Combine into one full dataset
gene = pd.concat([gene_train, gene_test], ignore_index=True)

print("\nCombined gene shape:", gene.shape)
print("Label distribution:")
print(gene['cancer'].value_counts())

# ── STEP 3: MUTATION SUMMARY FEATURES ─────────────────────────
feature_cols = [c for c in gene.columns if c != 'cancer']

gene['mean_expression']  = gene[feature_cols].mean(axis=1)
gene['std_expression']   = gene[feature_cols].std(axis=1)
gene['max_expression']   = gene[feature_cols].max(axis=1)
gene['min_expression']   = gene[feature_cols].min(axis=1)
gene['expression_range'] = gene['max_expression'] - gene['min_expression']

print("\nMutation summary features added")

# ── STEP 4: MUTATION FLAG ──────────────────────────────────────
threshold = gene['std_expression'].mean() + gene['std_expression'].std()
gene['mutation_flag'] = (gene['std_expression'] > threshold).astype(int)

print(f"Mutation threshold : {threshold:.4f}")
print(f"Mutation flagged   : {gene['mutation_flag'].sum()} samples")
print(f"Normal             : {(gene['mutation_flag'] == 0).sum()} samples")

# ── STEP 5: SELECT TOP 100 VARIABLE GENES ─────────────────────
gene_variances = gene[feature_cols].var().sort_values(ascending=False)
top_100_genes  = gene_variances.head(100).index.tolist()

print(f"\nTop 100 genes selected from {len(feature_cols)} total genes")

# ── STEP 6: BUILD FINAL FEATURE SET ───────────────────────────
mutation_cols = [
    'mean_expression',
    'std_expression',
    'max_expression',
    'min_expression',
    'expression_range',
    'mutation_flag'
]

gene_final = gene[top_100_genes + mutation_cols + ['cancer']].copy()

# ── STEP 7: ENCODE LABEL ──────────────────────────────────────
le = LabelEncoder()
gene_final['cancer_label'] = le.fit_transform(gene_final['cancer'])

print("\nLabel encoding:")
for label, encoded in zip(le.classes_, le.transform(le.classes_)):
    print(f"  {label} → {encoded}")

print("\nFinal gene dataset shape:", gene_final.shape)

# ── SAVE ──────────────────────────────────────────────────────
os.makedirs('data/engineered', exist_ok=True)
os.makedirs('models', exist_ok=True)

gene_final.to_csv('data/engineered/gene_mutation_features.csv', index=False)
joblib.dump(le,            'models/label_encoder_gene.pkl')
joblib.dump(top_100_genes, 'models/top_100_genes.pkl')

print("\nFiles saved successfully")

# ── SUMMARY ───────────────────────────────────────────────────
print("\n====== Module 4 Complete ======")
print(f"Total samples : {gene_final.shape[0]}")
print(f"Total features: {gene_final.shape[1] - 2}")
print(f"ALL samples   : {(gene_final['cancer'] == 'ALL').sum()}")
print(f"AML samples   : {(gene_final['cancer'] == 'AML').sum()}")
print("Ready for Module 5")