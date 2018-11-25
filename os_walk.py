#!/usr/bin/python3

import os,sys

d=input('ENter the Name of the Dir :-')

i=0
if not d:
   d=os.getcwd()
else:
   if os.path.isdir(d):
      for root,dirs,files in os.walk(d):
          print ('\n'*2)
          print ('+'*60)
          print ('The root of the DIr Structure:-',root)
          print ('Found "{}" SubDirectories:-'.format(len(dirs)))
          print ('List of SUbDirectories Are:-', dirs)
          print ('No of Files Found in this Dir:-',len(files)) 
          print ('List of Files Are:-')
          for filename in files:
              print (os.path.join(root,filename), ' ',i)
              if os.path.isfile(os.path.join(root,filename)):
                 i+=1
                 if i==10:
                    key=input('HIT Any Key To Continue:-')
                    i=0
              else:
                 print ('SOMETHING WRONG WITH OS.PATH.JOIN:-')
                 break
                  
                
