import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        original_url TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")