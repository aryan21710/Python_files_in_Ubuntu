#!/usr/bin/python3

from collections import defaultdict
import os

os.chdir('/home/aryan/python_scripts/ubuntu_scripts/hacker_rank')

a=defaultdict(int)
b=defaultdict(int)
c=defaultdict(int)
'''
nm=(input('ENTER THE 2 INTEGERS SEPARATED BY SPACES:-'))
nm=nm.split(' ')
alen=int(nm[0])
blen=int(nm[1])
print ('alen , blen:-',alen,blen)
'''
linecnt=1
with open('defaultdict_output.txt','r') as f:
     for line in f:
         if linecnt < 10001:
            line=line.rstrip()
            a[linecnt]=line
            linecnt+=1
         else:
            line=line.rstrip()
            b[linecnt]=line
            linecnt+=1
print ('A DICT:-',a)
print ('\n' * 4)
print ('B DICT:-',b)


print ('\n' * 4)
cnt=1
for k,v in b.items():
    for k1,v1 in a.items():
        if v not in a.values():
           c[v]=-1
        else:
           if v==v1:
              #print ('Match found:-',k,'@@',v,':::::',k1,'@@',v1)
              cnt+=1
              if v in c:
                 c[v1]=str(c[v1])+' '+str(k1)
              else:
                 c[v1]=k1

print ('\n' * 4)
print ('C DICT:-',c)
'''
with open('output_check.txt','w') as f:
     f.write(str(c))
'''      
with open('output_check.txt','w') as f:
    f.write('\n' * 4)
    for k,v in b.items():
        for k1,v1 in c.items():
            if v==k1:
               x='MATCHED:-'+ v +' AND '+k1
               #f.write(x)
               f.write(v1)
