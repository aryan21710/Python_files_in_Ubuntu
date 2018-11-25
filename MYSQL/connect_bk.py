#!/usr/bin/python3

import MySQLdb as mdb

sq_host='localhost'
sq_uname='root'
sq_passwd='Mango205'
sq_database='newtestdb'


connect_obj=mdb.connect(sq_host,sq_uname,sq_passwd,sq_database)

print ('SQL CONNECT OBJECT:-',connect_obj)
curs=connect_obj.cursor()
curs.execute('use newtestdb')
curs.execute("insert into APT(BANGALORE, NAGPUR, HYDERABAD) values('PRESTIGE TRANQULITY','ANANDAM','GRANDE')")
connect_obj.commit()
curs.execute('select * from APT')

print (curs.execute('select * from APT'))

connect_obj.close()




