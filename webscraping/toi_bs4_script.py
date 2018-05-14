#!/usr/bin/python3

import connectivity
import requests as req
from bs4 import BeautifulSoup as bs
import os,os.path,sys
import re

def format_output(place):
  
    if place=='inFile': 
       f2.write('%' * 100)
       f2.write('\n')
    elif place=='inConsole':
       print('%' * 100)
       print('\n')

def find_all_class_in_div(soup):
    format_output('inFile')
    bdy=soup.body
    div_class_list=[]
    f2.write("FOLLOWING ARE THE DIV'S ....\n")
    for idiv in bdy.find_all('div'):
              if idiv.get('class')!=None:
                 for i in range(0,len(idiv.get('class'))):
                     div_class_list.append(str(idiv.get('class')[i]))

    format_output('inFile')
    f2.write('THE LIST OF CLASSES ARE AS FOLLOWS....')
    for i in div_class_list:
        f2.write(i+'\n') 
    format_output('inFile')
 
    if 'top-story' in div_class_list and 'stories' in div_class_list:
         f2.write('TOP STORY AND STORIES CLASS FOUND....\n')
         
         topstory=bdy.find('div',class_='top-story')
         f2.write('topstory:-'+str(topstory)+'\n')
         return topstory
    else:
         print ('FUNCTION FIND_ALL_CLASS_IN_DIV FAILED....')
         return False
    
def get_headlines(news,soup):
    print ('*' * 100)
    print ('HEADLINES ARE AS FOLLOWS \n')
    print ('*' * 100)
    if news=='T':
       topstory=find_all_class_in_div(soup)
       if topstory:
          format_output('inConsole')
          for i in topstory.ul.find_all('li'):
              print(i.a.get('title'))
              link=str(i.a.get('href'))
              out=re.search('(^https)',link)
              if out:
                 print(link+'\n')
              else:
                 print ('https:/'+link+'\n')


    elif news=='E':
       stories=find_all_class_in_div(soup)
       if stories:
          format_output('inConsole')
          story=soup.body.find('div',class_='stories')
          format_output('inFile')
          f2.write('ENTERTAINMENT CLASS "STORIES" IS AS FOLLOWS...\n')
          f2.write(str(story)+'\n')
          for i in story.ul.find_all('li'):
              print (i.a.get('title') + '\n') 
              link=str(i.a.get('href'))
              out=re.search('(^https)',link)
              if out:
                 print(link+'\n')
              else:
                 print ('https:/'+link+'\n')



    print ('*' * 100)

reach=connectivity.chk_connect('www.google.com')
if reach:
   f2=open('toi_bs4_script.log','w')
   format_output('inFile')
   f2.write('ALL SITES ARE REACHABLE.....\n')
   link='https://timesofindia.indiatimes.com/'
   os.chdir('/home/ary/BKP/python_scripts/ubuntu_scripts/webscraping')

   reqObj=req.get(url=link,stream=True).text
   with open('toi_html_data','w') as f:
        f.write(reqObj)


   if os.path.exists('toi_html_data') and os.path.getsize('toi_html_data') > 0:
      f2.write('TOI HTML DATA DOWNLOADED LOCALLY USING REQUESTS MODULE\n')

     
      soup=bs(reqObj,"lxml")
      with open('toi_html_data2','w') as f:
           f.write(soup.prettify())
           format_output('inConsole')
           print('WHAT NEWS YOU WOULD LIKE TO READ, ENTER FROM FOLLOWING OPTION...')
           inp=input('T= TOP_STORY, E= ENTERTAINMENT, L=LATEST_NEWS :-')
           if inp.upper()=='T':
                 get_headlines('T',soup)
           elif inp=='E':
                 get_headlines('E',soup)


      f2.close()
   else:
      print('FAILED:-CHECK THE PAGE SOURCE, THE CLASS FOR TOP-STORY IS CHANGED....')
else:
   print('FAILED:- CHECK YOUR INTERNET CONNECTION..')  


 
