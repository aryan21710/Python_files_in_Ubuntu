#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
   for i in range(len(sys.argv)):
       print ('Argv[',i,']',' :=',sys.argv[i])
else:
   sys.argv.append('HELLO WORLD')
   for i in range(len(sys.argv)):
       print ('Argv[',i,']',' :=',sys.argv[i])

