from ConnectDatabase import Database
from RandomKeyGenerator import RandomKeyGenerator

class Session:

    def __init__(self):

        self.username = None
        self.sessionId = None
        self.database = Database()
        self.randomKey = RandomKeyGenerator()

    def createSession(self):
        self.randomKey.getRandomKey()
        chk = self.checkSessionId()
        while chk == 0 or chk == -1:
            if chk == -1:
                print "Sorry we cannot create a a session for you."
                break
            self.randomKey.getRandomKey()
            chk == self.checkSessionId()
        
    def checkSessionId(self):
        try:
            sql = "select * from session where session_id = '%s'"%self.randomKey.randomKey
            check = self.database.cursor.execute(sql)
            if check == 1L:
                return 0
            else:
                return 1
        except:
            return -1

    def deleteSession(self):
        sql = 'delete from session where username = "%s"'%username
        a = self.database.execute(sql)

    def checkUserSession(self):
        try:
            sql = 'select * from session where username = "%s"'%(username)
            check = self.database.cursor.execute(sql)

            if check == 1L:
                return 0
            else:
                return 1
        except:
            return -1
