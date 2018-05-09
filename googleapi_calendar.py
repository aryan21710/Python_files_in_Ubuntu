#!/usr/bin/python


from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
'''
from oauth2client.contrib.appengine import OAuth2Decorator

decorator = OAuth2Decorator(
  client_id='677710929975-ceh3jjdvfi1q9tvihv2unqvb3thdc9fp.apps.googleusercontent.com',
  client_secret='lTJXjodSGOC0IbfLeAgyPwef',
  scope='https://www.googleapis.com/auth/calendar')


class MainHandler(webapp.RequestHandler):
    @decorator.oauth_required
    def get(self):
        http = decorator.http()
        # http is authorized with the user's Credentials and can be
'''
flow = flow_from_clientsecrets('/home/ary/BKP/python_scripts/ubuntu_scripts/client_id.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='["urn:ietf:wg:oauth:2.0:oob","http://localhost"]')

service=build('calendar','v3')
print ('SERVICE OBJECT:_',service)

clist=service.calendarList().list(maxResults=5)
response=clist.execute()
print (type(response) ,'\n \n', response)
