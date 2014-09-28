import sqlite3
conn = sqlite3.connect('books.db')

c= conn.cursor()
c.execute("CREATE TABLE book (title, author, pdate)")
conn.commit()
conn.close()