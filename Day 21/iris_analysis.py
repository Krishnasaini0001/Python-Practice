# Day 21: combine pandas + sklearn

import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["species"] = data.target

print(df.head())
print("\nAverage measurements by species:")
print(df.groupby("species").mean())