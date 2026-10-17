# Day 57: first neural network with Keras
# install: pip install tensorflow

import tensorflow as tf
from tensorflow import keras
import numpy as np

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)  # y = 2x

model = keras.Sequential([keras.layers.Dense(1, input_shape=[1])])
model.compile(optimizer="sgd", loss="mean_squared_error")
model.fit(X, y, epochs=200, verbose=0)

print(f"Prediction for 10: {model.predict([10.0], verbose=0)[0][0]:.2f}")