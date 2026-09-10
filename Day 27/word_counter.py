# Day 27: word frequency counter

from collections import Counter

text = """Python is great. Python is easy to learn.
I love learning Python every day."""

words = text.lower().replace(".", "").split()
word_counts = Counter(words)

for word, count in word_counts.most_common(5):
    print(f"{word}: {count}")