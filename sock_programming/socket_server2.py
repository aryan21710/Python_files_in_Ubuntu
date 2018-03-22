#!/usr/bin/python3

import socket
from time import sleep

s=socket.socket()
h=socket.gethostname()
p=12222
s.bind((h,p))

s.listen(2)
f=open('/home/aryan/python_scripts/ubuntu_scripts/fakeetcpasswd.txt','rb')
l=f.read()
print ('\n'*2)
print ('FILE:-',l)
print ('\n'*2)
while True:
    c,addr=s.accept()
    print('CONNECTION RECEIVED FROM CLIENT:-',addr)
    print('*'*60)
    print ('$$$$DATA SENDING TO CLIENT:-$$$$')
    c.send(l)
   
c.close() 
