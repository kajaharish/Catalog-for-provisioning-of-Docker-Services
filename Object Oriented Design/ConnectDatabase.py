import MySQLdb as my

class Database:

    #This is contructor.
    #This is used for instantiating the class variables.
    def __init__(self):

        self.dbPointer = None
        self.cursor = None
        self.ipAddress = "172.17.0.2"
        self.dbUsername = "root"
        self.dbPassword = "123456"
        self.dbName = "minor_db"
    
    #This function is used to create a connection with the databse.
    def connect(self):
        self.dbPointer = my.connect(self.ipAddress,self.dbUsername,self.dbPassword,self.dbName)

        self.cursor = self.dbPointer.cursor()

    #This function is used to roll back all the changes which have been done to the database.
    def rollback(self):
        self.dbPointer.rollback()

    #This function closes the connection established with the database.
    def close(self):
        self.dbPointer.close()

    #This is an abstract function.
    #This is used to execute a query.
    def execute(self,query):
        try:
            self.cursor.execute(query)
            self.dbPointer.commit()
            return 1
        except MySQLdb.Error,e:
            print e
            self.dbPointer.rollback()
            return 0

    #This function commits the changes done in the database.
    def commit(self):
        self.dbPointer.commit()
