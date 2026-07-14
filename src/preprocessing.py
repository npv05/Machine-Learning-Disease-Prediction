# Module 1 and 2
import pandas as pd

# -----------------------------
# STEP 1: LOAD DATA
# -----------------------------
cancer = pd.read_csv("data/raw/breast_cancer.csv")
heart = pd.read_csv("data/raw/heart.csv")
diabetes = pd.read_csv("data/raw/diabetes.csv")

gene_train = pd.read_csv("data/raw/data_set_ALL_AML_train.csv")
labels = pd.read_csv("data/raw/actual.csv")

print("Data loaded successfully")


# -----------------------------
# STEP 2: CLEAN NORMAL DATASETS
# -----------------------------
cancer = cancer.dropna().drop_duplicates()
heart = heart.dropna().drop_duplicates()
diabetes = diabetes.dropna().drop_duplicates()

print("Basic datasets cleaned")


# -----------------------------
# STEP 3: PROCESS GENE DATA
# -----------------------------

# Convert columns → rows
gene_train = gene_train.transpose()

# Reset index
gene_train = gene_train.reset_index()

# Rename column
gene_train.rename(columns={'index': 'patient'}, inplace=True)
gene_train['patient'] = gene_train['patient'].astype(str)
labels['patient'] = labels['patient'].astype(str)

# -----------------------------
# STEP 4: PREPARE LABELS
# -----------------------------
labels.columns = ['patient', 'cancer']


# -----------------------------
# STEP 5: MERGE GENE + LABELS
# -----------------------------
gene_data = pd.merge(gene_train, labels, on='patient')


# -----------------------------
# STEP 6: ENCODE TARGET
# -----------------------------
gene_data['cancer'] = gene_data['cancer'].map({
    'ALL': 0,
    'AML': 1
})


# -----------------------------
# STEP 7: SAVE PROCESSED FILES
# -----------------------------
cancer.to_csv("data/processed/cancer.csv", index=False)
heart.to_csv("data/processed/heart.csv", index=False)
diabetes.to_csv("data/processed/diabetes.csv", index=False)
gene_data.to_csv("data/processed/gene.csv", index=False)

print("All datasets processed and saved!")