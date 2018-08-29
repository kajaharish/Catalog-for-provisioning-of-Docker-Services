from configure import Container
from ConnectDatabase import Database
class Python(Container):
	def __init__(self):
		self.python=1

	def insertdbpy(self,cursor,uname):
        	sql=('insert into container values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(self.container_name,uname,self.container_id,self.container_ip,self.start_time,self.end_time,self.web_server,self.db_server,self.php,self.python,self.uptime))
        	chk=cursor.execute(sql)
        	if chk==1L:
        	        return 1
        	else:
        	        return 0

	def runpy(self,uname,cursor):
		a=commands.getoutput("sshpass -p %s ssh -o StrictHostKeyChecking=no %s docker run -dt --name=%s ggandhi27/apache_with_python_cgi"%(self.passw,self.ipw,self.container_name))
		a=a[78:]
		if a:
			print("<p>Container started.</p><br>")
		inspectpy(self)
		chk=insertdbpy(self,cursor,uname)
		if chk==1:
			print("<p>Container started and values updated in table.</p><br>")
			return 1
		else:
			print("<p>There is some problem starting the container.</p><br>")
			return 0

	def inspectpy(self):
		cmd = "sshpass -p %s ssh -o StrictHostKeyChecking=no %s docker container inspect"%(self.passw,self.ipw)
		cmd1=cmd+" "+self.container_name
		tmp = commands.getoutput(cmd1)
		tmp1=tmp[78:]
		fp=open("/tmp/runpy.json","w")
		fp.write(tmp1)
		fp.close()
		fp=open("/tmp/runpy.json","r")
		b=json.load(fp)
		fp.close()
		self.container_id=b[0]["Id"]
		self.ipaddress=b[0]["NetworkSettings"]["Networks"]["bridge"]["IPAddress"]
		self.state=b[0]["State"]["Status"]
		self.start_time=b[0]["State"]["StartedAt"]
		self.end_time=b[0]["State"]["FinishedAt"]
		self.container_name=b[0]["Name"]
		if state=="running":
			return
		else:
			print("Container not running.")
			return

class Php(Container):
	def __init__(self):
		self.php=1

	def insertdbphp(self,cursor,uname):
	        sql=('insert into container values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(self.container_name,uname,self.container_id,self.container_ip,self.start_time,self.end_time,self.web_server,self.db_server,self.php,self.python,self.uptime))
	        chk=cursor.execute(sql)
	        if chk==1L:
	                return 1
	        else:
	                return 0

	def runphp(self,uname,cursor):
		a=commands.getoutput("sshpass -p %s ssh -o StrictHostKeyChecking=no %s docker run -dt --name=%s ggandhi27/apache_with_php"%(self.passw,self.ipw,self.container_name)
		a=a[78:]
		if a:
			print("Container running.")
		inspectphp(self)
		chk=insertdbphp(self,cursor,uname)
		if chk==1:
			print("<p>Container started and values updated in table.</p><br>")
			return 1
		else:
			print("<p>There is some problem starting the container.</p><br>")
			return 0

	def inspectphp(self):
		cmd = "sshpass -p %s ssh -o StrictHostKeyChecking=no %s docker container inspect"%(self.passw,self.ipw)
		cmd1=cmd+" "+self.container_name
		tmp = commands.getoutput(cmd1)
		tmp1=tmp[78:]
		fp=open("/tmp/runpy.json","w")
		fp.write(tmp1)
		fp.close()
		fp=open("/tmp/runpy.json","r")
		b=json.load(fp)
		fp.close()
		self.container_id=b[0]["Id"]
		self.container_ip=b[0]["NetworkSettings"]["Networks"]["bridge"]["IPAddress"]
		self.status=b[0]["State"]["Status"]
		self.start_time=b[0]["State"]["StartedAt"]
		self.end_time=b[0]["State"]["FinishedAt"]
		self.container_name=b[0]["Name"]
		if self.status=="running":
			return
		else:
			print("Conatiner does not start.")
			return

if __name__=="__main__":
	dbase=Database()
	dbase.connect(self)
	try:
		if dbase.dbpointer:
			con=Container()
			uname=con.getUserName(dbase.cursor)
			ch=con.fetchValue()
			if ch=="addpy":
				py=Python()
				py.fetchname(self)
				d=py.runpy(self,uname,dbase.cursor)
				if d==1:
					print("""<p>Name: %s
							    Id: %s
							    Status: %s	
							    IP: %s  </p>"""%(d["Name"],d["ID"],d["Status"],d["IP"]))
					dbase.commit(self)
					dbase.close(self)
			elif ch=="addphp":
				php=Php()
				php.fetchname(self)
				d=php.runphp(self,uname,dbase.cursor)
				if d==1:
					print("""<p>Name: %s
                	               	            Id: %s
                	               	            Status: %s  
                	               	            IP: %s  </p>"""%(d["Name"],d["ID"],d["Status"],d["IP"]))
					dbase.commit(self)
					dbase.close(self)
		else:
			print("<p>There is some problem in database connectivity.</p>")
		print("""</body>
			</html>""")
	except Exception as e:
		print(e)
		dbase.rollback(self)
		dbase.close(self)
		print("Wuhuuu!!")	
