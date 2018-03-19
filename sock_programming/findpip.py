#!/usr/bin/python3

import re
with open('pip','r') as f:
     expr='([a-zA-Z0-9-]+(pip))'
     for line in f:
         line=line.split()
         line=str(line)
         o=re.search(expr,line)
         if o:
            print ('MATCH:-',o.groups()) 

