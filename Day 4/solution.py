# Day 4: lists - add, remove, loop through

shopping_list = []

while True:
    item = input("Add an item (or type 'done' to finish): ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("\nYour shopping list:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")