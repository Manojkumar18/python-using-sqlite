import sqlite3


conn =sqlite3.connect('name.db')
conn1 = sqlite3.connect('mark.db')
c=conn.cursor()
c1=conn1.cursor()

nameofexam = str(input("Enter the Exam name :")).upper()
namesub1 =str(input("Enter subject 1 name : ")).upper()
namesub2 =str(input("Enter subject 2 name : ")).upper()
namesub3 =str(input("Enter subject 3 name : ")).upper()
namesub4 =str(input("Enter subject 4 name : ")).upper()
namesub5 =str(input("Enter subject 5 name : ")).upper()
namesub6 =str(input("Enter subject 6 name : ")).upper()


def create_table():
	c1.execute("CREATE TABLE IF NOT EXISTS markdb( examname TEXT, name TEXT,sub1name TEXT, sub2name TEXT, sub3name TEXT, sub4name TEXT, sub5name TEXT, sub6name TEXT)")
	print("data base create")
def subject_name():
	examname = nameofexam 
	sub1name = namesub1
	sub2name = namesub2
	sub3name = namesub3
	sub4name = namesub4
	sub5name = namesub5
	sub6name = namesub6
	c1.execute("INSERT INTO markdb( examname, sub1name, sub2name, sub3name, sub4name, sub5name, sub6name) VALUES ( ?, ?, ?, ?, ?, ?, ?)",( examname, sub1name, sub2name, sub3name, sub4name, sub5name, sub6name))
	conn1.commit()	



def mark_entry():
    c.execute('SELECT name FROM namedb ')
    data =c.fetchall()
    for x in data:
    	print(x[0]+" "+nameofexam+" MARKS")
    	examname = nameofexam
    	name=str(x[0])
    	sub1name =str(input("Enter "+ namesub1+" subject mark : "))
    	sub2name =str(input("Enter "+ namesub2+" subject mark : "))
    	sub3name =str(input("Enter "+ namesub3+" subject mark : "))
    	sub4name =str(input("Enter "+ namesub4+" subject mark : "))
    	sub5name =str(input("Enter "+ namesub5+" subject mark : "))
    	sub6name =str(input("Enter "+ namesub6+" subject mark : "))
    	c1.execute("INSERT INTO markdb( examname, name,sub1name, sub2name, sub3name, sub4name, sub5name, sub6name) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)",(  examname, name, sub1name, sub2name, sub3name, sub4name, sub5name, sub6name))
    	conn1.commit()
	 	
		
	 		 
create_table()
subject_name()
mark_entry()


c.close()
conn.close()
c1.close()
conn1.close()

  