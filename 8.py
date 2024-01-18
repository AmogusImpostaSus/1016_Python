import sqlite3

connection = sqlite3.connect(database="db.sl3", timeout=5)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")

names = ['Имя1', 'Имя2', 'Имя3', 'Имя4', 'Имя5', 'Имя6', 'Имя7', 'Имя8', 'Имя9', 'Имя10']

for name in names:
    cursor.execute('INSERT INTO Users (name) VALUES (?)', (name,))

connection.commit()
connection.close()
