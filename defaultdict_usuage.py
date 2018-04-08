#!/usr/bin/python3
'''
The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but it has one difference: 
The value fields' data type is specified upon initialization. 


 a Python dictionary throws a KeyError if you try to get an item with a key that is not currently 
in the dictionary. The defaultdict in contrast will simply create any items that you try to 
access (provided of course they do not exist yet). i

defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being 
thrown, a new entry is created. The type of this new entry is given by the argument of defaultdict
'''

from collections import defaultdict


d=defaultdict(list) # THE VALUES OF THE DICT WILL BE LIST

d['anandam'].append('E1001')
d['grande'].append('E1101')
d['sobha'].append('2094')
d['sobha'].append('6052')
d['prestige'].append('8051')
d['prestige'].append('8133')

for i in d:
    print (i,':', d[i])

print ('keys of defaultdict:=',d.keys())
print ('Values of defaultdict:=',d.values())
print ('TYpe of defaultdict:-',type(d))
print ('*' * 40)


d1=defaultdict(int) # THE VALUES OF THE DICT ARE INT
for i in range(10):
    d1[i] = i+i

print ('*' * 40)

print ('keys of defaultdict:=',d1.keys())
print ('Values of defaultdict:=',d1.values())
print ('TYpe of defaultdict:-',type(d1))

print ('*' * 40)

# FOLLOWING CODE WILL GIVE KEYERROR, AS FOR THE \
# KEY DOESNT EXIST, WE CANT INITIALIZE ITS VALUE
del d
d={}
try:
   
   d['anandam'].append('E1001')
   d['grande'].append('E1101')
   d['sobha'].append('2094')
   d['sobha'].append('6052')
   d['prestige'].append('8051')
   d['prestige'].append('8133')
   print ('keys of defaultdict:=',d.keys())  # THIS WILL THROW KEYERROR
   print ('Values of defaultdict:=',d.values())
except:
   print ('DICT ERROR')
