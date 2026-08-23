num = input("Enter a number: ")

step_diff = []
sum_diff = 0
largest = 0

for i in range(len(num) - 1):
    diff = abs(int(num[i]) - int(num[i + 1]))
    step_diff.append(diff)
    sum_diff += diff

    if diff > largest:
        largest = diff

print("Step Differences:", *step_diff)
print("Sum =", sum_diff)
print("Largest =", largest)

if sum_diff % len(num) == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")