# Day 10: try/except

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except ValueError:
        return "Error: invalid input"

num1 = input("First number: ")
num2 = input("Second number: ")

try:
    result = safe_divide(float(num1), float(num2))
    print(result)
except ValueError:
    print("Please enter valid numbers.")