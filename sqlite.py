import sqlite3

conn = sqlite3.connect('database.db')

from datetime import datetime

conn.execute("""CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                pages INTEGER,
                published INTEGER                
                )""")

values = ('Deep Learning',
          'Ian Goodfellow et al.',
          775,
          datetime(2016, 11, 18).timestamp())

conn.execute("""INSERT INTO books VALUES (?, ?, ?, ?)""", values)

r = conn.execute("""SELECT * FROM books""")
print(r.fetchall())
