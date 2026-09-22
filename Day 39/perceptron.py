# Day 39: building a simple perceptron with just numpy
# (this is what's under the hood of a basic neural network unit)

import numpy as np

def perceptron(inputs, weights, bias):
    total = np.dot(inputs, weights) + bias
    return 1 if total > 0 else 0

# simple AND gate
weights = np.array([1, 1])
bias = -1.5

for a in [0, 1]:
    for b in [0, 1]:
        result = perceptron(np.array([a, b]), weights, bias)
        print(f"{a} AND {b} = {result}")