# Day 47: visualizing a decision tree
# install: pip install matplotlib scikit-learn

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

data = load_iris()
model = DecisionTreeClassifier(max_depth=3)
model.fit(data.data, data.target)

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.savefig("tree.png")
print("Decision tree saved as tree.png")