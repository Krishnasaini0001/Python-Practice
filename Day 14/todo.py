# Day 14: to-do list saved to a file (combines days 8, 9, 13)

import json
import os

FILE = "todo.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

while True:
    action = input("(a)add, (v)view, (q)quit: ").lower()
    if action == "a":
        tasks.append(input("Task: "))
        save_tasks(tasks)
    elif action == "v":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif action == "q":
        break