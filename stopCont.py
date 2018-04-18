#!/usr/bin/python2
import commands as cmd
import json
import MySQLdb
print("Content-Type: text/html\n\r\n\r")
print("")
def stop_cont(name):
	chk=cmd.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker stop %s"%name)
	if chk==name:
		tmp=cmd.getstatusoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect %s"%name)
		fp=open("/tmp/tmp2.json","w")
        	fp.write(tmp[1])
        	fp.close()
        	fp=open("/tmp/tmp2.json","r")
        	b=json.load(fp)
        	fp.close()
        	d=dict()
        	d["Stime"]=b[0]["State"]["StartedAt"]
		d["Etime"]=b[0]["State"]["FinishedAt"]
		d["Status"]=b[0]["State"]["Status"]
		if d["Status"]=="exited":
			return d
		else:
			return 0
	else:
		print("Could not stop container.")
def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)
def updatedb(cursor,name,etime,utime):
	sql=('update container set end_time="%s", total_uptime="%s" where container_name="%s"'%(etime,utime,name))
	chk=cursor.execute(sql)
	if chk==1L:
		return 1
	else:
		return 0
if __name__=="__main__":
	name=raw_input("Enter the name of Container You want to stop : ")
	d=stop_cont(name)
	db,cursor=connectdb()
	try:
		if db:
			#tmp=d["Etime"]-d["Stime"]
			#print(tmp)
			chk=updatedb(cursor,name,d["Etime"],"0")
			if chk==1:
				print("Container Stopped and Values Updated in Table.")
				db.commit()
				db.close()
			else:
				print("Can't Update.")
		else:
			print("Can't connect to database.")
	except:
		print("Wuhuuuuu!!!")
		db.rollback()
