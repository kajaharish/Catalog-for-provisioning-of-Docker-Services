from ConnectDatabase import Database

class User:

    def __init__(self):
        self.username = None
        self.firstName = None
        self.lastName = None
        self.password = None
        self.address = None
        self.question = None
        self.answer = None
        self.email = None
        self.database = Database()
        self.database.connect()

    '''
    def __init__(self,uname,fname,lname,passw,addr,ques,ans,email):
        self.username = uname
        self.firstName = fname
        self.lastName = lname
        self.password = passw
        self.address = addr
        self.question = ques
        self.answer = ans
        self.email = email
        self.database = Database()
        self.database.connect()
    '''

    def addUser(self):
        
        sql = ('INSERT INTO user VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")' )% (self.username,self.firstName,self.lastName,self.password,self.address,self.question,self.answer,self.email)

        return self.database.execute(sql)


    def closeConnection(self):
        self.database.close()


    def createDatabaseUser(self):
        sql = ('create user "%s"@"172.17.0.1" identified by "%s"'%(username,password))
        print sql 
        return self.database.execute(sql)

    def getUsername(self):
        return self.username

    def isUserExisting(self):
        try:
            chk = self.database.cursor.execute('select * from user where username = "%s" or email = "%s"'%(self.username,self.email))
            if chk == 1L:
                return 0
            else:
                return 1
        except Exception as e:
            print e
            return -1

    def verifyUser(self):
        try:
            sql = ('select * from user where username = "%s" and password = "%s"'%(self.username,self.password))
            chk = self.database.cursor.execute(sql)
            if chk == 1L:
                return 0
            else:
                return 1
        except:
            return -1
