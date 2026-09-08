# Day 25: classification - pass/fail prediction

from sklearn.linear_model import LogisticRegression
import numpy as np

# hours studied vs pass(1)/fail(0)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

result = model.predict([[3.5]])
print(f"Prediction (0=fail, 1=pass): {result[0]}")