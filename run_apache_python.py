#!/usr/bin/python2
import commands as cmd
import json
import MySQLdb
print("Content-Type: text/html\r\n\r\n")
print("")
def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)

def insertdb(cursor,name,uname,cid,cip,stime,etime,web,db,php,py,utime):
	sql=('insert into container values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(name,uname,cid,cip,stime,etime,web,db,php,py,utime))
	chk=cursor.execute(sql)
	if chk==1L:
		return 1
	else:
		return 0

def firstStartApache(name):
	a=cmd.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker run -p 8080:80 -dt --network=mynet0 --name=%s ggandhi27/apache_with_python_cgi"%name)
	print(a)
	return a

def inspect(name):
	tmp=cmd.getstatusoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect %s"%name)
	fp=open("/tmp/tmp1.json","w")
	fp.write(tmp[1])
	fp.close()
	fp=open("/tmp/tmp1.json","r")
	b=json.load(fp)
	fp.close()
	d=dict()
	d["ID"]=b[0]["Id"]
	d["IP"]=b[0]["NetworkSettings"]["Networks"]["mynet0"]["IPAddress"]
	d["Status"]=b[0]["State"]["Status"]
	d["Stime"]=b[0]["State"]["StartedAt"]
	d["Etime"]=b[0]["State"]["FinishedAt"]
	if d["Status"]=="running":
		return d
	else:
		return 0
	
if __name__=="__main__":
	name=raw_input("Enter the anme of container you want to give : ")
	uname=raw_input("Enter the username : ")
	key=firstStartApache(name)
	d1=inspect(key)
	db=None
	cursor=None
	if d1==0:
		print("Container not started!!")
	else:
		print d1
	try:
		db,cursor=connectdb()
		if db:
			chk=insertdb(cursor,name,uname,d1["ID"],d1["IP"],d1["Stime"],d1["Etime"],1,0,0,1,"0")
			if chk==1:
				print("Container created and values updated in table.")
				db.commit()
				db.close()
			else:
				print("Waste of time!!")
		else:
			print("Database not connected!!")
	except:
		db.rollback()
		print("wuhuuuuu!!!")
