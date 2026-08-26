# Day 12: list comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

print(f"Squares: {squares}")
print(f"Evens: {evens}")