
from pyzomato import Pyzomato
import traceback
import re
import inspect
import pprint

def searchRestaurant(details,r):
    print ('\n\n')
    #print ('INSIDE FUNCTION:=',inspect.stack()[0][3])
    f=open('zomato_rest_output.txt','w')
    finalOut={}
    #print ('RESTAURANT ENTERED:-',r)
    if 'restaurants' in details.keys():
        #f.write('DETAILS.KEYS:_-'+str(details.keys()))
        lstRes=details['restaurants'] # LSTRES IS LIST OF DICTIONARIES.[{},{},{},..]
        #f.write('len of lstRes:-'+str(len(lstRes)))
        #f.write('listOf Restaurants:-'+str(type(lstRes)))
        #f.write('*' * 60)
        #f.write('\n\n')
        for i in range(len(lstRes)):
            #f.write('FOR INDEX OF LSTRES:-'+str(i)+':'+str(lstRes[i])+'\n') # CORRECT
            #f.write(str(lstRes[i]+'\n'))

            if 'restaurant' in lstRes[i].keys():
                d=lstRes[i]['restaurant']
                
                #f.write('*' * 60+'\n')
                #f.write('keys is:-'+ '\n')
                #f.write('DICT d AT INDEX:-'+ str(i) + ':::' +str(d)) # CORRECT
                #f.write('*' * 60)
                #f.write('values is:-'+ '\n')
                #f.write(str(d.values()))
                #f.write('\n\n')
                #f.write(str(len(d.keys())))
            # CORRECT TILL BELOW CODE
            '''
            for k,v in d.items():

                #f.write('ENTERING D.ITEM LOOP'+'\n')
                #f.write('FOR K:-'+str(k) +';;;;'+str(v)+'\n')
                if 'name' in d and 'average_cost_for_two' in d \
                        and 'user_rating' in d and 'location' in d and 'url' in d:
                    f.write('&&&&&&&&&&&&&&&&&&&&FINAL OUTPUT&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n')
                    f.write('d[url] :-'+ str(d['url'])+'\n')
                    f.write('d[name] :-'+ str(d['name'])+'\n')
                    f.write('d[location] :-'+ str(d['location'])+'\n')
                    f.write('d[rating] :-'+ str(d['user_rating'])+'\n')
                    f.write('d[avgPrice2] :-'+ str(d['average_cost_for_two'])+'\n')
                    break

                f.write('\n\n')
            '''

            flag=False
            cnt=1

            # CORRECT BELOW LOOP ALSO.
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
                        print ('*' * 60+'\n')
                        f.write ('NAME OF THE RESTAURANT:-'+n+'\n')
                        f.write ('AVERAGE COST FOR TWO:-'+ str(avgPrice)+'\n')
                        f.write ('RATING:-'+str(rating)+'\n')
                        f.write ('ADDRESS:-'+str(addr)+'\n')
                        f.write ('*' * 60+'\n')
                        finalOut[cnt]=output
                        cnt+=1
                        flag=True
                        break

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
r="Marriott"
try:
   details=p.search(q=r,city=c,count=10)
   print ('\n\n THE DETAILS OF THE RESTAURANT ARE AS FOLLOWS:-',details)
   searchRestaurant(details,r.upper())
except Exception as exc:
    print ('INVALID DETAILS ENTERED:-',exc)
    print ('TRACEBACK :-',traceback.format_exc())
'''


