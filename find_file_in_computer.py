#!/usr/bin/python3

import os,sys

f=input('Enter the Name of the File to Search:-')
d='/home/aryan'

print ('+'*60)
flag=0
if os.path.isdir(d):
      for root,dirs,files in os.walk(d):
          for filename in files:
              if filename==f:
                 print ('FILE FOUND:-')
                 print (os.path.join(root,filename))
                 flag=1
                 break

print ('+'*60)
if not flag:
   print ('FILE NOT FOUND ON THE SYSTEM:-')
