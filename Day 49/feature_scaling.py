# Day 49: why and how to scale features

from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1, 200], [2, 300], [3, 250], [4, 400]])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("Original:\n", data)
print("Scaled:\n", scaled_data)