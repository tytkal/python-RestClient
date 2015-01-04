'''
RestClient is an open source script that depends on requests library 
it was developed in 2012 and updated in 2014 by @Khalid Al-hussayen 
the script was used for my owen projects so it is limited to my use any one is welcome to update and fix the script.
'''
__author__ = 'khalid'
import urllib2 , hmac , base64
from hashlib import sha1
import hmac , requests
import json
'''
RestClient class is the only class :) it have the four popular http methods (GET,POST,PUT,DELETE) ,
to use the RestClient you need to declare object from it inilize the host with the base url and resource with your url resource , 
Then you can call any methods get or post etc.. the http responce will be hold in the reponce object 
call responce.json() if you want the data parce to json or responce.text for the plain data and res.responce.status_code.
responce is an requests responce object for more information you can see this url http://docs.python-requests.org/en/latest/user/quickstart/#response-content
'''
class RestClient:
    User_Agent = 'ubuntu'
    host = ''
    Content_Type = 'Aplication/json'
    resourse = ''
    Date = ''
    headers = {}
    data = []
    status_code = ''
    url = ''
    text = ''
    responce = None
    username = ''
    password = ''

    def put_header(self,key,value):
        self.headers[key]=value


    def get(self,append_url='',params={},is_auth=False):
	if is_auth:
        	self.responce = requests.get(self.host+self.resourse+append_url,headers=self.headers,params=params,auth=(self.username,self.password))
	else:
        	self.responce = requests.get(self.host+self.resourse+append_url,headers=self.headers,params=params)

    def post(self,params={},append_url='',is_auth=False):
	if is_auth:
        	self.responce = requests.post(self.host+self.resourse+append_url,data=params,headers=self.headers,auth=(self.username,self.password))
	else:
        	self.responce = requests.post(self.host+self.resourse+append_url,data=params,headers=self.headers)


    def put(self,params={},append_url='',is_auth=False):
	if is_auth:
        	self.responce = requests.put(self.host+self.resourse+append_url,data=params,headers=self.headers,auth=(self.username,self.password))
	else:
        	self.responce = requests.put(self.host+self.resourse+append_url,data=params,headers=self.headers)



    def delete(self,append_url='',params={},is_auth=False):
	if is_auth:
        	self.responce = requests.delete(self.host+self.resourse+append_url,params=params,headers=self.headers,auth=(self.username,self.password))
	else:
        	self.responce = requests.delete(self.host+self.resourse+append_url,params=params,headers=self.headers)

