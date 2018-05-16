from User import User
import cgi,cgitb

class SignUp:

    def __init__(self):
        self.user = None
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
        self.username = form.getvalue('username')
        self.firstName=form.getvalue('fname')
        self.lastName=form.getvalue('lname')
        self.password = form.getvalue('password')
        self.address = form.getvalue('address')
        self.question = form.getvalue('ques')
        self.answer = form.getvalue('answer')
        self.email = form.getvalue('email')

    
    def redirectToLogin(self):
        print('<html>')
        print('  <head>')
        print('    <meta http-equiv="refresh" content="0;url=http://127.0.0.1/login.html" />')
        print('  </head>')
        print('</html>')
    

if __name__ == "__main__":
    
    signup = SignUp()

