#!/usr/bin/python3
import math

inp=input('Enter 2 integers:-')
inp=inp.split(' ')
x=int(inp[0])
k=int(inp[1])
total=0
for i in range(1,5):
       total+=pow(x,(k-i))-1*pow(x,k-2)+5*pow(x,k-3)

total+=1
print ('TOTAL:-',total)
if total==k:
   print (True)
else:
   print (False)





