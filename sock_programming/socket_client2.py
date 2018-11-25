#!/usr/bin/python3

import socket,os,subprocess

s=socket.socket()
h=socket.gethostname()
p=12222

s.connect((h,p))
data=s.recv(1024)

subprocess.check_output(['touch','socket_client2_writetofile.txt'])

print ('$$$ DATA COMING FROM SERVER:- $$$',data)

if os.path.isfile('socket_client2_writetofile.txt'):
   print ('FILE TO WRITE EXISTS.....')
   with open('socket_client2_writetofile.txt','wb') as f:
        f.write(data)
print ('\n'*2)
print ('READING THE CONTENTS OF NEW FILE WRITTEN BY CLIENT:-')
print ('*' * 60)
with open('socket_client2_writetofile.txt','r') as f:
     for line in f:
         line=line.split()
         print (line)

print ('*' * 60)

subprocess.check_output(['rm','-rf','socket_client2_writetofile.txt'])
s.close()
