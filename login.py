#!/usr/bin/python2
import cgi, cgitb
import MySQLdb
import RandomKeyGenerator as rkg
import CookieGenerator as cookie

def connectDB():
    db = MySQLdb.connect("172.10.20.1","root","123456","minor_db")
    cursor = db.cursor()
    return (db,cursor)


def fetchDetails():
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    return (username,password)


def login(db,cursor,username,password):
    try:
        #Execute the SQL command
        sql = ('select * from user where username = "%s" and password = "%s"'%(username,password))
        chk = cursor.execute(sql)
        if chk == 1L:
            #Generate Session id.
            user_check = checkUser(cursor,username)
            if user_check == 1:
                ssn = 0
                while ssn == 0:
                    session_id = rkg.randomKey()
                    ssn_chk = checkSessionId(cursor,session_id)
                    if ssn_chk == 1:
                        ssn = 1
                        break
                #Create Cookie.
                cookie.genCookie(session_id)
                print "Content-type:text/html\r\n\r\n"
                #Update the cookie in the sessions table.
                createSession(db,cursor,session_id,username)
                print ("Login Successfull")
            else:
                print "Content-type:text/html\r\n\r\n"
                print "Already a session is created for the user."
        else:
            print ("Please check the username or password")
    except Exception as e:
        db.rollback()
        print "Not updated"


def checkSessionId(cursor,session_id):
    sql = "select * from session where session_id = '%s'"%session_id
    check = cursor.execute(sql)
    if check == 1L:
        return 0
    else:
        return 1


def checkUser(cursor,username):
    sql = "select * from session where username = '%s'"%username
    check = cursor.execute(sql)
    if check == 1L:
        return 0
    else:
        return 1


def createSession(db,cursor,session_id,username):
    sql = ("insert into session values ('%s','%s')")%(session_id,username)
    try:
        cursor.execute(sql)
        db.commit()
        return 1
    except:
        db.rollback()
        print ("Not able to start the session.")
        return 0


def closeDB(db):
    db.close()


if __name__=="__main__":
    cgitb.enable()
    db = None
    cursor = None
    username = None
    password = None
    db,cursor = connectDB()
    if db:
        username,password = fetchDetails()
        login(db,cursor,username,password)
        closeDB(db)
    else:
        print ("Not able to connect to the database")
