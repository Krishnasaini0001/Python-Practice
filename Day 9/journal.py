# Day 9: writing to a file

entry = input("Write today's journal entry: ")

with open("journal.txt", "a") as f:
    f.write(entry + "\n")

print("Saved!")