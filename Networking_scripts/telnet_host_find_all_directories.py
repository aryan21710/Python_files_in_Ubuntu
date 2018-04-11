#!/usr/bin/python3

import telnetlib as tlib
import getpass
import re


def connect_telnet(h,u,p,tn):
    print('INSIDE CONNECT_TELNET FUNCTION:-')
    print ('*' * 100)
    print ('LOgin Credentials:-',u,'@',h, 'with', tn)
    print ('*' * 100)

    #tn=tlib.Telnet(h)

    tn.read_until(b"login: ")
    tn.write((u+"\r\n").encode('ascii'))
    tn.read_until(b"Password: ")
    tn.write((p+"\r\n").encode('ascii'))
    tn.write(b"cd /home/aryan/python_scripts/ubuntu_scripts\n")
    tn.write(b"ls -l\n")
    tn.write(b"exit\n")
    output=(tn.read_all().decode('ascii'))
    tn.close()

    return output


def search(output):
    print ('*' * 100)
    print ('INSIDE THE SEARCH FUNCTION:------')
    print ('THIS WILL PRINT ALL THE DIRECTORIES.....')
    print ('*' * 100)

    output=output.split('\n')
    expr=r'^(d[-rwx]+)(.*)'
    
    for i in output:
        out=re.search(expr,i)
        if out:
           d=out.group(2).split(' ')[-1:]
           print ('DIRECTORY NAME:-',d, '**',out.group(1))    
        
    




h=input('Enter the Host to Login:-')
u=input('ENter the Username to Login:-')
p=getpass.getpass()
tn=tlib.Telnet(h)

output=connect_telnet(h,u,p,tn)
print ('The final output:-')
print ('*' * 100)
print (output)
print ('*' * 100)

search(output)









