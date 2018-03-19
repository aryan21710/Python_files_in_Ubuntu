#!/usr/bin/python3

import os,sys,subprocess,time,re


def get_filename():
    path=os.getcwd()
    lsout=subprocess.check_output(['ls','-l'])
    lsout=str(lsout)
    lsout=lsout.split('\n')

    for line in lsout:
        out=re.search('([_a-zA-Z]+.txt)',line)
        if out:
           filename=(out.group())
           print ('FOUND A FILE TO PROCEED:-',filename)
    lsout=str(subprocess.check_output(['ls','-l',filename]))
    print ('FILE:- {0}, OTHER INFO:- {1}'.format(filename,lsout))
    timestamp=re.search('[a-zA-Z]+\s+([0-9]{1,2})\s+[0-9]{2}:[0-9]{2}',lsout)
    if timestamp:
       print ('TIME:-',timestamp.group())

    print ('FILENAME:-"{0}", TIMESTAMP:-"{1}"'.format(filename,timestamp.group())) 
    
get_filename()






