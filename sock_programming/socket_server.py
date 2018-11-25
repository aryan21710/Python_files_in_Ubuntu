#!/usr/bin/python3

import socket

s = socket.socket()
host=socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(15)
filename='/home/aryan/python_scripts/ubuntu_scripts/fakeetcpasswd.txt'
print ('filename:-',filename)
while (True):
      c,addr=s.accept()
      print ('THE CLIENT IP {} AND OBJ IS {}'.format(addr,c))
      #c.sendall(b'CONNECTION SUCCESSFULL . THIS IS A TEST MESSAGE')
      c.sendto(filename, (host,port))
      c.close()
