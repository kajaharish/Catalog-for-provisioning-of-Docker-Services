#!/usr/bin/python

from os import environ
import cgi, cgitb
import MySQLdb
from random import choice
from string import ascii_uppercase
cgitb.enable()

cookie_id=''.join(choice(ascii_uppercase) for i in range(6))
cookie = Cookie.SimpleCookie()
cookie["session"] = cookie_id
cookie["session"]["expires"] = "Wed, 27-Mar-2019 00:00:00"

form = cgi.FieldStorage()
username = form["username"].value

db = MySQLdb.connect("localhost","root","Cascaders1@3","Minor")
cursor = db.cursor()
sql= 'INSERT INTO SESSION VALUES ("%s","%s")' % \
        (username,cookie["session"])
try:
        cursor.execute(sql)
        db.commit()
	print "data updated"
except:
	db.rollback()
