import MySQLdb as my

class Database:

    def __init__(self):

        self.db = my.connect("172.17.0.2","root","123456","minor_db")
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()
