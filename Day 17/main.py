# Day 17 part 2: using the module

from helpers import is_prime

for num in range(1, 20):
    if is_prime(num):
        print(f"{num} is prime")