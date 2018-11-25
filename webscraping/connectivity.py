#!/usr/bin/python

import telnetlib as tn
from scapy.all import *
def chk_connect(ip_rtr):

    res=sr1(IP(dst=ip_rtr)/ICMP(),retry=1,timeout=1)
    expr=r'(echo-reply)'
    try:
       print ('OUTPUT OF SR:-',res.summary())
       output=re.search(expr,str(res.summary()))
       print ('PASSED.....PACKETS RECEIVED:-',output.groups())
       return True
    except:
       print ('FAILED.....REASON:-REGEXP FAILED:-')
       return False

