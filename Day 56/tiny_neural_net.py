# Day 56: a tiny neural network with just numpy (no frameworks)

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# XOR-like tiny example
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
weights = np.random.rand(2)
bias = np.random.rand(1)

for row in inputs:
    z = np.dot(row, weights) + bias
    output = sigmoid(z)
    print(f"Input: {row}, Output: {output[0]:.3f}")