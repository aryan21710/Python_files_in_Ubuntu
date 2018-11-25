#!/usr/bin/python3

import requests as req
import os,os.path
import connectivity

path='/home/ary/BKP/python_scripts/ubuntu_scripts'
link='https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&h=650&w=940'

reach=connectivity.chk_connect('www.google.com')
os.chdir(path)
jpgFile='req_mod_imagefile.jpeg'

if reach:
   print ('\n * 2')
   print ('%' * 100)
   print ('Internet COnnectivity is Reachable....')
   print ('Local dir where the image will be stored:-',os.getcwd())
   print ('The link to download image:-',link)
   with open(jpgFile,'wb') as f:
        reqObj=req.get(url=link,stream=True)
        if reqObj.status_code==200:
           for line in reqObj:
               f.write(line)

  
   if os.path.exists(jpgFile):
      print ('SIZE OF THE FILE:-',os.path.getsize(jpgFile))
      if os.path.getsize(jpgFile) > 0:
         print ('IMAGE DOWNLOADED LOCALLY....')
   print ('\n * 2')
   print ('%' * 100)
else:
 
   print ('FAILED....CHECK YOUR NET CONNECTION....')





