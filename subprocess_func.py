#!/usr/bin/python3


import subprocess,os,sys
filename='file_size_timestamp.py'

os.chdir('/home/aryan/python_scripts/ubuntu_scripts')

print (os.getcwd())

chk=subprocess.check_output(['ls','-l',filename])
print (chk)



