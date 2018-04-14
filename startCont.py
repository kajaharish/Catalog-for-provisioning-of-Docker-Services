#!/usr/bin/python2
import json
import MySQLdb
import commands as cmd
print("Content-Type: text/html\n\r\n\r")
print("")
def startCont(name):
	chk=cmd.getoutput('sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker start %s'%name)
	if chk==name:
		tmp=cmd.getstatusoutput('sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect %s'%name)
		fp=open("/tmp/tmp3.json","w")
		fp.write(tmp[1])
		fp.close()
		fp=open("/tmp/tmp3.json","r")
		b=json.load(fp)
		fp.close()
		d=dict()
		d["Stime"]=b[0]["State"]["StartedAt"]
		d["Etime"]=b[0]["State"]["FinishedAt"]
		d["Status"]=b[0]["State"]["Status"]
		if d["Status"]=="running":
			return d
		else:
			print("Container not running!!")
	else:
		return 0
def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)
def updatedb(cursor,name,stime,etime):
	sql=('update container set start_time="%s",end_time="%s" where container_name="%s"'%(stime,etime,name))
	chk=cursor.execute(sql)
	if chk==1L:
		return 1
	else:
		return 0
if __name__=="__main__":
	name=raw_input("Enter the name of the container you want to start: ")
	d=startCont(name)
	db,cursor=connectdb()
	try:
		if db:
			chk=updatedb(cursor,name,d["Stime"],d["Etime"])
			if chk==1:
				print("Container started and values updated in table.")
				db.commit()
				db.close()
			else:
				print("Cannot Update table.")
		else:
			print("Database not connected.")
	except:
		print("Wuhuuuu!!!")
		db.rollback()
