# Day 23: cleaning data with pandas

import pandas as pd

df = pd.read_csv("messy_data.csv")
print("Before cleaning:")
print(df)

df = df.drop_duplicates()
df = df.dropna()

print("\nAfter cleaning:")
print(df)