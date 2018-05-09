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

    a=tn.read_until(b"login: ")
    a1=tn.write((u+"\r\n").encode('ascii'))
    b=tn.read_until(b"Password: ")
    b1=tn.write((p+"\r\n").encode('ascii'))
    c=tn.write(b"cd /home/aryan/python_scripts/ubuntu_scripts\n")
    c1=tn.write(b"ls -l\n")
    c2=tn.write(b"exit\n")

    print (a,":",a1,":",b,":",b1,":",c,":",c1,":",c2)
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









