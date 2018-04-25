#!/usr/bin/python2
import cgi,cgitb
import configure as cf
import MySQLdb
cgitb.enable()
print("Content-Type: text/html\r\n\r\n")
print("")

def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)

def fetchValue():
	form=cgi.FieldStorage()
	name=form.getvalue("name")
	return name

if __name__=="__main__":
	db,cursor=connectdb()
	print("""<html>
                <head>
                        <title>Container status</title>
                </head>
                <body>""")
	try:
		if db:
			name=fetchValue()
			if name:
				d=cf.start_cont(name)
				if d:
					print("Container Started.<br><br>")
					print("""<p>Name: %s
						    Id: %s
						    Status: %s	
						    IP: %s  </p>"""%(name,d["ID"],d["Status"],d["IP"]))
					c=cf.startdb(cursor,name,d["Stime"],d["Etime"])
					if c==1:
						print("Values updated in table.")
					else:
						print("There is some error in sql.")
					db.commit()
					db.close()
				else:
					print("Cannot start Container!!")
		else:
			print("<p>There is some problem in database connectivity.</p>")
		print("""</body>
			</html>""")
	except Exception as e:
		print(e)
		db.rollback()
		db.close()
		print("Wuhuuu!!")
		
		
