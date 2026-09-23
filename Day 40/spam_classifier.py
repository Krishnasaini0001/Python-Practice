# Day 40: mini project - simple spam classifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Win a free prize now",
    "Hey are we still on for lunch",
    "Claim your free money today",
    "Can you send me the report",
    "Congratulations you won a lottery",
    "Meeting moved to 3pm tomorrow",
]
labels = [1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

model = MultinomialNB()
model.fit(X, labels)

test_msg = ["Free lunch offer just for you"]
test_X = vectorizer.transform(test_msg)
prediction = model.predict(test_X)

print(f"Message: {test_msg[0]}")
print(f"Spam?: {'Yes' if prediction[0] == 1 else 'No'}")