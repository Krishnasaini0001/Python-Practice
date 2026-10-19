# Day 59: saving a trained model for later use

from sklearn.linear_model import LinearRegression
import numpy as np
import joblib
# install: pip install joblib

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

loaded_model = joblib.load("model.pkl")
print(f"Loaded Model Prediction For 5: {loaded_model.predict([[5]])[0]}")