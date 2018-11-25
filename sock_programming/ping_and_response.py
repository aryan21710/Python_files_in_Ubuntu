#!/usr/bin/python3

import socket,os,subprocess,re

h=input('Enter the FQDN Of the Website to Ping Or Enter Local \
to Ping local Machine:-')

if h.lower()=='local':
   s=socket.socket()
   h=socket.gethostname()


ip=socket.gethostbyname(h)
print ('\n' * 2)
print ('+'*60)
print ('PINGING "{0}" AT "{1}" :-'.format(h,ip))
png=subprocess.check_output(['ping','-c 5', ip])

png=str(png).split('\\n')
print ('PING RESPONDING:-',png)
print ('\n' * 2)
print ('+'*60)
t=str(type(png))
out=re.search(".*list.*",t)
if out:
   print ('ITS A LIST:-',out.group())
   if len(png) > 1:
      for i in png:
          out=re.search('([0-9]+)%(\s+packet\s+loss)',i)
          if out:
             print ('PING SUCCESSFUL. PACKET LOSS:-',out.group(1))
             break
