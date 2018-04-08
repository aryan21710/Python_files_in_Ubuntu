#!/usr/bin/python3

from collections import defaultdict

a=defaultdict(int)
b=defaultdict(int)
c=defaultdict(int)

nm=(input('ENTER THE 2 INTEGERS SEPARATED BY SPACES:-'))
nm=nm.split(' ')
alen=int(nm[0])
blen=int(nm[1])
print ('alen , blen:-',alen,blen)


for i in range(1,alen+1):
    a[i]=(input('Enter contents of Dictionary One at a Time:-'))

for i in range(1,blen+1):
    b[i]=(input('Enter contents of Dictionary One at a Time:-'))

print ('A DICT:-',a)
print ('B DICT:-',b)
for k,v in b.items():
    for k1,v1 in a.items():
        if v not in a.values():
           c[v]=-1
        else:
           if v==v1:
              if v in c:
                 c[v1]=str(c[v1])+' '+str(k1)
              else:
                 c[v1]=k1

print ('FINAL DICT:-',c) 
      
for k,v in b.items():
    for k1,v1 in c.items():
        if v==k1:
           print (v1,end='\n')

 
