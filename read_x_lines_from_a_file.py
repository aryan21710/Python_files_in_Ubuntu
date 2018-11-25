#!/usr/bin/python3

import os

os.chdir('/home/aryan/python_scripts/ubuntu_scripts/hacker_rank')

with open('defaultdict_output.txt','r') as f:
     for i in range(1000):
         print (f.readline(i),end='')
