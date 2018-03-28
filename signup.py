#!/usr/bin/env python
import cgi, cgitb
import MySQLdb
print "Content-type:text/html\n"
db = MySQLdb.connect("localhost","root","Cascaders1@3","Minor")
if db:
	print "Connection established"
	form = cgi.FieldStorage()
	username = form.getvalue('username')
	password = form.getvalue('password')
	security_ques = form.getvalue('security_ques')
	cursor = db.cursor()
	sql= 'INSERT INTO LOGIN	VALUES ("%s","%s","%s")' % \
	(username,password,security_ques)
try:
	cursor.execute(sql)
	db.commit()
	print "The data updated"
except:
	db.rollback()
	print " Not updated"
db.close()
