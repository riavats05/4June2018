#!/usr/bin/python2
import mysql.connector as mysql
connection=mysql.connect(user='root',password='riavats',host='localhost',database='adhoc1')
cur=connection.cursor()
cur.execute("select name,email from student")
output=cur.fetchall()
print output
print "1. Insert"
print "2. Update"
print "3. Exit"
value=raw_input("Enter choice")
if value=='1':
	cur.execute("Insert into student (name,email) values ('N2','n2@gmail.com')")
	print("One row inserted")
	connection.commit()
elif value=='2':
	cur.execute("Update student set name='Ria' where sr=1")
	print("Row Updated")
	connection.commit()
else:
	exit()

