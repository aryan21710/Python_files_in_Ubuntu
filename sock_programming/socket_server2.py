#!/usr/bin/python3

import socket
from time import sleep

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
h=socket.gethostname()
p=12222
print ('Hostname "{}" and Port "{}" To Connect To:-'.format(h,p))
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
