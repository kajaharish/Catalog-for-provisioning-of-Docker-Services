#!/usr/bin/python2

from Session import Session
from CookieGenerator import CookieGenerator
import cgi,cgitb

class Login:

    def __init__(self):

        self.username = None
        self.password = None
        self.session = Session()

    def fetchLoginValues(self):
        form = cgi.FieldStorage()
        self.username = form.getvalue('username')
        self.password = form.getvalue('password')
        self.session.username = self.username

    def login(self):
        try:
            self.session.database.connect()
            sql = ('select * from user where username = "%s" and password = "%s"'%(self.username,self.password))
            chk = self.session.database.cursor.execute(sql)
            if chk == 1L:
                checkUser = self.session.checkUserSession()
                if checkUser == 1:
                    self.session.createSession()
                    cookie = CookieGenerator()
                    cookie.genCookie(self.session.sessionId)
                    print "Content-type:text/html\r\n\r\n"
                    print ("Login Successfull")
                else:
                    print "User  is already logged in."
            else:
                print "Check username or password."
        except Exception as e:
            print ("Login Failed")
            print e
    
    def redirectToDashboard(self):
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content="0;url=http://127.0.0.1/scripts/Dashboard.py" />')
        print('  </head>')
        print('</html>')


if __name__ == "__main__":
    cgitb.enable()

    login = Login()
    login.fetchLoginValues()
    login.login()
    login.redirectToDashboard()
