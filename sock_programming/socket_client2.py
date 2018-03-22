#!/usr/bin/python3

import socket

s=socket.socket()
h=socket.gethostname()
p=12222

s.connect((h,p))
data=s.recv(1024)

print ('$$$ DATA COMING FROM SERVER:- $$$',data)
s.close()
