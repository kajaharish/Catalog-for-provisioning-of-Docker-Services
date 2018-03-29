#!/usr/bin/env python
import cgi, cgitb
import MySQLdb
print "Content-type:text/html\n"
db = MySQLdb.connect("172.17.0.2","root","123456","minor_db")
if db:
	print "Connection established"
	form = cgi.FieldStorage()
	username = form.getvalue('username')
        fname=form.getvalue('fname')
        lname=form.getvalue('lname')
	password = form.getvalue('password')
        address = form.getvalue('address')
	ques = form.getvalue('ques')
        ans = form.getvalue('answer')
        email = form.getvalue('email')
	cursor = db.cursor()
	sql= ('INSERT INTO user VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")' )% (username,fname,lname,password,address,ques,ans,email)
try:
	cursor.execute(sql)
	db.commit()
	print "The data updated"
except:
	db.rollback()
	print " Not updated"
db.close()
