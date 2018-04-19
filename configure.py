import commands as cmd
import json
def insertdbpy(cursor,name,uname,cid,cip,stime,etime,web,db,php,py,utime):
        sql=('insert into container values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(name,uname,cid,cip,stime,etime,web,db,php,py,utime))
        chk=cursor.execute(sql)
        if chk==1L:
                return 1
        else:
                return 0

def runpy(uname,cursor):
	a=cmd.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker run -dt --network=mynet0 ggandhi27/apache_with_python_cgi")
	if a:
		print("<p>Container started.</p><br>")
	d=dict()
	d=inspectpy(a)
	chk=insertdbpy(cursor,d["Name"],uname,d["ID"],d["IP"],d["Stime"],d["Etime"],1,0,0,1,"0")
	if chk==1:
		print("<p>Container started and values updated in table.</p><br>")
		return d
	else:
		print("<p>There is some problem starting the container.</p><br>")
		return 0

def inspectpy(contId):
	print("1")
	tmp=cmd.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect %s"%contId)
	fp=open("/tmp/tmp1.json","w")
	fp.write(tmp)
	print("3")
	fp.close()
	fp=open("/tmp/tmp1.json","r")
	print("1")
	b=json.load(fp)
	print("2")
	fp.close()
	d=dict()
	d["ID"]=b[0]["Id"]
	d["IP"]=b[0]["NetworkSettings"]["Networks"]["mynet0"]["IPAddress"]
	d["Status"]=b[0]["State"]["Status"]
	d["Stime"]=b[0]["State"]["StartedAt"]
	d["Etime"]=b[0]["State"]["FinishedAt"]
	d["Name"]=b[0]["Name"]
	if d["Status"]=="running":
		return d
	else:
		return 0

def insertdbphp(cursor,name,uname,cid,cip,stime,etime,web,db,php,py,utime):
        sql=('insert into container values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(name,uname,cid,cip,stime,etime,web,db,php,py,utime))
        chk=cursor.execute(sql)
        if chk==1L:
                return 1
        else:
                return 0

def runphp(uname,cursor):
	a=cmd.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker run -dt --network=mynet0 ggandhi27/apache_with_php")
	d=inspectphp(a)
	chk=insertdbphp(cursor,d["Name"],uname,d["ID"],d["IP"],d["Stime"],d["Etime"],1,0,1,0,"0")
	if chk==1:
		print("<p>Container started and values updated in table.</p><br>")
		return d
	else:
		print("<p>There is some problem starting the container.</p><br>")
		return 0

def inspectphp(name):
	tmp=cmd.getstatusoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect %s"%name)
	fp=open("/tmp/tmp1.json","w")
	fp.write(tmp[1])
	fp.close()
	fp=open("/tmp/tmp1.json","r")
	b=json.load(fp)
	fp.close()
	d=dict()
	d["ID"]=b[0]["Id"]
	d["Name"]=b[0]["Name"]
	d["IP"]=b[0]["NetworkSettings"]["Networks"]["mynet0"]["IPAddress"]
	d["Status"]=b[0]["State"]["Status"]
	d["Stime"]=b[0]["State"]["StartedAt"]
	d["Etime"]=b[0]["State"]["FinishedAt"]
	if d["Status"]=="running":
		return d
	else:
		return 0

def start_cont(name):
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
def startdb(cursor,name,stime,etime):
        sql=('update container set start_time="%s",end_time="%s" where container_name="%s"'%(stime,etime,name))
        chk=cursor.execute(sql)
        if chk==1L:
                return 1
        else:
                return 0

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
def stopdb(cursor,name,etime,utime):
        sql=('update container set end_time="%s", total_uptime="%s" where container_name="%s"'%(etime,utime,name))
        chk=cursor.execute(sql)
        if chk==1L:
                return 1
        else:
                return 0

def remove_cont(name):
        chk=cmd.getoutput('sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker rm %s'%name)
        if chk==name:
                return 1
        else:
                return 0
def deletedb(cursor,name):
        sql=('delete from container where container_name="%s"'%name)
        chk=cursor.execute(sql)
        if chk==1L:
                return 1
        else:
                return 0

