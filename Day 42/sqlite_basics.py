# Day 44: basic database with sqlite3 (built into Python)

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        score INTEGER
    )
""")

cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Alex", 88))
conn.commit()

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.close()