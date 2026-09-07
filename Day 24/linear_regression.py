# Day 24: predicting a number with linear regression

from sklearn.linear_model import LinearRegression
import numpy as np

# hours studied vs exam score
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 55, 65, 70, 80])

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[6]])
print(f"Predicted score for 6 hours studied: {predicted[0]:.1f}")