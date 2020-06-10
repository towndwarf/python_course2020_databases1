import sqlite3

conn = sqlite3.connect('stamdb.db')
cur = conn.cursor()
# Prepare a list of records to be inserted
purchases = [{2,'John Paul','john.paul@xyz.com','2020'},
             {3,'Chris Paul','john.paul@xyz.com','2018'},
            ]
# Use executemany() to insert multiple records at a time
cur.executemany('INSERT INTO consumers VALUES (?,?,?,?)', purchases)

for row in cur.execute('SELECT * FROM consumers'):
    print(row)
conn.commit()
conn.close()