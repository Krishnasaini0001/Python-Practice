# Day 48: unsupervised learning - K-Means clustering

from sklearn.cluster import KMeans
import numpy as np

# fake customer data: [age, spending score]
X = np.array([[25, 80], [30, 85], [45, 20], [50, 15], [23, 90], [48, 25]])

model = KMeans(n_clusters=2, random_state=1, n_init=10)
model.fit(X)

print(f"Cluster labels: {model.labels_}")
print(f"Cluster centers: {model.cluster_centers_}")