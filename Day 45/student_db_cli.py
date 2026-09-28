# Day 45: CLI app backed by SQLite

import sqlite3

def setup():
    conn = sqlite3.connect("students.db")
    conn.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, score INTEGER)")
    return conn

def add_student(conn, name, score):
    conn.execute("INSERT INTO students VALUES (?, ?)", (name, score))
    conn.commit()

def list_students(conn):
    for row in conn.execute("SELECT * FROM students"):
        print(row)

conn = setup()
while True:
    action = input("(a)dd, (v)iew, (q)uit: ").lower()
    if action == "a":
        add_student(conn, input("Name: "), int(input("Score: ")))
    elif action == "v":
        list_students(conn)
    elif action == "q":
        break
conn.close()