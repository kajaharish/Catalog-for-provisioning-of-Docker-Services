#!/usr/bin/python2
import cgi,cgitb
import configure as cf
import MySQLdb
cgitb.enable()
print("Content-Type: text/html\n\r\n\r")
print("")

def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)

def fetchValue():
	form=cgi.FieldStorage()
	ch=form.getvalue("choose")
	return ch

if __name__=="__main__":
	db,cursor=connectdb()
	print("""<html>
                <head>
                        <title>Container status</title>
                </head>
                <body>""")
	try:
		if db:
			ch=fetchValue()
			if ch=="addpy":
				d=cf.runpy("ankpathak",cursor)
				if d!=0:
					print("""<p>Name: %s
						    Id: %s
						    Status: %s	
						    IP: %s  </p>"""%(d["Name"],d["ID"],d["Status"],d["IP"]))
					db.commit()
					db.close()
			elif ch=="addphp":
				d=cf.runphp("ankpathak",cursor)
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
		
		
