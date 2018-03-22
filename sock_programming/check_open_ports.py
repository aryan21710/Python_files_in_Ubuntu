#!/usr/bin/python3

import socket,subprocess,re

s=socket.socket()
host=socket.gethostname()
nmap_lst_out=[]
s=socket.socket()

print ('The Name of the Local Machine:-',host)
print ('\n' * 2)
print ('*' * 60)
print('PLEASE WAIT SCANNING THE REMOTE HOST {} AT {}'.format(host,socket.gethostbyname(host)))
print ('*' * 60)
for port in range(1,1024):
    try:
       s.connect((host,port))
       open_port=socket.getservbyport(port)
       print ('PORT {0} OPEN'.format(open_port))
       s.close()
       s=socket.socket()
       
    except:
      #pass
      #print ("XXX PORT '{0}' CLOSED XXX:-".format(port))
      print ("\r+",end="")
    
   
nmap_out=subprocess.check_output(['nmap','UbuntuOnAryMac'])

nmap_out=str(nmap_out)
nmap_out=nmap_out.split('\\n')

for i in nmap_out:
    out=re.search('(open\s+)([a-zA-Z]+)',i)
    if out:
       nmap_lst_out.append(out.group(2))
       print ('NMAP OPEN PORT:-',out.group(2))



    
