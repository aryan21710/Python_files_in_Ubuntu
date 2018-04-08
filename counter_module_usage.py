#!/usr/bin/python3
'''
Counter is a container that tracks how many times equivalent values are added. 

The Collections module implements high-performance container datatypes (beyond 
the built-in types list, dict and tuple) and contains many useful data structures
that you can use to store information in memory.

Containers are objects that hold objects. They provide a way to access the contained objects and 
iterate over them. Examples of built in containers are Tuple, list and dictionary. 
Others are included in Collections module.

'''

from collections import Counter
import os

os.chdir('/home/aryan/python_scripts/ubuntu_scripts')
d=os.getcwd()
# BELOW IS THE CODE TO INITIALIZE THE COUNTER OBJ IN 3 DIFFERENT WAYS
c1=Counter(['s','a','s','r','r','a','a','a','s']) #INITIALIZED AS LIST
c2=Counter({'ary':3,'sim':2,'ryan':1}) # INITIALIZED AS DICT

c3=Counter()
for i in ['zx','duc','zx','busa','multi','multi']:
    c3[i]+=1

print ('*' * 40)
print ('C1 Counter:-',c1)
print ('C1 Counter:-',c2)
print ('C3 Counter:-',c3)
print ('C1 ELements:-',list(c1.elements()))
print ('C2 Elements:-',list(c2.elements()))
print ('C3 Elements:-',list(c3.elements()))
print ('C1 ITEMS:-',c1.items())
print ('C1 Keys:-',c1.keys())
print ('C1 Values:-',c1.values())
print ('*' * 40)

print ('\n')
print ('*' * 40)
c1.update('asraaars') # UPDATING THE CONTENTS OF COUNTER OBJECT
print ('After Update C1 ELements:-',list(c1.elements()))
print ('*' * 40)
print ('\n')

c4=Counter()
with open('fakeetcpasswd.txt','r') as f:
     print ('Reading file :-',os.path.join(d,'fakeetcpasswd.txt'))
     c4=Counter(f.read()) # ONE MORE WAY TO INITIALIZE THE COUNTER OBJ
     print ('Most COMMON 4 ELEMENTS OF THE LIST:-',c4.most_common(4)) 
     print ('Elements of C4 Counter :-',list(c4.elements()))

print ('*' * 40)
print ('\n'*2)


