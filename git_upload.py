#!/usr/bin/python3

import os,sys,subprocess
from scapy.all import * # TO IMPORT IN PYTHON3
import re

def connectivity(url):
    print ('\n','*' * 100)
    print ('The URL to Check COnnectivity to:-',url)
    ans=sr1(IP(dst=url)/ICMP())
    if ans.summary():
       print ('URL IS REACHABLE:-',ans.summary())
       return True 
    
     

def git_uplo(repo):
    print ('\n','*' * 100)
    print ('Local Dir Path :-',path)
    print ('Git Repository:-',repo)
    x=subprocess.check_output(['git','add', '-A'])
    print ('X:-',x)
    msg='GIT COMMIT'
    x1=subprocess.check_output(['git','commit', '-m',msg])
    print ('X1:-',x1)
    x2=subprocess.check_output(['git','push' ,repo, 'master'])
    print ('X2:-',x2)
    



url='www.github.com'
path=r'/home/aryan/python_scripts/ubuntu_scripts'
os.chdir(path)
repo= input('PLease Provide the Name of The Git repository to Upload to:-')

output1=connectivity(url)

if output1:
   output2=git_uplo(repo)




