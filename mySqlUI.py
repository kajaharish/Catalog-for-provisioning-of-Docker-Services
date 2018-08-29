#!/usr/bin/python2

print ("Content-Type: text/html\n\n")

import cgi,cgitb
import os
import MySQLdb

def connectDB():
    db = MySQLdb.connect("172.17.0.3","root","123456","minor_db")
    cursor = db.cursor()
    return (db,cursor)

def getUserName(cursor,sessionId):
    check = cursor.execute('select username from session where session_id = "%s"'%(sessionId))
    username = cursor.fetchone()
    return username;

def getPassword(cursor,username):
    check = cursor.execute('select password from user where username = "%s"'%(username))
    password = cursor.fetchone()
    return password


def getCookieValue():
    handler = {}
    if 'HTTP_COOKIE' in os.environ:
        cookies = os.environ['HTTP_COOKIE']
        cookies = cookies.split('; ')
        for cookie in cookies:
            cookie = cookie.split('=')
            handler[cookie[0]] = cookie[1]
    try :
        return handler["docker_session"]
    except KeyError:
        return ""


def callLoginPage():
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url=http://127.0.0.1/login.html" />')
    print('  </head>')
    print('</html>')

def connectUserDB(username,password,database):
    userDB = MySQLdb.connect("172.17.0.3",username,password,database)
    userCursor = userDB.cursor()
    return (userDB,userCursor)

def userDatabaseOperations(username,password,database,query):

    userDB,userCursor = connectUserDB(username,password,database)
    result = None
    if userDB :
        #print  "User database connected successfully."
        result = executeUserQuery(userCursor,userDB,query)
        return result
    else:
        return "Problem connecting the user database."


def executeUserQuery(userCursor,userDB,query):
    try:
        check = userCursor.execute(query)
        result = ""
        if check == 0L:
            userDB.commit()
            return "Query is executed successfully."
        else:
            userDB.commit()
            result = userCursor.fetchall()
            string = "<br/><br/>Query executed successfully.<br/>"
            for row in result:
                for x in row:
                    string = string + str(x) + "&nbsp;&nbsp;&nbsp;&nbsp;"
                string = string + "<br/>"
            return string
    except MySQLdb.Error,e:
        return e


if __name__  == "__main__":
    
    cgitb.enable()
    query = cgi.FormContent()["query"][0]
    
    #get the session id
    sessionId = getCookieValue()

    #get the username from the session id
    #
    #To get the username
    #
    #1 - Connect to the database.
    #2 - prepare query to get the username.
    #3 - fetch the password from the users table.
    

    if sessionId == "":
        callLoginPage()

    else:
        db = None
        cursor = None
        username = None
        password = None
        database = None
        result = None

        db,cursor = connectDB()
        
        if db:        
            username = getUserName(cursor,sessionId)[0]
        
            password = getPassword(cursor,username)[0]
            
            #This function is needed to be defined.
            #database = getDatabase(username)
            database = "test_db"

            result = userDatabaseOperations(username,password,database,query)
            

            print ('''
<!DOCTYPE html>

<html>
        <head>
            <title>
            Database Access Terminal
            </title>
            <style type="text/css">
            textarea
            {
                    width: 100%;
                    margin: 0;
                    padding: 0;
                    border-width: 10;
                    resize: none;
             }
            </style>
        </head>
        <body>
            <h1>Database Access Terminal</h1>
            <form action="/scripts/mySqlUI.py" method="POST">
            <textarea rows="10" cols="20" wrap="hard" name="query"required autofocus>Erase me to type in your queries.</textarea>
            </br>
            <input type="submit" placeholder="Execute" name="execute">
            </form>

            <h3>Output : </h3>
            </hr>
''')
            print("<h4>Result : %s</h4></br>"%result)
            print ("""
</body>
</html>
""")
        else:
            print "No database connectivity at the server level."
