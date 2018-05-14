#!/usr/bin/python3

import requests as req
from bs4 import BeautifulSoup as bs
import os,os.path
import re


def format_output():
    print ('\n'*2)
    print ('%' * 100)


link='http://www.pythonforbeginners.com'

# REQUESTS ALONG WITH TEXT WILL BE USED TO DOWNLOAD THE CONTENTS OF THE WEBSITE
# MAKE SURE YOU USE TEXT METHOD AS YOU NEED THE WHOLE HMTL CONTENTS OF THE FILE
html_data=req.get(url=link,stream=True).text

f=open('html_data','w')
f.write(html_data)


print ('METHOD #1 TO READ THE WEBSITE:=',html_data)
format_output()

# TO MAKE THE HTML DATA MORE READABLE...
soup=bs(html_data,"lxml")

format_output()
print ('METHOD #2 TO READ THE WEBSITE:=',soup.prettify())


format_output()
# PRINTING OUT ALL THE HEADLINES OF THE URL
print (soup.head.title.text)

format_output()
# PRINTING OUT ALL THE HEADLINES OF THE URL
hentry =soup.find('li',class_='hentry')

print (hentry.prettify())

format_output()
headline1=hentry.h2.a.get("title")
headline2=hentry.h2.a.text
if headline1==headline2:
   print ('PASS:-',headline1,':::',headline2)

format_output()
contents=hentry.find('div',class_='post-bodycopy cf')
print (contents.text)


format_output()
ulcontents=soup.find('ul',class_='nav nav-list')
print (ulcontents.prettify())


format_output()
# THIS WILL PRINT ALL THE HEADLINES AND ITS SUMMARY
for hentry in ulcontents.find_all('li',class_='hentry'):
    headline=hentry.h2.a.text
    print ('HEADLINE:-',headline)
    for divdata in hentry.find_all('div', class_='post-bodycopy cf'):
        summary=divdata.text
        print ('SUMMARY:-',summary)
    print ('\n' *2)
    

format_output()
# THIS WILL PRINT ALL THE META FROM THE HTML_PAGE
for i in soup.find_all('meta'):
    print(i)


format_output()
# CONTENTS PRINTS CHILDREN OF THE PARENT TAG. 1ST IDENTIFY THE PARENT TAG
# CONTENTS IS A LIST. LOOP OVER THE LIST TO PRINT THE CHILDREN OF A PARENT TAG
print ('TYPE of soup.body.ul.contents IS LIST:-',len(soup.body.ul.contents))
for i in range(0,len(soup.body.ul.contents)):
    print (soup.body.ul.contents[i])


format_output()
for child in  soup.body.ul.children:
    print ('child:-',child)
    
format_output()
for child in  soup.body.ul.descendants:
    print (child)


format_output()
# THIS WILL PRINT ALL THE TEXTS FROM THE HTML PAGE
# THIS WILL INCLUDE THE CONTENTS OF JAVASCRIPT CODE
print (soup.get_text())

# THE BELOW CODE IS SAME AS soup.get_text()
format_output()
for i in soup.stripped_strings:
    print (repr(i))


# THIS WILL PRINT ALL THE TEXTS FROM THE HTML PAGE
# THIS WILL INCLUDE THE CONTENTS OF JAVASCRIPT CODE
format_output()
for m in soup.find_all('meta'):
    print (m,':::',m.attrs)


