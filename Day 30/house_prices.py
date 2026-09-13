# Day 30: predict house price from size (mini project)

from sklearn.linear_model import LinearRegression
import numpy as np

# size in sq ft vs price in $1000s
size = np.array([[750], [900], [1200], [1500], [1800], [2100]])
price = np.array([150, 175, 220, 260, 300, 340])

model = LinearRegression()
model.fit(size, price)

new_size = [[1600]]
predicted_price = model.predict(new_size)
print(f"Predicted price for 1600 sq ft: ${predicted_price[0]:.0f}k")
print(f"Model formula: price = {model.coef_[0]:.3f} * size + {model.intercept_:.1f}")