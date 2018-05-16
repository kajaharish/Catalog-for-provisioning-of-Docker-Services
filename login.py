#!/usr/bin/python2

from ConnectDatabase import Database as DB
import cgi, cgitb
import MySQLdb
import RandomKeyGenerator as rkg
import CookieGenerator as cookie

class Login:
    
    def __init__(self):
        self.db = DB()


    def fetchDetails():
        form = cgi.FieldStorage()
        username = form.getvalue('username')
        password = form.getvalue('password')
        return (username,password)


    def login(username,password):
        try:
            #Execute the SQL command
            sql = ('select * from user where username = "%s" and password = "%s"'%(username,password))
            chk = self.db.cursor.execute(sql)
            if chk == 1L:
                #Generate Session id.
                user_check = checkUser(self.db.cursor,username)
                if user_check == 1:
                    ssn = 0
                    while ssn == 0:
                        session_id = rkg.randomKey()
                        ssn_chk = checkSessionId(session_id)
                        if ssn_chk == 1:
                            ssn = 1
                            break
                    #Create Cookie.
                    cookie.genCookie(session_id)
                    print "Content-type:text/html\r\n\r\n"
                    #Update the cookie in the sessions table.
                    createSession(session_id,username)
                    print ("Login Successfull")
                else:
                    print "Content-type:text/html\r\n\r\n"
                    print "Already a session is created for the user."
            else:
                print ("Please check the username or password")
        except Exception as e:
            db.db.rollback()
            print "Not updated"

    def checkSessionId(session_id):
        sql = "select * from session where session_id = '%s'"%session_id
        check = self.db.cursor.execute(sql)
        if check == 1L:
            return 0
        else:
            return 1


    def checkUser(username):
        sql = "select * from session where username = '%s'"%username
        check = self.db.cursor.execute(sql)
        if check == 1L:
            return 0
        else:
            return 1

    def createSession(session_id,username):
        sql = ("insert into session values ('%s','%s')")%(session_id,username)
        try:
            self.db.cursor.execute(sql)
            self.db.db.commit()
            return 1
        except:
            self.db.db.rollback()
            print ("Not able to start the session.")
            return 0



if __name__=="__main__":

    login = Login()
    cgitb.enable()
    username = None
    password = None

    if db:
        username,password = fetchDetails()
        login(username,password)
        db.close()
    else:
        print ("Not able to connect to the database")
