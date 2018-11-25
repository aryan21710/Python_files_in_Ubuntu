#!/usr/bin/python3

import re,codecs,os,sys,subprocess

def encode_decode(filename):
    uid,usr,passwd,encusr,encpass=[],[],[],[],[]
    if os.path.isfile(filename):

       with open (filename,'r') as f:
            for line in f:
                 line=line.split()
                 uid.append(line[0])
                 usr.append(line[1])
                 passwd.append(line[2])
                 print ('USERNAME "{0}", PASSWD "{1}" :-'.format(line[1],line[2]))

       with open(filename,'a') as f1:
            f1.write('*' * 15 + 'ENCYRPTING NOW' + '*' * 15 +'\n')
            for i in range(len(usr)): 
                usrenc=codecs.encode(usr[i],'rot13')
                print ('USERNAME:- "{}", ENCRYPTED USERNAME:- "{}"'.format(usr[i],usrenc))
                passwdenc=codecs.encode(passwd[i],'rot13')
                print ('PASSWD:- "{}", ENCRYPTED PASSWD:- "{}"'.format(passwd[i],passwdenc))
                f1.write(uid[i] + " " + usrenc + " " +passwdenc + '\n')            
                encusr.append(usrenc)         
                encpass.append(passwdenc)         

       with open(filename,'a') as f1:
            f1.write('*' * 15 + 'DECRYPTING NOW' + '*' * 15 +'\n')
            for i in range(len(encusr)): 
                usrenc=codecs.decode(encusr[i],'rot13')
                print ('USERNAME:- "{}", DECRYPTED USERNAME:- "{}"'.format(encusr[i],usrenc))
                passwdenc=codecs.decode(encpass[i],'rot13')
                print ('PASSWD:- "{}", DECRYPTED PASSWD:- "{}"'.format(encpass[i],passwdenc))
                f1.write(uid[i] + " " + usrenc + " " +passwdenc + '\n')            

filename='fakeetcpasswd.txt'
subprocess.check_output(['touch',filename])
flag=0
if os.path.isfile(filename):

   with open (filename,'r') as f:
        for line in f:
            out=re.search('(ENCYRPTING)',line)
            if out:
               flag=1
               break

if flag:
   print ('FILE IS ALREADY ENCRYPTED & DECYRPTED ONCE:-')
else:
   encode_decode(filename)
