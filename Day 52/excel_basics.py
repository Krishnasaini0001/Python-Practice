# Day 52: reading/writing Excel with pandas
# install: pip install openpyxl

import pandas as pd

df = pd.DataFrame({
    "name": ["Alex", "Sam", "Jordan"],
    "score": [88, 72, 95]
})

df.to_excel("scores.xlsx", index=False)

loaded = pd.read_excel("scores.xlsx")
print(loaded)