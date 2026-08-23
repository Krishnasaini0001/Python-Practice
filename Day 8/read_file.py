# Day 8: reading from a file

with open("notes.txt", "r") as f:
    lines = f.readlines()

print("Your notes:")
for line in lines:
    print(f"- {line.strip()}")