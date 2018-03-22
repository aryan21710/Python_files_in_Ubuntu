#!/usr/bin/python3

import os,sys,re,socket,time,subprocess

ip=input('PLEASE ENTER IP ADDRESS:-')
user=input('PLEASE ENTER USERNAME:-')
passwd=input('PLEASE ENTER PASSWD:-')

d=input('Enter a Dir OR Enter to Continue:-')
f=input('Enter a File OR Enter to Continue:-')

try:
   os.path.isdir(d)
   if not f:
      filename=os.path.join(d,'servers.txt')
   else:
      filename=os.path.join(d,f)
   print ('THE NAME OF THE FILE:-',filename)
   path=os.getcwd()
   with open(filename,'w') as f:
        f.write(ip+'\n')
        f.write(user+'\n')
        f.write(passwd+'\n')
   if os.path.isfile(filename):
      print ('FILE EXISTS:-READING THE CONTENTS OF THE FILE')
      with open(filename,'r') as f:
           print (f.readlines())
except:
   print ('PLEASE ENTER A VALID DIR:=')


print ('GLOBALS:-',globals())

print ('*' * 20)

print ('LOCALS:-',locals())

  




      
