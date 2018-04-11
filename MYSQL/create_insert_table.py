#!/usr/bin/python3

import MySQLdb as mdb

sq_host='localhost'
sq_user='root'
sq_passwd='Mango205'
sq_database='newtestdb'

sq_obj=mdb.connect(sq_host,sq_user,sq_passwd,sq_database)

curs=sq_obj.cursor()

curs.execute('use newtestdb')

print ('DATABASE VERSION INSTALLED:-',curs.execute("SELECT VERSION()"))

def create_table(curs,sq_obj):
    print ('\n' * 2)
    print ('*' * 60)
    print ('******I AM INSIDE CREATE TABLE FUNCTION-*******')
    curs.execute("create table MyMobiles(Brand VARCHAR(20),Model VARCHAR(20),Price_in_Thousands VARCHAR(20),Color VARCHAR(20))")
    sq_obj.commit()
    print ('YOUR TABLE IS READY:-')
    print (curs.execute('describe MyMobiles'))
    out=curs.execute('select * from MyMobiles')
    if out >= 1:
       output=curs.fetchall()
       print ('THE CONTENTS OF TABLE ARE:-',output)
    
    print ('*' * 60)

def insert_data(curs,sq_obj):
      print ('\n' * 2)
      print ('*' * 60)
      print ('INSERTING DATA INTO THE TABLE NOW:-')
      print ('BRAND SAMSUNG ALREADY EXISTS:-',curs.execute("select count(BRAND='SAMSUNG') FROM MyMobiles"))
      curs.execute("insert into MyMobiles(BRAND, MODEL, PRICE_IN_THOUSANDS, COLOR) values('SAMSUNG','NOTE8','60K','BLACK')")
      sq_obj.commit()
      out=curs.execute('select * from MyMobiles')
      if out >= 1:
         output=curs.fetchall()
         print ('AFTER INSERTION, THE CONTENTS OF TABLE ARE:-')
         print ('\n' * 2)
         print (output)
         print ('*' * 60)
         print ('\n' * 2)


inp=input('Enter C to Create a New Table OR Enter E for an Existing One:---')
if inp.upper()=='C':
   create_table(curs,sq_obj)
   while (True):
         inp=input('Enter I to Insert New Data OR EXIT to EXIT The Script:---')
         if inp.upper()=='I':
            insert_data(curs,sq_obj)
         elif inp.upper()=='EXIT':
            print ('OK EXITING THE SCRIPT NOW.....')
            break
            
         

sq_obj.close()
