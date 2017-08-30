import sqlite3 as sql

con=sql.connect("name.db")
c = con.cursor()

# con.row_factory = sql. Row

def read_date_db():
    c.execute('SELECT * FROM namedb ')# WHERE  name="manojkumar"')
    data =c.fetchall()
    for x in data:
    	print(x[1])
    

read_date_db()
c.close()
con.close()