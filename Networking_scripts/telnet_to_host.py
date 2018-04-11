#!/usr/bin/python3

import telnetlib
import getpass
import sys

h='localhost'
u='test'
p='test123'


tn=telnetlib.Telnet(h)
tn.read_until(b"login: ")
tn.write((u+"\r\n").encode('ascii'))
tn.read_until(b"Password: ")
tn.write((p+'\r\n').encode('ascii'))
tn.write(b"ls\n")
tn.write(b"exit\n")
print ('OUTPUT OF LS AFTER TELNETTING TO THE HOST:-',(tn.read_all().decode('ascii')))
tn.close()




