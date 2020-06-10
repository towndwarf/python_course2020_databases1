import sqlite3

conn = sqlite3.connect('dbsql.db')
cur = conn.cursor()
# cur.execute('SELECT * from countries')
# print("SINGLE ROW: ", cur.fetchone())
# cur.execute('SELECT `country-code`,`country_name` from countries')
# print("ALL ROWS: ",cur.fetchall())

# for row in cur.execute('SELECT * FROM countries'):
#    print(row)

code = 'ITA'
cur.execute("SELECT * FROM countries WHERE code = '%s'" % code)
print(cur.fetchone())


code = ('ISR',)
cur.execute('SELECT * FROM countries WHERE code = ?', code)
print(cur.fetchone())

cur.close()