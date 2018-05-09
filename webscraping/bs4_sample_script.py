#!/usr/bin/python3

import requests as req
from bs4 import BeautifulSoup as bs
import os,os.path
import re



link='http://www.pythonforbeginners.com'

r=req.get(url=link,stream=True)
data=r.text
if r.status_code==200:
   with open('temp_bs4_sample_script','wb') as f:
        for line in r:
            f.write(line)



   if os.path.exists('temp_bs4_sample_script'):
      if os.path.getsize('temp_bs4_sample_script') > 0:
         print ('FILE DOWNLOADED WITH SIZE:-',os.path.getsize('temp_bs4_sample_script'))


# BEAUTIFUL-SOUP CODE STARTS... 

# YOU NEED TO PROVIDE THE FILE IN TEXT FORMAT FOR BS TO PARSE THE HTML PAGE. (data=r.text)
# THATS THE REASON REQUESTS MODULE IS USED TO DOWNLOAD THE HTML PAGE FIRST

soup=bs(data,"lxml") # "lxml" is one of the html parser used to decode the html pages

print ('\n' * 2)
print ('&' * 100)
# THIS WILL PRINT THE NAMES OF ALL TAG WHICH ARE STARTING WITH H {HEAD, H1, H2, H3....}
for i in soup.find_all(re.compile('^h')):
    print (i.name)

print ('\n' * 2)
print ('&' * 100)

print ('\n' * 2)
print ('&' * 100)
# THIS WILL PRINT THE NAMES OF ALL TAGS 
for i in soup.find_all(True):
    print (i.name)

print ('\n' * 2)
print ('&' * 100)



print ('\n' * 2)
print ('&' * 100)
# THIS WILL PRINT THE CONTENTS OF PROPERTY TAG DATA UNDER META TAG
for i in soup.find_all('meta'):
    print (i.get('property'))

print ('\n' * 2)
print ('&' * 100)


print ('\n' * 2)
print ('&' * 100)
# THIS WILL PRINT THE CONTENTS OF ALL a AND title TAGS together
for i in soup.find_all(['a','title']):
    print (i)

print ('\n' * 2)
print ('&' * 100)


print ('\n' * 2)
print ('&' * 100)
# THIS WILL PRINT THE CONTENTS OF ALL a TAGS under which we have title=='Home'
for i in soup.find_all('a'):
    if i.get('title')=='Home':
       print ('FOUND:-',i.get('title'))

print ('\n' * 2)
print ('&' * 100)

print ('\n' * 2)
print ('&' * 100)
# THIS WILL PRINT THE CONTENTS OF ONLY THAT div TAGS under which we have class=='navbar-header'
# SINCE div.class contents are in list format, first we have to regexp to indentify only
# those div.class that are in list format.
for i in soup.find_all('div'):
    if re.search('list',str(type(i.get('class')))):
       #print (i.get('class'),':',len(i.get('class')),':',type(i.get('class')))
       if 'navbar-header' in i.get('class'):
           print ('FOUND:-',i.get('class'))
print ('\n' * 2)
print ('&' * 100)

print ('\n' * 2)
print ('&' * 100)
# PRETTIFY WILL PRINT THE CONTENTS OF ENTIRE HTML PAGE INTO A READABLE HTML FORMAT.
with open('prettify_html_file','w') as f: 
     f.write(soup.prettify())

if os.path.exists('prettify_html_file') and os.path.getsize('prettify_html_file') > 0:
   print ('PLEASE CHECK THE CONTENTS OF FILE prettify_html_file....')
print ('\n' * 2)
