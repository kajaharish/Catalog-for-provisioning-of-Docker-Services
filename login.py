#!/usr/bin/python
import cgi, cgitb
import MySQLdb
cgitb.enable()
print "Content-type:text/html\r\n\r\n"

def connectDB():
    db = MySQLdb.connect("172.17.0.2","root","123456","minor_db")
    cursor = db.cursor()
    return (db,cursor)

def fetchDetails():
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    return (username,password)

def login(cursor,username,password):
    try:
        #Execute the SQL command
        sql = ('select * from user where username = "%s" and password = "%s"'%(username,password))
        chk = cursor.execute(sql)
        if chk == 1L:
            print ("Login Successfull")
        else:
            print ("Please check the username or password")
    except:
        db.rollback()
        print " Not updated"

def closeDB(db):
    db.close()


if __name__=="__main__":
    db = None
    cursor = None
    username = None
    password = None
    db,cursor = connectDB()
    if db:
        username,password = fetchDetails()
        login(cursor,username,password)
        closeDB(db)
    else:
        print ("Not able to connect to the database")

