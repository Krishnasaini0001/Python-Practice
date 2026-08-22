# Day 5: functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

x = float(input("First number: "))
y = float(input("Second number: "))

print(f"Add: {add(x, y)}")
print(f"Subtract: {subtract(x, y)}")
print(f"Multiply: {multiply(x, y)}")
print(f"Divide: {divide(x, y)}")