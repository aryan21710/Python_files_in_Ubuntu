#!/usr/bin/python3

import socket

c=socket.socket()

ip=input('Enter Server\'s IP Address:-')
p=int(input('Enter Port:-'))
#host,fqdn,ipadd=socket.gethostbyadd(ip)
c.connect((ip,p))
print ('*' * 60)
print ('Connected to Server On {0}:{1}'.format(ip,p)) 
print ('Sending Server a Hello Message ....')
c.sendall(b'Hello Server.This is Client')
print ('Waiting for the Response....')
d=c.recv(1024)
print ('Server Returned Response from {0}:{1}:-{2}'.format(ip,p,d))
print ('*' * 60)
print ('\n'*2)


