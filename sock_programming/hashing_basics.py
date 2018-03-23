#!/usr/bin/python3
'''
THE BELOW HASHING RESULT CAN BE VERIFIED AT
hash.online-convert.com
'''



import hashlib

print ('Hashing Algorithms Available:-',hashlib.algorithms_available)
print ('\n')
print ('*' * 60)
inp=input('Enter Any String to Hash:-')
hobj=hashlib.md5()
hobj.update(inp.encode('utf-8')) # WITHOUT ENCODING UTF-8, IT WONT WORK 
print ('String "{}" became "{}" After MD5 Encryption'.format(inp,hobj.hexdigest()))


print ('\n')
print ('*' * 60)
hobj=hashlib.sha1()
hobj.update(inp.encode('utf-8')) # WITHOUT ENCODING UTF-8, IT WONT WORK 
print ('String "{}" became "{}" After SHA Encryption'.format(inp,hobj.hexdigest()))



