#!/usr/bin/python3
import sys
print (type(sys.argv[0]), ':::', sys.argv[0])
if len(sys.argv) > 1:
   print (type(sys.argv))
   for i in range(len(sys.argv)):
       print (type(sys.argv[i]))
       print ('Argv[',i,']',' :=',sys.argv[i])
else:
   sys.argv.append('HELLO WORLD')
   for i in range(len(sys.argv)):
       print ('Argv[',i,']',' :=',sys.argv[i])

