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
          print ('No of Dir Inside it:-',len(dirs))
          print ('The Dir Are:-', dirs)
          for filename in files:
              print ('No of Files Are:-',len(files)) 
              print ('The Files Are:-#',i,'"',os.path.join(root,filename),'"')
              if os.path.isfile(os.path.join(root,filename)):
                 i+=1
                 if i==10:
                    key=input('HIT Any Key To Continue:-')
                    i=0
              else:
                 print ('SOMETHING WRONG WITH OS.PATH.JOIN:-')
                 break
                  
                
