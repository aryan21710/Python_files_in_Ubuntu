#!/usr/bin/python3

import socket

c = socket.socket()
host=socket.gethostname()
port = 12345

print ('HOSTNAME OF SERVER "{0}" AND PORT:- "{1}"'.format(host,port))

c.connect((host,port))

print ('MESSAGE FROM SERVER :-',c.recv(1024))

c.close()

