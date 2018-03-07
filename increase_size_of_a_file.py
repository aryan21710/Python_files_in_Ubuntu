#!/usr/bin/python3
# THIS FILE WILL INCREASE THE SIZE OF A UNIX FILE BY PUTTING RANDOM CONTENTS IN IT
import os
import subprocess
import sys
import os.path


with open('a.txt','w') as f:
    
     print ('INITIAL SIZE OF THE FILE :- {}'.format(os.path.getsize('a.txt')))
     usersize=int(input('ENTER THE SIZE OF THE FILE U WANT TO CREATE:-'))
     if os.path.isfile('a.txt'):
        for i in range(0,usersize+1):
            if os.path.getsize('a.txt')<usersize:
               f.write(str(i)+'\n')
               #print('NEW SIZE OF THE FILE:- {}'.format(os.path.getsize('a.txt')))


print('FINAL SIZE OF THE FILE:- {}'.format(os.path.getsize('a.txt')))
