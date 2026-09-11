# Day 28: numpy arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"Array: {arr}")
print(f"Mean: {arr.mean()}")
print(f"Sum: {arr.sum()}")
print(f"Squared: {arr ** 2}")

matrix = np.array([[1, 2], [3, 4]])
print(f"\nMatrix:\n{matrix}")
print(f"Transpose:\n{matrix.T}")