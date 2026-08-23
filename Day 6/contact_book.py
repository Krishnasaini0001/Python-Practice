# Day 6: dictionaries

contacts = {}

while True:
    action = input("\n(a)dd contact, (v)iew all, (q)uit: ").lower()

    if action == "a":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif action == "v":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif action == "q":
        break