
from pyzomato import Pyzomato
import traceback
import re
import inspect

def searchRestaurant(details,r):
    print ('\n\n')
    #print ('INSIDE FUNCTION:=',inspect.stack()[0][3])
    f=open('ResDetails','w')
    finalOut={}
    #print ('RESTAURANT ENTERED:-',r)
    if 'restaurants' in details.keys():
        lstRes=details['restaurants']
        for i in lstRes:
            if 'restaurant' in i.keys():
                
                d=i['restaurant']
                
                f.write('*' * 60)
                f.write('d is:-'+ '\n')
                f.write(str(d))
                f.write('\n\n')
                f.write('d.keys :-'+ str(d.keys()))
                f.write('\n\n')
                
                flag=False
                cnt=1
                for k,v in d.items():
                    output={}
                    if 'name' in d and 'average_cost_for_two' in d \
                        and 'user_rating' in d and 'location' in d:
                        n=str(d['name'].upper())
                        avg=str(d['average_cost_for_two'])
                        #print ('NAME OF THE RESTAURANT:-',n)
                        regout=re.search(r,n)
                        if regout:
                            addr=d['location']['address']
                            rating=d['user_rating']['aggregate_rating']
                            avgPrice=d['average_cost_for_two']
                            output['address']=str(addr)
                            output['rating']=str(rating)
                            output['avgPrice2']=avgPrice
                            output['Name']=n
                            print ('FOUND YOUR RESTAURANT, DETAILS ARE AS FOLLOWS:-\n',)
                            print ('*' * 60)
                            print ('NAME OF THE RESTAURANT:-',n)
                            print ('AVERAGE COST FOR TWO:-',avgPrice)
                            print ('RATING:-',str(rating))
                            print ('ADDRESS:-',str(addr))
                            print ('*' * 60)
                            finalOut[cnt]=output
                            cnt+=1
                            flag=True

        if flag==False:
            print ('RESTAURANT DETAILS NOT FOUND... PLEASE ENTER THE CORRECT RESTAURANT NAME\n')
        else:
            #print ('IN ZOMATO_SCRIPT, THE DICTIONARY RETURNED:-',finalOut)
            return finalOut

    f.close()

'''
mykey='7dcf7b79d4c7bdfd5ffe013ae7361388'
p=Pyzomato(mykey)

print ('ZOMATO API OBJECT CREATED:-',p)
#c=raw_input('PLEASE ENTER THE CITY TO WHICH YOUR RESTAURANT BELONGS:-\n\n')
#r=raw_input('PLEASE ENTER THE NAME OF THE RESTAURANT WHICH YOU WANT TO LOOK FOR:-\n\n')
c='bangalore'
r="Ebony"
try:
   details=p.search(q=r,city=c,count=10)
   print ('\n\n THE DETAILS OF THE RESTAURANT ARE AS FOLLOWS:-',details)
   searchRestaurant(details,r.upper())
except Exception as exc:
    print ('INVALID DETAILS ENTERED:-',exc)
    print ('TRACEBACK :-',traceback.format_exc())
'''
