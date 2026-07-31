n = int(input())
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
difference = abs(n - reverse)
digits = len(str(difference))
print("Reverse =", reverse)
print("Difference =", difference)
print("Digits =", digits)
if difference == 0:
    print("Perfect Match")
elif difference % 9 == 0:
    print("Verified")
else:
    print("Rejected")