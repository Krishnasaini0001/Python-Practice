# Day 2: if/else conditionals

age = int(input("How old are you? "))

if age >= 18:
    print("You're an adult.")
else:
    years_left = 18 - age
    print(f"You have {years_left} years until you're an adult.")