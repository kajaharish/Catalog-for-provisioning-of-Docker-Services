#!/usr/bin/python2

from User import User

import cgi,cgitb

class SignUp:

    def __init__(self):
        self.user= User()
        self.username = None
        self.firstName = None
        self.lastName = None
        self.password = None
        self.address = None
        self.question = None
        self.answer = None
        self.email = None

    def fetchSignupDetails(self):
        form = cgi.FieldStorage()
        self.user.username = form.getvalue('username')
        self.user.firstName=form.getvalue('fname')
        self.user.lastName=form.getvalue('lname')
        self.user.password = form.getvalue('password')
        self.user.address = form.getvalue('address')
        self.user.question = form.getvalue('ques')
        self.user.answer = form.getvalue('answer')
        self.user.email = form.getvalue('email')

    
    def redirectToLogin(self):
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content="0;url=http://127.0.0.1/login.html" />')
        print('  </head>')
        print('</html>')
    

if __name__ == "__main__":


    print "Content-type:text/html\r\n\r\n"
    signup = SignUp()
    
    signup.fetchSignupDetails()
    
    check = signup.user.isUserExisting()

    if check == 1:
        checkAddUser = signup.user.addUser()
        if checkAddUser == 1:
            checkDatabaseUser = signup.user.createDatabaseUser()
            if checkDatabaseUser == 0:
                a = signup.user.deleteUser()
            else:
                signup.redirectToLogin()
    else:
        print ("Username or email already exists")
