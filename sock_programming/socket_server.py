#!/usr/bin/python3

import socket

s = socket.socket()
host=socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(15)

while (True):
      c,addr=s.accept()
      print ('THE CLIENT IP {} AND OBJ IS {}'.format(addr,c))
      c.send('CONNECTION SUCCESSFULL . THIS IS A TEST MESSAGE')
      c.close()
