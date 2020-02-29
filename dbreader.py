import sqlite3

con = sqlite3.connect('blogs.db')
cur = con.cursor()
cur.execute('select distinct url, title, content from blogs where content not like "None"')
rows = cur.fetchall()
con.close()
