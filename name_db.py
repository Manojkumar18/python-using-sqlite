import sqlite3

conn =sqlite3.connect('name.db')
c=conn.cursor()
    
def table_create():
    c.execute("CREATE TABLE IF NOT EXISTS namedb(rollnumber REAL, name TEXT)")
    print('create table successfully')
def name_entry(): 
    y = int(input('Enter the total number student in your class :'))
    for x in range(y):
        rollnumber=int (x+1)
        name=str(input("Enter ROLLNUMBER  "+str(rollnumber)+" name is :")).upper()
        c.execute("INSERT INTO namedb(rollnumber,name) VALUES(?,?)",(rollnumber,name))
        conn.commit()
        
table_create()
name_entry()
c.close()
conn.close()    