number = input("Enter a number: ")

sum_diff = 0
largest_diff = 0

print("\nStep Differences:")

for i in range(len(number) - 1):
    digit1 = int(number[i])
    digit2 = int(number[i + 1])

    diff = abs(digit1 - digit2)

    print(f"|{digit1} - {digit2}| = {diff}")

    sum_diff += diff

    if diff > largest_diff:
        largest_diff = diff

print("\nSum of Step Differences =", sum_diff)
print("Largest Step Difference =", largest_diff)

if sum_diff % len(number) == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")