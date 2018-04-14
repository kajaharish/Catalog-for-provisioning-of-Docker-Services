#!/usr/bin/python2
import commands as cmd
import MySQLdb
def removeCont(name):
	chk=cmd.getoutput('sshpass -p Cascaders1@3 ssh -o StrictHostKeyChecking=no root@127.0.0.1 docker rm %s'%name)
	if chk==name:
		return 1
	else:
		return 0
def connectdb():
	db=MySQLdb.connect("172.10.20.1","root","123456","minor_db")
	cursor=db.cursor()
	return (db,cursor)
def updatedb(cursor,name):
	sql=('delete from container where container_name="%s"'%name)
	chk=cursor.execute(sql)
	if chk==1L:
		return 1
	else:
		return 0
if __name__=="__main__":
	name=raw_input("Enter the name of container you want to remove: ")
	chk=removeCont(name)
	try:
		if chk==1:
			db,cursor=connectdb()
			if db:
				tmp=updatedb(cursor,name)
				if tmp==1:
					print("Container removed successfully.")
					db.commit()
					db.close()
			else:
				print("Can't connect to db!!")
		else:
			print("Cannot remove Container!!")
	except:
		print("Wuuhuuuu!!!")
		db.rollback()	
	
