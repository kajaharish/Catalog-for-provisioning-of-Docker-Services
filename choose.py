#!/usr/bin/python2
import cgi,cgitb
import configure as cf
import MySQLdb
import FetchCookie as fc
cgitb.enable()
print("Content-Type: text/html\r\n\r\n")
print("")

def getUserName(cursor):
	cookie = fc.getCookieValue()
	check = cursor.execute('select username from session where session_id = "%s"'%cookie)
	username = cursor.fetchone()[0]
	return username

def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)

def fetchValue():
	form=cgi.FieldStorage()
	ch=form.getvalue("choose")
	name=form.getvalue("name")
	return ch,name

if __name__=="__main__":
	db,cursor=connectdb()
	print("""<html>
                <head>
                        <title>Container status</title>
                </head>
                <body>""")
	try:
		if db:
			uname=getUserName(cursor)
			ch,name=fetchValue()
			if ch=="addpy":
				d=cf.runpy(uname,name,cursor)
				if d!=0:
					print("""<p>Name: %s
						    Id: %s
						    Status: %s	
						    IP: %s  </p>"""%(d["Name"],d["ID"],d["Status"],d["IP"]))
					db.commit()
					db.close()
			elif ch=="addphp":
				d=cf.runphp(uname,name,cursor)
				if d!=0:
					print("""<p>Name: %s
                                	            Id: %s
                                	            Status: %s  
                                	            IP: %s  </p>"""%(d["Name"],d["ID"],d["Status"],d["IP"]))
					db.commit()
					db.close()
		else:
			print("<p>There is some problem in database connectivity.</p>")
		print("""</body>
			</html>""")
	except Exception as e:
		print(e)
		db.rollback()
		db.close()
		print("Wuhuuu!!")
		
		
