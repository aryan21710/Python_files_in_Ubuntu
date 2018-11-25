#!/usr/bin/python3

import socket
from time import sleep

def server_side():
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

def client_side():

    
    s = socket.socket()
    host=socket.gethostname()
    port = 12345

    print ('HOSTNAME OF THE SERVER:- "{0}" AND PORT USED:-"{1}"'.format(host,port))


    s.connect((host,port))

    print ('MESSAGE FROM SERVER {}'.format(s.recv(1024)))

    s.close()


server_side()
client_side()
