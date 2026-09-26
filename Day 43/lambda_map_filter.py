# Day 43: lambda, map, filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Squared: {squared}")
print(f"Evens: {evens}")