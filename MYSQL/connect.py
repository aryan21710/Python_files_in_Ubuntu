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
try:
   curs.execute("create table APT(BANGALORE VARCHAR(20), NAGPUR VARCHAR(20), HYDERABAD VARCHAR(20))")
   connect_obj.commit()
except:
   print ('TABLE ALREADY EXISTS. CANT CREATE THE SAME TABLE:-')

try:
   curs.execute("select count(BANGALORE) from APT where BANGALORE='E81333'")
   output=curs.fetchall()
   '''
   curs.execute("insert into APT(BANGALORE, NAGPUR, HYDERABAD) values('E8133','E1001','E1101')")
   connect_obj.commit()
   curs.execute('select * from APT')
   output=curs.fetchall()
   '''
   print ('*' * 60)
   print ('THE TABLE AND ITS CONTENTS ARE .......',output)
   print ('*' * 60)
except:
   print ('CANT DISPLAY THE CONTENTS OF THE TABLE SINCE IT DOESNT EXIST:-')

print (curs.execute('select * from APT'))






