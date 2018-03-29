#!/usr/bin/python
import cgi, cgitb
import MySQLdb
print ("Content-type:text/html\n\n")

def connectDB():
    db = MySQLdb.connect("172.17.0.2","root","123456","minor_db")
    cursor = db.cursor()
    return (db,cursor)


def checkUsername(cursor,username,email):
    chk = cursor.execute('select * from user where username = "%s" or email = "%s"'%(username,email))
    if chk == 1L :
        return 0
    else:
        return 1

def fetchDetails():
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    fname=form.getvalue('fname')
    lname=form.getvalue('lname')
    password = form.getvalue('password')
    address = form.getvalue('address')
    ques = form.getvalue('ques')
    ans = form.getvalue('answer')
    email = form.getvalue('email')
    return (username,fname,lname,password,address,ques,ans,email)

def prepareQuery(username,fname,lname,password,address,ques,ans,email):
	return ('INSERT INTO user VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")' )% (username,fname,lname,password,address,ques,ans,email)

def executeQuery(db,sql):
    try:
    	cursor.execute(sql)
    	db.commit()
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content="0;url=http://127.0.0.1/login.html" />') 
        print('  </head>')
        print('</html>')
    except:
        db.rollback()
        print " Not updated"

def closeDB():
    db.close()

if __name__=="__main__":
    
    db = None
    cursor = None
    username = None
    fname = None
    lname = None
    password = None
    address = None
    email = None
    ques = None
    ans = None
    db,cursor = connectDB()
    if db:
        username,fname,lname,password,address,ques,ans,email=fetchDetails()
        chk = checkUsername(cursor,username,email)
        if chk == 1:
            sql = prepareQuery(username,fname,lname,password,address,ques,ans,email)
            executeQuery(db,sql)
        else:
            print ("Username or Email already exists")
        closeDB()
    else:
        print "DB not connected."
