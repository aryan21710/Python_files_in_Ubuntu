#!/usr/bin/python3

import connectivity
import requests as req
from bs4 import BeautifulSoup as bs
import os,os.path,sys
import ssl
from time import sleep
from requests.exceptions import Timeout, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError
from selenium import webdriver


path=r'/home/ary/BKP/python_scripts/ubuntu_scripts/webscraping/freelancer'
os.chdir(path)
link='https://www.zomato.com/bangalore/collections'
def req_html_data(link):
    print ('THE LINK TO BE SCRAPED:-',link.strip())
    cnt=8
    while (cnt>5):
          try:
             reqObj=req.get(url=link.strip(),stream=True,timeout=90,headers = {'user-agent': 'my-app/0.0.1'}).text
             #print ('REQOBJ...',reqObj)
             break 
          except (Timeout, ssl.SSLError, ReadTimeoutError, ConnectionError) as exc:
             print ('ERROR:-',exc)
             if exc:
                cnt-=1
                print ('SLEEPING NOW AGAIN FOR TIME:-',cnt)
                sleep(180)
                


    with open('zomato.html','w') as f:
         f.write(reqObj)
    if os.path.exists('zomato.html') and os.path.getsize('zomato.html') > 0:
       print ('ZOMATO HTML FILE READY:-')
       return reqObj
    else:
       return False


def process_html_data(soup):
    '''  
    listHotels=soup.find('div',class_='ui segment zred tac')
    listHotels=listHotels.parent.get('href') 
    '''

    listHotels=[]
    bdy=soup.body
    f=open('zomato_html.data','w')
    f.write(str(bdy))
    for collection in bdy.find_all('div',class_='collections-grid clearfix'):
        print ('collection....',collection)
    '''
    for i in collection.find_all('a'):
        listHotels.append(i.get('href'))
    '''
    print ('listHotels...',listHotels)

    
    return listHotels

def process_listOfHotels(listHotels):
    brw=webdriver.Firefox()
    link=brw.get(listHotels)
    link=link.click()
    print ('IN SELENIUM CODE....',link)


reach=connectivity.chk_connect('www.google.com')
print ('REACH...',reach)
#reqObj=req.get(url=link,stream=True).text

#print ('REQOBJ...',reqObj)
if reach:
   print ('NETWORK CONNECIVITY ACHIEVED.....')
   reqObj=req_html_data(link)
   if reqObj:
      #print ('REQOBJ...',reqObj)
      soup=bs(reqObj,'lxml')
      #print ('HTML DATA:-',soup.prettify())

      hotels=process_html_data(soup)


