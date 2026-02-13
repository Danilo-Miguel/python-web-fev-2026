import sqlite3

conn = sqlite3.connect("banco.db")

with open("esquema.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("Banco de dados criado com sucesso")

