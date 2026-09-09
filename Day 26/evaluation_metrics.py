# Day 26: precision, recall, confusion matrix

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1]

print(f"Accuracy: {accuracy_score(y_true, y_pred):.2f}")
print(f"Precision: {precision_score(y_true, y_pred):.2f}")
print(f"Recall: {recall_score(y_true, y_pred):.2f}")
print(f"Confusion Matrix:\n{confusion_matrix(y_true, y_pred)}")