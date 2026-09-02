# Day 19: intro to pandas
# install first: pip install pandas

import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print(f"\nAverage score: {df['score'].mean()}")
print(f"Top student: {df.loc[df['score'].idxmax(), 'name']}")