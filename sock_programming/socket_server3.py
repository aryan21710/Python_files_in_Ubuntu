#!/usr/bin/python3

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('*' * 60)
ip=input('Enter IP Address to Bind:-')
p=int(input('Enter POrt No to Bind:-'))
h=str(ip)
s.bind((h,p))
host,fqdn,ipaddr=socket.gethostbyaddr(ip)
print ('HostName to Bind to:-',host)
print ('Server\'s Socket Name:-',s.getsockname())
print ('*' * 60)

print ('\n'*2)
s.listen(5)
inp='y'
while (True):
      c,addr=s.accept()
      if inp.lower()=='y':
         print ('Inbound Request Coming From:-',addr)
         data=c.recv(1024)
         print ('Message Received "{0}" was "{1}":-'.format(s.getsockname(),data))
         print ('Sending a Response Back')
         c.sendall(b'Hello Client This is Server')
         inp=input('continue y or n?')
         print ('\n')
      elif inp.lower=='n':
         print ('Terminating the Socket......')
         s.close()
         break
   

      
