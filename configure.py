import commands
import json
class Container:
	def __init__(self):
		container_name=None
		ipaddress=None
		container_id=None
		start_time=None
		end_time=None
		uptime=None
		web_server=1
		db_server=1
		php=0
		python=0
		status=None
		passw="Cascaders1@3"
		ipw="root@127.0.0.1"
		
'''	def insertdbpy(cursor,name,uname,cid,cip,stime,etime,web,db,php,py,utime):
        	sql=('insert into container values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(name,uname,cid,cip,stime,etime,web,db,php,py,utime))
        	chk=cursor.execute(sql)
        	if chk==1L:
        	        return 1
        	else:
        	        return 0

	def runpy(uname,name,cursor):
		a=commands.getoutput("sshpass -p 123456 ssh -o StrictHostKeyChecking=no root@10.42.0.1 docker run -dt --name=%s ggandhi27/apache_with_python_cgi"%name)
		a=a[78:]
		if a:
			print("<p>Container started.</p><br>")
		d=dict()
		d=inspectpy(name)
		chk=insertdbpy(cursor,name,uname,d["ID"],d["IP"],d["Stime"],d["Etime"],1,0,0,1,"0")
		if chk==1:
			print("<p>Container started and values updated in table.</p><br>")
			return d
		else:
			print("<p>There is some problem starting the container.</p><br>")
			return 0

	def inspectpy(contId):
		cmd = "sshpass -p 123456 ssh -o StrictHostKeyChecking=no root@10.42.0.1 docker container inspect"
		cmd1=cmd+" "+contId
		tmp = commands.getoutput(cmd1)
		tmp1=tmp[78:]
		print(tmp1)
		print("<br><br>")
		fp=open("/tmp/runpy.json","w")
		fp.write(tmp1)
		fp.close()
		fp=open("/tmp/runpy.json","r")
		b=json.load(fp)
		fp.close()
		d=dict()
		d["ID"]=b[0]["Id"]
		d["IP"]=b[0]["NetworkSettings"]["Networks"]["bridge"]["IPAddress"]
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

	def runphp(uname,name,cursor):
		a=commands.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker run -dt --name=%s ggandhi27/apache_with_php"%name)
		a=a[78:]
		if a:
			print("Container running.")
		d=inspectphp(name)
		chk=insertdbphp(cursor,name,uname,d["ID"],d["IP"],d["Stime"],d["Etime"],1,0,1,0,"0")
		if chk==1:
			print("<p>Container started and values updated in table.</p><br>")
			return d
		else:
			print("<p>There is some problem starting the container.</p><br>")
			return 0
	
	def inspectphp(name):
		print "<br><br>"
		cmd = "sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker container inspect"
		cmd1=cmd+" "+name
		print("<br><br>")
		tmp = commands.getoutput(cmd1)
		print("<br><br>")
		tmp1=tmp[78:]
		fp=open("/tmp/runpy.json","w")
		fp.write(tmp1)
		fp.close()
		fp=open("/tmp/runpy.json","r")
		b=json.load(fp)
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
'''
#fetching data from form
	def fetchValue():
		form=cgi.FieldStorage()
		ch=form.getvalue("choose")
		return ch
	def fetchname(self):
		form=cgi.FieldStorage()
		self.container_name=form.getvalue("name")

	def getUserName(cursor):
		cookie = fc.getCookieValue()
		check = cursor.execute('select username from session where session_id = "%s"'%cookie)
		username = cursor.fetchone()[0]
		return username

	def start_cont(self.container_name):
	        chk=commands.getoutput('sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker start "%s"'%self.container_name)
	        chk=chk[78:]	
		if chk:
			tmp=commands.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect '%s'"%self.container_name)
			tmp1=tmp[78:]
			fp=open("/tmp/start.json","w")
			fp.write(tmp1)
			fp.close()
			fp=open("/tmp/start.json","r")
			b=json.load(fp)
			fp.close()
			d=dict()
			d["ID"]=b[0]["Id"]
			d["Stime"]=b[0]["State"]["StartedAt"]
			d["Etime"]=b[0]["State"]["FinishedAt"]
			d["Status"]=b[0]["State"]["Status"]
			d["IP"]=b[0]["NetworkSettings"]["Networks"]["mynet0"]["IPAddress"]
			if d["Status"]=="running":
				return d
			else:
				print("Container not running!!")
		else:
			return 0
	def startdb(cursor,self.container_name,self.start_time,self.end_time):
	        sql=('update container set start_time="%s",end_time="%s" where container_name="%s"'%(self.start_time,self.end_time,self.container_name))
	        chk=cursor.execute(sql)
	        if chk==1L:
	                return 1
	        else:
	                return 0
	
	def stop_cont(name):
	        chk=commands.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker stop '%s'"%name)
	        if chk:
			tmp=commands.getoutput("sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker inspect '%s'"%name)
			tmp1=tmp[78:]
			fp=open("/tmp/stop.json","w")
			fp.write(tmp1)
			fp.close()
			fp=open("/tmp/stop.json","r")
			b=json.load(fp)
			fp.close()
			d=dict()
			d["ID"]=b[0]["Id"]
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
	        chk=commands.getoutput('sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker rm "%s"'%name)
	        chk=chk[78:]
		print(chk)
		if chk:
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

