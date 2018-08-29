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
    
    def addUser(self):
        sql = ('INSERT INTO user VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")' )%(self.username,self.firstName,self.lastName,self.password,self.address,self.question,self.answer,self.email)
        return self.database.execute(sql)
    
    def closeConnection(self):
        self.database.close()


    def createDatabaseUser(self):
        sql = ('create user "%s"@"172.17.0.1" identified by "%s"'%(self.username,self.password))
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

    def deleteUser(self):
        try:
            sql = 'delete from user where username="%s"'%(self.username)
            return self.database.execute()
        except:
            return -1
