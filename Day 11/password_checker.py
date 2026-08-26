# Day 11: string methods

password = input("Enter a password: ")

has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
is_long_enough = len(password) >= 8

if has_upper and has_digit and is_long_enough:
    print("Strong password!")
else:
    print("Weak password. Needs: 8+ chars, uppercase, and a digit.")