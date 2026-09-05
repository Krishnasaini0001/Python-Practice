# Day 22: matplotlib basics
# install: pip install matplotlib

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
hours_studied = [1, 2, 1.5, 3, 2.5]
plt.plot(days, hours_studied, marker="o")
plt.title("Hours Studied per Day")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.savefig("study_chart.png")
plt.legend(["Hours Studied"])
plt.show()
print("Chart saved as study_chart.png")