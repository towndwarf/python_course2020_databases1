import sqlite3

conn = sqlite3.connect('stamdb.db')
cur = conn.cursor()
# One by one
cur.execute("INSERT INTO consumers VALUES (1,'Ishay Barr','i.barr@xyz.com','2020')")
conn.commit()
#conn = sqlite3.connect('db.db')
#cur.execute("DELETE FROM customers WHERE email='alexey.abraham@gmail.com'")
#conn.commit()

for row in cur.execute('SELECT * FROM consumers'):
    print(row)
cur.close()
conn.close()
