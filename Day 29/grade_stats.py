# Day 29: using numpy for real stats

import numpy as np

grades = np.array([88, 72, 95, 60, 78, 85, 90])

print(f"Mean: {grades.mean():.1f}")
print(f"Median: {np.median(grades)}")
print(f"Std deviation: {grades.std():.2f}")
print(f"Above average: {grades[grades > grades.mean()]}")