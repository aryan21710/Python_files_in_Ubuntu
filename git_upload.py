#!/usr/bin/python3

import os,sys,subprocess
from scapy.all import * # TO IMPORT IN PYTHON3
import re

def connectivity(url):
    print ('The URL to Check COnnectivity to:-',url)
    ans=sr1(IP(dst=url)/ICMP())
    if ans.summary():
       print ('URL IS REACHABLE:-',ans.summary())
       return True 
    
     





url='www.github.com'
path=r'/home/aryan/python_scripts/ubuntu_scripts'
os.chdir(path)
output=connectivity(url)
'''
subprocess.check_output[('git','add', '-A')]
msg='GIT COMMIT'
subrocess.check_output(['git','commit', '-m',msg])
'''



