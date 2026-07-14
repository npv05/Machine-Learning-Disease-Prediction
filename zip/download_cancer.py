from sklearn.datasets import load_breast_cancer
import pandas as pd

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

df.to_csv("breast_cancer.csv", index=False)

print("Breast cancer dataset saved!")