import sqlite3

conn = sqlite3.connect('dbsql.db')
cur = conn.cursor()
# Prepare a list of records to be inserted
purchases = [('John Paul','john.paul@xyz.com','2020'),
             ('Chris Paul','john.paul@xyz.com','2018'),
            ]
# Use executemany() to insert multiple records at a time
cur.executemany('INSERT INTO consumers(`name`,`email`,`year`) VALUES (?,?,?)', purchases)

for row in cur.execute('SELECT * FROM consumers'):
    print(row)
conn.commit()
conn.close()